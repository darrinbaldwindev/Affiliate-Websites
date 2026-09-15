# WordPress Presentation Payload Contract

**Status:** TEMPLATE CANDIDATE / NON-PRODUCTION INTERFACE CONTRACT  
**Scope:** Controlled Rewards API/read-model → WordPress presentation boundary  
**Canonical coordination:** `darrinbaldwindev/Overseer#49`

## Purpose

WordPress is the acquisition and presentation layer, not the canonical rewards database or commercial resolver. This contract defines the smallest payload WordPress may consume to render evidence state and a governed action boundary without duplicating canonical records or receiving raw tracking destinations.

## Response envelope

```json
{
  "schema": "affiliate.presentation.v1",
  "country": "AU",
  "entity_type": "program",
  "entity_id": "fixture-program",
  "display": {
    "state": "VERIFIED",
    "reason_codes": []
  },
  "commercial": {
    "state": "BLOCKED",
    "action": "join",
    "reason_codes": ["PUBLISHER_RELATIONSHIP_UNKNOWN"]
  },
  "evidence": {
    "verified_at": "2026-09-15",
    "freshness": "current"
  },
  "fixture": true
}
```

## Allowed presentation fields

- schema/version
- country
- stable entity type and ID
- governed display state
- reason codes suitable for non-sensitive presentation logic
- semantic commercial action
- commercial state (`BLOCKED`, `ELIGIBLE_FOR_RESOLUTION` or equivalent controlled status)
- evidence freshness/verification timestamps needed for user-visible trust state
- fixture/non-production marker where applicable

## Forbidden fields

The presentation payload must not contain:

- raw affiliate/tracking destination URLs;
- publisher/network credentials or IDs that are secrets;
- Supabase service-role credentials;
- internal approval tokens;
- raw commercial resolver secrets;
- unverified commission, earnings, price or availability claims;
- a consumer referral link presented as publisher affiliate approval.

## Fail-closed behavior

WordPress must render a non-affiliate/blocked action when any of the following is true:

1. the payload is missing or malformed;
2. country or entity identity does not match the requested context;
3. display state is conflicting/research-required/verification-due where policy blocks publication;
4. commercial state is blocked or unresolved;
5. publisher relationship is not independently eligible;
6. required disclosure/freshness/eligibility gates have not passed.

WordPress must not invent a destination, substitute another merchant/program, or infer publisher approval from consumer evidence.

## Commercial hand-off

When `commercial.state` indicates eligibility, WordPress may submit semantic context such as:

```json
{
  "country": "AU",
  "entity_type": "program",
  "entity_id": "fixture-program",
  "action": "join"
}
```

to the controlled commercial resolver. The resolver, not the editorial template or this presentation payload, determines whether a destination may be emitted.

## Canonical ownership

- PostgreSQL/Supabase remains the canonical structured store.
- Rewards API/read model owns canonical-to-presentation projection.
- Commercial resolver owns approved destination resolution.
- WordPress renders the supplied state and semantic action only.
- Country workstreams own country evidence; master owns this reusable boundary.

## Verification boundary

This document is an interface contract. It does not claim a live API endpoint, database migration, runtime WordPress integration, commercial resolver, click attribution, production affiliate relationship or production deployment.