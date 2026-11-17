# Stage 4: First win

## Goal

Make one real, finished piece of work for the business, using everything captured so far, so the owner sees straight away that the brain sounds like them and knows their business. Then learn from their corrections.

## What to say first

Suggest one thing, based on their goals, and give one alternative:

> Your first goal is more enquiries, so let's write a post you could put up this week about [their main offer]. Or, if you'd rather, I can draft a follow-up to someone who's been in touch. Which one?

## Steps

1. **Pick the workflow.** Read `business/goals.md` and the "First workflows to try" list in their business-type file ([coach](../business-types/coach.md), [consultant](../business-types/consultant.md), [agency or freelancer](../business-types/agency-freelancer.md), [local service](../business-types/local-service.md)). Match their top goal:

   | Their top goal is about… | First win | Workflow |
   |---|---|---|
   | More enquiries, visibility, growing an audience | A post for their main platform | marketing: [social-post](../../marketing/workflows/social-post.md) |
   | Converting people who are already interested | A follow-up to a real lead | sales: `lead-follow-up` |
   | Winning bigger projects or engagements | A proposal from recent call notes | sales: `call-to-proposal` |
   | Keeping clients happy, getting referrals or reviews | A testimonial or review request | delivery: `testimonial-request` |
   | Launching or changing an offer | A sharper version of one offer | offers: `design-offer` |
   | Feeling on top of things, time, focus | A plan for this week | hq: `today` or operations: `plan-week` |
   | Unclear, skipped, or nothing fits | A post for their main platform | marketing: [social-post](../../marketing/workflows/social-post.md) |

   Built-in workflows live in `.claude/skills/<department>/workflows/<name>.md`. Use the owner's own version in `departments/<department>/workflows/` if one exists.
2. **Make sure the department is on.** If it isn't in `active_departments`, say "That's a Sales job, which isn't switched on yet. Switch it on?" and, on a yes, set it up as in [stage 2](02-departments.md). If they say no, pick another first win from an active department.
3. **Run the workflow fully**, exactly as its file says: its "Load first" list, every step, and its quality check. Use the real details from `business/` (an actual offer, their customers' own words, their voice samples, their brand colours). Ask only the questions the workflow needs, one at a time. If a fact you need was skipped (`TODO`), ask for it now rather than inventing it.
4. **Save it** where the workflow's "Save to" section says, under `outputs/<department>/` as `YYYY-MM-DD-<short-name>.md`. Show the finished piece in the chat as well.
5. **Ask what they'd change:** "What would you change? Even small things: a word you'd never use, too formal, too long." Make the changes and show the new version.
6. **Save what you learned**, following the "Learning from corrections" rule in `CLAUDE.md`:
   - Tone or words ("too formal", "I never say 'journey'") → one line under "Corrections learned" in `business/voice.md`, with today's date.
   - Anything specific to the department ("always add my booking link") → one line under "Corrections learned" in `departments/<department>/context.md`, with today's date.
   - Tell them in one line what you saved: "Saved: no exclamation marks. I'll remember that for everything."
   - Two rounds of changes is usually plenty. If they're happy, stop.
7. **If they want to use it now** (post it, send it): that needs an explicit yes. Show exactly what will be posted or sent, where, to whom and when, and wait. If the tool isn't connected, tell them it's ready to copy and paste.

## What to write where

| What | Where |
|---|---|
| The finished piece | `outputs/<department>/YYYY-MM-DD-<short-name>.md` (or as the workflow says) |
| Tone and word corrections | `business/voice.md`, "Corrections learned" |
| Department-specific corrections | `departments/<department>/context.md`, "Corrections learned" |
| Any decision they make along the way | `memory/decisions.md`, with the date |

## How to finish

1. One line on what was made and where it's saved.
2. Set `setup_stage: extras` and `last_updated` in `business/profile.md`.
3. Say: "That's the main setup done. One last optional thing, then I'll show you what you can ask me." Go to [stage 5](05-extras.md).
