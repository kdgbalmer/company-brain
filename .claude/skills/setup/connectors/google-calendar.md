# Connect Google Calendar

You are walking the owner through connecting Google Calendar during setup (see [the setup skill](../SKILL.md)). Give one step at a time, in plain words, and wait for them to say "done" (or tell you what they see) before the next. Never ask them to paste a password, key or code into this chat. If anything goes wrong, use the section at the bottom. Setup never stops because one tool won't connect.

## What this lets the brain do

- Build "what should I work on today?" around the calls and sessions already booked.
- Prepare for the next client session or discovery call (who, when, what was said last time).
- Find free time for a new client and suggest slots to offer them.
- Spot an overloaded week before it happens.

## Before you start

- They need a paid Claude plan (Pro or above), signed in to Claude Code with that same Claude account.
- On a Team or Enterprise plan, an Owner of their Claude organisation has to switch Google Calendar on for the organisation first. If they aren't that Owner, they ask the Owner, and you carry on with the next tool meanwhile.

## Route 1 (preferred): the claude.ai connector

Google Calendar has an official connector made by Anthropic. If they connected Gmail a moment ago, this is the same routine.

1. "Open a web browser and go to claude.ai. Sign in with the same account you use for Claude Code. Say done when you're in."
2. "Go to **Customize**, then **Connectors**. (The direct address is claude.ai/customize/connectors.) Say done when you can see the Connectors page."
3. "Find **Google Calendar**. If it isn't in your list, click **Discover** and type Google Calendar into the search box. Click it, then click **Connect**."
4. "Google will ask you to sign in. Pick the Google account your work calendar is on, and click **Allow** on the permissions screen. Say done when you're back on the Connectors page."
5. "Google Calendar should now show as **Connected** (the button changes to **Disconnect**). Is that what you see?"
6. "Now come back to this Claude Code window and say done." Then check for yourself whether the **Google Calendar** connector's actions are now available to you. Don't ask the owner to type anything to check.
   - **Available:** say "I can see Google Calendar now." and go to the test below.
   - **Not yet:** Claude Code picks up new connectors when a session starts. Set the Google Calendar row in `business/tools.md` to Connected `pending` so nothing is lost (`setup_stage` stays `tools`). Then say: "I need a fresh start to see it. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on." When setup picks up again, check again and run the test.

## Route 2 (fallback)

There isn't a simple second route for Google Calendar. Anthropic runs this connector, and Google only allows its sign-in through claude.ai. If Route 1 doesn't work, use the manual fallback at the bottom.

If their calendar lives somewhere else (Outlook, Calendly, Acuity and so on), use [any-other-tool.md](any-other-tool.md) instead.

## Test it (read-only)

Use the calendar tools to list their next 3 events (title, day, time). Show them, then ask: "Your next 3 events are: [list]. Is that right?"

- **Yes:** it works. Record it.
- **No, or an error:** go to the section at the bottom. If the events are right but the times are off by hours, check the time zone in `business/profile.md` and say so.

Only read. Don't create, move or answer any event as part of the test.

## Record it

Add or update one row in `business/tools.md` (today's date as YYYY-MM-DD):

`| Google Calendar | <what they use it for, e.g. client sessions and discovery calls> | yes | claude.ai connector | YYYY-MM-DD |`

Then say in one line: "Your calendar's connected. I'll ask before I invite anyone to anything."

## Safety

- What a connector can do varies and can change over time. Once the calendar is connected, check which actions it actually offers you (for example: read only, or also create, move or answer events). Don't assume either way.
- **If it can create or change events:** the approval rule applies every time. Never create an invite that goes to other people, or move or cancel an event, without showing exactly who, when and what, and getting a yes.
- **If it can't:** give the owner the details ready to paste (title, day and time, who, link, a short description) so they can add it themselves. Say so in one line.

## If it doesn't work

Common fixes, in plain words:

- **Google Calendar isn't in the list on claude.ai:** they may be on a free plan, or on a Team/Enterprise plan where the Owner hasn't switched it on yet.
- **Google sign-in fails or loops:** try a private/incognito browser window, make sure they picked the right Google account, then try **Connect** again. If it shows **Reconnect**, click it and sign in again.
- **Work Google accounts:** some company Google accounts block outside apps. Their Google admin has to allow it.
- **Connected on claude.ai, but you still can't see it after a fresh start:** check they're signed in to Claude Code with the same Claude account. Ask them to type `/status` and press Enter, and tell you which account it shows. If it says an API key instead of their Claude account, ask them to type `/login` and pick their Claude account, then start a fresh session as above.
- **The test shows an empty or wrong calendar:** they may have connected a personal Google account, or their bookings live on a second calendar. Ask which calendar the client bookings go on.

Still stuck after one or two tries? Don't keep them there:

1. Record it in `business/tools.md` as `| Google Calendar | <use> | no | manual (copy and paste) | — |` (not connected).
2. Tell them: "No problem. When you want help planning, paste in or tell me what's booked, and I'll work around it. We can try connecting again any time: just say 'connect my calendar'."
3. Carry on with the next tool.

Sources: https://claude.com/docs/connectors/google/calendar, https://claude.com/docs/connectors/getting-started, https://code.claude.com/docs/en/mcp
