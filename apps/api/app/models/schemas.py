from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    origin: str = Field(..., min_length=2, max_length=120)
    destination: str = Field(..., min_length=2, max_length=120)
    departure_date: date
    return_date: Optional[date] = None
    window_days: int = Field(default=5, ge=0, le=30)
    max_stops: int = Field(default=1, ge=0, le=3)
    baggage_required: bool = False
    search_mode: str = Field(default="money", pattern="^(money|miles|mixed)$")
    budget_limit: Optional[float] = None
    preferred_program: Optional[str] = None


class OfferResult(BaseModel):
    airline: str
    source: str
    price_total: float
    stops: int
    duration_hours: float
    baggage_included: bool
    score: float
    notes: str
