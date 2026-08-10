class MemoryExtractor:


    def extract(self,message):

        profile = {}

        long_memory = []


        # 名字
        if "我叫" in message:

            name = message.split("我叫")[1]

            name = name.split("，")[0]
            name = name.split("。")[0]
            name = name.split(" ")[0]

            profile["name"] = name


        # 喜好

        if "我喜欢" in message:

            thing = message.replace(
                "我喜欢",
                ""
            )

            profile["like"] = thing


        # 长期记忆

        if len(message) > 3:

            long_memory.append(
                message
            )


        return {

            "profile": profile,

            "long": long_memory

        }