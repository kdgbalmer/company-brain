# Cash-flow check

## Purpose

Show the owner, week by week for the next 8 to 12 weeks, what money is expected in, what's expected out, and where things could get tight, so they can act early instead of finding out late.

## Use when

The owner is worried or planning: "will I be OK for money?", "can I afford a new laptop in March?", "what's coming in over the next couple of months?", "should I chase anyone?".

## Load first

- `departments/finance/ledger.md` (recent months, to spot regular costs and income)
- `departments/finance/context.md` (open invoices, payment terms, regular costs)
- `business/offers.md` (prices and payment plans)
- `business/tools.md` (connected payment tool with subscriptions or payouts?)
- `business/goals.md`
- Sales pipeline and client notes in `departments/sales/` and `departments/delivery/`, if they exist

## Steps

1. **Starting point.** Ask how much is in the business account today. Don't guess it and don't read it from a bank (the owner tells you). If they'd rather not say, run the check on in and out only and say so.
2. **Expected money in.** List, with dates: open invoices and their due dates; payment-plan instalments from current clients; recurring subscriptions from a connected tool; signed work not yet invoiced. Keep "likely" pipeline deals (from sales notes) in a separate column. Never count them as certain.
3. **Expected money out.** List regular costs you can see repeating in the ledger (software, rent, contractors, loan payments), plus anything the owner mentions (a planned purchase, a tax bill they know is due). Ask: "Anything big coming up I won't see in the ledger?" Don't estimate tax yourself.
4. **Lay it out by week.** A table: week starting, money in (certain), money in (likely), money out, running balance. Cover 8 weeks by default, 12 if asked.
5. **Spot the tight spots.** Name any week where the running balance (certain income only) drops below zero or below a safety level the owner has set in `context.md`.
6. **Suggest moves.** Up to three plain options: chase a specific overdue invoice, move a planned purchase, ask a client for a deposit, promote a specific offer from `offers.md`. Each is a suggestion, not an action.
7. **Show it** in the chat: the table and the tight spots first, then the suggestions.

## Check before handing over

- Every figure has a source: ledger, open invoice, offer price, connected tool, or the owner's own words. Unknowns are listed as unknown.
- Likely income is kept apart from certain income.
- The running balance adds up week to week.
- No tax estimates or financial advice beyond plain options. Tax questions go to their accountant.

## Save to

`outputs/finance/YYYY-MM-DD-cash-flow-check.md`, containing the table, tight spots, suggestions and the list of assumptions. Add any regular cost or safety level the owner told you to `departments/finance/context.md`.

## Needs a yes

Nothing for the check itself. Acting on a suggestion (sending a chaser email, sending an invoice) runs through its own workflow and needs its own yes. Never move money.
