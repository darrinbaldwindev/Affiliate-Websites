import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from validate_country_cta import validate

ROOT = Path(__file__).parent
BASE = json.loads((ROOT / "uk-governance.synthetic.json").read_text(encoding="utf-8"))


def run_case(data):
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "fixture.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        out = io.StringIO()
        with redirect_stdout(out):
            validate(str(path))
        return json.loads(out.getvalue())


def event_for(result, program_id):
    return next(event for event in result["audit_events"] if event["program_id"] == program_id)


class UkAuditReasonTests(unittest.TestCase):
    def test_unknown_uk_broadband_relationship_has_stable_reason(self):
        result = run_case(BASE)
        event = event_for(result, "UK-BROADBAND-FIXTURE-001")
        self.assertEqual(event["decision"], "BLOCKED")
        self.assertEqual(event["reason"], "NO_VERIFIED_PUBLISHER_RELATIONSHIP")
        self.assertEqual(event["country"], "UK")
        self.assertEqual(event["risk_class"], "TELECOM")

    def test_stale_uk_energy_has_stable_reason(self):
        result = run_case(BASE)
        event = event_for(result, "UK-ENERGY-FIXTURE-001")
        self.assertEqual(event["decision"], "BLOCKED")
        self.assertEqual(event["reason"], "STALE_EVIDENCE")
        self.assertEqual(event["risk_class"], "UTILITIES_HOME_ENERGY")

    def test_verified_uk_technology_is_allowed_without_tracking_url_in_audit(self):
        result = run_case(BASE)
        event = event_for(result, "UK-TECH-FIXTURE-001")
        self.assertEqual(event["decision"], "ALLOWED")
        self.assertEqual(event["reason"], "VERIFIED_SYNTHETIC_PUBLISHER")
        self.assertIsNone(event["tracking_url"])

    def test_consumer_referral_only_has_stable_reason(self):
        data = json.loads(json.dumps(BASE))
        target = next(item for item in data["programs"] if item["program_id"] == "UK-BROADBAND-FIXTURE-001")
        target["publisher_relationship"] = "CONSUMER_REFERRAL_ONLY"
        result = run_case(data)
        event = event_for(result, "UK-BROADBAND-FIXTURE-001")
        self.assertEqual(event["reason"], "CONSUMER_REFERRAL_ONLY")


if __name__ == "__main__":
    unittest.main()
