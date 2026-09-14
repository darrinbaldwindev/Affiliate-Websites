import json
import unittest
from pathlib import Path

DATA = Path(__file__).parents[2] / "data" / "au" / "surveys.staging.json"


class AuSurveyStagingSafetyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(DATA.read_text(encoding="utf-8"))
        cls.programs = cls.data["programs"]

    def test_file_is_staging_only(self):
        self.assertEqual(self.data.get("status"), "STAGING_ONLY")
        self.assertFalse(self.data.get("production_use"))
        self.assertFalse(self.data.get("commercial_activation"))
        self.assertEqual(self.data.get("country"), "AU")

    def test_every_program_has_evidence_and_no_tracking_destination(self):
        self.assertGreaterEqual(len(self.programs), 5)
        for item in self.programs:
            self.assertTrue(item.get("evidence"), item["id"])
            relation = item.get("publisher_relationship", {})
            self.assertEqual(relation.get("status"), "unknown", item["id"])
            self.assertIsNone(relation.get("tracking_destination"), item["id"])
            self.assertFalse(relation.get("cta_eligible"), item["id"])

    def test_primary_evidence_has_verification_date(self):
        for item in self.programs:
            for evidence in item["evidence"]:
                self.assertEqual(evidence.get("source_type"), "primary", item["id"])
                self.assertTrue(evidence.get("verified_at"), item["id"])
                self.assertTrue(evidence.get("source", "").startswith("https://"), item["id"])

    def test_partial_au_records_are_not_marked_active(self):
        for item in self.programs:
            state = item.get("consumer_claims", {}).get("evidence_state")
            if state == "partial":
                self.assertEqual(item.get("status"), "research_required", item["id"])


if __name__ == "__main__":
    unittest.main()
