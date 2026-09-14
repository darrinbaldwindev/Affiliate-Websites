# USA Vertical Batch 003 — Affiliate Account Readiness

**Executed:** 2026-09-15  
**Workstream:** USA Affiliate Website  
**Mode:** standing vertical autonomous batch  
**Objective:** convert the six destination-ready USA relationships into an actionable account/application checklist for Impact, Awin, User Interviews and Survey Junkie without guessing private account state.

## 1. Fresh repository scan

Current `main` baseline observed at batch start:

- `a29923fa52b475d6236d61963055c0c1d8609a87`

Current USA branch before this batch:

- branch: `usa/intelligence-contract`
- PR #6: open, not merged, latest fetch `mergeable=false`
- head before this batch: `d9b169cb5d42b7099a0de4411a29ea431e596131`
- divergence from `main`: **7 commits ahead / 116 commits behind**
- merge base: `aa91449a91f67fe474414efed71957728d5f1f2e`

The USA branch remains research/input only. No merge, rebase, deploy, credential change, live affiliate application, or production destination creation was performed.

## 2. Governing rule

A public program page or network signup page proves that an application path exists. It does **not** prove this project already has an approved publisher account, advertiser acceptance, tax setup, payment setup, or live tracking destination.

Private account state therefore remains `UNKNOWN` unless explicit account evidence is available.

## 3. Cross-network prerequisite matrix

| Platform / relationship | Public prerequisites now verified | Can prepare automatically from project/repo | Owner/private action required | Approval evidence required before CTA | Current state |
|---|---|---|---|---|---|
| Impact partner account / Freecash | account identity; mobile/email verification; business model; promotional methods; account type; display/company details; country/region; mailing address; timezone; payout currency; tax information; at least one verified media property; marketplace application | site description; audience proposition; content categories; promotional-method narrative; candidate media-property list; compliance/disclosure copy; Freecash campaign rationale | create/sign into account; verify phone/email; confirm legal entity/account type; confirm tax residency; provide tax forms; choose irreversible payout currency; verify ownership of media property; accept agreements | Impact marketplace approval + Freecash program acceptance/contract + approved canonical destination | BLOCKED_FOR_LIVE_CTA |
| Awin publisher account / SurveyRewards US + QuickRewards | company/display name; tax residency; personal contact; primary promotional type; promotional-space URL and description; relevant sectors; acceptance of publisher terms; compliance review; tax/payment details after joining | promotional-space description; sector mapping; site/audience summary; traffic-method statement; merchant-specific application notes; disclosure/compliance copy | create/sign into publisher account; confirm legal/tax residency; provide required tax number/docs; provide payment details; complete any identity/payment verification; accept terms; apply to each advertiser | Awin publisher approval + separate SurveyRewards US acceptance + separate QuickRewards acceptance + canonical destinations | BLOCKED_FOR_LIVE_CTA |
| User Interviews participant affiliate | relevant/high-quality site and audience; transparent affiliate disclosure; no paid ads, keyword bidding or audience arbitrage; affiliate relationship initiated via current program contact | affiliate suitability statement; audience description; editorial examples; disclosure language; traffic-source declaration; compliance statement | send/join through current affiliate contact/onboarding; provide requested identity/payment/invoicing details; accept any private terms | explicit affiliate acceptance + assigned referral link/destination + payout/invoicing terms | BLOCKED_FOR_LIVE_CTA |
| User Interviews researcher affiliate | site with high-quality relevant content; professional audience such as PM/UX/research; application form; qualified discovery call model | B2B audience profile; relevant content examples; site description; intended placements; disclosure text; application narrative | submit application; provide owner/contact identity; accept private program terms; complete payment setup | researcher-affiliate acceptance + unique landing page/link + canonical B2B destination | BLOCKED_FOR_LIVE_CTA |
| Survey Junkie publisher program | first/last name; email/password; company name/address/country/phone; primary website URL + description; tax classification; pay-to details; PayPal field; EIN/SSN field; business-registration jurisdiction; service agreement; 18+ declaration | website description; traffic/audience summary; compliance/disclosure copy; program-fit statement; site URL once final USA property is confirmed | submit personal/company data; confirm legal entity; provide tax ID; provide payment destination; identify business-registration jurisdiction; accept service agreement | direct publisher approval + accepted private payout/conversion terms + canonical destination | BLOCKED_FOR_LIVE_CTA |

