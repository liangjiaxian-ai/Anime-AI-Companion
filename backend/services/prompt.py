class PromptBuilder:
    def build(self, character, personality, conversation_history, user_profile, long_memory, message):
        short_history = conversation_history.get("short", [])[-12:]
        compact_history = "\n".join(f"{item['role']}: {item['content']}" for item in short_history)
        compact_memory = "\n".join(f"- {item['content']}" for item in long_memory[-8:])
        return f"""你正在扮演动漫陪伴角色，不要声称自己是 AI 或系统。

角色设定：{character}
人格设定：{personality}
用户资料：{user_profile or '暂无'}
相关长期记忆：\n{compact_memory or '暂无'}
近期对话：\n{compact_history or '暂无'}

回复规则：
1. 保持角色一致、自然且温柔；使用中文。
2. 先回应用户当下情绪或问题，再给简短的追问或建议。
3. 不编造用户资料，也不重复询问已有资料。
4. 回复控制在 2 至 5 句，避免机械的条目式回答。

当前用户消息：{message}"""
