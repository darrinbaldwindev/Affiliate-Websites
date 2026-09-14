import json
import sys
from pathlib import Path

ALLOWED_COUNTRIES = {"AU", "UK", "US"}
ALLOWED_CTA_STATES = {"VERIFIED_PUBLISHER", "NON_AFFILIATE_FALLBACK", "UNKNOWN", "STALE"}
ALLOWED_RELATIONSHIPS = {"VERIFIED_PUBLISHER", "CONSUMER_REFERRAL_ONLY", "UNKNOWN"}
ALLOWED_FRESHNESS = {"CURRENT", "STALE", "UNKNOWN", "FIXTURE"}


def fail(message: str):
    raise SystemExit(f"FAIL: {message}")


def validate(path: str):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("fixture") is not True:
        fail("fixture marker must be true")

    countries = data.get("countries", [])
    if not isinstance(countries, list):
        fail("countries must be a list")
    if len(countries) != len(set(countries)):
        fail("countries must not contain duplicates")
    if set(countries) != ALLOWED_COUNTRIES:
        fail("fixture must cover AU, UK and US")

    programs = data.get("programs", [])
    if not isinstance(programs, list) or not programs:
        fail("fixture must contain at least one program per country")

    seen = set()
    represented_countries = set()
    for item in programs:
        pid = item.get("program_id")
        if not pid or pid in seen:
            fail("program_id missing or duplicate")
        seen.add(pid)

        country = item.get("country")
        if country not in ALLOWED_COUNTRIES:
            fail(f"{pid}: invalid country")
        represented_countries.add(country)

        if item.get("cta_state") not in ALLOWED_CTA_STATES:
            fail(f"{pid}: invalid cta_state")
        if not item.get("consumer_reward_evidence"):
            fail(f"{pid}: consumer reward evidence is required independently of publisher evidence")

        relationship = item.get("publisher_relationship")
        cta_state = item.get("cta_state")
        source = item.get("publisher_evidence_source")
        verified_at = item.get("publisher_verified_at")
        url = item.get("destination_url")
        freshness = item.get("evidence_freshness")

        if relationship not in ALLOWED_RELATIONSHIPS:
            fail(f"{pid}: invalid publisher_relationship")
        if freshness not in ALLOWED_FRESHNESS:
            fail(f"{pid}: invalid evidence_freshness")

        if relationship == "VERIFIED_PUBLISHER":
            if not source or not verified_at:
                fail(f"{pid}: verified publisher requires source and timestamp")
            if freshness not in {"CURRENT", "FIXTURE"}:
                fail(f"{pid}: verified publisher evidence must be current")
            if cta_state != "VERIFIED_PUBLISHER":
                fail(f"{pid}: verified publisher relationship must resolve to VERIFIED_PUBLISHER")
            if not isinstance(url, str) or not url.startswith("https://example.invalid/"):
                fail(f"{pid}: fixture verified CTA must use example.invalid only")
        else:
            if cta_state == "VERIFIED_PUBLISHER":
                fail(f"{pid}: non-verified relationship cannot resolve to publisher CTA")
            if source or verified_at:
                fail(f"{pid}: non-verified relationship cannot carry publisher verification evidence")
            if url:
                fail(f"{pid}: non-verified relationship cannot contain commercial destination URL")

        if relationship == "CONSUMER_REFERRAL_ONLY" and cta_state != "NON_AFFILIATE_FALLBACK":
            fail(f"{pid}: consumer referral evidence must remain non-affiliate fallback")

        if freshness in {"UNKNOWN", "STALE"} and cta_state == "VERIFIED_PUBLISHER":
            fail(f"{pid}: unknown/stale evidence cannot publish verified CTA")

    if represented_countries != ALLOWED_COUNTRIES:
        fail("fixture programs must represent AU, UK and US")

    print(f"PASS: validated {len(seen)} governed CTA fixtures")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        fail("usage: validate_country_cta.py <fixture.json>")
    validate(sys.argv[1])
