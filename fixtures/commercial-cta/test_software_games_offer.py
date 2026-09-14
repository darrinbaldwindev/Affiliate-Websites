import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from validate_software_games_offer import validate

BASE_PATH = Path(__file__).with_name("software-games-offers.synthetic.json")


def load_base():
    return json.loads(BASE_PATH.read_text(encoding="utf-8"))


def run_case(data):
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "fixture.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        out = io.StringIO()
        with redirect_stdout(out):
            validate(str(path))
        return json.loads(out.getvalue())


def offer(data, offer_id):
    return next(item for item in data["offers"] if item["offer_id"] == offer_id)


class SoftwareGamesOfferTests(unittest.TestCase):
    def test_base_fixture_passes_and_never_emits_tracking_url(self):
        result = run_case(load_base())
        self.assertEqual(result["status"], "PASS")
        self.assertTrue(all(row["tracking_url"] is None for row in result["decisions"]))

    def assert_blocks(self, offer_id, field, value):
        data = load_base()
        item = offer(data, offer_id)
        item[field] = value
        item["expected_decision"] = "ALLOWED"
        with self.assertRaisesRegex(SystemExit, "expected_decision"):
            run_case(data)

    def test_stale_price_cannot_be_marked_allowed(self):
        data = load_base(); offer(data, "AU-WINDOWS-STALE-001")["expected_decision"] = "ALLOWED"
        with self.assertRaisesRegex(SystemExit, "expected_decision"): run_case(data)

    def test_region_mismatch_fails_closed(self):
        self.assert_blocks("AU-GAME-AUTH-001", "offer_region", "US")

    def test_windows_unknown_licence_type_fails_closed(self):
        self.assert_blocks("US-WINDOWS-MARKET-001", "licence_type", "UNKNOWN")

    def test_office_missing_licence_type_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "licence_type", None)

    def test_unapproved_merchant_fails_closed(self):
        self.assert_blocks("AU-GAME-AUTH-001", "merchant_approval", "UNKNOWN")

    def test_marketplace_unknown_seller_fails_closed(self):
        self.assert_blocks("US-WINDOWS-MARKET-001", "seller_provenance", "UNKNOWN")

    def test_wrong_currency_fails_closed(self):
        self.assert_blocks("AU-GAME-AUTH-001", "currency", "USD")

    def test_missing_disclosure_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "disclosure_present", False)

    def test_transferability_unknown_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "transferability", "UNKNOWN")

    def test_account_binding_unknown_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "account_binding", "UNKNOWN")

    def test_device_install_count_unknown_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "device_install_count", None)

    def test_device_install_count_zero_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "device_install_count", 0)

    def test_activation_platform_unknown_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "activation_platform", "UNKNOWN")

    def test_product_family_unknown_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "product_family", "UNKNOWN")

    def test_edition_unknown_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "edition", "UNKNOWN")

    def test_equivalence_group_unknown_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "equivalence_group", "UNKNOWN")

    def test_equivalence_group_mismatch_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "equivalence_group", "OFFICE_2024|PRO_PLUS|RETAIL|1_DEVICE")

    def test_blocked_offer_cannot_leak_destination(self):
        data = load_base(); offer(data, "AU-WINDOWS-STALE-001")["destination_url"] = "https://example.invalid/should-not-publish"
        with self.assertRaisesRegex(SystemExit, "blocked offer"): run_case(data)

    def test_allowed_fixture_cannot_use_live_destination(self):
        data = load_base(); offer(data, "AU-GAME-AUTH-001")["destination_url"] = "https://merchant.example/live"
        with self.assertRaisesRegex(SystemExit, "example.invalid"): run_case(data)

    def test_non_positive_price_fails_closed(self):
        self.assert_blocks("UK-OFFICE-DIRECT-001", "price", 0)

    def test_duplicate_offer_id_rejected(self):
        data = load_base(); data["offers"][1]["offer_id"] = data["offers"][0]["offer_id"]
        with self.assertRaisesRegex(SystemExit, "duplicate"): run_case(data)


if __name__ == "__main__":
    unittest.main()
