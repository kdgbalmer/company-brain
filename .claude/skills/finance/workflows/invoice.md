# Invoice

## Purpose

Draft one correct, ready-to-send invoice for one client, priced from the business's own offers, with the right number, due date and payment details, so the owner only has to check it and say yes.

## Use when

The owner asks to bill a client: "invoice Maple Studio for the March retainer", "send Priya her invoice for the 6-session package", "bill the Hendersons for the kitchen job, deposit already paid".

## Load first

- `business/profile.md` (business name, address, currency)
- `business/offers.md` (the offer being billed: price and payment options)
- `business/tools.md` (is an invoicing or payment tool connected?)
- `departments/finance/context.md` (payment terms, numbering, bank or payment details, tax line if any)
- `departments/finance/ledger.md` (deposits already paid, last invoice number)
- `departments/sales/` or `departments/delivery/` notes on this client, if the job needs them

## Steps

1. **Pin the facts.** You need: the client's name and billing contact, what's being billed (which offer, which dates or sessions), the amount, and the due date. Take prices from `offers.md`. If the client has a different agreed price, a deposit already paid, or anything you can't find, ask one question at a time. Never guess an amount.
2. **Number it.** Use the numbering in `departments/finance/context.md`. If there's none yet, look at past invoices in `outputs/finance/` and the ledger. If there are none, suggest `INV-YYYY-001`, confirm it with the owner, and save the format to `context.md`.
3. **Set the terms.** Use the payment terms in `context.md` (for example "due in 14 days"). If none are recorded, ask once and save the answer to `context.md`. Work out the actual due date.
4. **Draft the invoice.** Include: business name and contact details, client name and billing details, invoice number, issue date, due date, line items (description, quantity, price), any deposit already paid, total due, currency, and how to pay (bank details or payment link from `context.md`). If the owner charges tax, add the line exactly as recorded in `context.md`; if you're not sure whether tax applies, ask and suggest they check with their accountant.
5. **Write a short covering note.** Two or three lines in the owner's voice to go with it in the email.
6. **Show it.** Put the invoice and the note in the chat, then ask for the yes (see below).
7. **After a yes.** Send it or create it in the connected tool. Then add a line to `departments/finance/ledger.md` only when the money actually arrives (or the connected tool shows it paid), not when the invoice is sent. Note the invoice in `departments/finance/context.md` under an "Open invoices" list with number, client, amount and due date.

## Check before handing over

- Every amount traces back to `offers.md`, the ledger, or something the owner said. Nothing invented.
- Line items add up to the total, and any deposit is subtracted once.
- Invoice number is the next one in the sequence and isn't a duplicate.
- Due date is a real date, not just "14 days".
- Client name is spelled the way they spell it.
- Payment details match `context.md` exactly.

## Save to

`outputs/finance/YYYY-MM-DD-invoice-<number>-<client>.md` (or `.html` if the owner wants a printable version). Show the invoice in the chat as well.

## Needs a yes

Sending the invoice by email, or creating it in a payment or accounting tool. Before asking, show the amount and currency, who it goes to (name and email), the invoice number and the due date. Never take or move a payment.
