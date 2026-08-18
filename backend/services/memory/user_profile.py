import json

from database.database import SessionLocal
from models.user import User


class UserProfile:
    def __init__(self, user_id=None):
        self.user_id = user_id
        self.profile = {}

    def ensure_user(self):
        """Create the lightweight local user record before messages reference it."""
        if self.user_id is None:
            return
        session = SessionLocal()
        try:
            if session.get(User, self.user_id) is None:
                session.add(User(id=self.user_id, name=f"用户 {self.user_id}"))
                session.commit()
        finally:
            session.close()

    def update(self, key, value):
        if self.user_id is None:
            self.profile[key] = value
            return

        session = SessionLocal()
        try:
            user = session.get(User, self.user_id)
            if user is None:
                user = User(id=self.user_id, name=f"用户 {self.user_id}")
                session.add(user)
                session.flush()
            profile = json.loads(user.profile_json or "{}")
            profile[key] = value
            user.profile_json = json.dumps(profile, ensure_ascii=False)
            session.commit()
        finally:
            session.close()

    def set(self, key, value):
        self.update(key, value)

    def get(self):
        if self.user_id is None:
            return dict(self.profile)

        session = SessionLocal()
        try:
            user = session.get(User, self.user_id)
            return json.loads(user.profile_json or "{}") if user else {}
        finally:
            session.close()
