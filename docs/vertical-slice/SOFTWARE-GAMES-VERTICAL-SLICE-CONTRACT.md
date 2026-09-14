# Software & Games Vertical Slice Contract

**Scope:** reusable master comparison journey for AU, UK and US.

## Journey

`Global → Country → Software & Games → Category → Comparison → Offer Detail → Governed Commercial CTA`

Initial categories:

- Windows
- Microsoft Office / productivity
- Antivirus / security
- VPN / utilities
- PC games
- Game bundles
- Gift cards / subscriptions

## Master responsibilities

The master layer owns:

- reusable information architecture;
- comparison/detail UI components;
- evidence/trust labels;
- merchant-class display rules;
- price freshness display;
- disclosure placement;
- structured data/schema contracts;
- shared affiliate-resolution seam;
- fail-closed behaviour for missing/stale critical data.

## Country responsibilities

AU, UK and US workstreams independently own:

- merchant/program eligibility;
- current affiliate approval;
- local currency/tax presentation;
- country-specific availability/region restrictions;
- local legal/compliance copy;
- local search intent/content priorities;
- current price/stock/coupon evidence.

A country workstream must not redefine the master trust taxonomy or create a second affiliate resolver.

## Comparison model

A row/card should be able to represent:

- merchant;
- underlying seller if marketplace;
- exact product/edition;
- licence/activation type;
- platform/OS;
- region;
- devices/installations;
- transferability or key restriction;
- current observed price + currency;
- price verified-at timestamp;
- merchant class;
- evidence state/confidence;
- governed CTA availability.

## Ranking modes

The UI must support distinct ranking concepts:

1. lowest eligible observed price;
2. best verified value;
3. highest-assurance/authorised benchmark.

Do not collapse them into one “best” label unless evidence supports the claim.

## Fixture-safe first slice

Recommended fixture path:

`AU → Software & Games → Windows → Windows 11 Pro comparison → synthetic offer detail → governed CTA`

Use synthetic/non-production offers until live merchant approval and canonical data integration exist.

The fixture should exercise:

- one authorised-retail benchmark record;
- one direct-reseller record;
- one marketplace record;
- different licence restrictions;
- stale-price failure;
- wrong-region failure;
- missing licence-type failure;
- unapproved affiliate relationship failure;
- resolver-only CTA enforcement.

## Acceptance conditions

A bounded fixture slice is complete only when:

- same master theme/components work without country fork;
- country config determines currency/eligibility presentation;
- material licence differences are visible before click;
- stale/unapproved/wrong-country destinations fail closed;
- raw tracking URLs are absent from editorial templates;
- synthetic fixture state cannot be mistaken for production approval;
- automated checks cover the critical negative paths.

## Non-goals

This contract does not:

- approve any merchant;
- certify any licence/key;
- set live prices;
- create production affiliate relationships;
- bypass canonical Rewards API/data boundaries;
- provide legal advice.
