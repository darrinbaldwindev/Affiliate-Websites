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
            "program_id": "AU-SYNTH-001",
            "country": "AU",
            "consumer_reward_evidence": "FIXTURE",
            "publisher_relationship": "UNKNOWN",
            "publisher_evidence_source": None,
            "publisher_verified_at": None,
            "cta_state": "NON_AFFILIATE_FALLBACK",
            "destination_url": None,
            "evidence_freshness": "FIXTURE",
        },
        {
            "program_id": "UK-SYNTH-001",
            "country": "UK",
            "consumer_reward_evidence": "FIXTURE",
            "publisher_relationship": "VERIFIED_PUBLISHER",
            "publisher_evidence_source": "fixture://publisher-program",
            "publisher_verified_at": "2026-09-14T00:00:00Z",
            "cta_state": "VERIFIED_PUBLISHER",
            "destination_url": "https://example.invalid/fixture-affiliate",
            "evidence_freshness": "FIXTURE",
        },
        {
            "program_id": "US-SYNTH-001",
            "country": "US",
            "consumer_reward_evidence": "FIXTURE",
            "publisher_relationship": "CONSUMER_REFERRAL_ONLY",
            "publisher_evidence_source": None,
            "publisher_verified_at": None,
            "cta_state": "NON_AFFILIATE_FALLBACK",
            "destination_url": None,
            "evidence_freshness": "FIXTURE",
        },
    ],
}


def run_case(data):
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "fixture.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        validate(str(path))


class GovernedCtaTests(unittest.TestCase):
    def test_valid_fixture(self):
        run_case(BASE)

    def test_consumer_referral_cannot_be_publisher_cta(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][2]["cta_state"] = "VERIFIED_PUBLISHER"
        with self.assertRaises(SystemExit):
            run_case(data)

    def test_unknown_relationship_cannot_carry_url(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][0]["destination_url"] = "https://merchant.example/live"
        with self.assertRaises(SystemExit):
            run_case(data)

    def test_nonverified_relationship_cannot_carry_publisher_evidence(self):
        for index in (0, 2):
            data = json.loads(json.dumps(BASE))
            data["programs"][index]["publisher_evidence_source"] = "fixture://leaked-publisher-proof"
            data["programs"][index]["publisher_verified_at"] = "2026-09-14T00:00:00Z"
            with self.assertRaises(SystemExit):
                run_case(data)

    def test_verified_publisher_requires_source(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][1]["publisher_evidence_source"] = None
        with self.assertRaises(SystemExit):
            run_case(data)

    def test_verified_fixture_url_must_be_non_live(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][1]["destination_url"] = "https://merchant.example/live"
        with self.assertRaises(SystemExit):
            run_case(data)

    def test_stale_evidence_cannot_publish_verified_cta(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][1]["evidence_freshness"] = "STALE"
        with self.assertRaises(SystemExit):
            run_case(data)

    def test_missing_consumer_reward_evidence_rejected(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][1]["consumer_reward_evidence"] = None
        with self.assertRaises(SystemExit):
            run_case(data)

    def test_invalid_publisher_relationship_rejected(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][0]["publisher_relationship"] = "NETWORK_LISTED_ONLY"
        with self.assertRaises(SystemExit):
            run_case(data)

    def test_invalid_freshness_rejected(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][0]["evidence_freshness"] = "MAYBE"
        with self.assertRaises(SystemExit):
            run_case(data)

    def test_duplicate_program_id_rejected(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][2]["program_id"] = data["programs"][0]["program_id"]
        with self.assertRaises(SystemExit):
            run_case(data)


if __name__ == "__main__":
    unittest.main()
