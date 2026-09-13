# AU Governed CTA Resolution — Deterministic Test Matrix

**Status:** TEMPLATE CANDIDATE / NON-PRODUCTION ACCEPTANCE CONTRACT  
**Scope:** Affiliate-Websites issue #8 AU vertical slice  
**Runtime boundary:** Static/source-level only. This does not prove a live WordPress, affiliate-network, tracking or backend integration.

## Purpose

Define the smallest deterministic acceptance surface for the reusable AU journey:

`AU category -> comparison/guide -> program detail -> governed CTA resolver`

The WordPress layer supplies context only. It must not embed raw affiliate/tracking URLs or infer publisher monetisation from consumer referral/reward evidence.

## Resolver input contract

A CTA request must carry:

```json
{
  "country": "AU",
  "entity_type": "program",
  "entity_id": "fixture-au-cashback",
  "action": "join",
  "placement": "program-detail-primary",
  "relationship_state": "UNKNOWN",
  "evidence_state": "RESEARCHED",
  "fixture": true
}
```

`placement`, `relationship_state`, `evidence_state` and `fixture` are required acceptance metadata for the vertical slice even where a later production API uses a different internal representation.

## Deterministic resolution cases

| Case | Publisher relationship | Evidence/freshness | Expected CTA state | Destination rule | Click event |
|---|---|---|---|---|---|
| A | VERIFIED | current | `commercial-approved` | controlled resolver may return an approved destination | record country/entity/placement/relationship state; no secrets |
| B | UNKNOWN | any | `non-affiliate-fallback` | canonical non-affiliate destination only, or no outbound CTA | record fallback reason; no secrets |
| C | NOT_AVAILABLE | any | `blocked` | no affiliate destination | record blocked reason; no secrets |
| D | VERIFIED | stale | `non-affiliate-fallback` | fail closed from affiliate monetisation | record stale reason; no secrets |
| E | consumer-referral-only | current | `non-affiliate-fallback` | consumer referral URL must not populate publisher destination | record separation reason; no secrets |
| F | VERIFIED | current, but country ineligible | `blocked` | no destination | record eligibility failure; no secrets |
| G | missing entity or country context | any | `blocked` | no destination and no silent substitution | validation error only |
| H | fixture data | any | `blocked-test-safe` | never return production affiliate/tracking destination | optional test event only; clearly marked fixture |

## Disclosure acceptance

For any rendered CTA decision point:

- disclosure state must be visible before or at interaction;
- `commercial-approved` must state that the site may earn from the relationship;
- fallback/blocked states must not imply a commercial relationship;
- consumer reward/referral language must remain separate from publisher-affiliate disclosure;
- stale/unknown evidence must never be worded as a current verified offer.

## Click-event contract

Permitted non-secret event fields:

```json
{
  "event": "commercial_cta_resolution",
  "country": "AU",
  "entity_type": "program",
  "entity_id": "fixture-au-cashback",
  "placement": "program-detail-primary",
  "resolution_state": "blocked-test-safe",
  "relationship_state": "UNKNOWN",
  "fixture": true
}
```

Forbidden event fields include credentials, service-role tokens, private network IDs, secret signing material and raw unapproved tracking URLs.

## Source/static acceptance checklist

- [ ] Country remains `AU` from category through resolver input.
- [ ] Stable `entity_id` survives comparison -> detail -> CTA context.
- [ ] Unknown, stale and consumer-referral-only cases fail closed from publisher monetisation.
- [ ] Ineligible country state cannot resolve a destination.
- [ ] Missing context cannot silently resolve a different entity.
- [ ] Fixture records can never resolve production destinations.
- [ ] Editorial/theme source contains no raw production tracking URL.
- [ ] Click-event schema contains only non-secret context.
- [ ] Disclosure is represented at the decision point.
- [ ] Static/source validation is not described as live browser/backend verification.

## Promotion gate

A real AU program may replace a fixture only after its consumer proposition, AU eligibility, publisher relationship, destination authority, evidence source and freshness are individually verified. A visible reward, consumer referral offer or payout is not evidence of an active publisher affiliate relationship.
