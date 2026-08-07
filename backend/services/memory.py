class MemoryService:
    """
    记忆服务

    负责：
    1.保存聊天记录
    2.查询历史记录
    """


    def __init__(self):

        # 保存记忆列表
        self.memory = []


    def save(self, user_message, ai_response):

        # 创建一条聊天记录

        message = {

            "user": user_message,

            "assistant": ai_response
        }


        # append:
        # 列表添加元素

        self.memory.append(message)



    def search(self):

        # 返回最近5条记录

        return self.memory[-5:]