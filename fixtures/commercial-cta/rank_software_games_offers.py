from collections import defaultdict

ASSURANCE = {"AUTHORISED_RETAILER": 30, "DIRECT_RESELLER": 20, "MARKETPLACE": 10}
EVIDENCE = {"VERIFIED": 20, "FIXTURE_VERIFIED": 15, "CURRENT": 15}
PROVENANCE = {"NOT_APPLICABLE": 10, "DIRECT_MERCHANT": 10, "VERIFIED": 10}

COMMERCIAL_FIELDS = {
    "affiliate_commission_rate", "affiliate_bounty", "epc", "cookie_days",
    "payout_threshold", "network_bonus"
}


def identity_key(o):
    return (o.get("merchant_id"), o.get("source_sku"), o.get("offer_region"))


def detect_conflicts(offers):
    seen = {}
    conflicts = []
    material = (
        "product_family", "edition", "licence_type", "equivalence_group", "price", "currency",
        "transferability", "account_binding", "device_install_count", "activation_platform"
    )
    for o in offers:
        key = identity_key(o)
        if not all(key):
            conflicts.append((key, "IDENTITY_INCOMPLETE"))
            continue
        if key in seen:
            previous = seen[key]
            if any(previous.get(f) != o.get(f) for f in material):
                conflicts.append((key, "CONTRADICTORY_EVIDENCE"))
            else:
                conflicts.append((key, "DUPLICATE_IDENTITY"))
        else:
            seen[key] = o
    return conflicts


def eligible(offers):
    return [o for o in offers if o.get("publishable") is True and o.get("equivalence_group")]


def _assurance_score(o):
    return ASSURANCE.get(o.get("merchant_class"), 0) + EVIDENCE.get(o.get("evidence_state"), 0) + PROVENANCE.get(o.get("seller_provenance"), 0)


def _value_score(o):
    score = _assurance_score(o)
    if o.get("transferability") == "TRANSFERABLE":
        score += 8
    if o.get("account_binding") == "ACCOUNT_BOUND":
        score += 5
    count = o.get("device_install_count")
    if isinstance(count, int) and count > 0:
        score += min(count, 5)
    # price contributes only inside the already-normalized equivalence group
    price = o.get("price")
    if isinstance(price, (int, float)) and price > 0:
        score += 10 / price
    return score


def rank(offers, mode):
    conflicts = detect_conflicts(offers)
    if conflicts:
        raise ValueError(f"fail closed: {conflicts}")
    groups = defaultdict(list)
    for o in eligible(offers):
        groups[o["equivalence_group"]].append(o)
    ranked = {}
    for group, rows in groups.items():
        if mode == "lowest_observed_price":
            ranked[group] = sorted(rows, key=lambda o: (o["price"], -_assurance_score(o), o["offer_id"]))
        elif mode == "best_verified_value":
            ranked[group] = sorted(rows, key=lambda o: (-_value_score(o), o["price"], o["offer_id"]))
        elif mode == "highest_assurance":
            ranked[group] = sorted(rows, key=lambda o: (-_assurance_score(o), o["price"], o["offer_id"]))
        else:
            raise ValueError("unknown ranking mode")
    return ranked


def ranking_signature(offers, mode):
    ranked = rank(offers, mode)
    return {g: [o["offer_id"] for o in rows] for g, rows in ranked.items()}
