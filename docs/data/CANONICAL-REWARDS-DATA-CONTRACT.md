# Canonical Rewards Data Contract

**Status:** TEMPLATE CANDIDATE / IMPLEMENTATION CONTRACT  
**Scope:** Master schema for country-aware rewards intelligence and governed commercial resolution.

## 1. Design rules

The canonical model separates consumer opportunity data from publisher monetisation data. A record is not publishable merely because an affiliate relationship exists.

Every material commercial claim must carry evidence, verification and freshness metadata. Conflicting source claims are retained as conflicts rather than silently overwritten.

Recommended lifecycle:

`CONCEPT → RESEARCHED → VERIFIED → PUBLISHABLE → PUBLISHED → MONITORED`

## 2. Consumer program / opportunity

Stable identity for the consumer-facing opportunity.

```json
{
  "id": "program-uuid",
  "type": "consumer_reward_program",
  "name": "Example Program",
  "brand": "Example Brand",
  "reward_types": ["cashback"],
  "countries": ["AU"],
  "categories": ["cashback"],
  "eligibility": {},
  "status": "active",
  "evidence": [],
  "updated_at": "2026-09-03"
}
```

`status` is controlled data, not an editorial opinion. Examples: `active`, `paused`, `suspended`, `withdrawn`, `unknown`.

## 3. Merchant

```json
{
  "id": "merchant-uuid",
  "name": "Example Merchant",
  "website": "https://example.invalid/",
  "countries": ["AU"],
  "categories": ["retail"],
  "status": "active",
  "evidence": []
}
```

The example domain is non-production and must never be treated as a destination.

## 4. Consumer/user referral relationship

This is distinct from the publisher affiliate relationship.

```json
{
  "id": "referral-uuid",
  "program_id": "program-uuid",
  "benefit_type": "user_referral",
  "terms": {},
  "countries": ["AU"],
  "status": "unknown",
  "evidence": []
}
```

## 5. Publisher affiliate relationship

Represents the site's commercial relationship with a program/merchant.

```json
{
  "id": "affiliate-relationship-uuid",
  "program_id": "program-uuid",
  "merchant_id": "merchant-uuid",
  "network": "example-network",
  "country": "AU",
  "commission": {
    "type": "unknown",
    "value": null,
    "currency": null
  },
  "tracking_period": null,
  "restrictions": [],
  "status": "unknown",
  "terms_url": null,
  "evidence": []
}
```

Commission values are nullable because absence of a verified value is preferable to fabrication. Network presence alone does not establish merchant-level suitability or a current relationship.

## 6. Commercial offer / destination

The approved commercial action resolved at request time.

```json
{
  "id": "offer-uuid",
  "affiliate_relationship_id": "affiliate-relationship-uuid",
  "country": "AU",
  "action": "join",
  "destination": null,
  "status": "unresolved",
  "expires_at": null,
  "evidence": []
}
```

Raw production tracking URLs must not be stored in WordPress editorial content or exposed to unauthorised browser code. A controlled resolver may return an approved destination after eligibility, relationship, status and freshness checks.

## 7. Evidence / verification / freshness

Reusable metadata attached to material claims and relationships.

```json
{
  "source": "https://source.example.invalid/",
  "source_type": "primary",
  "claim": "Example claim",
  "verified_at": "2026-09-03",
  "effective_from": null,
  "effective_to": null,
  "freshness_due": null,
  "verification_status": "research_required",
  "confidence": "unknown",
  "notes": null
}
```

Allowed verification states should include at least:
- `research_required`
- `claimed`
- `verified`
- `conflicting`
- `stale`
- `rejected`
- `unknown`

Confidence is evidence quality, not certainty of commercial performance.

## 8. Change history

Material changes should be append-only events where practical:

```json
{
  "entity_type": "affiliate_relationship",
  "entity_id": "affiliate-relationship-uuid",
  "field": "commission",
  "previous_value": null,
  "new_value": null,
  "changed_at": "2026-09-03",
  "source": "primary",
  "reason": "verification_update"
}
```

Do not destroy prior verified states when a later source creates a conflict.

## 9. Commercial resolution / audit event

```json
{
  "event_id": "event-uuid",
  "occurred_at": "2026-09-03T00:00:00Z",
  "country": "AU",
  "entity_type": "program",
  "entity_id": "program-uuid",
  "action": "join",
  "affiliate_relationship_id": "affiliate-relationship-uuid",
  "resolution_status": "blocked",
  "reason": "verification_required"
}
```

Audit events should record the decision without unnecessarily storing personal information.

## 10. Minimum publication gate

A commercial record is publishable only when:

1. the consumer opportunity identity is known;
2. country eligibility is supported by current evidence;
3. the consumer-facing claim is supported;
4. the publisher relationship is independently established where required;
5. the commercial destination is approved by the resolver;
6. verification/freshness requirements are satisfied;
7. required disclosure is present; and
8. no unresolved conflict invalidates the intended claim.

If a gate fails, show a safe non-commercial state or withhold the commercial CTA. Never substitute a different opportunity silently.

## 11. API boundary

PostgreSQL/Supabase is the canonical data store. The Rewards API is the controlled business-logic boundary. WordPress consumes approved presentation data and semantic commercial actions; it does not become the system of record.

AgentOS may research and stage changes, but production merges must pass the project's verification/governance controls.

## 12. Fixture policy

Development fixtures must be explicitly marked as fixtures and must not contain invented live commissions, prices, availability or tracking URLs. Example domains and UUIDs in this document are illustrative only.

**Status:** Contract ready for implementation review. Database migrations, API endpoints, authentication and live records are separate implementation work and are not claimed by this document.
