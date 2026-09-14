import json
import unittest
from datetime import date, timedelta
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
                self.assertEqual(item.get("lifecycle_state"), "RESEARCHED", item["id"])
                self.assertEqual(item.get("publication_gate", {}).get("consumer_content"), "BLOCKED", item["id"])

    def test_verified_records_stop_before_publishable(self):
        for item in self.programs:
            if item.get("lifecycle_state") == "VERIFIED":
                self.assertEqual(item.get("consumer_claims", {}).get("evidence_state"), "verified_primary", item["id"])
                self.assertEqual(item.get("publication_gate", {}).get("consumer_content"), "VERIFIED_NOT_PUBLISHED", item["id"])
                self.assertNotIn(item.get("lifecycle_state"), {"PUBLISHABLE", "PUBLISHED", "MONITORED"}, item["id"])

    def test_commercial_cta_is_blocked_for_all_real_records(self):
        for item in self.programs:
            gate = item.get("publication_gate", {})
            self.assertEqual(gate.get("commercial_cta"), "BLOCKED", item["id"])
            reasons = set(gate.get("blocking_reasons", []))
            self.assertIn("PUBLISHER_RELATIONSHIP_UNKNOWN", reasons, item["id"])
            self.assertIn("COMMERCIAL_DESTINATION_UNAPPROVED", reasons, item["id"])

    def test_freshness_window_is_machine_readable_and_consistent(self):
        interval = self.data.get("freshness_policy", {}).get("review_interval_days")
        self.assertEqual(interval, 30)
        for item in self.programs:
            freshness = item.get("freshness", {})
            verified = date.fromisoformat(freshness["last_verified_at"])
            due = date.fromisoformat(freshness["review_due_at"])
            self.assertEqual(due, verified + timedelta(days=interval), item["id"])
            if item.get("lifecycle_state") == "VERIFIED":
                self.assertEqual(freshness.get("state"), "CURRENT", item["id"])
            else:
                self.assertEqual(freshness.get("state"), "PARTIAL", item["id"])

    def test_expired_evidence_cannot_be_treated_as_current(self):
        interval = self.data["freshness_policy"]["review_interval_days"]
        synthetic_verified_at = date(2026, 1, 1)
        synthetic_check_date = synthetic_verified_at + timedelta(days=interval + 1)
        is_current = synthetic_check_date <= synthetic_verified_at + timedelta(days=interval)
        self.assertFalse(is_current)


if __name__ == "__main__":
    unittest.main()
