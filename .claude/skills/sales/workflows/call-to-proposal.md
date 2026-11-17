# Call to proposal

## Purpose

Turn the owner's notes from a sales call into a clear, short proposal (or quote) in the client's own words, built only from the business's real offers and prices, plus the email that sends it.

## Use when

A call has happened (the business's first call with someone: discovery call, scoping call, intro call or site visit, in their own word) and the person is a fit and wants to go ahead. If they're not ready yet, use `lead-follow-up` instead. Examples: "write up a proposal for Jordan from today's call", "turn these notes into a quote", "send Leah the details of the 12-week programme".

## Load first

- The call notes or transcript (pasted by the owner, or from a connected tool)
- `business/offers.md` (what's included, format, price, payment options, how to buy)
- `business/voice.md` (tone rules, samples)
- `business/brand.md` (if the proposal will be a formatted document)
- `departments/sales/pipeline.md` or the connected CRM
- `departments/sales/context.md` (any proposal template, terms or payment details the owner has saved)

## Steps

1. **Get the notes.** If the owner hasn't pasted them, ask for them. Rough notes or a voice-to-text dump are fine. If a meeting tool is connected and has a transcript, read that. As soon as the notes are in, set the lead's stage in the pipeline to `call done, proposal not sent` (add a row if they're not there yet). If `departments/sales/pipeline.md` doesn't exist, create it with the header row given in the sales skill.
2. **Pull out what matters.** In the client's own words: where they are now, what they want, why now, what's in the way, any deadline, budget or decision-maker they mentioned. Note anything the owner promised on the call.
3. **Match the offer.** Pick the offer from `offers.md` that fits. If the owner agreed something custom on the call (a different length, an extra, a different price), use what the notes say and flag it clearly for the owner to confirm. Never invent a price, discount, bonus or guarantee.
4. **Draft the proposal.** Keep it to one or two pages:
   - Where you are now (their situation, in their words)
   - What you want (the result they described)
   - What we'll do (the offer: what's included, format, length)
   - Investment (price and payment options, exactly as in `offers.md` or the notes)
   - Next step (how to say yes and how to pay, and by when if there's a real reason for a date). Use the payment link or payment process from `offers.md`. If there isn't one, write `[ASK: payment link]` in its place and tell the owner. Never invent a link.

   Use the business's vocabulary: programme and sessions for a coach, engagement and phases for a consultant, project, brief or retainer for an agency or freelancer, quote and appointment for a local service.
5. **Draft the cover email.** Three to five lines, in the owner's voice, that recap the call in one line and point to the proposal and the one next step.
6. **Update the pipeline.** The stage stays `call done, proposal not sent` until the proposal has actually gone out; then set it to `proposal sent`, with the value from the price and a follow-up date about a week out.

## Check before handing over

- Every price, inclusion and term comes from `offers.md` or the owner's notes. Anything custom is flagged for the owner to confirm.
- No invented results, client stories, guarantees or deadlines.
- The client would recognise their own situation in the first section.
- One clear way to say yes and pay. Any missing payment link is an `[ASK: payment link]` gap, not a made-up link.

## Save to

`outputs/sales/YYYY-MM-DD-proposal-<client-name>.md` (proposal plus cover email). If the owner wants a formatted version, also save `outputs/sales/YYYY-MM-DD-proposal-<client-name>.html` using the colours and fonts in `brand.md`. Show both texts in the chat.

## Needs a yes

Sending the proposal or the cover email, sending a payment link or invoice, and any price or discount that isn't already in `offers.md`. Show the final text, the price, who it goes to and how it will be sent, and wait for a yes.
