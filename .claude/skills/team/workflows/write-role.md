# Write a role

## Purpose

Write one clear role, for a person or an AI agent: what they own, what they can decide alone, what needs the owner's yes, which workflows they run and how they report back.

## Use when

The owner says "I want to hire a VA, what would they do?", "write a job description for a freelance designer", "set up an AI agent to run my marketing", "who owns sales?", or wants to hand a department to someone else.

## Load first

- `business/profile.md` and `business/goals.md`
- `business/rules.md` (what always needs a yes, and anything the owner has loosened)
- The department's `departments/<dept>/context.md` and `departments/<dept>/role.md` (if the role covers a department)
- The workflows that department uses: the built-ins in `.claude/skills/<dept>/workflows/` and any in `departments/<dept>/workflows/`
- `departments/team/context.md` (if it exists)

## Steps

1. **Pin the brief.** You need: who will do it (a person or an AI agent), which department or area it covers, and roughly how much time it has (hours a week for a person; which jobs for an agent). Ask one question at a time for anything missing.
2. **Goal.** One or two lines on what good looks like, tied to a goal in `goals.md` where possible ("every enquiry gets a reply within one working day").
3. **Responsibilities.** List the jobs they own, as specific tasks ("draft three social posts a week", "chase unpaid invoices on Fridays"). Five to eight items at most. Ask the owner which of their own weekly jobs they most want to let go of.
4. **Decisions they can make alone.** List what they can decide without asking (which day to post, how to word a reply in the house voice, how to file things). Keep it to things that are easy to undo.
5. **What needs the owner's yes.** Start from `business/rules.md`: anything that posts, publishes, sends, invites others, touches money or deletes outside `outputs/` needs a yes unless the owner has loosened it there. Add anything else the owner wants to keep (a new client, a price, a refund, anything said on their behalf in public).
6. **Workflows they run.** List the workflows by name, with where each lives. For an AI agent, these are the workflows it should follow; for a person, these are the step-by-steps they can read.
7. **How they report.** Agree when and how: a daily or weekly note, where it goes (a line in `memory/log/`, a short message, a file in `outputs/`), and what it covers (done, waiting, needs a decision).
8. **Hands over to.** Which other departments or people they pass work to.
9. **Person or agent differences.** For a person, add: hours, how they're paid (ask the owner; never suggest a rate as fact), and what they need access to (in plain words, for the owner to set up). For an AI agent, add: which tools it can use from `business/tools.md` and the line "Follows the approval rule in `CLAUDE.md`; asks the owner before any action that needs a yes."
10. **Show the full role** and ask where to save it.

The role file keeps the same top block as every department's `role.md` (Owned by, Goal, Responsible for, Reports to, Needs a yes for, Hands over to), with "Owned by" set to the person's name, "AI agent", or the owner. Below it, add five short sections with these headings: Responsibilities, Decisions they can make alone, Needs the owner's yes, Workflows they run, How they report.

## Check before handing over

- Every responsibility is a task someone could start on day one.
- "Needs the owner's yes" includes everything in `business/rules.md` and never loosens it. Only the owner can loosen a rule, in `business/rules.md`.
- Every workflow listed actually exists.
- No pay, hours or names invented; they came from the owner. Example names are only placeholders the owner replaces.
- Plain words. No HR jargon.

## Save to

- If the role takes over a whole department: `departments/<dept>/role.md`. Show the old and new versions first and update after a yes.
- Otherwise: `departments/team/roles/<role-name>.md` (create the folders if needed).

Add a line to `departments/team/context.md` listing the role and where it's saved.

## Needs a yes

Changing a department's `role.md`: show the exact change first. Sending the role to anyone, posting it as a job ad, or agreeing pay needs an explicit yes, showing exactly what goes where.
