# No Documentation Garbage (Directive)

**Status**: ACTIVE
**Purpose**: Prevent governance-folder pollution

---

## The Rule

**One file per topic. Update it. Never create a new one.**

---

## Forbidden

- Creating `*_SUMMARY_*.md`, `*_ANALYSIS_*.md`, `*_DIAGNOSTIC_*.md`, `*_GUIDE_*.md`, `*_RESOLUTION_*.md` files
- Creating dated variants of existing files
- Creating more than ONE file to document a single incident, bug, or investigation
- Creating any file "to document your process" or "summarize what was done"

## Required

- Status → update `.agents/compass.md` directly
- Decisions → record in `.agents/session-notes/{project}.md`
- Architecture decisions → document in the spec's `design.md` (ADRs section)

<!-- Adapt the three write targets to your own file names. The point is that every
     kind of knowledge has exactly one designated home, and the agent never
     invents a new one mid-session. -->

## When Tempted to Create a New File

Ask: "Does a file for this topic already exist?"
- Yes → update it
- No → create ONE file, name it clearly, never create a companion file
