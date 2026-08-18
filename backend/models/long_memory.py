from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class LongMemoryModel(Base):

    __tablename__ = "long_memories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
        index=True
    )

    role: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        String(1000),
        nullable=False
    )
