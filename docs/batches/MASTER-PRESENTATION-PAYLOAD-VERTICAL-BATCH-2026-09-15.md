# Master Presentation Payload Vertical Batch — 2026-09-15

**Status:** EXECUTED / CI PENDING  
**Branch:** `work/master-presentation-payload-vertical-batch-2026-09-15`  
**Fresh baseline:** `1c4df2dbc269371bc53e3655a3374241fed5f265`  
**Canonical coordination:** `darrinbaldwindev/Overseer#49`

## Fresh scan result

- `main` was freshly scanned before mutation.
- Prior master publication-mapping PR #21 remained draft and materially divergent from moving `main`, with exact-head CI not emitted after its dependency fix.
- Current `main` had independently advanced the UK fixture-to-presentation seam and its validation workflow.
- To avoid stacking on stale/divergent PR #21, this batch starts from fresh `main` and advances the next independent master boundary.

## Vertical objective

`controlled read model → minimal WordPress payload → fail-closed display/action boundary → synthetic cases → existing CI`

## Executed

1. Added `docs/api/WORDPRESS-PRESENTATION-PAYLOAD-CONTRACT.md`.
2. Defined allowed/forbidden presentation fields and canonical ownership.
3. Added synthetic non-production payload cases at `fixtures/master/presentation-payload.synthetic.json`.
4. Added `unittest` safety checks at `fixtures/master/test_presentation_payload.py`.
5. Extended the existing Commercial CTA fixture workflow to exercise the master payload cases; no duplicate workflow/control plane created.

## Safety invariants

- WordPress receives semantic state, not a raw tracking destination.
- `VERIFIED` consumer evidence can remain commercially `BLOCKED`.
- `ELIGIBLE_FOR_RESOLUTION` permits only semantic resolver hand-off; it is not itself a destination.
- Malformed/missing/mismatched/unresolved state fails closed.
- No real program, rate, commission, earnings, price, affiliate relationship, credentials or tracking URL appears in the fixture.
- PostgreSQL/Supabase + controlled Rewards layer remain canonical.

## Verification boundary

Exact-head Commercial CTA fixture CI success is required before claiming this batch GREEN-for-CI. This batch does not prove live API/runtime WordPress integration, production resolver behavior, click attribution, physical Windows AgentOS mutation receipts, recovery, Green or PRS.

## Next safe dependent step

After exact-head CI, reconcile this generic contract against the existing UK presentation seam and AU Surveys read-model work to identify one reusable adapter shape without moving country-owned evidence into master.