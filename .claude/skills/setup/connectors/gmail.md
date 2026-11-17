# Connect Gmail

You are walking the owner through connecting Gmail during setup (see [the setup skill](../SKILL.md)). Give one step at a time, in plain words, and wait for them to say "done" (or tell you what they see) before the next. Never ask them to paste a password, key or code into this chat. If anything goes wrong, use the section at the bottom. Setup never stops because one tool won't connect.

## What this lets the brain do

- Find an enquiry or a client's last message in seconds ("what did the lead from Tuesday ask?").
- Summarise a long email thread before a call.
- Spot emails waiting on a reply so the daily plan can include them.
- Give the brain the real wording of client questions, so replies and posts sound right.

## Before you start

- They need a paid Claude plan (Pro or above), signed in to Claude Code with that same Claude account.
- On a Team or Enterprise plan, an Owner of their Claude organisation has to switch Gmail on for the organisation first. If they aren't that Owner, they ask the Owner to do it, and you carry on with the next tool meanwhile.

## Route 1 (preferred): the claude.ai connector

Gmail has an official connector made by Anthropic. Walk them through it:

1. "Open a web browser and go to claude.ai. Sign in with the same account you use for Claude Code. Say done when you're in."
2. "Go to **Customize**, then **Connectors**. (The direct address is claude.ai/customize/connectors.) Say done when you can see the Connectors page."
3. "Find **Gmail**. If it isn't in your list, click **Discover** and type Gmail into the search box. Click it, then click **Connect**."
4. "Google will ask you to sign in. Pick the Google account your business email is on, and click **Allow** on the permissions screen. Say done when you're back on the Connectors page."
5. "Gmail should now show as **Connected** (the button changes to **Disconnect**). Is that what you see?"
6. "Now come back to this Claude Code window and say done." Then check for yourself whether the **Gmail** connector's actions are now available to you. Don't ask the owner to type anything to check.
   - **Available:** say "I can see Gmail now." and go to the test below.
   - **Not yet:** Claude Code picks up new connectors when a session starts. Set the Gmail row in `business/tools.md` to Connected `pending` so nothing is lost (`setup_stage` stays `tools`). Then say: "I need a fresh start to see it. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on." When setup picks up again, check again and run the test.

## Route 2 (fallback)

There isn't a simple second route for Gmail. Anthropic runs this connector, and Google only allows its sign-in through claude.ai, so a home-made server is not worth it for a small business. If Route 1 doesn't work, use the manual fallback at the bottom.

## Test it (read-only)

Use the Gmail tools to list the subjects (and senders) of their last 3 emails. Show them, then ask: "I can see your last 3 emails: [subjects]. Is that right?"

- **Yes:** it works. Record it.
- **No, or an error:** go to the section at the bottom.

Only read. Don't open, label, move or reply to anything as part of the test.

## Record it

Add or update one row in `business/tools.md` (today's date as YYYY-MM-DD):

`| Gmail | <what they use it for, e.g. client and lead email> | yes | claude.ai connector | YYYY-MM-DD |`

Then say in one line: "Gmail's connected. I'll ask before anything goes out."

## Safety

- What a connector can do varies and can change over time. Once Gmail is connected, check which actions it actually offers you (for example: read and search only, or also draft, label or send). Don't assume either way.
- **If it can send** (or change or delete email): the approval rule applies every time. Show the exact email, who it goes to and when, and wait for a yes.
- **If it can't send:** write the reply into `outputs/` and hand the owner the finished text, ready to paste into Gmail. Say so in one line.
- Client emails stay private. Never copy them anywhere outside this folder.

## If it doesn't work

Common fixes, in plain words:

- **Gmail isn't in the list on claude.ai:** they may be on a free plan (connectors like this need a paid plan), or on a Team/Enterprise plan where the Owner hasn't switched Gmail on yet.
- **Google sign-in fails or loops:** try a private/incognito browser window, make sure they picked the right Google account, then try **Connect** again. If it shows **Reconnect**, click it and sign in again.
- **Work Google accounts:** some company Google accounts block outside apps. Their Google admin has to allow it.
- **Connected on claude.ai, but you still can't see it after a fresh start:** check they're signed in to Claude Code with the same Claude account. Ask them to type `/status` and press Enter, and tell you which account it shows. If it says an API key instead of their Claude account, ask them to type `/login` and pick their Claude account, then start a fresh session as above.
- **The test shows the wrong emails:** they connected a different Google account. Disconnect Gmail on claude.ai and connect again with the right one.

Still stuck after one or two tries? Don't keep them there:

1. Record it in `business/tools.md` as `| Gmail | <use> | no | manual (copy and paste) | — |` (not connected).
2. Tell them: "No problem. For now, paste in any email you want help with, and I'll draft the reply for you to copy back into Gmail. We can try connecting again any time: just say 'connect Gmail'."
3. Carry on with the next tool.

Sources: https://claude.com/docs/connectors/google/gmail, https://claude.com/docs/connectors/getting-started, https://code.claude.com/docs/en/mcp
