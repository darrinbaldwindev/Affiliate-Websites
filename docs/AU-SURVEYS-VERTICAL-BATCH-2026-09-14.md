# AU Surveys Vertical Batch — 2026-09-14

**Status:** ACTIVE WORK BATCH  
**Branch:** `work/au-surveys-vertical-batch`  
**Trigger:** when the owner says `cont` or `continue autonomously`, rescan current repository state first, update this batch if the evidence changed, then execute the next highest-value safe tasks vertically.

## Objective

Take one Australian user journey as far as possible without inventing commercial relationships or bypassing the canonical data/governance boundary:

`AU → Earn → Surveys → Best survey platforms → Program detail → Governed commercial action`

The goal is depth over breadth. Finish or materially advance the whole path before opening unrelated horizontal work.

## Repository scan snapshot

Current `main` already contains the Affiliate Master block theme, global homepage and reusable category/buying-guide/comparison/detail patterns, affiliate disclosure/commercial CTA patterns, canonical Rewards data contract, synthetic commercial-CTA validator/tests, and AU research/verification material.

Open historical branches remain separate. This batch must not create a competing master architecture, canonical data store, resolver or commercial authority.

## Evidence boundary

A public website, referral link, affiliate-network listing, or visible reward is not proof that this site has an approved publisher relationship. A live commercial CTA remains blocked unless the canonical gate establishes required country, consumer-claim, publisher-relationship, freshness, disclosure and destination evidence.

## Batch execution state

### B1 — Route and presentation shell — IMPLEMENTED
Created the AU Surveys category page template using the existing master information architecture. It communicates suitability, comparison criteria, limitations and verification without fabricated earnings or publisher claims.

### B2 — Comparison-ready fixture — IMPLEMENTED
Created an explicitly synthetic AU shortlist fixture. It contains no live rate, tracking URL or invented real-world publisher relationship.

### B3 — Buying-guide/comparison path — IMPLEMENTED AT SHELL/FIXTURE LEVEL
The AU shell covers eligibility, reward/payment type, participation model, qualification variability, cashout, trust/evidence, freshness and publisher-relationship state. Runtime data binding remains outside this batch.

### B4 — Detail path — IMPLEMENTED AT PRESENTATION BOUNDARY
Created `page-au-earn-surveys-detail.html` as a representative governed-data detail shell. WordPress runtime rendering/data binding is not claimed.

### B5 — Commercial CTA assurance — IMPLEMENTED / CI-GATED
Adversarial tests reuse the existing `validate_country_cta.py` authority and cover verified synthetic publisher state, conflicts, stale evidence, missing disclosure, unknown publisher state retaining a destination, and consumer-referral-only misuse. Unsafe variants fail closed; only the synthetic `example.invalid` fixture can resolve a synthetic destination.

### B6 — Current primary-source staging — IMPLEMENTED / NON-COMMERCIAL
`data/au/surveys.staging.json` holds real research records only. All publisher relationships remain UNKNOWN, every tracking destination is null, and every commercial CTA is blocked.

### B7 — Machine-readable lifecycle and freshness — IMPLEMENTED / CI-GATED
Staging records carry lifecycle state, publication gate, machine-readable blocking reasons, and a staging-only 30-day freshness policy. Tests enforce freshness consistency and an expired-evidence negative case.

### B8 — Additional AU candidate verification — IMPLEMENTED IN STAGING
Fresh first-party evidence was rechecked on 2026-09-14 and two further AU programs were staged:

- OpinionWorld Australia — AU online surveys/research; points redeemable for gift cards and PayPal credit.
- Valued Opinions Australia — AU paid surveys/product research; reward credit redeemable for Australian retailer vouchers.

Both are consumer-evidence VERIFIED but remain `VERIFIED_NOT_PUBLISHED`. Publisher relationship stays UNKNOWN, tracking destination is null and commercial CTA remains BLOCKED.

### B9 — WordPress-facing publication projection — IMPLEMENTED / CI PENDING
Added `data/au/surveys.publication-projection.json` as a derived, non-production view of the staging dataset. It contains no tracking/destination URLs and maps source state into only:

- `INFORMATIONAL_VERIFIED` for verified consumer records not yet published;
- `RESEARCH_REQUIRED` for partial/researched records;
- `BLOCKED` for every commercial state in the current real dataset.

`fixtures/au-surveys/test_publication_projection.py` verifies one-to-one record coverage, source-gate consistency, blocking-reason parity and URL absence. The existing Commercial CTA workflow now runs these projection tests.

## Current staged set

Consumer-evidence VERIFIED / informational-only:
- Octopus Group
- Ipsos iSay
- Prolific
- LifePoints
- OpinionWorld Australia
- Valued Opinions Australia

RESEARCH_REQUIRED:
- YouGov
- Toluna

No real staged record is commercially eligible.

## Verification evidence

- Head `bd2f510139173ca9fed446431fffe48744c4ceb0`: Theme Validation SUCCESS; Commercial CTA fixture validation SUCCESS.
- Head `07f76d2ff93d308b5d0cb0fe583d5049cde780b5`: Theme Validation SUCCESS; Commercial CTA fixture validation SUCCESS.
- Head `dd6e2b6b692c9a9b53e62b2e4cf6074c734c087a`: Commercial CTA fixture validation SUCCESS; Theme Validation was still in progress when rechecked.
- Current head after projection/candidate staging must obtain fresh exact-head CI before the new work is called verified.

## Current blockers

- No authenticated affiliate/publisher approval is established by repository or public-source evidence.
- No live AU survey destination should be enabled from public research evidence alone.
- Runtime WordPress rendering is not claimed unless exercised.
- Production Rewards API/database/resolver state is separate from documentation, staging data and synthetic fixtures.
- Volatile reward/referral/commission values require current primary/account-specific evidence before publication.
- YouGov and Toluna still need stronger AU-country-specific reward/eligibility evidence.

## Smallest next safe actions

1. Inspect exact-head CI for the projection and two newly staged records.
2. Build a derived informational comparison projection that excludes `RESEARCH_REQUIRED` records from best-of/ranking claims and never ranks by publisher economics.
3. Continue first-party verification of reputable AU candidates only where evidence materially improves consumer choice.
4. Prepare the WordPress/API binding contract for reading the publication projection without turning the projection into a new canonical store.
5. Keep commercial activation blocked pending authenticated publisher approval and account-specific terms.

## Standing `cont` protocol

For each future `cont` / `continue autonomously`:
1. rescan `main`, this branch, open PRs and newest commits;
2. reconcile the batch against any newer canonical contracts/tests;
3. execute the highest-value incomplete item above;
4. run or inspect available verification evidence;
5. update the batch/status and relevant PR/Overseer log;
6. stop only at a real permission, credential, external-account or evidence gate, then advance another safe item where possible.

Do not merge, deploy, approve, mark ready, alter credentials, activate commercial programs, purchase anything, or contact third parties unless separately authorised.