## 4. Impact / Freecash readiness

Current Impact documentation shows partner signup requires account/profile information, verified contact channels, promotional methods and at least one verified media property before marketplace participation. The marketplace application also requires tax residency/tax forms. Brand applications are separate from marketplace approval; accepted brand contracts carry final compensation and requirements.

### Auto-preparable package

The USA workstream can prepare without private credentials:

```text
site_name
site_url
site_description
audience_description
content_and_interests
business_model_description
promotion_methods[]
media_properties[]
traffic_sources[]
compliance_statement
affiliate_disclosure_text
Freecash_fit_statement
```

### Owner/private fields

Do not infer or store these in public repo documentation:

```text
legal_entity_name
account_type (individual/company)
mailing_address
mobile_number
login_email
password/SSO
tax_residency
tax_forms / tax IDs
indirect_tax_status
payout_currency
payment_destination
identity-verification material
```

`payout_currency` deserves explicit owner confirmation because Impact says it cannot be changed after that onboarding step.

### Gate

`Impact account approved` → `Freecash program applied/accepted` → `contract terms captured` → `canonical destination created` → `CTA may become eligible`.

## 5. Awin / SurveyRewards US + QuickRewards readiness

Awin's current publisher onboarding asks for primary region, promotional type, promotional-space URL and description, relevant sectors, and acceptance of publisher terms. Awin then reviews publisher applications. Advertiser programs are applied to separately after publisher approval.

Awin also requires tax/payment data for commission payment; exact required documents vary by tax residency. Therefore this workstream must not infer a tax form solely from the country served by the website.

### Auto-preparable package

```text
publisher_display_or_company_name
promotional_space_url
promotional_space_description
primary_promotion_type
relevant_sectors[]
audience_description
traffic_methods[]
content_examples[]
merchant_application_note_surveyrewards
merchant_application_note_quickrewards
affiliate_disclosure_text
```

### Owner/private fields

```text
legal_name
login_email
password
actual_tax_residency
business_type
registered_business_address
tax_number / tax document where required
payment details
identity/payment verification data
terms acceptance
```

### Separate advertiser gates

Do not treat Awin network acceptance as merchant acceptance.

1. Publisher account approved.
2. Apply to SurveyRewards US.
3. Capture advertiser acceptance and current terms.
4. Create SurveyRewards canonical destination.
5. Separately apply to QuickRewards.
6. Capture advertiser acceptance and current terms.
7. Create QuickRewards canonical destination.

## 6. User Interviews readiness

### Participant affiliate

Current public participant-affiliate guidance requires clear disclosure, forbids paid advertising and keyword bidding, forbids audience arbitrage, and currently directs interested affiliates to contact the program. Commission is tied to a newly referred participant completing a study.

Auto-preparable:

```text
site_description
audience_description
why_audience_is_relevant
planned_editorial_pages[]
traffic_sources[] = organic/editorial/email/social as actually applicable
paid_ads = false
keyword_bidding = false
audience_arbitrage = false
disclosure_copy
```

Owner/private action:

- initiate contact/onboarding;
- provide requested identity and invoicing/payment data;
- accept private program terms;
- obtain assigned affiliate link/identifier.

### Researcher affiliate

Current public page says UI evaluates site quality/relevance and whether the audience contains professionals who conduct research, such as product managers, UX/UI designers and user researchers. Application submission is required.

Auto-preparable:

```text
professional_audience_profile
research_related_content_examples[]
site_quality_summary
intended_B2B_placements[]
application_pitch
disclosure_copy
```

Owner/private action:

- submit application/contact details;
- accept program terms;
- receive unique landing page/link;
- complete payment setup.

Participant and researcher programs remain separate canonical records and destinations.

## 7. Survey Junkie readiness

The current first-party publisher application explicitly requests:

- first name / last name;
- email and password;
- company name;
- address, country and phone;
- primary website URL and website description;
- tax classification;
- pay-to selection;
- PayPal address field;
- EIN/SSN field;
- business-registration jurisdiction;
- acceptance of the Publisher Service Agreement;
- confirmation that the applicant is at least 18.

