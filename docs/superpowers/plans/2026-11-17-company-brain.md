# Company Brain Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A public, generic, plain-folder Claude Code repo that interviews a small service business, connects their tools, and then runs their departments' workflows as their company brain.

**Architecture:** System files (`CLAUDE.md`, `.claude/skills/*`) hold all logic; business files (`business/`, `departments/`, `outputs/`, `memory/`) are created by onboarding from templates inside the setup skill and are git-ignored. One skill per department, each routing to workflow markdown files with a fixed shape. A stdlib-only validator keeps the structure honest.

**Tech Stack:** Markdown, Claude Code skills, Python 3.9+ stdlib (validator + unittest only).

**Spec:** `docs/superpowers/specs/2026-11-17-company-brain-design.md`

## Global Constraints

- Generic: no real people, coaches, clients or businesses mentioned anywhere; examples are fictional.
- Claude Code only. No Cowork, ChatGPT or Obsidian instructions.
- Exactly ten skills: `setup`, `hq`, `marketing`, `sales`, `delivery`, `offers`, `finance`, `operations`, `team`, `builder`.
- Skill `description` ≤ 500 characters; `name` equals folder name.
- Every workflow file has these seven `##` headings, in order: `Purpose`, `Use when`, `Load first`, `Steps`, `Check before handing over`, `Save to`, `Needs a yes`.
- Repo ships no `business/`, `departments/`, `outputs/`, `memory/` at the root; `.gitignore` lists all four plus `.env`.
- Approval rule: reading and drafting are free; posting, sending, inviting others, money, and deleting outside `outputs/` need an explicit yes each time unless loosened in `business/rules.md`.
- Workflow lookup: `departments/<dept>/workflows/<name>.md` first, then `.claude/skills/<dept>/workflows/<name>.md`.
- Plain English for a non-technical owner. One question at a time in any interview.
- No runtime dependencies. Graphics = Canva connector or a self-contained HTML file the owner screenshots.
- MIT licence.

## Review Focus

- Owner says "set me up" twice or after finishing → setup offers to redo a single stage, never recreates/overwrites filled files. (Task 3: setup SKILL.md rule + validator check that templates exist.)
- Owner asks for something before setup is done → router offers to finish setup first but still helps if they insist. (Task 2: CLAUDE.md rule.)
- A request fits no department → router hands to builder, which writes into `departments/`, never `.claude/`. (Task 9 + validator banned-path rule.)
- A connector isn't available on their plan or fails the test → guide gives the fallback and marks the tool "not connected" in `tools.md`, setup continues. (Task 4: every connector guide has an "If it doesn't work" section; validator checks it.)
- A workflow links to a file that doesn't exist → validator link check fails. (Task 1.)

---

### Task 1: Skeleton and validator

**Files:**
- Create: `LICENSE`, `.gitignore`, `.env.example`, `README.md` (stub), `scripts/validate.py`, `tests/test_validate.py`

**Interfaces:**
- Produces: `python3 scripts/validate.py` → exit 0 and prints `OK` when the repo is valid; exit 1 and one line per problem otherwise. Functions: `check_repo(root: Path) -> list[str]` (list of problems).

Checks `check_repo` performs:
1. Skill set equals the ten names; each `SKILL.md` has frontmatter `name` == folder and `description` 1–500 chars.
2. Every `*.md` under any `workflows/` folder (in `.claude/skills/` and `examples/`) has the seven headings in order.
3. Every relative markdown link in any `.md` under `.claude/`, `examples/`, `README.md`, `CLAUDE.md` resolves to an existing file.
4. Required files exist: setup `templates/business/{profile,offers,customers,voice,brand,goals,tools,rules}.md`, `templates/department/{context,role}.md`, `templates/memory/decisions.md`; `business-types/{coach,consultant,agency-freelancer,local-service}.md`; `connectors/{gmail,google-calendar,google-drive,notion,canva,stripe,any-other-tool}.md`.
5. `templates/business/profile.md` contains `setup_stage:`.
6. Every connector guide contains `## If it doesn't work`.
7. `.gitignore` contains lines `business/`, `departments/`, `outputs/`, `memory/`, `.env`; none of those four folders exist at root.
8. (Removed: a banned-word list would itself leak names into the public repo. Run a one-off grep before publishing instead.)

