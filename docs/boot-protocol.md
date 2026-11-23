# The boot protocol (two hops)

Boot is a thin adapter, not a data dump.

1. **First hop:** the agent reads the adapter file (`AGENTS.md` at the repo
   root, or your runtime's equivalent). It points at the identity, profile, and
   compass files and at the live status source.
2. **Second hop:** the agent reads those files, then renders a short brief:
   decisions needed, ready work, blocked work, unverified state.

The adapter stays tiny. It changes only when the map changes. All real content
lives one hop away, in files the agent can also read mid-session. Keep the
adapter and its targets identical across every client that boots into the
workspace.

Boot is also a cost decision. Fetch the live status once, in one composed call,
and reuse it for the session. Re-querying the tracker on every turn burns
context and returns the same answer twice.

See [ADR-0004](../decisions/ADR-0004-gateway-is-shipped-and-onboarding-consumes-it.md)
for why the clone ships a gateway at all, and
[the clone ritual](../patterns/the-clone-ritual.md) for the pattern generalized
beyond onboarding.
