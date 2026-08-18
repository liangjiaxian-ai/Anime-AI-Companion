from fastapi.testclient import TestClient

from core.dependency import get_character_service, get_chat_service
from main import app


class FakeCharacterService:
    def get_character(self):
        return {"name": "星野"}


class FakeChatService:
    character_service = FakeCharacterService()

    def __init__(self):
        self.calls = []

    def chat(self, user_id, user_message):
        self.calls.append((user_id, user_message))
        return f"收到：{user_message}"


def test_chat_api_uses_request_user_id_and_returns_contract():
    fake_service = FakeChatService()
    app.dependency_overrides[get_chat_service] = lambda: fake_service
    app.dependency_overrides[get_character_service] = lambda: FakeCharacterService()
    try:
        with TestClient(app) as client:
            response = client.post("/chat/", json={"user_id": 42, "message": "你好"})
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == {
        "user_id": 42,
        "user": "你好",
        "character": "星野",
        "reply": "收到：你好",
    }
    assert fake_service.calls == [(42, "你好")]


def test_chat_api_rejects_blank_message():
    with TestClient(app) as client:
        response = client.post("/chat/", json={"message": "   "})
    assert response.status_code == 422


def test_homepage_serves_the_chat_interface():
    with TestClient(app) as client:
        response = client.get("/")
    assert response.status_code == 200
    assert "和星野聊聊吧" in response.text
