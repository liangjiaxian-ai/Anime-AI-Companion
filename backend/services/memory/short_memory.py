from database.database import SessionLocal
from models.message import Message


class ShortMemory:
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.history = []

    def add(self, role, content):
        if self.user_id is None:
            self.history.append({"role": role, "content": content})
            return

        session = SessionLocal()
        try:
            session.add(Message(user_id=self.user_id, role=role, content=content))
            session.commit()
        finally:
            session.close()

    def get_history(self):
        if self.user_id is None:
            return self.history[-20:]

        session = SessionLocal()
        try:
            messages = (session.query(Message).filter_by(user_id=self.user_id)
                        .order_by(Message.id.desc()).limit(20).all())
            return [{"role": message.role, "content": message.content} for message in reversed(messages)]
        finally:
            session.close()
