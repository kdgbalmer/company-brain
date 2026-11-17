# Weekly review

## Purpose

Look back at the week honestly and set next week's three priorities: what got done, how the numbers compare with the goals, what's stuck, and what comes next.

## Use when

The owner asks for a weekly review, "how did this week go?", "plan next week", or it's the end of the week and they've set this up as a regular habit.

## Load first

- `business/goals.md` (this quarter's goals and the numbers we watch)
- Every file in `memory/log/` from the last seven days
- `memory/decisions.md` (anything decided this week)
- `business/tools.md` (which tools are connected and can give real numbers)
- `departments/sales/pipeline.md` (if it exists)
- Last week's review in `outputs/hq/` (if there is one), to see what was promised
- `departments/hq/context.md` (if it exists)

## Steps

1. **What got done.** Read this week's logs and list what was finished, with file paths where there's an output. Keep it to the things that matter; group small jobs ("four social posts") rather than listing each one.
2. **Check last week's promises.** If there's a previous review, compare its three priorities with what happened. Mark each one: done, partly done, or not done.
3. **The numbers.** First check the dates: if a goal deadline, the quarter, an offer start date or a launch date in the business files is already in the past (check today's date), say so in one line and ask whether it still stands, or suggest running [quarterly-goals](quarterly-goals.md), before measuring against it. Then, for each number in the "numbers we watch" table in `goals.md`:
   - If a connected tool can give it (for example, payments from a connected payment tool, booked calls from a connected calendar), read it. If `tools.md` says a tool is connected but you can't read it right now, say so in one line and ask the owner for that number instead.
   - Otherwise, ask the owner for it. Ask for all the missing numbers in one short list so they can answer in one go. If they don't know one, write "not known" rather than guessing.
   - Show each number against its target and say plainly whether it's on track, behind or ahead.
4. **What's stuck.** List anything that has sat unfinished for more than a week, anything waiting on someone else, and any goal that's behind. For each, one line on what would unstick it.
5. **Next week's three priorities.** Pick three at most, each tied to a goal and written as a concrete outcome for the week ("send three proposals", not "work on sales"). Prefer finishing stuck things over starting new ones.
6. **Show and confirm.** Show the review in the chat and ask if the priorities look right. Adjust once if they want changes.

## Check before handing over

- Every number came from a connected tool or from the owner. None are estimated or made up; missing ones say "not known".
- Every "done" item is backed by a log entry or an output file.
- Next week has three priorities or fewer, each tied to a goal in `goals.md`.
- Nothing new is added to the goals themselves. If the review shows a goal needs changing, offer to run [quarterly-goals](quarterly-goals.md) instead.

## Save to

`outputs/hq/YYYY-MM-DD-weekly-review.md`, with five short sections: Done, Numbers, Stuck, Next week's priorities, Notes. Add one line to `memory/log/YYYY-MM-DD.md` pointing to it. If the owner makes a decision during the review, record it with [log-decision](log-decision.md).

## Needs a yes

Nothing in this workflow sends or publishes. If the owner wants the review shared with anyone (an accountant, a business partner, a team member), show exactly what will be sent and to whom, and wait for a yes.
