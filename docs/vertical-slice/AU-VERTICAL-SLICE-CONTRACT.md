# AU Vertical Slice Contract

**Status:** TEMPLATE CANDIDATE / IMPLEMENTATION CONTRACT
**Owner:** Master Affiliate Website Template
**Country input:** Australia workstream

## Purpose
Prove the reusable journey without embedding volatile affiliate data in WordPress templates:

`Global → AU → Category → Guide/Comparison → Detail → Commercial CTA`

## Route contract
- Global: `/`
- AU entry: `/au/` (deployment may map this to the AU subdomain)
- Category: `/au/<category>/`
- Guide: `/au/<category>/buying-guides/<guide>/`
- Comparison: `/au/<category>/comparisons/<comparison>/`
- Detail: `/au/<category>/<program-or-product>/`
- Commercial CTA: resolved through the governed commercial destination abstraction

## Presentation requirements
Every stage must provide:
- clear page purpose
- breadcrumbs where appropriate
- concise decision-support content
- trust/verification signal
- relevant internal links
- accurate action-oriented CTA
- affiliate disclosure when commercial relationship exists

## Data boundary
WordPress templates/patterns must not hard-code:
- commissions
- prices
- availability
- tracking URLs
- cookie duration
- affiliate approval status
- current promotional claims

Those values belong to the canonical structured data layer and must carry source, verification status and freshness metadata.

## Fixture policy
The first implementation may use clearly labelled non-production fixtures/placeholders to prove layout and data contracts. Fixtures must never be presented as live commercial facts.

## Acceptance gate
The slice is not production-ready until:
1. each route renders through the shared template system;
2. AU content is isolated to configuration/content, not duplicated theme code;
3. commercial CTA resolution has a defined API boundary;
4. outbound destinations can be verified before click;
5. affiliate disclosure is visible at the commercial decision point;
6. no fabricated commercial claims are introduced;
7. browser, accessibility, performance and end-to-end tracking tests are run in a real WordPress environment.

## Next implementation
Build the AU category shell and reusable guide/comparison/detail templates using fixture-safe content, then connect the governed commercial CTA interface without adding live affiliate destinations prematurely.
