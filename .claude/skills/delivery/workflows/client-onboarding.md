# Client onboarding

## Purpose

Get a new client off to a great start: set up their private client file, write the welcome message with clear first steps, and make sure nothing the owner normally does at the start gets missed.

## Use when

Someone has just said yes or paid: "onboard my new client Alex", "Maya signed up for the 3-month programme, get her set up", "new booking from the Hendersons, send the welcome".

## Load first

- `business/offers.md` (the offer they bought: what's included, format, length)
- `business/voice.md` (tone rules, samples)
- `business/tools.md` (calendar, inbox, file storage, payments connected?)
- `departments/delivery/context.md` (the owner's onboarding steps, intake questions, welcome pack, if saved)
- `departments/sales/pipeline.md` (the lead's row and any proposal in `outputs/sales/`, if sales is active)

## Steps

1. **Gather the basics.** Client name, which offer, start date, and how they like to be contacted. Look in the pipeline and the proposal first. Ask the owner only for what's missing, one question at a time.
2. **Create the client file.** Make `departments/delivery/clients/<client-name>.md` with the sections About, Goals, Log, Actions agreed and Next date. Fill in what you know from the proposal or call notes. Leave the rest for the first session. If the file already exists, add to it and don't overwrite it.
3. **Check the onboarding steps.** Use the owner's own checklist from `departments/delivery/context.md` if there is one. If not, propose a short one that fits the business type (for example: welcome message, book the first session or appointment, intake questions, agreement or terms, access to any materials, invoice or payment confirmed). Ask the owner which apply and save the agreed checklist to `departments/delivery/context.md` so it's reused next time.
4. **Draft the welcome message.** Warm, short, in the owner's voice. Thank them, say what happens next and when, list what you need from them (no more than three things), and how to reach the owner. Use the details of the offer as written in `offers.md`. Don't promise results.
5. **Draft the intake questions** (if the owner uses them). Five to eight plain questions that tell the owner what they need before the first session or job.
6. **Plan the first date.** If a calendar is connected, suggest times for the first session, meeting or appointment. Add it to the client file's Next date once agreed.
7. **Update the pipeline.** If sales is active, set the lead's stage to `won`.

## Check before handing over

- The client file exists and holds only what was actually said or agreed.
- The welcome message has one clear first step and no more than three asks.
- Offer details match `offers.md`. No invented results or promises.
- Every item on the onboarding checklist is either done, drafted, or flagged for the owner.

## Save to

`departments/delivery/clients/<client-name>.md` (client file) and `outputs/delivery/YYYY-MM-DD-onboarding-<client-name>.md` (welcome message, intake questions, checklist with status). Show the welcome message in the chat.

## Needs a yes

Sending the welcome message or intake questions, sending a calendar invite to the client, sharing any file or folder with them, and sending an invoice or payment link. Show exactly what will go, to whom, and when, and wait for a yes. Client notes are private and never leave this folder.
