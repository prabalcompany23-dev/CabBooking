# BA analysis, gaps, decisions & validation

> **Status:** Placeholder — fill as you work through the live project.  
> **Phase-1 tie-in:** Business Analysis Core (Area 4): gap analysis, root cause analysis, AS-IS/TO-BE, process mapping, MoSCoW, prioritization, impact analysis, change management, validation.  
> **Related artifacts:** [Design / AS-IS·TO-BE](../05-design/DESIGN.md) · [BRD](../04-requirements/brd/BRD.md) · [FRD](../04-requirements/frd/FRD.md) · [Traceability](../04-requirements/other/traceability-matrix.md)

Use this workbook across **Idea → Requirements → Design**. Export decision maps and process diagrams to [../artifacts/](../artifacts/) (e.g. Miro).

---

## 1. Business problem statement

_TBD_

| Element | Notes |
|---------|--------|
| **Current pain** | _TBD_ |
| **Who is affected** | _TBD_ |
| **Business impact** | _TBD_ |
| **Desired outcome** | _TBD_ |

---

## 2. Stakeholder analysis

| Stakeholder | Role | Interest | Influence | Engagement approach |
|-------------|------|----------|-----------|---------------------|
| _TBD_ | _TBD_ | _TBD_ | High / Med / Low | _TBD_ |

### RACI (key decisions / deliverables)

| Activity / deliverable | R | A | C | I |
|------------------------|---|---|---|---|
| _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

---

## 3. Elicitation log

| Date | Technique | Participants | Topic | Key findings | Follow-up |
|------|-----------|--------------|-------|--------------|-----------|
| _TBD_ | Interview / workshop / survey | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

---

## 4. Root cause analysis

### 4.1 Problem symptom (what we see)

_TBD_

### 4.2 Five Whys

| # | Why? | Answer |
|---|------|--------|
| 1 | Why does the problem occur? | _TBD_ |
| 2 | Why? | _TBD_ |
| 3 | Why? | _TBD_ |
| 4 | Why? | _TBD_ |
| 5 | Why? | _TBD_ |

**Probable root cause:** _TBD_

### 4.3 Fishbone (Ishikawa) — optional

| Category | Causes |
|----------|--------|
| People | _TBD_ |
| Process | _TBD_ |
| Technology | _TBD_ |
| Data | _TBD_ |
| Environment / policy | _TBD_ |

---

## 5. AS-IS → TO-BE summary

_Detail in [DESIGN.md](../05-design/DESIGN.md); summarize gaps here._

| Dimension | AS-IS (current) | TO-BE (target) |
|-----------|-----------------|----------------|
| Process | _TBD_ | _TBD_ |
| People / roles | _TBD_ | _TBD_ |
| Systems / tools | _TBD_ | _TBD_ |
| Data | _TBD_ | _TBD_ |
| Policy / rules | _TBD_ | _TBD_ |

---

## 6. Gap analysis

| Gap ID | Area | AS-IS | TO-BE | Gap description | Severity | Proposed response | Req / story ref |
|--------|------|-------|-------|-----------------|----------|-------------------|-----------------|
| GAP-001 | _TBD_ | _TBD_ | _TBD_ | _TBD_ | High / Med / Low | _TBD_ | _TBD_ |

**Summary:** _TBD_

---

## 7. Decision map / decision log

Record significant choices (solution options, scope, prioritization trade-offs).

### 7.1 Decision tree (text sketch)

```
Decision: _TBD_
├── Option A: _TBD_
│   ├── Pro: _TBD_
│   └── Con: _TBD_
└── Option B: _TBD_
    ├── Pro: _TBD_
    └── Con: _TBD_
```

_Mirror in Miro as a visual decision map when useful._

### 7.2 Decision register

| ID | Decision | Options considered | Criteria | Outcome | Date | Decider | Rationale |
|----|----------|-------------------|----------|---------|------|---------|-----------|
| DEC-001 | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

---

## 8. Prioritization (MoSCoW)

| ID | Item (requirement / epic / story) | MoSCoW | Rationale | Dependencies |
|----|-----------------------------------|--------|-----------|--------------|
| _TBD_ | _TBD_ | Must / Should / Could / Won't | _TBD_ | _TBD_ |

### Other prioritization (optional)

| Technique | When used | Result |
|-----------|-----------|--------|
| Value vs effort | _TBD_ | _TBD_ |
| Risk-based | _TBD_ | _TBD_ |
| Kano (if applicable) | _TBD_ | _TBD_ |

---

## 9. Assumptions, constraints & unknowns

| ID | Type | Statement | Owner | Validated? |
|----|------|-----------|-------|------------|
| ASM-001 | Assumption | _TBD_ | _TBD_ | ⬜ |
| CON-001 | Constraint | _TBD_ | _TBD_ | ⬜ |
| UNK-001 | Unknown | _TBD_ | _TBD_ | ⬜ |

---

## 10. Risk register

| Risk ID | Description | Cause | Impact | Likelihood | Mitigation | Owner |
|---------|-------------|-------|--------|------------|------------|-------|
| R-001 | _TBD_ | _TBD_ | _TBD_ | H/M/L | _TBD_ | _TBD_ |

---

## 11. Impact analysis (change)

_Use when scope, process, or systems change after baseline requirements._

| Change | Affected stakeholders | Processes | Systems | Data | Requirements impacted | Effort / risk |
|--------|----------------------|-----------|---------|------|----------------------|---------------|
| _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

---

## 12. Change management notes

| Change request | Reason | Approved? | Docs updated | Communication |
|----------------|--------|-----------|--------------|---------------|
| _TBD_ | _TBD_ | ⬜ | BRD / FRD / backlog | _TBD_ |

---

## 13. Validation & “what could go wrong” (error guessing)

Structured thinking about failures, edge cases, and bad data—**before** build and test. Feeds acceptance criteria and NFRs.

### 13.1 Validation checklist

| Check | Question | Result | Evidence |
|-------|----------|--------|----------|
| Completeness | Are all Must-haves traced to stories/AC? | ⬜ | _TBD_ |
| Consistency | Do BRD, FRD, and design conflict? | ⬜ | _TBD_ |
| Feasibility | Can we deliver within constraints? | ⬜ | _TBD_ |
| Stakeholder sign-off | Who approved what? | ⬜ | _TBD_ |

### 13.2 Error guessing / failure modes (BA lens)

| Scenario | What might go wrong | Likely cause | Impact | Mitigation / requirement |
|----------|---------------------|--------------|--------|---------------------------|
| Happy path breaks | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Bad or missing data | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| User misuse / edge case | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Integration failure | _TBD_ | _TBD_ | _TBD_ | _TBD_ |
| Security / access | _TBD_ | _TBD_ | _TBD_ | _TBD_ |

_Link outcomes to [FRD](../04-requirements/frd/FRD.md) NFRs and story acceptance criteria._

---

## 14. Traceability snapshot

| Business need | Gap | Decision | Requirement | Story | AC |
|---------------|-----|----------|-------------|-------|-----|
| _TBD_ | GAP-___ | DEC-___ | BR-/FR-___ | US-___ | _TBD_ |

_Full matrix: [traceability-matrix.md](../04-requirements/other/traceability-matrix.md)_

---

## 15. Workshop & diagram index

| Diagram | Tool | File in artifacts | Version |
|---------|------|-------------------|---------|
| Process map (BPMN-light) | Miro | _TBD_ | _TBD_ |
| Decision map | Miro | _TBD_ | _TBD_ |
| User journey | Miro | _TBD_ | _TBD_ |
