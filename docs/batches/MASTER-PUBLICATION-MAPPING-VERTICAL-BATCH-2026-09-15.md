# Master Publication Mapping Vertical Batch — 2026-09-15

**Status:** EXECUTED / CI PENDING  
**Branch:** `work/master-publication-mapping-vertical-batch-2026-09-15`  
**Baseline main:** `d3cf400aabe631dc6c2e37193eca8b192856eaba`  
**Canonical coordination:** `darrinbaldwindev/Overseer#49`

## Fresh scan

- Current `main` was scanned before execution.
- The canonical rewards contract already defines evidence/verification/freshness and keeps consumer opportunity data separate from publisher monetisation.
- The Commercial CTA contract already keeps raw tracking URLs outside editorial templates and delegates destination resolution to the governed commercial layer.
- The missing master dependency was a deterministic machine-readable presentation mapping between canonical state and WordPress display semantics.

## Vertical objective

`canonical evidence state → deterministic display state → independent commercial state → synthetic negative cases → CI`

## Executed

1. Added `docs/data/PUBLICATION-STATE-PRESENTATION-MAPPING.md`.
2. Added a synthetic non-production mapping matrix at `fixtures/master/publication-state-mapping.synthetic.json`.
3. Added automated fail-closed tests at `fixtures/master/test_publication_state_mapping.py`.
4. Wired those tests into the existing Commercial CTA fixture workflow rather than creating a duplicate workflow/control plane.
5. Preserved conflict precedence, stale-evidence blocking, unknown fail-closed behavior, and consumer-verification/publisher-approval separation.

## Safety

- No tracking URLs in the fixture.
- No real programs, commissions, rates, earnings, prices or affiliate relationships.
- `VERIFIED` consumer evidence never makes the commercial state eligible.
- Commercial state remains independently blocked in the synthetic matrix.
- WordPress remains a presentation consumer; PostgreSQL/Supabase + Rewards API remain canonical.

## Verification boundary

Completion-for-scope requires exact-head Commercial CTA fixture CI success. Runtime WordPress/API binding, live database state, resolver behavior and click attribution are not claimed.

## Next safe dependent step

After exact-head CI, define a bounded WordPress/API presentation payload contract that consumes this mapping without duplicating canonical records or exposing destinations, then exercise it against synthetic fixtures only.