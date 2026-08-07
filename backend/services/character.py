import json
from pathlib import Path


# 角色文件位置
CHARACTER_FILE = Path("../prompts/character.json")


class CharacterService:
    """
    角色服务

    负责：
    1.读取角色文件
    2.返回角色信息
    """


    def __init__(self):

        # 保存角色文件路径
        self.character_file = CHARACTER_FILE



    def load_character(self):

        """
        读取json文件
        """

        with open(
            self.character_file,
            "r",
            encoding="utf-8"
        ) as f:

            # json.load:
            # 把json文件转换成Python字典
            return json.load(f)



    def get_character(self):

        """
        给其他Service调用的方法
        """

        return self.load_character()