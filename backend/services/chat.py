class ChatService:


    def __init__(
        self,
        character_service,
        personality_service,
        memory_service,
        llm_client
    ):

        # 保存角色服务
        self.character_service = character_service

        # 保存人格服务
        self.personality_service = personality_service

        # 保存记忆服务
        self.memory_service = memory_service

        # 保存AI服务
        self.llm_client = llm_client



    def chat(self,user_message):

        # 获取角色信息
        character = self.character_service.get_character()


        # 获取人格信息
        personality = self.personality_service.get_personality()


        # 获取历史记忆
        memory = self.memory_service.search()


        # 生成Prompt
        prompt = f"""
        你现在扮演:
        {character}

        性格:
        {personality}

        历史:
        {memory}


        用户:
        {user_message}
        """


        # 调用AI
        response = self.llm_client.chat(prompt)


        # 保存回复
        self.memory_service.save(user_message,response)


        return response