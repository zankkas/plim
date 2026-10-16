# Skill Anatomy

A skill is a procedure an agent loads when it becomes relevant. The skill must earn its load: small at the entry point, deep where needed, provable over time.

## The shape

```
skills/{{skill-name}}/
├── SKILL.md          # the entry point: trigger, why, steps. One screen.
├── references/       # depth on demand: examples, tables, long detail
└── evals/            # the cases that prove the skill still works
```

## SKILL.md: the center

The file the agent actually reads. It carries:

- **Trigger**: when this skill applies, in one or two lines. This line lives in the runtime's permanent hint layer, so it must name the moment, not the theory.
- **Why**: the reason the procedure exists, so the agent can improvise correctly when reality does not match the steps.
- **Steps**: short, imperative, in execution order.
- **Non-goals**: what this skill deliberately does not do. Boundaries prevent skill creep.
- **Completion criterion**: how the agent knows it is done.

Everything else moves to `references/`. A skill that needs ten screens to start is two skills, or one skill and a reference.

## references/: depth on demand

Detail the agent needs only sometimes: worked examples, edge-case tables, background theory. The entry point points to them at the exact step where they matter. This keeps the hint layer cheap and the loaded context small.

## evals/: the stability layer

Skills drift. Steps get edited, triggers get broadened, and nobody notices until the skill fails in a live session. Evals are the fix:

- A list of scenarios with expected behavior: what the agent should do, what it must not do.
- One eval per step and one per boundary, minimum.
- Run them when the skill changes, and when a session surfaces behavior the skill did not anticipate.

Evals are also the promotion path: a skill that passes its evals can move between workspaces and runtimes with its guarantees intact.

## The test of a good skill

A fresh agent, one session in, finds the skill by trigger alone, executes it from the entry point alone, and checks itself against the completion criterion. If it needs the reference to survive the happy path, the split is wrong.
