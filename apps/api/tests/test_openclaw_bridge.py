import unittest

from app.services.openclaw_bridge import execute_personal_travel_agent


class OpenClawBridgeTest(unittest.TestCase):
    def test_bridge_returns_agent_payload(self):
        payload = {
            "origin": "GRU",
            "destination": "LIS",
            "departure_date": "2026-11-10",
            "return_date": "2026-11-20",
            "window_days": 3,
            "max_stops": 1,
            "baggage_required": True,
            "search_mode": "mixed",
        }

        result = execute_personal_travel_agent(payload)
        self.assertEqual(result["agent"], "personal-travel")
        self.assertEqual(result["source"], "openclaw")
        self.assertGreater(len(result["results"]), 0)


if __name__ == "__main__":
    unittest.main()
