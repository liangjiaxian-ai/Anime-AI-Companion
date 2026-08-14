from models.message import Message

class ChatService:

    def __init__(
        self,
        db,
        character_service,
        personality_service,
        memory_service,
        prompt_builder,
        llm_client
    ):
        self.db = db

        self.character_service = character_service
        self.personality_service = personality_service
        self.memory_service = memory_service
        self.prompt_builder = prompt_builder
        self.llm_client = llm_client



    def chat(self, user_id, user_message):


        character = self.character_service.get_character()


        personality = self.personality_service.get_personality()


        # 获取历史
        short_memory = self.memory_service.get_history()

        long_memory = self.memory_service.long_memory.search()

        conversation_history = {

            "short": short_memory,

            "long": long_memory

        }



       # 创建用户消息

        message = Message(
            role="user",
            content=user_message,
            user_id=user_id
        )


        # 保存用户消息

        self.db.add(message)
        self.db.commit()



        # 创建prompt

        system_prompt = self.prompt_builder.build(
            character,
            personality,
            conversation_history,
            self.memory_service.user_profile.get(),
            long_memory,
            user_message
        )



        # 调用LLM

        try:

            response = self.llm_client.chat(
                system_prompt,
                user_message
            )


        except Exception as e:

            print("LLM调用失败:",e)

            response = "抱歉，我暂时无法回答。"



        # 保存AI回复

        assistant_message = Message(
            role="assistant",
            content=response,
            user_id=user_id
        )


        self.db.add(assistant_message)
        self.db.commit()



        # 提取长期记忆

        self.memory_service.process_memory(
            user_message
        )



        return response