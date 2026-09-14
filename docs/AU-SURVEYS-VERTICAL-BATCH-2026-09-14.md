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
Fresh first-party evidence was rechecked on 2026-09-14. OpinionWorld Australia and Valued Opinions Australia were added as consumer-evidence VERIFIED records while commercial state remained blocked.

### B9 — WordPress-facing publication projection — IMPLEMENTED / CI-GATED
`data/au/surveys.publication-projection.json` is a derived, non-production view of the staging dataset. It contains no tracking/destination URLs and maps source state into only `INFORMATIONAL_VERIFIED`, `RESEARCH_REQUIRED`, and commercial `BLOCKED`. Tests require one-to-one source coverage, source-gate consistency, blocking-reason parity and URL absence.

### B10 — Flagship/core user-value priority projection — IMPLEMENTED / CI PENDING
Fresh first-party evidence materially improved two records:

- Pureprofile — paid surveys/cash rewards plus current AU/NZ consumer-referral terms; staged as VERIFIED consumer evidence.
- Toluna Influencers — Australia-specific registration material currently displays PayPal, Amazon Australia and Coles rewards; promoted from partial research to VERIFIED consumer evidence.

YouGov remains `RESEARCH_REQUIRED`: current first-party evidence confirms Australia as a YouGov panel market and confirms the global points/reward model, but the batch still lacks sufficiently specific Australian member reward-catalogue evidence for consumer publication.

Added `data/au/surveys.priority-projection.json` to express the current best-of ordering without using publisher commission or commercial economics. Current evidence-led ordering:

1. Octopus Group — FLAGSHIP
2. Pureprofile — FLAGSHIP
3. Prolific — FLAGSHIP
4. Ipsos iSay — CORE
5. LifePoints — CORE
6. Toluna Influencers — CORE
7. OpinionWorld Australia — SECONDARY
8. Valued Opinions Australia — SECONDARY
9. YouGov — RESEARCH_HOLD

`fixtures/au-surveys/test_priority_projection.py` requires unique contiguous ranks, known source IDs, no tracking/affiliate URL fields, no commission-rate input, current primary evidence for FLAGSHIP/CORE entries, and RESEARCH_HOLD for partial records. This projection is editorial/research staging only and does not grant publication or commercial eligibility.

## Current staged set

Consumer-evidence VERIFIED / informational-only:
- Octopus Group
- Pureprofile
- Prolific
- Ipsos iSay
- LifePoints
- Toluna Influencers
- OpinionWorld Australia
- Valued Opinions Australia

RESEARCH_REQUIRED:
- YouGov

No real staged record is commercially eligible.

## Verification evidence

- Head `31926c50968f911b619de89d5ff245b31db00f4d`: Theme Validation SUCCESS; Commercial CTA fixture validation SUCCESS.
- Earlier lifecycle/freshness and projection heads also obtained successful workflow evidence.
- Current exact head after Pureprofile/Toluna/priority-projection work must obtain fresh CI before this newest work is called verified.

## Current blockers

- No authenticated affiliate/publisher approval is established by repository or public-source evidence.
- No live AU survey destination should be enabled from public research evidence alone.
- Runtime WordPress rendering is not claimed unless exercised.
- Production Rewards API/database/resolver state is separate from documentation, staging data and derived projections.
- Volatile reward/referral/commission values require current primary/account-specific evidence before publication.
- YouGov still needs stronger AU-member reward-catalogue evidence before consumer-facing publication.

## Smallest next safe actions

1. Inspect exact-head CI for the Pureprofile/Toluna and priority-projection changes.
2. Add an API/read-model contract mapping the publication and priority projections to WordPress fields without making either projection canonical.
3. Continue first-party verification of reputable AU candidates only where evidence materially improves consumer choice.
4. Add ranking-change tests so a `RESEARCH_REQUIRED` or stale record cannot silently enter FLAGSHIP/CORE.
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
