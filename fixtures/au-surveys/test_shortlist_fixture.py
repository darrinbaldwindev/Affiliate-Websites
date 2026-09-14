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
        self.assertGreaterEqual(len(self.programs), 3)

    def test_unverified_relationships_cannot_have_destination(self):
        for program in self.programs:
            if program["publisher_relationship"] != "VERIFIED_PUBLISHER":
                self.assertIsNone(program.get("commercial_destination"), program["program_id"])
                self.assertEqual(program.get("cta_state"), "NON_AFFILIATE_FALLBACK", program["program_id"])

    def test_verified_fixture_is_still_synthetic(self):
        verified = [p for p in self.programs if p["publisher_relationship"] == "VERIFIED_PUBLISHER"]
        self.assertEqual(len(verified), 1)
        item = verified[0]
        self.assertTrue(item["publisher_evidence_source"].startswith("fixture://"))
        self.assertTrue(item["commercial_destination"].startswith("https://example.invalid/"))
        self.assertEqual(item["cta_state"], "VERIFIED_PUBLISHER")

    def test_disclosure_present_for_every_record(self):
        for program in self.programs:
            self.assertTrue(program.get("disclosure_present"), program["program_id"])


if __name__ == "__main__":
    unittest.main()
