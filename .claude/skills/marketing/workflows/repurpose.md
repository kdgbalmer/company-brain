# Repurpose

## Purpose

Turn one thing the owner has already made or said (a post, a talk, a video, call notes, an article, a newsletter) into a set of new pieces for different platforms, so one good idea works several times.

## Use when

The owner gives you a source and wants more out of it: "turn this blog post into social posts", "here's the transcript of my talk, what can we make from it?", "repurpose last week's newsletter for LinkedIn and Instagram".

## Load first

- The source itself (pasted text, a file in the folder, or a link)
- `business/voice.md`
- `business/customers.md` (to pick the ideas that matter most to them)
- `business/profile.md` (which platforms they're on)
- The offer the pieces point to, from `business/offers.md` (if any)
- The platform files in `.claude/skills/marketing/platforms/` for each platform you'll write for
- `departments/marketing/context.md`

## Steps

1. **Get the source.** If it's a link you can't read, or a video or audio file you can't open, ask the owner to paste the text or transcript. Don't guess what it says.
2. **Pin the brief.** You need: which platforms (default: the ones in `profile.md`), roughly how many pieces, and the one next step for readers. If anything is missing, ask one question. Otherwise state your assumption in one line and carry on.
3. **Mine the source.** List what's in it that can stand on its own: separate ideas, stories, strong lines worth quoting, steps or lists, questions it answers, and any numbers or results it actually states. Use only what's there. If the source is client call notes, leave out names and anything that could identify the client unless the owner says the client has agreed.
4. **Map pieces to platforms.** Make a table, one row per piece:

   | From the source | Platform | Format | Angle |
   |---|---|---|---|

   Formats can be a text post, a carousel, a short video script, a quote card, or an email. Give each piece its own angle so they don't feel like copies. Show the table and ask: "Want all of these, or just some?" If the owner already said "just write them", skip the question.
5. **Draft.** Run [social-post](social-post.md) for each post or script, [newsletter](newsletter.md) for an email, and [branded-graphic](branded-graphic.md) for a quote card or carousel the owner wants made. Each piece must make sense to someone who never saw the source.

## Check before handing over

- Does every piece stand alone, without "as I said in my talk" or "in my last post"?
- Is each piece written for its platform, not the same words pasted across platforms?
- Every claim, number and result comes from the source or the business files. Nothing added.
- No client names or private details unless the owner confirmed the client agreed.
- Each draft passes the checks in its own workflow.

## Save to

`outputs/marketing/YYYY-MM-DD-repurpose-<short-topic>.md`, containing a one-line note of the source, the table, and every draft grouped by platform. Show the table and the first draft in the chat, and say where the rest are.

## Needs a yes

Posting, scheduling or sending any of the pieces. Show each piece's final text, platform, account and time first. A yes covers that exact list only. If the owner has allowed a platform without asking in `business/rules.md`, post and confirm.
