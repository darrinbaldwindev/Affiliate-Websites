import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[2]
STAGING = ROOT / "data" / "au" / "surveys.staging.json"
PROJECTION = ROOT / "data" / "au" / "surveys.publication-projection.json"


class AuSurveyPublicationProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.staging = json.loads(STAGING.read_text(encoding="utf-8"))
        cls.projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
        cls.staging_by_id = {item["id"]: item for item in cls.staging["programs"]}
        cls.projected_by_id = {item["id"]: item for item in cls.projection["records"]}

    def test_projection_is_non_production_and_url_free(self):
        self.assertEqual(self.projection["status"], "STAGING_PROJECTION_ONLY")
        self.assertFalse(self.projection["production_use"])
        self.assertFalse(self.projection["contains_tracking_urls"])
        self.assertNotIn("http://", json.dumps(self.projection))
        self.assertNotIn("https://", json.dumps(self.projection))

    def test_projection_covers_each_staging_record_once(self):
        self.assertEqual(set(self.projected_by_id), set(self.staging_by_id))
        self.assertEqual(len(self.projection["records"]), len(self.projected_by_id))

    def test_display_state_matches_publication_gate(self):
        for program_id, source in self.staging_by_id.items():
            projected = self.projected_by_id[program_id]
            gate = source["publication_gate"]
            if gate["consumer_content"] == "VERIFIED_NOT_PUBLISHED":
                self.assertEqual(projected["display_state"], "INFORMATIONAL_VERIFIED", program_id)
            elif gate["consumer_content"] == "BLOCKED":
                self.assertEqual(projected["display_state"], "RESEARCH_REQUIRED", program_id)
            else:
                self.fail(f"Unexpected consumer publication state for {program_id}: {gate['consumer_content']}")

    def test_commercial_state_cannot_exceed_source_gate(self):
        for program_id, source in self.staging_by_id.items():
            projected = self.projected_by_id[program_id]
            self.assertEqual(source["publication_gate"]["commercial_cta"], "BLOCKED", program_id)
            self.assertEqual(projected["commercial_state"], "BLOCKED", program_id)
            self.assertEqual(
                set(projected["reason_codes"]),
                set(source["publication_gate"]["blocking_reasons"]),
                program_id,
            )


if __name__ == "__main__":
    unittest.main()
