# Software & Games Vertical Autonomous Batch 004 — 2026-09-15

**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Branch:** `work/software-games-batch-004`  
**PR:** #20  
**Mode:** vertical autonomous execution  
**Status:** COMPLETE ON BRANCH — PR OPEN, NOT MERGED

## Fresh scan baseline

Fresh scan of `main` found head `d3cf400aabe631dc6c2e37193eca8b192856eaba`. Batch 003 was closed. The canonical Software & Games journey and `fixtures/commercial-cta` validator remained the governing seams. Concurrent country work had expanded the shared workflow, so this batch correctly isolated changes on a branch rather than writing directly to `main`.

## Objective achieved

The batch turns existing offer assurance fields into a normalized comparison contract and deterministic ranking layer without creating a second commerce store or allowing affiliate economics to influence consumer ranking.

## Task results

- SG4-1 fresh repo/concurrency reconciliation — COMPLETE
- SG4-2 canonical normalized `software_offer` contract — COMPLETE
- SG4-3 fixture/research source mappings for GMG, GOG, Fanatical and Gamers-Outlet — COMPLETE
- SG4-4 duplicate-SKU/identity and contradictory-evidence detection — COMPLETE
- SG4-5 three independent ranking modes — COMPLETE
- SG4-6 commission/EPC/network-bonus ranking independence tests — COMPLETE
- SG4-7 tests wired into existing commercial fixture CI — COMPLETE
- SG4-8 exact-head CI verification — COMPLETE

## Implemented ranking modes

1. `lowest_observed_price` — price order only among publishable offers inside the same normalized equivalence group.
2. `best_verified_value` — deterministic consumer-value score using assurance, licence utility and price; affiliate economics excluded.
3. `highest_assurance` — merchant class, evidence and provenance assurance; affiliate economics excluded.

## New fail-closed controls

- incomplete merchant/SKU/region identity;
- duplicate identity records;
- contradictory material evidence for the same identity;
- cross-equivalence competition prevented by grouping;
- unpublishable offers excluded from ranking.

## Commission independence

Automated tests mutate affiliate commission from 0 through extreme values and add extreme EPC/network bonuses. Ranking signatures for all three modes must remain unchanged. This establishes a regression guard against affiliate economics contaminating consumer trust/value ordering.

## CI evidence

PR head before closure documentation: `e2ed29a84bbae207cd6508f3b4a07c531ba8bdc7`.

Commercial CTA fixture workflow run `34917427349`, job `104217987765`:

- existing country CTA validation — success
- governed UK CTA validation — success
- UK technology vertical slice — success
- existing Software & Games offer validation — success
- governed CTA + Software & Games assurance/ranking tests — success
- UK vertical-slice negative cases — success

The job completed all substantive and cleanup steps successfully. The final workflow wrapper was still updating when inspected, but every job step including `Complete job` reported success.

## Durable artifacts

- `docs/data/software-offer-normalized-contract.json`
- `docs/SOFTWARE-GAMES-SOURCE-MAPPING-2026-09-15.md`
- `fixtures/commercial-cta/rank_software_games_offers.py`
- `fixtures/commercial-cta/test_software_games_ranking.py`
- `.github/workflows/commercial-cta-fixture.yml` updated to execute ranking assurance tests

## Governance / residual risk

No merge or deployment was performed. No live affiliate URL, credential, merchant application or purchase was created. Source mappings remain research-level until actual programme approval/feed access exists. Production SKU normalization, live price freshness, legal licence provenance and country-specific approval remain OPEN.

## Next vertical batch

1. fresh scan `main` and PR #20 status before any new write;
2. reconcile/merge only when independently safe and requested/allowed by portfolio governance;
3. create normalized synthetic multi-merchant Windows/Office comparison fixtures using the new contract;
4. add price-observation timestamps/expiry policy rather than trusting a manual freshness label;
5. add evidence-reference identity/hash and contradictory-source precedence rules;
6. define presentation payload for three ranking modes without exposing affiliate economics;
7. extend to antivirus/games only after the Windows/Office slice remains fail-closed.
