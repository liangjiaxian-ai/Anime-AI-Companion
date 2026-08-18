
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from api.chat import router as chat_router
from api.character import router as character_router


PROJECT_DIR = Path(__file__).resolve().parents[1]
FRONTEND_DIR = PROJECT_DIR / "frontend"


@asynccontextmanager
async def lifespan(_: FastAPI):
    from database.init_db import init_db
    init_db()
    yield


app = FastAPI(
    title="Anime AI Companion",
    description="AI companion backend",
    version="1.0.0",
    lifespan=lifespan
)


if FRONTEND_DIR.exists():
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIR), name="assets")


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/status")
def status():
    return {
        "project": "Anime AI Companion",
        "status": "running",
        "version": "1.0.0"
    }


app.include_router(chat_router)
app.include_router(character_router)
