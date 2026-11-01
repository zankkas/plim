# ADR-0004: The gateway is shipped, and onboarding consumes it

## Status

Accepted (2026-11-01)

## Context

The target onboarding is one sentence: clone the repo, open your agent in that folder, say "plim, setup workspace". For that ritual to work, an agent booting inside a fresh clone must discover the onboarding procedure through its own boot path — before `.agents/` exists and before any human has edited a file. The kit's boot adapter (`templates/AGENTS.md`) describes an onboarded workspace and cannot serve as the entry point. `README.md` lists the onboard skill, but reading the README is optional behavior of a curious model, not a boot path.

## Decision

Ship a root `AGENTS.md` gateway. It is valid for exactly one state: the un-onboarded clone. It names the ritual ("plim, setup workspace"), points at `skills/onboard/SKILL.md`, and says nothing else that could become a false authority. It carries the marker `<!-- plim:gateway -->`. The filler refuses to overwrite a root `AGENTS.md` without the marker, so onboarding can never clobber a boot file the human wrote themselves; `--force` allows it, because start-over is already explicit. When onboarding fills the workspace, the marked file is consumed: the workspace adapter replaces it at the same path, and the two forms never coexist.

## Consequences

- A fresh clone works in every agent runtime that reads root `AGENTS.md`, with nothing installed by hand.
- Discovery no longer depends on the model choosing to read `README.md`.
- Gateway edits must stay pre-onboarding documents; workspace behavior belongs in `templates/AGENTS.md`.
- Runtimes that read only a runtime-specific adapter (Claude Code's `CLAUDE.md`) get a one-line pointer stub at the same root. The stub holds no governance content, so the gateway stays the single authority.
