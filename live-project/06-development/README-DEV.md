# Run locally (Book-a-Ride R1 round 1)



**Target URL:** `http://localhost:8080`  

**ADR:** [ADR-0001](./adr/ADR-0001-release-r1-tech-stack-localhost.md) (Accepted) · [ADR-0002](./adr/ADR-0002-data-model-r1.md)  

**Scope:** [release-R1-build-scope.md](../release-R1-build-scope.md) — L2 round 1



## Prerequisites



- Python **3.11+**

- [uv](https://docs.astral.sh/uv/)



## Setup



From `live-project/06-development/`:



```bash

cp .env.example .env

uv sync

uv run alembic upgrade head

```



Edit `.env` if you change pilot city/sport or ops password.



## Start



```bash

uv run uvicorn app.main:app --host 127.0.0.1 --port 8080 --reload

```



Open `http://localhost:8080`.



## Routes



| Path | Purpose |

|------|---------|

| `/` | Stub venue booking (name + contact) |
| `/guest` | Continue as guest (mobile + venue fields) |

| `/bookings/{id}` | Venue confirm + **Request cab to venue** CTA |

| `/bookings/{id}/ride/new` | Ride capture form |

| `/ride-requests/{id}/confirmed` | User confirmation (manual pilot copy) |

| `/ops/login` | Ops sign-in |

| `/ops/queue` | Ride request queue |

| `/ops/requests/{id}` | Status updates (WhatsApp sent / fulfilled / declined) |

| `/health` | Health check |



## Config (`.env`)



| Variable | Purpose |

|----------|---------|

| `DATABASE_URL` | SQLite path (default `./book_a_ride.db`) |

| `SECRET_KEY` | Session signing |

| `PILOT_CITY` / `PILOT_SPORT` | FR-101 gating |

| `OPS_USERNAME` / `OPS_PASSWORD` | Ops login (seeded on first run if user missing) |



## Tests



```bash

uv sync --group dev

uv run pytest

```



## Budget



$0 — OSS stack only; no WhatsApp Cloud or paid APIs in this build.


