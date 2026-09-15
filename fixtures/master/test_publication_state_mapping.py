import json
from pathlib import Path

FIXTURE = Path(__file__).with_name("publication-state-mapping.synthetic.json")


def derive(case):
    data = case["input"]
    verification = data.get("verification_status", "unknown")
    freshness = data.get("freshness_status", "unknown")
    conflict = bool(data.get("conflict")) or verification == "conflicting"

    if conflict:
        display = "CONFLICTING_INFORMATION"
    elif verification in {"research_required", "claimed", "unknown", "rejected"}:
        display = "RESEARCH_REQUIRED"
    elif freshness in {"stale", "due", "overdue"}:
        display = "VERIFICATION_DUE"
    elif verification == "verified" and freshness == "current":
        display = "VERIFIED"
    else:
        display = "RESEARCH_REQUIRED"

    commercial = "COMMERCIAL_ACTION_BLOCKED"
    return {"display_state": display, "commercial_state": commercial}


def test_fixture_is_non_production_and_has_no_urls():
    raw = FIXTURE.read_text(encoding="utf-8")
    data = json.loads(raw)
    assert data["fixture"] is True
    assert data["production_use"] is False
    assert data["contains_tracking_urls"] is False
    assert "http://" not in raw
    assert "https://" not in raw


def test_cases_match_fail_closed_mapping():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    for case in data["cases"]:
        assert derive(case) == case["expected"], case["id"]


def test_consumer_verified_does_not_imply_commercial_eligibility():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    case = next(c for c in data["cases"] if c["id"] == "verified-consumer-commercial-blocked")
    assert derive(case)["display_state"] == "VERIFIED"
    assert case["input"]["publisher_relationship_status"] == "unknown"
    assert derive(case)["commercial_state"] == "COMMERCIAL_ACTION_BLOCKED"


def test_conflict_precedes_verified():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    case = next(c for c in data["cases"] if c["id"] == "conflict-wins")
    assert derive(case)["display_state"] == "CONFLICTING_INFORMATION"
