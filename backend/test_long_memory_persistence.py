import pytest

from database.database import SessionLocal
from models.long_memory import LongMemoryModel
from services.memory.long_memory import LongMemory


@pytest.fixture
def memory():
    return LongMemory()

@pytest.fixture(autouse=True)
def clean_long_memory():
    db = SessionLocal()
    try:
        db.query(LongMemoryModel).delete()
        db.commit()
    finally:
        db.close()


def test_add_and_get_memory(memory):

    item = {
        "role": "user",
        "content": "用户喜欢猫"
    }

    memory.add(item)

    result = memory.get()

    assert len(result) == 1
    assert result[0]["content"] == "用户喜欢猫"


def test_duplicate_memory_is_not_added(memory):

    item = {
        "role": "user",
        "content": "用户喜欢猫"
    }

    memory.add(item)
    memory.add(item)

    result = memory.get()

    assert len(result) == 1


def test_search_memory(memory):

    memory.add({
        "role": "user",
        "content": "用户喜欢猫"
    })

    memory.add({
        "role": "user",
        "content": "用户喜欢看动漫"
    })

    result = memory.search("猫")

    assert len(result) == 1
    assert result[0]["content"] == "用户喜欢猫"


def test_memory_can_be_loaded_again():

    memory1 = LongMemory()

    memory1.add({
        "role": "user",
        "content": "用户喜欢猫"
    })

    # 模拟程序重新启动
    memory2 = LongMemory()

    result = memory2.search("猫")

    assert len(result) == 1
    assert result[0]["content"] == "用户喜欢猫"