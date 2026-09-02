# Implementation Status

**Last updated:** 2026-09-03

## Completed in application repository

- Repository contract and architecture documentation
- Master UX/global homepage specification
- Master Affiliate lightweight WordPress Block Theme scaffold
- Initial `theme.json` design tokens and semantic colour roles
- Theme bootstrap in `functions.php`
- Global header and footer shells
- Global homepage template shell
- Reusable country selector pattern with fake example domains removed
- Reusable Earn / Save / Compare pattern
- Reusable Trust / Methodology pattern
- Reusable Affiliate Disclosure pattern
- Country configuration contract
- Rewards API boundary contract
- Lightweight WordPress plugin register
- Initial GitHub Actions theme validation workflow

## In progress

- Country routing/configuration implementation
- AU country shell
- Category/detail template system
- Trust/evidence UI integration
- Rewards API client interface
- Central affiliate resolution/tracking abstraction
- SEO/schema, accessibility and performance verification

## Not yet verified

A live WordPress installation has not yet been connected to this repository, so browser-level rendering, WordPress Site Editor compatibility, Core Web Vitals, accessibility audits and end-to-end affiliate tracking remain unverified.

No live affiliate programs, commissions, prices or other volatile commercial facts have been invented or embedded as factual data.

## Next acceptance gate

Demonstrate:

`Global homepage → country selector → AU → category → guide/comparison → detail → commercial CTA`

with the same theme architecture capable of subsequently serving UK and US.
