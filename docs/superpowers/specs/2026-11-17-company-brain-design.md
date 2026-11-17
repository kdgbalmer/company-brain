# Company Brain — design

Date: 17 November 2026
Status: approved direction, 17 November 2026

## What this is and why

A free, public GitHub repo that a small service business downloads, opens in Claude Code, and says "set me up". It interviews them, connects their tools, and from then on acts as their company's second brain: they ask for something in plain words ("make an Instagram post about my spring offer") and it works out which department the job belongs to, loads only the context that job needs (brand, voice, offer, platform rules), runs that department's workflow step by step, and hands back the finished thing, or does it through a connected tool once they say yes.

Who it's for: anyone, anywhere, running a small service business, mostly solopreneurs (coaches, consultants, agencies/freelancers, local service businesses). Most are not technical. It is completely generic: no branding, links, offers, people or data from any particular business, coach or creator.

Success: a non-technical owner can go from download to their first real, on-brand piece of work in a single sitting, without anyone helping them, and keeps using it afterwards because asking it is faster than doing the job themselves.

## Goals

- One folder, three-step install, onboarding started by saying "set me up".
- A guided onboarding that interviews them, switches on the right departments, walks them through connecting their tools one at a time, and ends with a real first win.
- Eight preloaded departments with working skills and workflows for service businesses.
- Personalisation that adapts to business type (coach, consultant, agency/freelancer, local service) and lets the brain build new workflows or departments for businesses that don't fit the box.
- One shared business layer (who they are, offers, customers, voice, brand) that every department reads, so a change in one place changes everything.
- Safe by default: nothing leaves the business (posts, emails, payments, deletions) without the owner saying yes.

## Non-goals (v1)

