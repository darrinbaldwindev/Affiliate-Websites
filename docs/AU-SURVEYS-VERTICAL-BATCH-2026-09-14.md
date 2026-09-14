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

`data/au/surveys.staging.json` holds real research records only. Current staged set: Octopus Group, Ipsos iSay, Prolific, LifePoints, YouGov and Toluna. All publisher relationships remain UNKNOWN, every tracking destination is null, and every commercial CTA is blocked.

### B7 — Machine-readable lifecycle and freshness projection — IMPLEMENTED / CI PENDING

Added canonical lifecycle projection and explicit freshness metadata to staging records:

- strong AU primary evidence → `lifecycle_state: VERIFIED`;
- partial AU evidence → `lifecycle_state: RESEARCHED`;
- verified records stop at `VERIFIED_NOT_PUBLISHED`, not `PUBLISHABLE`;
- all commercial CTAs remain `BLOCKED` with machine-readable reasons;
- staging-only 30-day review metadata is explicit and labelled as a conservative working policy, not production policy;
- tests enforce lifecycle/freshness consistency and simulate expired evidence failing the current-state check.

### B8 — Additional AU candidate verification — RESEARCHED, STAGING ADDITION PENDING

Fresh first-party AU pages verified two further candidates suitable for staged consumer records:

- OpinionWorld Australia — AU paid surveys; rewards points redeemable for gift cards and PayPal credit;
- Valued Opinions Australia — AU paid surveys/product research; credit redeemable for Australian-brand vouchers.

Neither public site establishes this project's publisher approval. Any staged records must therefore remain commercial-CTA blocked with no tracking destination.

## Verification evidence

- Head `bd2f510139173ca9fed446431fffe48744c4ceb0`: Theme Validation SUCCESS; Commercial CTA fixture validation SUCCESS.
- Head `07f76d2ff93d308b5d0cb0fe583d5049cde780b5`: Theme Validation SUCCESS; Commercial CTA fixture validation SUCCESS.
- Publication/freshness commits `dd6e2b6b692c9a9b53e62b2e4cf6074c734c087a` and `ac3da8367944362c11bacd4141abd0c7f03adcdd` require fresh head-associated CI evidence before being called verified.

## Current blockers

- No authenticated affiliate/publisher approval is established by repository or public-source evidence.
- No live AU survey destination should be enabled from public research evidence alone.
- Runtime WordPress rendering is not claimed unless exercised.
- Production Rewards API/database/resolver state is separate from documentation, staging data and synthetic fixtures.
- Volatile reward/referral/commission values require current primary/account-specific evidence before publication.
- YouGov and Toluna still need stronger AU-country-specific reward/eligibility evidence.

## Smallest next safe actions

1. Inspect CI for the lifecycle/freshness head.
2. Stage OpinionWorld Australia and Valued Opinions Australia into the existing single AU surveys staging dataset with VERIFIED consumer evidence, UNKNOWN publisher relationship and BLOCKED CTA.
3. Add a derived informational comparison projection that excludes `RESEARCHED`/partial records from best-of claims without creating another source of truth.
4. Continue current first-party verification of remaining reputable AU candidates.
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
