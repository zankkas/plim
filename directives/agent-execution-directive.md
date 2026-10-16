# Agent Execution Directive

**Status**: ACTIVE
**Purpose**: Define how agents in this workspace execute tasks, from receiving work to delivering results. Every agent (spawned subagent, coding-agent session, background task) follows these rules.

---

## The Delivery Cycle

Every code task follows this sequence. No step is skipped unless the task is trivially small (< 5 lines, single-file, no logic change).

1. **Read the spec.** Before writing code, read the blueprint/task fully. Understand WHAT to build, WHERE it goes, and HOW to verify it.

2. **Consult the judgment layer, if one exists.** If your workspace runs a specialist or framework layer for engineering judgment, consult it for the task's domain and match the expert to the work:
   - Architecture/design decisions → the relevant design specialists
   - Testing strategy → the quality/testing specialist
   - Performance concerns → the performance specialist
   - Security implications → the security specialist
   - If unsure which expert → query with the problem statement and let the layer route it
   - If no judgment layer exists → skip this step cleanly and proceed

3. **Implement.** Write the code. Follow the spec's file paths, interfaces, and constraints. One logical change per commit.

4. **Verify.** Run the project's test suite. If the spec defines verification commands, run those exactly. If tests fail, fix them before proceeding.

5. **Self-review.** Before declaring done, re-read the diff against the spec. Check:
   - Does the implementation match the requirements?
   - Are there unhandled edge cases the spec calls out?
   - Is there dead code or unnecessary complexity?

6. **Request independent review.** For non-trivial work: spawn a fresh agent (or request human review) that sees ONLY the diff and the spec, not the implementation reasoning. The reviewer checks correctness, not style.

7. **Fix findings.** Address legitimate review findings. Re-verify. If a finding is wrong, explain why; do not silently ignore it.

8. **Deliver.** Open a PR (or report completion). Include: what was done, what was tested, and any decisions made during implementation that deviated from the spec.

---

## The Judgment Layer (pluggable)

A judgment layer is any workspace-owned source of specialist reasoning: persona libraries, expert frameworks, or a similar intelligence overlay. Wire it in `templates/AGENTS.md` terms: the boot adapter and this directive name it, or omit it entirely.

**When to consult it:**
- Before making an architecture decision that is not in the spec
- When the task involves a domain you are uncertain about
- When reviewing code: query for the relevant quality framework
- When a spec is ambiguous: the relevant specialist can help interpret intent

**When NOT to consult it:**
- For trivial tasks (rename a variable, fix a typo)
- When the spec already contains explicit, unambiguous instructions
- Mid-implementation for every line of code. It is for decisions, not narration

---

## Safety Boundary

Agents may do autonomously:
- Implement spec'd features on feature branches
- Run tests
- Open draft PRs
- Review code
- Fix lint/format/test failures
- Create or update spec documents (during planning phases)

Agents must NOT do without human approval:
- Merge to main/master
- Deploy to production
- Delete data or drop tables
- Change auth/permissions/security config
- Deviate from a spec's architecture decisions
- Create new projects or repos

---

## Work-State Integration

- Before starting work: query the canonical work item in the live tracker named by the compass.
- Agents may start execution only from an item marked ready, or from an explicit human decision that creates the work item.
- When starting work: update the work-item state where the tracker supports it.
- When blocked: record the blocker on the work item with the specific cause.
- When done: update the work item with completion evidence and link the implementation PR or artifact.
- Legacy snapshots and generated boards are migration artifacts. Do not update them as a current-state mirror.

---

## Priority Order (when rules conflict)

1. Safety boundary (never override)
2. Spec requirements (the spec wins over general preferences)
3. This directive (the delivery cycle)
4. Judgment-layer guidance (expert advice informs, does not override specs)
5. General best practices (fallback)
