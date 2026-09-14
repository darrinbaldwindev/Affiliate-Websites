# Software & Games Vertical Autonomous Batch 003 — 2026-09-14

**Repository:** `darrinbaldwindev/Affiliate-Websites`  
**Mode:** vertical autonomous execution  
**Status:** COMPLETE — bounded licence-equivalence and affiliate-readiness batch executed  
**Rule:** extend the canonical commercial CTA seam; do not create parallel commerce truth.

## Fresh scan baseline

Fresh scan confirmed Batch 002 was on `main` at `661370c4226ca45e97239a728e6b3483d65c5d6e`, with fixture-only Software & Games validation under `fixtures/commercial-cta/` and CI already wired. Existing machine gates covered country, currency, price freshness, licence type, merchant approval, marketplace provenance, disclosure and safe fixture URLs.

## Objective

Close the next false-equivalence risks for Windows/Office/productivity comparisons:

1. transferability status;
2. account binding status;
3. device/install count;
4. activation platform/method;
5. exact product family + edition identity;
6. explicit equivalence-group matching before offers can be compared as like-for-like.

## Task results

- SG3-1 fresh repo reconciliation — COMPLETE
- SG3-2 synthetic offer fixture extended with licence-detail fields and deliberate blocked cases — COMPLETE
- SG3-3 deterministic evaluator extended with fail-closed licence-detail gates — COMPLETE
- SG3-4 negative assurance tests added for each new gate — COMPLETE
- SG3-5 existing CI verified on exact head — COMPLETE
- SG3-6 affiliate-account prerequisites documented for GMG, GOG, Fanatical and Gamers-Outlet — COMPLETE
- SG3-7 batch closure and next slice — COMPLETE

## New enforced controls

For Windows, Office and productivity offers, the fixture validator now requires known values for:

- `licence_type`
- `transferability`
- `account_binding`
- positive integer `device_install_count`
- `activation_platform`
- `product_family`
- `edition`
- `equivalence_group`

The equivalence group must begin with the exact `product_family|edition|licence_type|` tuple. Mismatched or unknown identity blocks the offer.

## Verification evidence

Exact-head commercial fixture workflow:

- commit: `d9a57a320cd168a4beea32f52765a2823cd9abcd`
- workflow run: `34826554591`
- workflow: `Commercial CTA fixture validation`
- conclusion: **success**

Execution commits:

- `626df7496430c7a2e79aa4c19e39de92dd49e137` — Batch 003 created
- `ca9da76cfdd07d0d0967f4a520e0ef0f752856cd` — licence-equivalence gates added
- `f2dd846d7992556a63bee3083e73471e9afaa944` — synthetic licence-detail fixtures expanded
- `d9a57a320cd168a4beea32f52765a2823cd9abcd` — negative assurance tests expanded
- `9adc16b2663eb598cd3a30e5133e46524c472236` — affiliate-account readiness recorded

## Affiliate readiness findings

A durable readiness record now exists at `docs/SOFTWARE-GAMES-AFFILIATE-ACCOUNT-READINESS-2026-09-14.md`.

Key conclusions:

- **Green Man Gaming:** strong future candidate; Business Affiliate Program and product catalogue API are attractive once the public site/disclosure surface is ready.
- **GOG:** strong future candidate; Adtraction channel approval plus GOG programme approval are required before tracking goes live; product feed/API is suitable for governed ingestion.
- **Fanatical:** current landing page says Awin, while an older support FAQ still references CJ/Tapfiliate. Network must therefore be re-confirmed at application time.
- **Gamers-Outlet:** straightforward public affiliate registration and 8% standard commission signal, but programme approval must remain separate from offer-level Windows/Office provenance assurance.

No affiliate application, account creation, credential change, tracking-link publication, purchase or deployment occurred.

## Residual risks / still OPEN

- real merchant approvals and network account IDs;
- live feed credentials and terms-specific ingestion configuration;
- exact production Windows/Office SKU normalisation from merchant feeds;
- evidence for transferability/account-binding/device count on each real offer;
- browser/runtime validation of a comparison surface;
- legal conclusions about individual licence offers.

## Next vertical batch

On the next `cont` / `continue autonomously`:

1. fresh-scan repo and concurrent country work;
2. define the canonical normalized `software_offer` data contract for production-facing ingestion without creating another store;
3. map GMG/GOG/Fanatical/Gamers-Outlet source fields into that contract at research/fixture level;
4. add duplicate-SKU and contradictory-evidence tests;
5. add comparison ranking rules that separate `lowest_observed_price`, `best_verified_value`, and `highest_assurance`;
6. verify that commission cannot alter trust/equivalence ranking;
7. only then wire presentation fixtures through existing master components if reusable cleanly.

## Completion rule

This batch is complete because the new licence-equivalence controls are landed and exact-head CI is green, and affiliate-account prerequisites are durably recorded. Production merchant approval, production feeds, real offer provenance and live tracking remain explicitly OPEN until independently evidenced.
