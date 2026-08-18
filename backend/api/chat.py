from fastapi import APIRouter, Depends, HTTPException, status

from core.dependency import get_chat_service
from core.llm_client import LLMClientError
from models.chat import ChatRequest, ChatResponse


router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest, chat_service=Depends(get_chat_service)):
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="message cannot be blank")

    try:
        reply = chat_service.chat(user_id=request.user_id, user_message=message)
    except LLMClientError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc

    return {
        "user_id": request.user_id,
        "user": message,
        "character": chat_service.character_service.get_character()["name"],
        "reply": reply,
    }
