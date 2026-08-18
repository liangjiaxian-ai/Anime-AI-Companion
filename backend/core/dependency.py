from services.chat import ChatService

from services.character import CharacterService
from services.personality import PersonalityService
from services.memory_service import MemoryService

from services.prompt import PromptBuilder

from core.llm_client import LLMClient


character_service = CharacterService()


personality_service = PersonalityService()


memory_service = MemoryService()


prompt_builder = PromptBuilder()


llm_client = LLMClient()



chat_service = ChatService(
    character_service,
    personality_service,
    memory_service,
    prompt_builder,
    llm_client
)



def get_chat_service():

    return chat_service



def get_character_service():

    return character_service