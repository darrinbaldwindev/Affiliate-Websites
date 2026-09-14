# Master Detail State Wiring Vertical Batch — 2026-09-14

**Status:** ACTIVE / NON-PRODUCTION
**Branch:** `work/master-detail-state-wiring-vertical-batch-2026-09-14`
**Baseline main:** `661370c4226ca45e97239a728e6b3483d65c5d6e`
**Canonical coordination:** `darrinbaldwindev/Overseer#49`

## Standing trigger

Whenever the owner says `cont` or `continue autonomously`, rescan the current repository and coordination state first, then execute the highest-value incomplete dependent task vertically. Do not rely on stale branch assumptions.

## Fresh scan findings

- PR #16 exact head `0f3c63c94ba6ec22e0570ed5597ca3226eb1c700` passed Theme Validation run #53.
- `main` advanced independently to `661370c4226ca45e97239a728e6b3483d65c5d6e`.
- PR #16 became divergent from current `main`, so this batch starts from fresh `main` rather than rebasing or stacking onto that branch.
- Current master `detail-page.php` describes evidence/freshness and a governed next-step boundary but does not render a reusable publication/verification-state component.

## Vertical objective

`detail record -> visible publication state -> evidence context -> safe next-step boundary -> automated validation`

## Execution chain

1. Restore/promote the generic publication-state pattern on this fresh branch.
2. Wire the master detail-page shell to render that reusable pattern adjacent to evidence/verification content.
3. Keep state presentation generic: no country-specific rates, earnings, prices, commissions, destinations or legal claims.
4. Keep consumer reward/referral evidence explicitly separate from publisher affiliate approval.
5. Extend Theme Validation so the detail shell cannot silently lose publication-state wiring and the reusable state pattern cannot gain raw tracking destinations.
6. Open a draft PR and verify exact-head CI.
7. Record exact diff, blockers, UNKNOWNs and next safe action.
8. Report substantive results to `Overseer#49`.

## Required states

- `Verified`
- `Research required`
- `Verification due`
- `Conflicting information`
- `Commercial action blocked`

## Safety rules

- Publication/verification state is descriptive evidence state, not affiliate approval.
- Consumer reward/referral evidence never implies publisher approval.
- Raw tracking URLs remain outside editorial patterns.
- Commercial destinations are resolver-controlled.
- Country workstreams own local evidence and commercial facts; master owns reusable presentation semantics.
- No merge, mark-ready, rebase, deployment, credential change, production write, purchase or third-party contact without explicit owner authority.

## Completion rule

Complete-for-scope requires the reusable pattern, detail-page wiring, automated assertions, exact diff and exact-head CI success. Runtime WordPress rendering remains a separate gate unless actually exercised.
