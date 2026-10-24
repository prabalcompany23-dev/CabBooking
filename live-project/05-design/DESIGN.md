# Design — Lifecycle L1 (Release R1 scope)

**FRD:** FR-101 – FR-110 · **Word wireframes:** [epic-feature-user story.docx](../epic-feature-user%20story.docx)

## In-app (engineering)

| Flow | Notes |
|------|--------|
| Venue book (stub) | Full form (name + contact) or **Continue as guest** (`/guest`) — mobile + venue fields; stored as `Guest · XXXX` |
| Post-booking ride CTA | One button **Request cab to venue** (+ optional “No thanks”); pilot city/sport gate; own-vehicle rule |
| Request capture | Fields: name, contact, game time, pickup area |
| Request confirmation | Manual pilot messaging; SLA window (e.g. 2 hours) |
| Ops queue | View/update requests (may be admin tool or export — TBD in ADR) |

## Out of app (Phase 1)

Ops manual vendor booking; WhatsApp to user (US-103); payment to driver only.

## Not building (Release R2)

Fare estimate card, ride options, in-app payment, live map tracking, in-app rating — see Word FRD Phase 2.

## Process

AS-IS / TO-BE and gaps → [BA workbook](../ba-techniques/BA-ANALYSIS-DECISIONS-AND-GAPS.md)

## Technical decisions

→ [ADR-LOG.md](../06-development/ADR-LOG.md) when stack/queue/reporting are chosen.
