# Tool audit

## Purpose

Look at every tool the business uses and come back with a short, practical list: what overlaps, what it all costs, what's missing, and what could be connected to the brain to save the owner time.

## Use when

The owner asks: "what am I paying for?", "review my tools", "do I need all these apps?", "what else could you connect to?", or at the start of a new quarter or year.

## Load first

- `business/tools.md`
- `business/goals.md`
- `departments/operations/context.md`
- `departments/finance/ledger.md`, if it exists (to spot software costs)
- `.claude/skills/setup/connectors/` (the connector guides, to see what's easy to connect)

## Steps

1. **List what's there.** Start from `business/tools.md`. Scan the ledger for software or subscription costs that aren't in `tools.md` and ask about each: "I see a monthly payment to Notely. Is that a tool you still use?"
2. **Get the costs.** For each tool, ask what it costs and how often, unless the ledger already shows it. One question at a time, or one short list for several tools. If the owner doesn't know, mark it `unknown` rather than guessing a price.
3. **Ask what each one is really used for**, if `tools.md` doesn't already say. Note tools they pay for but rarely use.
4. **Find overlaps.** Group tools doing the same job (two note apps, two schedulers, a CRM and a spreadsheet both tracking leads). For each group, suggest which to keep based on what the owner uses most and what the brain can connect to.
5. **Find gaps.** Compare the tools with how the business works (`profile.md`) and its goals. Name up to three gaps that cost real time, e.g. "No booking link, so call times are agreed by email".
6. **Find what could be connected.** For each tool marked "no" or "manual" in `tools.md`, check whether a connector guide exists in `.claude/skills/setup/connectors/`. If it does, say so; if not, mention that the `any-other-tool` guide can search for one. Offer to run the setup connection step for any they want.
7. **Show the result** in the chat: a table (tool, used for, cost per month, keep / review / cancel, could connect?), then overlaps, gaps and the total monthly cost.

## Check before handing over

- Every cost came from the owner or the ledger. Unknown costs are marked unknown.
- Recommendations are suggestions. You haven't cancelled, downgraded or changed any tool.
- Nothing contains a password, API key or token.
- `tools.md` updates are only facts the owner confirmed.

## Save to

`outputs/operations/YYYY-MM-DD-tool-audit.md`, containing the table, overlaps, gaps and connection options. Update `business/tools.md` with any confirmed facts (a tool that was missing, what it's used for).

## Needs a yes

Cancelling, downgrading or changing any subscription or account, and connecting a new tool. The owner usually does cancellations themselves; you can give them the steps. Show exactly what would change and what it costs or saves before asking.
