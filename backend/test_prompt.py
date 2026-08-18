import sys

if "pytest" in sys.modules:
    import pytest
    pytest.skip("Manual prompt preview script; run it directly, not through pytest.", allow_module_level=True)

from services.prompt import PromptBuilder


builder = PromptBuilder()


character = {
    "name":"绫波丽",
    "age":17
}


personality={
    "temperament":"冷静",
    "worldview":"..."
}


prompt = builder.build(
    character,
    personality,
    {
        "short": [],
        "long": []
    },
    {},
    [],
    "你好"
)


print(prompt)
