# Inbox triage

## Purpose

Turn a full inbox into a short, sorted list with replies already drafted, so the owner can clear it in minutes. Nothing is sent, archived or deleted without their yes.

## Use when

The owner is behind on email: "go through my inbox", "what needs a reply today?", "sort my emails from this week", or they paste a batch of messages and ask what to do with them.

## Load first

- `business/tools.md` (is email connected?)
- `business/voice.md` (for drafted replies)
- `business/rules.md` (actions allowed without asking, house rules such as "never reply on Sundays")
- `business/offers.md` and `business/customers.md` (only if replies touch offers or enquiries)
- `departments/operations/context.md` (who handles what, standing preferences)

## Steps

1. **Get the emails.** If email is connected in `business/tools.md`, read the inbox: unread messages from the last 7 days unless the owner says otherwise. If it isn't connected, ask the owner to paste the emails (or just the sender, subject and the key lines) and work from that. Offer once to connect email through setup later.
2. **Sort each email into one of four piles.**
   - **Reply now:** needs the owner's answer and matters this week (clients, leads, money, deadlines).
   - **Delegate:** someone else on the team should handle it. Name who, using the roles in `departments/*/role.md` if they exist.
   - **Later:** worth reading or answering, but not this week.
   - **Archive:** newsletters, receipts, notifications, nothing to do.
3. **Hand off what belongs elsewhere.** A new enquiry goes to the sales department's way of handling leads; an invoice or receipt goes to the finance expense log. Mention it in the list rather than running it silently.
4. **Draft replies** for every "Reply now" email, in the owner's voice, short, answering exactly what was asked. Where you'd need a fact you don't have (a price not in `offers.md`, a date, a yes or no only the owner can give), leave a clear `[ASK: ...]` gap instead of guessing. For "Delegate", draft a one-line forward note.
5. **Show the list** in the chat, grouped by pile: sender, subject, one-line summary, and the draft reply under each "Reply now" item. Put the most urgent first.
6. **Act only on a yes.** Ask which drafts to send (as they are, or with edits) and whether to archive the "Archive" pile. Do exactly what was approved. If email is connected and the owner prefers, save replies as drafts in their mailbox instead of sending.

## Check before handing over

- Every "Reply now" email has a draft; every draft answers the question actually asked.
- No invented prices, dates, promises or results. Gaps are marked `[ASK: ...]`.
- Drafts sound like `voice.md`, not like a template.
- Client details stay in this folder; nothing is forwarded outside without a yes.
- Nothing was sent, archived or deleted yet.

## Save to

`outputs/operations/YYYY-MM-DD-inbox-triage.md`, containing the four piles and the drafts. Show it in the chat as well. Add any new standing preference ("always forward booking emails to the assistant") to `departments/operations/context.md`.

## Needs a yes

Sending or forwarding any email, saving drafts into their mailbox, archiving, labelling or deleting anything. Show the final text and the recipient for each email, and list exactly which messages will be archived or deleted. Deleting needs its own clear yes, never bundled with sending.
