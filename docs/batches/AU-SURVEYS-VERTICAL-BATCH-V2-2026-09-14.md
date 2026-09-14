# AU Surveys Vertical Batch V2 — 2026-09-14

**Workstream:** Affiliate Websites → Australia → Earn → Surveys  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Branch:** `work/au-surveys-vertical-batch-v2`  
**Mode:** maximum-value vertical autonomous execution  
**Status:** ACTIVE — runtime-ready presentation seam now CI-verified  
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

## Fresh scan snapshot — current cycle

- `main` advanced independently to `661370c4226ca45e97239a728e6b3483d65c5d6e` with Software & Games Batch 002 closure. This is a separate lane; no rebase/merge performed.
- AU Surveys PR #15 remains open, draft and mergeable, based on `work/au-surveys-vertical-batch`.
- PR #14 remains a separate timestamp-security lane; this batch does not duplicate its timestamp authority.
- Exact pre-cycle PR #15 head `6ab57d82f25307b162508d3cddcb42d3691e8f36` had Commercial CTA fixture validation SUCCESS.
- No Docker/`wp-env`/full WordPress runtime harness exists in the repository. This cycle therefore implemented and exercised the smallest real executable presentation seam inside the theme without fabricating a full WordPress runtime claim.

## Vertical objective

Drive one complete governed user journey as far as repository evidence permits:

`AU → Earn → Surveys → verified shortlist → comparison/read model → detail read model → publication gate → governed CTA boundary → runtime-ready presentation seam`

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

### V2-1 — WordPress/API read-model contract — IMPLEMENTED / CI-VERIFIED
Created `data/au/surveys.read-model-contract.json`.

The contract explicitly states:
- WordPress is not authoritative;
- canonical Rewards data/publication state/resolver are the authorities;
- category and detail record shapes are bounded;
- raw tracking/affiliate URLs are forbidden;
- lifecycle/freshness/commercial state cannot be editorially overridden;
- publisher economics cannot drive ranking;
- `commercial_action` remains null unless the canonical resolver authorises it.

### V2-2 — Projection drift and stale-state assurance — IMPLEMENTED / CI-VERIFIED
`fixtures/au-surveys/test_read_model_contract.py` verifies identity-set parity, current freshness for ranked verified records, research-hold behavior, commercial blocking, rank uniqueness and absence of URL/tracking/commission inputs.

### V2-3 — Comparison-detail deterministic mapping — IMPLEMENTED / CI-VERIFIED
`fixtures/au-surveys/build_presentation_read_model.py` plus `test_presentation_read_model.py` deterministically join staging + publication + priority state by stable program ID. List/detail presentation receives bounded fields and `commercial_action: null` for all current real records.

### V2-4 — Executable presentation verification — IMPLEMENTED / EXACT-HEAD CI GREEN
Added `wp-content/themes/affiliate-master/inc/au-surveys-renderer.php` as a pure PHP presentation renderer. It never loads staging/canonical data and never resolves affiliate URLs.

Added `fixtures/au-surveys/test_theme_renderer.php`, which executes that exact renderer against the generated governed read model and verifies:
- verified records render;
- RESEARCH_REQUIRED records are excluded from the verified list and fail closed on detail;
- blocked state emits no `<a>` link or URL;
- injected blocked commercial actions are ignored;
- untrusted text is HTML-escaped;
- commercial blocking remains visible to the user.

`functions.php` now exposes a presentation-only WordPress seam through:
- `affiliate_master_au_surveys_read_model` filter;
- `[affiliate_au_surveys_list]` shortcode;
- `affiliate_master_au_survey_program_id` filter;
- `[affiliate_au_survey_detail]` shortcode.

The theme does not read `data/au/*.json` directly. If no governed provider supplies records/context, the UI fails closed to unavailable/informational output.

The AU category/detail templates now call the governed shortcodes instead of embedding synthetic comparison rows as apparent runtime content.

Exact executable head: `03643ca8fd423a2462c0205cadc4f87f5ec7f8dc`.

