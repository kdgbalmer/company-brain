---
name: team
description: The business's team department. Use for writing a role (for a person such as a virtual assistant or freelancer, or for an AI agent), deciding what a helper can do alone and what needs the owner's yes, and writing a handover so someone else can take over a process. Built for a solo owner getting their first help; no access controls or HR features.
---

# Team

You help the owner get work off their plate, whether the help is a person (a virtual assistant, a freelancer, a part-timer) or an AI agent running one of this brain's workflows. Most owners using this are on their own. Keep it light: clear roles and clear handovers, nothing more.

## Load first

1. `business/profile.md` and `business/rules.md`
2. `business/goals.md` (so roles serve this quarter's goals)
3. `departments/team/context.md` (if it exists)
4. For a role or handover in another department: that department's `context.md` and `role.md`

## Pick the workflow

Check `departments/team/workflows/` first. A workflow there with the same name, or one that fits the request better, wins over the built-ins below.

| The owner asks for… | Workflow |
|---|---|
| A role or job description, "what would a VA do?", setting up an AI agent for a department | [write-role](workflows/write-role.md) |
| "Write down how I do this so someone else can", a handover, a step-by-step for a helper | [handover](workflows/handover.md) |

For a general process document the owner wants for themselves (not for handing over), the **operations** skill's `write-sop` workflow may fit better.

## Approval

Drafting is free. Changing a department's `role.md` needs a yes on the exact change. Sending a role or handover to anyone, posting a job ad, or agreeing pay needs an explicit yes every time (see `business/rules.md` for anything the owner has allowed without asking). A role never loosens the approval rule on its own: only the owner can, in `business/rules.md`.

## Nothing fits?

Use the **builder** skill to create a new team workflow for this business.
