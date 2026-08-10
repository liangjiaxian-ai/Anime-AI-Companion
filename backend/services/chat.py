from models.message import Message

class ChatService:

    def __init__(
        self,
        character_service,
        personality_service,
        memory_service,
        prompt_builder,
        llm_client
    ):

        # 保存角色服务
        self.character_service = character_service

        # 保存人格服务
        self.personality_service = personality_service

        # 保存记忆服务
        self.memory_service = memory_service

        # 保存提示词服务
        self.prompt_builder = prompt_builder

        # 保存AI服务
        self.llm_client = llm_client



    def chat(self,user_message):


        character = self.character_service.get_character()


        personality = self.personality_service.get_personality()


        # 先保存用户消息
        self.memory_service.add_message(
            "user",
            user_message
        )


        # 获取历史
        short_memory = self.memory_service.get_history()

        long_memory = self.memory_service.long_memory.search()

        conversation_history = {

            "short": short_memory,

            "long": long_memory

        }



        message = Message(
            "user",
            user_message
        )


        system_prompt = self.prompt_builder.build(
            character,
            personality,
            conversation_history,
            user_message
        )


        try:

            response = self.llm_client.chat(
                system_prompt,
                message.content
            )


        except Exception as e:

            print("LLM调用失败:",e)

            return "抱歉，我刚刚走神了..."


        # 保存AI回复

        self.memory_service.add_message(
            "assistant",
            response
        )


        # 提取长期记忆

        self.memory_service.process_memory(
            user_message
        )


        return response