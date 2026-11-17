# Stage 3: Tools

## Goal

Know every tool the business uses, connect the ones that will help most right now, prove each connection works with a read-only test, and record it all in `business/tools.md`. A tool that won't connect never blocks setup: mark it and move on.

## What to say first

> Now your tools. Connecting one means I can look at it when you ask, for example "what's in my diary on Thursday?" or "find the email from the plumber". I can read and draft, but I'll always ask you first before I send, post, book anyone in or touch money.
>
> Which tools do you use to run the business? For example: email (Gmail?), a calendar, Google Drive, Notion, Canva, Stripe, a booking system, an invoicing app. Just list them.

## Steps

**First, if you're resuming.** If setup picks up at stage `tools` and any row in `business/tools.md` has Connected `pending`, deal with those first, before asking anything new. For each one, check whether its actions are now available to you, run its guide's test, and change `pending` to `yes` (or follow the guide's "If it doesn't work" section). Tell the owner in one line what's now working. Then ask about any tools still left to connect and carry on from step 3.

1. **List them all in `business/tools.md`.** One row per tool they name, with "What we use it for" filled in (ask in a few words if it's not obvious). Leave "Connected?" blank for now.
2. **Suggest which to connect now.** Pick up to three that matter most for their active departments and their first win (email and calendar are usually the most useful). Say: "Let's connect Gmail and your calendar now. The others can wait; just say 'connect Canva' whenever you like." Let them choose.
3. **For each tool, open its guide** and follow it with the owner:

   | Tool | Guide |
   |---|---|
   | Gmail | [gmail](../connectors/gmail.md) |
   | Google Calendar | [google-calendar](../connectors/google-calendar.md) |
   | Google Drive | [google-drive](../connectors/google-drive.md) |
   | Notion | [notion](../connectors/notion.md) |
   | Canva | [canva](../connectors/canva.md) |
   | Stripe | [stripe](../connectors/stripe.md) |
   | Anything else | [any-other-tool](../connectors/any-other-tool.md) |

   How to walk them through a guide:
   - Give **one step at a time**, in plain words, and wait for "done" before the next one. Say exactly what to click and what they should see.
   - **Check for yourself whether it's connected.** Don't ask the owner to type commands to check. After they've connected a tool, see whether its actions are now available to you, and tell them in one line.
   - If you can't see it yet, Claude Code needs a fresh session to pick it up. Save progress first: set the tool's row in `business/tools.md` to Connected `pending`, and leave `setup_stage` as `tools`. Then tell them: "I need a fresh start to see it. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on." Connect any other tools you can first, so they only need one fresh start.
   - **API keys** (only for guides that need one): ask them to paste the key into the `.env` file in this folder themselves, and show them the exact line to add. Don't ask them to paste a key into the chat. If they do anyway, put it in `.env`, never in any markdown file, and don't repeat it back.
4. **Run the guide's read-only test.** Show the owner what you found and ask: "Does that look right?" For example: "I can see your last three emails: one from Sam about Thursday, an invoice reminder, and a newsletter. Right?" Never send, post, change or delete anything as a test.
5. **Record the result** in that tool's row of `business/tools.md`:
   - **Connected?** `yes` if the test worked; `pending` while waiting for a fresh start; `no` if it didn't work; `manual` if they'd rather copy and paste.
   - **How:** `claude.ai connector`, `local MCP`, `API key in .env`, or `manual (copy and paste)`.
   - **Tested on:** today's date as `YYYY-MM-DD` (leave blank if not tested).
6. **If it doesn't work,** follow the guide's "If it doesn't work" section. If that doesn't fix it within a couple of tries, mark it `no`, say "No problem, we'll leave that one. I can still work with it if you copy and paste things in.", and move on to the next tool.
7. **Tools without a guide** (booking systems, invoicing apps, CRMs and so on): use [any-other-tool](../connectors/any-other-tool.md). If nothing can connect it, mark it `manual`.
8. **Social platforms** (Instagram, Facebook, LinkedIn, TikTok): these usually stay `manual`. Say so plainly: "I'll write your posts; you paste them into the app and post them yourself." Only try to connect one if a claude.ai connector or an official server from the platform's own company exists (see [any-other-tool](../connectors/any-other-tool.md), Options 1 and 2).

**No tools, or "not now":** that's fine. Record what they use as `manual` and go to the next stage. Everything works by copy and paste; connecting just saves them time.

## What to write where

| What | Where |
|---|---|
| Every tool, connected or not | `business/tools.md`, one row each |
| API keys | `.env` only, never markdown |
| Nothing else | Don't change other business files in this stage |

## Connecting one tool later

When the owner says "connect <tool>" after setup: add or find its row in `business/tools.md`, follow its guide as above, run the test, update the row. Don't change `setup_stage`.

## How to finish

1. Recap in a couple of lines: what's connected, what's manual, what's left for later.
2. Set `setup_stage: first-win` and `last_updated` in `business/profile.md`.
3. Say: "Now the fun part. Let's make one real thing for your business, using everything you've told me." Go to [stage 4](04-first-win.md).
