# SETUP — for the agent, not the human

You have been handed this file. The human wants a Plim workspace, and they
should not have to read anything else to get one.

1. **Get the kit.** Clone `https://github.com/zankkas/plim` into a directory the
   human chooses. If you cannot run commands, ask them for the folder and read
   the files from it.
2. **Read `skills/onboard/SKILL.md` and follow it.** It asks the human a few
   plain questions, fills the templates itself, and replaces the shipped
   `AGENTS.md` with their workspace adapter. The human edits no files.
3. **Run the doctor.** `python3 scripts/doctor.py`. Show its output verbatim.
   Until it prints `no drift found`, do not tell the human the workspace is set
   up.
4. **Stop.** Report what exists now, and the one ritual they repeat: boot the
   adapter, capture decisions as they land, close with the close-session skill.

Do not invent work, status, or habits. A fresh clone has no history, and the
human is the only source of both.
