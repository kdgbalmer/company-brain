# Connect Notion

You are walking the owner through connecting Notion during setup (see [the setup skill](../SKILL.md)). Give one step at a time, in plain words, and wait for them to say "done" (or tell you what they see) before the next. Never ask them to paste a password, key or code into this chat. If anything goes wrong, use the section at the bottom. Setup never stops because one tool won't connect.

## What this lets the brain do

- Read the notes, client trackers, SOPs and content calendars they already keep in Notion.
- Pull a client's history from their Notion page before a session or follow-up.
- Add finished work to a Notion page or database when they ask (a new SOP, a content plan, a client summary).

## Before you start

- They need a paid Claude plan (Pro or above), signed in to Claude Code with that same Claude account.
- On a Team or Enterprise Claude plan, an Owner of their Claude organisation has to add Notion for the organisation first.
- The connector sees what their Notion account can see. If they share a workspace with others, the brain sees those pages too.

## Route 1 (preferred): the claude.ai connector

Notion has an official connector, made by Notion, in the claude.ai directory.

1. "Open a web browser and go to claude.ai. Sign in with the same account you use for Claude Code. Say done when you're in."
2. "Go to **Customize**, then **Connectors**. (The direct address is claude.ai/customize/connectors.) Say done when you can see the Connectors page."
3. "Click **Discover**, type Notion into the search box, and click **Notion**. Then click **Connect** (it may say **Connect to Claude**)."
4. "Notion will ask you to sign in and choose a workspace. Pick your business workspace and click **Allow** (or **Select pages** if it asks, and tick the pages the brain should see). Say done when you're back on the Connectors page."
5. "Notion should now show as **Connected**. Is that what you see?"
6. "Now come back to this Claude Code window and say done." Then check for yourself whether the **Notion** connector's actions are now available to you. Don't ask the owner to type anything to check.
   - **Available:** say "I can see Notion now." and go to the test below.
   - **Not yet:** Claude Code picks up new connectors when a session starts. Set the Notion row in `business/tools.md` to Connected `pending` so nothing is lost (`setup_stage` stays `tools`). Then say: "I need a fresh start to see it. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on." When setup picks up again, check again and run the test.

## Route 2 (fallback): Notion's own server, added straight to Claude Code

Use this if the claude.ai connector isn't available to them. It still signs in through Notion in the browser, so there's no key to handle.

1. Ask: "Can I add Notion's official connection to Claude Code? It only sets up the link; you'll sign in to Notion yourself." On a yes, run:
   `claude mcp add --transport http notion https://mcp.notion.com/mcp`
2. Set the Notion row in `business/tools.md` to Connected `pending` so nothing is lost, then: "I need a fresh start to pick this up. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on."
3. After the restart, check for yourself whether Notion's actions are available to you. If they are, go to the test. If Notion still needs signing in, walk them through it: "One more step to sign in. In the box where you type to me, type /mcp and press Enter. That works the same in the desktop app and in a terminal: it opens a list of your connections. Pick **notion** (click it in the desktop app, or use the arrow keys and Enter in a terminal), then choose **Authenticate**. Your browser opens. Sign in to Notion, pick your workspace, click **Allow**, then come back here and say done."
4. Run the test below. Record How as `local MCP`.

**Last resort: a Notion key.** Only if both of the above fail and they're comfortable with it. Notion's own docs now call their old key-based local server unmaintained, so use the key with Notion's API directly:

