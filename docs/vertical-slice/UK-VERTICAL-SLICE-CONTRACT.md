# UK Vertical Slice Contract

**Status:** COUNTRY IMPLEMENTATION CONTRACT / TEMPLATE-COMPATIBLE  
**Owner:** United Kingdom Affiliate Website workstream  
**Master dependency:** shared Affiliate Website template architecture

## Purpose

Prove the UK journey without duplicating master theme logic or embedding volatile affiliate data in WordPress templates:

`Global → UK → Category → Guide/Comparison → Detail → Governed Commercial CTA`

## Route contract

- Global: `/`
- UK entry: `/uk/` (deployment may map this to the UK subdomain)
- Category: `/uk/<category>/`
- Guide: `/uk/<category>/buying-guides/<guide>/`
- Comparison: `/uk/<category>/comparisons/<comparison>/`
- Detail: `/uk/<category>/<program-or-product>/`
- Commercial CTA: resolved through the shared governed commercial destination abstraction

## First UK fixture vertical

The recommended first fixture-safe vertical is **technology/appliances**, because it exercises:

- category navigation;
- merchant/program comparison;
- product-like decision support;
- feed/API-ready presentation;
- trust/freshness signals;
- a governed commercial CTA;
- minimal regulated-product complexity compared with insurance/finance.

Fixture candidates may reference neutral merchant/category identities only when clearly marked non-production. Live prices, commissions, offers, approval states and tracking destinations must not be invented.

## Presentation requirements

Every stage must provide:

- clear page purpose;
- UK country context;
- breadcrumbs where appropriate;
- concise decision-support content;
- verification/freshness signal;
- relevant internal links;
- accurate action-oriented CTA;
- affiliate disclosure where a commercial relationship exists;
- accessible semantic structure.

## Data boundary

WordPress templates/patterns must not hard-code:

- commissions;
- prices;
- availability/stock;
- tracking URLs;
- cookie/attribution duration;
- affiliate approval status;
- live promotional claims;
- regulated-product eligibility assertions.

Those values belong to the canonical structured data layer and must carry evidence, verification status and freshness metadata.

## Country data rule

UK country data extends the shared canonical model. Do not create a separate UK source of truth.

Required country attributes include:

- `country = UK`;
- country eligibility;
- category classification;
- programme/merchant identity;
- affiliate relationship state;
- evidence source and type;
- observed/verified dates;
- freshness state;
- restrictions;
- regulatory/compliance risk classification;
- commercial-resolution eligibility.

## UK-specific risk classes

The UK resolver/publishability workflow must be able to distinguish at least:

1. ordinary retail/product affiliate;
2. telecom/broadband;
3. travel;
4. insurance/financial promotion;
5. health-sensitive content;
6. utilities/home-energy lead generation.

Higher-risk classes may require extra verification and must fail closed if required evidence is absent or stale.

## Acceptance gate

The UK slice is not production-ready until:

1. each route renders through the shared template system;
2. UK content/configuration is isolated from reusable master code;
3. commercial CTA resolution uses the shared API boundary;
4. outbound destinations can be verified before click;
5. affiliate disclosure appears at the commercial decision point;
6. no fabricated commercial claims are introduced;
7. stale/unverified commercial records fail closed;
8. regulated/high-risk categories cannot bypass their enhanced gate;
9. browser, accessibility, performance and end-to-end tracking tests run in a real WordPress environment.

## Initial implementation sequence

1. UK country shell/configuration.
2. Technology/appliances category shell.
3. Fixture-safe comparison page.
4. Fixture-safe detail page.
5. Governed CTA integration using the existing commercial resolver seam.
6. Trust/source/freshness presentation.
7. Automated fixture checks for stale/unapproved destination blocking.
8. Real WordPress/browser verification when environment exists.

## Non-claims

This contract does not claim:

- live UK programme acceptance;
- live affiliate destinations;
- current prices/commissions;
- production Rewards API deployment;
- browser-verified WordPress rendering;
- legal approval of regulated categories.
