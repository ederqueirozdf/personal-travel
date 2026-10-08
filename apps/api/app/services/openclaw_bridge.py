from typing import Any, Dict

from app.services.search_service import build_search_response


def execute_personal_travel_agent(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Bridge between OpenClaw agent workflow and the local travel search API."""
    normalized = {
        "origin": payload.get("origin", "GRU"),
        "destination": payload.get("destination", "LIS"),
        "departure_date": payload.get("departure_date"),
        "return_date": payload.get("return_date"),
        "window_days": int(payload.get("window_days", 5)),
        "max_stops": int(payload.get("max_stops", 1)),
        "baggage_required": bool(payload.get("baggage_required", False)),
        "search_mode": payload.get("search_mode", "mixed"),
    }

    result = build_search_response(normalized)
    result["agent"] = "personal-travel"
    result["source"] = "openclaw"
    return result
