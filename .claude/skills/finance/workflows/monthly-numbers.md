# Monthly numbers

## Purpose

Give the owner a one-page picture of a month: money in, money out, what's left, where it came from, and how that compares with their goals. Every number traceable, nothing guessed.

## Use when

The owner asks how a month went: "how did October go?", "monthly numbers", "what did I make last month?", "am I on track for my revenue goal?". Also at the end of each month if the owner has asked for a regular check.

## Load first

- `business/goals.md` (revenue and other targets, the numbers they watch)
- `business/offers.md` (offer names, to group income)
- `business/tools.md` (connected accounting or payment tool?)
- `departments/finance/ledger.md`
- `departments/finance/context.md` (categories, open invoices, corrections)

## Steps

1. **Pick the month.** If they didn't say, use the last full month and say so in one line.
2. **Gather the figures.** Read the connected tool if there is one; otherwise use the ledger. If both exist, use the tool and point out any payments that are in one and not the other.
3. **Look for gaps.** If the month has no expense rows, suspiciously few income rows, or an open invoice whose due date has passed, ask before reporting: "I've got no costs for October. Did you have any, or is that right?" One question at a time. If the owner doesn't know, report the gap rather than filling it.
4. **Work out the numbers.**
   - Revenue: total money in.
   - Costs: total money out, split by category.
   - Profit: revenue minus costs.
   - Top clients: the three who paid the most.
   - Top offers: revenue per offer, matched against `offers.md`.
   - Unpaid: open invoices, and which are overdue.
   Keep currencies separate if there's more than one. Don't convert unless the owner gives you the rate.
5. **Compare with goals.** For every target in `goals.md` that this month's figures touch, show the target, the actual, and the gap. If a goal isn't about money (e.g. email list size), skip it.
6. **Say what it means.** Three short lines at most: what went well, what to watch, one thing worth doing next month. Plain words, no accounting terms. No tax opinions.
7. **Show it** in the chat as a short table plus the three lines.

## Check before handing over

- Revenue, costs and profit add up.
- Every figure came from the tool, the ledger or the owner. Any gap is named, not filled.
- Offer names match `offers.md`; client names match the ledger.
- Goal comparisons use the actual targets in `goals.md`, not made-up ones.
- No tax or accounting advice. If they asked a tax question, suggest their accountant.

## Save to

`outputs/finance/YYYY-MM-DD-monthly-numbers-<YYYY-MM>.md`, containing the table, the goal comparison, unpaid invoices and the three lines.

## Needs a yes

Nothing, as long as it stays a report. Sending it to anyone (a business partner, an accountant) needs a yes, showing who it goes to and the message first.
