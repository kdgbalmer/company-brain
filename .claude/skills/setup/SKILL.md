---
name: setup
description: Onboarding for this company brain, and redoing any part of it later. Use when the owner says "set me up", "onboard me", "carry on with setup", "redo my brand", "redo my voice", "redo my offers", "connect <tool>" (Gmail, Google Calendar, Google Drive, Notion, Canva, Stripe or any other), or "switch on <department>", or when business/profile.md is missing or its setup_stage is not done. Interviews one question at a time, connects tools, and ends with a first real piece of work.
---

# Setup

You are setting up this company brain for a small service business. The owner is busy and usually not technical. Talk like a helpful person sitting next to them: plain words, short messages, one question at a time, no jargon. Never make them feel they're filling in a form.

## Start here

1. Look for `business/profile.md`.
   - Missing: this is a fresh start. Go to [stage 1](stages/01-interview.md).
   - Present: read `setup_stage` in its frontmatter and pick up from the table below. Tell them in one line where you're picking up ("Last time we got through your offers and customers. Next up is your voice.").
2. If the owner asked for one specific thing ("redo my brand", "connect Stripe", "switch on finance"), skip the table and go to [Redo one part](#redo-one-part).

| `setup_stage` | What it means | Go to |
|---|---|---|
| `not-started` | Files may exist but nothing is filled in | [Stage 1: interview](stages/01-interview.md) |
| `interview` | Interview started, not finished | [Stage 1: interview](stages/01-interview.md), from the first topic that's still blank |
| `departments` | Interview done | [Stage 2: departments](stages/02-departments.md) |
| `tools` | Departments chosen | [Stage 3: tools](stages/03-tools.md) |
| `first-win` | Tools done | [Stage 4: first win](stages/04-first-win.md) |
| `extras` | First piece of work made | [Stage 5: extras](stages/05-extras.md) |
| `done` | Setup finished | Don't start again. Ask which part they'd like to redo (see below). |

After each stage, update `setup_stage` (and `last_updated`, as `YYYY-MM-DD`) in `business/profile.md` before moving on. That's what makes setup resumable: the owner can stop at any point and say "set me up" next time.

## Redo one part

If setup is `done` (or the owner asks for one thing mid-setup), run only that part. Don't change `setup_stage` unless the part you ran is the one setup was waiting on.

| The owner says… | Do this |
|---|---|
| "Set me up" when setup is already done | "You're already set up. Which part would you like to redo: your business details, offers, customers, voice, brand, goals, departments or tools?" |
| "Redo my brand / voice / offers / customers / goals" | Run just that topic from [stage 1](stages/01-interview.md) |
| "Change my business details" | Run the "business and type" topic from [stage 1](stages/01-interview.md) |
| "Switch on <department>" / "switch off <department>" | [Stage 2](stages/02-departments.md), that department only |
| "Connect <tool>" | [Stage 3](stages/03-tools.md), that tool only |
| "Show me what you can do" | The cheat-sheet at the end of [stage 5](stages/05-extras.md) |

## Files: create once, never overwrite

The repo ships with no business files. You create them from the blank templates in this skill, and only if they're missing.

| Template | Becomes | Created in |
|---|---|---|
| [templates/business/profile.md](templates/business/profile.md) | `business/profile.md` | Stage 1 |
| [templates/business/offers.md](templates/business/offers.md) | `business/offers.md` | Stage 1 |
| [templates/business/customers.md](templates/business/customers.md) | `business/customers.md` | Stage 1 |
| [templates/business/voice.md](templates/business/voice.md) | `business/voice.md` | Stage 1 |
| [templates/business/brand.md](templates/business/brand.md) | `business/brand.md` (plus an empty `business/brand-assets/` folder) | Stage 1 |
| [templates/business/goals.md](templates/business/goals.md) | `business/goals.md` | Stage 1 |
| [templates/business/tools.md](templates/business/tools.md) | `business/tools.md` | Stage 1 |
| [templates/business/rules.md](templates/business/rules.md) | `business/rules.md` | Stage 1 |
| [templates/memory/decisions.md](templates/memory/decisions.md) | `memory/decisions.md` (plus an empty `memory/log/` folder) | Stage 1 |
| (no template) | an empty `outputs/` folder | Stage 1 |
| [templates/department/context.md](templates/department/context.md) | `departments/<dept>/context.md` | Stage 2 |
| [templates/department/role.md](templates/department/role.md) | `departments/<dept>/role.md` (plus an empty `departments/<dept>/workflows/` folder) | Stage 2 |

Rules:

- **Only create a file if it doesn't exist.** If it exists, leave it and work inside it.
- **Never overwrite a filled file.** To change something that's already written, edit that one section in place. If the section already has an answer, show the owner the old and new wording side by side and wait for a yes before saving.
- **Write as you go.** Save each answer as soon as it's confirmed, so stopping halfway loses nothing.
- **"Skip" is always fine.** Write `TODO` in that field and keep a list of skipped items to mention at the end of the stage.
- **Never invent.** If you don't know a fact, ask or write `TODO`. Drafts from their website or documents are always shown for confirmation before they're saved as fact.
- **Keys never go in markdown.** Passwords, API keys and tokens only ever go in the `.env` file. Never repeat a key back in the chat.
- Keep the template's headings so every department can find things. Remove the `<!-- ... -->` hint comments once a section is filled.

## Business types

Each type has a file that says which departments to switch on first, the first workflows to try, a few extra interview questions, and the words that business uses:

- [Coach](business-types/coach.md): coaching, mentoring, training people one-to-one or in groups
- [Consultant](business-types/consultant.md): advice and expertise sold as projects or engagements to other businesses
- [Agency or freelancer](business-types/agency-freelancer.md): making things for clients (design, websites, video, copy, marketing, admin)
- [Local service](business-types/local-service.md): in-person services in a local area (trades, cleaning, beauty, fitness, pet care, repairs)

**Fits none of these?** Pick the closest one, tell the owner in one line ("You're closest to a coach, so I'll start from that and adjust"), set `business_type: other` in `business/profile.md`, and write the differences under "Things to know" in the profile (the words they use for their clients and their work, how they get paid, anything the closest type gets wrong). Use the closest type's file for everything else. If they need a workflow none of the departments has, note it and offer the **builder** skill once setup is finished.

## The stages

1. [Interview](stages/01-interview.md): who the business is (about 15 to 20 minutes)
2. [Departments](stages/02-departments.md): which parts of the business to switch on (2 minutes)
3. [Tools](stages/03-tools.md): connect email, calendar, files and so on (about 5 minutes per tool)
4. [First win](stages/04-first-win.md): make one real thing together (5 to 10 minutes)
5. [Extras](stages/05-extras.md): an optional weekly routine, then a "things you can ask me" list

## Approval still applies

Setup reads and writes the owner's business files freely. Anything that leaves the business (posting, sending, inviting other people, money, deleting outside `outputs/`) needs an explicit yes every time, exactly as in `CLAUDE.md`, even during the first win.
