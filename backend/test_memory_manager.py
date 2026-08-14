import pytest

from database.database import SessionLocal
from models.long_memory import LongMemoryModel
from services.memory.memory_manager import MemoryManager


@pytest.fixture
def memory_manager():
    return MemoryManager()

@pytest.fixture(autouse=True)
def clean_long_memory():
    db = SessionLocal()

    try:
        db.query(LongMemoryModel).delete()
        db.commit()
    finally:
        db.close()


def test_initial_state(memory_manager):
    assert memory_manager.get_history() == []
    assert memory_manager.search_memory() == []
    assert memory_manager.get_profile() == {}


def test_add_message(memory_manager):
    memory_manager.add_message(
        "user",
        "你好，我叫小明"
    )

    history = memory_manager.get_history()

    assert len(history) == 1
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "你好，我叫小明"


def test_add_multiple_messages(memory_manager):
    memory_manager.add_message(
        "user",
        "你好"
    )

    memory_manager.add_message(
        "assistant",
        "你好，小明"
    )

    history = memory_manager.get_history()

    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[1]["role"] == "assistant"


def test_add_long_memory(memory_manager):
    memory = {
        "content": "用户喜欢猫",
        "role": "user"
    }

    memory_manager.add_long_memory(memory)

    memories = memory_manager.search_memory()

    assert len(memories) == 1
    assert memories[0] == memory


def test_search_long_memory(memory_manager):
    memory_manager.add_long_memory({
        "content": "用户喜欢猫",
        "role": "user"
    })

    memory_manager.add_long_memory({
        "content": "用户喜欢看动漫",
        "role": "user"
    })

    result = memory_manager.search_memory("猫")

    assert len(result) == 1
    assert result[0]["content"] == "用户喜欢猫"


def test_update_profile(memory_manager):
    memory_manager.update_profile(
        "name",
        "小明"
    )

    profile = memory_manager.get_profile()

    assert profile["name"] == "小明"


def test_update_multiple_profile_fields(memory_manager):
    memory_manager.update_profile(
        "name",
        "小明"
    )

    memory_manager.update_profile(
        "favorite",
        "猫"
    )

    profile = memory_manager.get_profile()

    assert profile["name"] == "小明"
    assert profile["favorite"] == "猫"