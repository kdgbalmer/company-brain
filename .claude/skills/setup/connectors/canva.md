# Connect Canva

You are walking the owner through connecting Canva during setup (see [the setup skill](../SKILL.md)). Give one step at a time, in plain words, and wait for them to say "done" (or tell you what they see) before the next. Never ask them to paste a password, key or code into this chat. If anything goes wrong, use the section at the bottom. Setup never stops because one tool won't connect.

## What this lets the brain do

- Make post graphics, carousels and simple flyers straight into their Canva account, ready for them to tweak.
- Find and reuse their existing designs and templates so new graphics look like the old ones.
- Use their brand colours, fonts and logo from Canva (if they have a Canva plan with a brand kit).
- Export a finished design as an image or PDF.

## Before you start

- They need a paid Claude plan (Pro or above), signed in to Claude Code with that same Claude account.
- On a Team or Enterprise Claude plan, an Owner of their Claude organisation has to add Canva for the organisation first.
- They need a Canva account. A free one works for the basics. Some Canva features, such as brand kits, need a paid Canva plan.

## Route 1 (preferred): the claude.ai connector

Canva has an official connector, made by Canva, in the claude.ai directory.

1. "Open a web browser and go to claude.ai. Sign in with the same account you use for Claude Code. Say done when you're in."
2. "Go to **Customize**, then **Connectors**. (The direct address is claude.ai/customize/connectors.) Say done when you can see the Connectors page."
3. "Click **Discover**, type Canva into the search box, and click **Canva**. Then click **Connect** (it may say **Connect to Claude**)."
4. "Canva will ask you to sign in and allow access. Sign in to the Canva account your business designs are in (if you have a team in Canva, pick that team). Click **Allow**, and say done when you're back on the Connectors page."
5. "Canva should now show as **Connected**. Is that what you see?"
6. "Now come back to this Claude Code window and say done." Then check for yourself whether the **Canva** connector's actions are now available to you. Don't ask the owner to type anything to check.
   - **Available:** say "I can see Canva now." and go to the test below.
   - **Not yet:** Claude Code picks up new connectors when a session starts. Set the Canva row in `business/tools.md` to Connected `pending` so nothing is lost (`setup_stage` stays `tools`). Then say: "I need a fresh start to see it. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on." When setup picks up again, check again and run the test.

## Route 2 (fallback)

There isn't a simple second route for Canva. Canva's other connection options are for software developers and need a registered developer app. If Route 1 doesn't work, use the fallback at the bottom: the brain makes graphics as a branded web page they screenshot.

## Test it (read-only)

Use the Canva tools to list their 5 most recent designs (names). If they have a brand kit, also list its name. Show them, then ask: "I can see these designs in your Canva: [names]. Is that right?"

- **Yes:** it works. Record it. If you found a brand kit and `business/brand.md` has no colours yet, offer to copy the colours and fonts across (show them first).
- **No, or an error:** go to the section at the bottom.

Only read. Don't create, edit or export a design as part of the test.

## Record it

Add or update one row in `business/tools.md` (today's date as YYYY-MM-DD):

`| Canva | <what they use it for, e.g. social graphics and flyers> | yes | claude.ai connector | YYYY-MM-DD |`

Then say in one line: "Canva's connected. I'll make designs for you to check; nothing gets published from here."

## Safety

- Creating a draft design in their Canva is fine when they've asked for a graphic. Tell them its name so they can find it.
- Never publish, share, post, or send a design to anyone, and never delete or overwrite one of their existing designs, without an explicit yes, every time.
- Some Canva features may use paid Canva content or credits. Say so before using them.

## If it doesn't work

Common fixes, in plain words:

- **Canva isn't in the list on claude.ai:** they may be on a free Claude plan, or on a Team/Enterprise plan where the Owner hasn't added it.
- **Sign-in fails or shows the wrong account:** try a private/incognito browser window, then connect again with the right Canva account. If it shows **Reconnect**, click it and sign in again.
- **Connected on claude.ai, but you still can't see it after a fresh start:** check they're signed in to Claude Code with the same Claude account. Ask them to type `/status` and press Enter, and tell you which account it shows. If it says an API key instead of their Claude account, ask them to type `/login` and pick their Claude account, then start a fresh session as above.
- **No designs show up:** they may have connected a personal Canva account, or their designs sit in a Canva team they didn't pick. Disconnect and connect again, choosing the right one.
- **Brand kit missing:** brand kits need a paid Canva plan. That's fine; the brain uses `business/brand.md` instead.

Still stuck after one or two tries? Don't keep them there:

1. Record it in `business/tools.md` as `| Canva | <use> | no | manual (copy and paste) | — |` (not connected).
2. Tell them: "No problem. When you need a graphic, I'll make it as a page in your brand colours that you open in your browser and screenshot, or I'll give you the exact words and layout to drop into a Canva template. We can try connecting again any time: just say 'connect Canva'."
3. Carry on with the next tool.

Sources: https://claude.com/marketplace/connectors-plugins, https://claude.com/docs/connectors/getting-started, https://code.claude.com/docs/en/mcp, https://www.canva.dev/blog/developers/canva-mcp-ga/
