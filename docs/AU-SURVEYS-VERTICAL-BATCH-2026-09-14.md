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

### B1 — Route and presentation shell

Create the AU Surveys category page template using the existing header/footer and master information architecture.

**Acceptance:** page communicates who surveys suit, what to compare, limitations, and how verification works; no fabricated earnings or publisher claims.

### B2 — Comparison-ready fixture

Create an explicitly synthetic AU survey shortlist fixture that exercises the presentation model without introducing live rates, tracking URLs or invented relationship state.

**Acceptance:** fixture is clearly marked synthetic/fixture-only and compatible with later mapping to canonical Rewards records.

### B3 — Buying-guide/comparison path

Use the existing reusable master patterns and/or a bounded AU template to represent comparison criteria:

- AU eligibility;
- reward/payment type;
- typical participation model;
- qualification variability;
- payout/cashout conditions;
- trust/evidence strength;
- verification freshness;
- publisher relationship state.

**Acceptance:** ranking language is user-value-first, never affiliate-rate-first.

### B4 — Detail path

Create one representative detail shell that can later consume a canonical survey-program record. It must distinguish consumer reward/referral status from publisher monetisation status.

**Acceptance:** no direct tracking URL in editorial content; safe fallback if monetisation is unverified.

### B5 — Commercial CTA assurance

Exercise the existing governed CTA fixture/validator against AU survey-style states: unknown relationship, consumer-referral-only, conflict, stale evidence, missing disclosure, and verified-publisher fixture.

**Acceptance:** unsafe states block; only the fully synthetic verified fixture can resolve a synthetic destination.

### B6 — Verification and handoff

Record exact files/commits, automated test evidence if available, unresolved gates, and the smallest next safe actions. No overall GREEN without independent verification.

## Current blockers that must remain explicit

- No authenticated affiliate/publisher approval is established by repository evidence alone.
- No live AU survey destination should be enabled from public research evidence alone.
- Runtime WordPress rendering is not claimed unless actually exercised.
- Production Rewards API/database/resolver state is separate from documentation and synthetic fixtures.
- Volatile reward, referral and commission values require current primary/account-specific evidence before publication.

## Standing `cont` protocol

For each future `cont` / `continue autonomously`:

1. rescan `main`, this branch, open PRs and newest commits;
2. reconcile the batch against any newer canonical contracts/tests;
3. execute the highest-value incomplete item above;
4. run or inspect available verification evidence;
5. update the batch/status and relevant PR/Overseer log;
6. stop only at a real permission, credential, external-account or evidence gate, then advance another safe item where possible.

Do not merge, deploy, approve, mark ready, alter credentials, activate commercial programs, purchase anything, or contact third parties unless separately authorised.