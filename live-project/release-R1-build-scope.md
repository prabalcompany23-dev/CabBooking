# Release R1 — build scope (Lifecycle L2)

**Product:** Playo · **Feature:** Book-a-Ride (manual / concierge pilot)  
**Not in this build:** **Release R2** (FR-201+, ride-partner API, in-app payment, live tracking)

Glossary → [LIFECYCLE-AND-RELEASES.md](./LIFECYCLE-AND-RELEASES.md)

## Release R1 (what L2 implements)

Manual pilot: in-app capture + ops queue + logging + venue cancel/reschedule sync. Ops fulfils via vendor + **WhatsApp**; user pays **driver** (cash/UPI). One pilot city + sport (config).

| FRD | Summary |
|-----|---------|
| FR-101–102 | Ride prompt (pilot only); own-vehicle rule |
| FR-103–105 | Capture → ops queue; confirmation; phone validate & dedupe |
| FR-106–107 | Ops + WhatsApp (ops-led) |
| FR-108 | Log requests/outcomes; weekly summary |
| FR-109–110 | Venue cancel/reschedule → queue flags |

Backlog: [backlog.md](./04-requirements/other/backlog.md) · Word plan: [Project_Plan doc](./Project_Plan_Book-a-Ride_Phase1_Phase2.docx)

## Tech

**Fixed:** **http://localhost:8080**  
**Decide components first:** [TECH-COMPONENTS-TO-DECIDE.md](./06-development/TECH-COMPONENTS-TO-DECIDE.md) → then [ADR-0001](./06-development/adr/ADR-0001-release-r1-tech-stack-localhost.md)

---

## Minimum implementation — Lifecycle L2 **round 1** (pick this first)

Smallest demo that proves the **E2E skeleton** on localhost:8080. Ops can still use WhatsApp outside the app.

| Order | Deliverable | Stories / FR | Notes |
|-------|-------------|--------------|--------|
| 1 | App shell + SQLite + pilot config (city, sport) | — | ADR-0001 accepted |
| 2 | **Simulated venue booking** (stub page) | — | Generates `venue_booking_id` |
| 3 | **Ride CTA** after booking (one button + optional “No thanks”) | US-101 | FR-101–102; gate pilot city/sport |
| 4 | **Capture form** → save **ops queue** row | US-101 | FR-103; name, contact, game time, pickup |
| 5 | **Confirmation screen** (manual pilot copy) | US-102, US-105 | FR-104–105; no payment UI |
| 6 | **`/ops` queue list** + status `NEW` | US-104 (partial) | FR-108 log create |
| 7 | Ops: mark **WhatsApp sent** / **Fulfilled** / **Declined** | US-103, US-104 | FR-106–107 process; no WhatsApp API |

**Explicitly defer to L2 round 2 (still Release R1):**

- US-106 venue cancel/reschedule sync (FR-109–110)
- Phone validation, dedupe, &lt;30 min urgent flag (edge cases)
- Weekly summary report page (FR-108 full)
- Ops SLA alerts

**Out of scope until Release R2:** US-201+, fare API, in-app pay, tracking.

### Round 1 definition of done

- User can complete: book (stub) → CTA → form → confirmation.
- Ops can see request on `/ops` and update status.
- All steps on **localhost:8080**.

### Word plan alignment

Maps to **Rollout R1 weeks 2–3** subset (vertical slice before full FR-108/109/110).