- Teams, multiple users, per-person access. Each department has a role file so a person or agent can own it later, but nothing team-specific is built now.
- Plugin packaging. Someone may convert it to a plugin later; the folder layout keeps that conversion easy (see Approaches).
- ChatGPT, Cowork or other tools. Claude Code only (CLI or the desktop app's Code tab).
- Product or e-commerce businesses (inventory, shipping, stock).
- Scheduled jobs switched on by default. Onboarding may offer them at the end; the owner opts in.
- A web app, database, or anything that needs hosting. It is files.

## Anti-goals (would make this a failure even if it works)

- Generic AI output. Every workflow must pull the business's voice, offers, customers and brand before writing. A post that could have been written for any business is a bug.
- Posting, sending, paying or deleting anything without an explicit yes.
- An interview that feels like a 60-question form. One question at a time, skippable, resumable, and it can shortcut by reading their website or existing documents.
- Overwhelming a non-technical user with setup jargon. Every connection step is click-by-click in plain words.
- Secrets in the business files. API keys never go into markdown.

## Constraints and known facts

- Claude Code loads skills from `.claude/skills/<name>/SKILL.md` in the folder it's opened in. Skills in nested subfolders only load once Claude touches that subfolder, so all skills sit at the root `.claude/skills/`.
- The skill list has a budget (about 1% of context); with dozens of skills, descriptions get cut and routing gets worse. Hence one skill per department, not one per task.
- Claude Code only. The desktop app's Code tab is the recommended route for non-technical users; the README covers it first and the CLI second. A paid Claude plan is required.
- Tool connections: the simplest route for both apps is connecting the service once on the claude.ai account (Customize → Connectors). Local MCP servers (`claude mcp add` / `.mcp.json`) are the fallback when no connector exists. API keys go in a git-ignored `.env`.
- Public repo: MIT licence, no personal data, example content uses a fictional business.

## Approaches considered

| | Approach | Trade-off |
|---|---|---|
| A | Plugin (generic skills) + the user's own business folder | Cleanest updates; needs a test that plugin skills can read/write the chosen folder; more install steps |
| **B (picked)** | **One plain folder: everything in the repo, user downloads and opens it** | Simplest to understand and build; solid in Claude Code; updates mean copying new files over |
| C | One repo that works as both | Covers everything but two install paths and double the breakage; not worth it for v1 |

Picked: B, basic for now, plugin maybe later. To keep that later step cheap, B keeps a hard line between **system files** (generic, ours: `.claude/skills/`, `CLAUDE.md`, `README.md`) and **business files** (theirs: `business/`, `departments/`, `outputs/`, `memory/`). The system never stores business facts; the business files never hold logic. Converting to a plugin later = moving `.claude/skills/` into a plugin, untouched business files stay in their folder.

## How it works

### Folder layout

```
company-brain/
  README.md                 for humans: what it is, 3-step install, what to say first
  CLAUDE.md                 the brain's operating rules (router, approval rule, where things live)
  LICENSE                   MIT
  .gitignore                .env, business/, departments/, outputs/, memory/, OS junk (see Privacy)
  .env.example              placeholder names for any API keys
  .claude/
    settings.json           sensible permissions (read freely; ask before shell/network writes)
    skills/
      setup/                onboarding (see below)
      hq/
      marketing/
      sales/
      delivery/
      offers/
      finance/
      operations/
      team/
      builder/              creates new workflows/departments for the business
  business/                 THE SHARED LAYER — created by onboarding from setup/templates/ (not shipped)
    profile.md              name, what they do, business type, setup progress
    offers.md               each offer: who, outcome, price, format, link
    customers.md            ideal customer, problems, words they use, objections
    voice.md                tone rules + real samples of their writing
    brand.md                colours (hex), fonts, logo paths, visual do/don't
    brand-assets/           logo files, photos
    goals.md                this quarter's goals and numbers
    tools.md                every tool: connected? how? tested when?
    rules.md                approval rule + any actions they've loosened
  departments/
    <dept>/
      context.md            what this department needs to know for this business
      role.md               who owns this department (owner by default; later a person or agent)
      workflows/            the business's own or customised workflows (override built-ins)
  outputs/
    <dept>/YYYY-MM-DD-<slug>.md   everything the brain produces
  memory/
    decisions.md            decisions with dates
    log/YYYY-MM-DD.md       what was done each session
  examples/                 a fully filled-in fictional business so people can see "done"
```

### Templates and safe updates

The repo ships no `business/`, `departments/`, `outputs/` or `memory/` folders. Blank templates for all of them live in `.claude/skills/setup/templates/`, and onboarding creates the real folders from them. So updating the brain later (copying a newer `.claude/`, `CLAUDE.md` and `README.md` over) can never wipe an owner's filled-in files. The README's "Updating" section says exactly which files and folders to copy.

### Privacy

Coaches' session notes and lead details are confidential. `.gitignore` excludes `business/`, `departments/`, `outputs/`, `memory/` and `.env` by default, so someone who forks the public repo and pushes cannot publish their customers' data by accident. The README explains this in one paragraph and how to back the folder up instead (a private repo with the ignore lines removed, or their normal cloud drive).

### The router (CLAUDE.md)

`CLAUDE.md` is short and does four jobs:

1. If `business/profile.md` says setup isn't finished, offer to continue setup before anything else.
2. Route every request to a department skill (marketing, sales…). If it's unclear, ask one question. If no department fits, offer the builder skill.
3. Before any department works, it reads `business/profile.md`, `voice.md`, `brand.md`, the relevant parts of `offers.md`/`customers.md`, and that department's `context.md`. Nothing else, to keep context small.
4. The approval rule (below), and end-of-session logging to `memory/log/`.

### Department skills

Each department is one skill: `SKILL.md` (when to use it, what context to load, which workflow fits which request) plus a `workflows/` folder of step-by-step workflow files, plus reference files where needed (e.g. `marketing/platforms/instagram.md` with format, length, hashtag and image-size rules).

Lookup order for a workflow: `departments/<dept>/workflows/<name>.md` (theirs) first, then `.claude/skills/<dept>/workflows/<name>.md` (built-in). That's how a business customises a workflow without editing system files.

Every workflow file has the same shape: purpose, when to use, context to load, steps, quality check before handing over, what to save and where, and which steps need approval.

### v1 departments and workflows

Service-business focus. Lean on purpose: 3–6 workflows each, done well.

| Department | Built-in workflows |
|---|---|
| **HQ** | What should I work on today; weekly review; set quarterly goals; log a decision |
| **Marketing** | Social post (any platform, via platform reference files: Instagram, LinkedIn, Facebook, TikTok/Reels script, YouTube Shorts script); week of content; email newsletter; repurpose one piece into many; lead magnet; website/landing page copy |
| **Sales** | Follow up a lead; prep for a discovery call; call notes → proposal; pipeline review |
| **Delivery** | Onboard a new client; prep a session/project check-in; session notes → follow-up email; ask for a testimonial; wrap up a client |
| **Offers** | Design or refine an offer; price check; plan a launch; sales page copy |
| **Finance** | Draft an invoice; monthly numbers review; log expenses; cash-flow check |
| **Operations** | Inbox triage; plan my week in the calendar; write an SOP; tool audit |
| **Team** | Write a role (person or AI agent); write a handover |

### Business types

`setup/business-types/` holds one file per type: `coach.md`, `consultant.md`, `agency-freelancer.md`, `local-service.md`. Each says which departments and workflows to switch on first, the type-specific interview questions, and the default vocabulary (e.g. local service: "bookings" not "pipeline"). Same eight departments every time; the type changes emphasis, not structure. A new type later = one new file.

### Onboarding (setup skill)

Triggered by "set me up" or automatically when setup is unfinished. Progress lives in `business/profile.md` so it can stop and resume. Any stage can be re-run later ("redo my brand", "connect Stripe").

1. **Interview.** One question at a time. Offers a shortcut first: "Got a website, a LinkedIn profile or a doc about your business? Paste it and I'll draft the answers for you to correct." Covers: the business and type, offers, ideal customer, voice (asks them to paste 3–5 things they've written), brand (colours, fonts, logo; can read them off their website), goals. Writes `business/*`.
2. **Departments.** From the business type and answers, proposes which departments to switch on; writes each active department's `context.md` and `role.md`. Dormant departments stay as templates.
3. **Tools.** Asks what they use. For each: a click-by-click guide from `setup/connectors/<tool>.md` (claude.ai connector first, local MCP or API key fallback), then a live read-only test ("I can see your last 3 emails — correct?"). Records result in `business/tools.md`. v1 guides: Gmail, Google Calendar, Google Drive, Notion, Canva, Stripe, and a generic "any other tool" guide that searches for a connector/MCP.
4. **First win.** Runs one real workflow end to end, picked from their goals (usually a social post or a follow-up email), using everything just captured.
5. **Optional extras.** Offers (never switches on silently) a recurring weekly review or content batch, explaining how to schedule it.

### Approval rule

Written in `CLAUDE.md` and `business/rules.md`:

- Free: reading files, reading connected tools, drafting into `outputs/`.
- Needs an explicit yes, every time, showing exactly what will happen: posting or publishing anything, sending any message or email, creating calendar invites for other people, anything involving money (invoices sent, payments, refunds), deleting anything outside `outputs/`.
- The owner can loosen a specific action ("you can post to Instagram without asking"); that is recorded in `business/rules.md` with the date.

### Builder skill

When a request fits no workflow ("I run retreats"), the builder asks a few questions and writes a new workflow (or department) into `departments/` using the standard workflow shape. It never edits system files.

### Learning over time

Lightweight: when the owner corrects an output ("too formal", "never say 'journey'"), the department appends the rule to `business/voice.md` or its `context.md` and says so. Decisions go to `memory/decisions.md`.

## Decided by the maintainer

- Public, free, from scratch, fully generic: works for anyone, anywhere; no mention of any particular coach, client or business.
- For service businesses (coaches, consultants, a mix), not product sellers.
- Claude Code only. Not Cowork, Obsidian or ChatGPT.
- Onboarding interviews them and walks them step by step through connecting their tools (MCP/API), and the brain can then act through those tools.
- Plain folder repo now; plugin maybe later.
- v1 is initial setup only; no team features.

## Builder calls (the maintainer can overrule)

- Repo name `company-brain`, under kdgbalmer, MIT licence.
- Eight departments as listed; one skill per department plus setup and builder (10 skills).
- Approval rule as above.
- Scheduled jobs offered, never on by default.
- A fictional example business in `examples/` (a coach), so people can see a finished brain.
- Generated work saved as markdown in `outputs/`; graphics via the Canva connector when connected, otherwise a branded HTML graphic the owner opens in the browser and screenshots. No headless browser or other dependency, so the install stays three steps.
- Templates live inside the setup skill and onboarding creates the business folders, so updates can't overwrite their data.
- Business folders are git-ignored by default for privacy.
- Install steps state that a paid Claude plan is needed (Claude Code and claude.ai connectors require one).
- Final check is the builder doing a cold run as a non-technical owner using the example business, plus a short test script anyone can hand to a first user.

## Left to the builder

- Exact wording of every workflow and interview question (written for a non-technical solopreneur, British or neutral English).
- Current click paths in the connector guides (check against today's claude.ai UI).
- `.claude/settings.json` permission specifics.
- Name and details of the fictional example business.
