# USA Vertical Batch 001 — Current-Main Reconciliation and CTA Readiness

**Executed:** 2026-09-14  
**Workstream:** USA Affiliate Website  
**Batch trigger:** owner requested standing vertical batching  
**Objective:** reconcile USA commercial research with current master CTA governance, then refresh the highest-value monetisable candidates.

## 1. Repository scan

Current `main` head observed at batch start:

- `d901b3e2c0c772cdc43019dd96cf2b19bdded0a6` — `test(cta): cover conflicts disclosures eligibility and audit`

The current USA branch `usa/intelligence-contract` was **3 commits ahead and 82 commits behind** `main` before this batch's USA-only documentation commits. The merge base was `aa91449a91f67fe474414efed71957728d5f1f2e`.

Conclusion: USA research remains useful, but the branch predates major master implementation work and must be reconciled against current `main` on every autonomous batch. No rebase/merge was performed.

## 2. Current master contract discovered

Current master architecture now has a governed country CTA fixture/validator covering AU, UK and US. Relevant current-main files include:

- `docs/API-CONTRACT.md`
- `fixtures/commercial-cta/country-programs.synthetic.json`
- `fixtures/commercial-cta/validate_country_cta.py`
- `fixtures/commercial-cta/test_country_cta.py`

The current Rewards API contract requires stable structured opportunity data and an approved commercial destination. Editorial content must not carry raw tracking URLs.

The current validator independently requires consumer reward evidence, country eligibility evidence and disclosure. It separates these from publisher evidence and allows only these publisher relationship states:

- `VERIFIED_PUBLISHER`
- `CONSUMER_REFERRAL_ONLY`
- `UNKNOWN`

A verified publisher CTA requires a source, verification timestamp, current evidence, verified relationship state and destination. A consumer-referral-only record must remain a non-affiliate fallback. Conflicting, stale or unknown publisher evidence cannot resolve to a verified publisher CTA.

## 3. Critical USA reconciliation finding

The existing USA research principle **publisher affiliate != participant referral** is now directly aligned with executable master behavior rather than merely being a research recommendation.

The current synthetic US fixture deliberately models `CONSUMER_REFERRAL_ONLY` and resolves it to `NON_AFFILIATE_FALLBACK`. Therefore the USA registry should now treat publisher-verification state as a concrete CTA gate, not just metadata.

### MERGE CANDIDATE status

The earlier USA merge candidates for relationship separation, evidence freshness and conflict handling are substantially represented in current master CTA governance. Future USA batches should stop proposing them as novel architecture and instead supply country evidence that satisfies the contract.

## 4. Live commercial revalidation — highest-value slice

Observed 2026-09-14 from current first-party/network sources.

### Freecash — CTA candidate: VERIFIED-PUBLISHER INPUT READY, destination still approval-dependent

Current first-party partner material continues to state:

- partner onboarding through Impact;
- CPA of **$3-$10** for a simple email registration;
- no user purchase required for that registration conversion;
- custom CPA deals may be issued during onboarding.

Current partner advertising guidelines, updated July 2026, describe Freecash as rewards for games, surveys, app testing and offers and require promotional accuracy.

Sources:
- https://freecash.com/academy/en/discover/partner/become-a-partner
- https://freecash.com/en/policies/partner-advertiser-policy

USA decision:
- consumer proposition: CURRENT;
- publisher relationship: VERIFIED_PUBLISHER;
- publisher evidence conflict: false in current evidence reviewed;
- commercial terms: CURRENT first-party public claim;
- destination: **NOT YET APPROVED/CONFIGURED in repo evidence reviewed**;
- publishable CTA: BLOCKED until controlled destination exists.

### User Interviews — CTA candidate: VERIFIED-PUBLISHER INPUT READY, two distinct relationships

Current first-party researcher affiliate page continues to state **$100 per qualified discovery call**.

Current participant affiliate page continues to state at least **$15** and currently up to **$30** for a newly referred participant who completes a study, plus a volume bonus above 100 qualifying participants/month.

Current participant guidance also says acceptance into studies is selective and that it is typical to be approved for only **1-2 studies per year**, reinforcing the editorial rule that paid research is not guaranteed income.

Sources:
- https://www.userinterviews.com/research-affiliates
- https://www.userinterviews.com/user-interviews-affiliates
- https://support.userinterviews.com/hc/en-us/articles/51535829031571-Create-a-participant-account

