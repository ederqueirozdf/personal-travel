import unittest

from app.services.ranking import rank_offers


class TravelLogicTest(unittest.TestCase):
    def test_rank_offers_prefers_cheapest_realistic_option(self):
        offers = [
            {
                "source": "cash",
                "airline": "LATAM",
                "price_total": 4200,
                "stops": 2,
                "duration_hours": 19,
                "bagage_included": False,
            },
            {
                "source": "cash",
                "airline": "TAP",
                "price_total": 2800,
                "stops": 1,
                "duration_hours": 14,
                "bagage_included": True,
            },
        ]

        ranked = rank_offers(offers)
        self.assertEqual(ranked[0]["airline"], "TAP")


if __name__ == "__main__":
    unittest.main()