1. "In your browser, go to notion.so/profile/integrations and create a new **internal** integration for your workspace. On its **Capabilities** settings, tick **Read content** only. Copy the secret it shows you, but don't paste it here." (Notion's developer pages also offer personal access tokens on some accounts. Either works.)
2. "Now give it access: open each Notion page the brain should see, click the **•••** menu at the top right, find **Connections**, and add the integration you just made. Pages inside it are included."
3. Put the key in `.env` as `NOTION_API_KEY` (see "Putting a key in .env" below).
4. Run the test with: `set -a; . ./.env; set +a; curl -s -X POST https://api.notion.com/v1/search -H "Authorization: Bearer $NOTION_API_KEY" -H "Notion-Version: 2022-06-28" -H "Content-Type: application/json" -d '{"page_size": 10}'` and read only the page titles from the result. Record How as `API key in .env`.

### Putting a key in .env

The owner puts the key in the file themselves. You never see it, type it or print it.

1. If there's no `.env` file in the top of this folder, create one containing just the line `NOTION_API_KEY=`. If `.env` exists but has no such line, add that line to the end. Never read out what's already in the file.
2. Ask, then open it for them: on a Mac `open -e .env`, on Windows `notepad .env`.
3. "Paste your key straight after the = sign, no spaces or quotes. Save (Cmd+S on a Mac, Ctrl+S on Windows), close the file and say done."
4. Check it's there without showing it: `grep -c '^NOTION_API_KEY=.\+' .env` should print `1`.
5. Load the key inside the same command that uses it, as in the test above. Never `cat` the file or echo the key. `.env` is git-ignored, so it never leaves their computer.

If they paste a key into the chat by mistake: don't save it anywhere, and ask them to delete that key in Notion and make a new one, because the chat isn't a safe place for it.

## Test it (read-only)

List the pages the brain can see (up to 10 titles). Show them, then ask: "I can see these Notion pages: [titles]. Are those the right ones, and is anything missing that I should see?"

- **Yes:** it works. Record it.
- **Missing pages:** with the connector, they may have picked only some pages at sign-in; with a key, they need to add the integration to those pages. Fix, then test again.
- **An error:** go to the section at the bottom.

Only read. Don't create or edit any page as part of the test.

## Record it

Add or update one row in `business/tools.md` (today's date as YYYY-MM-DD):

`| Notion | <what they use it for, e.g. client notes and SOPs> | yes | claude.ai connector | YYYY-MM-DD |`

(How is `local MCP` or `API key in .env` if they used Route 2.) Then say in one line: "Notion's connected. I'll ask before I change anything in it."

## Safety

- Reading is fine. Save new work to `outputs/` by default.
- Add or change Notion pages only when they ask for that specific change, and show what will go where first.
- Never delete, move or share a Notion page without an explicit yes, every time. Other people may rely on those pages.
- Client notes stay private. Never copy them anywhere outside this folder or their own Notion.

## If it doesn't work

Common fixes, in plain words:

- **Notion isn't in the list on claude.ai:** they may be on a free Claude plan, or on a Team/Enterprise plan where the Owner hasn't added it. Try Route 2.
- **Sign-in shows the wrong workspace:** disconnect Notion on claude.ai (open it under **Your connectors**, click **Disconnect**), connect again and choose the right workspace.
- **Connected on claude.ai, but you still can't see it after a fresh start:** check they're signed in to Claude Code with the same Claude account. Ask them to type `/status` and press Enter, and tell you which account it shows. If it says an API key instead of their Claude account, ask them to type `/login` and pick their Claude account, then start a fresh session as above.
- **The test finds no pages:** nothing has been shared with the connection yet. See "Missing pages" above.
- **Their Notion is a company workspace:** a Notion workspace owner may need to allow connections or tokens in Notion's **Settings**, under **Connections**.

Still stuck after one or two tries? Don't keep them there:

1. Record it in `business/tools.md` as `| Notion | <use> | no | manual (copy and paste) | — |` (not connected).
2. Tell them: "No problem. Paste in any Notion page you want me to use, and I'll write things for you to paste back into Notion. We can try connecting again any time: just say 'connect Notion'."
3. Carry on with the next tool.

Sources: https://claude.com/marketplace/connectors/notion, https://claude.com/docs/connectors/getting-started, https://code.claude.com/docs/en/mcp, https://developers.notion.com/guides/mcp/get-started-with-mcp
