# Software & Games Vertical Autonomous Batch 002 — 2026-09-14

**Workstream:** Master Affiliate Websites / cross-country commercial research  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Mode:** vertical autonomous execution  
**Status:** IN EXECUTION  
**Rule:** reuse the canonical commercial CTA seam; synthetic fixtures never become production merchant truth.

## Fresh scan baseline

Fresh repository scan on 2026-09-14 confirmed:

- `fixtures/commercial-cta/` is the canonical bounded commercial CTA test seam;
- `validate_country_cta.py` already enforces AU/UK/US coverage, publisher evidence, disclosure, freshness and non-live synthetic URLs;
- `test_country_cta.py` already exercises negative fail-closed cases;
- `.github/workflows/commercial-cta-fixture.yml` runs fixture validation and negative tests on relevant changes;
- Software & Games governance artifacts from Batch 001 are present on `main`;
- no separate Software & Games runtime, resolver, affiliate store or country fork should be created.

## Objective

Extend the existing governed commercial CTA fixture seam with Software & Games offer-level decision logic covering:

1. stale price/evidence;
2. country/region mismatch;
3. missing or unknown licence type for Windows/Office/productivity offers;
4. unapproved merchant relationship;
5. marketplace seller/provenance uncertainty;
6. incorrect country currency;
7. missing disclosure;
8. unsafe/live fixture destination URLs.

## Tasks

### SG2-1 — Fresh repo reconciliation — COMPLETE

Canonical fixture, tests and CI workflow inspected before any mutation.

### SG2-2 — Synthetic Software & Games comparison fixture — IN EXECUTION

Add AU/UK/US fixture offers with both publishable and deliberately blocked cases. No real prices, tracking parameters or live commercial destinations.

### SG2-3 — Deterministic fail-closed offer evaluator — IN EXECUTION

Add a bounded validator that computes ALLOWED/BLOCKED from evidence rather than trusting input labels.

### SG2-4 — Negative assurance tests — IN EXECUTION

Cover stale evidence, wrong region, unknown licence type, unapproved merchant, uncertain marketplace provenance, currency mismatch, disclosure omission and URL leakage.

### SG2-5 — Existing CI extension — IN EXECUTION

Extend `.github/workflows/commercial-cta-fixture.yml`; do not create a parallel workflow unless technically required.

### SG2-6 — AU/UK/US authorised benchmark research — OPEN

Research stable authorised software/game benchmark merchants separately from resellers/marketplaces. Record sources and country scope; do not infer affiliate approval.

### SG2-7 — Feed/API automation suitability — OPEN

Confirm which merchants provide stable catalogue/feed/API mechanisms and what freshness/terms constraints must be represented in canonical commercial data.

### SG2-8 — Verification and closure — OPEN

Re-scan resulting repository state and available CI evidence, then update this batch with exact commits, remaining blockers and next vertical slice.

## Hard rules

- No production affiliate URLs or credentials.
- Fixture URLs must use `example.invalid`.
- Cheapest observed price is not a trust or recommendation claim.
- Marketplace brand trust cannot substitute for underlying seller provenance.
- Windows/Office/productivity comparisons require licence type before publication.
- Wrong-country offers and wrong-country currencies fail closed.
- Synthetic approval is fixture evidence only; it is never evidence of a real merchant relationship.
- Reuse the existing commercial CTA architecture.
