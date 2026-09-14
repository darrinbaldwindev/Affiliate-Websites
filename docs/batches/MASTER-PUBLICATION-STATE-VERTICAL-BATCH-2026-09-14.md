# Master Publication State Vertical Batch — 2026-09-14

**Status:** ACTIVE / NON-PRODUCTION
**Branch:** `work/master-publication-state-vertical-batch-2026-09-14`
**Baseline main:** `4dd4c1e40841224245a4056c3e7917c8f0141500`
**Canonical coordination:** `darrinbaldwindev/Overseer#49`

## Standing trigger

Whenever the owner says `cont` or `continue autonomously`, first rescan current repository and coordination state, then execute the highest-value incomplete dependent task vertically. Do not reuse stale assumptions.

## Why this batch exists

The fresh scan found the AU Surveys branch had diverged materially from `main` (29 commits ahead, 13 behind), while `main` itself had advanced with UK, software/games and portfolio batch work. Rather than stack more changes on a divergent country branch, this batch starts from current `main` and promotes one reusable master capability that multiple country workstreams need: a clear publication/verification-state presentation contract.

## Vertical objective

`country evidence state -> master presentation state -> visible trust label -> safe action boundary -> automated validation`

## Execution chain

1. Inspect current master trust/methodology pattern and theme validation workflow.
2. Add a reusable publication-state pattern to the master Block Theme.
3. Encode only generic states; no country-specific commercial data, rates, legal claims or tracking URLs.
4. Update Theme Validation so the reusable pattern cannot silently lose its core safety wording/state labels.
5. Run exact-head GitHub Actions through a draft PR.
6. Record exact diff, CI result, blockers and next safe action.
7. Report substantive result to `Overseer#49`.

## Required reusable states

- `VERIFIED` — evidence checked, but not necessarily commercially enabled.
- `RESEARCH REQUIRED` — evidence incomplete; do not present as recommendation-ready.
- `VERIFICATION DUE` — previously checked but freshness review required.
- `CONFLICTING INFORMATION` — conflicting evidence must remain visible and block certainty.
- `COMMERCIAL ACTION BLOCKED` — relationship/destination/disclosure/freshness gate has not passed.

## Safety rules

- Verification state is separate from publisher affiliate approval.
- Consumer reward/referral evidence never implies publisher approval.
- No raw tracking URL belongs in this pattern.
- No unsupported earnings, price, commission, availability or legal claim may be hard-coded.
- Country workstreams supply local evidence; the master owns the reusable presentation semantics.
- No merge, ready transition, deployment, credential change or production write without explicit owner authority.

## Completion rule

This batch is complete-for-scope only when the pattern exists, automated checks cover its required semantics, exact diff is known, and exact-head CI succeeds. Runtime WordPress rendering remains a separate gate unless actually exercised.
