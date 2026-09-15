import html
import json
import sys
from pathlib import Path

BLOCKED_REASONS = {
    "STALE": "STALE_EVIDENCE",
    "UNKNOWN": "UNKNOWN_EVIDENCE",
    "NON_AFFILIATE_FALLBACK": "NO_VERIFIED_PUBLISHER_RELATIONSHIP",
}


def fail(message: str):
    raise SystemExit(f"FAIL: {message}")


def render(content_path: str, cta_path: str):
    content = json.loads(Path(content_path).read_text(encoding="utf-8"))
    cta = json.loads(Path(cta_path).read_text(encoding="utf-8"))
    if content.get("fixture") is not True or content.get("country") != "UK":
        fail("presentation input must be an explicit UK fixture")

    detail = next((item for item in content.get("journey", []) if item.get("type") == "detail"), None)
    if not detail:
        fail("detail presentation payload is required")
    program_id = detail.get("program_id")
    resolver_ref = detail.get("commercial_action", {}).get("resolver_ref")
    if not program_id or resolver_ref != program_id:
        fail("presentation must preserve exact program/resolver correlation")

    programs = {item.get("program_id"): item for item in cta.get("programs", [])}
    target = programs.get(program_id)
    if not target:
        fail("presentation resolver reference is absent from governed CTA data")
    if target.get("country") != "UK":
        fail("presentation cannot cross country boundary")

    state = target.get("cta_state")
    freshness = target.get("evidence_freshness")
    allowed = state == "VERIFIED_PUBLISHER" and freshness in {"CURRENT", "FIXTURE"}
    reason = "VERIFIED_SYNTHETIC_PUBLISHER" if allowed else BLOCKED_REASONS.get(state, f"CTA_STATE_{state}")
    if freshness == "STALE":
        allowed = False
        reason = "STALE_EVIDENCE"

    payload = {
        "country": "UK",
        "route": detail.get("route"),
        "pattern": detail.get("pattern"),
        "title": detail.get("title"),
        "evidence_state": detail.get("evidence_state"),
        "program_id": program_id,
        "resolver_ref": resolver_ref,
        "commercial_decision": "ALLOWED" if allowed else "BLOCKED",
        "commercial_reason": reason,
        "destination_url": target.get("destination_url") if allowed else None,
        "disclosure_required": detail.get("disclosure_required") is True,
    }
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        fail("usage: render_presentation.py <content_fixture.json> <cta_fixture.json>")
    render(sys.argv[1], sys.argv[2])
