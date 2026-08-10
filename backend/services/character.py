import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

CHARACTER_FILE = BASE_DIR / "prompts" / "character.json"


class CharacterService:

    def __init__(self):
        self.character_file = CHARACTER_FILE


    def load_character(self):

        with open(
            self.character_file,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)


    def get_character(self):

        return self.load_character()