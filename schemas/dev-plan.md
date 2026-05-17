# Dev plan schema

Filename: `.ai/plans/NNN-<slug>.md`

```markdown
---
id: NNN
slug: <kebab-case>
status: draft|in-review|approved|executing|review|done|killed
tier: patch|feature|component|project
created: YYYY-MM-DD
updated: YYYY-MM-DD
depends_on: [<plan_ids>]
modules_touched:
  - <path>
current_phase: <int>
total_phases: <int>
brief: <relative path to brief>
---

## Context
<What background does an executor need to start?>

## Goal
<Restate the brief's What/Why in plan terms.>

## Success criteria
<Plan-level; aggregates phase-level acceptance.>

## Out of scope
<Restate from brief + anything else discovered during planning.>

## Phases

### Phase 1: <name>
- status: pending|active|done
- files_allowed:
  - <path or glob>
- acceptance:
  - <testable criterion>
- validation:
  - <command or check>

### Phase 2: ...

## Risks
<Including overlaps detected with other active plans.>

## Open questions

## Links
```