USA decision:
- researcher affiliate: VERIFIED_PUBLISHER/B2B affiliate input;
- participant affiliate: VERIFIED publisher relationship but separate qualification event and audience;
- consumer earnings: variable; never present as guaranteed income;
- destination: **NOT YET APPROVED/CONFIGURED in repo evidence reviewed**;
- publishable CTA: BLOCKED until the controlled destination layer represents the chosen relationship explicitly.

### Survey Junkie — publisher relationship verified, payout still UNKNOWN

Current first-party partnerships page continues to invite affiliates and states affiliates earn commission for driving traffic. A live publisher application and service agreement flow also exists.

The public first-party material reviewed in this batch does not expose a current commission amount. Therefore exact publisher payout remains **UNKNOWN**.

Sources:
- https://www.surveyjunkie.com/partnerships
- https://affiliates.surveyjunkie.com/Account/Application
- https://affiliateterms.surveyjunkie.com/

Additional privacy note: Survey Junkie's current Surf to Earn product can track searches, websites visited, apps used, shopping activity and ads viewed after opt-in. This requires a materially higher privacy/data-sensitivity flag than ordinary survey participation.

Source:
- https://www.surveyjunkie.com/pulse-program

USA decision:
- publisher relationship: VERIFIED_PUBLISHER;
- exact payout: UNKNOWN;
- privacy burden: elevated for Surf to Earn;
- destination: not approved/configured in repo evidence reviewed;
- publishable CTA: BLOCKED pending destination plus relationship-specific evidence record.

### SurveyRewards US — strong completed-survey CPA candidate

Current Awin program terms state:

- **$0.75 per valid completed survey**;
- first 20 completed surveys per unique user;
- up to **$15 per referred user**;
- new-user requirement;
- no VPN/proxy/bot traffic;
- incentivized traffic prohibited;
- email, social, content/blog and general web traffic allowed;
- PPC requires explicit approval and brand bidding is prohibited;
- false earnings claims prohibited.

Source:
- https://ui.awin.com/merchant-profile-terms/104951

USA decision:
- publisher relationship: VERIFIED_PUBLISHER;
- qualification event: completed survey, not registration;
- commercial terms: CURRENT network evidence;
- traffic restrictions: material and must travel with destination metadata;
- destination: not approved/configured in repo evidence reviewed;
- publishable CTA: BLOCKED pending controlled destination.

### QuickRewards — simple conversion model candidate

Current Awin profile states:

- **$1** after the visitor registers and earns at least **$0.25**;
- 30-day attribution period;
- higher rates may be available for high-volume affiliates.

Source:
- https://ui.awin.com/merchant-profile/87781

USA decision:
- publisher relationship: VERIFIED_PUBLISHER;
- qualification event: registration plus $0.25 earned;
- attribution: 30 days;
- destination: not approved/configured in repo evidence reviewed;
- publishable CTA: BLOCKED pending controlled destination.

## 5. Batch result — revised USA commercial priority

### First destination-readiness queue

1. **Freecash** — strongest broad consumer + current public CPA evidence.
2. **User Interviews participant affiliate** — strong consumer/research differentiation.
3. **User Interviews researcher affiliate** — strong B2B monetisation; separate destination/record.
4. **SurveyRewards US** — unusually clear completed-survey economics and traffic rules.
5. **QuickRewards** — clear conversion event and 30-day attribution.
6. **Survey Junkie** — trusted mainstream program, but exact public commission still UNKNOWN.

This queue is for controlled destination preparation/application work, not approval to expose raw affiliate URLs.

## 6. What changed from the old USA plan

The largest current blocker is no longer finding more survey/research names. The repo now has enough master governance to make the next useful USA work **destination-readiness and structured evidence mapping**.

High-value consumer opportunities without verified publisher relationships remain editorial candidates, but they should resolve to a non-affiliate fallback until a publisher relationship is proven.

## 7. Verification

- No new branch was created.
- No merge/rebase/deploy occurred.
- No credentials were changed.
- Current-main CTA fixture and validator were inspected before this batch result was written.
- Publisher relationships and consumer referrals remain separate.
- Exact Survey Junkie payout remains UNKNOWN.
- No raw tracking URL was introduced.

## 8. Next vertical objective

Create a **USA destination-readiness matrix** for the six records above, mapping each one to the exact fields required by the current Rewards API/governed CTA contract and identifying which blocker is public evidence, private network/application acceptance, destination configuration, disclosure text, or freshness monitoring.
