---
id: planning/plan-create
version: 0.1.0
purpose: Produce a draft dev plan from a BRIEF
inputs: [BRIEF, PROJECT.md, plans/INDEX.md, FOLLOWUPS.md, CONVENTIONS.md]
outputs: [.ai/plans/NNN-<slug>.md with status: draft]
next_stage: PLAN_REVIEW
---

{{> _partials/orient }}
{{> _partials/conventions-reminder }}
{{> _partials/quant-guardrails }}

## Task

Produce a draft dev plan at `.ai/plans/{{PLAN_ID}}-{{SLUG}}.md` conforming to `.ai/kit/schemas/dev-plan.md`.

Inputs to consult:
- Brief: `.ai/plans/{{PLAN_ID}}-{{SLUG}}.brief.md` (source of truth for WHAT)
- Existing plans: `.ai/plans/INDEX.md`
- Deferred items: `.ai/FOLLOWUPS.md` (incorporate any relevant)

Steps:
1. Read the brief in full.
2. Compute `modules_touched` honestly. Run `python .ai/kit/scripts/overlap-check.py` to detect overlap with active plans. List overlaps in the Risks section.
3. Decompose into phases. Each phase MUST have:
   - A clear goal
   - `files_allowed` list (exact paths or globs)
   - At least one testable acceptance criterion
   - A validation command or check
4. Phase boundaries align with logical commit points.
5. For research tiers, include kill-criteria.
6. Set front matter: status=draft, tier from brief, current_phase=1, total_phases=N.
7. Apply quant guardrails. Flag risks.

Do not implement anything. Plan only.

{{> _partials/exit }}
