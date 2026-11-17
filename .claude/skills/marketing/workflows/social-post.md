# Social post

## Purpose

Write one ready-to-post piece for one platform, in the owner's voice, about one idea, ending with one clear next step for the reader.

## Use when

The owner asks for a post, caption or script for a single platform: "write an Instagram post about my spring offer", "LinkedIn post about what happened with a client this week", "TikTok script on the three mistakes people make".

## Load first

- `business/voice.md` (tone rules, samples, corrections)
- `business/customers.md` (their words, struggles and objections)
- The offer this post points to, from `business/offers.md` (if any)
- `business/brand.md` (if there's a graphic)
- The platform file in `.claude/skills/marketing/platforms/`
- `departments/marketing/context.md`

## Steps

1. **Pin the brief.** You need: the platform, the one idea, and what the reader should do next (follow, comment, click a link, book a call, reply). If any of these is missing and you can't tell from the request, ask one question to get them. Otherwise state your assumption in one line and carry on. Assumptions about format, angle or call to action are fine to state and carry on with. Facts about the business (dates, prices, results, names, what's included) are not: they must come from the business files, or you ask. If an offer start date, a launch date or a deadline the post would mention is already in the past, say so in one line and ask before using it.
2. **Find the angle.** Write three possible opening lines, each a different type: a bold claim, a specific story moment, a question in the customer's own words. Pick the strongest for this platform and audience. Show the other two at the end as alternatives.
3. **Draft.** Follow the platform file for length, line breaks and format. One idea only. Use concrete details from the business (a real offer, a real type of client, a real number from the files) instead of general advice. Sound like the samples in `voice.md`.
4. **End with one next step.** Exactly one call to action that matches the brief.
5. **Add the extras the platform needs.** Hashtags, a title, on-screen text or a shot list, following the platform file.
6. **Visual.** If the platform needs an image and the owner hasn't supplied one, suggest one in a line. If they want it made, run the `branded-graphic` workflow.

## Check before handing over

- Read it as the ideal customer: does the first line make them stop? Would they know what to do next?
- Could this post have come from any other business? If yes, add a specific detail from the business files.
- No words from the "never use" list in `voice.md`. No invented results, testimonials or numbers.
- Length and format match the platform file.

## Save to

`outputs/marketing/YYYY-MM-DD-<platform>-<short-topic>.md`, containing the post, the alternative opening lines, and any hashtags or shot list. Show the post in the chat as well.

## Needs a yes

Posting or scheduling it through a connected tool. Show the final text, the platform, the account and the time first. If the owner has allowed this platform without asking in `business/rules.md`, post and confirm.
