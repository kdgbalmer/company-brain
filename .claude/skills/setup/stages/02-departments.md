# Stage 2: Departments

## Goal

Switch on the parts of the business the brain should look after now, and give each one a short context file and a role file. The rest stay off until the owner needs them. HQ is always on.

## The eight departments

Use these plain descriptions when you talk to the owner:

| Department | What it looks after |
|---|---|
| `hq` | Your priorities, today's plan, weekly review, goals and decisions. Always on. |
| `marketing` | Posts, content, newsletters, website words, graphics, freebies |
| `sales` | Enquiries, follow-ups, discovery calls, proposals, who's in the pipeline |
| `delivery` | Looking after clients once they've bought: onboarding, sessions or projects, follow-ups, testimonials |
| `offers` | Creating or changing what you sell, pricing, launches, sales pages |
| `finance` | Invoices, expenses, money in and out, monthly numbers |
| `operations` | Inbox, calendar, step-by-step processes, tools and admin |
| `team` | Roles and handovers, for people or AI helpers |

## What to say first

Don't send an intro and then a separate suggestion. Work out the suggestion first (steps 1 and 2), then say it all in **one message** that ends with one question, using the owner's words (clients or customers). For example:

> Next: which parts of your business I should look after. There are eight. I'd start with HQ, Marketing, Sales and Delivery: that covers getting clients in and looking after them. Offers, Finance, Operations and Team stay off for now, and you can switch any of them on later by saying "switch on finance". Sound right?

## Steps

1. **Read** `business/profile.md` (especially `business_type`), `business/offers.md`, `business/goals.md`, and the "Switch on first" list in the matching business-type file ([coach](../business-types/coach.md), [consultant](../business-types/consultant.md), [agency or freelancer](../business-types/agency-freelancer.md), [local service](../business-types/local-service.md)).
2. **Build the suggestion.** Start from the type file's list. `hq` is always in. Then adjust from their answers:
   - A goal about launching, a new offer or a price change → add `offers`.
   - A goal about money, or they mentioned chasing invoices → add `finance`.
   - They mentioned a busy inbox, a messy calendar or lots of admin → add `operations`.
   - They have staff, contractors or an assistant, or want to hand work over → add `team`.
   - Keep the starting set to about four or five. Too many at once is overwhelming.
3. **Propose it in that one message** (see "What to say first"): one plain line per department saying why, name the ones staying off, and end with one question.
4. **Wait for a yes or changes.** If they want everything on, that's fine.
5. **Create the folders** for each active department, only for files that don't exist yet:
   - `departments/<dept>/context.md` from [the context template](../templates/department/context.md). Replace `[Department]` with the department's name. Fill in:
     - "What this department does for this business": two or three lines specific to them (from the interview).
     - "What it needs to know": the facts from `business/` this department will use most (for sales: how people enquire and book, the booking link; for delivery: how sessions or projects run; for marketing: which platforms they're on). Keep it short; don't copy whole files.
     - "Workflows we use most": the workflows the business-type file suggests for this department.
     - Leave "Custom workflows" and "Corrections learned" as they are.
   - `departments/<dept>/role.md` from [the role template](../templates/department/role.md). Replace `[Department]`. Fill in:
     - Owned by: the owner's name from `business/profile.md`.
     - Goal: one line, tied to their goals where possible.
     - Responsible for: a short list in their vocabulary.
     - Hands over to: the departments it passes work to (for example sales hands over to delivery when someone buys).
   - An empty `departments/<dept>/workflows/` folder. Their own versions of workflows go here later.
6. **Update** `active_departments` in the frontmatter of `business/profile.md` (for example `[hq, marketing, sales, delivery]`).
7. **Tell them in one line** what you created: "Done. Each one has a short notes file you can read in the `departments` folder."

## Switching one department on or off later

- **"Switch on <dept>":** create just that department as in step 5, add it to `active_departments`, and ask one or two questions if its context file would otherwise be thin (for finance: "How do you invoice now, and what are your payment terms?"; for team: "Who helps you at the moment?"). Then tell them two or three things they can now ask for.
- **"Switch off <dept>":** remove it from `active_departments` and say "I've switched it off. Its notes are still in the folder if you switch it back on." Never delete the folder.
- Don't change `setup_stage` when doing either of these after setup is finished.

## What to write where

| What | Where |
|---|---|
| Active list | `active_departments` in `business/profile.md` frontmatter |
| Department notes | `departments/<dept>/context.md` |
| Who owns it | `departments/<dept>/role.md` |
| Their own workflows (later) | `departments/<dept>/workflows/` |

Departments that are off get no folder.

## How to finish

1. Set `setup_stage: tools` and `last_updated` in `business/profile.md`.
2. Ask: "Next, your tools: email, calendar, files and so on. Connecting them means I can read your inbox or diary when you ask. Shall we do that now?" If yes, go to [stage 3](03-tools.md). If they'd rather not connect anything, go there anyway: stage 3 just records what they use.
