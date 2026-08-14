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