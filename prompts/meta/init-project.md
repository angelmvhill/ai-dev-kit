<!--
id: meta/init-project
version: 0.1.0
purpose: Scaffold .ai/ directory and initialize STATE for a new or existing project
inputs:
  - project_name
  - project_root (absolute path)
  - project_description (one paragraph)
outputs:
  - .ai/PROJECT.md
  - .ai/STATE.md
  - .ai/JOURNAL.md
  - .ai/FOLLOWUPS.md
  - .ai/briefs/ (empty)
  - .ai/plans/ (empty)
  - .ai/reviews/ (empty)
-->

## Task
Initialize the ai-dev-kit workflow in this project.

## User must provide
- **project_name**: short identifier (kebab-case).
- **project_root**: absolute path to the repo root.
- **project_description**: 1 paragraph — what this project does, why it exists, success criteria. If unclear, ask 3 targeted questions and stop.

## AI must do
1. Confirm `project_root` exists and is a git repo. If not, stop.
2. Check whether `.ai/` already exists. If yes, do not overwrite — report contents and stop.
3. Create the directory layout:
   ```
   .ai/
   ├── PROJECT.md
   ├── STATE.md
   ├── JOURNAL.md
   ├── FOLLOWUPS.md
   ├── briefs/
   ├── plans/
   └── reviews/
   ```
4. Populate `PROJECT.md` by copying `templates/project.template.md`. Set front matter `name`, `started` (today, UTC), `type` (`research`|`build`|`hybrid` — ask the user if unclear). Fill body sections from `project_description`: Problem, Goal / hypothesis, Success criteria, Scope, Out of scope, Key references, Conventions notes. Anything not provided becomes a `TODO:` line in the relevant section.
5. Populate `STATE.md` by copying `templates/state.template.md`. Set: `status: CHARTER`, `last_updated` (today), `last_session: bootstrap`, `last_prompt: meta/init-project`, `next_action: write PROJECT.md`, `kit_version` (pin from kit `CHANGELOG.md`). Leave `active_plan`, `current_phase`, `blockers` at their default values from the template.
6. Populate `FOLLOWUPS.md` by copying `templates/followups.template.md`. Create empty `JOURNAL.md` with a single header line: `# Journal`.
7. Print the resulting tree and the `TODO:` items in `PROJECT.md` that the user must complete before running any other prompt.

## Output format
- File tree (literal).
- Bulleted list of `TODO:`s in `PROJECT.md` for the user.
- Next step line.

## Constraints
- Never overwrite an existing `.ai/` directory.
- Do not invent project details — anything not provided becomes a `TODO:`.
- No code changes outside `.ai/`.

{{> _partials/postamble-wrap }}
