# Software & Games Vertical Autonomous Batch 002 — 2026-09-14

**Workstream:** Master Affiliate Websites / cross-country commercial research  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Mode:** vertical autonomous execution  
**Status:** COMPLETE — bounded batch GREEN  
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

### SG2-2 — Synthetic Software & Games comparison fixture — COMPLETE

Created `fixtures/commercial-cta/software-games-offers.synthetic.json` with AU/UK/US allowed and deliberately blocked cases. No real merchant tracking URLs are present; publishable fixture destinations use `example.invalid` only.

Commit: `4dd4c1e40841224245a4056c3e7917c8f0141500`

### SG2-3 — Deterministic fail-closed offer evaluator — COMPLETE

Created `fixtures/commercial-cta/validate_software_games_offer.py`.

The evaluator computes ALLOWED/BLOCKED from evidence and rejects stale price, region mismatch, currency mismatch, invalid/non-positive price, missing disclosure, missing Windows/Office/productivity licence type, unapproved merchant state and unverified marketplace seller provenance. Input `expected_decision` cannot override the computed result.

Commit: `1e24693ef3d7ef9c32fb8184dcbc9a7683d7eb98`

### SG2-4 — Negative assurance tests — COMPLETE

Created `fixtures/commercial-cta/test_software_games_offer.py` covering:

- stale evidence falsely labelled ALLOWED;
- region mismatch;
- Windows unknown licence type;
- Office missing licence type;
- unapproved merchant;
- unknown marketplace seller provenance;
- wrong currency;
- missing disclosure;
- blocked-offer destination leakage;
- live destination in allowed fixture;
- non-positive price;
- duplicate offer ID;
- no emitted tracking URL in fixture decisions.

Commit: `d98152c6997c51325343f6c20024d5faff46339a`

### SG2-5 — Existing CI extension — COMPLETE / GREEN

Extended `.github/workflows/commercial-cta-fixture.yml` rather than creating a parallel workflow. It now validates both the existing country CTA fixture and Software & Games fixture and runs both negative-test suites.

Commit: `18d29a6bf0c884822dae213f5dbff42c8c4215ca`

GitHub Actions evidence:

- workflow: `Commercial CTA fixture validation`
- run: `34822295201`
- exact head: `18d29a6bf0c884822dae213f5dbff42c8c4215ca`
- conclusion: **success**

### SG2-6 — AU/UK/US authorised benchmark research — COMPLETE

Created `docs/SOFTWARE-GAMES-AUTHORISED-BENCHMARKS-2026-09-14.md`.

Established Microsoft Store direct as the principal high-assurance Windows/Microsoft-software benchmark for AU/UK/US when an exact comparable SKU exists. Recorded Fanatical, Green Man Gaming and GOG as strong authorised/high-trust game benchmark candidates, while keeping country eligibility and exact SKU availability evidence-scoped.

Commit: `64a1b84c7f875134f683378e5bf274270a41cce5`

### SG2-7 — Feed/API automation suitability — COMPLETE

Created `docs/SOFTWARE-GAMES-FEED-AUTOMATION-MATRIX-2026-09-14.md`.

Current priority order:

1. Green Man Gaming catalogue API;
2. GOG Product Feed API;
3. Fanatical/Awin after structured-feed capability is confirmed for the account;
4. Eneba XML/CSV only behind marketplace provenance controls;
5. GAMIVO XML only behind marketplace/reseller provenance and attribution controls.

No feed/API availability was treated as affiliate approval or publication permission.

Commit: `04228679b5827322d325d5f6b29cf2ac8de00406`

### SG2-8 — Verification and closure — COMPLETE

Exact-head CI passed for the code/fixture boundary. Research artifacts are now durable on `main`. This is a **bounded batch GREEN**, not production-commercial GREEN: merchant/network account approvals, credentials, production feed terms, real country/SKU availability and canonical tracking-link resolution remain outside this synthetic batch.

## Hard rules retained

- No production affiliate URLs or credentials.
- Fixture URLs use `example.invalid`.
- Cheapest observed price is not a trust or recommendation claim.
- Marketplace brand trust cannot substitute for underlying seller provenance.
- Windows/Office/productivity comparisons require licence type before publication.
- Wrong-country offers and wrong-country currencies fail closed.
- Synthetic approval is fixture evidence only; it is never evidence of a real merchant relationship.
- Reuse the existing commercial CTA architecture.

## Execution commits

- `655083a5c7db9ce56925c43dce2eb9636d38d098` — create Batch 002
- `4dd4c1e40841224245a4056c3e7917c8f0141500` — synthetic offer fixture
- `1e24693ef3d7ef9c32fb8184dcbc9a7683d7eb98` — fail-closed evaluator
- `d98152c6997c51325343f6c20024d5faff46339a` — negative assurance tests
- `18d29a6bf0c884822dae213f5dbff42c8c4215ca` — CI integration
- `64a1b84c7f875134f683378e5bf274270a41cce5` — authorised benchmark matrix
- `04228679b5827322d325d5f6b29cf2ac8de00406` — feed/API automation matrix

## Next autonomous vertical slice

On the next `cont` / `continue autonomously`, fresh-scan first, then prioritise the smallest safe progression toward production-quality comparison data:

1. inspect the canonical commercial data contract for fields needed by Software & Games;
2. add bounded schema/fixture coverage for licence transferability, account binding, install/device count and activation platform;
3. test edition/SKU mismatch so unlike products cannot be ranked as equivalent;
4. define price freshness windows without inventing merchant-specific caching rights;
5. map the first real affiliate-account/application prerequisites for GMG, GOG, Fanatical/Awin and the chosen software-reseller candidate;
6. keep all unresolved merchant approvals and production tracking URLs fail-closed.
