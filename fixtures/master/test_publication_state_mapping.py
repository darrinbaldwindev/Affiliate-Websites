import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).with_name("publication-state-mapping.synthetic.json")


def derive(case):
    data = case["input"]
    verification = data.get("verification_status", "unknown")
    freshness = data.get("freshness_status", "unknown")
    conflict = bool(data.get("conflict")) or verification == "conflicting"

    if conflict:
        display = "CONFLICTING_INFORMATION"
    elif verification in {"research_required", "claimed", "unknown", "rejected"}:
        display = "RESEARCH_REQUIRED"
    elif freshness in {"stale", "due", "overdue"}:
        display = "VERIFICATION_DUE"
    elif verification == "verified" and freshness == "current":
        display = "VERIFIED"
    else:
        display = "RESEARCH_REQUIRED"

    return {"display_state": display, "commercial_state": "COMMERCIAL_ACTION_BLOCKED"}


class PublicationStateMappingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = FIXTURE.read_text(encoding="utf-8")
        cls.data = json.loads(cls.raw)

    def test_fixture_is_non_production_and_has_no_urls(self):
        self.assertTrue(self.data["fixture"])
        self.assertFalse(self.data["production_use"])
        self.assertFalse(self.data["contains_tracking_urls"])
        self.assertNotIn("http://", self.raw)
        self.assertNotIn("https://", self.raw)

    def test_cases_match_fail_closed_mapping(self):
        for case in self.data["cases"]:
            self.assertEqual(derive(case), case["expected"], case["id"])

    def test_consumer_verified_does_not_imply_commercial_eligibility(self):
        case = next(c for c in self.data["cases"] if c["id"] == "verified-consumer-commercial-blocked")
        self.assertEqual(derive(case)["display_state"], "VERIFIED")
        self.assertEqual(case["input"]["publisher_relationship_status"], "unknown")
        self.assertEqual(derive(case)["commercial_state"], "COMMERCIAL_ACTION_BLOCKED")

    def test_conflict_precedes_verified(self):
        case = next(c for c in self.data["cases"] if c["id"] == "conflict-wins")
        self.assertEqual(derive(case)["display_state"], "CONFLICTING_INFORMATION")


if __name__ == "__main__":
    unittest.main()
