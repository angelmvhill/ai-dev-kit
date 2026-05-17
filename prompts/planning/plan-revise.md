---
id: planning/plan-revise
version: 0.1.0
purpose: Consolidate review + redteam into a revised plan ready for human approval
inputs: [draft plan, review, redteam]
outputs: [.ai/plans/NNN-<slug>.md status: in-review]
next_stage: EXECUTE (after human flips status to approved)
---

{{> _partials/orient }}

## Task

Consolidate findings from review and redteam files and update the plan.

Steps:
1. Read draft, review, redteam.
2. For each finding, classify: accept / reject / defer.
   - Findings raised by BOTH review and redteam → auto-elevate to blocking; must be addressed.
3. Accepted findings → revise the plan.
4. Rejected findings → append rationale to `.ai/DECISIONS.md`.
5. Deferred findings → append to `.ai/FOLLOWUPS.md` with link back to plan id.
6. Update plan front matter: bump `updated`, ensure `modules_touched` and `total_phases` reflect changes.
7. **Do not** flip `status` to `approved` — that is the human's gate. Set `status: in-review` and report to the human exactly what needs sign-off.

{{> _partials/exit }}
