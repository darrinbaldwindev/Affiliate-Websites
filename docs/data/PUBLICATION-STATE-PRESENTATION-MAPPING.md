# Publication State → Presentation Mapping

**Status:** TEMPLATE CANDIDATE / NON-PRODUCTION CONTRACT  
**Scope:** Master mapping between canonical evidence/lifecycle state and WordPress-facing presentation state.  
**Canonical coordination:** `darrinbaldwindev/Overseer#49`

## Purpose

WordPress needs a deterministic way to present evidence state without becoming a second source of truth. This contract maps canonical verification/freshness/commercial inputs to display semantics only.

The mapping does **not** store or resolve affiliate destinations, commissions, prices, earnings, referral terms or publisher approval.

## Inputs

The controlled Rewards layer supplies, at minimum:

```json
{
  "verification_status": "verified",
  "freshness_status": "current",
  "conflict": false,
  "publisher_relationship_status": "unknown",
  "commercial_resolution_status": "blocked"
}
```

## Deterministic mapping

| Canonical condition | WordPress display state | Commercial implication |
| --- | --- | --- |
| `conflict = true` or `verification_status = conflicting` | `CONFLICTING_INFORMATION` | blocked |
| `verification_status` in `research_required`, `claimed`, `unknown`, `rejected` | `RESEARCH_REQUIRED` | blocked |
| `freshness_status` in `stale`, `due`, `overdue` | `VERIFICATION_DUE` | blocked until policy permits current evidence |
| `verification_status = verified` and freshness is current | `VERIFIED` | **no affiliate approval implied** |
| commercial resolution is blocked/unresolved | `COMMERCIAL_ACTION_BLOCKED` may be shown alongside the evidence state | no destination |

Precedence is fail-closed: conflict → research required → freshness due → verified. Commercial state is evaluated independently and can remain blocked even when consumer evidence is verified.

## Separation rule

`VERIFIED` means the relevant consumer-facing evidence passed its verification gate. It does not mean:

- a publisher affiliate relationship exists;
- a consumer referral program is a publisher affiliate program;
- a commercial destination is approved;
- a commission/rate is known;
- the site may emit a tracked outbound URL.

Commercial eligibility requires the separate canonical publication/resolution gates defined by the Rewards data and Commercial CTA contracts.

## WordPress output

A presentation response may contain:

```json
{
  "entity_id": "program-uuid",
  "display_state": "VERIFIED",
  "commercial_state": "COMMERCIAL_ACTION_BLOCKED",
  "reason_codes": ["PUBLISHER_RELATIONSHIP_UNKNOWN"],
  "verified_at": "2026-09-15"
}
```

It must not contain a raw tracking URL. WordPress may render labels, explanatory copy and semantic CTA context from this projection, but it must not treat the projection as canonical data.

## Safety invariants

1. Unknown input fails closed to `RESEARCH_REQUIRED`.
2. Conflict cannot be silently downgraded to `VERIFIED`.
3. Stale evidence cannot be presented as current verified evidence.
4. Consumer verification cannot change publisher relationship status.
5. Commercial blocked/unresolved state cannot expose a destination.
6. Country workstreams own source evidence; master owns these reusable presentation semantics.
7. PostgreSQL/Supabase + Rewards API remain canonical; WordPress remains a presentation consumer.

## Verification boundary

This is a mapping/interface contract. It does not claim a live Rewards API, database migration, runtime WordPress binding, destination resolver or click attribution implementation.