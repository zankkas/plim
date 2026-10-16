# ADR-0002: Capture at the moment of decision; the close audits

**Status**: Accepted (2026-10-16)
**Review**: revisit if session capture shows measurable flow interruption

## Context

The alternative design batched all recording into the session-close ritual. It made every close heavy, and heavy closes get skipped. A skipped close loses the reasoning, which is the part that matters.

## Decision

Decisions, ideas, limitations, and verified knowledge are captured the moment they happen, in a few lines, by the capture-as-you-go skill. The end-of-session skill audits what was captured, classifies for graduation, and reconciles the tracker. The close never reconstructs from memory what capture could have caught live.

## Consequences

- Fidelity rises: the why is written while it is still in context.
- The exit ritual shrinks to minutes.
- Cost: the agent must distinguish decisions from thinking out loud mid-flow. The boundary rule: speculation goes to the intake surface, not the decision log.
