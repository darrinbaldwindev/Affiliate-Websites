# Software & Games Source Mapping — 2026-09-15

**Scope:** research/fixture-level mapping into normalized `software_offer`. This is not evidence of live feed credentials or production approval.

| Merchant | Source shape / future ingestion | Normalized identity | Region/currency | Licence semantics | Assurance treatment |
|---|---|---|---|---|---|
| Green Man Gaming | Product catalogue API after affiliate access | merchant + source product/SKU + region | map explicit API/store territory and currency | games: platform/DRM/region; software fields N/A unless catalogue expands | authorised-retailer candidate; approval still required |
| GOG | Product Feed API after programme/network approval | merchant + feed product id + region | map feed/store country/currency | DRM-free game/product attributes; do not infer Windows/Office licence semantics | authorised-retailer candidate; approval still required |
| Fanatical | Affiliate-network catalogue/deeplink/feed capability to be confirmed at approval | merchant + network/catalogue id + region | country/store currency must be explicit | game platform/DRM/region; bundle identity normalized separately | authorised-retailer candidate; current network must be reconfirmed |
| Gamers-Outlet | Merchant catalogue/page/feed capability to be confirmed | merchant + merchant SKU/product id + region | activation region and displayed currency mapped separately | Windows/Office require explicit licence type, transferability, account binding, installs and activation platform | direct-reseller candidate; affiliate approval never substitutes for offer provenance |

## Mapping rules

1. Never synthesize missing source identifiers from titles alone.
2. Merchant title text may assist candidate matching but cannot establish SKU equivalence.
3. Region restrictions and storefront currency are separate fields.
4. For Windows/Office/productivity, unknown licence semantics block publication.
5. Feed/API records must preserve `observed_at` and source evidence reference so freshness can be evaluated.
6. Marketplace records, if later added, require underlying seller identity/provenance and cannot inherit merchant-level assurance automatically.
7. Affiliate economics are stored only as commercial metadata and are excluded from ranking inputs.

## Normalization examples

A Windows 11 Pro OEM offer and Windows 11 Pro Retail offer are different equivalence groups even if their marketing titles are nearly identical. An Office 2024 Pro Plus one-device non-transferable key cannot compete in the same like-for-like group as an account-bound transferable licence. Game offers must normalize edition, platform/DRM and activation region before price comparison.
