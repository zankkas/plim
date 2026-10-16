# The Agent Definition Stack

Every artifact in this kit is also a part of an agent's definition. That is the quiet payoff of the layering: once a workspace runs this way, spawning a new agent is not a new problem. It is an instantiation.

## The mapping

| Agent part | Kit layer | Question it answers for the agent |
|---|---|---|
| Character | `SOUL.md` | Who is this agent? Voice, boundaries, values? |
| Principal | `PROFILE.md` | Who does it work for, and how does that human operate? |
| Mission | `directives/` | Which hard rules define the work it must do? |
| Scope | live tracker | What is it working on right now? |
| Expectations | `evals/` | What must its behavior never regress on? |
| Failure points | skills' boundaries + non-goals | What must it never do? |
| Judgment routing | SOUL decision routing | Which decisions are not its to make? |
| Schedule | hygiene cadence, runtime cron | When does it wake, audit, and report? |
| Memory | session notes, wiki | What survives its sessions? |

Two agents differ in character and mission. Two agents never differ in structure. That is what makes the second agent cheaper than the first, and the tenth cheaper than the second.

## Instantiating an agent

1. **Write the SOUL.** Character first: name, voice, boundaries. Borrow the section architecture, not the sentences.
2. **Write or point at the PROFILE.** The principal's traits, pitfalls, working model. Agents serving the same human share this.
3. **Assemble the mission.** Pick the directives that apply; write new ones only for duties no existing directive covers.
4. **Define the failure points before the first task.** Skills it will run get evals on day one, not after the first incident.
5. **Give it scope and a schedule.** A tracker surface it owns, and the passes it wakes for.
6. **Connect the body.** Whatever runtime hosts it (a chat client, a messaging channel, a cron loop) points at the same definition files. The runtime is the body; the stack is the person.

## What this is not

Not a claim that agents are interchangeable. Character is the differentiator, and the definition stack is what keeps the character stable across sessions, channels, and runtimes. Without the stack, every channel you add re-invents the agent and drifts.
