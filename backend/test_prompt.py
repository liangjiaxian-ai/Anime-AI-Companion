from services.prompt import PromptBuilder


builder = PromptBuilder()


prompt = builder.build(
    "星野",
    "温柔，活泼",
    "用户昨天考试失败",
    "今天很累"
)


print(prompt)