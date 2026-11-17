# Stage 5: Extras

## Goal

Offer one optional weekly routine (never switch it on without a clear yes), mark setup as finished, and leave the owner with a short list of things they can ask for, tailored to the departments they've switched on.

## What to say first

Offer the routine that fits them best: the weekly review if `hq` is their main need, or a content batch if `marketing` is on and their goals are about visibility. Offer one, mention the other:

> One optional extra. I can do a weekly review every Monday: what got done last week, how you're doing against your goals, and the three things that matter most this week. Or a weekly batch of posts for you to approve. Would you like either? It's fine to say no.

## Steps

1. **Wait for their answer.** No is a fine answer: skip to "How to finish".
2. **If yes, explain the two ways to run it**, in plain words:
   - **Just ask.** Open this folder in Claude Code each Monday and say "weekly review" (or "this week's posts"). Nothing to set up.
   - **Let it run on a schedule.** In the Claude desktop app, open the scheduled tasks section, create a new task, choose this folder, set it to repeat weekly (for example Monday at 8am) and use this as the instruction:
     - Weekly review: `Run my weekly review and save it to outputs/hq.`
     - Content batch: `Draft this week's posts and save them to outputs/marketing. Don't post anything.`

     It runs on their own computer, so the computer needs to be on at that time. They set it up themselves; you can talk them through it one step at a time if they'd like.
3. **Make the approval point clear:** "A scheduled run only drafts. It never posts, sends or books anything; those still wait for your yes."
4. **Record the choice** in `memory/decisions.md` with today's date (for example "Weekly review every Monday, owner scheduling it in the desktop app"). If they said no, record nothing.
5. **Set up the department it needs.** The weekly review uses `hq`; the content batch uses `marketing`. If that department isn't on, switch it on as in [stage 2](02-departments.md) after asking.

## What to write where

| What | Where |
|---|---|
| Setup finished | `setup_stage: done` and `last_updated` in `business/profile.md` |
| Routine they chose (if any) | `memory/decisions.md` |
| Session summary | `memory/log/YYYY-MM-DD.md` |

## How to finish

1. Set `setup_stage: done` and `last_updated` in `business/profile.md`.
2. Append three to five lines to `memory/log/YYYY-MM-DD.md`: setup finished, departments switched on, tools connected, the first piece made (with its file path), and anything still marked `TODO`.
3. Show the cheat-sheet below. Include **HQ** and the **Setup** lines always, and only the sections for departments in `active_departments`. Use the business's own words from its type file (bookings, sessions, engagements, briefs) and, where you can, their real offer names and platforms instead of the generic examples. Keep it short.
4. End with one line: "That's it. Just tell me what you need in plain words, and I'll work out the rest."

## The cheat-sheet

**Things you can ask me**

**HQ**
- "What should I work on today?"
- "Run my weekly review."
- "Set my goals for next quarter."
- "Note down a decision: we're dropping the monthly plan."

**Marketing**
- "Write an Instagram post about [offer]."
- "Plan next week's content."
- "Turn this voice note into a LinkedIn post and a newsletter."
- "Make a graphic for this quote."

**Sales**
- "Follow up with the person who enquired on Tuesday."
- "Help me prepare for my discovery call tomorrow."
- "Turn these call notes into a proposal."
- "Who should I chase this week?"

**Delivery**
- "Onboard my new client."
- "Prep for my session with [client] on Thursday."
- "Turn these notes into a follow-up email."
- "Ask [client] for a testimonial."

**Offers**
- "Help me design a new offer."
- "Am I charging enough for [offer]?"
- "Plan the launch of [offer]."
- "Write the sales page for [offer]."

**Finance**
- "Draft an invoice for [client]."
- "How did last month go, money-wise?"
- "Log these expenses."
- "Will I have enough cash next month?"

**Operations**
- "Sort my inbox."
- "Plan my week in the calendar."
- "Write a step-by-step process for how I onboard clients."
- "Which tools am I paying for that I don't use?"

**Team**
- "Write a role for a part-time assistant."
- "Write a handover so someone can cover while I'm away."

**Setup and changes**
- "Redo my brand." (or voice, offers, customers, goals)
- "Connect Stripe." (or any tool)
- "Switch on finance." (or any department)
- "Make a new workflow for [something I do often]."
