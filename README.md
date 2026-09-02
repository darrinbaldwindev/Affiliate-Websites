# Affiliate Websites

Master WordPress template and country implementation framework for the Global Consumer Rewards & Micro-Earning Platform Engine.

## Project role

This repository is the application/source repository for the Affiliate Websites project.

- **Master template:** reusable WordPress Block Theme and shared implementation contracts.
- **Country implementations:** Australia, United Kingdom and United States use the shared framework while retaining country-specific content, commercial relationships and SEO priorities.
- **Control/log repository:** `darrinbaldwindev/Overseer` remains the governance and reporting repository.

## Architecture

```text
Global homepage
      |
      +--> AU country site
      +--> UK country site
      +--> US country site

WordPress presentation/editorial layer
      |
      +--> Rewards API
                |
                +--> PostgreSQL / Supabase

AgentOS --> research / verification / monitoring / orchestration
Cloudflare --> CDN / WAF / edge
```

WordPress is **not** the canonical rewards intelligence database. Structured rewards, merchant, affiliate and verification data belongs behind the controlled API/data layer.

## Master UX contract

Primary journey:

**discover → understand → trust → click**

The master experience is lightweight, mobile-first, accessible, fast and commercially transparent. It avoids deceptive urgency, fake scarcity, excessive popups, misleading CTAs and casino-like visual patterns.

## Country architecture

Initial country destinations:

- `au.domain`
- `uk.domain`
- `us.domain`

The same theme/framework supports all three. Country workstreams own local content, commercial data, categories, merchants, affiliate programs, pricing, SEO/AEO opportunities and compliance requirements.

## Theme strategy

Use a **custom lightweight WordPress Block Theme** based on native Gutenberg/Site Editor capabilities.

Core theme structure:

```text
wp-content/
└── themes/
    └── affiliate-master/
        ├── theme.json
        ├── templates/
        ├── parts/
        ├── patterns/
        └── assets/
```

No heavyweight page builder is a core dependency.

## Planned implementation sequence

1. Block Theme shell and design tokens
2. Global header, footer and navigation
3. Country selector/routing framework
4. Global homepage
5. Country homepage template
6. Category, comparison, product, merchant and program templates
7. Trust, methodology, source and disclosure components
8. Rewards API integration points
9. Central affiliate-resolution and click-tracking abstraction
10. SEO/schema, accessibility, performance and security validation
11. AU → UK → US vertical-slice verification

## Data integrity

Commercial facts must retain source, source type, verification date, status, confidence and freshness where applicable. Conflicting information is flagged rather than silently overwritten.

Do not publish fabricated prices, commissions, ratings, reviews, affiliate relationships, eligibility, outcomes or verification claims.

## Evidence states

Supported evidence states include:

- FACT
- VERIFIED
- INFERENCE
- RECOMMENDATION
- HYPOTHESIS
- UNKNOWN
- CLAIMED
- IMPLEMENTED
- VERIFIED IMPLEMENTATION

## Development status

Repository established. Master UX and global homepage specifications are recorded in the Overseer governance log. Application implementation begins with the Block Theme shell.

## Governance

See the Affiliate Website Template master governance and UX specifications in `darrinbaldwindev/Overseer` Issues #37–39. Material template changes should use branches and pull requests where practical; country-specific changes must not silently redefine the master architecture.
