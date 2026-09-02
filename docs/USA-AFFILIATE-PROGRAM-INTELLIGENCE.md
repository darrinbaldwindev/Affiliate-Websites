# USA Affiliate Program Intelligence

**Workstream:** USA Affiliate Website  
**Status:** Country-workstream proposal / implementation input  
**Purpose:** Define the evidence-backed commercial intelligence required to select and operate US affiliate programs.

## 1. Commercial objective

Build a US consumer decision-support site that recommends legitimate opportunities based on consumer usefulness first and monetisation second. Affiliate relationships are a means of funding useful content, not a reason to recommend an inferior opportunity.

## 2. Opportunity taxonomy

Programs must be classified by the consumer activity they enable:

- Surveys
- Paid research studies
- Focus groups
- Paid interviews
- UX / website / app testing
- Product testing
- B2B / professional research
- Rewards / GPT / games / offers
- Cashback / shopping rewards
- Passive research
- Academic research
- Clinical research
- Mystery shopping
- Micro-tasking

A program may have multiple opportunity types, but each type must retain its own eligibility and evidence.

## 3. Consumer value and monetisation are separate

Maintain separate scores:

- `consumer_value_score`
- `publisher_monetisation_score`

Do not rank a program highly solely because its affiliate payout is attractive.

Consumer value should consider legitimacy, opportunity quality, expected reward, time commitment, eligibility breadth, payout options, usability, trust, privacy burden and identity-verification burden.

## 4. Affiliate vs referral distinction

Do not collapse these into one field. Record the commercial relationship type explicitly:

- Publisher affiliate
- Affiliate-network recruitment
- Participant referral
- B2B referral
- Creator/influencer program
- Other / unknown

A participant referral reward is not evidence of a publisher affiliate commission.

## 5. Commercial freshness

Maintain separate timestamps:

- `program_status_verified_at`
- `commercial_terms_verified_at`

A program can be active while its current publisher payout remains unknown. Historical commission documents must never be presented as current without fresh verification.

Recommended status values:

- ACTIVE
- PENDING_VERIFICATION
- PAUSED
- CLOSED
- CONFLICTING
- UNKNOWN

## 6. Attribution as first-class data

Where available, record:

- attribution model
- cookie / attribution window
- first-click / last-click rules
- overwrite behaviour
- qualification event
- minimum qualification requirements
- payout timing
- exclusions
- geographic restrictions
- network
- destination type

For example, registration-only CPA, completed-study CPA and purchase commission are materially different events and must not be treated as equivalent.

## 7. Evidence model

Every commercial field should retain:

- source URL / source identifier
- source type
- observed date
- effective date if stated
- evidence classification
- confidence
- conflict status
- verification notes

Evidence classifications:

- FACT
- VERIFIED
- INFERENCE
- RECOMMENDATION
- HYPOTHESIS
- UNKNOWN
- CLAIMED
- CONFLICTING

Company-reported member counts, payout totals and similar marketing claims must be labelled as company claims rather than independent facts.

## 8. US-specific fields

At minimum:

```text
program_id
program_name
merchant_owner
country
opportunity_type
consumer_value_score
publisher_monetisation_type
publisher_payout
consumer_reward
program_status
program_status_verified_at
commercial_terms_verified_at
network
attribution_model
attribution_window
qualification_event
eligibility
age_requirement
identity_verification_required
data_sensitivity_level
privacy_notes
device_requirements
time_commitment
payout_methods
payout_timing
shipping_or_location_requirements
restrictions
source
source_type
evidence_confidence
conflict_status
last_reviewed
next_review_due
destination
```

## 9. Initial US candidate set

### Priority A / launch candidates

1. Freecash
2. User Interviews
3. Survey Junkie
4. UserTesting
5. Respondent
6. Ipsos iSay
7. Branded Surveys
8. FocusGroup.com / Sago

### Priority A/B

9. Swagbucks
10. Prime Opinion
11. KashKick
12. Prolific
13. AttaPoll
14. Fieldwork
15. Toluna / ThinkAction

### Specialist / monitoring

- YouGov
- Rare Patient Voice
- specialist academic research platforms
- specialist product-testing platforms
- mystery-shopping platforms

This is a research shortlist, not an approval to publish every candidate.

## 10. Current evidence notes

### Freecash

Current first-party material supports a publisher partner program through Impact and advertises CPA economics for qualifying registrations. Current US referral terms also exist. Publisher affiliate and participant referral must remain separate records.

### User Interviews

Current first-party material supports both participant referral and a researcher/publisher affiliate pathway. The researcher affiliate proposition is materially different from participant acquisition and should be represented separately.

### Survey Junkie

Current first-party partnership material supports publisher participation. Exact current publisher economics should remain UNKNOWN until directly verified.

### UserTesting

Current first-party material supports paid participant testing and an affiliate relationship. Exact current publisher economics should remain UNKNOWN until directly verified.

### Respondent

Current first-party material supports participant referrals and paid research opportunities. Referral documentation has shown conflicting reward amounts across first-party surfaces; publish no single amount until reconciled.

### Ipsos iSay

Current first-party material supports publisher recruitment through Impact. Exact current commission should remain UNKNOWN unless directly confirmed.

### Branded Surveys

Current first-party affiliate terms support registration-based affiliate attribution and qualification rules. Exact current commission should remain UNKNOWN unless directly confirmed.

### Swagbucks

Current consumer operation is verified. Historical first-party affiliate economics exist, but historical figures must not be treated as current. Current publisher terms require fresh verification.

### FocusGroup.com / Sago

Current first-party consumer research participation is verified. Publisher economics require separate verification.

## 11. Privacy and trust

Privacy burden is a commercial decision factor. Passive research, detailed profiling, health research and government-ID verification require additional disclosure and should not be ranked solely on payout.

Health and clinical research must receive specialist governance before publication.

## 12. No-fabrication rule

Never invent or infer as fact:

- current commission rates
- cookie windows
- EPC
- approval status
- consumer payout
- availability
- reviews or ratings
- eligibility
- merchant relationships
- tracking behaviour

If current evidence is unavailable, use `UNKNOWN` and schedule verification.

## 13. Recommended launch scoring

Suggested weighted model:

- Consumer value: 35%
- Evidence / trust: 20%
- Monetisation potential: 15%
- US eligibility / reach: 10%
- Content depth / SEO utility: 10%
- Privacy / friction adjustment: 10%

The score is a prioritisation aid, not a factual claim about earnings.

## 14. Merge candidates for Master template

**MERGE CANDIDATE — separate consumer value and monetisation scores**  
Prevents commission-first ranking.

**MERGE CANDIDATE — separate program status and commercial-term verification dates**  
Prevents active-program assumptions from becoming stale commission claims.

**MERGE CANDIDATE — attribution as a first-class commercial object**  
Supports reliable click resolution and reporting.

**MERGE CANDIDATE — opportunity-type taxonomy**  
Enables useful matching and category-level SEO rather than generic affiliate lists.

**MERGE CANDIDATE — privacy-adjusted ranking**  
Makes data sensitivity and identity requirements visible in recommendations.

## 15. Next implementation step

Convert the candidate set into a structured US program registry with one evidence record per material commercial claim. Resolve conflicting and UNKNOWN commercial terms from current first-party/network sources before any program is marked PUBLISHABLE.
