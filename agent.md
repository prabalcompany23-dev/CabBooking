# Agent guide

**Repo:** Track A `study-plan/` + Track B **Playo Book-a-Ride** `live-project/`  
**Naming:** [LIFECYCLE-AND-RELEASES.md](./live-project/LIFECYCLE-AND-RELEASES.md) — never bare “Phase 1” (means career doc, L1 BA, or Word rollout).

## Two tracks

| Track | Purpose | Main files |
|-------|---------|------------|
| **A — Career program** | Learning, courses, CV | [study-plan/](./study-plan/), [Phase-1.docx](./Phase-1.docx) |
| **B — Playo Book-a-Ride** | L1 BA + L2 implementation | [LIVE-PROJECT.md](./LIVE-PROJECT.md), [live-project/](./live-project/) |

## Map

| Path | Track | Role |
|------|-------|------|
| study-plan/ | A | Study plan |
| Phase-1.docx | A | Frozen competency matrix |
| live-project/LIFECYCLE-AND-RELEASES.md | B | L1/L2 vs Release R1/R2 |
| live-project/release-R1-build-scope.md | B | L2 build scope + **min round 1** |
| live-project/01–05 | B | **Lifecycle L1** (BA) |
| live-project/06-development | B | **Lifecycle L2** (code, localhost:8080) |
| REQUIREMENTS-DOCS.md + Word docx | B | Authoritative reqs |

## Agent rules

1. Do not reword Phase-1.docx §3 matrix unless asked.
2. **L1** = analysis artifacts only. **L2** = `06-development/`. Build **Release R1** only until go/no-go; **Release R2** = spec only.
3. Min first implementation → release-R1-build-scope.md **round 1** table.
4. Playo business decisions → ba-techniques workbook. Technical → ADR-LOG.
5. Commits only when user asks.

## State

- **L1:** Word + md requirements in place (draft).
- **L2:** Not started; ADR-0001 Proposed.
- **First code slice:** round 1 in release-R1-build-scope.md.
