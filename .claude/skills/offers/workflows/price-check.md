# Price check

## Purpose

Help the owner choose or test a price by reasoning through three things: the value to the customer, the owner's time cost, and what the market charges. Give a clear range and a recommendation with the reasons, never a made-up number.

## Use when

The owner asks "what should I charge?", "is my price too low?", "can I raise my prices?", "how should I price this new package?", or is stuck on the price step of [design-offer](design-offer.md).

## Load first

- The offer in `business/offers.md` (or the draft from `outputs/offers/`)
- `business/customers.md` (who's buying and what the result is worth to them)
- `business/goals.md` (revenue and client targets)
- `departments/finance/context.md` (if it exists, for costs and hours)
- `departments/offers/context.md` (if it exists)

## Steps

1. **Pin the offer.** Confirm which offer, what's included and the current price (if there is one). If there's no clear offer yet, run [design-offer](design-offer.md) first.
2. **Value to the customer.** Ask the owner what the result is worth to a typical customer: money saved or earned, time saved, stress removed, what they'd otherwise pay someone else. Use only what the owner tells you or what's in `customers.md`. If they don't know, write down what you'd need to find out.
3. **Time cost.** Ask how many hours one customer takes in total, including prep, admin and messages between sessions. Ask for any direct costs (materials, software, venue, travel). Work out the effective hourly rate at the current or proposed price and show the sum plainly.
4. **The market.** Ask: "What do two or three others who do something similar charge?" Use only the prices the owner gives you. Don't look up or invent competitor prices. If they don't know, suggest they check a few competitors' websites and come back, and carry on with the other two reasons.
5. **The goal maths.** Using `goals.md`, show how many customers they'd need at each price to hit the quarter's revenue goal, and whether they have the hours for that.
6. **Recommend.** Give a low, middle and high price, and say which one you'd start at and why, in three lines or fewer. Point out any risk plainly (too few hours left, well above what the owner says the market charges). It's their decision.
7. **If raising a price:** suggest how to handle existing customers (keep their price for a while, or give notice) and ask which they prefer.

## Check before handing over

- Every number came from the owner or the business files. Competitor prices are only ones the owner supplied.
- The hourly-rate and goal sums are shown, so the owner can check them.
- The recommendation is about pricing the owner's own service. No investment, tax, legal or other regulated financial advice. If the question strays there (tax on the income, VAT registration, pensions), say it's one for their accountant or adviser.
- Prices are shown with the currency the business uses, and say whether tax is included if the owner has told you.

## Save to

`outputs/offers/YYYY-MM-DD-price-check-<offer>.md`, with the three reasons, the sums, the range and the recommendation. If the owner picks a price, offer to update the offer in `business/offers.md` (after a yes on the exact change) and record it in `memory/decisions.md`.

## Needs a yes

Updating the price in `business/offers.md`: show the exact change first. Changing a price in any live tool (booking page, checkout, payment link, invoice template) is a money action: show the old and new price and where it changes, and wait for an explicit yes.
