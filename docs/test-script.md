# First-user test script

Use this to check that a brand-new person can get from download to a first real piece of work without help. Give it to someone who has never seen the repo. Watch, don't help. Note every place they hesitate.

## Before you start
- They have a paid Claude plan and the Claude desktop app installed.
- They have their website address or a short description of their business ready.
- 45 minutes.

## The test

| # | They do | Pass if |
|---|---|---|
| 1 | Download the ZIP from GitHub and unzip it | Done in under 3 minutes without asking |
| 2 | Open the folder in the Claude app's Code tab | The brain says hello and mentions setup isn't finished |
| 3 | Type `set me up` | It explains what's coming and how long it takes, then asks **one** question |
| 4 | Paste their website address when offered | It drafts answers and asks them to check, rather than asking every question from scratch |
| 5 | Answer the interview, typing `skip` once | The skipped field is marked TODO; nothing stalls |
| 6 | Close the app halfway through, reopen, say "set me up" | It resumes at the same stage |
| 7 | Accept the suggested departments | `departments/` folders appear only for the active ones |
| 8 | Connect one tool (e.g. Google Calendar) | Click-by-click steps; a read-only test shows real data; `business/tools.md` updated |
| 9 | Skip a tool they don't have | Setup carries on |
| 10 | Get their first win | A finished piece that mentions their real offer and sounds like them, saved in `outputs/` |
| 11 | Say "too formal" | It rewrites, then says what it saved to `business/voice.md` |
| 12 | Ask "post it" | It shows exactly what will be posted and waits for a yes |
| 13 | Ask "what should I work on today?" | Three priorities tied to their goals |
| 14 | Ask for something unusual ("help me plan a retreat") | It offers to build a workflow and saves it in `departments/` |

## After
- Which step took longest?
- Where did they nearly give up?
- Would they open it again tomorrow? Why or why not?
