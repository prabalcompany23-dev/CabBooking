# Tech components to decide (before final stack)

**Goal:** List every **component** that needs a technology choice for **Lifecycle L2 · Release R1**.  
**Fixed already:** serve on **`http://localhost:8080`** (host/port). **Budget $0:** OSS tools only; no paid APIs in R1.  
**Next step:** R1-R1 decisions complete → [ADR-0001](./adr/ADR-0001-release-r1-tech-stack-localhost.md) accepted · app in `app/`.

**Scope keys:** **R1-R1** = L2 round 1 min slice · **R1-R2** = later R1 · **R2** = Release R2 (ignore for now)

---

## A. Application structure

| # | Component | What it does (R1) | Scope | Options to consider | Decision |
|---|-----------|-------------------|-------|---------------------|----------|
| A1 | **Deployment unit** | One runnable app for demo | R1-R1 | Single monolith · User app + Ops app (2 processes) | **Single monolith @ :8080** |
| A2 | **User-facing UI** | Stub venue book, prompt, form, confirmation (US-101–102, US-105) | R1-R1 | Server pages (Thymeleaf/EJS) · SPA (React/Vue) · Hybrid | **Server-rendered pages (Jinja2)** |
| A3 | **Ops-facing UI** | Queue list, status updates (US-103–104) | R1-R1 | Same app `/ops` · Separate admin app · Spreadsheet export only | **Same app `/ops`** |
| A4 | **API style** | Browser forms + optional JSON | R1-R1 | MVC only · REST `/api/*` + UI · REST only + separate SPA | **MVC only (form POST)** |

---

## B. Backend runtime

| # | Component | What it does (R1) | Scope | Options to consider | Decision |
|---|-----------|-------------------|-------|---------------------|----------|
| B1 | **Language / framework** | All business logic FR-101–110 | R1-R1 | Java Spring Boot 3 · Node Express · Python FastAPI · .NET | **Python FastAPI** |
| B2 | **Build tool** | Compile/package | R1-R1 | Maven · Gradle · npm/pnpm · uv/poetry | **uv + pyproject.toml** |
| B3 | **Config / pilot gating** | Pilot city + sport (FR-101) | R1-R1 | `application.yml` · `.env` · DB-driven config table | **`.env` / env vars** |

---

## C. Data & persistence

| # | Component | What it does (R1) | Scope | Options to consider | Decision |
|---|-----------|-------------------|-------|---------------------|----------|
| C1 | **Database engine** | Store bookings, ride requests, logs (FR-108) | R1-R1 | H2 file · SQLite · PostgreSQL · MySQL | **SQLite file** |
| C2 | **Data access** | CRUD, queries for weekly report | R1-R1 | JPA/Hibernate · Spring JDBC · Prisma · raw SQL | **SQLAlchemy ORM** |
| C3 | **Schema / migrations** | `venue_bookings`, `ride_requests`, status enum | R1-R1 | Flyway/Liquibase · manual SQL · JPA auto-ddl (dev only) | **Alembic** |
| C4 | **Audit / event log** | Request created, declined, fulfilled (US-104) | R1-R2 | Same table + status history · Separate audit table | _TBD_ |

---

## D. Domain integrations (R1)

| # | Component | What it does (R1) | Scope | Options to consider | Decision |
|---|-----------|-------------------|-------|---------------------|----------|
| D1 | **Playo venue booking** | Trigger ride prompt after book | R1-R1 | In-app **stub** only · Mock REST client · Future real API (defer) | **In-app stub form** |
| D2 | **“Own vehicle” flag** | Suppress prompt (FR-102) | R1-R1 | Field on stub booking form · Hardcoded false for demo | **Checkbox on stub form** |
| D3 | **WhatsApp (US-103)** | Driver details to user | R1-R1 | **Manual** (ops phone) + app marks “sent” · WhatsApp Business API (overkill) | **Manual + status in app** |
| D4 | **SMS / call fallback** | Edge case US-103 | R1-R2 | Defer · Twilio/etc. | _TBD_ |
| D5 | **Venue cancel/reschedule** | Sync ride request (FR-109–110) | R1-R2 | In-app buttons on stub booking · Domain events · Mock webhook | _TBD_ |

---

## E. Cross-cutting (R1)

| # | Component | What it does (R1) | Scope | Options to consider | Decision |
|---|-----------|-------------------|-------|---------------------|----------|
| E1 | **Authentication** | Protect `/ops` | R1-R1 | None (local demo) · HTTP basic · Simple login session | **Simple login session** |
| E2 | **Phone validation** | FR-105, India numbers | R1-R2 | libphonenumber · Regex · Defer to round 2 | _TBD_ |
| E3 | **Dedupe / idempotency** | Same game double submit (US-102) | R1-R2 | Unique constraint · Token · Defer | _TBD_ |
| E4 | **Reporting (weekly)** | FR-108 full | R1-R2 | SQL + HTML page · CSV download · Excel | _TBD_ |
| E5 | **Logging / errors** | NFR graceful failures | R1-R1 | Framework default · Structured JSON logs | **Framework default** |
| E6 | **Testing** | Regression on flows | R1-R1 | Unit + few integration tests · Manual only for round 1 | **pytest (few tests)** |

---

## F. Release R2 only (do not decide now)

| Component | Notes |
|-----------|--------|
| Ride-partner API client | FR-201+ |
| Payment gateway | FR-205+ |
| Live tracking / maps | FR-209+ |
| In-app rating storage | FR-211 |

---

## Suggested decision order (for workshop)

1. **A1, B1, C1** — monolith vs split, backend, database (drives everything)  
2. **A2, A3, A4** — how user + ops interact with backend  
3. **D1, D3** — stub booking + manual WhatsApp (likely fixed for R1-R1)  
4. **E1** — ops auth for localhost demo  
5. **C3** — schema/migrations before first code  
6. Defer **D5, E2, E3, E4** to **R1-R2**

---

## Map components → min round 1 deliverables

| Round 1 deliverable | Components involved |
|--------------------|---------------------|
| App shell + config | A1, B1–B3, C1–C3, E5 |
| Stub venue booking | D1, D2 |
| Ride prompt + capture + confirm | A2, A4, B1, C1–C2 |
| Ops queue | A3, C1–C2, E1, D3 (status only) |

When **Decision** column is filled for all **R1-R1** rows, finalize ADR-0001 or replace with per-layer ADRs (0001 app, 0002 data, 0003 integrations).
