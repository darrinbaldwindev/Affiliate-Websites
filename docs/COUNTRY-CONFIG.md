# Country Configuration Contract

Status: Master implementation contract v0.1

## Purpose

Country configuration is stable site configuration. It must not become the canonical store for volatile rewards, merchant, commission or eligibility intelligence. That intelligence belongs behind the Rewards API / PostgreSQL boundary.

## Required country fields

Each country implementation should define:

- `code`: ISO-style two-letter code (`AU`, `GB`, `US`)
- `name`: display name
- `locale`: primary WordPress locale
- `currency`: ISO currency code
- `timezone`: primary site timezone
- `country_url`: canonical country site URL
- `status`: `planned`, `active`, or `retired`
- `legal_region`: local compliance region used by policy/content layers

## Initial configuration

| Code | Name | Locale | Currency | Status |
|---|---|---|---|---|
| AU | Australia | en_AU | AUD | active-design |
| GB | United Kingdom | en_GB | GBP | active-design |
| US | United States | en_US | USD | active-design |

The production `country_url` values are deployment configuration, not hard-coded example domains. The architecture target is a global homepage with country subdomains.

## Rules

1. Do not hard-code affiliate network links into templates.
2. Do not hard-code commission rates, payout claims, eligibility claims or merchant status into the theme.
3. Country selection must remain manual and accessible; geolocation may assist but must never be the only route.
4. Country-specific editorial content stays in the country implementation.
5. Shared components remain country-neutral and consume country context.
6. Every volatile commercial field needs source, verification/effective date, status and confidence metadata in the canonical data layer.

## Evidence states

Use the project evidence vocabulary: `FACT`, `VERIFIED`, `INFERENCE`, `RECOMMENDATION`, `HYPOTHESIS`, `UNKNOWN`, `CLAIMED`, `IMPLEMENTED`, `VERIFIED IMPLEMENTATION`.
