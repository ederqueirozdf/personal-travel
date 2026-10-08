from typing import Any, Dict, Iterable, List


def _score_offer(offer: Dict[str, Any]) -> float:
    price_total = float(offer.get("price_total", 0) or 0)
    stops = int(offer.get("stops", 0) or 0)
    duration_hours = float(offer.get("duration_hours", 0) or 0)
    baggage_included = bool(offer.get("baggage_included", False))
    source = str(offer.get("source", "cash"))

    score = 1000.0
    score -= price_total / 20.0
    score -= stops * 80.0
    score -= duration_hours * 4.0
    score += 20.0 if baggage_included else -15.0
    score += 10.0 if source == "miles" else 0.0
    return score


def rank_offers(offers: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    ranked = []
    for offer in offers:
        item = dict(offer)
        item["score"] = _score_offer(offer)
        ranked.append(item)

    ranked.sort(key=lambda item: item["score"], reverse=True)
    return ranked
