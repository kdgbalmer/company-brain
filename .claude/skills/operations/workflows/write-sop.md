# Write an SOP

## Purpose

Get a task the owner repeats out of their head and into a clear, step-by-step document that someone else (a new hire, a freelancer, an AI agent, or the owner on a tired day) could follow and get the same result.

## Use when

The owner says: "write down how I onboard a new client", "make a checklist for sending the monthly report", "I want to hand off booking calls, write the process", or a task keeps coming up that only they know how to do.

## Load first

- `departments/operations/context.md`
- `departments/operations/sops/` (to avoid writing a duplicate, and to match the style of existing ones)
- `business/tools.md` (the tools the task uses)
- The department `context.md` the task belongs to, if it isn't operations

## Steps

1. **Name the task.** Confirm in one line what the SOP covers and give it a short name, e.g. `client-onboarding`. If an SOP with that name exists in `departments/operations/sops/`, offer to update it instead.
2. **Interview the owner, one question at a time.** Stop as soon as you have enough. Typical questions:
   - What starts this task? (an email arrives, a date, a new client signs)
   - Walk me through what you do, step by step, the last time you did it.
   - Which tools, files or templates do you use at each step?
   - What does "done right" look like?
   - Where does it usually go wrong, or what do people forget?
   - Who should do it in future, and what can they decide without asking you?
   If the owner pastes notes, a screen recording transcript or an old checklist, work from that and only ask about the gaps.
3. **Write the SOP** in this shape:
   - **What it's for** (one line) and **who does it**
   - **When it starts** (the trigger) and **how long it takes**
   - **What you need** (tools, logins named but never written down, templates)
   - **Steps:** numbered, one action each, starting with a verb, with the tool named
   - **Done means:** the checks that prove it's finished
   - **Watch out for:** the common mistakes
   - **Ask the owner before:** any decision the doer can't make alone
4. **Read it back.** Show it in the chat and ask: "Could someone new follow this without calling you?" Fix what the owner flags.
5. **Save it** and add it to a "SOPs" list in `departments/operations/context.md` (name, one-line description, date).

## Check before handing over

- Every step is one action a newcomer could do. No "sort out the usual stuff".
- Tools are named; no passwords, API keys or login details anywhere in the file.
- Nothing invented: every step came from the owner or their notes.
- The approval rule still applies inside the SOP: steps that send, post, invite or touch money say "get a yes from the owner" unless `rules.md` allows it.

## Save to

`departments/operations/sops/<name>.md` (create the `sops/` folder if it doesn't exist). Show the SOP in the chat as well.

## Needs a yes

Nothing for writing it. Sharing or sending the SOP to anyone (a team member, a freelancer) needs a yes, showing who it goes to and how.
