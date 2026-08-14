import pytest

from services.memory_service import MemoryService


@pytest.fixture
def memory_service():
    return MemoryService()


def test_add_message(memory_service):
    memory_service.add_message("user", "你好，我叫小明")

    history = memory_service.get_history()

    assert len(history) == 1
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "你好，我叫小明"


def test_add_message_only_user_processes_memory(memory_service):
    memory_service.add_message("assistant", "你好")

    history = memory_service.get_history()

    assert len(history) == 1
    assert history[0]["role"] == "assistant"


def test_add_long_memory(memory_service):
    memory_service.add_long_memory("用户喜欢猫")

    memories = memory_service.long_memory.get()

    assert any(
        item["content"] == "用户喜欢猫"
        for item in memories
    )


def test_update_profile(memory_service):
    memory_service.update_profile("name", "小明")

    profile = memory_service.user_profile.get()

    assert profile["name"] == "小明"


def test_process_memory(memory_service):
    memory_service.process_memory("我叫小明")

    profile = memory_service.user_profile.get()

    assert isinstance(profile, dict)