# Plim

<!-- plim:gateway — this file is the shipped boot gateway for the un-onboarded clone.
Onboarding (skills/onboard/fill.py) replaces it with the workspace adapter. -->

*Governance for agent workspaces.*

A fresh clone has rules to fill and no history. Until onboarding happens, treat everything current as unverified: this file is all the agent has, and it must not invent work, status, or habits.

## The setup ritual

When the human says **"plim, setup workspace"** (or otherwise asks to set this workspace up):

- If `.agents/SOUL.md` exists and contains no `{{`, onboarding already happened; do not run it again, and do not run it a second time in this conversation even when asked to set up again.

1. Read `skills/onboard/SKILL.md` and follow it. It asks a few plain questions and fills the templates itself; the human edits no files.
2. When onboarding finishes, this gateway is gone: the filler has replaced it with the workspace adapter at this same path. Boot from that adapter from now on.

Do not run onboarding more than once. Re-running needs an explicit start-over.

## If the human is not setting up

Keep the boot light. Read `README.md` for orientation, say in two lines that the governance layer stays empty until onboarding, and offer the ritual above. Do not preload directives or skills; they are read on demand after onboarding.
