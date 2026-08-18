from fastapi import APIRouter, Depends

from core.dependency import get_character_service
from typing import Dict, Any

router = APIRouter(
    prefix="/character",
    tags=["Character"]
)


@router.get("/")
def character(
    character_service = Depends(get_character_service)
) -> Dict[str, Any]:

    return character_service.get_character()