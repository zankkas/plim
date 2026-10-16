---
name: session-handoff
description: Protocol for maintaining context across sessions and embedding persona knowledge.
---

# Ritual: System Context Handoff

**Trigger**: At the end of a session when work is incomplete and must continue in a fresh session.

## The Philosophy

Context is volatile. Sessions are ephemeral. To maintain continuous consciousness across disjointed sessions, we must **crystallize** dynamic context into static files before checking out. A fresh agent should never have to "read the logs" to understand the state.

When execution requires a specific engineering mindset (backend, frontend, and so on), we also **embed decision patterns** directly into the handoff to give the next agent character without runtime lookup.

## The Standard

The **Context Handoff** process consists of 3 strict steps:

### 1. Crystallization (The "Save State")

Before leaving, you MUST update the "Truth Files" to reflect the exact current reality.

* **Requirements/Design**: Update `REQUIREMENTS.md` or `DESIGN.md` with any new decisions made during the chat.
* **Status**: Keep status in the live tracker, where it belongs. If your workspace stores per-project state locally, update that file to reflect what is done versus pending.
* **Tasks**: Ensure `task.md` or `tasks/*.md` accurately shows the next immediate step.

### 2. Cleanup (The "Hygiene")

Remove potential sources of confusion for the next agent.

* **Delete/Archive**: Move obsolete notes (for example `investigation_notes.md`) to an `archive/` folder.
* **Update Readme**: Ensure the project root `README.md` does not contain outdated "Known Issues".

### 3. The Transition Prompt (The "Bridge")

Append a structured session entry to `.agents/session-notes/{project}.md`. This keeps all session context co-located per project and readable by all IDEs.

#### Variant A: Standard Handoff

Use this for general purpose continuity.

```markdown
# PROMPT: [Phase Name] Continuation

Copy and paste the following prompt to start the next session.

---

**Initialize [Phase Name].**

I have just completed the [Previous Activity].
We have a crystallized set of files in [Directory].

**Your Goal**: [High level goal].

**Strict Session Protocol**:
1.  **Step 1: Alignment**: Read [List of Truth Files].
2.  **Step 2: Ritual Observance**: We follow [Ritual Name].
3.  **Step 3: Execution**: [Immediate next step].

**Context Loading**:
*   Please read [Truth Files] now to begin.
```

#### Variant B: Persona-Embedded Handoff

Use this when **transitioning to execution** or when specific expertise is needed immediately.

1. **Identify personas**: choose Primary (for example backend) and Secondary (for example QA).
2. **Extract patterns**: use your workspace's judgment or persona layer to find their "Decision Patterns". Skip cleanly if none exists.
3. **Embed in prompt**:

```markdown
# [Phase] Execution Handoff

## Personas (Embedded)

### Primary: [Persona Name]
**Domain**: [from persona]
**Decision Patterns**:
- "[pattern 1]"
- "[pattern 2]"

### Secondary: [Persona Name]
**Decision Patterns**:
- [key patterns]

---

## Start Prompt
[Standard Handoff Content]
```

## The Workflow

1. **Assess**: user requests deeper context or session end.
2. **Crystallize**: agent updates specs and status files.
3. **Select Variant**: Standard for planning/general, Embedded for detailed execution.
4. **Bridge**: agent creates the prompt file.
5. **Handoff**: agent notifies the user that the system is ready.
