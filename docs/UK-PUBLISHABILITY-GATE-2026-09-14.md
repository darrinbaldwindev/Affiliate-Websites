# UK Affiliate Publishability Gate — 2026-09-14

**Status:** COUNTRY GOVERNANCE CONTRACT  
**Country:** United Kingdom  
**Purpose:** prevent research candidates from becoming publishable or commercially actionable without current evidence, approval and category-appropriate compliance.

## Principle

Monetisation potential is not sufficient for publication.

A UK record progresses only through:

`CONCEPT → RESEARCHED → VERIFIED → PUBLISHABLE → PUBLISHED → MONITORED`

Failure of any mandatory gate means the commercial CTA must remain blocked or fall back to a non-commercial editorial state.

## Core gate — all categories

A candidate may become `PUBLISHABLE` only when all applicable checks pass:

1. stable merchant/program identity established;
2. UK availability/eligibility supported by current evidence;
3. consumer-facing claims are source-backed;
4. publisher affiliate relationship is actually approved where required;
5. commercial destination is resolver-approved;
6. required disclosure is present;
7. price/offer/commission/attribution claims are within freshness tolerance;
8. restrictions are represented and enforced;
9. no unresolved source conflict invalidates the intended claim;
10. commercial destination is not stored as scattered raw tracking URL in editorial content;
11. required sponsored-link treatment is applied;
12. monitoring/reverification owner and next-review date exist.

## Freshness classes

### F1 — highly volatile
Examples: price, stock, promotion, tariff, voucher, cashback level, commission rate, booking availability.

Rule: must come from current controlled data or be omitted. Do not publish stale snapshots as current facts.

### F2 — medium volatility
Examples: cookie/attribution duration, returns windows, programme restrictions, validation periods, affiliate eligibility.

Rule: re-verify before launch and on a scheduled cadence.

### F3 — lower volatility
Examples: merchant identity, broad category, non-promotional product class.

Rule: verify initially and monitor for material changes.

## Risk-class gates

### Class R1 — ordinary retail/product affiliate
Examples: technology, appliances, home, sports, fashion, ordinary consumer products.

Additional requirements:
- current product/merchant eligibility;
- price and stock freshness if shown;
- promotion/voucher rules enforced;
- returns/validation constraints represented where material;
- comparison claims supported by evidence.

### Class R2 — telecom/broadband
Additional requirements:
- exact geographic/service availability logic where relevant;
- tariff/price freshness;
- contract length and material eligibility conditions;
- installation/activation/validation rules;
- no implication that a provider is available at an address without evidence;
- comparison ordering/ranking rationale disclosed where commercial relationships may influence presentation.

Fail closed when availability or current tariff evidence is missing.

### Class R3 — travel
Additional requirements:
- booking/cancellation conditions treated as volatile;
- destination/activity availability current where shown;
- no stale price/availability promise;
- material restrictions and affiliate link requirements enforced;
- travel editorial separated from unsupported safety/visa/legal guarantees.

### Class R4 — insurance / financial promotion
**Default state: HOLD unless enhanced compliance is satisfied.**

Additional requirements:
- identify whether content constitutes or communicates a regulated financial promotion;
- verify the regulated/authorised status of relevant firms where applicable;
- verify current programme terms and approved publisher status;
- fair, clear and not misleading presentation;
- no unsubstantiated savings, suitability or outcome claims;
- comparison/ranking methodology documented;
- required risk/eligibility disclosures presented;
- legal/compliance review recorded before production enablement.

No normal retail override may bypass this class.

### Class R5 — health-sensitive content
Examples: products/services where copy could become medical or health claims.

Additional requirements:
- avoid unsupported treatment/diagnosis claims;
- separate product features from health outcomes;
- use primary evidence for material health claims;
- block content that would require professional/regulated advice beyond site scope.

### Class R6 — utilities / home-energy lead generation
Examples: solar, energy, heating or installation leads.

Additional requirements:
- current geographic/service eligibility;
- installer/provider identity and status verification where relevant;
- no unverified grant/subsidy/savings claims;
- finance/payment claims treated under applicable financial-promotion gate;
- lead consent/privacy pathway verified;
- no implied guaranteed savings or installation outcome.

## Ranking independence

Commercial scoring and editorial ranking must be stored separately.

A high-paying candidate may rank poorly for the user. A lower-paying candidate may be the better recommendation. The system must be able to explain recommendation criteria without relying on commission size as the sole determinant.

## Resolver behaviour

The commercial resolver should return one of:

- `approved` — destination may be used;
- `blocked_unverified`;
- `blocked_stale`;
- `blocked_relationship_inactive`;
- `blocked_country_ineligible`;
- `blocked_regulatory_gate`;
- `blocked_conflict`;
- `blocked_destination_invalid`.

Do not silently substitute a different merchant/program when a requested commercial action is blocked.

## Minimum audit record

Record:

- entity/program ID;
- country;
- intended action;
- relationship ID if applicable;
- decision status;
- blocking reason;
- evidence/freshness version;
- decision timestamp.

Avoid unnecessary personal data in audit events.

## Current UK rollout rule

Initial implementation should favour R1 ordinary retail/product categories and low-regulatory-risk services. Broadband may proceed only through R2. Insurance/financial candidates remain research-only until the R4 enhanced gate is explicitly satisfied.
