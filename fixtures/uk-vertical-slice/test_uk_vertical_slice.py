import json
import tempfile
import unittest
from pathlib import Path

from validate_uk_vertical_slice import validate

ROOT = Path(__file__).parent
CONTENT = json.loads((ROOT / "technology-appliances.synthetic.json").read_text(encoding="utf-8"))
CTA = json.loads((ROOT.parent / "commercial-cta" / "uk-governance.synthetic.json").read_text(encoding="utf-8"))


def run_case(content, cta=CTA):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        content_path = td / "content.json"
        cta_path = td / "cta.json"
        content_path.write_text(json.dumps(content), encoding="utf-8")
        cta_path.write_text(json.dumps(cta), encoding="utf-8")
        validate(str(content_path), str(cta_path))


class UkVerticalSliceTests(unittest.TestCase):
    def test_valid_fixture_passes(self):
        run_case(CONTENT)

    def test_wrong_country_route_rejected(self):
        data = json.loads(json.dumps(CONTENT))
        data["journey"][1]["route"] = "/au/technology-appliances/comparisons/example-appliances/"
        with self.assertRaisesRegex(SystemExit, "inside UK"):
            run_case(data)

    def test_unknown_resolver_ref_rejected(self):
        data = json.loads(json.dumps(CONTENT))
        data["journey"][-1]["program_id"] = "UK-NOT-THERE"
        data["journey"][-1]["commercial_action"]["resolver_ref"] = "UK-NOT-THERE"
        with self.assertRaisesRegex(SystemExit, "absent"):
            run_case(data)

    def test_live_price_field_rejected(self):
        data = json.loads(json.dumps(CONTENT))
        data["journey"][-1]["price"] = "£999"
        with self.assertRaisesRegex(SystemExit, "forbidden live field"):
            run_case(data)

    def test_raw_tracking_url_rejected(self):
        data = json.loads(json.dumps(CONTENT))
        data["journey"][-1]["tracking_url"] = "https://example.invalid/track"
        with self.assertRaisesRegex(SystemExit, "forbidden live field"):
            run_case(data)

    def test_missing_disclosure_requirement_rejected(self):
        data = json.loads(json.dumps(CONTENT))
        data["journey"][-1]["disclosure_required"] = False
        with self.assertRaisesRegex(SystemExit, "disclosure"):
            run_case(data)

    def test_country_mismatched_cta_program_rejected(self):
        data = json.loads(json.dumps(CONTENT))
        data["journey"][-1]["program_id"] = "AU-GUARD-001"
        data["journey"][-1]["commercial_action"]["resolver_ref"] = "AU-GUARD-001"
        with self.assertRaisesRegex(SystemExit, "UK-bound"):
            run_case(data)

    def test_nonstandard_risk_class_rejected_for_first_slice(self):
        cta = json.loads(json.dumps(CTA))
        for item in cta["programs"]:
            if item["program_id"] == "UK-TECH-FIXTURE-001":
                item["risk_class"] = "REGULATED_FINANCE"
        with self.assertRaisesRegex(SystemExit, "STANDARD"):
            run_case(CONTENT, cta)

    def test_unverified_cta_state_rejected(self):
        cta = json.loads(json.dumps(CTA))
        for item in cta["programs"]:
            if item["program_id"] == "UK-TECH-FIXTURE-001":
                item["cta_state"] = "NON_AFFILIATE_FALLBACK"
        with self.assertRaisesRegex(SystemExit, "verified publisher"):
            run_case(CONTENT, cta)


if __name__ == "__main__":
    unittest.main()
