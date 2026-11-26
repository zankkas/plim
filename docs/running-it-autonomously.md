# Running it autonomously

Plim describes the rules a runner has to honour. It does not ship a runner.

The kit was extracted from a workspace that runs a fleet every day, but the
engine — scheduler, queue, model routing, dashboard, alerting — is deliberately
not here. That layer has to match your tracker, your budget, and your
infrastructure. Shipping one would make the kit a product with a maintenance
surface it cannot test.

What the kit does give you is the contract. Any runner that claims to work with
Plim has to satisfy these five, and each one is checkable.

## The five contracts

1. **One live source of status.** The runner reads what is active from the
   tracker, once per session, and reports state as *unverified* when the tracker
   cannot be reached. It never reconstructs status from memory, a cache, or a
   generated dashboard. (ADR-0001)

2. **Evals gate the change.** A skill edit ships only with a recorded eval pass.
   The runner runs them; a human does not have to remember to. (ADR-0003)

3. **A decision is written when it is made.** The runner captures it in the
   session note at the moment it lands, not in an end-of-run summary. A decision
   that exists only in the run's transcript is lost to the next run. (ADR-0002)

4. **Irreversible actions wait for a person.** Publish, deploy, delete, send,
   pay: the runner prepares, shows the plan, and stops. Dry run is the default;
   the human performs the destructive step.

5. **A wake means new work, not new text.** A comment, a label, or an edit to an
   issue is not evidence that nobody is on it. A runner that treats every
   mutation as fresh work will duplicate runs, and the duplicates park as
   decisions nobody needed to make. This one is here because it was learned the
   expensive way.

## What the runner has to provide

The kit names these as yours to choose:

- **A scheduler and a queue** with retries, so a crashed run is visible rather
  than silently lost.
- **A budget ceiling per job**, so one bad run cannot spend a month.
- **An approval surface** a person can reach without reading a transcript.
- **An audit trail** that answers "why did this happen?" a week later.
- **One kill switch.** If stopping everything takes two steps, it will not be
  used.

`patterns/agent-definition-stack.md` maps the layers a runner instantiates, from
character to schedule.

## How to test a runner against the kit

Ask these five, in order. A "no" anywhere means the runner is using the kit as
decoration.

1. Kill the network and start a run. Does it say *unverified*, or does it
   reconstruct status?
2. Change a skill without running evals. Does the change ship?
3. Ask what was decided last week. Is the answer in a note, or in the model's
   recollection?
4. Point it at something irreversible. Does it stop, or does it proceed because
   the plan looked good?
5. Touch an issue with a comment. Does it start another run?

## What it looks like when the contract is ignored

- Two authorities on status, disagreeing, and nobody able to tell which is live.
- A skill that works in April and quietly stops working in June.
- The same decision made three times across three sessions, differently.
- An agent that approves its own deployment because the request sounded routine.
- Three parked runs of one brief, and a board full of questions nobody asked.

## Where this kit stops

At the contract. If you already run an agent loop, these five sentences are what
to audit it against. If you do not, the files in this repo are still the thing to
copy first: they are what the loop will be judged by once it exists.
