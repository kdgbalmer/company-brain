# Expense log

## Purpose

Get money in and money out recorded in the ledger quickly and consistently, so monthly numbers and cash-flow checks have something true to work from.

## Use when

The owner gives you a payment or a pile of them: "log £45 for Canva", "I just got paid 1,200 by Maple Studio", a photo or text of a receipt, a pasted bank statement, a CSV export. Also "what did I spend on software this year?" when the answer needs the ledger tidied first.

## Load first

- `business/tools.md` (connected accounting or payment tool?)
- `departments/finance/ledger.md`
- `departments/finance/context.md` (categories in use, corrections)
- `business/profile.md` (default currency)

## Steps

1. **Check where it belongs.** If a connected accounting tool is the record of truth, say so and ask whether they want it in the ledger as well or entered in the tool (entering it in the tool needs a yes). Otherwise use `departments/finance/ledger.md`, creating it with the standard table if it doesn't exist (see the finance skill).
2. **Read what they gave you.** For each payment find: date, in or out, amount, currency, who it was to or from, and what it was for. For a bank export, list every row you'll add before adding them.
3. **Fill gaps by asking.** If an amount or date is unreadable or missing, ask. One question at a time, or one short list for a batch ("Three rows have no date. Were they all on the 4th?"). Never guess a figure.
4. **Pick a category.** Use the categories already in `context.md`. If none exist yet, suggest a short set (for example: Sales, Software, Marketing, Contractors, Travel, Equipment, Fees, Other), confirm once, and save them to `context.md`. Don't invent a new category for every row.
5. **Spot duplicates.** If a row matches one already in the ledger (same date, amount and name), flag it and ask instead of adding it twice.
6. **Add the rows** to the bottom of the ledger, in date order for the batch: `| 2026-03-04 | Out | 45.00 | GBP | Software | Canva | Monthly plan |`.
7. **Confirm** in one line: how many rows added, total in, total out.
8. **Paid invoices.** If a row settles an open invoice in `context.md`, mark that invoice paid there.

## Check before handing over

- Every row has all seven columns filled. Amounts are plain numbers, dates are `YYYY-MM-DD`.
- No duplicates, no guessed amounts.
- Categories come from the agreed list.
- The table still renders (one row per line, pipes lined up with the header).

## Save to

`departments/finance/ledger.md` (the ledger itself). If the owner asks for a summary of what was logged, save it to `outputs/finance/YYYY-MM-DD-expense-log.md`.

## Needs a yes

Entering anything into a connected accounting or payment tool: show the rows first. Deleting or changing an existing ledger row: show the old and new row first. Never pay, refund or move money.
