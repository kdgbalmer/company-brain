# Content week

## Purpose

Plan a run of posts (usually a week) across the platforms the business actually uses, tied to this quarter's goals and one offer, then draft every post so the owner only has to check and post.

## Use when

The owner asks for more than one post at once: "plan my content for next week", "give me five posts for Instagram and LinkedIn", "I need content for the next two weeks", "fill my content calendar".

## Load first

- `business/goals.md` (what the content has to move this quarter)
- `business/offers.md` (the one offer this run points to)
- `business/customers.md` (their struggles, words and objections)
- `business/voice.md`
- `business/profile.md` (which platforms they're on)
- The platform files in `.claude/skills/marketing/platforms/` for each platform in the plan
- `departments/marketing/context.md`
- The last two or three content plans in `outputs/marketing/` (so you don't repeat ideas)

## Steps

1. **Pin the brief.** You need: how many days, which platforms, how many posts a day (default one per platform per posting day), and which offer the run supports. Take the platforms from `profile.md` and the offer from the goal it serves in `goals.md`. If the offer isn't clear, ask one question: "Which offer should this week lead people towards?" Otherwise state your assumptions in one line and carry on. If a goal deadline, the quarter, an offer start date or a launch date in the business files is already in the past (check today's date), say so in one line and ask whether it still stands (or suggest the HQ quarterly-goals workflow for an old goal) before building the week around it.
2. **Choose the mix.** Spread the posts across five types:
   - **Teach**: one useful thing the ideal customer can use today.
   - **Story**: a moment from the owner's work or life that makes a point.
   - **Proof**: a real result, client win or testimonial from the business files.
   - **Offer**: says plainly what the offer is, who it's for and how to get it.
   - **Behind the scenes**: how the owner works, what a day or a session looks like.

   For five posts, a good default is two teach, one story, one proof, one offer. Don't open the week with the offer post. Never invent proof: if the files have no real result or testimonial to use, swap that slot for a teach or behind-the-scenes post and ask the owner in one line if they have a result they're happy to share.
3. **Build the plan as a table.** One row per post:

   | Day | Platform | Type | The one idea | Opening line | Next step for the reader |
   |---|---|---|---|---|---|

   Every idea should come from a struggle, objection or phrase in `customers.md`, or from something real in the business. Each post should still make sense to someone who sees only that one.
4. **Show the plan.** Ask one question: "Happy with this, or want to change anything before I write them?" If the owner already said "just write them", skip the question.
5. **Draft every post.** Run the [social-post](social-post.md) workflow for each row, using the row as its brief. The same idea can appear on two platforms, but rewrite it for each platform file rather than pasting the same text.
6. **Visuals.** List which posts need an image. Offer to make them with [branded-graphic](branded-graphic.md).

## Check before handing over

- Does every post serve the goal and point, directly or indirectly, towards the one offer?
- Is the mix right, with no two posts making the same point?
- Read the opening lines in a row: are they different enough that a follower wouldn't scroll past "the same post again"?
- No invented results, testimonials, client stories or numbers. Every proof post uses something real from the files or from the owner.
- Each draft passes the checks in [social-post](social-post.md).

## Save to

`outputs/marketing/YYYY-MM-DD-content-week-<short-topic>.md`, containing the plan table, then every draft in day order with its platform, alternative opening lines and hashtags. Show the plan table and the first post in the chat, and say where the rest are.

## Needs a yes

Posting or scheduling any of the posts through a connected tool. Show the full list first: each post's final text, platform, account and time. A yes covers that exact list only. If something changes, ask again. Platforms the owner has allowed without asking in `business/rules.md` can be scheduled and confirmed afterwards.
