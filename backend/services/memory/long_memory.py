class LongMemory:

    def __init__(self):
        self.memory=[]


    def add(self,item):

        if item not in self.memory:
            self.memory.append(item)


    def search(self, keyword=None):

        if keyword is None:
            return self.memory

        result=[]

        for item in self.memory:
            if keyword in item["content"]:
                result.append(item)

        return result