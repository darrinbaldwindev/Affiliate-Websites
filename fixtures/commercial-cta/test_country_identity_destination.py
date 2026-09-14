import json
import unittest

from test_country_cta import BASE, run_case


class CountryIdentityDestinationTests(unittest.TestCase):
    def test_program_identity_must_match_declared_country(self):
        data = json.loads(json.dumps(BASE))
        data["programs"][1]["program_id"] = "US-SYNTH-999"
        with self.assertRaisesRegex(SystemExit, "program_id must be bound to declared country"):
            run_case(data)

    def test_duplicate_verified_synthetic_destination_rejected(self):
        data = json.loads(json.dumps(BASE))
        duplicate = json.loads(json.dumps(data["programs"][1]))
        duplicate["program_id"] = "UK-SYNTH-002"
        data["programs"].append(duplicate)
        with self.assertRaisesRegex(SystemExit, "duplicate verified synthetic destination"):
            run_case(data)

    def test_verified_synthetic_destination_rejects_query_or_fragment(self):
        for suffix in ("?campaign=synthetic", "#fragment"):
            data = json.loads(json.dumps(BASE))
            data["programs"][1]["destination_url"] = f"https://example.invalid/fixture-affiliate{suffix}"
            with self.assertRaisesRegex(SystemExit, "canonical example.invalid path"):
                run_case(data)

    def test_audit_output_is_deterministic_under_program_permutation(self):
        baseline = run_case(BASE)
        data = json.loads(json.dumps(BASE))
        data["programs"] = list(reversed(data["programs"]))
        permuted = run_case(data)
        self.assertEqual(permuted, baseline)
        self.assertEqual(
            [event["program_id"] for event in permuted["audit_events"]],
            sorted(event["program_id"] for event in permuted["audit_events"]),
        )


if __name__ == "__main__":
    unittest.main()
