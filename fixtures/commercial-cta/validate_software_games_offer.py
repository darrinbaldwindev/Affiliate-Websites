import json
import sys
from pathlib import Path

ALLOWED_COUNTRIES = {"AU", "UK", "US"}
CURRENCIES = {"AU": "AUD", "UK": "GBP", "US": "USD"}
ALLOWED_CATEGORIES = {"WINDOWS", "OFFICE", "PRODUCTIVITY", "ANTIVIRUS", "VPN", "UTILITY", "GAME", "GIFT_CARD", "SUBSCRIPTION"}
ALLOWED_MERCHANT_CLASSES = {"AUTHORISED_RETAILER", "DIRECT_RESELLER", "MARKETPLACE"}
REQUIRES_LICENCE_DETAIL = {"WINDOWS", "OFFICE", "PRODUCTIVITY"}


def fail(message: str):
    raise SystemExit(f"FAIL: {message}")


def _known(value):
    return value not in {None, "", "UNKNOWN"}


def evaluate_offer(item: dict):
    reasons = []
    country = item.get("country")
    category = item.get("category")
    merchant_class = item.get("merchant_class")

    if country not in ALLOWED_COUNTRIES:
        reasons.append("INVALID_COUNTRY")
    if category not in ALLOWED_CATEGORIES:
        reasons.append("INVALID_CATEGORY")
    if merchant_class not in ALLOWED_MERCHANT_CLASSES:
        reasons.append("INVALID_MERCHANT_CLASS")
    if item.get("merchant_approval") != "FIXTURE_VERIFIED":
        reasons.append("MERCHANT_NOT_APPROVED")
    if item.get("price_freshness") not in {"CURRENT", "FIXTURE"}:
        reasons.append("PRICE_NOT_CURRENT")
    if country in ALLOWED_COUNTRIES and item.get("offer_region") != country:
        reasons.append("REGION_MISMATCH")
    if country in CURRENCIES and item.get("currency") != CURRENCIES[country]:
        reasons.append("CURRENCY_MISMATCH")
    if not isinstance(item.get("price"), (int, float)) or item.get("price", 0) <= 0:
        reasons.append("INVALID_PRICE")
    if item.get("disclosure_present") is not True:
        reasons.append("DISCLOSURE_MISSING")
    if merchant_class == "MARKETPLACE" and item.get("seller_provenance") != "VERIFIED":
        reasons.append("MARKETPLACE_SELLER_UNVERIFIED")

    if category in REQUIRES_LICENCE_DETAIL:
        if not _known(item.get("licence_type")):
            reasons.append("LICENCE_TYPE_UNKNOWN")
        if not _known(item.get("transferability")):
            reasons.append("TRANSFERABILITY_UNKNOWN")
        if not _known(item.get("account_binding")):
            reasons.append("ACCOUNT_BINDING_UNKNOWN")
        installs = item.get("device_install_count")
        if not isinstance(installs, int) or isinstance(installs, bool) or installs <= 0:
            reasons.append("DEVICE_INSTALL_COUNT_UNKNOWN")
        if not _known(item.get("activation_platform")):
            reasons.append("ACTIVATION_PLATFORM_UNKNOWN")
        if not _known(item.get("product_family")):
            reasons.append("PRODUCT_FAMILY_UNKNOWN")
        if not _known(item.get("edition")):
            reasons.append("EDITION_UNKNOWN")
        if not _known(item.get("equivalence_group")):
            reasons.append("EQUIVALENCE_GROUP_UNKNOWN")
        elif _known(item.get("product_family")) and _known(item.get("edition")) and _known(item.get("licence_type")):
            expected_prefix = f"{item['product_family']}|{item['edition']}|{item['licence_type']}|"
            if not str(item.get("equivalence_group")).startswith(expected_prefix):
                reasons.append("EQUIVALENCE_GROUP_MISMATCH")

    decision = "BLOCKED" if reasons else "ALLOWED"
    return decision, reasons


def validate(path: str):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("fixture") is not True:
        fail("fixture marker must be true")
    if data.get("vertical") != "software-games":
        fail("vertical must be software-games")

    countries = data.get("countries", [])
    if not isinstance(countries, list) or set(countries) != ALLOWED_COUNTRIES or len(countries) != 3:
        fail("fixture must declare AU, UK and US exactly once")

    offers = data.get("offers", [])
    if not isinstance(offers, list) or not offers:
        fail("fixture must contain offers")

    seen = set()
    represented = set()
    decisions = []
    for item in offers:
        oid = item.get("offer_id")
        if not oid or oid in seen:
            fail("offer_id missing or duplicate")
        seen.add(oid)
        if item.get("country") in ALLOWED_COUNTRIES:
            represented.add(item.get("country"))

        decision, reasons = evaluate_offer(item)
        if item.get("expected_decision") != decision:
            fail(f"{oid}: expected_decision does not match computed {decision}: {','.join(reasons)}")

        url = item.get("destination_url")
        if decision == "ALLOWED":
            if not isinstance(url, str) or not url.startswith("https://example.invalid/"):
                fail(f"{oid}: allowed fixture offer requires example.invalid destination")
        elif url is not None:
            fail(f"{oid}: blocked offer must not contain destination URL")

        decisions.append({"offer_id": oid, "decision": decision, "reasons": reasons, "tracking_url": None})

    if represented != ALLOWED_COUNTRIES:
        fail("fixture offers must represent AU, UK and US")

    required_block_reasons = {
        "PRICE_NOT_CURRENT", "REGION_MISMATCH", "LICENCE_TYPE_UNKNOWN", "MERCHANT_NOT_APPROVED",
        "MARKETPLACE_SELLER_UNVERIFIED", "TRANSFERABILITY_UNKNOWN", "ACCOUNT_BINDING_UNKNOWN",
        "DEVICE_INSTALL_COUNT_UNKNOWN", "ACTIVATION_PLATFORM_UNKNOWN", "EQUIVALENCE_GROUP_MISMATCH",
    }
    observed = {reason for result in decisions for reason in result["reasons"]}
    missing = sorted(required_block_reasons - observed)
    if missing:
        fail(f"fixture must exercise required fail-closed reasons: {','.join(missing)}")

    print(json.dumps({"status": "PASS", "validated": len(seen), "decisions": decisions}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        fail("usage: validate_software_games_offer.py <fixture.json>")
    validate(sys.argv[1])
