# Software & Games Vertical Autonomous Batch 003 — 2026-09-14

**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Mode:** vertical autonomous execution  
**Status:** IN EXECUTION  
**Rule:** extend the canonical commercial CTA seam; do not create parallel commerce truth.

## Fresh scan baseline

Fresh scan confirmed Batch 002 is on `main` at `661370c4226ca45e97239a728e6b3483d65c5d6e`, with fixture-only Software & Games validation under `fixtures/commercial-cta/` and CI already wired.

Current machine gates cover country, currency, price freshness, licence type, merchant approval, marketplace provenance, disclosure and safe fixture URLs.

## Objective

Close the next false-equivalence risks for Windows/Office/productivity comparisons:

1. transferability status;
2. account binding status;
3. device/install count;
4. activation platform/method;
5. exact edition/SKU identity;
6. explicit equivalence-group matching before offers can be compared as like-for-like.

## Tasks

- SG3-1 fresh repo reconciliation — COMPLETE
- SG3-2 extend synthetic offer fixture with licence-detail fields — IN EXECUTION
- SG3-3 extend deterministic evaluator with fail-closed licence-detail gates — IN EXECUTION
- SG3-4 add negative assurance tests for each new gate — IN EXECUTION
- SG3-5 run/verify existing CI on exact head — OPEN
- SG3-6 document affiliate-account prerequisites for GMG, GOG, Fanatical and one software-key merchant — OPEN
- SG3-7 close batch with exact commits, residual risks and next slice — OPEN

## Hard rules

- Unknown transferability/account-binding/device count/activation details block Windows/Office/productivity publication.
- Offers must not be described as equivalent unless `product_family`, `edition`, `licence_type`, and `equivalence_group` match the intended comparison class.
- Synthetic fixture data is not production merchant truth.
- No live affiliate URLs, credentials, applications, purchases or deployments.
