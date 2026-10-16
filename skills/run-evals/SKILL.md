---
name: run-evals
description: >
  Run a skill's eval cases as a reasoning pass and report the verdict per
  case. Use after a skill was edited, when a hygiene pass is due, or when a
  session shows behavior a skill did not anticipate.
---

# Run Evals

**Why:** evals that are never run are decoration. This skill is the execution layer for the kit's own eval cases, in workspaces that have no checking tool yet.

## Steps

1. **Load the skill under test.** Read its current SKILL.md and any references it names.
2. **Load its cases.** Read `evals/cases.md`; use `evals/cases.json` when present, matching case by id.
3. **Walk each case.** Act the scenario out in reasoning: does the current procedure produce the expected behaviors? Does it prevent the forbidden ones? Judge the skill as written, not as intended.
4. **Report per case.** One line per case id: pass or fail, and for a fail, the exact step that no longer holds.
5. **Stop on failure.** A failed case blocks the change that caused it: fix the skill or fix the case. Never ship both broken.
6. **Record the run.** Append a one-line dated result next to the eval file: date, cases passed, verdict.

## Boundaries

- This pass judges the written procedure, not the agent's general behavior in past sessions. Session evidence feeds new cases; it does not replace the walk.
- One case failure is enough to stop. Do not average, do not round up.
- Cases are versioned artifacts: changing a case is a decision, recorded like one.

## Completion criterion

Every case id has a verdict, failures have a stated cause, and the run result is recorded with a date.
