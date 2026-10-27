# Environment Plumbing Directive

**Status**: ACTIVE
**Purpose**: Define how agents in this workspace fix, wire, and verify the plumbing a runtime depends on — files jobs read, backends, credentials, fallbacks. Most plumbing failures are not code bugs; they are a consumer reading a path the producer never wrote, or a fallback silently doing the primary's job.

---

## Rule 1: Fix the path the consumer reads

Before creating or "fixing" a file a scheduled job, cron, boot adapter, or template references: **read the job's prompt / consumer config and get the EXACT path it opens.** Do not fix the path quoted in an issue, a ticket, or a previous agent's summary — those describe intent, not consumption.

- A near-duplicate path (`file.md` vs `file/template.md`) may already exist from an earlier interim fix. Two files that both claim to be the template is worse than one missing file: it guarantees a future agent renders the wrong one. Consolidate on one and delete the other in the same pass.
- When two versions of a definition conflict (template, persona, directive, config fragment), prefer the version already tracked upstream with a manifest/status header over a freshly rewritten one. It is the registered shape; the rewrite is usually an improvisation that lost the history.

**Completion criterion**: the consumer's next run reads the file without an error logged — not "the file exists somewhere plausible."

## Rule 2: Verify the primary, not the fallback

Any system with a fallback path (keyless search rescue, degraded model routing, cached config, stale snapshot) will return **success: true while the primary is silently dead**. A green result is not evidence the wiring works.

- When verifying a backend, credential, or integration: read the *warning/error channel* of the result, not just the success flag. If the result says "served by <fallback>", the primary is still broken.
- To verify the primary itself, cross-check an independent channel: the runtime's log line, the provider's own report, or a probe that can only succeed through the primary.
- Fallbacks are load-bearing and stay enabled. The rule is never "disable the fallback" — it is "never mistake the fallback firing for the primary working."

## Rule 3: Credentials are scoped to where they are read

Profiled / sandboxed / multi-tenant runtimes almost always isolate secrets **per profile**. A key pasted into a global store is invisible to every profile that needs it, and the failure looks like an auth error — or worse, like a fallback silently absorbing it (see Rule 2).

- Before declaring a key "wired", verify the *consuming process* resolves it: read the key env name from the consumer's own source (its `KEY_ENV` constant, its docs, its setup schema) — guessing the name fails at first call even when the value is correct.
- Write the key where the consumer reads it (the profile's own `.env` / secret store), with restrictive permissions, and verify via the consumer's log that the primary path fired.
- Never move, rename, or edit secrets in chat. If the operator must act (a rename in a file you cannot touch), state the exact one-line change and stop.

## Rule 4: Leave the plumbing documented at the point of failure

When a plumbing fix required investigation (a wrong slug, an inheritance gap, a masked fallback), record the trap **in the skill or directive that owns the workflow** — not in a session note nobody reads. The next agent to touch this surface must inherit the answer, not the archaeology.

- One rule per lesson, imperative form, in the skill that will load when the trap is near.
- If no skill owns it, this directive is the fallback home — add it here, and open a ticket to give it a real home.

---

## Priority Order

1. Safety boundary (never override)
2. Spec requirements
3. This directive
4. General best practices (fallback)
