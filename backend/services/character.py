import json
from pathlib import Path


CHARACTER_FILE = Path("../prompts/character.json")


def load_character():

    with open(
        CHARACTER_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def get_character():

    return load_character()