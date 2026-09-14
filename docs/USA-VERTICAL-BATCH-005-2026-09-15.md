# USA Vertical Batch 005 — 2026-09-15

## Scope
Four homogeneous relationship-classification reconciliations for the USA Affiliate workstream. External public material is evidence only, never authority. No publication, application, credential, network approval, or production action is authorized by this batch.

## Security
- Risk class: S1 research/data update; repository write itself is scoped S2 non-production.
- Applicable gates: SG-05, SG-06, SG-07, SG-10, SG-14, SG-15, SG-20.
- Core rule: consumer/member referral evidence must not promote to publisher-affiliate authority.

## Fresh-state anchor
- PR: Affiliate-Websites #6
- Pre-batch head: `410dfd3e8ebdf2ffed31717463c6b3c5c84e2029`
- Branch: `usa/intelligence-contract`
- Master/CTA authority remains separate and is not modified here.

## Records consumed

### US-V5-01 — Respondent
**Result: VERIFIED_CURRENT participant/member referral; publisher affiliate UNKNOWN.**

Current first-party participant referral policy dated 2026-04-01 states:
- $20 signup/network referral after a brand-new referred participant earns $75+ from completed studies and payment is PAID;
- $50 project referral after a referred participant completes a qualifying project carrying a $100+ incentive;
- spam/misleading promotion prohibited.

Current Respondent country material includes the United States among primary recruitment markets.

Evidence:
- https://help.respondent.io/en/articles/5464425-respondent-referral-policy-for-participants
- https://help.respondent.io/en/articles/5471299-what-countries-can-i-recruit-in-on-respondent

Disposition: prior registry conflict is resolved for participant-referral economics only. Publisher economics remain UNKNOWN and must not inherit participant-referral evidence.

### US-V5-02 — UserTesting
**Result: publisher affiliate UNKNOWN; false-positive evidence removed.**

The current page titled `UserTesting Affiliates` lists corporate affiliates/subsidiaries and their business-support purposes. It is not evidence of a publisher-marketing affiliate program. Contributor terms independently support the consumer/contributor opportunity but not publisher monetisation.

Evidence:
- https://www.usertesting.com/usertesting-affiliates
- https://www.usertesting.com/privacy-center/terms-of-service-contributor

Disposition: editorial/contributor coverage remains eligible when otherwise current; monetised publisher CTA remains HOLD until a distinct publisher program is evidenced.

### US-V5-03 — Swagbucks
**Result: VERIFIED_CURRENT member referral; publisher affiliate UNKNOWN.**

Current first-party help states a member earns 10% of eligible referral earnings while the referral remains active, with no maximum on that percentage stream. Conditional bonus terms and prohibited referral-traffic methods are also documented.

Evidence:
- https://help.swagbucks.com/hc/en-us/articles/360030542251-How-do-I-Earn-SB-from-Referrals
- https://help.swagbucks.com/hc/en-us/articles/205640984-How-do-I-Earn-SB-from-Referrals

Disposition: member referral may support editorial/referral classification only. It does not prove publisher approval.

### US-V5-04 — Ipsos iSay
**Result: VERIFIED_PUBLISHER relationship; exact commission UNKNOWN; destination/approval HOLD.**

Current first-party partner material states that affiliates earn commission for panel signups and that Ipsos iSay uses Impact Radius for application/tracking/materials. The reviewed public material does not provide an exact commission amount.

Evidence:
- https://www.ipsosisay.com/fr-fr/partner-us

Disposition: relationship type may be `VERIFIED_PUBLISHER`; exact payout remains UNKNOWN. No controlled destination or live network approval is established by this research.

## Repository result
Updated `docs/USA-AFFILIATE-PROGRAM-REGISTRY.md` to:
- replace stale/conflicting Respondent wording with current first-party referral economics;
- stop treating UserTesting's corporate-affiliates page as publisher-program evidence;
- classify Swagbucks as member referral only unless distinct publisher evidence emerges;
- preserve Ipsos publisher relationship while keeping exact commission and destination approval UNKNOWN.

## Verification checklist
- referral vs publisher relationship remains separated: PASS
- unknown publisher economics remain UNKNOWN: PASS
- no raw affiliate tracking destination added: PASS
- no application/network approval inferred: PASS
- no production/publication authority added: PASS
- no credential material read or stored: PASS

## Remaining blockers / next batch
1. Build a destination-readiness matrix for the first six publisher relationships already prioritized in the registry.
2. Find a distinct current UserTesting publisher-marketing program if one exists.
3. Find a distinct Swagbucks publisher/partner program if one exists.
4. Obtain current Ipsos iSay US relationship-specific destination/approval terms without inferring commission.
5. Verify Prime Opinion, KashKick, and Toluna/ThinkAction publisher relationship states as a separate homogeneous batch.

No merge, deploy, application, credential action, outreach, live publication, spend, or production mutation occurred.