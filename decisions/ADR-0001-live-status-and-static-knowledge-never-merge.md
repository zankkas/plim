# ADR-0001: Live status and static knowledge never merge

**Status**: Accepted (2026-10-16)
**Review**: revisit if a runtime emerges where the tracker and the files share one storage model

## Context

Agents mirror status into static files because static files are what they can read at boot. The copies contradict the live source within days, and every session then trusts a lying authority.

## Decision

Two kinds of truth, two homes. The live tracker owns current status. Static files own orientation, decisions, and verified knowledge. They never merge, and a tracker that cannot be reached is reported as unverified rather than reconstructed from local copies.

## Consequences

- Sessions that start offline lose status, not correctness: the agent says so.
- Hygiene audits authority drift every pass.
- Cost: one extra step in every close (reconcile the tracker instead of writing a status file). Accepted; the alternative cost is silent lies.
