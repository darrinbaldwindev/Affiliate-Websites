# AU Affiliate Application Queue

## Objective

Create a practical first application sequence for the Australian implementation. This is an operator queue, not a claim that any relationship has already been approved.

## Apply first

| Order | Target | Route | Why first | Gate before publishing |
|---:|---|---|---|---|
| 1 | Commission Factory | Publisher application | Gives access to the largest immediate AU merchant pool and tracking infrastructure | Account approved + individual advertiser approvals |
| 2 | Awin | Publisher application | Broad international advertiser pool and AU publisher support | Account approved + individual advertiser approvals |
| 3 | Ozdingo | Commission Factory advertiser application | Strong displayed economics, broad catalogue and AU relevance | Advertiser approval + final approved rate |
| 4 | Under Armour | Commission Factory advertiser application | 8% public rate, 30-day cookie, feed | Approval + placement restrictions |
| 5 | De'Longhi AUNZ | Commission Factory advertiser application | 7.5%, 30-day cookie, product feed | Approval + feed access |
| 6 | ASICS | Commission Factory advertiser application | Strong brand + product feed + running content | Approval + resolve displayed/terms rate conflict |
| 7 | RunDNA | Commission Factory advertiser application | 7%, ~A$180 AOV, feed | Traffic-source approval |
| 8 | More Telecom | Commission Factory advertiser application | 15% public rate + telecom comparison intent | Approval + non-commissionable SKU rules |
| 9 | Aussie Broadband | Commission Factory advertiser application | Tiered CPA can support high-value comparison content | Approval + residential-only rules + content approval |
| 10 | BambooSIM | Commission Factory advertiser application | 10%, digital delivery, deep links/API/custom partnership potential | Approval + current rate/terms |

## Separate relationship outreach

These should not be treated as ordinary merchant applications:

- ShopBack — pursue publisher/commercial relationship; public cashback economics do not prove our eligibility.
- Octopus Group — pursue a publisher/referral partnership; public member referral terms do not prove a site-level relationship.
- Ipsos iSay — pursue a partnership or approved referral route; current public consumer referral programme is restricted to eligible members.
- Prolific — establish whether a publisher/partner acquisition route exists before creating a monetised CTA.
- UserTesting — investigate the affiliate/partner route separately from the contributor programme.

## Do not publish yet

No programme should receive a live revenue CTA merely because:

- its public website exists;
- it has a consumer referral URL;
- another website links to it;
- a search result reports a commission;
- Commission Factory lists it but our publisher account/programme approval is not confirmed.

## Approval evidence to capture

For each successful application record:

1. Network account ID (stored securely, not in public repo).
2. Advertiser/program ID.
3. Approval timestamp.
4. Approved commission structure.
5. Attribution/tracking terms.
6. Promotion restrictions.
7. Product feed/deep-link availability.
8. Approved traffic sources.
9. Current programme terms URL.
10. Next verification date.

Never commit private credentials, API keys, publisher IDs that are intended to remain confidential, or payment information to the repository.

## Immediate implementation consequence

The WordPress site should be capable of rendering a programme card with a non-commercial informational state before approval, but the commercial CTA should remain disabled until the governed eligibility gate passes.
