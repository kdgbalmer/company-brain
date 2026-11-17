# Pipeline review

## Purpose

Give the owner a quick, honest view of every open lead, flag the ones going cold, and propose the three most valuable next actions so they know exactly who to contact today.

## Use when

The owner asks who to chase or how sales are looking: "who should I follow up with?", "pipeline check", "how's sales this week?", "anything slipping through the cracks?". Also useful as part of a weekly review.

## Load first

- `departments/sales/pipeline.md`, or the connected CRM listed in `business/tools.md`
- `business/offers.md` (to fill in missing values)
- `business/goals.md` (sales targets, if any)
- `departments/sales/context.md`

## Steps

1. **Read the pipeline.** Every row that isn't `won` or `lost`. If the pipeline is empty or missing, say so and offer to build it (create `departments/sales/pipeline.md` with the header row given in the sales skill): ask the owner to list the people they're talking to, one line each, and add them.
2. **Fill gaps.** If a row has no value but the offer is known, fill it from `offers.md`. If a row has no next step or date, flag it rather than guessing.
3. **Flag stale leads.** A lead is stale if its next-step date has passed, or nothing has happened for more than 7 days at `new` or `contacted`, more than 2 days at `call done, proposal not sent`, or more than 10 days at `proposal sent`. Use the owner's own thresholds if `departments/sales/context.md` has them.
4. **Total it up.** Number of open leads by stage, and the total value at `call booked`, `call done, proposal not sent` and `proposal sent`. Compare with `goals.md` if there's a sales target.
5. **Pick the three most valuable next actions.** Rank by value, how close they are to a yes, and how overdue they are. For each: who, what to do (one action), and why now. For example: "Chase Tom (proposal sent 12 days ago, worth the 6-month package). Send a short check-in."
6. **Suggest clean-up.** Leads with three unanswered follow-ups: suggest moving them to `lost`. Leads with no next step: suggest one. Don't change stages to `won` or `lost` without the owner saying so.
7. **Offer to draft.** Offer to run `lead-follow-up` for any of the three actions.

## Check before handing over

- Every lead in the summary is really in the pipeline. Nothing invented.
- Values match the prices in `offers.md` or what's in the pipeline.
- Exactly three next actions, each one specific and doable today.
- Short enough to read in a minute: the three actions first, the detail below.

## Save to

`outputs/sales/YYYY-MM-DD-pipeline-review.md`, containing the three actions, the stale-lead list, the stage totals and suggested clean-up. Show the three actions in the chat. Apply any pipeline changes the owner agrees to in `departments/sales/pipeline.md` (or the CRM).

## Needs a yes

Sending any follow-up, and marking a lead `won` or `lost`. Nothing is sent from this workflow on its own; any message goes through `lead-follow-up` and its own yes.
