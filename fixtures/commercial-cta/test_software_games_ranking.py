import copy
import unittest

from rank_software_games_offers import detect_conflicts, ranking_signature


def base_offers():
    common = {
        "country": "AU", "currency": "AUD", "category": "WINDOWS",
        "product_family": "WINDOWS_11", "edition": "PRO", "licence_type": "RETAIL",
        "equivalence_group": "WINDOWS_11|PRO|RETAIL|AU", "offer_region": "AU",
        "transferability": "TRANSFERABLE", "account_binding": "ACCOUNT_BOUND",
        "device_install_count": 1, "activation_platform": "MICROSOFT_ACCOUNT",
        "publishable": True, "evidence_state": "VERIFIED"
    }
    return [
        {**common, "offer_id": "AUTH-1", "merchant_id": "authorised", "source_sku": "A1",
         "merchant_class": "AUTHORISED_RETAILER", "seller_provenance": "NOT_APPLICABLE",
         "price": 249.0, "affiliate_commission_rate": 1.0},
        {**common, "offer_id": "DIRECT-1", "merchant_id": "direct", "source_sku": "D1",
         "merchant_class": "DIRECT_RESELLER", "seller_provenance": "DIRECT_MERCHANT",
         "price": 49.0, "affiliate_commission_rate": 8.0},
        {**common, "offer_id": "MARKET-1", "merchant_id": "market", "source_sku": "M1",
         "merchant_class": "MARKETPLACE", "seller_provenance": "VERIFIED",
         "price": 19.0, "affiliate_commission_rate": 25.0}
    ]


class SoftwareGamesRankingTests(unittest.TestCase):
    def test_lowest_price_is_price_order(self):
        sig = ranking_signature(base_offers(), "lowest_observed_price")
        self.assertEqual(sig["WINDOWS_11|PRO|RETAIL|AU"], ["MARKET-1", "DIRECT-1", "AUTH-1"])

    def test_highest_assurance_prefers_authorised(self):
        sig = ranking_signature(base_offers(), "highest_assurance")
        self.assertEqual(sig["WINDOWS_11|PRO|RETAIL|AU"][0], "AUTH-1")

    def test_commission_cannot_change_any_ranking(self):
        original = base_offers()
        poisoned = copy.deepcopy(original)
        poisoned[0]["affiliate_commission_rate"] = 0
        poisoned[1]["affiliate_commission_rate"] = 99
        poisoned[2]["affiliate_commission_rate"] = 1000000
        poisoned[2]["epc"] = 999999
        poisoned[2]["network_bonus"] = 999999
        for mode in ("lowest_observed_price", "best_verified_value", "highest_assurance"):
            self.assertEqual(ranking_signature(original, mode), ranking_signature(poisoned, mode))

    def test_non_equivalent_offer_cannot_compete_in_same_group(self):
        offers = base_offers()
        other = copy.deepcopy(offers[1])
        other["offer_id"] = "OEM-1"
        other["source_sku"] = "OEM1"
        other["licence_type"] = "OEM"
        other["equivalence_group"] = "WINDOWS_11|PRO|OEM|AU"
        offers.append(other)
        sig = ranking_signature(offers, "lowest_observed_price")
        self.assertIn("WINDOWS_11|PRO|OEM|AU", sig)
        self.assertNotIn("OEM-1", sig["WINDOWS_11|PRO|RETAIL|AU"])

    def test_duplicate_identity_fails_closed(self):
        offers = base_offers()
        offers.append(copy.deepcopy(offers[0]))
        self.assertTrue(any(reason == "DUPLICATE_IDENTITY" for _, reason in detect_conflicts(offers)))
        with self.assertRaisesRegex(ValueError, "fail closed"):
            ranking_signature(offers, "highest_assurance")

    def test_contradictory_same_sku_fails_closed(self):
        offers = base_offers()
        contradictory = copy.deepcopy(offers[0])
        contradictory["offer_id"] = "AUTH-1-CONFLICT"
        contradictory["price"] = 99.0
        offers.append(contradictory)
        self.assertTrue(any(reason == "CONTRADICTORY_EVIDENCE" for _, reason in detect_conflicts(offers)))
        with self.assertRaisesRegex(ValueError, "CONTRADICTORY_EVIDENCE"):
            ranking_signature(offers, "lowest_observed_price")

    def test_unpublishable_offer_excluded(self):
        offers = base_offers()
        offers[2]["publishable"] = False
        sig = ranking_signature(offers, "lowest_observed_price")
        self.assertNotIn("MARKET-1", sig["WINDOWS_11|PRO|RETAIL|AU"])


if __name__ == "__main__":
    unittest.main()
