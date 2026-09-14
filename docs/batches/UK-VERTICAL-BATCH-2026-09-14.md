# UK Vertical Autonomous Batch — 2026-09-14

**Workstream:** United Kingdom Affiliate Website  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Mode:** vertical autonomous execution  
**Status:** ACTIVE  
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

## Task stack

### B1 — Repo reconciliation
**Goal:** prove current state before editing.

Acceptance:
- inspect repository tree;
- inspect master README/architecture/data boundary;
- inspect AU vertical-slice contract as reusable precedent;
- inspect current UK opportunity ranking;
- identify stale status statements without treating them as current implementation evidence.

### B2 — Structured UK research register
**Goal:** create a machine-readable research-only candidate dataset aligned with the canonical data contract.

Acceptance:
- UK-only records;
- stable slugs/IDs;
- category/network/model fields;
- research status and freshness metadata;
- no live tracking URLs;
- no claim that affiliate approval exists;
- volatile rates treated as evidence snapshots, not production configuration.

### B3 — UK commercial scoring matrix
**Goal:** rank candidates by usefulness, not headline commission.

Score 0–5 on:
- revenue potential;
- purchase/lead intent;
- AOV/CPA potential;
- content/search depth;
- catalogue breadth;
- feed/API suitability;
- UK fit;
- trust;
- programme stability;
- restriction/validation risk;
- regulatory risk;
- comparison suitability;
- useful editorial depth.

Produce:
- launch cohort;
- expansion cohort;
- regulated/hold cohort;
- explicit UNKNOWNs.

### B4 — UK vertical-slice contract
**Goal:** define the UK country acceptance path using the reusable master architecture.

Target journey:

`Global → UK → Category → Guide/Comparison → Detail → Governed Commercial CTA`

No hard-coded commission, price, tracking URL, cookie duration, approval state or volatile promotion in WordPress templates.

### B5 — UK publishability gate
**Goal:** prevent high-paying but unsafe/stale/regulatory-sensitive candidates becoming publishable merely because they monetize well.

Must distinguish:
- ordinary retail/product affiliate programmes;
- telecom/broadband;
- travel;
- insurance/financial promotions;
- health-sensitive claims;
- utilities/home-energy lead generation.

Regulated or high-risk categories require a stronger evidence/compliance gate before any commercial CTA can be production-enabled.

### B6 — Implementation mapping
**Goal:** map UK research to existing master contracts instead of creating a country-specific data silo.

Expected boundary:
- research register = staging evidence;
- canonical structured data = Supabase/Postgres behind Rewards API;
- WordPress = approved presentation data only;
- affiliate destination = controlled resolver;
- AgentOS = research/verification/monitoring/orchestration.

### B7 — Verification and log
**Goal:** verify repository writes and CI state, then update this batch with results.

Do not claim browser rendering, live programme approval, end-to-end tracking, accessibility, Core Web Vitals or production affiliate resolution without evidence.

## Execution order

1. B1 repository reconciliation — execute first.
2. B2 structured UK research register.
3. B3 commercial scoring matrix.
4. B4 UK vertical-slice contract.
5. B5 UK publishability gate.
6. B6 map outputs to master architecture.
7. B7 verify files/CI and record results.

## Completion rule

A batch is complete when bounded repository artifacts are created/updated and their state is verified. Items requiring live merchant approval, credentials, production infrastructure, legal review or browser/runtime evidence remain explicitly OPEN rather than being inferred complete.
