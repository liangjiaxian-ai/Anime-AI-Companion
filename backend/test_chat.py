from services.chat import ChatService

from services.character import CharacterService

from services.personality import PersonalityService

from services.memory import MemoryService

from core.llm_client import LLMClient



character_service = CharacterService()

personality_service = PersonalityService()

memory_service = MemoryService()

llm_client = LLMClient()



chat_service = ChatService(
    character_service,
    personality_service,
    memory_service,
    llm_client
)



result = chat_service.chat(
    "今天有点累"
)


print(result)