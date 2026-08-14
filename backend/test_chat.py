from services.character import CharacterService
from services.personality import PersonalityService
from services.memory_service import MemoryService
from services.prompt import PromptBuilder
from services.chat import ChatService
from core.llm_client import LLMClient
from database.database import SessionLocal



character_service = CharacterService()

personality_service = PersonalityService()

memory_service = MemoryService()

prompt_builder = PromptBuilder()

llm_client = LLMClient()

db = SessionLocal()


chat_service = ChatService(
    db,
    character_service,
    personality_service,
    memory_service,
    prompt_builder,
    llm_client
)



result = chat_service.chat(
    1,
    "今天有点累"
)


print(result)