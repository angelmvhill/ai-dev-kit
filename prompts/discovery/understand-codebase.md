<!--
id: discovery/understand-codebase
version: 0.1.0
purpose: Produce a structured map of the codebase before planning or implementing
inputs:
  - focus_area (optional, free-text)
  - depth (one of: shallow, standard, deep)
outputs:
  - .ai/notes/codebase-map-<yyyy-mm-dd>.md
-->

{{> _partials/preamble-orient }}

## Task
Read and understand the repository. Produce a structured map an implementation agent (or you, in a later session) can rely on without re-reading the codebase.

## User must provide
- **focus_area** (optional): if the upcoming work targets a subsystem (e.g., "data ingestion pipeline"), name it. AI will go deeper there.
- **depth**:
  - `shallow` — top-level dirs, README, conventions only. ~5 min read.
  - `standard` — adds module-level summaries for code dirs. ~15 min read.
  - `deep` — adds ownership boundaries, key types/dataclasses, invariants, test patterns. Required before any planning prompt.

## AI must do
1. Read in this order, only as deep as the requested depth requires:
   - `README.md`, top-level `*.md` (architecture, conventions)
   - `AGENTS.md` / `CLAUDE.md` / `.cursor/rules/*` (agent rules)
   - `pyproject.toml` / `package.json` / equivalent (deps, scripts, Python version)
   - Repo tree to 2 levels
   - For each top-level code dir: docstrings, `__init__.py`, key public classes
   - Test layout: framework, naming pattern, fixture conventions
   - `git log --oneline -30` for recent change context
   - If `focus_area` given: read every file in that module + its tests
2. Identify **ownership boundaries**: which module owns state, normalization, I/O, orchestration, persistence, recovery.
3. Identify **invariants**: things that must never happen silently (raises, rejects, mark-stale rules).
4. Identify **schemas**: typed dataclasses, frozen records, timestamp conventions (UTC vs local).
5. Identify **test patterns**: what a "good test" looks like in this repo.
6. Note any **landmines**: vague abstractions, mixed concerns, places where conventions break down.
7. Advance STATE: `status: DISCOVERY`, `next_action: planning/plan-create`, `last_prompt: discovery/understand-codebase`, `last_updated` (today).

## Output format
Write to `.ai/notes/codebase-map-<yyyy-mm-dd>.md`:
```markdown
# Codebase map — <focus_area or "full"> — <date>

## Tech stack
- Language/runtime/version
- Key libraries
- Build/run/test commands (exact invocations)

## Top-level layout
<tree, 2 levels, with 1-line descriptions>

## Modules (focused list)
For each relevant module:
- **Purpose**: 1 sentence
- **Owns**: state | I/O | normalization | orchestration | persistence | none
- **Key types**: dataclasses, protocols, enums
- **Public interface**: functions/classes called from outside
- **Invariants**: what must never happen / what raises

## Conventions
- Types (dataclass slots, frozen, typing)
- Timestamps (UTC-aware? boundary handling)
- Error handling (raise vs log vs mark-stale)
- Logging (style, levels)
- Testing (framework, fixtures, what's mocked vs real)

## Recent activity
- Last 10-30 commits, grouped by theme

## Landmines / open questions
- Bulleted, with file:line references where possible
```

## Constraints
- Do not modify any source file.
- Do not invent. If you don't know, write "unknown — needs user input."
- Cite file paths for every claim about behavior.
- If `focus_area` is given, every module outside it gets at most a 1-line summary.

{{> _partials/postamble-wrap }}
