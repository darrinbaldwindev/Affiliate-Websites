#!/usr/bin/env python3
import json
from pathlib import Path

REQUIRED = {
    "country", "entity_type", "entity_id", "action", "placement",
    "relationship_state", "evidence_state", "country_eligible", "fixture"
}


def resolve(case):
    data = case["input"]
    missing = REQUIRED - data.keys()
    if missing:
        return {"resolution_state": "blocked", "destination_kind": "none", "affiliate_allowed": False}
    if data["fixture"]:
        return {"resolution_state": "blocked-test-safe", "destination_kind": "none", "affiliate_allowed": False}
    if not data["country_eligible"]:
        return {"resolution_state": "blocked", "destination_kind": "none", "affiliate_allowed": False}
    if data["relationship_state"] in {"UNKNOWN", "CONSUMER_REFERRAL_ONLY"}:
        return {"resolution_state": "non-affiliate-fallback", "destination_kind": "canonical-non-affiliate", "affiliate_allowed": False}
    if data["evidence_state"] != "CURRENT":
        return {"resolution_state": "non-affiliate-fallback", "destination_kind": "canonical-non-affiliate", "affiliate_allowed": False}
    if data["relationship_state"] == "VERIFIED":
        return {"resolution_state": "commercial-approved", "destination_kind": "governed-approved", "affiliate_allowed": True}
    return {"resolution_state": "blocked", "destination_kind": "none", "affiliate_allowed": False}


def main():
    fixture_path = Path(__file__).parent / "fixtures" / "au-cta-resolution-cases.json"
    payload = json.loads(fixture_path.read_text(encoding="utf-8"))
    failures = []
    for case in payload["cases"]:
        actual = resolve(case)
        if actual != case["expected"]:
            failures.append((case["id"], case["expected"], actual))
    if failures:
        for case_id, expected, actual in failures:
            print(f"FAIL {case_id}: expected={expected} actual={actual}")
        raise SystemExit(1)
    print(f"PASS {len(payload['cases'])} AU CTA fail-closed cases")


if __name__ == "__main__":
    main()
