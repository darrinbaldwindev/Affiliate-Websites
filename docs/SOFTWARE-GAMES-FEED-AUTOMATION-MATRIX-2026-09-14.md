# Software & Games — Feed/API Automation Matrix

**Checked:** 2026-09-14  
**Purpose:** identify merchant ingestion routes suitable for a governed price-comparison/deals engine.  
**Important:** technical feed availability does not equal merchant approval, country eligibility, legal clearance or permission to publish an offer.

## Current matrix

| Merchant | Merchant model | Automation mechanism evidenced | Affiliate economics evidenced | Integration posture |
|---|---|---|---|---|
| Green Man Gaming | authorised retailer | Entire product catalogue API; 7,000+ games | up to 5% sale; 10% GMG bundles | **HIGH PRIORITY** |
| GOG | authorised digital storefront | Product Feed API | 6% net sales; 7-day last click | **HIGH PRIORITY** |
| Eneba | marketplace | XML/CSV feed after affiliate application approval | standard 2–5% revenue share | **CONDITIONAL** — seller provenance required |
| GAMIVO | marketplace/reseller platform | XML feed available on request for automated sites / comparison engines | up to 8%; 24-hour attribution | **CONDITIONAL** — marketplace/provenance controls required |
| Fanatical | authorised retailer | Affiliate tracking/analytics through Awin; deal previews evidenced | programme through Awin | **HIGH TRUST; FEED/API NEEDS SEPARATE CONFIRMATION** |

## Primary evidence

### Green Man Gaming

GMG's affiliate page explicitly advertises access to its entire product catalogue API covering more than 7,000 games. It also states that it sources games directly from more than 700 publishers.

Source: https://www.greenmangaming.com/affiliates

### GOG

GOG's affiliate page explicitly advertises a Product Feed API, 6% commission on net sales and seven-day last-click tracking.

Source: https://affiliate.gog.com/

### Eneba

Eneba's affiliate page states that approved affiliates can receive an XML/CSV product feed with filters. It publishes a standard 2–5% revenue share.

Source: https://www.eneba.com/become-affiliate

### GAMIVO

GAMIVO's affiliate FAQ says XML feeds can be requested for an automated website or price-comparison engine. It currently advertises commission up to 8% and a 24-hour referral attribution period.

Source: https://www.gamivo.com/affiliate

### Fanatical

Fanatical's affiliate programme operates through Awin and supplies affiliate tracking, analytics and previews of upcoming deals. Its current public affiliate page does not, from the evidence checked in this batch, establish a catalogue API/feed equivalent to GMG/GOG; that capability therefore remains **UNKNOWN** rather than inferred.

Source: https://www.fanatical.com/en/affiliates

## Canonical ingestion requirements

Any future importer should normalise external feed data into the existing governed commercial data model before WordPress receives it. At minimum ingestion should preserve:

- merchant and seller identity separately;
- merchant class (`AUTHORISED_RETAILER`, `DIRECT_RESELLER`, `MARKETPLACE`);
- country/region eligibility;
- SKU/product identity and edition;
- licence type and activation platform;
- seller provenance where applicable;
- native currency and observed price;
- source/feed timestamp and local ingestion timestamp;
- affiliate relationship/evidence state;
- source URL or feed record identifier;
- disclosure/publication state.

## Fail-closed rules

An imported offer must not become a governed commercial CTA merely because it exists in a feed. Publication remains blocked where any required condition is absent or uncertain, including:

1. stale price/evidence;
2. country or activation-region mismatch;
3. incorrect country currency where a country-local offer is claimed;
4. Windows/Office/productivity licence type unknown;
5. merchant relationship unapproved;
6. marketplace seller provenance unknown;
7. disclosure missing;
8. destination/tracking URL not produced through the canonical resolver.

These rules are now represented in the synthetic Software & Games commercial-CTA fixture and validator.

## Recommended implementation order

1. **GMG catalogue API** — strongest combination of authorised inventory + explicit catalogue API + affiliate economics.
2. **GOG Product Feed API** — authorised/high-trust feed path with explicit attribution terms.
3. **Fanatical/Awin** — high-trust merchant; determine whether Awin exposes a suitable product feed for the approved account before implementation.
4. **Eneba XML/CSV** — useful breadth, but only behind marketplace seller-provenance controls.
5. **GAMIVO XML** — useful for comparison coverage; retain 24-hour attribution and marketplace/reseller risk metadata.

## What remains UNKNOWN

- actual account approval for this project with any merchant/network;
- exact per-country catalogue coverage for every merchant;
- feed credentials, rate limits and contractual caching/display limits;
- exact permitted price-refresh intervals;
- whether Fanatical/Awin will expose an appropriate structured product feed to this account;
- production tracking-link formats and resolver integration.

None of those UNKNOWN items should be filled by inference. They become verified only after account/network evidence exists.
