from database.database import SessionLocal
from models.long_memory import LongMemoryModel


class LongMemory:

    def __init__(self):
        pass


    def add(self, item):
        session = SessionLocal()

        try:
            if isinstance(item, str):
                role = "user"
                content = item
            else:
                role = item["role"]
                content = item["content"]

            # 防止重复记忆
            existing = session.query(LongMemoryModel).filter_by(
                role=role,
                content=content
            ).first()

            if existing is None:

                memory = LongMemoryModel(
                    role=role,
                    content=content
                )

                session.add(memory)

                session.commit()

        finally:

            session.close()


    def get(self):

        session = SessionLocal()

        try:

            memories = session.query(
                LongMemoryModel
            ).all()

            return [
                {
                    "role": memory.role,
                    "content": memory.content
                }
                for memory in memories
            ]

        finally:

            session.close()


    def search(self, keyword=None):

        session = SessionLocal()

        try:

            memories = session.query(
                LongMemoryModel
            ).all()

            if keyword is None:

                return [
                    {
                        "role": memory.role,
                        "content": memory.content
                    }
                    for memory in memories
                ]


            result = []

            for memory in memories:

                if keyword in memory.content:

                    result.append({
                        "role": memory.role,
                        "content": memory.content
                    })

            return result

        finally:

            session.close()