from fastapi import APIRouter

from app.models.schemas import SearchRequest
from app.services.search_service import build_search_response

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/search")
async def search_flights(payload: SearchRequest):
    return build_search_response(payload.model_dump())
