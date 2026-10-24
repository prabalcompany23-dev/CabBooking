# Lifecycle vs releases (naming)

Avoid bare **“Phase 1”** — it means three different things.

| Term | Meaning |
|------|---------|
| **Career program** | BA learning · [Phase-1.docx](../Phase-1.docx) · [study-plan/](../study-plan/) |
| **Lifecycle L1 — Business analysis** | Folders `01`–`05`, Word/md requirements · **no app code** |
| **Lifecycle L2 — Implementation** | `06-development/` · ADR · **localhost:8080** |
| **Release R1 — Manual pilot** | Word “Phase 1” rollout · FR-101–110 · US-101–106 |
| **Release R2 — Automated MVP** | Word “Phase 2” rollout · FR-201+ · **after** R1 go/no-go |

## When product development starts

| Source | When |
|--------|------|
| **Word project plan** | Engineering **Rollout R1 week 2** (FR-101–105), week 3 (FR-106–110) |
| **This repo** | Code in **`06-development/`** when you enter **Lifecycle L2**, building **Release R1** scope |

## Folders

| Folder | Lifecycle |
|--------|-----------|
| `01-idea` … `05-design` | L1 |
| `06-development` | L2 |
| `07-analytics` | L1 metrics design · L2 when data exists |

## Build scope doc

[release-R1-build-scope.md](./release-R1-build-scope.md) · **Minimum L2 round 1** at bottom of that file.
