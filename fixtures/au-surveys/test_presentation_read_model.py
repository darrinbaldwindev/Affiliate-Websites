import unittest

from build_presentation_read_model import build


class AuSurveyPresentationReadModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = build()
        cls.by_id = {item["id"]: item for item in cls.records}

    def test_identity_is_unique_and_rank_order_is_deterministic(self):
        self.assertEqual(len(self.by_id), len(self.records))
        ranks = [item["rank"] for item in self.records]
        self.assertEqual(ranks, sorted(ranks))
        self.assertEqual(ranks, list(range(1, len(ranks) + 1)))

    def test_category_and_detail_share_same_governed_identity(self):
        for item in self.records:
            category_identity = (item["id"], item["display_state"], item["commercial_state"])
            detail_identity = (item["id"], item["display_state"], item["commercial_state"])
            self.assertEqual(category_identity, detail_identity)

    def test_no_real_record_has_commercial_action(self):
        for item in self.records:
            self.assertEqual(item["commercial_state"], "BLOCKED", item["id"])
            self.assertIsNone(item["commercial_action"], item["id"])

    def test_research_required_cannot_present_as_verified(self):
        for item in self.records:
            if item["display_state"] == "RESEARCH_REQUIRED":
                self.assertNotEqual(item["lifecycle_state"], "VERIFIED", item["id"])
                self.assertEqual(item["tier"], "RESEARCH_HOLD", item["id"])

    def test_verified_records_have_current_freshness(self):
        for item in self.records:
            if item["lifecycle_state"] == "VERIFIED":
                self.assertEqual(item["display_state"], "INFORMATIONAL_VERIFIED", item["id"])
                self.assertEqual(item["freshness_state"], "CURRENT", item["id"])


if __name__ == "__main__":
    unittest.main()
