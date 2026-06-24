<!--
id: _partials/preamble-orient
version: 0.1.0
purpose: Standard orientation block included at the top of every prompt
-->

## Orient before acting

Before doing anything else, read in order (only those that exist):
1. `.ai/STATE.md` — current workflow position, active plan, current phase. **Required.**
2. `.ai/PROJECT.md` — charter, goals, out-of-scope. **Required.**
3. `.ai/CONVENTIONS.md` — project house rules (extends `.ai/kit/CONVENTIONS.md`); project-local wins on conflict.
4. `.ai/FOLLOWUPS.md` — deferred items from prior phases.
5. The repo's own conventions file if present (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*`, or equivalent).

If a **required** file (`STATE.md` or `PROJECT.md`) is missing or empty, stop and tell the user before proceeding. If an optional file is missing, note it and continue — do not improvise project rules that aren't written down.

State your understanding in 2-4 sentences before starting the task: what state we're in, what the task is, what files you intend to touch. The user will confirm or correct.
