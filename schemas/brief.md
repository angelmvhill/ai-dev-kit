# BRIEF schema

Filename: `.ai/plans/NNN-<slug>.brief.md`
Authored by: human (NEVER by LLM)

The brief defines WHAT and WHY. It is the source of truth for the plan that follows.

```markdown
---
plan_id: NNN
slug: <kebab-case>
author: <human>
date: YYYY-MM-DD
tier: patch|feature|component|project
---

## What
<Unambiguous functional description. No HOW.>

## Why
<Goal: business need, research hypothesis, system requirement.>

## Interface
<Inputs, outputs, callers, dependencies.>

## Acceptance criteria
<Testable. For research: include falsifiability conditions.>

## Constraints
<Performance, integration, data, latency, compatibility.>

## Explicitly out of scope
<What this work will NOT touch or attempt.>

## Open questions for the planner
<Things the human is uncertain about and wants the planner to address.>
```
