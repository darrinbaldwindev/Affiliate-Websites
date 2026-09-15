# UK Vertical Autonomous Batch — 2026-09-15 B

**Workstream:** United Kingdom Affiliate Website
**Repository:** `darrinbaldwindev/Affiliate-Websites`
**Mode:** vertical autonomous execution
**Status:** COMPLETE — fixture-to-presentation assurance slice
**Rule:** evidence controls completion; WordPress remains presentation, not canonical commercial truth.

## Fresh scan

`main` was re-scanned before mutation at `d3cf400aabe631dc6c2e37193eca8b192856eaba`. The existing UK technology/appliances fixture already mapped category → comparison → buying guide → detail → shared commercial CTA, and the master theme remained deliberately generic.

The highest-value gap was the boundary between approved structured fixture data and presentation: exact program/resolver correlation, missing payload behaviour, country isolation and stale/unapproved commercial suppression.

## B15 — Governed fixture-to-presentation seam — COMPLETE

Created `fixtures/uk-vertical-slice/render_presentation.py`.

The bounded adapter consumes the UK content fixture and the shared governed CTA fixture, then emits a presentation payload containing route, pattern, title, evidence state, exact `program_id`/`resolver_ref`, disclosure requirement, commercial decision/reason and a destination only when the synthetic CTA is currently allowed.

It fails closed when the detail payload is missing, correlation differs, the resolver target is absent or the target crosses the UK country boundary.

Commit: `b24e1b9ab8c61ee21e1f00d6bea9dd2f5e25936e`

## B16 — Presentation negative assurance — COMPLETE

Created `fixtures/uk-vertical-slice/test_presentation_seam.py`.

Tests cover:
- exact program/resolver correlation;
- missing detail payload;
- correlation mismatch;
- missing governed resolver target;
- wrong-country resolver target;
- stale CTA suppressing destination with `STALE_EVIDENCE`;
- unapproved relationship suppressing destination with `NO_VERIFIED_PUBLISHER_RELATIONSHIP`.

Commit: `26b3a4743ba1084531f0f7638a316af2a0ebefe9`

## B17 — CI integration — COMPLETE AND VERIFIED

Updated `.github/workflows/commercial-cta-fixture.yml` so CI now:
1. validates shared country CTA fixtures;
2. validates UK governance fixture;
3. validates UK technology vertical-slice structure;
4. exercises the fixture-to-presentation seam;
5. runs shared commercial negative assurance;
6. runs UK vertical-slice plus presentation negative assurance.

Commit: `24a960995f351dae048c6e048f0a21da9107f502`

GitHub Actions run `34917585789`, run #67, completed every validation and negative-assurance step successfully on this exact head. This is bounded CI evidence for the fixture/presentation contract only; it is not browser or production evidence.

## Assurance result

The first UK technology/appliances slice now preserves exact identity from structured content through presentation to the governed commercial reference. Missing, mismatched, wrong-country, stale and unapproved states fail closed before an outbound destination is exposed.

No UK-specific canonical store, resolver, scheduler or duplicate theme architecture was introduced.

## Still OPEN

- real WordPress runtime adapter/API consumption;
- production Rewards API/Supabase data;
- live UK affiliate programme approvals and destinations;
- browser-rendered route verification;
- accessibility and Core Web Vitals evidence;
- outbound click/tracking receipts;
- live freshness monitoring;
- legal/compliance approval for regulated categories.

## Next vertical batch

1. re-scan main and concurrent country work;
2. add a reusable WordPress-side presentation adapter boundary that accepts already-governed payloads without storing canonical commercial truth;
3. wire the detail/commercial CTA pattern to that adapter using safe fallback rendering when payload is absent/blocked;
4. add PHP/theme validation for escaping, disclosure and no raw tracking URL persistence;
5. verify Theme Validation plus Commercial CTA CI and record exact evidence.
