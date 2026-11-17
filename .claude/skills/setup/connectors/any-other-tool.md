# Connect any other tool

Use this when the owner uses a tool that has no guide of its own here: a booking system, CRM, accounting app, email newsletter tool, project board, and so on. You are walking them through it during setup (see [the setup skill](../SKILL.md)). Give one step at a time, in plain words, and wait for them to say "done" (or tell you what they see) before the next. Never ask them to paste a password, key or code into this chat. Setup never stops because one tool won't connect.

Work down the four options below in order and stop at the first one that works. Don't spend more than a few minutes on any one tool; "manual" is a perfectly good answer.

**Social platforms** (Instagram, Facebook, LinkedIn, TikTok and the like) usually stay `manual`: the brain drafts the post, and the owner posts it by copy and paste. Only connect one if Option 1 or Option 2 turns up a claude.ai connector or an official server from the platform's own company. Never use an unofficial one for a social account.

## First, two questions

Ask one at a time:

1. "What's the tool called?" (Get the exact name and, if unsure, its website.)
2. "What do you use it for, and what would you want me to do with it?" (For example: "see who's booked this week", "check which invoices are unpaid", "find a client's notes".)

Tell them in one or two lines what connecting it would let the brain do, based on their answer.

## Option 1 (best): a claude.ai connector

1. Check for yourself first: search the web for "<tool name> Claude connector" and look for a listing on claude.com or claude.ai (the connector directory), or on the tool's own website.
2. Then have them look: "Open a web browser, go to claude.ai and sign in with the same account you use for Claude Code. Go to **Customize**, then **Connectors** (the direct address is claude.ai/customize/connectors). Click **Discover** and type <tool name> into the search box. Is it there?"
3. If it is: "Click it, then click **Connect** (it may say **Connect to Claude**). Sign in to <tool name> and approve access. Say done when it shows as **Connected**."
4. "Now come back to this Claude Code window and say done." Then check for yourself whether <tool name>'s actions are now available to you. Don't ask the owner to type anything to check.
   - **Available:** say "I can see <tool name> now." and run the test below. How = `claude.ai connector`.
   - **Not yet:** Claude Code picks up new connectors when a session starts. Set the row in `business/tools.md` to Connected `pending` so nothing is lost (`setup_stage` stays `tools`), then say: "I need a fresh start to see it. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on." When setup picks up again, check again and run the test.

Notes: connectors need a paid Claude plan. On a Team or Enterprise Claude plan, an Owner may need to add the connector for the organisation first. If they see **Request** instead of **Connect**, that's what's happening.

## Option 2: an official MCP server from the tool's company

An "MCP server" is the tool's own plug for AI assistants.

