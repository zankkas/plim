# Skill Awareness Directive

**Status**: ACTIVE
**Purpose**: Make skill usage automatic. Assistants propose relevant skills at session start without being asked.

---

## The Rule

**After loading the compass, before starting work, scan available skills, match against the current session's task, and propose 2-5 relevant ones.**

Do not auto-load skills (that burns context). Propose. Let the user accept or reject. Then load only the accepted ones.

---

## The 3-Step Pattern

### Step 1: Scan (cost: ~0 tokens)

The assistant already has the available-skills block in its system prompt. It knows all skill names, descriptions, and trigger keywords. No tools needed.

### Step 2: Match (cost: reasoning only)

Cross-reference skill trigger keywords against what the user asked for. Three sources of signal:

| Signal | Example |
|--------|---------|
| **User's explicit ask** | "design a module" → design or architecture skills |
| **Compass context** | Working on an orchestrator → the relevant domain skills |
| **Task type** | Writing specs → spec-review skill; committing code → git skill; building UI → UI skill |

Use the skill's `description` field. It contains trigger phrases. If the user's words overlap with trigger phrases, that skill is a candidate.

### Step 3: Propose (cost: ~one sentence per skill)

Format:

```
Before I dive in: I see 3 skills that could add value here:

- **spec-review**: audit the spec for gaps before execution (catches wiring errors cheaply)
- **tracer-bullet**: thinnest end-to-end path first, reversibility check
- **architecture-check**: verify dependency direction between modules

Want me to load any/all of these before I proceed?
```

Only propose skills that are genuinely relevant. Do not propose 10 skills to impress. 2-5, each with a one-line *why for this specific task*.

---

## When NOT to Propose

Skip the proposal when:
- The user gave a trivial task ("what time is it?", "list files", "run this command")
- The user is mid-conversation in an ongoing task (skills were already evaluated at session start)
- The user explicitly said "no skills" or "just do it"
- You already proposed skills this session and the user declined

---

## After Acceptance

If the user says "yes, load X and Y":
1. Load each accepted skill file.
2. Apply the skill's framework to the task (scoring, checklist, audit, whatever the skill prescribes).
3. Surface findings before proceeding to execution.

---

## Discovery Locations

Skills live wherever your runtime surfaces them: agent-global skill directories, workspace `.agents/skills/`, or runtime packages. No configuration is needed beyond putting the files there. Adapt this section to your actual runtime.
