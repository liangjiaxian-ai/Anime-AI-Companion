class ChatMessage:
    """
    聊天消息对象

    用来保存：
    1. 谁说的话
    2. 说了什么
    """

    def __init__(self, role, content):
        """
        初始化聊天消息

        role:
            角色身份
            user / assistant

        content:
            消息内容
        """

        self.role = role

        self.content = content