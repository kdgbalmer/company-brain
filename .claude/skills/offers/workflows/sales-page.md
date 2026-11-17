# Sales page

## Purpose

Write a sales page for one offer that speaks in the customer's own words, answers their real objections, uses only genuine proof, and ends with one clear way to buy or book.

## Use when

The owner asks for a sales page, an offer page, a "work with me" page, or the page a launch points to: "write the page for my 12-week programme", "my sales page isn't converting, rewrite it".

## Load first

- The offer in `business/offers.md` (who it's for, result, what's included, format, price, how to buy, objections)
- `business/customers.md` (struggles, wants, words they use, why they hesitate)
- `business/voice.md` and `business/brand.md`
- `departments/delivery/testimonials.md` (if it exists; the only source of proof)
- `departments/offers/context.md` and `departments/marketing/context.md` (if they exist)

## Steps

1. **Pin the brief.** Confirm the offer, where the page will live (website, booking tool, a one-page link) and the one action at the bottom (buy now, book a call, apply). If the offer is missing its price or how to buy, ask for it. Don't invent one.
2. **Gather the customer's words.** Pull the exact phrases from `customers.md`: how they describe the problem, what they want instead, why they hesitate. If there are none, ask the owner for two or three things real customers have said.
3. **Gather the proof.** Read `departments/delivery/testimonials.md`. Use only testimonials that are there, quoted exactly, with the name or initials as given. If there's no testimonials file or it's empty, leave a clearly marked gap (`[TESTIMONIAL NEEDED]`) and suggest the **delivery** skill's `testimonial-request` workflow. Never write, paraphrase into a quote, or "improve" a testimonial.
4. **Draft the page** in this order, each section short:
   - **Headline:** the outcome, in the customer's words.
   - **The problem:** what it's like now, using their phrases.
   - **What changes:** the result, specific and honest.
   - **What you get:** each part of the offer and why it matters to them.
   - **Who it's for and who it isn't:** from `customers.md`.
   - **Proof:** real testimonials only.
   - **About the owner:** a few lines on why they're the right person, from `profile.md`.
   - **Price and how to buy:** exactly as in `offers.md`, including payment options.
   - **Questions:** the main objections and honest answers.
   - **One call to action,** repeated at the end.
5. **Write two headline options** besides the one used, and show them at the end.
6. **Optional page file.** If the owner wants to see it laid out, also make a simple self-contained HTML version using the colours and fonts in `brand.md`.

## Check before handing over

- Read it as the ideal customer: do they recognise themselves in the first screen? Is it clear what to do next?
- Every testimonial appears word for word in `departments/delivery/testimonials.md`. No invented results, numbers, client names or "as seen in" claims.
- Price, payment options and inclusions match `business/offers.md` exactly.
- Any deadline or "limited places" line is true.
- No words from the "never use" list in `voice.md`.

## Save to

`outputs/offers/YYYY-MM-DD-sales-page-<offer>.md` (and `.html` if made). Show the headline and first section in the chat with the file path.

## Needs a yes

Publishing or updating the page on a website or any live tool: show the final text and exactly where it goes, and wait for a yes. Turning on a payment or checkout link is a money action and needs its own explicit yes.
