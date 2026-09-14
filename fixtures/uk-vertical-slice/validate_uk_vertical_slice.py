import json
import sys
from pathlib import Path

ALLOWED_PATTERNS = {
    "category": "affiliate-master/category-page",
    "comparison": "affiliate-master/comparison-page",
    "buying-guide": "affiliate-master/buying-guide",
    "detail": "affiliate-master/detail-page",
}
FORBIDDEN_KEYS = {"commission", "price", "sale_price", "stock", "cookie_days", "tracking_url", "affiliate_url", "live_destination"}


def fail(message: str):
    raise SystemExit(f"FAIL: {message}")


def walk_forbidden(value, path="root"):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_KEYS:
                fail(f"forbidden live field {key} at {path}")
            walk_forbidden(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            walk_forbidden(child, f"{path}[{index}]")


def validate(content_path: str, cta_path: str):
    content = json.loads(Path(content_path).read_text(encoding="utf-8"))
    cta = json.loads(Path(cta_path).read_text(encoding="utf-8"))

    if content.get("fixture") is not True or content.get("country") != "UK":
        fail("vertical slice must be an explicit UK fixture")
    walk_forbidden(content)

    category = content.get("category", {})
    if category.get("route") != "/uk/technology-appliances/":
        fail("category route must use the canonical UK technology-appliances path")
    if category.get("pattern") != ALLOWED_PATTERNS["category"]:
        fail("category must reuse the shared category-page pattern")
    if not category.get("trust_signal"):
        fail("category trust signal is required")

    journey = content.get("journey", [])
    expected_types = ["category", "comparison", "buying-guide", "detail"]
    if [item.get("type") for item in journey] != expected_types:
        fail("journey must contain category, comparison, buying-guide and detail in canonical order")

    routes = set()
    for item in journey:
        item_type = item.get("type")
        route = item.get("route")
        if not isinstance(route, str) or not route.startswith("/uk/technology-appliances/"):
            fail(f"{item_type}: route must remain inside UK technology-appliances")
        if route in routes:
            fail("journey routes must be unique")
        routes.add(route)
        if item.get("pattern") != ALLOWED_PATTERNS[item_type]:
            fail(f"{item_type}: must reuse shared master pattern")

    detail = journey[-1]
    if detail.get("evidence_state") != "FIXTURE":
        fail("detail evidence state must remain FIXTURE")
    if detail.get("disclosure_required") is not True:
        fail("detail must require affiliate disclosure")

    action = detail.get("commercial_action", {})
    if action.get("pattern") != "affiliate-master/commercial-cta":
        fail("detail must use the shared governed commercial CTA pattern")
    program_id = detail.get("program_id")
    if not program_id or action.get("resolver_ref") != program_id:
        fail("detail and commercial resolver reference must use the same program_id")

    programs = {item.get("program_id"): item for item in cta.get("programs", [])}
    target = programs.get(program_id)
    if not target:
        fail("referenced program_id is absent from governed CTA fixture")
    if target.get("country") != "UK":
        fail("referenced CTA program must be UK-bound")
    if target.get("risk_class") != "STANDARD":
        fail("first UK technology slice must use STANDARD risk class")
    if target.get("cta_state") != "VERIFIED_PUBLISHER":
        fail("fixture detail expects a synthetic verified publisher CTA")
    if target.get("destination_country") != "UK":
        fail("fixture commercial destination must be country-bound to UK")

    print(json.dumps({
        "status": "PASS",
        "country": "UK",
        "category": category.get("slug"),
        "routes_validated": len(routes),
        "resolver_ref": program_id,
        "live_commercial_fields": 0,
    }, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        fail("usage: validate_uk_vertical_slice.py <content_fixture.json> <cta_fixture.json>")
    validate(sys.argv[1], sys.argv[2])
