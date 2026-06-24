# Changelog

## v0.2.0 — workflow restructure + reconciliation
Restructured the prompt set for production-grade execution and reconciled all docs, schemas, and prompts so they no longer contradict each other.

- **Status vocabulary (canonical, granular)**: `STATE.md` `status` is now one of `INIT, CHARTER, DISCOVERY, PLAN_DRAFT, PLAN_REVIEWED, PLAN_REDTEAMED, PLAN_IN_REVIEW, PLAN_APPROVED, PHASE_IMPLEMENTED, PHASE_REVIEWED, PHASE_ADDRESSED, PHASE_VERIFIED, INTEGRATED, DONE`. Each names the milestone just completed; `WORKFLOW.md` maps each to the next prompt. Every prompt now advances to the correct milestone; `route.md` covers all statuses.
- **Layout (separate dirs)**: plans in `.ai/plans/NNN-<slug>.plan.md`, briefs in `.ai/briefs/`, reviews in `.ai/reviews/`, codebase maps in `.ai/notes/`. `WORKFLOW.md`, schemas, `README.md`, and `init-project.md` all agree.
- **Journal**: single structured multi-line format (Did/Learned/Decided/Next), newest-first, used by both `postamble-wrap` and `session-wrap`.
- **Schemas**: `dev-plan` gains `version` and `codebase_map`, drops unused `executing`/`review` plan statuses, adds `integrated` phase status; `state` documents the status enum and adds `last_prompt`/`kit_version`.
- **Recovered prompts** (were referenced but missing): planning/plan-redteam, execution/small-change, execution/feature-add, review/quant-validation, operations/commit-message, operations/pr-description; partials conventions-reminder and quant-guardrails. All adapted to current conventions.
- **Naming/scope**: kit renamed to `ai-dev-kit`; removed non-general (weather) example; quant language retained as an optional overlay (`quant-guardrails`, `quant-validation`).
- **Current file set**:
  - Partials: preamble-orient, postamble-wrap, conventions-reminder, quant-guardrails
  - planning: charter, brainstorm, plan-create, plan-review, plan-redteam, plan-revise, plan-cross-analyze
  - discovery: understand-codebase
  - execution: phase-execute, small-change, feature-add
  - review: code-review, quant-validation, review-address, verify
  - operations: integrate, commit-message, pr-description
  - meta: init-project, session-wrap, route
  - Schemas: brief, dev-plan, state, project, journal, review, decisions, followups
  - Scripts: deviation-check.py, plans-index.py, overlap-check.py
  - Templates: project, state, brief, dev-plan, followups, kit.yaml

## v0.1.0 — initial kit
- Workflow state machine in WORKFLOW.md
- Schemas: brief, dev-plan, state, project, journal, review, decisions, followups
- Partials: orient, exit, conventions-reminder, quant-guardrails
- Prompts:
  - planning: charter, plan-create, plan-review, plan-redteam, plan-revise
  - discovery: understand-codebase
  - execution: phase-execute, small-change, feature-add
  - review: code-review, quant-validation, review-address, verify
  - operations: integrate, commit-message, pr-description
  - meta: session-wrap, route
- Scripts: deviation-check.py, plans-index.py, overlap-check.py
- Templates: project, state, brief, dev-plan, followups, kit.yaml
