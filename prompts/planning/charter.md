<!--
id: planning/charter
version: 0.1.0
purpose: Write or refine PROJECT.md — the durable charter of the whole project
inputs:
  - none required (reads existing PROJECT.md)
outputs:
  - updated .ai/PROJECT.md
  - advanced STATE.md status
-->

{{> _partials/preamble-orient }}

## Task
Write or refine `PROJECT.md` — the durable charter of the whole project. This is the umbrella under which every brief and plan lives. Get this right; you'll rarely edit it again.

## User must provide
- Willingness to answer up to ~6 targeted questions in **one round**. The AI asks all questions in a single message, the user replies in one message, the AI fills the document.

## AI must do
1. Read `.ai/PROJECT.md`. Identify sections that are empty, marked `TODO:`, or contain placeholder text from the template.
2. Read `.ai/STATE.md`. If `status` is not `INIT`, ask the user whether this is an intentional re-charter (mid-project re-framing is valid, but flag it).
3. For each incomplete or weak section, formulate one targeted question. Ask all questions together in a single numbered list. Wait for the user.
4. With the user's answers, write content for each section:
   - **Problem**: what is broken or missing in the world that this project exists to address. 2–4 sentences. Concrete, not aspirational.
   - **Goal / hypothesis**: for `build` projects, the system that will exist when done. For `research` projects, the hypothesis being tested. For `hybrid`, both.
   - **Success criteria**: 3–5 bullets, each verifiable in code, data, or operations. "Sharpe ≥ 1.5 on out-of-sample data from 2024-01-01" — not "good performance."
   - **Scope**: bullet list of capability areas this project covers. Area level, not feature level.
   - **Out of scope**: bullet list of things explicitly excluded *forever* from this repo. This is the scope-creep killer. Be aggressive.
   - **Key references**: papers, datasets, prior systems, related repos.
   - **Conventions notes**: anything future-you or another contributor needs to know — Python version, deployment target, branch model, hard rules.
5. Run an internal consistency check:
   - Do any success criteria depend on something marked out of scope?
   - Is the goal achievable given the implied constraints?
   - Are there open questions critical enough that the charter shouldn't be finalized?
6. Write the updated `PROJECT.md`. Surface a diff summary (sections changed, content added).
7. Advance STATE: `status: CHARTER`, `next_action: discovery/understand-codebase`, `last_prompt: planning/charter`, `last_updated` (today).

## Output format
1. **Questions** block (single batch).
2. After user answers: the full updated `PROJECT.md`.
3. **Diff summary**: what changed.
4. **Consistency findings**: list, or "no issues."
5. **Next step**: `discovery/understand-codebase`.

## Constraints
- Ask all questions in one batch. No long interrogation chains.
- Do not invent. If the user's answer is vague, write `TODO:` and surface it as an open question rather than fabricating content.
- This prompt is for the **whole project**, not the current piece of work. If the user starts describing a specific feature, redirect: "That sounds like a brief — let's get the charter done first, then write a brief for the feature."
- Do not modify any file outside `.ai/PROJECT.md` and `.ai/STATE.md`.

{{> _partials/postamble-wrap }}