- [ ] Write `tests/test_validate.py` (unittest): builds a minimal valid repo in a temp dir → `check_repo` returns `[]`; then one test per check that breaks it (missing skill, bad description length, missing heading, dead link, missing template, missing `setup_stage:`, connector without fallback section, root `business/` folder present, banned string) and asserts a problem mentioning the file.
- [ ] Run `python3 -m unittest discover tests -v` → fails (no module).
- [ ] Implement `scripts/validate.py`.
- [ ] Run tests → pass. Run `python3 scripts/validate.py` on the repo → fails listing missing skills (expected until later tasks).
- [ ] Commit.

### Task 2: Router and settings

**Files:** Create `CLAUDE.md`, `.claude/settings.json`

`CLAUDE.md` (under 120 lines) sections: What this folder is; First: check setup (`business/profile.md` missing or `setup_stage` not `done` → offer setup; if they insist, help with what's known); How to handle any request (route table: request type → skill); What to load (profile, voice, brand, relevant offers/customers, dept `context.md` — nothing else); Workflow lookup order; Approval rule (exact list from Global Constraints, plus "show exactly what will be sent/posted/paid"); Learning from corrections (append rule to `voice.md` or dept `context.md`, say so); End of session (append to `memory/log/YYYY-MM-DD.md`); Never (store keys in markdown, edit `.claude/` on the owner's behalf, invent facts about the business — ask instead).

`settings.json`: allow `Read`, `Glob`, `Grep`, `Write`/`Edit` within project; leave Bash and network to default prompts.

- [ ] Write both; run validator (links in CLAUDE.md resolve once skills exist; acceptable failures only for missing skills). Commit.

### Task 3: Setup skill (onboarding)

**Files:** `.claude/skills/setup/SKILL.md`; `stages/01-interview.md`, `02-departments.md`, `03-tools.md`, `04-first-win.md`, `05-extras.md`; `templates/business/*.md` (8), `templates/department/{context,role}.md`, `templates/memory/decisions.md`; `business-types/{coach,consultant,agency-freelancer,local-service}.md`.

SKILL.md: triggers ("set me up", "onboard me", "redo my brand", "connect <tool>"); reads `setup_stage` (`not-started|interview|departments|tools|first-win|extras|done`); creates folders from templates only if absent; never overwrites a filled file — re-running a stage edits in place after showing the change; updates `setup_stage` after each stage.

Stage 01: shortcut offer (paste website/LinkedIn/doc → draft answers to confirm); question order: business & type, offers, ideal customer, voice (paste 3–5 samples), brand (colours hex, fonts, logo; can read from website), goals; one question at a time; "skip" allowed and noted as `TODO` in file.
Stage 02: propose active departments from business-type file; create `departments/<dept>/{context.md,role.md,workflows/}` for active ones; role owner = the owner.
Stage 03: list tools they use; for each, follow `connectors/<tool>.md` (or `any-other-tool.md`); run the guide's read-only test; record in `business/tools.md`.
Stage 04: pick one workflow from goals (default: marketing social post), run it fully, save to `outputs/`.
Stage 05: offer recurring weekly review / content batch; explain how to schedule in Claude Code desktop; never enable silently; set `setup_stage: done`; show "what you can ask me" cheat-sheet.

Business-type files: active departments, first workflows, extra interview questions, vocabulary swaps.

- [ ] Write files; validator passes checks 4–5 for setup. Commit.

### Task 4: Connector guides

**Files:** `.claude/skills/setup/connectors/{gmail,google-calendar,google-drive,notion,canva,stripe,any-other-tool}.md`

Each: what it lets the brain do; route 1 claude.ai connector (Settings → Connectors on claude.ai, then check it shows in Claude Code via `/mcp`); route 2 local MCP / API key into `.env` (never markdown) where one exists; the read-only test to run; `## If it doesn't work` (fallback + mark "not connected" in `tools.md`, carry on). `any-other-tool.md`: search the claude.ai connector directory, then the MCP registry, then API docs; if nothing, mark manual.

