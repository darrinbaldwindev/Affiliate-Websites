# Affiliate Websites — Implementation Status

**Checkpoint:** 2026-09-03

## Repository

`darrinbaldwindev/Affiliate-Websites` is the canonical application/source repository. `darrinbaldwindev/Overseer` remains the control and governance repository.

## Scan result

The repository is an intentionally minimal WordPress Block Theme foundation. The application repository is now present and implementation has begun.

Current theme assets include:

- `style.css`
- `theme.json`
- `functions.php`
- `templates/home.html`
- `templates/index.html`
- `templates/page.html`
- `templates/404.html`
- `parts/header.html`
- `parts/footer.html`
- `patterns/global-homepage.php`

## Completed in this checkpoint

- Confirmed canonical application repository and default branch `main`.
- Added minimal WordPress theme bootstrap in `functions.php`.
- Established reusable design tokens and semantic colour roles in `theme.json`.
- Added reusable header/footer template parts.
- Added global homepage starter template and reusable global homepage pattern.
- Added generic page template and accessible 404/search template.
- Recorded implementation status and governance boundaries.

## Current health

**Repository health: GOOD FOUNDATION / EARLY IMPLEMENTATION**

The codebase is deliberately small, understandable and aligned with the approved architecture. No heavyweight page builder or unnecessary plugin dependency is present. However, it is not production-ready: the homepage is still a starter composition, country routing is not wired, and the commercial/data/API layers do not yet exist.

## Highest-value next work

1. Build the real global homepage from the approved section contract.
2. Add country configuration and explicit AU/UK/US routing without hard-coded duplicated sites.
3. Build country homepage, category and detail templates/patterns.
4. Add trust/evidence/disclosure components.
5. Define the Rewards API client boundary and central affiliate CTA abstraction without embedding credentials or raw tracking URLs.
6. Add SEO/schema, accessibility and performance validation.
7. Add a plugin register and deployment/staging/recovery documentation.
8. Prove the AU vertical slice before broadening to UK and US.

## Governance

Do not add a heavyweight page builder. Do not move volatile rewards/affiliate intelligence into WordPress as the canonical store. Do not publish unverified commercial claims. Use the master contracts recorded in Overseer Issues #37–39 as the governing architecture.
