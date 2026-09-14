# Software & Games Publishability Gate — 2026-09-14

**Scope:** Windows, Office/productivity software, antivirus/security, VPN/utilities, games, bundles, gift cards and related digital licences.

## Gate outcome

Each offer resolves to one of:

- **PASS** — eligible for governed publication after project affiliate approval and country resolution;
- **HOLD** — potentially usable, but critical evidence is missing/stale;
- **REJECT** — known conflict, ineligible region, misleading licence representation, prohibited destination or unresolved material contradiction.

## Mandatory common fields

An offer cannot PASS without:

1. stable merchant identifier;
2. merchant class;
3. exact product/edition;
4. country eligibility (AU/UK/US independently);
5. current destination through the shared affiliate resolver, not embedded raw tracking URL;
6. price currency and verification timestamp if price is shown;
7. source URL/source type;
8. evidence state and confidence;
9. current project affiliate relationship state;
10. material restrictions visible to the user before click.

## Licence-specific requirements

### Windows / operating systems

HOLD unless the record identifies, where the seller provides evidence:

- edition;
- device count;
- region;
- activation/licence classification;
- OEM/retail/other status when known;
- hardware-transfer/reinstallation restrictions when material.

Do not state that an OEM, retail, volume-derived or otherwise restricted licence is equivalent merely because the software edition name matches.

### Office / productivity suites

HOLD unless the record identifies:

- edition/year;
- supported OS;
- device/installation count;
- account binding where material;
- transferability/reinstallation limitations where known;
- region.

### Antivirus / VPN / security subscriptions

HOLD unless the record identifies:

- term length;
- device count;
- new-customer/renewal condition where relevant;
- renewal/auto-renewal behaviour where known;
- region and activation restriction.

### Games

HOLD unless the record identifies:

- title/edition;
- activation platform/store;
- region;
- preorder/release condition where relevant;
- seller identity for marketplace offers when needed for provenance/risk assessment.

## Merchant-class rules

### AUTHORIZED_RETAIL_SIGNAL

May qualify for PASS once country eligibility, live offer freshness and project affiliate approval are verified. Merchant-level authorisation evidence does not remove product-level freshness requirements.

### DIRECT_RESELLER_REQUIRES_PROVENANCE_DILIGENCE

Default **HOLD** for Windows/Office/software until the promoted offer has adequate licence/provenance evidence. A low price or direct checkout is not provenance evidence.

### MARKETPLACE_OR_MULTI_SELLER_HIGH_DILIGENCE

Default **HOLD** unless the underlying seller/offer can be identified and the comparison UI clearly communicates marketplace status. Marketplace reputation cannot silently substitute for seller-level evidence.

## Price rules

- Price must include currency.
- Country/tax treatment must not be guessed.
- Coupon-dependent prices must show the coupon requirement and freshness.
- “From” prices cannot be presented as the exact price of a specific offer.
- A price older than the configured freshness window fails closed to HOLD.
- Cheapest offer is not automatically “best”.

## Affiliate rules

- Public existence of an affiliate programme is not the same as this project's approval.
- Commission/cookie/feed terms are research metadata until current affiliate approval is verified.
- Raw tracking links stay outside editorial content.
- Affiliate economics must not affect licence classification or trust language.

## User-facing comparison requirement

Where materially different licence classes exist, comparison UI should separate:

- cheapest eligible observed offer;
- best verified-value offer;
- highest-assurance/authorised benchmark.

If evidence is insufficient to support those labels, use neutral sorting and disclose uncertainty instead.

## Fail-closed conditions

Immediate HOLD or REJECT for:

- missing region on region-restricted product;
- stale or source-less price;
- unknown underlying marketplace seller where seller identity is material;
- contradictory licence type claims;
- unsupported “official”, “genuine”, “lifetime”, “transferable” or equivalent trust claims;
- project affiliate relationship not approved/current;
- wrong-country destination;
- destination bypassing shared resolver;
- material restriction omitted from user-facing copy.

## Verification cadence

Suggested baseline (implementation/configuration remains separate):

- price/stock/coupon: high volatility — verify frequently;
- affiliate rate/cookie/payout/feed: medium volatility — verify before publication and on scheduled review;
- merchant business model/provenance class: medium volatility — review on material change;
- licence restrictions: verify per offer and whenever source wording changes.

This document defines a research/publishability contract only. It does not authorize live publication or represent legal advice.