- [ ] Write; validator check 6 passes. Commit.

### Task 5: Marketing skill

**Files:** `.claude/skills/marketing/SKILL.md`; `workflows/{social-post,content-week,newsletter,repurpose,lead-magnet,web-copy,branded-graphic}.md`; `platforms/{instagram,linkedin,facebook,tiktok,youtube-shorts}.md`; `assets/graphic-template.html`.

Department SKILL.md shape (used by every department in Tasks 5–8): frontmatter; Load first; routing table (request → workflow link); lookup order; approval reminder; "If nothing fits → builder".
Platform files: format, length, hook rules, hashtags, image/video sizes, posting via connector or manual.
`graphic-template.html`: self-contained, CSS variables for brand colours/fonts, 1080×1350 canvas; `branded-graphic.md` fills it from `brand.md` and saves to `outputs/marketing/`.

- [ ] Write; validator passes for marketing. Commit.

### Task 6: Sales and Delivery skills

Sales `workflows/{lead-follow-up,discovery-call-prep,call-to-proposal,pipeline-review}.md`. Delivery `workflows/{client-onboarding,session-prep,session-follow-up,testimonial-request,client-wrap-up}.md`. Delivery workflows note client notes are private and stay in `outputs/`/`departments/`.

- [ ] Write; validate; commit.

### Task 7: HQ and Offers skills

HQ `workflows/{today,weekly-review,quarterly-goals,log-decision}.md` (weekly-review reads `memory/log/` and `goals.md`). Offers `workflows/{design-offer,price-check,launch-plan,sales-page}.md`.

- [ ] Write; validate; commit.

### Task 8: Finance, Operations, Team skills

Finance `workflows/{invoice,monthly-numbers,expense-log,cash-flow-check}.md` (invoice sending = needs a yes). Operations `workflows/{inbox-triage,plan-week,write-sop,tool-audit}.md`. Team `workflows/{write-role,handover}.md` (role works for a person or an AI agent).

- [ ] Write; validate; commit.

### Task 9: Builder skill

**Files:** `.claude/skills/builder/SKILL.md`, `.claude/skills/builder/workflow-template.md` (the seven headings, blank).

Builder: asks ≤5 questions, writes new workflow to `departments/<dept>/workflows/<slug>.md` (or a new `departments/<new-dept>/` with context/role/workflows), adds a line to that dept's `context.md` listing custom workflows, never writes in `.claude/`. The router (CLAUDE.md) and department SKILL.md files check `departments/<dept>/workflows/` for custom ones.

- [ ] Write; validate; commit.

### Task 10: Example business

**Files:** `examples/harbour-coaching/` mirroring a finished brain: `business/*` filled for a fictional career coach, `departments/{marketing,sales,delivery}/{context,role}.md`, one custom workflow `departments/delivery/workflows/group-programme-kickoff.md`, two `outputs/` samples, `memory/decisions.md`.

- [ ] Write; validator passes (workflow headings, links, banned strings). Commit.

### Task 11: README, test script, cold run

**Files:** `README.md` (what it is; what you need: paid Claude plan + Claude Code desktop app; 3-step install: download ZIP or clone → open folder in Claude Code → type "set me up"; what to ask it; privacy note on git-ignored folders and backups; updating: copy `.claude/`, `CLAUDE.md`, `README.md` over; adding your own workflows; licence), `docs/test-script.md` (a first-user walkthrough with pass/fail checks).

- [ ] Write; `python3 scripts/validate.py` → `OK`; unittest passes.
- [ ] Cold run: copy repo to a scratch dir, run `claude -p` with "set me up" as a fictional owner for the interview's first turns and one workflow request; confirm it routes to setup, then marketing, and writes to the right folders. Fix anything found.
- [ ] Commit.

### Task 12: Publish

- [ ] `gh repo create kdgbalmer/company-brain --public --source . --push --description "A Claude Code second brain for small service businesses"`.
- [ ] Confirm the repo page renders the README.
