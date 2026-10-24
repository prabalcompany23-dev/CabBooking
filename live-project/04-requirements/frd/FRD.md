# FRD — Playo Book-a-Ride

**Source of truth:** [../../FRD_Book-a-Ride_Phase1_Phase2 (1).docx](../../FRD_Book-a-Ride_Phase1_Phase2%20(1).docx)  
**Stories:** [epic-feature-user story.docx](../../epic-feature-user%20story.docx)  
**L2 build (R1):** [release-R1-build-scope.md](../../release-R1-build-scope.md)

## Phase 1 functional requirements (in build)

| ID | Feature area | Requirement (short) | Story |
|----|--------------|---------------------|-------|
| FR-101 | Ride prompt | “Need help getting there?” after venue confirm; pilot city/sport only | US-101 |
| FR-102 | Ride prompt | Skip or adjust if “Own vehicle” | US-101 |
| FR-103 | Request capture | Yes → name, contact, game time, pickup area → ops queue | US-101 |
| FR-104 | Confirmation | User sees manual-process confirmation + time window | US-102 |
| FR-105 | Confirmation | Validate phone; dedupe same-game requests | US-102 |
| FR-106 | Manual booking | Ops books vendor; WhatsApp driver details ≥30 min before pickup | US-103 |
| FR-107 | Manual booking | WhatsApp states fare + pay driver directly | US-103, US-105 |
| FR-108 | Pilot logging | Log accept/decline + outcome; weekly summary | US-104 |
| FR-109 | Cancellation sync | Venue cancel → ride request cancelled in ops queue | US-106 |
| FR-110 | Reschedule sync | Venue reschedule → “needs re-confirmation”; notify user (WhatsApp) | US-106 |

**Phase 1 scope:** no automated booking, no in-app payment (see US-105).

## Release R2 (not in current L2 build)

FR-201 – FR-212 — automated partner flow; see Word FRD.

## Non-functional (both phases)

Graceful failures (no blank/stuck UI); traceability to venue booking; no charge without confirmed booking (Phase 2 payment rules).
