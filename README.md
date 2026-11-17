# Company Brain

A second brain for your small business that runs in Claude Code.

Download this folder, open it in Claude Code and type **set me up**. It interviews you about your business: your offers, customers, voice, brand and goals. Then it helps you connect the tools you already use. After that you just ask for things:

> "Write an Instagram post about my new group programme."
> "Follow up with the lead I spoke to on Tuesday."
> "What should I work on today?"
> "Turn my notes from today's session into a recap email."
> "Draft an invoice for Sam for March."

It works out which department the job belongs to and pulls in your brand, voice and offer details. It runs a tested workflow for that job and hands you finished work in your style. It always asks before it posts, sends, books anyone in, or touches money.

It's built for service businesses: coaches, consultants, agencies, freelancers and local service businesses. It works for a one-person business, and every department has a role file, so you can bring in help later (a person or an AI agent).

---

## What you need

- A **paid Claude plan** (Pro or Max) or a Team/Enterprise seat. Claude Code and tool connectors need one.
- **Claude Code.** The easiest way is the Claude desktop app's **Code** tab (download from [claude.com/download](https://claude.com/download)). The terminal version works too.

## Install in three steps

1. **Get the folder.** On this page click the green **Code** button → **Download ZIP**, then unzip it somewhere you'll keep it, e.g. `Documents/Company Brain`. (Comfortable with git? `git clone` it instead.)
2. **Open it in Claude Code.** In the desktop app, open the **Code** tab, start a new session and pick the folder. In the terminal, `cd` into the folder and run `claude`.
3. **Type `set me up`.**

Setup takes about 15–20 minutes for the interview, plus a few minutes per tool you connect. You can stop any time and say "set me up" later to carry on. It remembers where you got to.

**Shortcut:** when it asks, paste your website address or a document about your business, and it drafts most of the answers for you to check.

## What's inside

Eight departments, each with ready-made workflows:

| Department | What you can ask for |
|---|---|
| **HQ** | Today's priorities, a weekly review, quarterly goals, logging decisions |
| **Marketing** | Social posts (Instagram, LinkedIn, Facebook, TikTok, YouTube Shorts), a week of content, newsletters, repurposing, lead magnets, website copy, branded graphics |
| **Sales** | Lead follow-ups, discovery call prep, proposals from call notes, pipeline review |
| **Delivery** | New client onboarding, session prep, session recap emails, testimonial requests, wrapping up a client |
| **Offers** | Designing an offer, checking a price, launch plans, sales pages |
| **Finance** | Invoices, expense log, monthly numbers, cash-flow check |
| **Operations** | Inbox triage, planning your week, writing SOPs, tool audit |
| **Team** | Writing a role (for a person or an AI agent), handovers |

Something your business does that isn't covered, like retreats, a podcast or workshops? Just ask: "make me a workflow for running my retreats." The **builder** creates it and the brain uses it from then on.

To see a finished example, look at [examples/harbour-coaching](examples/harbour-coaching/README.md). It's a made-up career coach with everything filled in.

## How it's organised

```
CLAUDE.md          how the brain behaves (you don't need to touch this)
.claude/skills/    the departments and their built-in workflows
business/          who you are: profile, offers, customers, voice, brand, goals, tools, rules
departments/       each department's notes, plus your own custom workflows
outputs/           everything the brain makes for you, by department and date
memory/            decisions and a daily log
```

`business/`, `departments/`, `outputs/` and `memory/` don't exist until you run setup. They're **yours**.

## Your data stays on your computer

Your business folders hold client notes, leads and numbers, so they are **not** pushed to GitHub. The `.gitignore` file excludes them. Back them up the way you back up anything else (iCloud, Google Drive, Dropbox, an external drive). If you want them in git, use a **private** repository and remove those lines from `.gitignore`.

Passwords and API keys only ever go in a file called `.env`, which is also never pushed. The brain will never ask you to paste a key into the chat.

## Staying in control

The brain reads and drafts freely. It **always asks first**, and shows you exactly what will happen, before it:

- posts or publishes anything
- sends an email or message
- sends a calendar invite to someone else
- does anything involving money
- deletes anything

You can relax a specific one, e.g. "you can post to LinkedIn without asking." It writes that down in `business/rules.md` so you can always see what you've allowed.

## Making it yours

- **Correct it.** Say "too formal" or "we never say 'journey'" and it fixes the work and remembers the rule.
- **Change a built-in workflow.** Say "change how you write my newsletters so…". It copies the workflow into `departments/marketing/workflows/` and edits your copy. Your version wins from then on.
- **Redo a part of setup.** Say "redo my brand", "update my offers", "connect Stripe" or "switch on finance".

## Updating to a newer version

Your own files are never in the download, so updating is safe:

1. Download the new version.
2. Copy its `.claude/` folder, `CLAUDE.md` and `README.md` over your old ones.
3. Leave `business/`, `departments/`, `outputs/`, `memory/` and `.env` alone.

## For contributors

`python3 scripts/validate.py` checks the structure: skills, workflow shape, links, templates, privacy rules. `python3 -m unittest discover tests` tests the checker. Every workflow file uses the same seven sections: Purpose, Use when, Load first, Steps, Check before handing over, Save to, Needs a yes.

## Licence

MIT. Use it, change it, share it.
