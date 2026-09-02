# AU Vertical Slice — Fixture Contract

**Status:** TEMPLATE CANDIDATE / SAFE TEST DATA

## Purpose

Provide a deterministic, non-commercial fixture set for proving the AU journey without inventing live affiliate facts.

## Fixture entities

Use clearly synthetic identifiers:

- `fixture-au-cashback` — consumer opportunity
- `fixture-example-merchant` — merchant
- `fixture-affiliate-relationship` — publisher relationship
- `fixture-au-guide` — buying guide
- `fixture-au-comparison` — comparison

All fixture records must carry `fixture: true` and must never be presented as live recommendations.

## Required journey

`Global → AU → Cashback category → Guide/Comparison → Detail → Governed CTA`

The CTA must resolve to a test-safe blocked state unless a controlled non-production resolver is explicitly configured.

## Forbidden fixture data

Do not fabricate:

- real commissions
- real prices
- real availability
- real merchant terms
- real consumer earnings
- real tracking URLs
- claims that a merchant/program is verified

## Acceptance checks

- Country context remains AU throughout the journey.
- Canonical entity IDs are stable between pages and API requests.
- Detail pages expose evidence state explicitly.
- Commercial CTA contains context, not a production destination.
- Blocked/unresolved CTA state is understandable to users.
- No secret or service-role credential appears in theme/source content.

## Promotion gate

Fixtures are for architecture and interaction testing only. They must be replaced by individually verified country records before production publication.
