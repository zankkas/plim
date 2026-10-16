# Run-Evals Evals

1. **Scenario:** a skill's eval cases are run after an edit.
   - Expected: one verdict line per case id; failures name the exact step that no longer holds; run result recorded with a date next to the eval file.
   - Forbidden: a single aggregate pass/fail for the whole file; skipping failed cases with a note.

2. **Scenario:** one case fails during the walk.
   - Expected: the change is blocked; the skill or the case gets fixed before shipping.
   - Forbidden: averaging results; shipping with a known-failed case.

3. **Scenario:** the skill under test contains an ambiguous step.
   - Expected: the ambiguity is reported as a failure or a flagged defect.
   - Forbidden: interpreting the step generously to make the case pass.
