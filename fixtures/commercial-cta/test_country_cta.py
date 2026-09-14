import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from validate_country_cta import validate

BASE = {
    "fixture": True,
    "countries": ["AU", "UK", "US"],
    "programs": [
        {
            "program_id": "AU-SYNTH-001", "country": "AU", "consumer_reward_evidence": "FIXTURE",
            "country_eligibility_evidence": "FIXTURE", "publisher_relationship": "UNKNOWN",
            "publisher_evidence_source": None, "publisher_verified_at": None, "publisher_evidence_conflict": False,
            "cta_state": "NON_AFFILIATE_FALLBACK", "destination_url": None, "evidence_freshness": "FIXTURE",
            "disclosure_present": True,
        },
        {
            "program_id": "UK-SYNTH-001", "country": "UK", "consumer_reward_evidence": "FIXTURE",
            "country_eligibility_evidence": "FIXTURE", "publisher_relationship": "VERIFIED_PUBLISHER",
            "publisher_evidence_source": "fixture://publisher-program", "publisher_verified_at": "2026-09-14T00:00:00Z",
            "publisher_evidence_conflict": False, "cta_state": "VERIFIED_PUBLISHER",
            "destination_url": "https://example.invalid/fixture-affiliate", "evidence_freshness": "FIXTURE",
            "disclosure_present": True,
        },
        {
            "program_id": "US-SYNTH-001", "country": "US", "consumer_reward_evidence": "FIXTURE",
            "country_eligibility_evidence": "FIXTURE", "publisher_relationship": "CONSUMER_REFERRAL_ONLY",
            "publisher_evidence_source": None, "publisher_verified_at": None, "publisher_evidence_conflict": False,
            "cta_state": "NON_AFFILIATE_FALLBACK", "destination_url": None, "evidence_freshness": "FIXTURE",
            "disclosure_present": True,
        },
    ],
}


def run_case(data):
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "fixture.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        out = io.StringIO()
        with redirect_stdout(out):
            validate(str(path))
        return json.loads(out.getvalue())


class GovernedCtaTests(unittest.TestCase):
    def test_valid_fixture_emits_non_tracking_audit(self):
        result = run_case(BASE)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["validated"], 3)
        self.assertTrue(all(event["tracking_url"] is None for event in result["audit_events"]))
        allowed = next(event for event in result["audit_events"] if event["program_id"] == "UK-SYNTH-001")
        self.assertEqual(allowed["decision"], "ALLOWED")

    def test_consumer_referral_cannot_be_publisher_cta(self):
        data = json.loads(json.dumps(BASE)); data["programs"][2]["cta_state"] = "VERIFIED_PUBLISHER"
        with self.assertRaises(SystemExit): run_case(data)

    def test_unknown_relationship_cannot_carry_url(self):
        data = json.loads(json.dumps(BASE)); data["programs"][0]["destination_url"] = "https://merchant.example/live"
        with self.assertRaises(SystemExit): run_case(data)

    def test_nonverified_relationship_cannot_carry_publisher_evidence(self):
        for index in (0, 2):
            data = json.loads(json.dumps(BASE)); data["programs"][index]["publisher_evidence_source"] = "fixture://leak"; data["programs"][index]["publisher_verified_at"] = "2026-09-14T00:00:00Z"
            with self.assertRaises(SystemExit): run_case(data)

    def test_verified_publisher_requires_source(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["publisher_evidence_source"] = None
        with self.assertRaises(SystemExit): run_case(data)

    def test_verified_fixture_url_must_be_non_live(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["destination_url"] = "https://merchant.example/live"
        with self.assertRaises(SystemExit): run_case(data)

    def test_stale_evidence_cannot_publish_verified_cta(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["evidence_freshness"] = "STALE"
        with self.assertRaises(SystemExit): run_case(data)

    def test_missing_consumer_reward_evidence_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["consumer_reward_evidence"] = None
        with self.assertRaises(SystemExit): run_case(data)

    def test_country_eligibility_is_independent_required_evidence(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["country_eligibility_evidence"] = None
        with self.assertRaisesRegex(SystemExit, "country eligibility"):
            run_case(data)

    def test_disclosure_required_for_publishable_synthetic_cta(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["disclosure_present"] = False
        with self.assertRaisesRegex(SystemExit, "disclosure"):
            run_case(data)

    def test_conflicting_publisher_evidence_blocks_verified_cta(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["publisher_evidence_conflict"] = True
        with self.assertRaisesRegex(SystemExit, "conflicting publisher evidence"):
            run_case(data)

    def test_invalid_publisher_relationship_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"][0]["publisher_relationship"] = "NETWORK_LISTED_ONLY"
        with self.assertRaises(SystemExit): run_case(data)

    def test_invalid_freshness_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"][0]["evidence_freshness"] = "MAYBE"
        with self.assertRaises(SystemExit): run_case(data)

    def test_duplicate_program_id_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"][2]["program_id"] = data["programs"][0]["program_id"]
        with self.assertRaises(SystemExit): run_case(data)

    def test_empty_program_batch_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"] = []
        with self.assertRaises(SystemExit): run_case(data)

    def test_missing_country_program_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"] = [item for item in data["programs"] if item["country"] != "US"]
        with self.assertRaises(SystemExit): run_case(data)

    def test_duplicate_country_declaration_rejected(self):
        data = json.loads(json.dumps(BASE)); data["countries"].append("AU")
        with self.assertRaises(SystemExit): run_case(data)

    def test_future_publisher_datetime_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["publisher_verified_at"] = "2999-01-01T00:00:00Z"
        with self.assertRaisesRegex(SystemExit, "cannot be in the future"):
            run_case(data)

    def test_future_publisher_date_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["publisher_verified_at"] = "2999-01-01"
        with self.assertRaisesRegex(SystemExit, "cannot be in the future"):
            run_case(data)

    def test_malformed_publisher_timestamp_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["publisher_verified_at"] = "not-a-date"
        with self.assertRaisesRegex(SystemExit, "invalid publisher verification timestamp"):
            run_case(data)

    def test_naive_publisher_datetime_rejected(self):
        data = json.loads(json.dumps(BASE)); data["programs"][1]["publisher_verified_at"] = "2026-09-14T00:00:00"
        with self.assertRaisesRegex(SystemExit, "must include timezone"):
            run_case(data)


if __name__ == "__main__":
    unittest.main()
