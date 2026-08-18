from services.memory.short_memory import ShortMemory
from services.memory.long_memory import LongMemory
from services.memory.user_profile import UserProfile
from services.memory.memory_extractor import MemoryExtractor


class MemoryService:


    def __init__(self, user_id=None):

        self.user_id = user_id
        self.short_memory = ShortMemory(user_id)

        self.long_memory = LongMemory(user_id)

        self.user_profile = UserProfile(user_id)

        self.extractor = MemoryExtractor()


    def for_user(self, user_id):
        """Create a user-scoped facade while retaining legacy test support."""
        return MemoryService(user_id)


    def ensure_user(self):
        self.user_profile.ensure_user()



    def add_message(
        self,
        role,
        content
    ):

        # 保存短期记忆
        self.short_memory.add(
            role,
            content
        )


        # 只处理用户消息
        if role == "user":

            self.process_memory(content)



    def get_history(self):

        return self.short_memory.get_history()



    def add_long_memory(
        self,
        memory
    ):

        self.long_memory.add(memory)



    def update_profile(
        self,
        key,
        value
    ):

        self.user_profile.update(
            key,
            value
        )


    def process_memory(
            self,
            message
    ):

        result = self.extractor.extract(
            message
        )


        # 用户资料

        for key,value in result["profile"].items():

            self.user_profile.update(
                key,
                value
            )


        # 长期记忆

        for item in result["long"]:

            self.long_memory.add(
                item
            )
