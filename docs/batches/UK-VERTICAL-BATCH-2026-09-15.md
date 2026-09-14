# UK Vertical Autonomous Batch — 2026-09-15

**Workstream:** United Kingdom Affiliate Website  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Mode:** vertical autonomous execution  
**Status:** COMPLETE — bounded repository batch executed  
**Rule:** evidence controls completion; fixture success is not production readiness.

## Standing trigger

On `cont` or `continue autonomously`:

1. scan current repository state;
2. reconcile concurrent movement and prior batch results;
3. define the highest-value bounded vertical slice;
4. execute it against shared architecture;
5. run/inspect available CI evidence;
6. record exact results, open risks and next batch.

## Scan baseline

Fresh `main` scan showed:

- shared Block Theme patterns already exist for country homepage, category, buying guide, comparison, detail and commercial CTA;
- the commercial CTA workflow already validates country fixtures, UK governance fixture and Software/Games fixtures;
- UK governance fixture already contains a STANDARD synthetic technology programme plus blocked telecom, finance and stale energy examples;
- no need exists for UK-specific theme templates or a second commercial resolver.

The reusable category and detail patterns intentionally contain decision-support placeholders and defer volatile commercial facts to approved structured sources/resolution.

## Batch objective

Prove the first UK fixture-safe content journey:

`UK technology/appliances category → comparison + buying guide → detail → governed commercial CTA`

without embedding live merchant facts or duplicating master theme code.

## B15 — UK technology/appliances content fixture — COMPLETE

Created:

`fixtures/uk-vertical-slice/technology-appliances.synthetic.json`

The fixture maps:

- `/uk/technology-appliances/` → shared category pattern;
- UK comparison route → shared comparison pattern;
- UK buying-guide route → shared buying-guide pattern;
- UK detail route → shared detail pattern;
- detail commercial action → shared governed commercial CTA pattern;
- resolver reference → `UK-TECH-FIXTURE-001` in the existing UK governed CTA fixture.

The fixture contains no live merchant price, commission, stock, cookie duration, tracking URL or affiliate destination.

Commit: `a29923fa52b475d6236d61963055c0c1d8609a87`

## B16 — Route/content/resolver validator — COMPLETE

Created:

`fixtures/uk-vertical-slice/validate_uk_vertical_slice.py`

The validator requires:

- explicit UK fixture identity;
- canonical UK technology/appliances path;
- reuse of shared master patterns;
- unique UK-scoped routes;
- fixture evidence state;
- required disclosure at detail stage;
- exact detail/resolver program-ID correlation;
- referenced CTA record exists and is UK-bound;
- first slice uses STANDARD risk class;
- synthetic verified publisher state and UK destination-country binding;
- rejection of forbidden live commercial fields anywhere in the fixture.

Commit: `88f2ab65e6874d25bebb3dc586e21fec314bb046`

## B17 — UK vertical-slice negative assurance — COMPLETE

Created:

`fixtures/uk-vertical-slice/test_uk_vertical_slice.py`

Negative cases prove fail-closed rejection for:

- wrong-country route;
- unknown resolver/program reference;
- embedded price;
- raw tracking URL;
- missing disclosure requirement;
- CTA record belonging to another country;
- non-STANDARD risk class for this first low-regulatory-complexity slice;
- unverified CTA state.

Commit: `9bf749a8b1a387c0e9238927f7081ffae249e516`

## B18 — Stable audit reason codes — COMPLETE

Updated:

`fixtures/commercial-cta/validate_country_cta.py`

Blocked valid fixture states now emit stable machine-readable reasons instead of generic state strings:

- `STALE_EVIDENCE`
- `UNKNOWN_EVIDENCE`
- `CONSUMER_REFERRAL_ONLY`
- `NO_VERIFIED_PUBLISHER_RELATIONSHIP`
- `NON_PUBLISHABLE_CTA_STATE`

Audit events also expose country and risk class while continuing to emit no tracking URL.

Commit: `a99210b1b9c49e37182afd61da253c1459d872e7`

## B19 — UK audit reason assurance — COMPLETE

Created:

`fixtures/commercial-cta/test_uk_audit_reasons.py`

Assertions cover:

- UK broadband blocked due to no verified publisher relationship;
- UK energy blocked due to stale evidence;
- UK technology allowed as a synthetic verified publisher CTA;
- consumer-referral-only reason stability;
- audit events never surface tracking URLs.

Commit: `2781175639e4e67547e2bf947dbd81c9ee4fdb4f`

## B20 — CI integration — COMPLETE / GREEN

Updated:

`.github/workflows/commercial-cta-fixture.yml`

The workflow now watches `fixtures/uk-vertical-slice/**`, validates the UK technology fixture against the existing UK CTA governance fixture, runs existing CTA/Software-Games tests, runs UK audit-reason tests, and runs UK vertical-slice negative tests.

Commit: `e80ec54c4cb56c12bce391c904ddee0d99ae91d6`

Verified CI:

- workflow: **Commercial CTA fixture validation**
- run: **#61 / 34853950440**
- head: `e80ec54c4cb56c12bce391c904ddee0d99ae91d6`
- conclusion: **success**

This is executable evidence that the new UK fixture, validator, shared CTA validator changes and negative assurance suite passed together on `main`.

## What this proves

The repository now has executable evidence that the first UK technology/appliances journey can be represented through shared patterns and a shared governed CTA contract while rejecting country drift, resolver drift and embedded volatile commercial data.

It does **not** prove live WordPress rendering, production Rewards API integration, live affiliate approval, live merchant data, tracking receipts, legal approval, accessibility or Core Web Vitals.

## Still OPEN

- actual WordPress page assembly/rendering from this fixture;
- browser-level route verification;
- production Rewards API/Supabase resolver implementation;
- end-to-end click receipt/audit correlation;
- live UK merchant/feed ingestion;
- freshness monitoring and withdrawal handling;
- accessibility and performance evidence;
- regulated-category runtime enforcement beyond fixtures.

## Next vertical batch

1. fresh scan of `main` and concurrent work;
2. inspect current WordPress route/page assembly seam and any existing fixture-to-page tooling;
3. implement the smallest reusable fixture-to-presentation adapter or test seam without turning WordPress into the source of truth;
4. prove detail-page commercial CTA correlation survives presentation mapping;
5. add failure cases for missing/stale structured presentation payloads;
6. verify Theme Validation plus relevant CTA CI and record exact evidence.

## Completion rule

Only bounded repository artifacts with direct verification are marked complete. Production/runtime/legal/commercial states remain OPEN until separately evidenced.
