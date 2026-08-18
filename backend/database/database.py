from pathlib import Path

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import declarative_base, sessionmaker


# 项目根目录
BASE_DIR = Path(__file__).resolve().parents[2]

# 项目根目录/data/memory.db
DATABASE_PATH = BASE_DIR / "data" / "memory.db"

# 确保 data 目录存在
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"


engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


def _upgrade_existing_sqlite_schema():
    """Keep direct scripts and the web app compatible with the original DB."""
    inspector = inspect(engine)
    table_names = set(inspector.get_table_names())

    with engine.begin() as connection:
        if "users" in table_names:
            user_columns = {column["name"] for column in inspector.get_columns("users")}
            if "profile_json" not in user_columns:
                connection.execute(text("ALTER TABLE users ADD COLUMN profile_json TEXT NOT NULL DEFAULT '{}'"))
        if "long_memories" in table_names:
            memory_columns = {column["name"] for column in inspector.get_columns("long_memories")}
            if "user_id" not in memory_columns:
                connection.execute(text("ALTER TABLE long_memories ADD COLUMN user_id INTEGER"))


_upgrade_existing_sqlite_schema()


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()
