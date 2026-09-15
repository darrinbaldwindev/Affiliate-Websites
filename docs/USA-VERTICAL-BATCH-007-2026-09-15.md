# USA Vertical Batch 007 — Relationship Verification + Ipsos Application Extension

**Executed:** 2026-09-15  
**Workstream:** USA Affiliate Website  
**Mode:** standing vertical autonomous batch

## Fresh scan

At batch start `main` remained `d3cf400aabe631dc6c2e37193eca8b192856eaba`; `usa/intelligence-contract` was 13 commits ahead / 122 behind with merge base `aa91449a91f67fe474414efed71957728d5f1f2e`.

No branch creation, merge, rebase, deployment, account application, credential action or live CTA activation occurred.

## Objective

Execute the next homogeneous research slice:
1. extend the reusable application pack to Ipsos iSay / Impact;
2. verify current publisher relationship state for Prime Opinion, KashKick and Toluna/ThinkAction using current first-party evidence where discoverable;
3. fail closed where public evidence is insufficient.

## Ipsos iSay / Impact

**Result:** `VERIFIED_PUBLISHER`; exact commission `UNKNOWN`; destination/account approval `HOLD`.

Current first-party Ipsos iSay partner material states affiliates earn commission for people recruited to sign up to the panel and that the program uses Impact Radius for signup, tracking and marketing materials. The public page reviewed does not state a numeric commission.

Evidence:
- https://www.ipsosisay.com/fr-fr/partner-us

Action executed:
- added a dedicated Impact / Ipsos iSay application section to `docs/USA-AFFILIATE-APPLICATION-PACK.md`;
- retained exact commission as UNKNOWN;
- required advertiser acceptance, accepted contract terms and controlled destination before CTA activation.

## Prime Opinion

**Consumer state:** `VERIFIED_CURRENT` US paid-survey product.  
**Publisher relationship:** `UNKNOWN` from current first-party evidence reviewed.

Current US Prime Opinion pages verify a US consumer survey/reward proposition and identify Prime Opinion as a Prime Insights product. Searches of current first-party Prime Opinion material in this batch did not surface a distinct public publisher affiliate agreement, network, commission, qualification event or traffic policy.

Evidence:
- https://primeopinion.com/en-us
- https://primeopinion.com/en-us/about
- https://primeopinion.com/contact

Disposition:
- retain editorial/consumer opportunity eligibility;
- do not promote a consumer/referral relationship to publisher authority;
- monetised publisher CTA remains `HOLD/UNKNOWN` until distinct first-party or accepted-network evidence exists.

## KashKick

**Consumer state:** `VERIFIED_CURRENT` US rewards opportunity.  
**Member referral:** `VERIFIED_CURRENT`.  
**Publisher relationship:** `UNKNOWN` from first-party evidence reviewed.

Current KashKick Help Center states US members must be at least 18, be a permanent US resident or citizen, and provide a valid US address. Current earning modes include surveys, games, deals, shopping and referrals. The current member referral program pays 25% of referred friends' rewards from games and deals; surveys and other earning activities are excluded from that referral stream.

KashKick also describes a B2B partner model in which brands/app developers/research partners pay KashKick for engagement, but that is not evidence of an open publisher affiliate program for this website.

Evidence:
- https://helpcenter.kashkick.com/en/articles/10752670-who-can-earn
- https://helpcenter.kashkick.com/en/articles/10771389-refer-a-friend
- https://kashkick.com/about-us/

Disposition:
- classify the 25% mechanism as `MEMBER_REFERRAL`, not publisher affiliate;
- retain publisher relationship/economics as `UNKNOWN`;
- no live publisher CTA based on the member referral evidence.

## Toluna / ThinkAction

**Publisher relationship:** `UNKNOWN / NEEDS FRESH FIRST-PARTY VERIFICATION`.

The prior registry contains evidence of a Toluna/ThinkAction affiliate-network proposition for survey/panel recruitment, but the available material was already marked stale. The current first-party-domain search in this batch did not return sufficiently specific current publisher terms, economics, qualification event or traffic restrictions to promote that record to VERIFIED_CURRENT.

Disposition:
- preserve historical/lead value only;
- do not publish current commission or network claims from stale evidence;
- keep CTA fail-closed;
- next verification should target a current Toluna/ThinkAction publisher signup/terms page or accepted private network evidence.

## Verification table

| Program | Consumer opportunity | Member/referral | Publisher relationship | Publisher economics | CTA |
|---|---|---|---|---|---|
| Ipsos iSay | VERIFIED | separate | VERIFIED_PUBLISHER via Impact Radius | UNKNOWN | HOLD pending approval/destination |
| Prime Opinion | VERIFIED US | not used as authority | UNKNOWN | UNKNOWN | HOLD |
| KashKick | VERIFIED US | VERIFIED 25% games/deals rewards | UNKNOWN | UNKNOWN | HOLD |
| Toluna/ThinkAction | historical lead | separate | UNKNOWN / stale evidence | UNKNOWN | HOLD |

## Controls passed

- fresh repo comparison first: PASS
- first-party evidence preferred: PASS
- member referral not promoted to publisher relationship: PASS
- stale Toluna evidence not treated as current: PASS
- unknown commissions remain UNKNOWN: PASS
- no raw affiliate destination committed: PASS
- no account/network acceptance inferred: PASS
- no production CTA enabled: PASS

## Result

Ipsos iSay is now application-pack ready alongside Freecash on Impact, while Prime Opinion and KashKick remain valuable consumer/editorial opportunities without verified publisher authority. Toluna/ThinkAction remains a research lead rather than a publishable current commercial relationship.

## Next vertical objective

1. Fresh-scan first.
2. Reconcile the USA registry with Batch 007 classifications for Prime Opinion, KashKick and Toluna/ThinkAction.
3. Inspect current master changes behind the USA branch and classify integration conflicts/obsolete assumptions.
4. Reconcile PR #6 description with the full current scope and evidence state.
5. Prepare a safe integration plan without autonomously rebasing or merging.