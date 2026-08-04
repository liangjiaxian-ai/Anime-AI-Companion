
from fastapi import FastAPI

from api.chat import router as chat_router
from api.character import router as character_router


app = FastAPI(
    title="Anime AI Companion",
    description="AI companion backend",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Anime AI Companion Backend Running"
    }


@app.get("/status")
def status():
    return {
        "project": "Anime AI Companion",
        "status": "running",
        "version": "0.1.0"
    }


app.include_router(chat_router)
app.include_router(character_router)