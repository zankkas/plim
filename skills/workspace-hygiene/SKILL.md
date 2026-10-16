---
name: workspace-hygiene
description: >
  Periodically audit the governance layer for authority drift, duplicate
  operational skills, stale adapters, and broken references. Use weekly or
  when the workspace feels noisy, contradictory, or stale.
---

# Workspace Hygiene

**Why:** Governance decays when a view, cache, skill, or session ritual quietly becomes a second authority.

## Checks

### 1. Authority

- [ ] The live tracker named in the boot adapter and compass is stated as the current authority.
- [ ] All boot adapters (AGENTS.md, CLAUDE.md, and any runtime steering files) are identical thin adapters.
- [ ] The compass contains orientation, not a status table or queue.
- [ ] Any legacy snapshot, generated board, or migration artifact is clearly marked as such.

### 2. Operational skills

- [ ] Exactly one model-invoked close procedure owns session continuity.
- [ ] Capture, handoff, hygiene, and synthesis skills have distinct triggers and write targets.
- [ ] No close procedure commits, pushes, merges, deploys, closes issues, or deletes data automatically.
- [ ] No operational skill writes a second status registry.
- [ ] No active skill assumes missing metadata, dashboard, or journal files.

### 3. Continuity

- [ ] The newest session note is concise and records decisions, risks, and one next action.
- [ ] Durable human patterns belong in `.agents/PROFILE.md`; temporary work state does not.
- [ ] Open work has a canonical item in the live tracker, or is explicitly reported as unlinked.
- [ ] Tracker-unavailable mode is reported as unverified, never replaced with memory or local cache.

### 4. Ceremony weight

Overkill is not a one-time admission. It is a state that returns as the workspace grows. Check it:

- [ ] The exit ritual still takes minutes, not more. If the close grew heavy, move its weight to the scheduled passes.
- [ ] Every directive still earns its place. A rule nobody has needed in weeks is a candidate for retirement.
- [ ] Templates and wiki pages are still the shortest accurate version of what they hold.
- [ ] One ceremony exists per moment. Two rituals for the same trigger means one is retirement-ready.

### 5. References

Spot-check paths named by the active adapters and operational skills. Flag missing paths. Do not silently create replacement files.

## Fix policy

- Remove or rewrite stale instructions directly when the correction is mechanical.
- Ask before deleting a skill that may be intentionally invoked by another client.
- Do not promote session-note patterns into PROFILE automatically.
- Do not commit or push as part of hygiene.

## Report

Return under 20 lines:

- Authority: pass or finding
- Adapter parity: pass or finding
- Close workflow: pass or finding
- Duplicate skills: list
- Broken references: list
- Recommended smallest fix
