# Review schema

Filename: `.ai/reviews/NNN-<slug>.review.md` (or `.redteam.md`, or `NNN-<slug>-phase-<n>.code-review.md`)

Shared shape across plan reviews, code reviews, redteam reviews, quant validations. Multiple review types may coexist in one file (sections labeled by review_type).

```markdown
---
review_of: NNN
reviewer: <model id or human>
review_type: plan|plan-redteam|code|quant-validation
date: YYYY-MM-DD
verdict: blocked|changes-requested|approved
---

## Blocking
- [ ] <finding> | severity: high | category: scope|correctness|missing|deviation|safety

## Recommended
- [ ] <finding> | category: ...

## Nits

## Questions for human

## Approved as-is
```

For `review_type: code`, additionally include these sections BEFORE Quality findings:

```markdown
## In-scope, passed
- <acceptance criterion N>: <how verified>

## In-scope, failed
- <acceptance criterion N>: <what's wrong>

## Out-of-scope additions
- <file X>: <description>

## Missing deliverables
- <acceptance criterion N>: not addressed
```
