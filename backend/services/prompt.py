class PromptBuilder:

    def build(
        self,
        character,
        personality,
        conversation_history,
        user_profile,
        long_memory,
        message
    ):

        prompt = f"""
        
角色设定：

{character}


性格:

{personality}


历史:

{conversation_history}


用户信息:

{user_profile}


相关记忆:

{long_memory}


# 回复规则

1. 保持角色一致
2. 参考用户信息
3. 不重复询问已知信息
4. 表现自然情绪

用户:

{message}
"""

        return prompt