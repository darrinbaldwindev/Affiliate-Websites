import json
from pathlib import Path

ROOT = Path(__file__).parents[2]
STAGING = ROOT / "data" / "au" / "surveys.staging.json"
PUBLICATION = ROOT / "data" / "au" / "surveys.publication-projection.json"
PRIORITY = ROOT / "data" / "au" / "surveys.priority-projection.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build():
    staging = load(STAGING)
    publication = {r["id"]: r for r in load(PUBLICATION)["records"]}
    priority = {r["id"]: r for r in load(PRIORITY)["records"]}
    records = []
    for source in staging["programs"]:
        pid = source["id"]
        pub = publication[pid]
        rank = priority[pid]
        records.append({
            "id": pid,
            "name": source["name"],
            "display_state": pub["display_state"],
            "tier": rank["tier"],
            "rank": rank["rank"],
            "participation_summary": source["consumer_claims"]["participation"],
            "reward_summary": source["consumer_claims"]["reward_summary"],
            "lifecycle_state": source["lifecycle_state"],
            "evidence_state": source["consumer_claims"]["evidence_state"],
            "freshness_state": source["freshness"]["state"],
            "last_verified_at": source["freshness"]["last_verified_at"],
            "review_due_at": source["freshness"]["review_due_at"],
            "commercial_state": pub["commercial_state"],
            "blocking_reasons": pub["reason_codes"],
            "commercial_action": None,
        })
    return sorted(records, key=lambda item: item["rank"])


if __name__ == "__main__":
    print(json.dumps({"records": build()}, indent=2))
