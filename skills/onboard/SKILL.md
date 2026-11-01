---
name: onboard
description: >
  Set up a freshly cloned workspace on the first session, when `.agents/SOUL.md`
  is missing, or when template placeholders are still unfilled. Ask a few plain
  questions, then fill the templates. The person does not copy files or edit
  placeholders.
---

# Onboard

**Why:** The clone already holds the structure. The first session fills it by conversation. Sending the person into the templates puts them back at ground zero.

## Steps

1. **Stop if setup already happened.** If `.agents/SOUL.md` exists and contains no `{{` placeholder, say onboarding already happened and stop. Do not ask the questions again. Re-run only when the person explicitly says to start over. Then pass `--force` and let the filler overwrite. Do not merge the old files with the new answers by hand.
2. **Ask the required questions, one at a time, in plain language.** Do not show placeholder token names. Do not ask the person to copy or edit files.
   - What should the agent call you?
   - What is this workspace called?
   - Where should the agent look up what is active now? "Nowhere yet" is a valid answer.
   - What short name should the decision log use? One word, such as "work".
   - In a few lines, who are you and what is this workspace for?
3. **Offer the optional questions once.** A skip leaves that field empty. Do not invent a strength, a pitfall, a working style, or a public voice. The filler removes the template examples, so a skip does not leave a sample person in the profile.
   - A strength, and what the agent should do about it.
   - A pitfall, and the question the agent should ask when it shows up.
   - How you like to work.
   - What you own, and what the agent should carry.
   - Any rules for public writing. If there are none, skip, and the voice section is deleted.
4. **If the answer is that there is no live tracker,** write this value and no other: `No live tracker yet. Report current work as unverified.` Do not invent a tracker, a board, or a repository.
5. **Run the filler.** Write the answers to a JSON file using the field names from `python3 skills/onboard/fill.py --help`, then run `python3 skills/onboard/fill.py --dest . --answers <file>` from the repo root. Do not edit files under `templates/` or `wiki/templates/`. Do not fill wiki page templates. Do not fill placeholders by hand. Do not commit or push.
6. **If the filler exits non-zero,** say what it refused and ask only for the missing answer. Then run it again.
7. **Read the result back in a few lines:** who the workspace is for, where current work lives, and the path of the decision note. Run `python3 scripts/doctor.py` and read its verdict in one line. If it reports findings, show them and stop without claiming onboarding is done.

## Non-goals

- Do not onboard wiki page templates. They stay templates until a real page exists.
- Do not overwrite a filled soul file unless the person said to start over.

## Completion criterion

`.agents/SOUL.md`, `.agents/PROFILE.md`, `.agents/compass.md`, the root `AGENTS.md`, and `.agents/session-notes/<domain>.md` exist. None of them contain `{{`. The profile does not contain the template examples. The person heard the read-back, and the doctor's verdict was read back too.