Because several of these are private identity/tax/payment fields, the workstream can prepare the commercial narrative but cannot truthfully submit or complete this application autonomously without owner-supplied account data and explicit acceptance of contractual terms.

### Auto-preparable

```text
primary_website_description
audience_description
traffic_sources[]
content_categories[]
compliance_statement
disclosure_copy
privacy_treatment_for_Surf_to_Earn
```

### Owner/private action

```text
personal identity fields
company/legal identity
address and phone
login credentials
tax classification
EIN/SSN or applicable tax identifier
payment destination / PayPal
business-registration jurisdiction
contract acceptance
18+ declaration
```

## 8. Common application pack to prepare once

A reusable non-sensitive affiliate application pack should be maintained for all networks:

```text
brand/site name
canonical site URL
one-sentence positioning
100-250 word publisher description
audience profile
countries served
content categories
traffic sources
promotion methods
SEO/editorial strategy
email/social usage if applicable
paid-media policy
incentivized-traffic policy
affiliate disclosure standard
privacy/trust statement
example high-quality pages
contact role (not private address/ID)
```

This pack can be reused across Impact, Awin, User Interviews and Survey Junkie while program-specific claims remain separate.

## 9. What can be automated now

The USA workstream can autonomously prepare:

- publisher/site description;
- audience definition;
- promotional-space descriptions;
- category/sector mappings;
- traffic-source declarations based on intended site architecture;
- affiliate disclosure copy;
- program-specific application pitches;
- compliance assertions that are true by design (for example, no keyword bidding planned where prohibited);
- a checklist of outstanding private/account fields;
- destination-record templates that remain disabled/null.

It cannot autonomously truthfully complete:

- legal identity selections;
- tax residency or tax classifications;
- tax IDs/forms;
- payment details;
- phone/email verification;
- contractual acceptance on the owner's behalf unless specifically authorized in an interactive account flow;
- identity verification;
- merchant/network acceptance;
- production tracking-link creation before approval.

## 10. Immediate owner-input minimum

To unlock the first real applications, the smallest owner-side decision set is:

1. confirm the legal applicant/entity to use for affiliate programs;
2. confirm actual tax residency/business registration jurisdiction;
3. confirm the primary publisher/site URL to present to networks;
4. choose/contact email and phone for network verification;
5. choose payment destination where required;
6. explicitly accept each network/program agreement during application.

These are deliberately not inferred from user location, site geography, repository identity, or prior project context.

## 11. Verification

- Fresh repository/PR state was inspected before research.
- Current first-party Impact onboarding/marketplace documentation reviewed.
- Current first-party Awin publisher onboarding, terms and tax guidance reviewed.
- Current User Interviews participant and researcher affiliate pages reviewed.
- Current Survey Junkie publisher application reviewed.
- No account state was invented.
- No credentials, tax IDs or payment details were requested or stored in repo.
- No live application was submitted.
- No production destination or tracking link was created.
- No new branch, merge, rebase or deploy occurred.

## 12. Result

The next bottleneck is now precisely defined: **the research and non-sensitive application material can be prepared autonomously, but legal/tax/payment identity plus account verification and contractual acceptance are the hard external gates.**

The strongest sequence remains:

1. prepare one reusable affiliate application pack;
2. use it for Impact/Freecash;
3. use it for Awin, then apply separately to SurveyRewards US and QuickRewards;
4. apply separately to both User Interviews affiliate paths;
5. complete Survey Junkie once legal/tax/payment fields are available;
6. create canonical destinations only after acceptance evidence exists.

## 13. Next autonomous vertical objective

On the next `cont` / `continue autonomously`:

1. fresh-scan first;
2. create the reusable **USA Affiliate Application Pack** using only repo-confirmed project/site positioning and non-sensitive fields;
3. draft network-specific application text for Impact, Awin, User Interviews participant, User Interviews researcher and Survey Junkie;
4. create a compact owner-input checklist containing only unresolved legal/tax/payment/contact fields;
5. keep all guessed/private fields blank and all production CTAs fail-closed.
