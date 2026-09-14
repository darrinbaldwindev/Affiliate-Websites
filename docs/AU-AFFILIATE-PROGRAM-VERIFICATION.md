# Australia Affiliate Program Verification — Round 2

**Verification date:** 2026-09-03
**Scope:** Current public evidence for the highest-priority AU commercial candidates.

## Verified publisher-network candidates

| Program | Network | Current displayed economics | Tracking / validation | Feed / deep-link signal | Key restrictions / notes | Status |
|---|---|---:|---|---|---|---|
| Ozdingo Shopping | Commission Factory | 15% displayed per sale; program copy also states 10% | 30d / 30d | Promotions; confirm feed after approval | Open promotional methods except PPC; AU stock; broad catalogue | VERIFIED-PUBLIC |
| Under Armour | Commission Factory | 8% per sale | 30d / 45d | Daily product feed | Manual de-dupe against other channels; free shipping over A$129 | VERIFIED-PUBLIC |
| ASICS | Commission Factory | 5% displayed; program terms state 10% base | 30d / 60d | Data feed | Product exclusions; UNiDAYS codes non-commissionable | VERIFIED-PUBLIC / RATE-CONFLICT |
| De'Longhi AUNZ | Commission Factory | 7.5% per sale | 30d / 30d | Product datafeed | AU/NZ market; broad appliance content opportunity | VERIFIED-PUBLIC |
| RunDNA | Commission Factory | 7% per sale | 30d / 30d | Updated feed | Traffic sources require approval; no Facebook PPC; no direct-to-merchant PPC | VERIFIED-PUBLIC |
| Red Equipment | Commission Factory | 10% default; 5% voucher; 5% paddleboard sales | 30d / 30d | Confirm feed after approval | Trademark PPC prohibited; only authorised voucher codes | VERIFIED-PUBLIC |
| Technogym Australia | Commission Factory | 5% per sale | 30d / 30d | Confirm after approval | AU website sales only; PPC prohibited | VERIFIED-PUBLIC |
| Linen House | Commission Factory | 5% per sale | 30d / 30d | Confirm after approval | PPC prohibited; performance may unlock higher commission; AOV > A$180 | VERIFIED-PUBLIC |
| OzMobiles | Commission Factory | 2% per sale | 30d / 90d | Confirm after approval | AU shipping; coupon-code restrictions; 12-month warranty / 30-day returns stated | VERIFIED-PUBLIC |
| My Muscle Chef | Commission Factory | 3% displayed; program terms state 6% new customer / 3% returning | 30d / 30d | Confirm after approval | No commission on referral/corporate codes; repeat subscriptions non-commissionable | VERIFIED-PUBLIC / RATE-CONFLICT |
| More Telecom | Commission Factory | 15% per sale | 30d / 30d | Confirm after approval | Some hardware SKUs may be non-commissionable | VERIFIED-PUBLIC |
| Aussie Broadband | Commission Factory | A$18–A$75 broadband CPA by cart tier; mobile A$6–A$12 from stated October schedule | 14d / 30d | Banners; confirm feed | Residential plans only; phone sales non-commissionable; content approval required | VERIFIED-PUBLIC |
| BCF | Commission Factory | 0.5% coupon / 2% content / 3% loyalty-cashback | 10d / 45d | Confirm after approval | Clearance 0% CPA; channel-specific rates | VERIFIED-PUBLIC |
| BambooSIM | Commission Factory | 10% per sale | 30d / 30d | Product feeds + deep links | Travel eSIM; open to custom campaigns/API/white-label discussions | VERIFIED-PUBLIC |
| Global Shop Direct | Commission Factory | Up to 10%; 5% comparison/coupon, 7% cashback, 8% loyalty, 10% content | Confirm program terms | Product feed | Paid search excluded; internal coupon codes non-commissionable | VERIFIED-PUBLIC |
| Crazy Sales | Commission Factory | 5% per sale | 30d / 60d | Full product feed | Strict no-PPC policy; 9,000+ products stated | VERIFIED-PUBLIC |

## Consumer referral/reward candidates

### Ipsos iSay

The Australian Refer a Friend programme is publicly documented. A successful referral earns the referring member 500 points after the referred person joins, completes their profile and completes at least one survey. The referred person must be 18+ and live in Australia; rewards are capped at 10 successful referrals per month. This is a **consumer referral programme**, not evidence of a publisher affiliate agreement.

### ShopBack

ShopBack Australia states that cashback is funded from commissions paid by affiliate stores after successful purchases. This establishes the underlying affiliate economics of the consumer cashback product, but does **not** by itself establish that Affiliate Websites has a publisher relationship with ShopBack. A separate publisher/commercial relationship must be confirmed before using a ShopBack affiliate CTA for site revenue.

## Network onboarding

### Commission Factory

Commission Factory is the highest-priority AU network onboarding route. Its current publisher pages advertise 600+ brands, free publisher membership, tracking/reporting tools and weekly payments. Application requires publisher traffic sources; the application process includes billing/tax information and a card pre-authorisation. Current help guidance says publisher review can take up to three business days.

### Awin

Awin Australia currently advertises 30,000+ brands and 1M+ approved partners globally and explicitly supports publishers promoting products/services through tracked recommendations. Awin should be the second network application after Commission Factory, followed by advertiser-specific discovery.

## Commercial ranking update

### Priority A — build into the first AU commercial architecture

1. ShopBack — consumer cashback anchor; relationship to be confirmed
2. Commission Factory — network infrastructure
3. Ozdingo — broad catalogue + strong displayed commission
4. Under Armour — strong rate + feed + product intent
5. De'Longhi — high-value appliance content + feed
6. ASICS — strong brand + running/sports comparisons + feed
7. More Telecom — unusually strong percentage + recurring comparison content
8. Aussie Broadband — high-intent broadband comparison economics
9. RunDNA — strong AOV + feed + specialist authority
10. BambooSIM — high-margin digital travel product + deep-link/API potential

### Priority B — second wave

11. Red Equipment
12. Linen House
13. My Muscle Chef
14. INTERSPORT Australia
15. OzMobiles
16. Technogym Australia
17. Crazy Sales
18. Global Shop Direct
19. BCF
20. Wendy Wu Tours

## Data-governance decision

Do not store only a single `commission_rate` field. The commercial schema must support:

- `displayed_rate`
- `terms_rate`
- `rate_type`
- `new_customer_rate`
- `returning_customer_rate`
- `channel_rate`
- `tracking_days`
- `validation_days`
- `product_feed_available`
- `deep_link_available`
- `approval_required`
- `traffic_source_restrictions`
- `coupon_restrictions`
- `de_dupe_rules`
- `last_verified_at`
- `source_urls`
- `evidence_state`

Where network display and programme copy disagree, the record must be marked `RATE-CONFLICT` and the live CTA must use the currently approved rate returned by the network/account rather than an editorially inferred number.

## Source register

Public evidence reviewed on 2026-09-03 includes current Commission Factory advertiser pages for Ozdingo, Under Armour, ASICS, De'Longhi, RunDNA, Red Equipment, Technogym, Linen House, OzMobiles, My Muscle Chef, More Telecom, Aussie Broadband, BCF, BambooSIM, Global Shop Direct and Crazy Sales; Commission Factory publisher onboarding/help pages; Awin Australia publisher pages; Ipsos iSay AU referral terms; and ShopBack Australia support documentation.

This document records public evidence only. It does not claim that Affiliate Websites has been approved by any advertiser or network.
