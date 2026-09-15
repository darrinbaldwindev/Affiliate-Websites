# AU Surveys Vertical Batch V2 — 2026-09-14

**Workstream:** Affiliate Websites → Australia → Earn → Surveys  
**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Branch:** `work/au-surveys-vertical-batch-v2`  
**Mode:** maximum-value vertical autonomous execution  
**Status:** ACTIVE — WordPress presentation contract seam CI-verified  
**Standing trigger:** whenever the owner says `cont` or `continue autonomously`, execute this protocol again from a fresh repository scan.

## Owner instruction

Each autonomous cycle MUST fresh-scan `main`, this branch, relevant PRs and CI; reconcile concurrent changes; execute the highest-value safe vertical tranche; add fail-closed assurance; inspect exact-head evidence; update durable logs; and move to another safe task if external credentials/approval block one path. No merge, deploy, ready transition, credential change, account application, purchase, third-party contact or live commercial activation without separate authority.

Evidence controls completion. No overall GREEN from implementation claims alone.

## Fresh scan snapshot — 2026-09-15 cycle

- `main` advanced independently to `d3cf400aabe631dc6c2e37193eca8b192856eaba`, most recently recording the UK technology vertical batch. This is a concurrent lane; no rebase/merge performed.
- AU Surveys PR #15 remains open, draft, mergeable and unmerged, based on `work/au-surveys-vertical-batch`.
- Pre-cycle PR #15 head `9b135262c8d399db4c1fc34740808e3b7ad6b07c` had both Theme Validation and Commercial CTA fixture validation SUCCESS.
- Repository still has no full WordPress+database+browser harness. This cycle therefore strengthened the real theme bootstrap/presentation contract seam without fabricating browser-runtime evidence.

## Vertical objective

`AU → Earn → Surveys → verified shortlist → comparison/read model → detail read model → publication gate → governed CTA boundary → WordPress presentation seam → full runtime/browser evidence`

Depth beats horizontal expansion.

## Current consumer shortlist

Informationally verified, commercially blocked: Octopus Group, Pureprofile, Prolific, Ipsos iSay, LifePoints, Toluna, OpinionWorld Australia, Valued Opinions Australia.

Research hold: YouGov AU reward detail.

All real publisher relationships remain UNKNOWN. No real tracking destination is stored.

## Completed V2 tranches

### V2-1 — WordPress/API read-model contract — CI-VERIFIED
`data/au/surveys.read-model-contract.json` defines a non-authoritative presentation contract. WordPress is not authority; raw tracking/affiliate URLs are forbidden; publisher economics cannot drive ranking; commercial action remains null unless canonical resolution authorises it.

### V2-2 — Projection drift/staleness assurance — CI-VERIFIED
`fixtures/au-surveys/test_read_model_contract.py` verifies identity parity, freshness/ranking constraints, research-hold behavior, commercial blocking and absence of tracking/commission ranking inputs.

### V2-3 — Deterministic comparison/detail mapping — CI-VERIFIED
`build_presentation_read_model.py` + `test_presentation_read_model.py` join staging/publication/priority by stable program ID and preserve fail-closed commercial state.

### V2-4 — Executable presentation renderer — CI-VERIFIED
`wp-content/themes/affiliate-master/inc/au-surveys-renderer.php` is a pure PHP presentation renderer. It does not load canonical/staging data or resolve affiliate URLs. Tests prove verified records render, research-hold records fail closed, blocked records emit no links/URLs, injected blocked actions are ignored, and untrusted text is escaped.

### V2-5 — WordPress bootstrap/presentation seam — IMPLEMENTED / EXACT-HEAD CI GREEN
`functions.php` registers the presentation-only filters and shortcodes used by the AU category/detail templates.

Added `fixtures/au-surveys/test_wordpress_presentation_seam.php`, a bounded WordPress-contract harness that executes the real theme bootstrap with minimal WordPress function stubs. It verifies:
- both AU Surveys shortcodes register from the real `functions.php`;
- no governed provider => list/detail fail closed;
- a governed record reaches list and detail through the same stable identity;
- BLOCKED commercial state survives the WordPress seam and emits no links;
- unknown requested program ID cannot fall through to another record;
- malformed provider output fails closed.

Updated Theme Validation to syntax-check and execute this harness and to assert the AU templates contain the expected governed shortcodes.

Implementation commits:
- `8455c2406eed06b42ee739619b80d8b351b11405` — WordPress presentation-seam assurance harness;
- `44d66031135c70ca7c4f5978183fbf7e070ff8fd` — CI execution and template-wiring checks.

Exact-head evidence at `44d66031135c70ca7c4f5978183fbf7e070ff8fd`:
- Theme Validation run `34917641023` / job `104218630922` — SUCCESS; `Exercise WordPress presentation seam` passed;
- Commercial CTA fixture validation run `34917640911` / job `104218630513` — SUCCESS.

This is stronger executable evidence of the theme/WordPress contract boundary. It is deliberately **not** labelled full WordPress/browser verification because no actual WordPress database/server/browser session was run.

### V2-6 — Research depth — CONTINUOUS
YouGov remains RESEARCHED / RESEARCH_REQUIRED / RESEARCH_HOLD. Existing first-party evidence supports the global points/rewards model and Australia as a panel market but not a sufficiently direct AU-specific member reward catalogue. Do not substitute global examples for AU-specific rewards.

### V2-7 — Commercial readiness — EXTERNALLY BLOCKED
Publisher application/approval/destination evidence remains separate from consumer research. Public referral pages never count as publisher approval.

### V2-8 — Full WordPress/browser verification — OPEN
Remaining runtime gap: an actual WordPress environment with database/server plus browser route rendering. Do not create a competing production/deployment architecture merely to satisfy a test. Prefer a bounded disposable CI/dev harness if one can be added safely and reused across country verticals.

## Next highest-value safe actions

1. Fresh-scan before mutation and reconcile newer shared-main work.
2. Design the smallest **reusable cross-country disposable WordPress runtime harness**, not an AU-only deployment stack; first inspect whether concurrent UK/US work has created such a seam.
3. If safe, boot WordPress with the Affiliate Master theme and a fixture provider, then verify AU category/detail routes and fail-closed no-provider behavior.
4. Add semantic/accessibility assertions for generated list/detail output (heading structure, status text, no deceptive CTA, useful empty/research states).
5. Continue AU evidence depth only where it improves consumer choice; keep YouGov on hold absent AU-specific reward evidence.
6. Keep all publisher approvals and real destinations blocked pending authenticated evidence.

## Final closure criteria

The AU Surveys vertical is not overall GREEN until the canonical source/read-model boundary, deterministic mapping, stale/conflict failure, exact-head CI, executable presentation, full WordPress/browser rendering, commercial approval gates and required independent assurance are all evidenced.

## Governance invariants

- WordPress is presentation/editorial, never authority for volatile rewards, eligibility, affiliate approval, prices or destinations.
- Canonical Rewards data/resolver remains authoritative.
- Consumer referral and publisher affiliate relationship are separate.
- UNKNOWN remains UNKNOWN.
- VERIFIED consumer evidence does not imply PUBLISHABLE or commercially eligible.
- Publisher economics never controls consumer ranking.
- No production tracking URL in editorial content or staging projections.
- Stale/conflicting evidence fails closed.
- No merge/deploy/ready/credential/account/application/purchase/contact/live activation without separate owner authority.
