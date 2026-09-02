# WordPress → Rewards API Integration Seam

**Status:** TEMPLATE CANDIDATE / IMPLEMENTATION CONTRACT

## Purpose

Define a safe integration seam before a live Rewards API exists. The WordPress theme remains presentation-focused and must not contain credentials, raw affiliate tracking URLs, or commercial-resolution logic.

## Request model

A semantic commercial CTA supplies:

- country code
- entity type
- canonical entity ID
- requested action

Example:

```json
{
  "country": "AU",
  "entity_type": "program",
  "entity_id": "program-uuid",
  "action": "join"
}
```

## Server-side flow

```text
WordPress request
  → server-side resolver
  → Rewards API
  → country eligibility
  → consumer opportunity status
  → publisher relationship
  → verification/freshness gates
  → approved destination
  → auditable resolution event
```

The browser should receive only the minimum response required for the current interaction.

## Failure states

The integration must support explicit states rather than fallback redirects:

- `resolved`
- `blocked`
- `unavailable`
- `verification_required`
- `stale`
- `conflicting`
- `not_eligible`
- `configuration_error`

A failed resolution must not silently select another program or merchant.

## Secrets

- API credentials remain server-side.
- Service-role database credentials never enter theme files, page content or browser JavaScript.
- Environment configuration belongs outside version-controlled public source.
- Logs must avoid unnecessary personal data and secrets.

## Caching

Resolved commercial responses may be cached only according to freshness policy. Cache keys must include country and canonical entity/action context. Stale commercial responses must not bypass verification gates.

## Analytics

Record a resolution/audit event before redirect where the implementation permits. Separate page engagement from qualified commercial clicks. Do not require personally identifying data for the core attribution event.

## Current implementation boundary

This document defines the seam only. No live API endpoint, credentials, production destination or end-to-end redirect is claimed here.
