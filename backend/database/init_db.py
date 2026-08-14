from database.database import Base, engine
from models.long_memory import LongMemoryModel
from database.database import SessionLocal


character_service = CharacterService()

personality_service = PersonalityService()

memory_service = MemoryService()

prompt_builder = PromptBuilder()

llm_client = LLMClient()


db = SessionLocal()


def init_db():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":

    init_db()