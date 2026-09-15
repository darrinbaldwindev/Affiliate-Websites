# USA Vertical Batch 002 — Destination Readiness Matrix

**Executed:** 2026-09-14  
**Workstream:** USA Affiliate Website  
**Mode:** standing vertical autonomous batch  
**Objective:** convert the six highest-priority USA commercial relationships into implementation-ready destination records aligned to the current Rewards API and governed CTA contract.

## 1. Fresh repository scan

Current `main` head at batch start:

- `661370c4226ca45e97239a728e6b3483d65c5d6e` — `docs: close software games vertical batch 002`

Current USA branch state before this batch:

- branch: `usa/intelligence-contract`
- head: `f327bcf290f9bc0e66368418d2af8cac0e6897d3`
- compared with `main`: **6 commits ahead / 103 commits behind**
- merge base: `aa91449a91f67fe474414efed71957728d5f1f2e`
- PR #6: open; latest fetch reported `mergeable=false`

Conclusion: the USA branch is now substantially stale relative to master. This batch therefore treats current `main` contracts as authoritative and performs USA-only research/documentation without merge, rebase, deploy, production destination writes, or new branch creation.

## 2. Master contract used

Current master Rewards API requires structured opportunity records with stable IDs, country/category, summary, eligibility, reward, requirements, evidence metadata, current status/freshness, and approved commercial destination metadata.

Commercial click flow:

`visitor → country → program/product/merchant → eligibility → approved current commercial relationship → destination → tracked outbound click`

Current governed CTA validation requires consumer reward evidence and country eligibility evidence independently of publisher evidence. Monetised publisher CTAs require current publisher evidence, verification timestamp, verified relationship state and a destination. Stale, conflicting or unknown publisher evidence fails closed. Consumer-referral-only records cannot masquerade as publisher affiliate CTAs.

## 3. Destination-readiness status vocabulary

For this batch:

- **EVIDENCE_READY** — enough public evidence exists to populate the research/commercial record.
- **APPLICATION_REQUIRED** — publisher/network approval still required before a live destination can exist.
- **DESTINATION_REQUIRED** — a controlled server-side destination ID/link is not yet present in repo evidence.
- **PRIVATE_TERMS_REQUIRED** — exact commercial terms require accepted account/insertion order/private network access.
- **DISCLOSURE_REQUIRED** — relationship-specific disclosure must travel with the content/CTA.
- **MONITOR** — commercial/freshness fields require ongoing revalidation.
- **BLOCKED_FOR_LIVE_CTA** — must not resolve to a production monetised CTA yet.

## 4. Six-record destination-readiness matrix

