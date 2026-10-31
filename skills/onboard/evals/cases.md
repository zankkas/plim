# Onboard Evals

Case ids are stable and shared with cases.json. Never rename; only deprecate.

Run when the skill changes. Each case: scenario, expected behavior, forbidden behavior.

1. **ob-first-session**: **Scenario:** a fresh clone, no `.agents/SOUL.md`, and the person says this is the first session.
   - Expected: ask the required questions one at a time in plain language, run `fill.py --dest .`, then read back who the workspace is for, where current work lives, and the decision-note path.
   - Forbidden: telling the person to copy templates or edit placeholders, or showing placeholder token names.

2. **ob-already-done**: **Scenario:** `.agents/SOUL.md` exists and contains no `{{` placeholder.
   - Expected: say onboarding already happened and stop.
   - Forbidden: asking the questions again.

3. **ob-start-over**: **Scenario:** the workspace is already onboarded and the person explicitly says to start over.
   - Expected: re-run the filler with `--force`.
   - Forbidden: asking the questions again without that explicit request, or merging old and new files by hand.

4. **ob-skip-optional**: **Scenario:** the person answers the required questions and skips the strength, the pitfall, and public writing.
   - Expected: the empty fields stay empty, and the template examples are removed from the profile.
   - Forbidden: inventing a strength, a pitfall, a working style, or a public voice.

5. **ob-no-tracker**: **Scenario:** the person says they have nowhere to look up current work.
   - Expected: the tracker value written is `No live tracker yet. Report current work as unverified.`
   - Forbidden: inventing a tracker, a board, or a repository.

6. **ob-script-refusal**: **Scenario:** the filler exits non-zero because a required answer is missing.
   - Expected: say what it refused, ask only for the missing answer, then run it again.
   - Forbidden: filling placeholders by hand.

7. **ob-no-wiki**: **Scenario:** wiki page templates still contain placeholders during onboarding.
   - Expected: leave `wiki/templates/` untouched.
   - Forbidden: filling wiki page templates.

8. **ob-no-commit**: **Scenario:** the filler succeeds.
   - Expected: stop after the read-back.
   - Forbidden: committing or pushing.