1. Search the tool company's own website and help docs for "MCP" or "AI assistant" or "connect to Claude". The official MCP Registry (registry.modelcontextprotocol.io) is also worth a look.
2. **Prefer official.** Use a server only if the tool's own company publishes it (it's on their website or their official code page). An unofficial server, built by someone else, could see or change everything in their account. If only unofficial ones exist, tell the owner plainly that it's not from the tool's company and recommend Option 3 or manual instead. Never install one without that warning and a clear yes.
3. **Check what it can change.** Many official servers can make changes, not just read: take payments, issue refunds, edit or delete records, send messages. If the company offers a read-only option (a read-only scope, permission or setting), prefer it, and tell the owner to pick it when they sign in. Whatever it can do, the approval rule applies to every change: nothing is sent, paid, changed or deleted without an explicit yes, every time.
4. **Prefer the kind you sign in to in the browser** (the company's docs give a web address for it). Ask: "Can I add <tool name>'s official connection to Claude Code? You'll sign in yourself." On a yes, add it using exactly the transport and address the company's own docs give. Don't guess either one, and don't assume the address ends in a particular way:
   `claude mcp add --transport <http or sse, as their docs say> <short-name> <the exact address from their docs>`
5. Set the row in `business/tools.md` to Connected `pending`, then: "I need a fresh start to pick this up. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on."
6. After the restart, check for yourself whether <tool name>'s actions are available to you. If they are, run the test. If it still needs signing in, walk them through it: "One more step to sign in. In the box where you type to me, type /mcp and press Enter. That works the same in the desktop app and in a terminal: it opens a list of your connections. Pick <short-name> (click it in the desktop app, or use the arrow keys and Enter in a terminal), then choose **Authenticate**. Sign in to <tool name> in the browser, approve, then come back here and say done." How = `local MCP`.
7. If the official server only works with a key, put the key in `.env` (below) and follow the company's instructions for Claude Code, keeping the key out of every file except `.env`. If those instructions need extra software installed (such as Node.js or Docker), tell the owner and let them choose; manual is fine too.

## Option 3: the tool's API with a key in .env

Most business tools have an "API" (a way for other software to read from them) and give out "API keys" in their settings.

1. Search the tool's help docs for "API key". Look for a key that can only **read** (some tools call it read-only, restricted, or let you tick permissions). Prefer that every time.
2. Walk them through creating the key on the tool's website, one click at a time, using the tool's own help page. "Copy the key, but don't paste it here."
3. Pick a name for it: the tool's name in capitals with `_API_KEY` on the end (for example `ACMEBOOKINGS_API_KEY`).
4. Put it in `.env` (below).
5. Read the tool's API docs to find the simplest read-only request that lists recent items, and run it with the key loaded inside the same command, for example:
   `set -a; . ./.env; set +a; curl -s https://api.example.com/v1/bookings?limit=3 -H "Authorization: Bearer $ACMEBOOKINGS_API_KEY"`
   Only use reading requests (GET or search). How = `API key in .env`.

### Putting a key in .env

The owner puts the key in the file themselves. You never see it, type it or print it.

1. If there's no `.env` file in the top of this folder, create one containing just the line `NAME_API_KEY=` (with the real name). If `.env` exists but has no such line, add that line to the end. Never read out what's already in the file.
2. Ask, then open it for them: on a Mac `open -e .env`, on Windows `notepad .env`.
3. "Paste your key straight after the = sign, no spaces or quotes. Save (Cmd+S on a Mac, Ctrl+S on Windows), close the file and say done."
4. Check it's there without showing it: `grep -c '^NAME_API_KEY=.\+' .env` should print `1`.
5. Load the key inside the same command that uses it. Never `cat` the file or echo the key. `.env` is git-ignored, so it never leaves their computer.

If they paste a key into the chat by mistake: don't save it anywhere, and ask them to delete that key in the tool and make a new one, because the chat isn't a safe place for it.

## Option 4: manual

If none of the above exists, or it's more hassle than it's worth, that's fine. Record it as manual (below) and tell them how it'll work: they paste in or download what's needed, and the brain drafts things for them to paste back.

## Test it (read-only)

Whatever route worked, run the smallest read-only check that proves the brain sees *their* data: list the last 3 (or next 3) of whatever the tool holds, such as bookings, contacts, invoices, tasks or subscribers. Show just the names, dates or amounts, then ask: "I can see [the 3 items]. Is that right?"

- **Yes:** it works. Record it.
- **No, or an error:** see the section at the bottom.

Only read. Don't create, change, send or delete anything as part of the test.

## Record it

Add or update one row in `business/tools.md` (today's date as YYYY-MM-DD):

`| <Tool name> | <what they use it for> | yes | <claude.ai connector, local MCP or API key in .env> | YYYY-MM-DD |`

For manual: `| <Tool name> | <what they use it for> | manual | manual (copy and paste) | — |`

While waiting for a fresh start: `| <Tool name> | <what they use it for> | pending | <the route you're trying> | — |`. When setup picks up again, test it and change `pending` to `yes` (or `no` if it still won't work).

## Safety

The approval rule applies to every tool, whatever it is: reading is fine, but get an explicit yes, every time, before anything that sends a message, posts, invites other people, involves money, or deletes something. Show exactly what will happen first.

## If it doesn't work

Common fixes, in plain words:

- **The connector or server isn't listed:** it may not exist yet. Move to the next option.
- **Connected on claude.ai, but you still can't see it after a fresh start:** check they're signed in to Claude Code with the same Claude account. Ask them to type `/status` and press Enter, and tell you which account it shows. If it says an API key instead of their Claude account, ask them to type `/login` and pick their Claude account, then start a fresh session as above.
- **Sign-in fails:** try a private/incognito browser window, and check they're signing in to the business account, not a personal one.
- **The key test says "unauthorized" or "forbidden":** the key may be missing a read permission, may have been copied with a space, or may be a test key. Fix it in the tool, or paste it again in `.env`.
- **The tool's company says API access needs a higher plan:** don't push them to upgrade during setup. Go manual.

Still stuck after one or two tries? Don't keep them there:

1. Record it in `business/tools.md` as `| <Tool name> | <use> | no | manual (copy and paste) | — |` (not connected).
2. Tell them: "No problem. For now, paste in or download what you need from <tool name>, and I'll draft anything that has to go back in for you to copy. We can try again any time: just say 'connect <tool name>'."
3. Carry on with the next tool.

Sources: https://claude.com/docs/connectors/getting-started, https://code.claude.com/docs/en/mcp, https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
