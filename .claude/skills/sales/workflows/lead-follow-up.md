# Lead follow-up

## Purpose

Write the next message to one lead, in the owner's voice, that moves them one step closer to a call or a yes, and log the lead in the pipeline so they're never forgotten.

## Use when

A new enquiry comes in, or a lead has gone quiet: "reply to the woman who filled in my contact form", "follow up with the lead from Tuesday", "chase Sam about the quote I sent", "someone DM'd asking about prices".

## Load first

- `business/voice.md` (tone rules, samples, corrections)
- `business/offers.md` (the offer they asked about, its price and how to book)
- `business/customers.md` (who is a fit, why people hesitate)
- `business/tools.md` (inbox, calendar or CRM connected?)
- `departments/sales/pipeline.md` or the connected CRM
- `departments/sales/context.md`

## Steps

1. **Find the lead.** Look them up in the pipeline (or CRM). If they're not there, add a row: name, where they came from, stage `new`. If an inbox is connected, read their message and any earlier replies. If not, ask the owner to paste what the lead said. Don't guess at what they asked.
2. **Work out where they are.** New enquiry, waiting on a call, waiting on a proposal, or gone quiet? How long since the last contact? Note which offer they're probably interested in. If it isn't clear, the message's job is to find out.
3. **Pick one next step.** Usually one of: book a call, answer their question, send the details of the offer, or check whether it's still a good time. Only one per message.
4. **Draft the message.** Short, warm, and specific to what they said, in the owner's voice. Answer their actual question first. Use the booking link or process from `offers.md` if it's there. If they asked about price and `offers.md` has it, give it plainly. If it doesn't, ask the owner and don't make one up. For a lead who's gone quiet, make it easy to reply ("Is this still on your list, or shall I close the file for now?") and never guilt-trip.
5. **Plan the next touch.** Suggest when to follow up if there's no reply (for example 3 days for a new enquiry, a week after a proposal). Stop after three unanswered follow-ups and suggest moving them to `lost`.
6. **Update the pipeline.** Set the stage, the next step and its date. Fill in value from `offers.md` if you know the offer.

## Check before handing over

- Does it answer what the lead actually asked?
- Exactly one next step, and is it easy to say yes to?
- Every price, link and detail comes from `offers.md`. No invented results, discounts or deadlines.
- It sounds like the samples in `voice.md`, not like a sales template.
- The pipeline row is updated.

## Save to

`outputs/sales/YYYY-MM-DD-follow-up-<lead-name>.md`, containing the message and the suggested next follow-up date. Show the message in the chat as well. Update `departments/sales/pipeline.md` (or the CRM).

## Needs a yes

Sending the message by email, DM or any connected tool, and sending a calendar invite or booking link that books the lead in. Show the final text, who it goes to and how it will be sent first. Updating the pipeline and drafting in `outputs/` don't need a yes.
