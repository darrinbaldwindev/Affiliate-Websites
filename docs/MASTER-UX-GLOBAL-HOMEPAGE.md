# Master UX & Global Homepage Specification

**Version:** 1.0  
**Status:** Master implementation contract

## 1. UX doctrine

The core journey is **discover → understand → trust → click**.

The experience must be:

- lightweight
- mobile-first
- attractive but restrained
- fast
- accessible
- useful before commercial
- transparent about affiliate relationships
- free of deceptive urgency, fake scarcity and misleading CTAs

## 2. Global homepage role

The global homepage is the authority, orientation and country-routing layer. It should explain what the platform does and route users to the appropriate country experience rather than becoming a giant opportunity directory.

### Section order

1. Header/navigation
2. Hero and country selection
3. Earn / Save / Compare opportunity overview
4. Small set of featured decision-support modules
5. How it works
6. Trust and methodology
7. AU / UK / US country paths
8. Selected guides/comparisons/articles where genuinely useful
9. FAQ where useful
10. Footer, disclosures and legal links

## 3. Country selector

AU, UK and US are first-class choices. Geolocation can provide convenience but must not prevent manual country selection or access to another legitimate country experience.

Country selection should be explicit and persistent where appropriate. Destination pattern:

```text
au.domain
uk.domain
us.domain
```

## 4. Design system

Define reusable tokens in `theme.json` and patterns for:

- typography
- spacing
- content widths
- breakpoints
- buttons
- cards
- badges
- borders/radius/shadows
- colour roles
- focus states

Use semantic colour roles such as background, surface, text, muted, border, primary action, secondary action, trust/success, warning and error.

## 5. Component library

### Primitives

Container, Stack, Cluster, Grid, Heading, Text, Button, Link, Badge, Icon, Divider.

### Navigation

Header, primary navigation, mobile navigation, search, country selector, breadcrumbs.

### Commercial/editorial

Hero, Opportunity Card, Product Card, Merchant Card, Comparison Table, Recommendation Card, CTA Block, Affiliate Disclosure, Trust/Methodology Block, Source/Evidence Block, FAQ, Related Content, Footer.

Prefer native WordPress blocks and patterns. Add custom blocks only where native blocks cannot provide the required behaviour, accessibility or performance.

## 6. Opportunity card

Minimum visible information:

- name
- short proposition
- reward/opportunity type
- country availability
- verification/trust signal
- accurate primary CTA

Progressively disclose deeper details on the destination page.

## 7. CTA rules

CTA labels must describe the real action. Examples:

- See Opportunity →
- Check Availability →
- Join & Earn →
- Get Cashback →
- Compare Options →
- Read Guide →

Avoid vague labels such as `Click Here`.

## 8. Country homepage

Reusable structure:

1. Country header/navigation
2. Country hero
3. Opportunity categories
4. Featured opportunities
5. Comparison module
6. Buying guides
7. Merchant/product modules where relevant
8. Trust/methodology
9. FAQ
10. Related content
11. Footer/disclosures

Country content and commercial claims remain country-workstream owned.

## 9. Trust UX

Trust information should appear at decision points. Reusable trust blocks support methodology, source attribution, verification date, update date, author/editor, limitations, affiliate relationship and correction pathway.

Evidence states:

`FACT`, `VERIFIED`, `INFERENCE`, `RECOMMENDATION`, `HYPOTHESIS`, `UNKNOWN`, `CLAIMED`, `IMPLEMENTED`, `VERIFIED IMPLEMENTATION`.

## 10. SEO/AEO

Use strong conventional SEO foundations: semantic HTML, unique metadata, clean URLs, canonicals, hreflang, XML sitemaps, robots controls, breadcrumbs, appropriate structured data, clear entities, factual answers, source attribution, author/editor information, freshness and internal linking.

Special AI markup or `llms.txt` must not be a core dependency.

## 11. Accessibility

Semantic landmarks/headings, keyboard operation, visible focus, accessible names/labels, sufficient contrast, meaningful alt text, accessible tables/forms, validation messaging and screen-reader-compatible mobile navigation are required.

## 12. Performance

The theme should minimise CSS/JS, third-party scripts and database-heavy frontend dependencies. Use responsive images, appropriate lazy loading, CDN/cache compatibility and representative Core Web Vitals measurement.

## 13. Commercial layer

Editorial content must not contain scattered raw affiliate tracking URLs. Commercial destinations are resolved centrally so country, program status and current relationship can be applied consistently and changes can be made without rewriting editorial content.

## 14. Vertical-slice acceptance

The first implementation must demonstrate:

`Global homepage → country selector → AU country shell → category → guide/comparison → detail → commercial CTA`

before broadening the system. The same framework must subsequently support UK and US without separate theme codebases.
