from fastapi import APIRouter

from app.models.schemas import SearchRequest
from app.services.openclaw_bridge import execute_personal_travel_agent
from app.services.search_service import build_search_response

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/search")
async def search_flights(payload: SearchRequest):
    return build_search_response(payload.model_dump())


@router.post("/agent/personal-travel/execute")
async def run_openclaw_agent(payload: dict):
    return execute_personal_travel_agent(payload)


@router.get("/agent/personal-travel/profile")
async def get_openclaw_profile():
    return {
        "agent": "personal-travel",
        "role": "travel-agent",
        "permissions": [
            "search_flights",
            "get_search_status",
            "send_message",
        ],
        "status": "ready",
    }
