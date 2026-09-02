# Rewards API Boundary Contract

Status: Master implementation contract v0.1

## Principle

WordPress is the presentation/editorial layer. The Rewards API is the application boundary for structured opportunity intelligence. PostgreSQL/Supabase is the canonical persistence layer. AgentOS performs research, verification and monitoring but does not expose credentials to the browser.

## Read model

The frontend should be able to request:

- opportunities by country and category
- opportunity/program detail
- merchant/product detail where applicable
- comparison-ready fields
- evidence/source metadata
- current status and freshness
- approved commercial destination metadata

## Minimum opportunity response

```json
{
  "id": "stable-id",
  "country": "AU",
  "category": "surveys",
  "name": "Example Program",
  "status": "active",
  "summary": "Short factual description.",
  "eligibility": [],
  "reward": {},
  "requirements": [],
  "evidence": {
    "state": "VERIFIED",
    "source": "https://source.example/",
    "verified_at": "2026-09-03"
  },
  "commercial": {
    "available": true,
    "destination_id": "approved-destination-id"
  }
}
```

The example is a schema illustration only; no example program, commission, reward or destination should be published as real data.

## Commercial click flow

`visitor → country → program/product/merchant → eligibility → approved current commercial relationship → destination → tracked outbound click`

Editorial content must reference stable IDs or application data, not raw affiliate tracking URLs. Resolution and tracking remain server-side.

## Safety and integrity

- Never expose network credentials or tracking secrets to the browser.
- Never infer a current commission or eligibility rule from stale content.
- Preserve conflicting evidence for review rather than silently choosing one value.
- Record source, source type, observed/effective date, verification date, status, confidence and change history for volatile fields.
- If data is unavailable or stale, the UI should say so rather than fabricate certainty.
