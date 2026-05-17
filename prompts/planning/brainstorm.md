<!--
id: planning/brainstorm
version: 0.1.0
purpose: Explore the solution space for a problem before writing a dev plan
inputs:
  - problem_statement
  - constraints (optional)
  - non_goals (optional)
outputs:
  - .ai/briefs/<NNN>-<slug>.brainstorm.md
-->

{{> _partials/preamble-orient }}

## Task
Explore the solution space for a problem. Output is a **brainstorm document**, not a plan. The goal is to surface options, tradeoffs, and a recommended direction the user can react to before any plan is written.

## User must provide
- **problem_statement**: what is broken, missing, or being added, and why it matters now. 1-3 paragraphs.
- **constraints** (optional): hard limits — latency budgets, compatibility requirements, tools that must be used, deadlines.
- **non_goals** (optional): things explicitly out of scope for this round.
- **codebase context**: path to an existing `codebase-map-*.md` from `discovery/understand-codebase`, OR explicit permission for AI to skim the repo first.

If problem_statement is vague or has more than one problem inside it, **ask up to 3 clarifying questions and stop**.

## AI must do
1. Restate the problem in one sentence. User confirms before you continue.
2. Generate **2-4 distinct solution approaches** at the architecture level (not implementation). Each must be substantively different — not three flavors of the same idea.
3. For each approach, write:
   - **Sketch**: 3-6 sentences. Which modules/files are affected. What ownership boundary it respects or changes.
   - **Why it works**: the property of the problem that makes this approach fit.
   - **Why it might not**: failure modes, integration risk, hidden complexity.
   - **Cost**: rough engineering effort (S/M/L) and operational/runtime cost.
   - **Reversibility**: easy / medium / hard to undo if it doesn't work.
4. Identify **decision drivers**: 2-4 axes that should drive the choice (e.g., latency, blast radius, time-to-first-signal, team size of one).
5. Recommend one approach with a clear "I'd pick X because Y" sentence. Note what would have to be true for you to pick differently.
6. List **open questions** the user must answer before plan-create.

## Output format
Write to `.ai/briefs/<NNN>-<slug>.brainstorm.md`:
```markdown
# Brainstorm: <slug>
Date: <yyyy-mm-dd>
Problem: <one-sentence restatement>

## Approaches
### A: <name>
- Sketch:
- Why it works:
- Why it might not:
- Cost:
- Reversibility:

### B: <name>
...

## Decision drivers
- ...

## Recommendation
<one paragraph>

## Open questions for user
- ...
```

## Constraints
- No code. No file lists down to the function. This is architecture-level only.
- No "we could combine A and B" cop-outs unless you also describe the combined approach as its own option C.
- Do not skip "Why it might not." Every approach has one.
- If you cannot honestly produce 2 distinct approaches, say so and stop.

{{> _partials/postamble-wrap }}
