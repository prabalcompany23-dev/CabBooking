# ADR-0002: Release R1 round 1 data model



- **Status:** Accepted

- **Date:** 2026-09-27

- **Type:** Technical

- **Related:** ADR-0001 · FR-103, FR-108 (partial) · US-101–104



## Context



L2 round 1 needs persistent stub venue bookings, ride requests for the ops queue, and a demo ops user. Audit history (C4) deferred to R1-R2.



## Decision



### `venue_bookings`



| Column | Type | Notes |

|--------|------|--------|

| id | integer PK | |

| player_name | string | |

| contact | string | Phone or email (minimal validation in R1) |

| city | string | Pilot gating (FR-101) |

| sport | string | Pilot gating |

| venue_name | string | |

| game_starts_at | datetime | |

| own_vehicle | boolean | FR-102 — suppress ride CTA when true |

| created_at | datetime | |



### `ride_requests`



| Column | Type | Notes |

|--------|------|--------|

| id | integer PK | |

| venue_booking_id | FK → venue_bookings | |

| pickup_area | string | FR-103 |

| status | enum | `NEW`, `WHATSAPP_SENT`, `FULFILLED`, `DECLINED` |

| ops_notes | string nullable | Optional driver/vendor notes for ops |

| created_at | datetime | |

| updated_at | datetime | |



Player name/contact/game time come from the linked booking (no duplicate columns in R1).



### `ops_users`



| Column | Type | Notes |

|--------|------|--------|

| id | integer PK | |

| username | string unique | |

| password_hash | string | bcrypt; seed from `.env` on first startup if empty |



## Consequences



- Alembic initial revision creates these tables.

- Status updates overwrite `ride_requests.status`; no separate audit table in round 1.



## Options not chosen



- Separate audit/event table — deferred (C4).

- Denormalized player fields on `ride_requests` — avoided for round 1 simplicity.

