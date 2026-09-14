# Affiliate Websites — Vertical Batch Contract

Status: ACTIVE NON-PRODUCTION WORKFLOW
Canonical coordination: `darrinbaldwindev/Overseer#49`

## Standing trigger
Whenever the owner says `cont` or `continue autonomously`, run one new vertical batch using this contract.

## Batch discipline
1. Freshly scan the canonical repository before choosing work.
2. Re-read the current Level 2 coordination state when it could change priorities.
3. Identify the highest-value incomplete objective already supported by repository evidence.
4. Avoid duplicate architecture, duplicate workstreams, and duplicate control-plane systems.
5. Prefer a vertical chain of dependent tasks over many shallow parallel tasks.
6. Keep all work bounded, non-production, recoverable, and evidence-first.
7. Do not merge, deploy, change credentials, contact suppliers, make purchases, enable production autonomy, or make production writes without owner authority.
8. Verify exact changes after every mutation and record blockers/UNKNOWNs rather than inventing completion.
9. Report substantive results durably back to the coordination layer for ChatGPT Overseer.
10. Continue to the next useful dependent task until the batch reaches an authority, credential, environment, or safety boundary.

## Default batch shape

### A. Scan
- current `main` head
- repository tree and recent implementation areas
- open issues / draft PRs relevant to this workstream
- existing Level 2 fixtures, tests, workflows and status docs
- stale assumptions from prior batches

### B. Select one vertical objective
The objective should usually span as much of this chain as is safely available:

`inspect -> bounded edit -> validation/test -> exact diff -> replay/recovery check -> durable evidence -> coordination report`

### C. Execute
- work from current repository evidence
- use existing project structures before creating new ones
- isolate risky changes to a non-production branch/worktree
- preserve master-template vs country-workstream ownership
- preserve consumer-truth / affiliate-truth separation
- never fabricate commercial, legal, verification, price, commission, availability or tracking claims

### D. Verify
For every mutation capture, where available:
- baseline ref/hash
- changed path set
- exact diff
- validation/test outcome
- replay/idempotency result
- recovery/failure behavior
- unresolved UNKNOWNs

### E. Report
Durably report:
- batch identity
- baseline head
- files/issues/PRs inspected
- exact actions completed
- evidence produced
- blockers/UNKNOWNs
- next smallest safe action
- status: ACTIVE / BLOCKED / COMPLETE-FOR-SCOPE

## Current Level 2 priority workload
Use `docs/level2/AGENTOS-WORKLOAD-2026-09-13.md` and `fixtures/level2/au-program-publishability.json` as the primary bounded Affiliate-Websites acceptance workload until superseded by stronger repository evidence.

Expected fixture truth:
```json
{
  "schema": "affiliate.level2.publishability.v1",
  "country": "AU",
  "program": "FIXTURE_PROGRAM",
  "rewards_user": true,
  "affiliate_program_verified": false,
  "publishable": false,
  "reason": "SYNTHETIC_FIXTURE_ONLY",
  "production_write": false
}
```

The fixture is synthetic, non-production, grants no affiliate approval, and must never be promoted into live commercial content.

## Batch success rule
A batch is successful when it produces the maximum useful, safely verified progress from the current repository state without crossing governance boundaries. Worker self-report alone is not completion; repository evidence and, where applicable, AgentOS receipts plus Green/PRS control the claim.