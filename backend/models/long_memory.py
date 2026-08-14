from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class LongMemoryModel(Base):

    __tablename__ = "long_memories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    role: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )