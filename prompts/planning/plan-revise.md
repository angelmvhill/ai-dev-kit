<!--
id: planning/plan-revise
version: 0.1.0
purpose: Revise a dev plan to address review and/or redteam feedback
inputs:
  - plan_path
  - review_paths (one or more)
outputs:
  - .ai/plans/<plan-id>.plan.md (version bumped)
  - changelog block at top
-->

{{> _partials/preamble-orient }}

## Task
Revise the dev plan to address feedback. Preserve every architecture detail from the prior version unless the feedback explicitly justifies its removal.

## User must provide
- **plan_path**: path to the current plan.
- **review_paths**: one or more review/redteam files to incorporate.

## AI must do
1. Read the current plan, every review/redteam file, the brief, and the codebase map.
2. Build a **change ledger**: for each review item, decide one of:
   - **ACCEPT** — incorporate the change.
   - **MODIFY** — incorporate a variant, with reason.
   - **REJECT** — leave the plan unchanged, with reason (e.g., out of scope, conflicts with brief, would violate ownership boundary).
3. Apply ACCEPTs and MODIFYs to the plan.
4. Bump `version` in front matter (patch for typo/clarity fixes, minor for structural changes, major for scope or architecture changes). Set `status: in-review`.
5. Prepend a **Changelog** section to the plan body listing every change made this revision, grouped by phase, citing which review item drove it.
6. Run a **lost-detail check**: compare against the prior version section by section. Any architecture component, contract, invariant, or test requirement that was in the prior version and is no longer present must be either present in the new version or listed in the changelog with an explicit deletion reason.

## Output format
Updated plan file with:
- bumped `version` and `status: in-review` in front matter
- new `## Changelog (vX.Y.Z)` section directly after front matter
- inline `## Change ledger` table (ACCEPT/MODIFY/REJECT with one-sentence reason per review item)
- the revised plan body

## Constraints
- Token-aware. Do not rewrite untouched sections.
- Never silently delete content. If you remove something, the changelog must say so and why.
- If review items conflict with each other, surface the conflict to the user and stop — do not arbitrate alone.
- Status flips to `approved` only by the human user, never by you.

{{> _partials/postamble-wrap }}
