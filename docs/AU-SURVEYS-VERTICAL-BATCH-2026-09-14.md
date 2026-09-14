# AU Surveys Vertical Batch — 2026-09-14

**Status:** ACTIVE WORK BATCH  
**Branch:** `work/au-surveys-vertical-batch`  
**Trigger:** when the owner says `cont` or `continue autonomously`, rescan current repository state first, update this batch if the evidence changed, then execute the next highest-value safe tasks vertically.

## Objective

Take one Australian user journey as far as possible without inventing commercial relationships or bypassing the canonical data/governance boundary:

`AU → Earn → Surveys → Best survey platforms → Program detail → Governed commercial action`

The goal is depth over breadth. Finish or materially advance the whole path before opening unrelated horizontal work.

## Repository scan snapshot

Current `main` already contains:

- the Affiliate Master block theme;
- global homepage and reusable category/buying-guide/comparison/detail patterns;
- affiliate disclosure and commercial CTA patterns;
- a canonical Rewards data contract;
- a synthetic commercial-CTA fixture plus validator/tests;
- AU affiliate research, verification and publishability documents.

Open work remains distributed across several historical homepage branches, AU research, USA research, and reconciliation PRs. This batch must not create a competing master architecture, scheduler, canonical data store, or affiliate-resolution authority.

## Evidence boundary

A public website, referral link, affiliate-network listing, or visible reward is not proof that this site has an approved publisher relationship.

A live commercial CTA remains blocked unless the canonical commercial gate can establish all required evidence, freshness, disclosure and destination conditions. Where this is not established, the UI must render a neutral/non-affiliate state.

## Batch execution order

### B1 — Route and presentation shell — IMPLEMENTED

Created the AU Surveys category page template using the existing header/footer and master information architecture.

**Acceptance:** page communicates who surveys suit, what to compare, limitations, and how verification works; no fabricated earnings or publisher claims.

### B2 — Comparison-ready fixture — IMPLEMENTED

Created an explicitly synthetic AU survey shortlist fixture that exercises the presentation model without introducing live rates, tracking URLs or invented real-world relationship state.

**Acceptance:** fixture is clearly marked synthetic/fixture-only and compatible with later mapping to canonical Rewards records.

### B3 — Buying-guide/comparison path — IMPLEMENTED AT SHELL/FIXTURE LEVEL

The AU category template and synthetic shortlist represent the comparison criteria without ranking by publisher economics.

Criteria include:

- AU eligibility;
- reward/payment type;
- typical participation model;
- qualification variability;
- payout/cashout conditions;
- trust/evidence strength;
- verification freshness;
- publisher relationship state.

**Remaining:** runtime data binding to the future Rewards API/canonical store is not implemented or claimed.

### B4 — Detail path — IMPLEMENTED AT PRESENTATION BOUNDARY

Created `page-au-earn-surveys-detail.html` as a representative detail shell. It explicitly requires governed data for eligibility, reward and commercial fields and renders a safe development fallback when no approved action exists.

**Remaining:** WordPress runtime rendering/data binding is not yet verified.

### B5 — Commercial CTA assurance — IMPLEMENTED / CI-GATED

Added adversarial tests against the existing `validate_country_cta.py` authority. The AU survey cases cover:

- fully synthetic verified publisher state;
- conflicting publisher evidence;
- stale publisher evidence;
- missing disclosure;
- unknown publisher relationship retaining a destination;
- consumer-referral-only state attempting a publisher CTA.

Unsafe variants are expected to fail closed. The only passing commercial case remains a fully synthetic `example.invalid` fixture.

### B6 — Current primary-source staging — IMPLEMENTED / NON-COMMERCIAL

Created `data/au/surveys.staging.json` after a 2026-09-14 primary-source refresh. Current staging set:

- Octopus Group — current AU primary evidence; publisher relationship UNKNOWN;
- Ipsos iSay — current AU referral evidence; publisher relationship UNKNOWN;
- Prolific — Australia supported for participants; publisher relationship UNKNOWN;
- LifePoints — current AU rewards evidence; publisher relationship UNKNOWN;
- YouGov — global panel/reward evidence only; AU-specific reward detail still RESEARCH_REQUIRED;
- Toluna — current reward/community evidence but AU-specific catalogue still RESEARCH_REQUIRED.

No record is CTA-eligible. No tracking destination is stored. CI tests assert these boundaries.

## Verification evidence

- PR #13 head `bd2f510139173ca9fed446431fffe48744c4ceb0`: Theme Validation completed SUCCESS.
- PR #13 head `bd2f510139173ca9fed446431fffe48744c4ceb0`: Commercial CTA fixture validation completed SUCCESS.
- Subsequent commits add CTA adversarial cases plus staging-data safety checks; their final workflow result must be inspected before claiming them verified.

## Current blockers that must remain explicit

- No authenticated affiliate/publisher approval is established by repository or public-source evidence.
- No live AU survey destination should be enabled from public research evidence alone.
- Runtime WordPress rendering is not claimed unless actually exercised.
- Production Rewards API/database/resolver state is separate from documentation, staging data and synthetic fixtures.
- Volatile reward, referral and commission values require current primary/account-specific evidence before publication.
- YouGov and Toluna need stronger AU-country-specific reward/eligibility evidence before consumer-facing publication.

## Smallest next safe actions

1. Inspect the newest CI runs for CTA adversarial and staging safety tests.
2. Add a machine-readable publication-state projection so WordPress can distinguish `RESEARCH_REQUIRED`, informational-only and commercial-eligible records without storing tracking URLs.
3. Add exact freshness-due metadata and a stale-data negative case to AU survey staging.
4. Verify additional top AU survey candidates from current first-party sources and add them only when country evidence is adequate.
5. Keep all commercial activation blocked pending authenticated publisher approval and account-specific terms.

## Standing `cont` protocol

For each future `cont` / `continue autonomously`:

1. rescan `main`, this branch, open PRs and newest commits;
2. reconcile the batch against any newer canonical contracts/tests;
3. execute the highest-value incomplete item above;
4. run or inspect available verification evidence;
5. update the batch/status and relevant PR/Overseer log;
6. stop only at a real permission, credential, external-account or evidence gate, then advance another safe item where possible.

Do not merge, deploy, approve, mark ready, alter credentials, activate commercial programs, purchase anything, or contact third parties unless separately authorised.
