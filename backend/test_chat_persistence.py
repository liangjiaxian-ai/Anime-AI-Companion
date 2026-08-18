from database.database import SessionLocal
from models.long_memory import LongMemoryModel
from models.message import Message
from models.user import User
from services.character import CharacterService
from services.chat import ChatService
from services.memory_service import MemoryService
from services.personality import PersonalityService
from services.prompt import PromptBuilder


class FakeLLMClient:
    def chat(self, system_prompt, user_message):
        assert "当前用户消息" in system_prompt
        return "我会记住这件事的。"


def _make_chat_service():
    return ChatService(
        CharacterService(),
        PersonalityService(),
        MemoryService(),
        PromptBuilder(),
        FakeLLMClient(),
    )


def test_chat_persists_and_isolates_a_users_memory():
    user_id = 987_654
    session = SessionLocal()
    try:
        session.query(Message).filter_by(user_id=user_id).delete()
        session.query(LongMemoryModel).filter_by(user_id=user_id).delete()
        existing_user = session.get(User, user_id)
        if existing_user:
            session.delete(existing_user)
        session.commit()

        reply = _make_chat_service().chat(user_id, "我叫测试同学，我喜欢猫")
        reloaded_memory = MemoryService().for_user(user_id)

        assert reply == "我会记住这件事的。"
        assert reloaded_memory.user_profile.get()["name"] == "测试同学"
        assert reloaded_memory.user_profile.get()["like"] == "猫"
        assert [item["role"] for item in reloaded_memory.get_history()] == ["user", "assistant"]
        assert reloaded_memory.long_memory.search("喜欢猫")[0]["content"] == "我叫测试同学，我喜欢猫"
    finally:
        session.query(Message).filter_by(user_id=user_id).delete()
        session.query(LongMemoryModel).filter_by(user_id=user_id).delete()
        user = session.get(User, user_id)
        if user:
            session.delete(user)
        session.commit()
        session.close()
