from core.llm_client import LLMClientError


class ChatService:
    def __init__(self, character_service, personality_service, memory_service, prompt_builder, llm_client):
        self.character_service = character_service
        self.personality_service = personality_service
        self.memory_service = memory_service
        self.prompt_builder = prompt_builder
        self.llm_client = llm_client

    def chat(self, user_id, user_message):
        memory_service = self.memory_service.for_user(user_id)
        memory_service.ensure_user()
        character = self.character_service.get_character()
        personality = self.personality_service.get_personality()

        history = memory_service.get_history()
        long_memory = memory_service.long_memory.search(user_message)
        conversation_history = {"short": history, "long": long_memory}

        # Persist and extract user details before generating the reply.
        memory_service.add_message("user", user_message)
        prompt = self.prompt_builder.build(
            character,
            personality,
            conversation_history,
            memory_service.user_profile.get(),
            long_memory,
            user_message,
        )

        try:
            response = self.llm_client.chat(prompt, user_message)
        except LLMClientError:
            raise

        memory_service.add_message("assistant", response)
        return response
