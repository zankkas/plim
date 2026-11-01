# The Clone Ritual

Every repo whose first user experience is an agent conversation wants the same shape: clone it, open your agent in the folder, one sentence, and the agent is doing the work. This pattern makes that ritual reachable — the shipped boot files do the discovery, not the model's curiosity.

## Why

Runtimes auto-read a root `AGENTS.md` when the agent opens in a folder. If that file does not exist in a fresh clone, the agent has nothing resident to tell it that a skill exists, so discovery depends on the model choosing to read `README.md`. The gap is not the skill's quality; it is that the skill is one hop away from the boot path.

## The three shipped files

1. **Root `AGENTS.md` gateway, marked `<!-- {{kit}}:gateway -->`.** Valid for the un-onboarded clone only, or persistent for support-side kits. It names the trigger phrase, points at the skill, and holds nothing else that could become a false authority.
2. **A pointer stub for other runtimes** (`CLAUDE.md` and equivalents): "Read `AGENTS.md` now and follow it." One line, zero governance content — the gateway stays the single authority.
3. **The skill itself, honest on its own:** eval cases in `evals/` (a skill edit without a recorded eval run does not ship), and a loader description inside the per-session budget (~260 bytes) so resident injection stays cheap.

## Consumed gateways vs persistent gateways

- **Consumed** (onboarding kits): the gateway exists only while `.agents/` is empty. The fill step *overwrites that same path* with the real workspace adapter, and refuses to touch a root boot file that does not carry the marker — onboarding can never clobber a boot file the human wrote. See [ADR-0004](../decisions/ADR-0004-gateway-is-shipped-and-onboarding-consumes-it.md).
- **Persistent** (support/facilitator kits: installers, rescue flows): no fill step exists, so the gateway stays. It keeps two facts resident: the lane split (what the agent builds vs what the human executes on the device) and the hard bounds that must hold *before* the full skill is read.

## The trigger phrase

Name it, mark it on the gateway, and define it by generalization: `**"{{kit}}, setup {{thing}}"** — or otherwise asks to set this up`. The phrase makes discovery exact; the generalization makes variants (onboard, initialize, "set it up") fire. Idempotence belongs on the gateway as a concrete check (`if the filled state exists, say it already happened and stop`), not as an abstract warning.

## Failure modes this pattern prevents

- A fresh clone whose agent boots into silence and asks the human what to do.
- The agent starting to hand-fill template files instead of running the skill's fill step.
- Manual placement instructions ("put the skill where your agent reads skills") — that is a first-session tax, not onboarding.
- Diagnosis-before-evidence: the persistent gateway states the evidence-first bound before the full skill loads.

## Proof of a good ritual

The user sentence is one sentence and mentions only clone, open, and the phrase. If the README's quickstart needs a numbered list to make the ritual work, the gateway is not thin enough yet.