GitHub Actions evidence at that exact head:
- Theme Validation run `34826642659` — SUCCESS;
- Commercial CTA fixture validation run `34826642642` — SUCCESS.

This verifies the executable PHP presentation seam and its fail-closed behavior. It does **not** claim a full WordPress+database browser session because the repo has no such runtime harness yet.

### V2-5 — Research depth — CONTINUOUS
Fresh YouGov first-party recheck completed on 2026-09-14. Current official YouGov material verifies the global member model: paid survey/data-sharing activity in points, Wallet accumulation, reward conversion and fair-reward principles. It still did not surface sufficiently direct AU-specific member reward-catalogue evidence to justify promotion. `yougov-au` therefore remains RESEARCHED / RESEARCH_REQUIRED / RESEARCH_HOLD.

Do not substitute the 2026 global Reality Report examples (bank transfer/Amazon/ASOS/Asda) for an AU-specific reward catalogue.

### V2-6 — Commercial readiness ledger — BLOCKED BY EXTERNAL APPROVAL
Publisher application/approval/destination evidence remains separate from consumer research. Public referral pages never count as publisher approval.

### V2-7 — Full browser/runtime verification — OPEN
The remaining runtime gap is a real WordPress environment/browser session. Do not claim this until an actual WordPress runtime exists and the category/detail pages are rendered through it with a governed provider fixture/adapter.

### V2-8 — Final vertical closure criteria
The AU Surveys vertical can only be called implementation-ready when:
- canonical source/read-model boundary is explicit;
- list/detail mapping is deterministic;
- stale/conflicting/partial evidence fails closed;
- exact-head CI passes;
- executable presentation renderer is exercised;
- full WordPress/browser rendering is evidenced;
- no real commercial CTA is enabled without authenticated publisher approval and approved destination;
- independent Green/PRS evidence exists where required.

## Current execution commits

Earlier V2 tranche:
- `dfc96b5ceb45d19b656236101e9a0824902f9c81` — create V2 standing batch protocol.
- `87cd44b33742d24d1235de7844a42ca75cd75510` — define non-authoritative read-model contract.
- `214ee4e21734902d886c0bd71c24da9a2d037f62` — add read-model/drift assurance tests.
- `25fbaf30be9a3478f66bfe6b888d07166c6f9d87` — wire read-model tests into CI.
- `47381f5b65930f57e61ddd65f14702cd1181172b` — add deterministic presentation read-model builder.
- `c6a3bda2990834f0fa0ba596f4048f2eaf354e21` — add deterministic list/detail mapping tests.
- `a7937e307d394be89b37cc92df3b2144b603c5f9` — wire deterministic mapping tests into CI.

Current runtime-ready tranche:
- `eba9993527c2451fbb37a6e8cf50052bda9314d7` — pure PHP AU surveys renderer.
- `7fcc6a5523c21ce48a6a60d5a8de30697ad715d9` — executable renderer assurance test.
- `3d04ee331fd1486f1d2dea052ddf2a8e7aee0d7e` — Theme Validation executes governed renderer.
- `dbee2c82b2c7c9029967ba4deefcf015dc11ff6f` — WordPress filter/shortcode presentation seam.
- `d90e241d52557a0079c205f2bcbb4be237c312a1` — category template governed renderer binding.
- `03643ca8fd423a2462c0205cadc4f87f5ec7f8dc` — detail template governed renderer binding; exact-head Theme + Commercial CTA CI GREEN.

## Next highest-value safe actions

1. Fresh-scan before any mutation.
2. Reconcile any newer `main`, PR #13/#14/#15 and CI changes.
3. Establish the smallest bounded real WordPress runtime harness only if it can reuse existing theme/data authority without creating a parallel deployment architecture.
4. Exercise category and detail pages in a browser/runtime if the harness exists; capture evidence and test unavailable-provider behavior.
5. Add accessibility/semantic checks for generated list/detail HTML where they materially improve user safety/usability.
6. Continue YouGov AU-specific reward-catalogue research; keep hold if country-specific evidence remains insufficient.
7. Keep publisher approvals/destinations blocked pending authenticated external evidence.

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
