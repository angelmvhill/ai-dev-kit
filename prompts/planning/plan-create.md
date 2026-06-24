<!--
id: planning/plan-create
version: 0.1.0
purpose: Produce an implementation-ready, phased dev plan for the active repo
inputs:
  - brief_path
  - brainstorm_path (optional)
  - codebase_map_path
outputs:
  - .ai/plans/<NNN>-<slug>.plan.md
-->

{{> _partials/preamble-orient }}

## Task
Write the dev plan as an **implementation-ready engineering document for this repo**, not a generic project outline. An implementation agent should be able to execute it phase by phase without inventing architecture.

## User must provide
- **brief_path**: path to the brief describing the work.
- **brainstorm_path** (optional): path to a brainstorm doc if one was produced.
- **codebase_map_path**: path to the latest `codebase-map-*.md` from `discovery/understand-codebase`. **Required.** If absent, stop and tell the user to run `discovery/understand-codebase` first.
- **followups_to_include** (optional): IDs from `.ai/FOLLOWUPS.md` to fold into this plan.

## AI must do
1. Read the brief, brainstorm (if any), codebase map, `PROJECT.md`, and `FOLLOWUPS.md`.
2. Start with **Context**: what this plan does and why it belongs in this repo now.
3. Define **Goals** and **Out of Scope** explicitly. Out of scope is non-negotiable scope discipline — write it.
4. Describe the **architecture** in terms of concrete modules, ownership boundaries, invariants, and testable contracts. Match the style of existing repo docs.
5. Break work into **numbered phases**. Each phase groups related changes (by file, class, or feature). For each phase, include:
   - **Problem being solved** and why it belongs in that module.
   - **File-level changes**: NEW vs MODIFY, with relative paths.
   - **Data model / API contract changes**: field names, types, semantics. Use typed dataclasses (slots=True for mutable, frozen=True for pure data).
   - **Ownership boundaries**: who owns state, normalization, I/O, orchestration, recovery, persistence. State owners do not perform I/O; normalizers are the single raw-data boundary; orchestration lives in engine/task layers.
   - **Invariants and failure behavior**: what must never happen silently, what raises, what logs, what marks stale, what rejects.
   - **Tests required**: happy path, boundary cases, malformed input, ordering/idempotency, regression coverage. Tests are deliverables; do not weaken assertions to fit the implementation.
   - **Acceptance criteria**: concrete enough to verify in code and tests. Each must be checkable as pass/fail.
   - **Scope lock**: the exact file list this phase may touch. Files shared with other phases note which behavior belongs here.
   - **Exact commit message** for the phase (one line, conventional-commit style if repo uses it).
6. Add a **Phase 0** if any prerequisite is needed (env, deps, scaffolding).
7. End with a **Risks & rollback** section: what could go wrong per phase, and how to back out.
8. Advance STATE: `status: PLAN_DRAFT`, `active_plan: <NNN-slug>`, `next_action: planning/plan-review`, `last_prompt: planning/plan-create`, `last_updated` (today).

## Code standards the plan must enforce
- Explicit and deterministic. No "refactor as needed" language.
- Preserve module boundaries. State owners do not perform I/O; normalizers are the single raw-data boundary.
- Typed dataclasses for schemas, `slots=True` default, frozen when pure data.
- Timestamps UTC-aware unless a local-time boundary is explicit and documented.
- No raw provider/exchange dicts past the normalization boundary.
- Fail loudly on invalid config or unknown runtime conditions when silent continuation would hide bugs.
- No new concurrency / worker pools / background tasks unless the phase explicitly requires it and ownership is clear.
- Small, explicit, testable interfaces.
- Match existing pytest style: focused unit tests, readable fixtures, direct assertions, coverage for malformed inputs, edge cases, ordering, idempotency.

## Output format
Write to `.ai/plans/<NNN>-<slug>.plan.md` matching `templates/dev-plan.template.md`. Fill front matter:
```yaml
---
id: <NNN>
slug: <kebab-case>
version: 0.1.0
status: draft
tier: <patch|feature|component|project from brief>
created: <yyyy-mm-dd>
updated: <yyyy-mm-dd>
depends_on: []
modules_touched:
  - <module1>
  - <module2>
current_phase: 1
total_phases: <count>
brief: <brief_path>
codebase_map: <codebase_map_path>
---
```
Body sections, in order: Context · Goal · Success criteria · Out of scope · Phases (numbered, each with `status: pending`, `files_allowed`, `acceptance`, `validation`, plus the per-phase content described above) · Risks · Open questions · Links.

## Constraints
- The plan must be concise but specific enough that an implementation agent could execute it phase by phase without inventing architecture.
- Every phase must name actual files in this repo. No placeholder file names.
- If you encounter a decision you cannot make from the brief + codebase map, list it under "Open questions for user" at the bottom and **do not invent an answer**.
- If the plan exceeds ~8 phases, reconsider grouping. Surface the concern to the user.

{{> _partials/postamble-wrap }}
