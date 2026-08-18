from sqlalchemy import inspect, text

from database.database import Base, engine
# Import every model before create_all so SQLAlchemy registers their tables.
from models.long_memory import LongMemoryModel  # noqa: F401
from models.message import Message  # noqa: F401
from models.user import User  # noqa: F401


def init_db():
    """Create tables and apply the two safe SQLite upgrades used by this MVP."""
    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    user_columns = {column["name"] for column in inspector.get_columns("users")}
    memory_columns = {column["name"] for column in inspector.get_columns("long_memories")}

    with engine.begin() as connection:
        if "profile_json" not in user_columns:
            connection.execute(text("ALTER TABLE users ADD COLUMN profile_json TEXT NOT NULL DEFAULT '{}'"))
        if "user_id" not in memory_columns:
            connection.execute(text("ALTER TABLE long_memories ADD COLUMN user_id INTEGER"))


if __name__ == "__main__":

    init_db()
