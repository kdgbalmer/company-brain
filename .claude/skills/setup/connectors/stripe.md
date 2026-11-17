# Connect Stripe

You are walking the owner through connecting Stripe during setup (see [the setup skill](../SKILL.md)). Give one step at a time, in plain words, and wait for them to say "done" (or tell you what they see) before the next. Never ask them to paste a password, key or code into this chat. If anything goes wrong, use the section at the bottom. Setup never stops because one tool won't connect.

## What this lets the brain do

- Answer "how much came in this month?" and build the monthly numbers from real payments.
- See which invoices are unpaid or overdue, so follow-ups go out on time.
- Check whether a new client has paid before onboarding starts.
- See which offers actually sell, to guide pricing and launches.

**The brain only reads from Stripe unless the owner says yes.** The connection itself may be able to do more (take payments, issue refunds, change prices), and what it offers can change, so check its actions once connected. The approval rule applies to every change.

## Before you start

- For Route 1 they need a paid Claude plan (Pro or above), signed in to Claude Code with that same Claude account.
- On a Team or Enterprise Claude plan, an Owner of their Claude organisation has to add Stripe for the organisation first.
- They need to be able to sign in to their Stripe account (and an admin role on it for Route 2's key).

## Route 1 (preferred): the claude.ai connector

Stripe has an official connector, made by Stripe, in the claude.ai directory.

1. "Open a web browser and go to claude.ai. Sign in with the same account you use for Claude Code. Say done when you're in."
2. "Go to **Customize**, then **Connectors**. (The direct address is claude.ai/customize/connectors.) Say done when you can see the Connectors page."
3. "Click **Discover**, type Stripe into the search box, and click **Stripe**. Then click **Connect** (it may say **Connect to Claude**)."
4. "Stripe will ask you to sign in and approve access. Choose your real business account (live mode), not a test sandbox. If Stripe lets you pick what Claude may do, choose read-only. Click to approve, and say done when you're back on the Connectors page."
5. "Stripe should now show as **Connected**. Is that what you see?"
6. "Now come back to this Claude Code window and say done." Then check for yourself whether the **Stripe** connector's actions are now available to you. Don't ask the owner to type anything to check.
   - **Available:** say "I can see Stripe now." and go to the test below.
   - **Not yet:** Claude Code picks up new connectors when a session starts. Set the Stripe row in `business/tools.md` to Connected `pending` so nothing is lost (`setup_stage` stays `tools`). Then say: "I need a fresh start to see it. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on." When setup picks up again, check again and run the test.

Optional extra safety for Route 1: on claude.ai, under **Customize**, **Connectors**, open **Stripe** and set the tools that change things to **Needs approval** or **Blocked** under **Tool permissions**.

## Route 2 (fallback): Stripe's own server, added straight to Claude Code

Use this if the claude.ai connector isn't available to them. It signs in through Stripe in the browser, so there's no key to handle.

1. Ask: "Can I add Stripe's official connection to Claude Code? It only sets up the link; you'll sign in to Stripe yourself." On a yes, run:
   `claude mcp add --transport http stripe https://mcp.stripe.com/`
2. Set the Stripe row in `business/tools.md` to Connected `pending` so nothing is lost, then: "I need a fresh start to pick this up. If you're in the Claude desktop app, start a new session in this same folder. If you're in a terminal, type /exit, then run claude again here. Then say 'set me up' and we'll carry on."
3. After the restart, check for yourself whether Stripe's actions are available to you. If they are, go to the test. If Stripe still needs signing in, walk them through it: "One more step to sign in. In the box where you type to me, type /mcp and press Enter. That works the same in the desktop app and in a terminal: it opens a list of your connections. Pick **stripe** (click it in the desktop app, or use the arrow keys and Enter in a terminal), then choose **Authenticate**. Your browser opens. Sign in to Stripe, choose your live account, pick read-only if it asks, approve, then come back here and say done."
4. Run the test below. Record How as `local MCP`.

**Last resort: a read-only Stripe key.** Only if both of the above fail. Use a *restricted* key that can only read, never the full "secret key".

1. "In your browser, go to dashboard.stripe.com/apikeys (make sure you're in live mode, not a sandbox). Click **Create restricted key**. If Stripe asks how the key will be used, pick the option for giving an AI agent access if it's there."
2. "Name it something like Company brain read-only. Set **Read** on Charges, PaymentIntents, Customers, Invoices, Subscriptions, Products, Prices, Balance and Payouts. Leave everything else on **None**. Don't give it **Write** on anything."
3. "Click **Create key**, copy the key (it starts with `rk_live_`), but don't paste it here." Stripe may text or email them a code first. That code is theirs to type in Stripe, not here.
4. Put the key in `.env` as `STRIPE_API_KEY` (see "Putting a key in .env" below).
5. Run the test with: `set -a; . ./.env; set +a; curl -s -G https://api.stripe.com/v1/charges -u "$STRIPE_API_KEY:" -d limit=3`. Amounts come back in the smallest unit (pence or cents) and dates as timestamps, so convert both before showing them. Record How as `API key in .env`.

### Putting a key in .env

The owner puts the key in the file themselves. You never see it, type it or print it.

1. If there's no `.env` file in the top of this folder, create one containing just the line `STRIPE_API_KEY=`. If `.env` exists but has no such line, add that line to the end. Never read out what's already in the file.
2. Ask, then open it for them: on a Mac `open -e .env`, on Windows `notepad .env`.
3. "Paste your key straight after the = sign, no spaces or quotes. Save (Cmd+S on a Mac, Ctrl+S on Windows), close the file and say done."
4. Check it's there without showing it: `grep -c '^STRIPE_API_KEY=.\+' .env` should print `1`.
5. Load the key inside the same command that uses it, as in the test above. Never `cat` the file or echo the key. `.env` is git-ignored, so it never leaves their computer.

If they paste a key into the chat by mistake: don't save it anywhere, and ask them to delete (expire) that key in Stripe and make a new one, because the chat isn't a safe place for it.

## Test it (read-only)

List their last 3 payments: amount, currency and date (no customer card details). Show them, then ask: "Your last 3 payments in Stripe were: [list]. Is that right?"

- **Yes:** it works. Record it.
- **No payments, or very odd ones:** they may be connected to a test sandbox instead of their live account. Reconnect and choose live mode.
- **An error:** go to the section at the bottom.

## Record it

Add or update one row in `business/tools.md` (today's date as YYYY-MM-DD):

`| Stripe | <what they use it for, e.g. client payments and invoices> | yes | claude.ai connector | YYYY-MM-DD |`

(How is `local MCP` or `API key in .env` if they used Route 2.) Then say in one line: "Stripe's connected. I'll only read from it, and I'll never touch money without your yes."

## Safety

- Reading only, by default. Use Stripe to look things up and report numbers. If the connection can make changes, that doesn't change this.
- Never create a charge, refund, invoice, payment link, coupon, price change, subscription change or payout without an explicit yes in the chat, every time. Before asking, show exactly what will happen: the amount, the currency, who it's for, and what it does.
- Stripe may also ask the owner to approve some actions (such as refunds) in their Stripe Dashboard. That's on top of your yes, not instead of it.
- Never show full card or bank details, even if a tool returns them.

## If it doesn't work

Common fixes, in plain words:

- **Stripe isn't in the list on claude.ai:** they may be on a free Claude plan, or on a Team/Enterprise plan where the Owner hasn't added it. Try Route 2.
- **Stripe blocks the connection:** if their Stripe account has several users, a Stripe administrator may need to allow AI tool (MCP) access in the Stripe Dashboard settings.
- **Connected on claude.ai, but you still can't see it after a fresh start:** check they're signed in to Claude Code with the same Claude account. Ask them to type `/status` and press Enter, and tell you which account it shows. If it says an API key instead of their Claude account, ask them to type `/login` and pick their Claude account, then start a fresh session as above.
- **The key test says "permission" or "unauthorized":** the restricted key is missing a **Read** permission, or the key was copied with a space. Fix it in Stripe or paste it again in `.env`.
- **Payments look like test data:** they're in sandbox mode. Switch Stripe to live mode and reconnect (or make the key again in live mode).

Still stuck after one or two tries? Don't keep them there:

1. Record it in `business/tools.md` as `| Stripe | <use> | no | manual (copy and paste) | — |` (not connected).
2. Tell them: "No problem. When you want the monthly numbers, download a payments report from Stripe (or paste the totals in), and I'll do the rest. We can try connecting again any time: just say 'connect Stripe'."
3. Carry on with the next tool.

Sources: https://docs.stripe.com/mcp, https://docs.stripe.com/keys, https://claude.com/docs/connectors/getting-started, https://code.claude.com/docs/en/mcp
