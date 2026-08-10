class UserProfile:


    def __init__(self):

        self.profile = {}


    def update(
        self,
        key,
        value
    ):

        self.profile[key] = value



    def get(self):

        return self.profile