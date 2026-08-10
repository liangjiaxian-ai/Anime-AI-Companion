from services.chat import ChatService

from services.character import CharacterService
from services.personality import PersonalityService
from services.memory_service import MemoryService
from services.prompt import PromptBuilder

from core.llm_client import LLMClient



# 创建依赖

character_service = CharacterService()

personality_service = PersonalityService()

memory_service = MemoryService()

prompt_builder = PromptBuilder()

llm_client = LLMClient()



# 创建聊天服务

chat_service = ChatService(
    character_service,
    personality_service,
    memory_service,
    prompt_builder,
    llm_client
)



# 模拟用户输入

response1 = chat_service.chat(
    "我叫小明"
)


print(
    "第一次:",
    response1
)



response2 = chat_service.chat(
    "我喜欢猫"
)


print(
    "第二次:",
    response2
)


print(
    memory_service.user_profile.get()
)

print(
    memory_service.long_memory.search()
)