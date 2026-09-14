# Software & Games Merchant Assurance Matrix — 2026-09-14

**Purpose:** prioritise merchants for the Affiliate Websites software/games vertical without confusing low price or high commission with trust.

## Evidence classes

- **AUTHORISED_RETAIL_SIGNAL** — merchant provides strong public evidence of direct publisher/authorised supply relationships. Still requires current offer/country verification.
- **DIRECT_RESELLER_REQUIRES_PROVENANCE_DILIGENCE** — merchant sells directly but licence/key sourcing for each promoted offer needs explicit verification.
- **MARKETPLACE_OR_MULTI_SELLER_HIGH_DILIGENCE** — underlying seller/offer provenance must be assessed separately; marketplace reputation alone is insufficient.
- **UNKNOWN** — insufficient evidence; do not infer.

## Current matrix

| Merchant | Class | Affiliate signal | Automation signal | Commercial value | Assurance posture |
|---|---|---|---|---|---|
| Green Man Gaming | AUTHORIZED_RETAIL_SIGNAL | Up to 5% standard; 10% bundles | Product catalog API, 7,000+ games | High | Preferred gaming candidate once project approval/country eligibility is verified |
| GOG | AUTHORIZED_RETAIL_SIGNAL | 6% net sales; 7-day last click | Product feed API | High | Preferred gaming candidate once approved |
| Fanatical | AUTHORIZED_RETAIL_SIGNAL | Global Awin programme | Feed/API not verified in this batch | High | Preferred gaming candidate once approved |
| Gamers-Outlet | DIRECT_RESELLER_REQUIRES_PROVENANCE_DILIGENCE | 8% standard; EUR 50 payout threshold | UNKNOWN | High | Strong commercial candidate, but Windows/Office/software offers require licence-type and provenance evidence before recommendation |
| GAMIVO | MARKETPLACE_OR_MULTI_SELLER_HIGH_DILIGENCE | Up to 8%; 24-hour window; EUR 250 threshold | XML feed available on request | High | Useful comparison source; do not convert marketplace-level trust into seller-level assurance |
| K4G | MARKETPLACE_OR_MULTI_SELLER_HIGH_DILIGENCE | 5% direct + 0.80% / 0.20% tiers; 30 days | UNKNOWN | Medium-high | Comparison/research candidate; seller/offer diligence required |

## Ranking logic

A merchant may rank highly only when it performs across **both** commercial and assurance dimensions.

Suggested weighted research score:

- 25% licence/provenance confidence
- 20% affiliate economics
- 15% structured feed/API suitability
- 15% country availability / localisation
- 10% pricing competitiveness
- 10% support/refund clarity
- 5% merchant reputation signal

**Mandatory override:** any missing critical licence, region or seller evidence can force HOLD regardless of numeric score.

## Product-specific assurance requirements

### Windows
Record at minimum:

- exact edition;
- activation/licence type where evidenced;
- OEM/retail/other classification where evidenced;
- device count;
- region;
- transferability/reinstallation limits where stated;
- merchant and underlying seller where applicable;
- source and verification date.

### Microsoft Office
Record at minimum:

- exact product/year/edition;
- Windows/macOS eligibility;
- account-binding status where evidenced;
- device/installation count;
- transferability/reinstallation limits;
- region;
- merchant/seller class;
- source/freshness.

### Antivirus / security / VPN
Record at minimum:

- product/tier;
- term length;
- device count;
- renewal behaviour where known;
- new-customer/renewal restriction where relevant;
- region;
- activation method;
- source/freshness.

### Games
Record at minimum:

- title/edition;
- platform/store (Steam, GOG, etc.);
- activation region;
- key/direct-entitlement type where known;
- preorder/release state where relevant;
- merchant/seller class;
- source/freshness.

## Publication doctrine

The comparison UI should be able to show three different ideas without collapsing them:

1. **Lowest observed eligible price**
2. **Best verified-value offer**
3. **Highest-assurance / authorised benchmark**

These may be three different merchants.

Affiliate commission must never be shown as a reason that one licence is safer, more legitimate or more suitable than another.

## Primary sources verified 2026-09-14

- Gamers-Outlet affiliate page and affiliate agreement
- Fanatical affiliate programme page
- Green Man Gaming affiliate programme page
- GOG affiliate programme page
- GAMIVO affiliate programme page
- K4G affiliate terms

All programme terms are volatile and require freshness checks before production use.
