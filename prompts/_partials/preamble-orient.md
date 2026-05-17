<!--
id: _partials/preamble-orient
version: 0.1.0
purpose: Standard orientation block included at the top of every prompt
-->

## Orient before acting

Before doing anything else, read in order:
1. `.ai/STATE.md` — current workflow position, active plan, active phase.
2. `.ai/PROJECT.md` — charter, goals, out-of-scope.
3. `.ai/FOLLOWUPS.md` — deferred items from prior phases.
4. The repo's conventions file (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/*`, or equivalent).

If any of these files are missing or empty, stop and tell the user which one is missing before proceeding. Do not improvise.

State your understanding in 2-4 sentences before starting the task: what state we're in, what the task is, what files you intend to touch. The user will confirm or correct.
