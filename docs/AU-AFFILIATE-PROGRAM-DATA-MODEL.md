# AU Affiliate Program Data Model

## Purpose

Define the minimum governed record needed to move an Australian affiliate/reward programme from research into a live commercial CTA.

## Record shape

```text
program_id
name
country
category
program_type
network
relationship_status
application_url
merchant_url
tracking_url_template

commission:
  rate_type
  displayed_rate
  approved_rate
  new_customer_rate
  returning_customer_rate
  channel_rates
  currency

attribution:
  tracking_days
  validation_days
  clickless_tracking
  de_dupe_rules

catalogue:
  product_feed_available
  deep_link_available
  feed_last_verified_at

eligibility:
  country_requirements
  age_requirements
  audience_requirements

restrictions:
  ppc
  coupon
  cashback
  price_comparison
  social
  email
  trademark
  product_exclusions

content:
  approved_claims
  prohibited_claims
  source_urls

verification:
  evidence_state
  last_verified_at
  verifier
  next_review_at
```

## Relationship states

- `DISCOVERED` — found during research; no relationship assumed.
- `APPLICATION_READY` — current application route identified.
- `APPLIED` — application submitted by the operator.
- `APPROVED` — programme/network approval confirmed.
- `REJECTED` — application rejected.
- `SUSPENDED` — previously approved but not currently promotable.
- `EXPIRED` — evidence/terms have expired and require re-verification.

## Evidence states

- `VERIFIED` — supported by current authoritative programme/network evidence.
- `CLAIMED` — programme claims the information but network/account confirmation is still required.
- `CONFLICT` — authoritative sources disagree; do not surface volatile figure as fact.
- `UNKNOWN` — not established.

## CTA eligibility gate

A programme may be promoted through the commercial CTA layer only when:

1. `country = AU` or the programme explicitly supports Australian users.
2. `relationship_status = APPROVED`.
3. `evidence_state = VERIFIED`.
4. `last_verified_at` is within the configured freshness window for the field.
5. The destination URL is known and valid.
6. Promotional restrictions permit the intended placement.
7. Any required disclaimer/disclosure is attached.
8. The click destination is generated through the governed affiliate resolver rather than hard-coded into editorial content.

## Freshness policy

Different fields need different review frequencies:

| Field | Suggested review |
|---|---|
| commission / bonus | 7 days |
| tracking / validation | 30 days |
| promotional restrictions | 30 days |
| application / relationship status | 30 days |
| merchant URL | 30 days |
| product feed availability | 30 days |
| evergreen brand description | 90 days |

These are starting governance defaults, not advertiser terms.

## Important conflict example

Current public Commission Factory pages can show a network display rate that differs from programme copy. ASICS currently displays 5% while its programme terms state a 10% base; My Muscle Chef displays 3% while its terms describe 6% for new customers and 3% for returning users. These must remain structured fields, not flattened into a single number.

## Recommended commercial resolution

Editorial content asks for:

```text
GET /commercial/programs?country=AU&category=sports&goal=save
```

The controlled commercial layer resolves the current eligible programme, approved destination and tracking parameters. Editorial templates never own volatile commission rates or affiliate URLs.

## Initial launch ordering

The first AU commercial implementation should prioritise:

1. Commission Factory network onboarding.
2. Ozdingo / Under Armour / De'Longhi / ASICS / RunDNA / More Telecom / Aussie Broadband / BambooSIM as verified public candidates.
3. Consumer reward relationships such as ShopBack and Ipsos iSay separately from publisher affiliate programmes.
4. Additional merchants only after approval and evidence gates pass.
