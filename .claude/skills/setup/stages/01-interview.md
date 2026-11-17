# Stage 1: Interview

## Goal

Learn who the business is and write it down in `business/`, so every piece of work after this sounds like the owner and talks about their real offers, customers and goals. It should feel like a chat with someone curious about their business, not a form.

## What to say first

Keep it to a few short lines, in your own words:

> Hi. I'm going to get to know your business so everything I make sounds like you, not like a robot.
>
> It takes about 15 to 20 minutes. I'll ask one thing at a time. You can say "skip" to anything, and you can stop whenever you like: I save as we go, and next time you just say "set me up" and we carry on.
>
> Quick shortcut first: have you got a website, a LinkedIn, Instagram or Facebook page, or any document about your business (a brochure, a sales page, an about page)? Paste the link or the text, or drop the file in here, and I'll draft the answers for you to check. If not, no problem, we'll just talk.

Then wait for their answer.

## Steps

### 1. Get the files ready

- Create any missing files from the templates (see the table in [SKILL.md](../SKILL.md)). Never replace a file that already exists.
- Set `setup_stage: interview` in `business/profile.md`.
- If you're resuming, read what's already written and start from the first topic that's still blank. Don't ask again for anything already answered.

### 2. The shortcut (if they took it)

- **A website link:** read the home page, and the about, services or pricing pages if you can find them. Note the colours and fonts the site uses if you can see them.
- **A LinkedIn link:** LinkedIn usually blocks reading. If it does, say so in one line and ask them to copy and paste their "About" section and headline instead.
- **An Instagram or Facebook link:** these pages often can't be read automatically. Don't keep trying: ask them to copy and paste their bio (Instagram) or "About" text (Facebook) instead, plus a recent post or two if they like.
- **A document or pasted text:** read it all.

Draft answers for every topic below from what you read. Then go through the topics **one at a time**: show your draft for that topic in a few lines and ask "Is that right, or what would you change?" Save it once they confirm. Ask a normal question only for the gaps the material didn't cover. Never save a guess as fact.

### 3. The topics, in this order

**Use their words.** Until you know the business type, say "customers". Once topic a has settled the type, use that type's "Words to use" in every question from then on (customers or clients, bookings or sessions, jobs or projects), and the owner's own words if they use different ones. The example questions below are written with neutral wording; swap in theirs.

Ask one question per message. Follow up only on what's missing or vague. Short, warm reactions between questions are good ("That's a clear niche."); long ones aren't. After each topic, save it and say in one line where it went ("Saved to your profile.").

**a. The business and its type** → `business/profile.md`

- Start with: "In a sentence or two, what do you do, and who for?"
- Then, as needed: business name, their own name, where they're based (and time zone), website and main social profiles, how customers usually find them and buy, and what makes them different from the alternatives.
- Work out the business type from their answers (coach, consultant, agency-freelancer, local-service) and check it with them: "Sounds like you're a consultant. Fair?" If it fits none, follow the "Fits none of these?" rule in [SKILL.md](../SKILL.md).
- Write `business_type` in the frontmatter. Open the matching type file ([coach](../business-types/coach.md), [consultant](../business-types/consultant.md), [agency or freelancer](../business-types/agency-freelancer.md), [local service](../business-types/local-service.md)) and note its extra questions and vocabulary.
- Add the type's "Words to use" to the "Things to know" section of the profile, so every department uses the right words.

**b. Offers** → `business/offers.md`

- "What do you sell right now? Just list them, we'll go through each one."
- Then for each offer, one at a time: "Tell me about [offer]: who it's for, what they get, how long it lasts and what it costs." Follow up only on the gaps: the result the customer gets, how to buy or book, the usual objections and how they answer them, and whether it's live, paused or coming soon.
- One `## Offer:` block per offer. Use the type's vocabulary (programme, engagement, retainer, booking).

**c. Ideal customer** → `business/customers.md`

- "Think of your favourite customer. Who are they, and what was going on for them when they came to you?" (Use their word: client, customer, or whatever they say.)
- Then: what they struggle with **in their own words** (ask "What do they actually say when they first get in touch?"), what they want instead, why they hesitate to buy, where they spend time online, and who isn't a good fit.

