# AU Earn Category Vertical

**Status:** FOUNDATION IMPLEMENTED — presentation layer only  
**Date:** 2026-09-03

## Purpose

Establish the first Australian category slice beneath the AU country shell. The category is intentionally framed around user value rather than affiliate commission.

## Current route contract

- Country shell: `/au/`
- Category concept: `/au/earn/`
- Template: `wp-content/themes/affiliate-master/templates/page-au-earn.html`

The WordPress template is a routing/content foundation. It does not prove production subdomain routing or a deployed URL.

## Initial content scope

1. Paid surveys and research
2. User testing
3. Cashback and rewards
4. Tasks and offers

The first priority research candidates are ShopBack, Octopus Group, Ipsos iSay, Prolific and UserTesting. They remain separate relationship types until publisher/referral eligibility is confirmed.

## Commercial safety boundary

No live affiliate CTA, commission claim, tracking URL or merchant destination is hard-coded into this category template. Commercial records must come from the governed structured data layer after approval and freshness checks.

## Next acceptance steps

1. Build an AU earn buying-guide shell.
2. Build comparison/detail presentation states using non-live fixtures.
3. Define the governed CTA interface and resolver contract.
4. Connect only approved, verified commercial records.
5. Verify mobile, accessibility, performance, structured data, links and disclosure presentation.
6. Replace fixtures with controlled data only after the commercial verification gate passes.

## Verification boundary

The repository contains source-level implementation only. A live WordPress runtime, real subdomain routing, network account approval, affiliate click attribution and production analytics have not been independently verified here.
