# ADR-0003: Evals are the regression gate for skills

**Status**: Accepted (2026-10-16)
**Review**: revisit when a skill marketplace or cross-workspace promotion becomes real

## Context

Skills drift. Steps get edited and triggers get broadened, and the failure surfaces only in a live session, sometimes in front of end users. Prose review does not catch behavioral regression.

## Decision

Every skill in this kit carries an `evals/` folder: scenarios with expected and forbidden behavior, one per step and one per boundary at minimum. Evals run when the skill changes. Behavior that used to work must keep working after an edit.

## Consequences

- Skills can be versioned and promoted between workspaces with their guarantees intact.
- Cost: writing evals roughly doubles the effort of shipping a skill. Accepted; the alternative is silent degradation in production sessions.
- Boundaries are first-class: what a skill must not do is tested as strictly as what it must do.
