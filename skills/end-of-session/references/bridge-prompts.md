# Bridge Prompt Templates

Paste-ready prompts for the next session. Variant A carries general continuity. Variant B carries the decision patterns of a specific expertise, for sessions that need a mindset from the first message.

## Variant A: standard handoff

```markdown
**Initialize {{PHASE_NAME}}.**

Completed so far: {{PREVIOUS_ACTIVITY}}
Crystallized files: {{DIRECTORY_OR_FILES}}

**Goal**: {{HIGH_LEVEL_GOAL}}

**Session protocol**:
1. Alignment: read {{TRUTH_FILES}}.
2. Rituals: follow {{RITUALS}}.
3. Execute: {{IMMEDIATE_NEXT_STEP}}.
```

## Variant B: persona-embedded handoff

Use when the next session executes, not plans, and needs a specific expertise immediately.

1. Identify the primary and secondary persona or mindset (for example backend and QA).
2. Extract their decision patterns from your workspace's judgment or persona layer. Skip cleanly if none exists.
3. Embed them above the standard handoff content:

```markdown
## Personas (embedded)

### Primary: {{PERSONA_NAME}}
Domain: {{DOMAIN}}
Decision patterns:
- "{{PATTERN_1}}"
- "{{PATTERN_2}}"

### Secondary: {{PERSONA_NAME}}
Decision patterns:
- "{{KEY_PATTERNS}}"

---

{{VARIANT_A_CONTENT}}
```
