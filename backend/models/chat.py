from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """A message sent by one application user."""

    user_id: int = Field(default=1, ge=1, description="Application user identifier")
    message: str = Field(min_length=1, max_length=2_000, description="User message")


class ChatResponse(BaseModel):
    user_id: int
    user: str
    character: str
    reply: str
