import json
import unittest
from pathlib import Path

FIXTURE = Path(__file__).with_name("shortlist.synthetic.json")


class AuSurveyShortlistFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(FIXTURE.read_text(encoding="utf-8"))
        cls.programs = cls.data["programs"]

    def test_fixture_is_explicitly_non_production(self):
        self.assertTrue(self.data.get("fixture"))
        self.assertFalse(self.data["safety"]["production_use"])
        self.assertFalse(self.data["safety"]["contains_live_rates"])
        self.assertFalse(self.data["safety"]["contains_live_tracking_urls"])
        self.assertFalse(self.data["safety"]["contains_claimed_real_relationships"])

    def test_all_records_are_au(self):
        self.assertEqual(self.data.get("country"), "AU")
        self.assertGreaterEqual(len(self.programs), 6)

    def test_unverified_relationships_cannot_have_destination(self):
        for program in self.programs:
            if program["publisher_relationship"] != "VERIFIED_PUBLISHER":
                self.assertIsNone(program.get("commercial_destination"), program["program_id"])
                self.assertEqual(program.get("cta_state"), "NON_AFFILIATE_FALLBACK", program["program_id"])

    def test_only_fully_safe_verified_fixture_can_have_destination(self):
        enabled = [p for p in self.programs if p.get("commercial_destination")]
        self.assertEqual(len(enabled), 1)
        item = enabled[0]
        self.assertEqual(item["publisher_relationship"], "VERIFIED_PUBLISHER")
        self.assertFalse(item["publisher_evidence_conflict"])
        self.assertEqual(item["evidence_freshness"], "FIXTURE_FRESH")
        self.assertTrue(item["disclosure_present"])
        self.assertTrue(item["publisher_evidence_source"].startswith("fixture://"))
        self.assertTrue(item["commercial_destination"].startswith("https://example.invalid/"))
        self.assertEqual(item["cta_state"], "VERIFIED_PUBLISHER")

    def test_conflicting_verified_relationship_is_blocked(self):
        item = next(p for p in self.programs if p["program_id"] == "AU-SURVEY-SYNTH-004")
        self.assertEqual(item["publisher_relationship"], "VERIFIED_PUBLISHER")
        self.assertTrue(item["publisher_evidence_conflict"])
        self.assertIsNone(item["commercial_destination"])
        self.assertEqual(item["cta_state"], "BLOCKED_CONFLICT")

    def test_stale_verified_relationship_is_blocked(self):
        item = next(p for p in self.programs if p["program_id"] == "AU-SURVEY-SYNTH-005")
        self.assertEqual(item["publisher_relationship"], "VERIFIED_PUBLISHER")
        self.assertEqual(item["evidence_freshness"], "STALE")
        self.assertIsNone(item["commercial_destination"])
        self.assertEqual(item["cta_state"], "BLOCKED_STALE")

    def test_missing_disclosure_is_blocked(self):
        item = next(p for p in self.programs if p["program_id"] == "AU-SURVEY-SYNTH-006")
        self.assertEqual(item["publisher_relationship"], "VERIFIED_PUBLISHER")
        self.assertFalse(item["disclosure_present"])
        self.assertIsNone(item["commercial_destination"])
        self.assertEqual(item["cta_state"], "BLOCKED_DISCLOSURE")


if __name__ == "__main__":
    unittest.main()
