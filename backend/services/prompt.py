class PromptBuilder:

    def build(
        self,
        character,
        personality,
        conversation_history,
        message
    ):

        prompt = f"""
你现在扮演:

{character}


性格:

{personality}


历史:

{conversation_history}


用户:

{message}
"""

        return prompt