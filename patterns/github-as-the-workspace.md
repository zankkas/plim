# GitHub as the Workspace

Most people use GitHub to host code. A governed agent workspace uses it for something broader: it is the knowledge layer, the governance layer, and the memory of the operation.

## What the repo carries

- **Code**, when there is code. That part is standard.
- **Specs and strategy**, versioned like code. A spec is an executable input; its history is the record of how thinking evolved.
- **Governance**, the identity, navigation, and continuity files. The workspace travels with its rules.
- **Issues and a project board**, as the live status authority.

## What this buys

**One truth across machines.** Any computer that clones the repo wakes up with the same governance, the same knowledge, and the same history. The workspace is no longer tied to one machine.

**Time travel.** Every decision, every spec revision, every governance change is a commit. Going back is a checkout. This is not an archive; it is the tranquility to move fast, because nothing is ever silently lost.

**History as reasoning.** The blame view works on prose the same way it works on code. When a rule raises the question of who decided this and why, the answer is one diff away.

**Agents work through it too.** Issues carry scope and discussion. Pull requests carry review. Agents file, comment, and reconcile the same way humans do, which means human and agent work share one surface instead of two.

## The honest trade-off

Parts of this are overkill. A repo used mostly for knowledge accumulates cleanup debt the same way a code repo accumulates technical debt: stale branches, merged-away notes, half-finished specs. The fix is the same discipline as code: periodic pruning, clear archive conventions, and the hygiene pass. Without it, the knowledge layer becomes a second landfill.

## When to reach for this pattern

- Work spans more than one machine.
- Agents and humans need a shared source of truth.
- The reasoning behind decisions matters as much as the decisions.
- You want the option to go back, not the obligation to.

If none of these hold, a plain folder is fine. GitHub earns its keep when memory and multi-machine truth are the problem.
