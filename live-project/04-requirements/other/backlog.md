# Backlog — Phase 1 (Epic → Feature → Story)

**Source:** [epic-feature-user story.docx](../../epic-feature-user%20story.docx) · **Wireframes:** in Word under each story.

## Epic E1 — Validate Ride Demand Through a Manual Pilot

*As Playo, test ride interest after venue booking via manual process before full integration.*

| Feature | Stories | FRD |
|---------|---------|-----|
| **F1.1** Capture ride interest post-booking | US-101 | FR-101–103 |
| **F1.2** Manual ride coordination | US-102, US-103 | FR-104–107 |
| **F1.3** Pilot measurement | US-104 | FR-108 |
| **F1.4** Payment (cash/UPI to driver — no in-app pay) | US-105 | FR-107 |
| **F1.5** Cancellation & rescheduling | US-106 | FR-109–110 |

---

### US-101 — Ask if the user needs a ride after booking

**As** user who just booked a venue **I want** a ride prompt **so that** I don’t search elsewhere.

**AC:** Prompt after venue confirm (“Need help getting there?” Yes/No); **pilot city + sport only**; Yes → capture name, contact, game time, pickup area → **ops queue**; No → normal completion.

**Edge:** Own vehicle → no prompt (or note); outside pilot → no prompt; abandon before capture → not complete; &lt;30 min to game → **flag urgent/late**.

**UI (Word):** Post-booking ride prompt.

---

### US-102 — Confirm the request was received

**AC:** Confirmation screen; team will reach out within window (e.g. 2 h); states **manual pilot** not instant book.

**Edge:** Ops SLA breach → internal alert; invalid phone → fail before queue; duplicate submit → dedupe one ticket.

**UI:** Request received confirmation.

---

### US-103 — Receive ride details via WhatsApp *(ops-led)*

**AC:** Ops books vendor; WhatsApp with driver name, vehicle, pickup time **≥30 min before pickup**; fare + pay driver stated.

**Edge:** No WhatsApp → SMS/call fallback; no driver → notify early; driver cancel → rebook + re-notify.

**Not in-app booking confirm in P1** — WhatsApp is the user’s “confirmed” moment.

---

### US-104 — Track pilot demand internally

**AC:** Log every request (accept/decline) with game time, pickup area, **outcome**; **weekly summary** (volume + fulfilment) for go/no-go.

**Edge:** Ops must close-out outcome; multi-game same user = separate rows; user cancel = distinct status.

**Build:** Logging + report (FR-108); ops close-out UI.

---

### US-105 — Know how and when I’ll pay

**AC:** No Playo payment in P1; WhatsApp + copy state fare **estimate**, pay driver cash/UPI at ride end.

**Edge:** Explicit “not in app” messaging; fare disputes = known P1 limitation.

**Build:** Copy on US-102 screen + WhatsApp template (not payment gateway).

---

### US-106 — Cancel/reschedule ride when game changes

**AC:** Venue **cancel** → ride request **cancelled** in ops queue; **reschedule** → **needs re-confirmation**; ops alerted if vendor already booked; user **WhatsApp** on cancel/re-arrange.

**Edge:** Cancel after driver en route → urgent path; reconfirm new time explicitly; outside pilot after reschedule → cancel ride.

**Build:** Link `venue_booking_id` → ride request; event handler (FR-109–110).

---

## E2E Phase 1

`Venue booked → US-101 → US-102 → (US-105 messaging) → US-103 WhatsApp`

## Out of backlog (Release R2)

Epic *Automate Single-Rider Ride Booking*, US-201+, FR-201+ — see Word doc.