**d. Voice** → `business/voice.md`

- "Now the most useful bit. Could you paste three to five things you've written yourself? Posts, emails to customers, a newsletter, your about page, even a long text message. Real ones, not polished ones. This is how I learn to sound like you."
- Save each one, word for word, under "Samples of real writing" (`### Sample 1`, `### Sample 2` and so on).
- From the samples, write three to five plain rules under "How we sound" and the words they lean on under "Words we use". Show them: "Here's how I'd describe your writing: … Does that sound like you?"
- Then: "Any words or phrases you never want me to use?" → "Words we never use".
- If they have nothing written, ask them one question to answer the way they'd say it to a friend ("Why did you start this business?") and use that as Sample 1.

**e. Brand** → `business/brand.md`

- "Do you have brand colours? If you know the codes (they look like #1A2B3C), paste them. If not, describe them and I'll suggest codes for you to check." If you read colours from their website, show them and ask.
- Then fonts (if they don't know, write `TODO` and move on; it's not important yet).
- Then the logo: "If you have a logo file, put a copy in the `business/brand-assets` folder inside this project (or drop it into the chat and tell me where it is, and I'll copy it there)." List each file under "Logo".
- Then one question about visual style: "Photos or illustrations? Busy or minimal? Anything you'd hate to see?" → "Visual style".
- Then one question for "Visual do and don't": "Any rules for your graphics? For example: always use your logo, only one line of text on an image, no more than two colours, never use stock photos. If you'd like, I can work these out from your website or a few of your posts for you to check." If they take the offer, read the site (or ask them to paste or drop in two or three posts), draft three or four do's and don'ts, show them, and save once they confirm.

**f. Goals** → `business/goals.md`

- "What are the one to three things you most want to happen in the next three months? A number and a date for each helps, like '4 new clients by the end of March'."
- Then: "Which numbers do you keep an eye on?" (enquiries a week, clients signed, monthly income, email list size). Fill in "Now" and "Target" where they know them.
- Then: "Anything you've decided not to do right now?"

**g. The extra questions for their type**

Ask the extra questions from their business-type file, one at a time, and save each answer where that file says. Skip any the owner has already answered earlier in the interview.

### 4. Handling "skip", "I don't know" and stopping

- **Skip:** write `TODO` in that field, add it to your list of skipped items, move on without comment.
- **"I don't know":** offer one quick way to answer ("Most people in your position say X or Y. Either of those?") and accept a skip.
- **Stopping:** everything answered so far is already saved. Say: "No problem. Everything's saved. Say 'set me up' any time and we'll carry on from [next topic]."

## What to write where

| Topic | File | Sections |
|---|---|---|
| Business and type | `business/profile.md` | frontmatter `business_type`, "The business in one sentence", "Business name and owner", "How the business works", "What makes it different", "Things to know" (vocabulary) |
| Offers | `business/offers.md` | one `## Offer:` block each |
| Ideal customer | `business/customers.md` | every section |
| Voice | `business/voice.md` | "How we sound", "Words we use", "Words we never use", "Samples of real writing" |
| Brand | `business/brand.md` (files in `business/brand-assets/`) | "Colours", "Fonts", "Logo", "Visual style", "Visual do and don't" |
| Goals | `business/goals.md` | "This quarter", "The numbers we watch", "What we're not doing right now" |
| Type questions | Wherever the business-type file says | |

Leave `business/rules.md`, `business/tools.md` and `memory/decisions.md` as their templates for now.

## Redoing one topic later

When the owner says "redo my brand" (or voice, offers, customers, goals, business details): read the current file, show what's there in a few lines, then ask that topic's questions again. Save changes section by section, showing the old and new wording before each one. Add new offers as new blocks; only remove an offer if they say so. Don't touch `setup_stage`.

## How to finish

1. Give a short recap: one line per file, and the list of anything skipped ("You skipped fonts and your second offer's price. Fill those in any time by saying 'redo my brand' or 'redo my offers'.").
2. Set `setup_stage: departments` and `last_updated` in `business/profile.md`.
3. Ask: "Next is quick: choosing which parts of your business I should look after. Carry on?" If yes, go to [stage 2](02-departments.md).
