from fastapi import APIRouter
from models.chat import ChatRequest
from services.character import load_character
from services.personality import build_personality_prompt
from core.ai import chat_with_ai

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
def chat(request: ChatRequest):

    character = load_character()

    personality = build_personality_prompt()

    reply = chat_with_ai(
    personality,
    request.message
    )

    return {
    "user": request.message,
    "character": character["name"],
    "reply": reply
    }
