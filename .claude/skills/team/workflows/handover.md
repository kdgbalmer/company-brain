# Handover

## Purpose

Write down one process the owner does, step by step, so someone else (a person or an AI agent) can do it the same way without asking.

## Use when

The owner says "write down how I do this so my VA can take it over", "hand over my invoicing", "I want an agent to do my weekly newsletter", "I'm going on holiday, who covers what?", or a role from [write-role](write-role.md) lists a job with no instructions yet.

## Load first

- `business/rules.md` (what always needs a yes)
- The department's `departments/<dept>/context.md` (if the process belongs to one)
- Any existing workflow for this job in `departments/<dept>/workflows/` or `.claude/skills/<dept>/workflows/`
- The role it's going to, in `departments/<dept>/role.md` or `departments/team/roles/` (if one exists)
- `business/tools.md` (which tools the process uses)

## Steps

1. **Pin the process.** Agree the one job being handed over, who it's going to (a person or an AI agent) and how often it happens. If there's already a workflow for it, say so: the handover can point to it and only add what's specific to this business.
2. **Walk it through.** Ask the owner to talk you through the last time they did it, start to finish. Ask one question at a time: "What do you open first?", "Then what?", "How do you know it's done?". Write what they actually do, not what they think they should do.
3. **Capture the details.** For each step note: the tool used, where files live, any template or wording they reuse, and how long it takes. Never write passwords, keys or login details into the file. Write "the owner gives you access to <tool>" instead.
4. **Mark the decisions.** Flag each point where a judgement is made ("if the client is late paying, I…"). For each, write the rule the owner uses. If they say "it depends", ask for two examples and write the rule from those.
5. **Mark the yes points.** Every step that posts, publishes, sends, invites others, touches money or deletes outside `outputs/` gets a clear "Stop: get the owner's yes" line, unless `business/rules.md` loosens it for that action.
6. **What good looks like.** Describe the finished result, with an example if there's a past one in `outputs/`. Add the two or three mistakes the owner most wants avoided.
7. **When things go wrong.** What to do if a tool is down, a client replies with something unexpected, or a step doesn't apply. Default: stop and ask the owner.
8. **Show the handover** and ask the owner to read it as if they were the new person. Fix anything they'd still need to ask about.
9. **Offer a trial run.** Suggest the next time this job comes up, the new person or agent does it from the handover while the owner checks it.

## Check before handing over

- Someone with no background could follow it start to finish without asking a question.
- Every step that needs a yes is marked, and nothing loosens `business/rules.md`.
- No passwords, keys, tokens or private client details in the file.
- It describes what the owner actually does, in their words, not a generic version.

## Save to

`departments/<dept>/handovers/<process-name>.md` if it belongs to a department, otherwise `departments/team/handovers/<process-name>.md` (create the folders if needed). If the role file exists, add a link to the handover under "Workflows they run". If the owner wants it to become a reusable workflow the brain runs itself, offer the **builder** skill.

## Needs a yes

Sending the handover to anyone or sharing it outside this folder: show exactly what goes to whom and wait for a yes. Changing an existing role file to link it: show the change first.
