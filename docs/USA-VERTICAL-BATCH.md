# USA Affiliate Website — Vertical Batch Operating File

**Workstream:** USA Affiliate Website  
**Standing trigger:** `cont` or `continue autonomously`  
**Execution mode:** vertical, evidence-first, highest-value incomplete slice  
**Branch:** `usa/intelligence-contract` unless explicitly superseded  
**Governance:** country-workstream contribution only; do not silently modify master architecture, merge, deploy, rebase, alter credentials, or create duplicate control-plane infrastructure.

## Purpose

Make each autonomous batch do as much useful, verifiable work as possible while keeping communication compact. Every batch starts from current repository evidence, not from memory or the previous batch alone.

## Batch algorithm

Whenever the owner says `cont` or `continue autonomously`, execute the following sequence without waiting for another prompt unless genuinely blocked by unavailable authority or credentials.

### 1. Rescan current repository state

Inspect current `main`, recent commits, relevant open PR/issue state, current USA branch state, applicable master contracts, fixtures/tests, and any files changed since the previous batch.

Minimum checks:
- latest `main` head and recent commit intent;
- `main...usa/intelligence-contract` divergence;
- USA PR state and changed files;
- master API/architecture/commercial CTA contracts that affect the USA workstream;
- current USA research/registry files;
- relevant CI/test evidence where available.

Do not create a new branch merely because the existing USA branch is stale. Surface divergence explicitly.

### 2. Reconcile before adding work

Classify each current USA artifact as:
- **CURRENT** — aligned to current master contracts;
- **NEEDS UPDATE** — useful but missing newer master requirements;
- **SUPERSEDED** — replaced by a stronger current contract;
- **CONFLICT** — incompatible with current master behavior;
- **MERGE CANDIDATE** — reusable idea worth master review.

Never silently choose between conflicting evidence or contracts.

### 3. Choose one vertical objective

Select the smallest slice that creates the largest practical movement toward a commercially useful USA site. Prefer, in order:
1. publishability blockers for high-value USA programs;
2. commercial relationship verification;
3. eligibility/reward/privacy/disclosure evidence needed by the governed CTA contract;
4. structured registry/API readiness;
5. high-value opportunity expansion where the launch set is weak;
6. SEO/AEO/content assets only after evidence and destination readiness exist.

Avoid broad horizontal research when a narrower blocker can be closed.

### 4. Execute a full evidence bundle

For each program or opportunity touched, separate:
- consumer proposition;
- US availability and eligibility;
- reward/incentive evidence;
- publisher affiliate relationship;
- participant/member referral relationship;
- B2B referral/affiliate relationship;
- attribution/qualification event;
- traffic restrictions;
- disclosure requirements;
- identity/privacy/data-sensitivity burden;
- program-status freshness;
- commercial-term freshness;
- conflicts and UNKNOWNs.

Current first-party or network evidence outranks third-party summaries. Historical figures remain historical.

### 5. Map to the master runtime contract

Every candidate intended for a CTA must be able to populate the master Rewards API/read-model and governed commercial click flow:

`visitor → country → program/product/merchant → eligibility → approved current commercial relationship → destination → tracked outbound click`

Country research must not embed raw affiliate tracking URLs into editorial content.

Before calling a candidate CTA-ready, require enough evidence to satisfy current country CTA validation: country/program coverage, eligibility, disclosure, evidence state/freshness, relationship separation, approved destination state, and auditability.

### 6. Produce a durable repository result

Prefer updating the existing USA branch/PR with one coherent artifact over creating multiple documents or branches. Valid outputs include:
- registry update;
- verification matrix;
- reconciliation report;
- publication gate;
- content brief backed by verified data;
- fixture/input proposal for master review;
- PR handoff/comment.

Do not claim a write until it has been fetched or otherwise independently verified.

### 7. Verify the batch

At minimum verify:
- repository write exists at the claimed path/ref;
- monetary/commercial claims retain source and status;
- referral and publisher affiliate data are not conflated;
- UNKNOWN remains UNKNOWN;
- no master contract was silently overridden;
- no duplicate branch/control layer was created.

If runnable tests or CI evidence exist for touched implementation contracts, inspect them. Do not claim tests passed unless evidence exists.

### 8. Record batch closure

Each batch report should state only what materially changed:
- **Repo state** — current baseline/divergence;
- **Objective executed**;
- **Evidence gained or contradictions found**;
- **Repository artifact/commit/PR update**;
- **Verification**;
- **Remaining blocker**;
- **Next vertical objective**.

## USA launch priority model

### Tier 1 — monetisable + useful
Programs with strong consumer value and verified publisher/B2B monetisation receive first verification effort.

Current leading cluster includes Freecash, User Interviews, Survey Junkie, Ipsos iSay, Branded Surveys, and other candidates whose current commercial relationship can be proven.

### Tier 2 — useful but monetisation incomplete
High-value research/testing opportunities such as Dscout, PlaybookUX, uTest, TestingTime, Userlytics, CloudResearch Connect, Respondent, Fieldwork, Sago and similar programs may be recommended editorially only when consumer evidence is current; publisher economics stay UNKNOWN unless independently verified.

### Tier 3 — specialist/high-risk
Health, clinical, passive-data, finance, legal or similarly sensitive opportunities require additional governance and must not be promoted solely because of payout.

## Standing merge candidates

Preserve these USA-derived concepts for master review:
- separate consumer value from publisher monetisation;
- separate publisher affiliate, participant referral, B2B referral and creator relationships;
- separate program-status verification date from commercial-term verification date;
- attribution/qualification as first-class data;
- privacy/data-sensitivity adjustment;
- matching-engine fields by activity, time, device, geography, reward preference and privacy tolerance.

## Stop conditions

Continue within the batch until one of these occurs:
- the chosen vertical objective is verified complete;
- the next action requires unavailable credentials/application acceptance/private network terms;
- further action would require merge/deploy/rebase/production write or other authority not granted;
- current evidence is insufficient and the uncertainty has been explicitly recorded.

Then select the next safe vertical objective in the next batch.
