from fastapi import APIRouter
from services.character import get_character


router = APIRouter(
    prefix="/character",
    tags=["Character"]
)


@router.get("/")
def character_info():
    return get_character()