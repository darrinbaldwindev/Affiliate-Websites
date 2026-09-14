# UK Vertical Autonomous Batch — 2026-09-14

**Workstream:** United Kingdom Affiliate Website  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Mode:** vertical autonomous execution  
**Status:** COMPLETE — bounded repository batch executed  
**Rule:** evidence controls completion; research claims are not production truth.

## Standing trigger

When the owner says **`cont`** or **`continue autonomously`** in this workstream, execute this cycle without asking for confirmation unless a safety/governance boundary requires it:

1. scan current repository state and recent relevant evidence;
2. reconcile completed work, stale assumptions, blockers and highest-value gaps;
3. create or update the current vertical batch;
4. execute as many bounded tasks in the batch as practical;
5. verify resulting repository state and available CI evidence;
6. record completed work, unresolved risks and the smallest useful next batch.

Do not create duplicate architecture, canonical stores, schedulers, governance systems or country-specific forks of reusable master code.

## Repository scan baseline

Current repository evidence shows the project has progressed beyond the older high-level status wording. The tree includes:

- lightweight WordPress Block Theme and master UX contracts;
- country configuration and API contracts;
- canonical rewards data contract;
- governed commercial-CTA contract/server seam;
- commercial-CTA fixture and CI workflow;
- legal page register;
- AU vertical-slice contract/readiness/fixture material;
- Level-2 AgentOS workload fixture;
- UK affiliate opportunity ranking/research.

The UK workstream therefore should not duplicate AU/master architecture. Its highest-value work is to turn UK research into structured, reusable country data/governance and a UK-specific acceptance path.

## Batch objective

Convert the UK opportunity research into an implementation-ready, governance-safe UK vertical package while preserving the master architecture and separating volatile commercial research from production truth.

## Task results

### B1 — Repo reconciliation — COMPLETE

Verified current repository tree, master README/data boundary, canonical rewards data contract, AU vertical-slice precedent and current UK opportunity research before writing new artifacts.

Important reconciliation finding: the repository contains newer commercial-CTA, canonical-data, legal, Level-2 and vertical-slice artifacts that are not fully reflected in older status wording. Work in this batch used the newer repository evidence rather than duplicating those systems.

### B2 — Structured UK research register — COMPLETE

Created:

`docs/data/uk-affiliate-opportunity-research.json`

The register contains UK-only research candidates with stable IDs, categories, networks/commercial models, feed/comparison signals, regulatory-risk classes, research state and freshness state.

Safety boundaries:
- research-only;
- no live tracking URLs;
- no claim of programme approval;
- volatile terms require re-verification;
- production truth remains behind the canonical data/API workflow.

### B3 — UK commercial scoring matrix — COMPLETE

Created:

`docs/UK-COMMERCIAL-SCORING-MATRIX-2026-09-14.md`

The matrix separates:
- launch cohort;
- expansion cohort;
- regulated/hold cohort.

The scores are prioritisation judgements, not measured conversion performance. High commercial value cannot bypass verification or publishability gates.

### B4 — UK vertical-slice contract — COMPLETE

Created:

`docs/vertical-slice/UK-VERTICAL-SLICE-CONTRACT.md`

Target journey:

`Global → UK → Category → Guide/Comparison → Detail → Governed Commercial CTA`

Recommended first fixture-safe category: technology/appliances, because it exercises comparison/feed/CTA/trust behaviour with less regulatory complexity than insurance/finance.

### B5 — UK publishability gate — COMPLETE

Created:

`docs/UK-PUBLISHABILITY-GATE-2026-09-14.md`

Defined common publication requirements, freshness classes and six UK risk classes:

1. ordinary retail/product affiliate;
2. telecom/broadband;
3. travel;
4. insurance/financial promotion;
5. health-sensitive content;
6. utilities/home-energy lead generation.

Insurance/financial promotion defaults to HOLD until enhanced compliance evidence is satisfied. Broadband must use a separate telecom gate rather than ordinary retail rules.

### B6 — Implementation mapping — COMPLETE

The new artifacts preserve the existing boundary:

- UK research register = staging/research evidence;
- canonical structured data = PostgreSQL/Supabase behind Rewards API;
- WordPress = approved presentation data only;
- affiliate destination = shared controlled resolver;
- AgentOS = research/verification/monitoring/orchestration.

No alternate UK source of truth was created.

### B7 — Verification and log — COMPLETE WITH EXPLICIT LIMITS

Verified `main` after writes. The UK publishability-gate commit became current `main` head during verification.

Relevant commits in this batch:
- `9d24c433d071a43f48de53c987234a0ca7320b44` — batch file created;
- `20eeccd46aaccac3a823fa51d6da88691b60e5f9` — structured UK research register;
- `8e694313eca12dda925672258ede3e429aa2514c` — UK commercial scoring matrix;
- `a613dfe44846cb107896af230a3e95554cc8ae1a` — UK vertical-slice contract;
- `12a53a13d3e935b58a20d9ec8e42d83d7d5a07ba` — UK publishability gate.

Repository activity also showed concurrent AU vertical-batch work with a successful Theme Validation run on AU pull request #13. That CI success is useful repository-health evidence but is **not** claimed as validation of this UK documentation batch.

## Still OPEN

The following are not claimed complete:

- live UK programme approvals;
- current production affiliate destinations;
- current rates/prices/stock/offers;
- production Rewards API/Supabase integration;
- UK WordPress/browser rendering;
- accessibility/Core Web Vitals verification;
- end-to-end affiliate tracking;
- regulated-category legal/compliance approval;
- runtime tests proving stale/unapproved UK destinations fail closed.

## Next vertical batch

On the next `cont` / `continue autonomously`:

1. re-scan repo and concurrent PR/main movement;
2. inspect existing commercial-CTA fixture implementation in detail;
3. build a **UK fixture dataset** matching the shared commercial-CTA contract;
4. add bounded negative tests for UK stale, unapproved, wrong-country and regulated-gate failures without creating a second resolver;
5. add the first UK country/category fixture shell only if it can reuse the master theme cleanly;
6. verify CI and record exact evidence.

## Completion rule

A batch is complete when bounded repository artifacts are created/updated and their state is verified. Items requiring live merchant approval, credentials, production infrastructure, legal review or browser/runtime evidence remain explicitly OPEN rather than being inferred complete.
