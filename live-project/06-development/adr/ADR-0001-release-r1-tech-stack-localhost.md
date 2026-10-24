# ADR-0001: Release R1 tech stack & localhost:8080



- **Status:** Accepted

- **Date:** 2026-09-27

- **Type:** Technical · Design

- **Related:** Lifecycle **L2** · Release **R1** · FR-101–110 · [release-R1-build-scope.md](../../release-R1-build-scope.md)



## Context



**L2** implements **Release R1** (manual pilot): user prompt/capture/confirmation, ops queue, logging; later rounds add cancel/sync and weekly reports. **Release R2** (automation) out of scope. Target: **`http://localhost:8080`**.



**Budget:** **$0** — open-source tools only; **no paid third-party APIs** in R1 (WhatsApp Cloud, maps, payment, ride partners). Fulfilment is manual ops + phone.



Component choices: [TECH-COMPONENTS-TO-DECIDE.md](../TECH-COMPONENTS-TO-DECIDE.md).



## Decision



| Layer | Choice |

|-------|--------|

| Runtime | Single monolith on **port 8080** |

| Backend | **Python FastAPI** |

| UI | **Jinja2** server pages + **`/ops`** queue |

| API style | MVC (form POST) |

| Database | **SQLite** (local file) |

| ORM / migrations | SQLAlchemy + Alembic |

| Tooling | **uv** + `pyproject.toml` |

| Config | `.env` (pilot city/sport, secrets) |

| WhatsApp | Manual ops (mark status in app; no Meta API in round 1) |

| Venue booking | In-app stub form |



## Consequences



- Round 1 vertical slice per [release-R1-build-scope.md](../../release-R1-build-scope.md).

- Data model in [ADR-0002](./ADR-0002-data-model-r1.md).

- Code lives under `06-development/app/`.



## Notes



No cloud hosting in R1; localhost demo only.

