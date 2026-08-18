import sys

if "pytest" in sys.modules:
    import pytest
    pytest.skip("Manual memory learning script; run it directly, not through pytest.", allow_module_level=True)

from services.memory.short_memory import ShortMemory
from services.memory.long_memory import LongMemory
from services.memory.user_profile import UserProfile



print("======测试短期记忆======")

short_memory = ShortMemory()


short_memory.add(
    "user",
    "你好，我叫小明"
)


short_memory.add(
    "assistant",
    "你好小明，我是星野"
)


print(
    short_memory.get_history()
)



print("\n======测试长期记忆======")

long_memory = LongMemory()


long_memory.add(
    "用户喜欢猫"
)


print(
    long_memory.search()
)



print("\n======测试用户资料======")

profile = UserProfile()


profile.set(
    "name",
    "小明"
)


profile.set(
    "favorite",
    "猫"
)


print(
    profile.get()
)
