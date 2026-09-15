import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).with_name("presentation-payload.synthetic.json")


class PresentationPayloadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = FIXTURE.read_text(encoding="utf-8")
        cls.data = json.loads(cls.raw)

    def test_fixture_is_non_production_and_contains_no_urls(self):
        self.assertTrue(self.data["fixture"])
        self.assertFalse(self.data["production_use"])
        self.assertFalse(self.data["contains_tracking_urls"])
        self.assertNotIn("http://", self.raw)
        self.assertNotIn("https://", self.raw)

    def test_required_identity_and_state_fields_exist(self):
        for case in self.data["cases"]:
            payload = case["payload"]
            self.assertEqual(payload["schema"], "affiliate.presentation.v1")
            self.assertIn(payload["country"], {"AU", "UK", "US"})
            self.assertTrue(payload["entity_type"])
            self.assertTrue(payload["entity_id"])
            self.assertIn("state", payload["display"])
            self.assertIn("state", payload["commercial"])
            self.assertTrue(payload["fixture"])

    def test_blocked_commercial_state_never_hands_off(self):
        for case in self.data["cases"]:
            commercial = case["payload"]["commercial"]
            if commercial["state"] == "BLOCKED":
                self.assertEqual(case["expected_action"], "NON_AFFILIATE_FALLBACK")

    def test_verified_consumer_state_can_remain_commercially_blocked(self):
        case = next(c for c in self.data["cases"] if c["id"] == "verified-consumer-commercial-blocked")
        self.assertEqual(case["payload"]["display"]["state"], "VERIFIED")
        self.assertEqual(case["payload"]["commercial"]["state"], "BLOCKED")
        self.assertIn("PUBLISHER_RELATIONSHIP_UNKNOWN", case["payload"]["commercial"]["reason_codes"])

    def test_eligible_case_is_semantic_handoff_only(self):
        case = next(c for c in self.data["cases"] if c["id"] == "eligible-semantic-handoff-only")
        self.assertEqual(case["expected_action"], "RESOLVER_HANDOFF")
        payload = case["payload"]
        self.assertEqual(payload["commercial"]["state"], "ELIGIBLE_FOR_RESOLUTION")
        self.assertEqual(payload["commercial"]["action"], "join")
        self.assertNotIn("destination", payload["commercial"])
        self.assertNotIn("url", payload["commercial"])


if __name__ == "__main__":
    unittest.main()