| Record | Audience / event | Publisher evidence | Economics | Eligibility / reward evidence | Traffic / disclosure constraints | Destination state | Live CTA state | Primary blocker |
|---|---|---|---|---|---|---|---|---|
| `US-FREECASH-PUBLISHER` | Consumer rewards/GPT; email-registration CPA | VERIFIED_PUBLISHER via Impact | Public first-party claim: $3–$10 CPA; custom CPA possible | Consumer proposition and broad/global availability supported; final approved traffic geo belongs to accepted account terms | Advertising must remain accurate; affiliate disclosure required | No approved production destination ID found in repo | BLOCKED_FOR_LIVE_CTA | APPLICATION_REQUIRED + DESTINATION_REQUIRED |
| `US-UI-PARTICIPANT-AFFILIATE` | Consumer paid research; new participant signs up and completes a study | VERIFIED_PUBLISHER participant-affiliate program | At least $15, currently up to $30 for qualifying participants | Consumer research participation verified; study acceptance selective; do not imply guaranteed earnings | Explicit affiliate disclosure; no paid ads/search bidding/audience arbitrage under current guidelines | No controlled relationship-specific destination found | BLOCKED_FOR_LIVE_CTA | APPLICATION/ONBOARDING + DESTINATION_REQUIRED |
| `US-UI-RESEARCHER-AFFILIATE` | B2B professional traffic; qualified discovery call | VERIFIED_PUBLISHER researcher affiliate | $100 per qualified discovery call | Audience should be research-relevant professionals such as PM/UX/research roles | High-quality relevant audience; disclosure; paid-search/bidding/arbitrage restrictions must remain attached | No controlled B2B destination found | BLOCKED_FOR_LIVE_CTA | APPLICATION_REQUIRED + DESTINATION_REQUIRED |
| `US-SURVEYREWARDS-AWIN` | Survey consumer; valid completed survey | VERIFIED_PUBLISHER via Awin | $0.75 per valid survey; first 20 per user; up to $15 | New real unique user; valid registration; successful survey completion; no VPN/proxy/bot | Incentivized traffic prohibited; PPC approval required; brand bidding prohibited; misleading earnings claims prohibited | No approved Awin destination ID found | BLOCKED_FOR_LIVE_CTA | NETWORK ACCEPTANCE + DESTINATION_REQUIRED |
| `US-QUICKREWARDS-AWIN` | Rewards consumer; registration + at least $0.25 earned | VERIFIED_PUBLISHER via Awin | $1; 30-day attribution; higher-volume rate may exist | Membership free; conversion occurs only after required earning threshold | Exact account-level traffic rules should be retained from Awin terms | No approved Awin destination ID found | BLOCKED_FOR_LIVE_CTA | NETWORK ACCEPTANCE + DESTINATION_REQUIRED |
| `US-SURVEYJUNKIE-PUBLISHER` | Survey/research consumer; publisher traffic conversion event not publicly quantified here | VERIFIED_PUBLISHER | Exact public payout UNKNOWN | Consumer survey/focus-group participation current; Surf to Earn has materially higher privacy burden | Publisher service agreement/application required; relationship disclosure required; passive-behaviour collection needs explicit privacy treatment | No approved publisher destination ID found | BLOCKED_FOR_LIVE_CTA | PRIVATE_TERMS_REQUIRED + DESTINATION_REQUIRED |

## 5. Current source verification

### Freecash

Current first-party partner material continues to state partnership through Impact and a CPA of **$3–$10 for a simple email registration**, with no user purchase required. It also says onboarding may issue a custom CPA deal.

Source: https://freecash.com/academy/en/discover/partner/become-a-partner

### User Interviews — participant affiliate

Current participant-affiliate material states affiliates are paid at least **$15** and currently up to **$30** when a newly referred participant signs up and completes a study. It requires transparent affiliate disclosure and prohibits paid advertising, keyword bidding and audience arbitrage.

Source: https://www.userinterviews.com/user-interviews-affiliates

Important distinction: the ordinary logged-in participant referral program (give/earn $10, or featured-study $30) is a separate member-referral mechanism and must not be substituted for publisher-affiliate economics.

Source: https://support.userinterviews.com/hc/en-us/articles/51535883439379-Earn-money-with-our-participant-referral-program

### User Interviews — researcher affiliate

Current researcher-affiliate material states **$100 per qualified discovery call** and targets audiences containing professionals who conduct user research, including product managers, UX/UI designers and user researchers.

Source: https://www.userinterviews.com/research-affiliates

### SurveyRewards US

Current Awin terms state **$0.75 USD per valid Survey Complete**, capped to the first 20 completed surveys per unique user, with maximum potential **$15 per unique referred user**. Qualifying leads must be real unique people with valid registration details and must not use proxies, VPNs or bots.

Source: https://ui.awin.com/merchant-profile-terms/104951

### QuickRewards

Current Awin program material states **$1** once a referred visitor registers and earns at least **$0.25**, and lists a **30-day attribution period**.

Source: https://ui.awin.com/merchant-profile/87781

### Survey Junkie

Current first-party partnerships material confirms an active affiliate program and says affiliates earn commission for driving traffic. A current publisher application exists and requests company/site/payment/tax information and acceptance of a publisher service agreement. Public material reviewed in this batch does not expose the exact commission; it therefore remains **UNKNOWN**.

Sources:
- https://www.surveyjunkie.com/partnerships
- https://affiliates.surveyjunkie.com/Account/Application
- https://affiliateterms.surveyjunkie.com/

Survey Junkie's Surf to Earn offering tracks opted-in digital behaviour such as searches, websites visited and apps used. This must be represented as a materially higher privacy/data-sensitivity path than ordinary opinion surveys.

