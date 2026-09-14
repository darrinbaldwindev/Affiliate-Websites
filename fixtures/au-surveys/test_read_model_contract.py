import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[2]
CONTRACT = ROOT / "data" / "au" / "surveys.read-model-contract.json"
STAGING = ROOT / "data" / "au" / "surveys.staging.json"
PUBLICATION = ROOT / "data" / "au" / "surveys.publication-projection.json"
PRIORITY = ROOT / "data" / "au" / "surveys.priority-projection.json"


class AuSurveyReadModelContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        cls.staging = json.loads(STAGING.read_text(encoding="utf-8"))
        cls.publication = json.loads(PUBLICATION.read_text(encoding="utf-8"))
        cls.priority = json.loads(PRIORITY.read_text(encoding="utf-8"))
        cls.staging_by_id = {item["id"]: item for item in cls.staging["programs"]}
        cls.publication_by_id = {item["id"]: item for item in cls.publication["records"]}
        cls.priority_by_id = {item["id"]: item for item in cls.priority["records"]}

    def test_wordpress_is_explicitly_non_authoritative(self):
        boundary = self.contract["presentation_boundary"]
        self.assertFalse(boundary["wordpress_is_authority"])
        self.assertFalse(boundary["may_store_raw_tracking_urls"])
        self.assertFalse(boundary["may_store_raw_affiliate_destinations"])
        self.assertFalse(boundary["may_rank_by_publisher_economics"])
        self.assertFalse(boundary["may_override_lifecycle_state"])
        self.assertFalse(boundary["may_override_freshness_state"])
        self.assertFalse(boundary["may_override_commercial_state"])

    def test_contract_forbids_raw_commercial_fields(self):
        forbidden = set(self.contract["detail_record"]["commercial_action"]["forbidden_fields"])
        self.assertTrue({"raw_url", "tracking_url", "affiliate_url", "commission_rate"}.issubset(forbidden))
        serialized = json.dumps(self.contract).lower()
        self.assertNotIn("utm_", serialized)

    def test_projection_identity_is_consistent(self):
        staging_ids = set(self.staging_by_id)
        self.assertEqual(set(self.publication_by_id), staging_ids)
        self.assertEqual(set(self.priority_by_id), staging_ids)

    def test_verified_priority_records_cannot_be_partial_or_stale(self):
        for program_id, ranked in self.priority_by_id.items():
            source = self.staging_by_id[program_id]
            if ranked["tier"] in {"FLAGSHIP", "CORE", "SECONDARY"}:
                self.assertEqual(source["lifecycle_state"], "VERIFIED", program_id)
                self.assertEqual(source["freshness"]["state"], "CURRENT", program_id)
                self.assertEqual(ranked["display_state"], "INFORMATIONAL_VERIFIED", program_id)

    def test_research_hold_is_never_promoted(self):
        for program_id, ranked in self.priority_by_id.items():
            source = self.staging_by_id[program_id]
            if source["lifecycle_state"] != "VERIFIED":
                self.assertEqual(ranked["tier"], "RESEARCH_HOLD", program_id)
                self.assertEqual(ranked["display_state"], "RESEARCH_REQUIRED", program_id)

    def test_all_current_real_records_remain_commercially_blocked(self):
        for program_id, projected in self.publication_by_id.items():
            source = self.staging_by_id[program_id]
            self.assertEqual(projected["commercial_state"], "BLOCKED", program_id)
            self.assertEqual(source["publication_gate"]["commercial_cta"], "BLOCKED", program_id)
            self.assertFalse(source["publisher_relationship"]["cta_eligible"], program_id)
            self.assertIsNone(source["publisher_relationship"]["tracking_destination"], program_id)

    def test_priority_ranks_are_unique_and_contiguous(self):
        ranks = sorted(item["rank"] for item in self.priority["records"])
        self.assertEqual(ranks, list(range(1, len(ranks) + 1)))

    def test_priority_projection_contains_no_commercial_economics_or_urls(self):
        self.assertFalse(self.priority["commercial_economics_used"])
        serialized = json.dumps(self.priority).lower()
        for forbidden in ["http://", "https://", "affiliate_url", "tracking_url", "commission_rate", "utm_"]:
            self.assertNotIn(forbidden, serialized)


if __name__ == "__main__":
    unittest.main()
