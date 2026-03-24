# Open Book — Client Project Plans

Live, client-facing project plan dashboards hosted on GitHub Pages. Each client gets a clean web page — shareable via URL, always current, no PDF needed. Team members can edit dates and mark milestones done directly in the browser. Date changes sync back to Monday.com automatically.

**Live site:** [plans.teamopenbook.com](https://plans.teamopenbook.com)

---

## Active clients

| Client | URL | Status |
|---|---|---|
| Stony Brook School | [plans.teamopenbook.com/stony-brook](https://plans.teamopenbook.com/stony-brook) | Live |
| Holy Family Ministries | [plans.teamopenbook.com/holy-family](https://plans.teamopenbook.com/holy-family) | To add |

---

## Repo structure

```
openbook-client-plans/
├── _template/
│   └── index.html    ← master template — never edit this directly
├── stony-brook/
│   └── index.html    ← working example
├── holy-family/
│   └── index.html    ← add next
└── README.md
```

Each client is a folder with a single `index.html` file. That's the whole site.

---

## Two URLs per client

| URL | Who it's for | What it does |
|---|---|---|
| `plans.teamopenbook.com/CLIENT-NAME` | Client | Read-only view |
| `plans.teamopenbook.com/CLIENT-NAME?key=ob-team-2026` | Team only | Enables editing |

Password for the "Team" button (bottom right of any page): `ob-team-2026`

---

## What you can do in the browser — no GitHub needed

Open the team URL. In team mode:

- **Edit a date** — click it, type the new date, Save. Syncs to Monday automatically.
- **Mark a milestone done** — hover the row, click ✓ Mark done.
- **Add a milestone** — click + Add milestone at the bottom of the table.
- **Reorder rows** — drag the ⠿ handle on the left of any row.
- **Filter by workstream** — use the pill buttons above the milestone table.
- **Show/hide completed** — toggle on the right side of the filter bar.

---

## Adding a new client plan

### Step 1 — Get Monday subitem IDs (5 min)

Ask Claude: *"Pull the milestone subitem IDs for [CLIENT NAME] from Monday board 18397531209."*

You'll get a list like:
```
11278184073 | Apr 9  | Present Messaging Guide to Client
11518218163 | Apr 14 | Calibration Session
```

### Step 2 — Duplicate the template (1 min)

1. Open `_template/index.html` → pencil icon → Select all → Copy
2. Repo root → Add file → Create new file
3. Name it `CLIENT-NAME/index.html`
4. Paste — don't commit yet

### Step 3 — Fill in client data (20 min)

**Header:** replace `CLIENT_NAME` and `MONTH DD, YYYY`

**Project Overview table:** replace workstream rows, set status classes:
- `pill-complete` / `pill-active` / `pill-upcoming`

**Key Milestones table — row types:**

```html
<!-- Completed -->
<tr class="row-done" data-ws="Workstream Name">

<!-- Approval or key meeting -->
<tr class="row-approval" data-id="MONDAY_SUBITEM_ID" data-ws="Workstream Name">

<!-- Standard upcoming -->
<tr data-id="MONDAY_SUBITEM_ID" data-ws="Workstream Name">

<!-- No Monday subitem (e.g. on-site event) -->
<tr data-id="null" data-ws="Workstream Name">
```

> ⚠️ Every upcoming row needs `data-ws="Workstream Name"` — this powers the filter pills. Match the name exactly to what's in the Project Overview table.

**Project Close table:** update close date and 90-day check-in dates.

### Step 4 — Commit (1 min)

Commit message: `Add [CLIENT NAME] project plan`

Live in ~60 seconds.

---

## GitHub edits needed for

- Adding a Monday subitem ID to a newly added milestone row
- Updating workstream status pills in the Project Overview table
- Changing the project title or close dates in the header
- Creating a new client plan

To give someone edit access: **Settings → Collaborators → Add people**. Web editor only — no terminal needed.

---

## How Monday sync works

Date edits fire a GraphQL mutation to Monday's API:

- **Column:** `timerange_mm00qh4t` on board `18397531209`
- **Mutation:** `change_subitem_column_value` — subitems require this, not `change_column_value`
- **Format:** `{ "from": "2026-04-09", "to": "2026-04-09" }` (same date for start/end)
- **Rows with `data-id="null"`** skip Monday sync — update locally only

The Monday API token is hardcoded in the `<script>` block near the top of each `index.html`. Rotate it in every client file if it expires.

---

## Known issues fixed (March 2026)

Two bugs in the original build were corrected:

1. **Drag to reorder** — function referenced wrong tbody ID (`ms-body` → `milestone-body`). Fixed.
2. **Monday date sync** — used `change_column_value` instead of `change_subitem_column_value`. Fixed.

If either breaks again, check these first.

---

## DNS

`plans.teamopenbook.com` → CNAME → `open-book-communications.github.io`

Domain verified via TXT record at `_github-pages-challenge-Open-Book-Communications.plans.teamopenbook.com`.

> If the domain stops resolving after any account changes, re-verify in **org Settings → Pages → Verified domains**.

---

## Full documentation

Internal setup guide and operator notes live in Notion → Apps → **Client Project Plans — System Documentation**.

---

*Built March 2026 · Open Book Communications · Minneapolis, MN*
