# Affiliate Websites — Architecture

## Purpose

Reusable master WordPress framework for country-specific affiliate/rewards websites serving Australia, the United Kingdom and the United States.

## System boundary

```text
Visitor
  ↓
Cloudflare CDN / WAF
  ↓
WordPress Block Theme
  ↓
Rewards API
  ↓
PostgreSQL / Supabase

AgentOS
  ├─ research
  ├─ verification
  ├─ monitoring
  └─ orchestration
```

## Responsibilities

### WordPress

Presentation, editorial content, SEO acquisition, templates, navigation and reusable UI.

### Rewards API

Controlled boundary for structured reward/program/merchant data, commercial resolution and approved frontend queries.

### PostgreSQL / Supabase

Canonical structured intelligence store. WordPress must not become the authoritative store for volatile commercial intelligence.

### AgentOS

Research, verification, monitoring, content workflows and controlled orchestration. Production writes must follow governed API/staging/verification paths.

### Cloudflare

CDN, WAF and edge delivery.

## Country model

```text
www.domain
├── au.domain
├── uk.domain
└── us.domain
```

Country implementations share the master theme/framework while maintaining independent local content, commercial relationships, SEO priorities and compliance requirements.

## Data integrity

Commercial claims retain source, source type, verification date, verification status, confidence and freshness/effective date where relevant. Conflicts are preserved and surfaced rather than silently overwritten.

## Affiliate resolution

```text
visitor
 → country
 → program/product/merchant
 → country eligibility
 → current approved commercial relationship
 → destination
 → tracked outbound click
```

Raw tracking URLs should remain outside editorial content.

## Security boundary

Browser clients must not receive broad internal database credentials. Supabase service-role credentials and other secrets remain server-side. Use least privilege, RLS where appropriate, staging/production separation, backups and controlled deployment.

## Initial WordPress strategy

Use a custom lightweight Block Theme:

```text
wp-content/themes/affiliate-master/
├── theme.json
├── templates/
├── parts/
├── patterns/
└── assets/
```

Avoid a heavyweight page builder as a foundational dependency.

## Implementation principle

Build a vertical slice before expanding breadth. Prove global routing, one country, one category, comparison/guide/detail flow and commercial CTA before implementing the full catalogue.
