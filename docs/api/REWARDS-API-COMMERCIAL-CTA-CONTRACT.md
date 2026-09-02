# Rewards API — Commercial CTA Contract

**Status:** TEMPLATE CANDIDATE / INTERFACE CONTRACT

## Purpose
Define the boundary between WordPress presentation and the canonical rewards/commercial system.

## Request
A frontend CTA should identify the context, not carry a raw tracking URL:

```json
{
  "country": "AU",
  "entity_type": "program",
  "entity_id": "example-id",
  "action": "join"
}
```

## Resolution responsibilities
The governed commercial layer resolves:
- current country eligibility
- active consumer opportunity/program
- applicable publisher affiliate relationship
- approved destination
- tracking/attribution parameters
- commercial status
- verification/freshness state

## Response contract
Conceptual response:

```json
{
  "status": "verified",
  "destination": "https://approved-destination.example/",
  "display_action": "Join & Earn",
  "disclosure_required": true,
  "verified_at": "2026-09-03"
}
```

The destination above is illustrative only and must never be used as a live affiliate URL.

## Safety rules
- Never expose internal API credentials in browser code.
- Never hard-code production tracking URLs into editorial templates.
- Reject inactive, suspended, unverified or stale commercial relationships according to policy.
- Do not silently substitute a different merchant/program when resolution fails.
- Preserve an auditable resolution event for qualified outbound clicks.
- Country eligibility must be checked before commercial resolution.

## WordPress integration
The theme may provide a semantic CTA component/pattern. The actual destination is supplied by the controlled API layer or an equivalent server-side resolver.

## Verification boundary
This is an interface contract, not a live API implementation. End-to-end destination resolution and click attribution remain unverified until a controlled backend is connected.
