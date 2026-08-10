from services.memory_service import MemoryService


memory = MemoryService()


memory.add_message(
    "user",
    "你好，我叫小明"
)


memory.update_profile(
    "name",
    "小明"
)


memory.add_long_memory(
    "用户喜欢猫"
)


print(
    memory.get_history()
)


print(
    memory.user_profile.get()
)


print(
    memory.long_memory.search()
)