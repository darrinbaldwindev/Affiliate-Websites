import copy
import json
import tempfile
import unittest
from pathlib import Path

from validate_country_cta import validate


BASE = {
    "fixture": True,
    "countries": ["AU", "UK", "US"],
    "programs": [
        {
            "program_id": "AU-SURVEY-GATE-001",
            "country": "AU",
            "consumer_reward_evidence": "FIXTURE",
            "country_eligibility_evidence": "FIXTURE",
            "publisher_relationship": "VERIFIED_PUBLISHER",
            "publisher_evidence_source": "fixture://au-surveys/publisher-program",
            "publisher_verified_at": "2026-09-14T00:00:00Z",
            "publisher_evidence_conflict": False,
            "cta_state": "VERIFIED_PUBLISHER",
            "destination_url": "https://example.invalid/au-surveys-fixture",
            "evidence_freshness": "FIXTURE",
            "disclosure_present": True,
        },
        {
            "program_id": "UK-SYNTH-SAFE",
            "country": "UK",
            "consumer_reward_evidence": "FIXTURE",
            "country_eligibility_evidence": "FIXTURE",
            "publisher_relationship": "UNKNOWN",
            "publisher_evidence_source": None,
            "publisher_verified_at": None,
            "publisher_evidence_conflict": False,
            "cta_state": "NON_AFFILIATE_FALLBACK",
            "destination_url": None,
            "evidence_freshness": "FIXTURE",
            "disclosure_present": True,
        },
        {
            "program_id": "US-SYNTH-SAFE",
            "country": "US",
            "consumer_reward_evidence": "FIXTURE",
            "country_eligibility_evidence": "FIXTURE",
            "publisher_relationship": "CONSUMER_REFERRAL_ONLY",
            "publisher_evidence_source": None,
            "publisher_verified_at": None,
            "publisher_evidence_conflict": False,
            "cta_state": "NON_AFFILIATE_FALLBACK",
            "destination_url": None,
            "evidence_freshness": "FIXTURE",
            "disclosure_present": True,
        },
    ],
}


class AuSurveysCtaGateTests(unittest.TestCase):
    def run_fixture(self, data):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            validate(str(path))

    def au(self, data):
        return data["programs"][0]

    def test_fully_synthetic_verified_state_can_pass(self):
        self.run_fixture(copy.deepcopy(BASE))

    def test_conflicting_publisher_evidence_blocks_verified_cta(self):
        data = copy.deepcopy(BASE)
        self.au(data)["publisher_evidence_conflict"] = True
        with self.assertRaises(SystemExit):
            self.run_fixture(data)

    def test_stale_publisher_evidence_blocks_verified_cta(self):
        data = copy.deepcopy(BASE)
        self.au(data)["evidence_freshness"] = "STALE"
        with self.assertRaises(SystemExit):
            self.run_fixture(data)

    def test_missing_disclosure_blocks_verified_cta(self):
        data = copy.deepcopy(BASE)
        self.au(data)["disclosure_present"] = False
        with self.assertRaises(SystemExit):
            self.run_fixture(data)

    def test_unknown_relationship_cannot_keep_destination(self):
        data = copy.deepcopy(BASE)
        item = self.au(data)
        item["publisher_relationship"] = "UNKNOWN"
        item["publisher_evidence_source"] = None
        item["publisher_verified_at"] = None
        item["cta_state"] = "NON_AFFILIATE_FALLBACK"
        with self.assertRaises(SystemExit):
            self.run_fixture(data)

    def test_consumer_referral_only_cannot_be_publisher_cta(self):
        data = copy.deepcopy(BASE)
        item = self.au(data)
        item["publisher_relationship"] = "CONSUMER_REFERRAL_ONLY"
        item["publisher_evidence_source"] = None
        item["publisher_verified_at"] = None
        with self.assertRaises(SystemExit):
            self.run_fixture(data)


if __name__ == "__main__":
    unittest.main()
