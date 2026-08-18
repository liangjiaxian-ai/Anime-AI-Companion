import re


class MemoryExtractor:


    def extract(self, message):

        profile = {}

        long_memory = []


        # 名字
        if "我叫" in message:

            name = message.split("我叫")[1]

            name = name.split("，")[0]
            name = name.split("。")[0]
            name = name.split(" ")[0]

            if name:
                profile["name"] = name


        # 喜好

        if "我喜欢" in message:

            thing = message.split("我喜欢", 1)[1]
            thing = re.split(r"[，。！？!?\n]", thing, maxsplit=1)[0]

            if thing.strip():
                profile["like"] = thing.strip("，。！! ")


        # 长期记忆

        if len(message) > 3:

            long_memory.append({"role": "user", "content": message.strip()})


        return {

            "profile": profile,

            "long": long_memory

        }
