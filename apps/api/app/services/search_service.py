from datetime import date, timedelta
from typing import Any, Dict, List

from app.services.ranking import rank_offers


def _date_shift(base_date: date, days: int) -> str:
    return (base_date + timedelta(days=days)).isoformat()


def build_search_response(payload: Dict[str, Any]) -> Dict[str, Any]:
    origin = payload.get("origin", "GRU")
    destination = payload.get("destination", "LIS")
    departure_date = payload.get("departure_date")
    if isinstance(departure_date, str):
        departure_date = date.fromisoformat(departure_date)

    return_date = payload.get("return_date")
    if isinstance(return_date, str):
        return_date = date.fromisoformat(return_date)
    if return_date is None:
        return_date = departure_date + timedelta(days=8)

    window_days = int(payload.get("window_days", 5))
    max_stops = int(payload.get("max_stops", 1))
    baggage_required = bool(payload.get("baggage_required", False))

    offers: List[Dict[str, Any]] = []

    for offset in range(-window_days, window_days + 1):
        alt_departure = departure_date + timedelta(days=offset)
        alt_return = return_date + timedelta(days=offset)

        if offset == 0:
            offers.extend([
                {
                    "airline": "LATAM",
                    "source": "cash",
                    "price_total": 2890.0,
                    "stops": 1,
                    "duration_hours": 13.5,
                    "baggage_included": True,
                    "departure_date": alt_departure.isoformat(),
                    "return_date": alt_return.isoformat(),
                    "notes": "Rota direta via conexão curta em São Paulo.",
                },
                {
                    "airline": "TAP",
                    "source": "cash",
                    "price_total": 3180.0,
                    "stops": 0,
                    "duration_hours": 12.5,
                    "baggage_included": False,
                    "departure_date": alt_departure.isoformat(),
                    "return_date": alt_return.isoformat(),
                    "notes": "Mais confortável, mas sem bagagem inclusa.",
                },
                {
                    "airline": "Azul",
                    "source": "miles",
                    "price_total": 2450.0,
                    "stops": 1,
                    "duration_hours": 15.5,
                    "baggage_included": True,
                    "miles_needed": 31000,
                    "taxes": 120.0,
                    "program": "Azul",
                    "departure_date": alt_departure.isoformat(),
                    "return_date": alt_return.isoformat(),
                    "notes": "Boa economia em milhas com taxa baixa.",
                },
            ])
        elif offset in (-2, 2):
            offers.extend([
                {
                    "airline": "Gol",
                    "source": "cash",
                    "price_total": 2510.0,
                    "stops": 2,
                    "duration_hours": 18.0,
                    "baggage_included": False,
                    "departure_date": alt_departure.isoformat(),
                    "return_date": alt_return.isoformat(),
                    "notes": "Preço baixo, mas mais escalas e bagagem extra.",
                },
                {
                    "airline": "Iberia",
                    "source": "miles",
                    "price_total": 2650.0,
                    "stops": 1,
                    "duration_hours": 14.0,
                    "baggage_included": True,
                    "miles_needed": 34000,
                    "taxes": 140.0,
                    "program": "Iberia",
                    "departure_date": alt_departure.isoformat(),
                    "return_date": alt_return.isoformat(),
                    "notes": "Promoção com boa relação custo-benefício para pontos.",
                },
            ])

    filtered = []
    for offer in offers:
        if offer.get("stops", 0) <= max_stops:
            if baggage_required and not offer.get("baggage_included", False):
                continue
            filtered.append(offer)

    ranked = rank_offers(filtered)[:3]
    top_options = []
    for index, offer in enumerate(ranked, start=1):
        economy = round(float(offer.get("price_total", 0)) - 2890.0, 2)
        top_options.append({
            "rank": index,
            "airline": offer["airline"],
            "source": offer["source"],
            "program": offer.get("program"),
            "total_price": float(offer.get("price_total", 0)),
            "stops": int(offer.get("stops", 0)),
            "duration_hours": float(offer.get("duration_hours", 0)),
            "baggage_included": bool(offer.get("baggage_included", False)),
            "score": round(float(offer.get("score", 0)), 2),
            "economy_vs_original": round(economy, 2),
            "why_cheap": "Menor volume de demanda fora do pico, com conexão curta e tarifa mais competitiva." if offer["source"] == "cash" else "Oferta forte em milhas com taxa baixa e valor real por ponto acima da média.",
            "drawbacks": "Mais escalas ou bagagem extra se a tarifa for mais barata" if int(offer.get("stops", 0)) > 0 else "Menor flexibilidade para ajustes de voo.",
            "departure_date": offer.get("departure_date"),
            "return_date": offer.get("return_date"),
        })

    return {
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date.isoformat(),
        "return_date": return_date.isoformat(),
        "window_days": window_days,
        "results": top_options,
    }
