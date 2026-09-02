# WordPress Plugin Register

Status: Master implementation contract v0.1

The master site should remain lightweight. Plugins are capabilities with a defined role, not dependencies to add by default.

## Required/expected capability areas

| Capability | Preferred approach | Rule |
|---|---|---|
| Block editing | Native Gutenberg / Site Editor | Core-first; no heavyweight page builder |
| SEO | One established SEO plugin if required | Avoid overlapping SEO plugins |
| Caching/performance | Hosting/CDN + one cache layer | Avoid duplicate page/object cache systems |
| Image optimisation | CDN/WordPress-native where sufficient | Do not add multiple optimisers |
| Forms | Minimal, accessibility-tested form plugin if needed | Only where a form is actually required |
| Analytics/measurement | Consent-aware implementation | Non-essential tracking must respect applicable consent requirements |
| Security | Hosting/WAF + one complementary security layer where needed | Avoid redundant scanners/firewalls |

## Hard rules

1. No plugin may become the canonical rewards database.
2. No plugin may store affiliate credentials in page content.
3. Plugin selection must be documented before production adoption.
4. Prefer WordPress core features when they meet requirements.
5. Every plugin must have a maintenance/security rationale and an owner.
6. Remove unused plugins rather than accumulating optional dependencies.

## Deployment baseline

Cloudflare handles edge/CDN/WAF responsibilities. WordPress handles presentation and editorial content. Rewards API/PostgreSQL handles structured intelligence. AgentOS handles research, verification and orchestration.