Source: https://www.surveyjunkie.com/pulse-program

## 6. Required canonical fields before production destination creation

For each relationship above, create/retain these fields in the canonical data layer before a live destination is approved:

```text
id
country = US
category
name
status
summary
eligibility[]
reward{}
requirements[]
evidence.state
evidence.source
evidence.source_type
evidence.verified_at
commercial.available
commercial.relationship_type
commercial.network
commercial.qualification_event
commercial.attribution_window
commercial.payout_claim
commercial.payout_visibility = PUBLIC | PRIVATE | UNKNOWN
commercial.traffic_restrictions[]
commercial.disclosure_required
commercial.publisher_verified_at
commercial.commercial_terms_verified_at
commercial.conflict_status
commercial.destination_id
privacy.data_sensitivity_level
privacy.notes
monitor.next_review_due
```

A production destination must remain absent/null until network or direct-program acceptance is confirmed and the server-side destination is created through the canonical commercial layer.

## 7. Relationship separation required

User Interviews demonstrates why one merchant can require multiple canonical records:

- participant publisher affiliate;
- researcher/B2B publisher affiliate;
- ordinary participant member referral;
- featured-study participant referral.

These have different audiences, events, rewards and permitted promotion methods. They must never share one generic `affiliate` field or one undifferentiated destination.

## 8. Application and access queue

The next owner/account-access work should be performed in this order because it unlocks the strongest combination of consumer value and clear public economics:

1. **Freecash / Impact** — confirm whether an Impact publisher account/application is already available; obtain approved campaign relationship and create canonical destination only after acceptance.
2. **User Interviews participant affiliate** — apply/onboard separately from ordinary member referrals; capture accepted promotion rules.
3. **User Interviews researcher affiliate** — apply separately for professional/B2B audience; create separate destination from participant traffic.
4. **Awin / SurveyRewards US** — confirm publisher account and merchant acceptance; retain completed-survey event and traffic restrictions.
5. **Awin / QuickRewards** — confirm publisher account and merchant acceptance; retain registration+$0.25 qualification and 30-day attribution.
6. **Survey Junkie** — complete direct publisher application/service agreement, then record the private conversion/payout terms rather than inventing them.

## 9. What is ready now vs not ready

### Ready now

- six stable candidate relationship records;
- current public publisher evidence for all six;
- current public economics for five records (Freecash, both User Interviews affiliate paths, SurveyRewards US, QuickRewards);
- exact public Survey Junkie publisher payout intentionally preserved as UNKNOWN;
- qualification-event separation;
- traffic/disclosure/privacy requirements sufficient for application preparation;
- field mapping to current Rewards API / CTA governance.

### Not ready

- no claim of merchant/network account acceptance;
- no production destination IDs;
- no tracking links;
- no credential storage;
- no production CTA activation;
- no assumption that public rate equals the user's future accepted account rate;
- no merger of participant referral and publisher affiliate programs.

## 10. Batch verification

- Fresh current `main` and PR/branch state inspected first.
- Current API contract and executable CTA validator inspected.
- Current first-party/network commercial pages revalidated for the six relationships.
- No new branch created.
- No merge/rebase/deploy performed.
- No production affiliate URL introduced.
- No credentials touched.
- UNKNOWN fields remain UNKNOWN.
- Relationship-specific differences retained.

## 11. Result

The USA workstream now has a concrete bridge from research to implementation: **six commercially credible relationship records are evidence-ready but all six remain fail-closed for live monetised CTAs until account acceptance and controlled destination creation occur.**

The highest-value blocker has moved from program discovery to **publisher account/application state plus canonical destination provisioning**.

## 12. Next autonomous vertical objective

On the next `cont` / `continue autonomously`:

1. fresh-scan first;
2. determine which of Impact, Awin, User Interviews and Survey Junkie application/account prerequisites can be satisfied from current repo/project evidence without guessing private account state;
3. create a USA affiliate-account prerequisites checklist with exact required business/site/tax/payment/traffic information per network/program;
4. identify which fields can be prepared automatically and which require owner input or external account approval;
5. keep all live destinations fail-closed until approval evidence exists.
