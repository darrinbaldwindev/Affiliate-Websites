# Software & Games Affiliate Account Readiness — 2026-09-14

**Status:** research-only readiness record. No application, approval, credential, live tracking URL or production integration is implied.

## Green Man Gaming

Primary source: https://www.greenmangaming.com/affiliates

Current evidence:
- website operators are directed to the **Business Affiliate Program**;
- commission starts at up to 5% per sale, with 10% on GMG bundles;
- approved business affiliates can access the product catalogue API covering 7,000+ games;
- partner networks provide tracking/offer links.

Project prerequisites before application:
1. production-ready website/domain and software/games editorial surface;
2. affiliate disclosure/privacy pages;
3. business/contact identity suitable for the partner-network application;
4. canonical country configuration and governed CTA resolver ready to store approval/network identifiers separately from editorial content.

**Readiness:** APPLY_LATER — technically attractive, but do not apply until the public site and disclosure surface are ready.

## GOG

Primary sources:
- https://affiliate.gog.com/
- https://support.gog.com/hc/en-us/articles/4405004689297-How-to-join-the-GOG-Affiliate-Program

Current evidence:
- programme advertises 6% of net sales, 7-day last-click tracking and a Product Feed API;
- programme is open to media, creators, enthusiasts and business partners, but approval is not guaranteed;
- GOG support instructs applicants to email `affiliate@gog.com` with a website/channel link and register the relevant channel with Adtraction;
- each channel must be registered/approved, then used to apply to the GOG programme;
- GOG documents a 200 requests/hour/IP limit on the `api.gog.com/products/*` endpoint, while other documented game endpoints have different limits.

Project prerequisites before application:
1. live website/channel URL;
2. Adtraction publisher/channel account;
3. affiliate disclosure/privacy pages;
4. feed ingestion that respects documented rate limits and stores freshness metadata;
5. no production tracking links until both Adtraction channel and GOG programme approval are evidenced.

**Readiness:** APPLY_LATER — strong feed fit; approval and Adtraction channel evidence remain mandatory.

## Fanatical

Primary sources:
- https://www.fanatical.com/en/affiliates
- https://support.fanatical.com/hc/en-us/articles/360001415777-Affiliate-Partner-FAQ

Current evidence:
- current affiliate landing page says the global programme operates through **Awin** and is free to join;
- it welcomes website/blog, creator, incentive/loyalty and editorial partners;
- an older support FAQ still references CJ for traditional websites and Tapfiliate for video/stream channels.

Because the current landing page and older FAQ conflict on the network used for traditional websites, the canonical project state is **NETWORK_REQUIRES_RECONFIRMATION_AT_APPLICATION**. The newer/current landing page should be preferred operationally, but no production integration should assume a network until the application destination is verified at application time.

Project prerequisites before application:
1. live website/domain;
2. disclosure/privacy pages;
3. publisher identity/payment details required by the current network;
4. confirmation of the current network/application path immediately before account creation.

**Readiness:** APPLY_LATER_WITH_NETWORK_RECHECK.

## Gamers-Outlet

Primary sources:
- https://www.gamers-outlet.net/en/affiliate/login
- https://www.gamers-outlet.net/en/affiliate/register
- https://www.gamers-outlet.net/en/affiliate-agreement

Current evidence:
- programme is free and publicly advertises a standard 8% commission;
- registration requests identity/contact details, website, optional company/tax information and a payout method;
- payout methods shown include cheque, PayPal and bank transfer;
- agreement states payout can be requested once balance reaches EUR 50 and commission is based on net sales after returns, chargebacks and discounts.

Project prerequisites before application:
1. public website/domain;
2. affiliate disclosure/privacy pages;
3. payment/tax/business details as applicable;
4. offer-level licence provenance policy kept active — programme approval does not prove the provenance or equivalence of an individual Windows/Office key.

**Readiness:** APPLY_LATER — commercially simple application path, but offer-level licence assurance remains a separate hard gate.

## Portfolio rule

Merchant/program approval and offer publishability are independent gates. A merchant can be approved while a specific offer remains blocked for stale price, wrong country, unknown licence type, uncertain transferability/account binding, device-count ambiguity, activation ambiguity or marketplace seller provenance.
