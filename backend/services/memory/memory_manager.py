from services.memory.short_memory import ShortMemory
from services.memory.long_memory import LongMemory
from services.memory.user_profile import UserProfile


class MemoryManager:

    def __init__(self):

        self.short_memory = ShortMemory()

        self.long_memory = LongMemory()

        self.user_profile = UserProfile()


    # =========================
    # 短期记忆
    # =========================

    def add_message(
        self,
        role,
        content
    ):

        self.short_memory.add(
            role,
            content
        )


    def get_history(self):

        return self.short_memory.get_history()


    # =========================
    # 长期记忆
    # =========================

    def add_long_memory(
        self,
        memory
    ):

        self.long_memory.add(
            memory
        )


    def search_memory(
        self,
        keyword=None
    ):

        return self.long_memory.search(
            keyword
        )


    # =========================
    # 用户资料
    # =========================

    def update_profile(
        self,
        key,
        value
    ):

        self.user_profile.update(
            key,
            value
        )


    def get_profile(self):

        return self.user_profile.get()