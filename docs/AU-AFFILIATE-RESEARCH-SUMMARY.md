# AU Affiliate Research — Current Decision Summary

**As of:** 2026-09-03

## Decision

The Australian launch should be built around a small set of high-confidence commercial pathways rather than a large directory.

### Highest-value candidates currently identified

**Network infrastructure**
- Commission Factory — first application.
- Awin — second network application.

**Earn**
- ShopBack — cashback/rewards anchor; relationship must be confirmed.
- Octopus Group — local paid research/referral candidate.
- Ipsos iSay — AU referral candidate with current public referral terms.
- Prolific — premium research candidate; publisher route needs confirmation.
- UserTesting — user-testing candidate; affiliate route needs confirmation.

**Save / shopping**
- Ozdingo — unusually strong public Commission Factory economics and broad catalogue.
- Under Armour — strong rate, feed and product intent.
- De'Longhi — high-value appliances plus feed.
- ASICS — strong brand and feed; current displayed rate conflicts with programme copy.
- Linen House — strong AOV and AU brand relevance.
- Crazy Sales — large catalogue and feed.

**Compare / services**
- More Telecom — 15% public commission; useful NBN/mobile comparison opportunity.
- Aussie Broadband — tiered broadband CPA up to A$75 on qualifying cart tiers in current public programme information.
- OzMobiles — AU-only refurbished/new-device proposition; useful price-conscious technology comparison.

**Travel**
- BambooSIM — 10% public commission, 30-day tracking, deep-link/feed/API/custom partnership signals.
- Wendy Wu Tours — retain for later travel content.

## Why these win

The shortlist is weighted toward:

1. Australian eligibility and relevance.
2. Trusted or differentiated consumer proposition.
3. High purchase/intention signal.
4. Useful content depth.
5. Repeat or comparison potential.
6. Product feeds/deep links where available.
7. Meaningful commission or CPA economics.
8. Reasonable policy/restriction profile.

## Critical implementation rule

A public affiliate listing is **not** approval. The site must not create a live commercial CTA until the programme/network relationship is approved and the destination/terms are captured in the governed commercial data layer.

The research also demonstrates why a single commission field is insufficient: ASICS and My Muscle Chef currently show differences between network display rates and programme terms. The schema therefore needs displayed, approved, new-customer, returning-customer and channel-specific rate fields.

## Next autonomous stage

1. Build the AU programme seed dataset using the governed schema.
2. Build reusable programme/category/detail templates against non-volatile fields.
3. Add commercial CTA eligibility states: informational, pending approval, approved, expired/suspended.
4. Add tracking contract documentation before any real affiliate URLs are introduced.
5. Continue merchant discovery until each major AU category has sufficient verified candidates.
