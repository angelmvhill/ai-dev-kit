---
id: discovery/understand-codebase
version: 0.1.0
purpose: Build context on the existing codebase before planning
inputs: [PROJECT.md, codebase]
outputs: [JOURNAL.md notes]
next_stage: PLAN
---

{{> _partials/orient }}

## Task

Build a concise mental model of the codebase as it pertains to this project.

Steps:
1. Read `.ai/PROJECT.md` to understand the scope.
2. Survey: top-level structure, key modules in scope, entry points, tests.
3. Identify: existing code that will be touched, code that must NOT be touched, external dependencies.
4. Produce a summary ≤500 words appended to `.ai/JOURNAL.md` under a "Discovery" heading.
5. List open questions about the codebase that affect planning.

Do not propose changes. Do not write a plan. Discovery only.

{{> _partials/exit }}
