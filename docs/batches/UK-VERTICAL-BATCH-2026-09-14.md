# UK Vertical Autonomous Batch — 2026-09-14

**Workstream:** United Kingdom Affiliate Website  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Mode:** vertical autonomous execution  
**Status:** COMPLETE — second bounded repository batch executed  
**Rule:** evidence controls completion; research claims are not production truth.

## Standing trigger

When the owner says **`cont`** or **`continue autonomously`** in this workstream, execute this cycle without asking for confirmation unless a safety/governance boundary requires it:

1. scan current repository state and recent relevant evidence;
2. reconcile completed work, stale assumptions, blockers and highest-value gaps;
3. create or update the current vertical batch;
4. execute as many bounded tasks in the batch as practical;
5. verify resulting repository state and available CI evidence;
6. record completed work, unresolved risks and the smallest useful next batch.

Do not create duplicate architecture, canonical stores, schedulers, governance systems or country-specific forks of reusable master code.

## First batch — research-to-governance package

Completed previously:

- repo reconciliation;
- `docs/data/uk-affiliate-opportunity-research.json`;
- `docs/UK-COMMERCIAL-SCORING-MATRIX-2026-09-14.md`;
- `docs/vertical-slice/UK-VERTICAL-SLICE-CONTRACT.md`;
- `docs/UK-PUBLISHABILITY-GATE-2026-09-14.md`;
- mapping to shared Supabase/Postgres → Rewards API → WordPress → controlled resolver architecture.

No live programme approval, production destination, commission, price, stock or promotional fact was inferred from research.

## Second batch — governed UK commercial CTA assurance

### B8 — Fresh repository scan — COMPLETE

Re-scanned `main` before work. The repository had moved since the first batch and now included additional commercial-CTA and software/games fixture work plus `.overseer/VERTICAL-BATCH-ADOPTION.md`.

The shared commercial-CTA fixture already enforced:

- current/fixture evidence for verified publisher CTAs;
- publisher evidence source + verification timestamp;
- independent country eligibility evidence;
- disclosure presence;
- conflict rejection;
- non-live `example.invalid` destinations in fixtures;
- fail-closed handling for unknown/stale/non-verified relationships.

Therefore this batch extended the shared validator rather than creating a UK resolver.

### B9 — Country-bound destination gate — COMPLETE

Updated:

`fixtures/commercial-cta/validate_country_cta.py`

A verified CTA must now carry `destination_country`, and it must exactly match the programme country. Non-verified relationships may not carry `destination_country` at all.

This creates an explicit wrong-country fail-closed gate suitable for AU/UK/US rather than a UK-only exception.

Commit:

`297ff4baba968f7ec079a86651ea57cfa9e4cba7`

### B10 — Risk-class / enhanced compliance gate — COMPLETE

The shared validator now recognises controlled risk classes:

- `STANDARD`
- `TELECOM`
- `TRAVEL`
- `REGULATED_FINANCE`
- `HEALTH_SENSITIVE`
- `UTILITIES_HOME_ENERGY`

A verified CTA in `REGULATED_FINANCE`, `HEALTH_SENSITIVE` or `UTILITIES_HOME_ENERGY` cannot publish unless `enhanced_compliance_gate_passed` is explicitly true.

This is fixture/governance enforcement only. It does **not** claim legal approval, FCA approval, merchant approval or production readiness.

### B11 — Shared fixture migration — COMPLETE

Updated:

`fixtures/commercial-cta/country-programs.synthetic.json`

The existing synthetic records now carry explicit destination-country and risk-class fields while preserving non-live fixture destinations.

Commit:

`0562018880c7fbf0ddf15c0c7f6818d144719610`

### B12 — Negative assurance tests — COMPLETE

Updated:

`fixtures/commercial-cta/test_country_cta.py`

Added bounded tests proving rejection of:

- verified CTA whose destination country differs from programme country;
- destination-country metadata on a non-verified relationship;
- regulated-finance verified CTA without enhanced compliance gate;
- health-sensitive verified CTA without enhanced compliance gate;
- utilities/home-energy verified CTA without enhanced compliance gate;
- invalid risk classes.

Also added a positive fixture case proving a regulated synthetic CTA can pass only when the enhanced gate is explicitly asserted.

Commit:

`7c15d44242302789ca65c235cddd6672f683eafa`

### B13 — Dedicated UK governed fixture — COMPLETE

Created:

`fixtures/commercial-cta/uk-governance.synthetic.json`

The UK-focused fixture includes:

- standard UK technology example with a synthetic verified publisher CTA;
- UK broadband/telecom non-affiliate fallback;
- UK regulated-finance non-affiliate fallback;
- UK utilities/home-energy stale state;
- AU/US guard records so the shared country fixture contract remains intact.

It contains no live merchant tracking URLs or claimed live approval.

Commit:

`fba51ecb11597c698e17ccd4cdbd9b5bada9dd48`

### B14 — CI integration — COMPLETE AND VERIFIED

Updated:

`.github/workflows/commercial-cta-fixture.yml`

CI now validates the dedicated UK governed fixture through the same shared validator before running the negative assurance suite.

Commit:

`9a1ff841c2003bde0e045d39bd40b32af508ba3f`

Concurrent repository work landed immediately after this commit (`f2dd846d7992556a63bee3083e73471e9afaa944`) with `9a1ff841...` as its parent. Commercial CTA fixture validation run **#50 / 34826525159** completed successfully on that descendant head. Therefore the successful run includes this UK validator, fixture, workflow and test work plus the concurrent software/games change.

## Assurance result

The UK vertical now has executable evidence for several core fail-closed properties:

- stale verified evidence cannot publish;
- unknown/unapproved publisher relationship cannot publish a commercial destination;
- conflicting publisher evidence cannot publish;
- missing disclosure cannot publish;
- wrong-country commercial destination cannot publish;
- regulated/high-risk classes cannot publish a verified CTA without an explicit enhanced compliance gate;
- fixtures cannot smuggle live merchant URLs into verified synthetic CTA records.

This materially strengthens the UK acceptance path while retaining one shared commercial resolver contract.

## Still OPEN

Not claimed complete:

- live UK programme approvals;
- live production affiliate destinations;
- actual FCA/legal/compliance approval for regulated categories;
- production Rewards API/Supabase integration;
- runtime resolver implementation outside the synthetic validator;
- live WordPress/browser rendering;
- accessibility/Core Web Vitals evidence;
- end-to-end click/tracking receipts;
- freshness monitoring against live programme sources;
- address-level broadband availability resolution.

## Next vertical batch

On the next `cont` / `continue autonomously`:

1. re-scan main and concurrent work;
2. inspect reusable `country-homepage`, `category-page`, `buying-guide`, `comparison-page`, `detail-page` and `commercial-cta` patterns;
3. create a UK technology/appliances fixture content contract that maps cleanly onto those shared patterns;
4. add fixture-safe UK category → comparison/guide → detail mappings without hard-coded volatile commercial facts;
5. strengthen CTA audit-event assertions so blocked UK decisions expose stable machine-readable reason codes;
6. verify Theme Validation and Commercial CTA CI and record exact results.

## Completion rule

A batch is complete when bounded repository artifacts are created/updated and their state is verified. Items requiring live merchant approval, credentials, production infrastructure, legal review or browser/runtime evidence remain explicitly OPEN rather than being inferred complete.
