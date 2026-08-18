import sys

if "pytest" in sys.modules:
    import pytest
    pytest.skip("Manual provider smoke script; run it directly, not through pytest.", allow_module_level=True)

from core.llm_client import LLMClient


client = LLMClient()


result = client.chat(
    """
    你是Anime-AI-Companion中的AI陪伴角色。
    你的名字叫星野。
    你性格温柔，喜欢陪伴用户。
    """,

    "你是谁？"
)


print(result)
