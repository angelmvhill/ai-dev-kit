# Dev plan schema

Filename: `.ai/plans/NNN-<slug>.plan.md`

```markdown
---
id: NNN
slug: <kebab-case>
version: 0.1.0
status: draft|in-review|approved|done|killed
tier: patch|feature|component|project
created: YYYY-MM-DD
updated: YYYY-MM-DD
depends_on: [<plan_ids>]
modules_touched:
  - <path>
current_phase: <int>
total_phases: <int>
brief: <relative path to brief, e.g. ../briefs/NNN-<slug>.brief.md>
codebase_map: <relative path to codebase map, or null>
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
- status: pending|active|done|integrated
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
