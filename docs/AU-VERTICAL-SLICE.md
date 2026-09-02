# AU Vertical Slice — Implementation Contract

## Status

Foundation implementation on branch `feat/au-vertical-slice-foundation`.

## Acceptance path

`Global homepage → AU country shell → category → guide/comparison → detail → commercial CTA`

## Current scope

- Global homepage implemented as a native WordPress block template.
- AU country shell implemented as `page-au.html`.
- Country navigation remains compatible with the shared master theme.
- Commercial destinations are intentionally not hard-coded into editorial templates.

## Data boundary

AU commercial records must eventually arrive through the controlled rewards/API layer. WordPress templates must not become the authoritative store for volatile programme, merchant, offer or affiliate relationship data.

## Evidence requirements

Before an AU commercial record is published, retain source, source type, verification date/status, confidence and freshness/effective date where relevant. Conflicts remain visible to the governed workflow rather than being silently overwritten.

## Next vertical-slice stages

1. AU category template and fixture.
2. AU guide/comparison template and fixture.
3. AU detail template and evidence block.
4. Central commercial-resolution interface.
5. Outbound click event contract.
6. Accessibility/performance checks.
7. Browser/WordPress verification before merge.
