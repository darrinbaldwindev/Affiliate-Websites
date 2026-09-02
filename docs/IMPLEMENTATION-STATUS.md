# Affiliate Websites — Implementation Status

**Checkpoint:** 2026-09-03

## Repository

`darrinbaldwindev/Affiliate-Websites` is now the canonical application/source repository for the Affiliate Websites project. `darrinbaldwindev/Overseer` remains the control and governance repository.

## Scan result

The repository is an intentionally minimal WordPress Block Theme foundation. The README and architecture documents establish the intended WordPress → Rewards API → PostgreSQL/Supabase boundary, country model and verification-first commercial architecture.

Current theme assets include:

- `style.css`
- `theme.json`
- `functions.php`
- `templates/home.html`
- `templates/page.html`
- `parts/header.html`
- `parts/footer.html`

## Completed in this checkpoint

- Added minimal WordPress theme bootstrap in `functions.php`.
- Established reusable design tokens in `theme.json`.
- Added global homepage starter template.
- Added reusable page template.
- Added header and footer template parts.

## Still required

1. Proper global homepage composition and country-routing controls.
2. Country configuration model for AU/UK/US.
3. Country homepage template.
4. Category/program/product/merchant/comparison templates and patterns.
5. Trust, evidence and disclosure components.
6. Rewards API integration boundary.
7. Central affiliate resolver/click abstraction.
8. SEO/schema foundations and validation.
9. Accessibility/performance/security test harness.
10. Plugin register and deployment/staging documentation.
11. AU vertical slice validation before UK/US expansion.

## Governance

Do not add a heavyweight page builder. Do not move volatile rewards/affiliate intelligence into WordPress as the canonical store. Do not publish unverified commercial claims. Use the master contracts recorded in Overseer Issues #37–39 as the governing architecture.
