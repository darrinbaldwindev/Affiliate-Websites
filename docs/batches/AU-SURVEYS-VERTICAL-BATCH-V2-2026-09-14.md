# AU Surveys Vertical Batch V2 — 2026-09-14

**Workstream:** Affiliate Websites → Australia → Earn → Surveys  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Branch:** `work/au-surveys-vertical-batch-v2`  
**Mode:** maximum-value vertical autonomous execution  
**Status:** ACTIVE  
**Standing trigger:** whenever the owner says `cont` or `continue autonomously`, execute this protocol again from a fresh repository scan.

## Owner instruction

Each autonomous cycle MUST:

1. fresh-scan `main`, this branch, relevant open PRs, newest commits and CI before planning;
2. reconcile concurrent changes before writing so no duplicate authority, canonical store, resolver, scheduler or governance path is created;
3. select the highest-value incomplete vertical tranche that can be completed safely in the current cycle;
4. execute as much of that tranche as possible, not merely describe it;
5. add or strengthen machine-readable evidence, fail-closed tests and CI whenever the work changes publication/commercial state;
6. inspect exact-head CI or other independent evidence before calling work verified;
7. update this batch, the active PR and the canonical Overseer log with exact commits, evidence and blockers;
8. continue to another safe tranche if the first one is blocked by credentials/account approval/external permissions;
9. leave merge, deploy, ready-for-review, credential changes, account applications, purchases, third-party contact and live commercial activation untouched unless separately authorised.

Evidence controls completion. No overall GREEN from implementation claims alone.

## Fresh scan snapshot

- `main` advanced independently to `edb79f2c3dc45394c1342934e653c674cc158178` with a completed Software & Games research/governance batch.
- AU Surveys PR #13 remains an open draft lane and already contains category/detail shells, real research staging, publication projection, priority projection and commercial fail-closed tests.
- PR #14 is a separate security/fixture lane that strengthens publisher timestamp validation. Its authority should be reused/reconciled when eventually incorporated; this batch must not duplicate timestamp authority.
- Historical AU/USA/legal PRs remain open. They are context, not permission to merge or rewrite this lane.
- V2 incremental draft PR #15 is based on `work/au-surveys-vertical-batch`, so V2 changes remain isolated from the original batch and from unrelated `main` work.

## Vertical objective

Drive one complete governed user journey as far as repository evidence permits:

`AU → Earn → Surveys → verified shortlist → comparison/read model → detail read model → publication gate → governed CTA boundary → runtime-ready contract`

Depth beats horizontal expansion.

## Current verified shortlist state

Informationally verified, commercially blocked:
- Octopus Group
- Pureprofile
- Prolific
- Ipsos iSay
- LifePoints
- Toluna
- OpinionWorld Australia
- Valued Opinions Australia

Research hold:
- YouGov AU reward detail

All real publisher relationships remain UNKNOWN. No real tracking destination is stored.

## Execution backlog, in priority order

### V2-1 — WordPress/API read-model contract — IMPLEMENTED / CI PENDING
Created `data/au/surveys.read-model-contract.json`.

The contract explicitly states:
- WordPress is not authoritative;
- canonical Rewards data/publication state/resolver are the authorities;
- category and detail record shapes are bounded;
- raw tracking/affiliate URLs are forbidden;
- lifecycle/freshness/commercial state cannot be editorially overridden;
- publisher economics cannot drive ranking;
- `commercial_action` remains null unless the canonical resolver authorises it.

### V2-2 — Projection drift and stale-state assurance — IMPLEMENTED / CI PENDING
Added `fixtures/au-surveys/test_read_model_contract.py`.

It verifies:
- staging, publication and priority projections have identical program identity sets;
- Flagship/Core/Secondary records are VERIFIED and CURRENT;
- non-verified records remain RESEARCH_HOLD/RESEARCH_REQUIRED;
- every current real record stays commercially BLOCKED with null destination;
- priority ranks are unique/contiguous;
- the priority projection contains no URLs, tracking parameters or commission-rate inputs.

### V2-3 — Comparison-detail deterministic mapping — IMPLEMENTED / CI PENDING
Added `fixtures/au-surveys/build_presentation_read_model.py` plus `test_presentation_read_model.py`.

The builder deterministically joins staging + publication + priority state by stable program ID, then emits presentation-safe list/detail fields with `commercial_action: null` for all current real records. Tests verify stable identity, contiguous ordering, current freshness for verified records, RESEARCH_HOLD behavior and commercial blocking.

### V2-4 — Runtime presentation verification — NEXT
Exercise the AU survey templates against bounded fixture/read-model data. Claim runtime verification only if actually exercised.

### V2-5 — Research depth — CONTINUOUS
Continue first-party AU verification only where it improves consumer choice. YouGov AU reward catalogue remains highest evidence gap. Add new programs only with material differentiation and strong first-party AU evidence.

### V2-6 — Commercial readiness ledger — BLOCKED BY EXTERNAL APPROVAL
Track publisher application/approval/destination evidence separately from consumer research. Public referral pages never count as publisher approval.

### V2-7 — Final vertical closure criteria
The AU Surveys vertical can only be called implementation-ready when:
- canonical source/read-model boundary is explicit;
- list/detail mapping is deterministic;
- stale/conflicting/partial evidence fails closed;
- exact-head CI passes;
- runtime template rendering is evidenced;
- no real commercial CTA is enabled without authenticated publisher approval and approved destination;
- independent Green/PRS evidence exists where required.

## Current execution commits

- `dfc96b5ceb45d19b656236101e9a0824902f9c81` — create V2 standing batch protocol.
- `87cd44b33742d24d1235de7844a42ca75cd75510` — define non-authoritative read-model contract.
- `214ee4e21734902d886c0bd71c24da9a2d037f62` — add read-model/drift assurance tests.
- `25fbaf30be9a3478f66bfe6b888d07166c6f9d87` — wire read-model tests into CI.
- `47381f5b65930f57e61ddd65f14702cd1181172b` — add deterministic presentation read-model builder.
- `c6a3bda2990834f0fa0ba596f4048f2eaf354e21` — add deterministic list/detail mapping tests.
- `a7937e307d394be89b37cc92df3b2144b603c5f9` — wire deterministic mapping tests into CI.

## Per-cycle maximum-value rule

A `cont` cycle should normally attempt, in order:
1. reconcile repo/PR/CI;
2. close one implementation gap;
3. close one assurance gap;
4. close one evidence/research gap;
5. update durable logs;
6. inspect exact-head verification.

If one item is externally blocked, immediately move to the next safe item instead of stopping.

## Governance invariants

- WordPress is presentation/editorial, not authority for volatile rewards, eligibility, affiliate approval, prices or destinations.
- Canonical Rewards data/resolver remains authoritative.
- Consumer referral and publisher affiliate relationship are separate.
- UNKNOWN remains UNKNOWN.
- VERIFIED consumer evidence does not imply PUBLISHABLE or commercially eligible.
- Publisher economics must never control consumer ranking.
- No production tracking URL in editorial content or staging projections.
- Stale/conflicting evidence fails closed.
- No merge/deploy/ready/credential/account/application/purchase/contact/live activation without separate owner authority.
