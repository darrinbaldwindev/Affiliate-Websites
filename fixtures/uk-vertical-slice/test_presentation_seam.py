import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from render_presentation import render

ROOT = Path(__file__).resolve().parents[2]
CONTENT = json.loads((Path(__file__).parent / "technology-appliances.synthetic.json").read_text(encoding="utf-8"))
CTA = json.loads((ROOT / "fixtures/commercial-cta/uk-governance.synthetic.json").read_text(encoding="utf-8"))


def run_case(content, cta):
    with tempfile.TemporaryDirectory() as td:
        content_path = Path(td) / "content.json"
        cta_path = Path(td) / "cta.json"
        content_path.write_text(json.dumps(content), encoding="utf-8")
        cta_path.write_text(json.dumps(cta), encoding="utf-8")
        out = io.StringIO()
        with redirect_stdout(out):
            render(str(content_path), str(cta_path))
        return json.loads(out.getvalue())


class PresentationSeamTests(unittest.TestCase):
    def test_exact_program_correlation_is_preserved(self):
        result = run_case(CONTENT, CTA)
        self.assertEqual(result["program_id"], "UK-TECH-FIXTURE-001")
        self.assertEqual(result["resolver_ref"], result["program_id"])
        self.assertEqual(result["commercial_decision"], "ALLOWED")
        self.assertTrue(result["disclosure_required"])

    def test_missing_detail_fails_closed(self):
        content = json.loads(json.dumps(CONTENT))
        content["journey"] = [x for x in content["journey"] if x["type"] != "detail"]
        with self.assertRaisesRegex(SystemExit, "detail presentation payload"):
            run_case(content, CTA)

    def test_correlation_mismatch_fails_closed(self):
        content = json.loads(json.dumps(CONTENT))
        content["journey"][-1]["commercial_action"]["resolver_ref"] = "UK-OTHER"
        with self.assertRaisesRegex(SystemExit, "exact program/resolver correlation"):
            run_case(content, CTA)

    def test_unknown_program_fails_closed(self):
        content = json.loads(json.dumps(CONTENT))
        content["journey"][-1]["program_id"] = "UK-MISSING"
        content["journey"][-1]["commercial_action"]["resolver_ref"] = "UK-MISSING"
        with self.assertRaisesRegex(SystemExit, "absent from governed CTA"):
            run_case(content, CTA)

    def test_wrong_country_program_fails_closed(self):
        content = json.loads(json.dumps(CONTENT))
        content["journey"][-1]["program_id"] = "AU-GUARD-001"
        content["journey"][-1]["commercial_action"]["resolver_ref"] = "AU-GUARD-001"
        with self.assertRaisesRegex(SystemExit, "country boundary"):
            run_case(content, CTA)

    def test_stale_cta_never_exposes_destination(self):
        cta = json.loads(json.dumps(CTA))
        target = next(x for x in cta["programs"] if x["program_id"] == "UK-TECH-FIXTURE-001")
        target["cta_state"] = "STALE"
        target["evidence_freshness"] = "STALE"
        result = run_case(CONTENT, cta)
        self.assertEqual(result["commercial_decision"], "BLOCKED")
        self.assertEqual(result["commercial_reason"], "STALE_EVIDENCE")
        self.assertIsNone(result["destination_url"])

    def test_unapproved_cta_never_exposes_destination(self):
        cta = json.loads(json.dumps(CTA))
        target = next(x for x in cta["programs"] if x["program_id"] == "UK-TECH-FIXTURE-001")
        target["cta_state"] = "NON_AFFILIATE_FALLBACK"
        target["publisher_relationship"] = "UNKNOWN"
        target["destination_url"] = None
        target["destination_country"] = None
        target["publisher_evidence_source"] = None
        target["publisher_verified_at"] = None
        result = run_case(CONTENT, cta)
        self.assertEqual(result["commercial_decision"], "BLOCKED")
        self.assertEqual(result["commercial_reason"], "NO_VERIFIED_PUBLISHER_RELATIONSHIP")
        self.assertIsNone(result["destination_url"])


if __name__ == "__main__":
    unittest.main()
