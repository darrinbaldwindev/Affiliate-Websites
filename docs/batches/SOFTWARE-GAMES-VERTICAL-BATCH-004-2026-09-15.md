# Software & Games Vertical Autonomous Batch 004 — 2026-09-15

**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Branch:** `work/software-games-batch-004`  
**Mode:** vertical autonomous execution  
**Status:** IN EXECUTION

## Fresh scan baseline

Fresh scan of `main` found head `d3cf400aabe631dc6c2e37193eca8b192856eaba`. Batch 003 is closed. The canonical Software & Games journey and `fixtures/commercial-cta` validator remain the governing seams. Concurrent country work has expanded the shared workflow, so this batch uses a branch rather than writing directly to `main`.

## Objective

Turn the existing offer assurance fields into a canonical normalized comparison contract and deterministic ranking layer without creating a second commerce store or allowing affiliate economics to influence trust.

## Tasks

- SG4-1 fresh repo/concurrency reconciliation — COMPLETE
- SG4-2 define canonical normalized `software_offer` contract — IN EXECUTION
- SG4-3 define fixture-level source mappings for GMG, GOG, Fanatical and Gamers-Outlet — OPEN
- SG4-4 add duplicate-SKU and contradictory-evidence detection — OPEN
- SG4-5 implement three independent ranking modes — OPEN
- SG4-6 prove commission cannot alter trust/equivalence ranking — OPEN
- SG4-7 wire tests into existing commercial fixture CI — OPEN
- SG4-8 verify exact-head CI and close batch — OPEN

## Required ranking modes

1. `lowest_observed_price` — only among publishable, equivalent offers.
2. `best_verified_value` — deterministic consumer-value score using assurance and licence utility; affiliate commission excluded.
3. `highest_assurance` — merchant/provenance/evidence assurance only; affiliate commission excluded.

## Hard rules

- Affiliate commission, EPC, bounty, network incentives and payout terms MUST NOT influence trust, equivalence, publishability or consumer-value ranking.
- Offers may only compete as like-for-like when their normalized equivalence group matches.
- Duplicate merchant/SKU/region records and contradictory evidence fail closed.
- Source mappings are research/fixture mappings, not proof of live feed access or merchant approval.
- No production affiliate links, credentials, applications, purchases, merges or deployments.
