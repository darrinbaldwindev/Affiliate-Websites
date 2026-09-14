import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[2]
STAGING = ROOT / "data" / "au" / "surveys.staging.json"
PRIORITY = ROOT / "data" / "au" / "surveys.priority-projection.json"


class AuSurveyPriorityProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.staging = json.loads(STAGING.read_text(encoding="utf-8"))
        cls.priority = json.loads(PRIORITY.read_text(encoding="utf-8"))
        cls.staging_by_id = {item["id"]: item for item in cls.staging["programs"]}
        cls.records = cls.priority["records"]

    def test_priority_projection_is_non_production_and_commission_free(self):
        self.assertEqual(self.priority["status"], "STAGING_PRIORITY_ONLY")
        self.assertFalse(self.priority["production_use"])
        self.assertFalse(self.priority["commercial_economics_used"])
        serialized = json.dumps(self.priority).lower()
        self.assertNotIn("commission_rate", serialized)
        self.assertNotIn("tracking_url", serialized)
        self.assertNotIn("affiliate_url", serialized)

    def test_priority_ids_exist_and_ranks_are_unique_contiguous(self):
        ids = [item["id"] for item in self.records]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(set(ids).issubset(self.staging_by_id))
        ranks = sorted(item["rank"] for item in self.records)
        self.assertEqual(ranks, list(range(1, len(self.records) + 1)))

    def test_verified_records_are_not_misrepresented_as_publishable(self):
        for item in self.records:
            source = self.staging_by_id[item["id"]]
            if source["lifecycle_state"] == "VERIFIED":
                self.assertEqual(item["display_state"], "INFORMATIONAL_VERIFIED", item["id"])
                self.assertEqual(source["publication_gate"]["commercial_cta"], "BLOCKED", item["id"])

    def test_research_hold_is_required_for_partial_records(self):
        for item in self.records:
            source = self.staging_by_id[item["id"]]
            if source["consumer_claims"]["evidence_state"] == "partial":
                self.assertEqual(item["tier"], "RESEARCH_HOLD", item["id"])
                self.assertEqual(item["display_state"], "RESEARCH_REQUIRED", item["id"])

    def test_flagship_and_core_entries_have_current_primary_evidence(self):
        for item in self.records:
            if item["tier"] in {"FLAGSHIP", "CORE"}:
                source = self.staging_by_id[item["id"]]
                self.assertEqual(source["freshness"]["state"], "CURRENT", item["id"])
                self.assertEqual(source["consumer_claims"]["evidence_state"], "verified_primary", item["id"])
                self.assertTrue(source["evidence"], item["id"])


if __name__ == "__main__":
    unittest.main()
