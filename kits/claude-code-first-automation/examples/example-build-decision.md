# Example: build-decision-2026-05-30.md (worked example output)

Generated for the example intake (`example-intake-filled.md`). Client:
Lin Law Group. Workflow chosen: weekly annual-review-due CSV clean
and format.

---

# Build decision

Chose: python script, called from a Claude Code slash command
For: clean the weekly annual-review-due CSV into a two-tab sheet
ready for paralegal outreach
Because: question 1 of the decision tree, the input is a CSV file
the paralegal already exports to disk, the output is a file written
to disk, no live account needs to be touched on the case management
side (read-only by policy, and there is no API anyway). Question 4
also applies for the optional final step of pushing the cleaned
sheet to Google Drive, handled by the `gws` CLI.

Inputs:
- `~/lin-law/inbox/reviews-raw-<date>.csv`, exported manually by
  the paralegal every Friday morning, columns vary slightly
  week to week, encoding is UTF-8 with BOM

Output:
- `~/lin-law/outbox/reviews-<date>.xlsx`, two tabs (new this week,
  carryover from last week), sorted by review-due date ascending,
  Address column formatted to match the letter template

Tool touched:
- `gws` CLI (Google Workspace) for the optional final step,
  uploads the .xlsx to the shared Drive folder. Auth is already
  configured on the paralegal's machine, so the script just shells
  out to `gws drive upload`.

Auth handling:
- No .env file needed. `gws` handles its own OAuth token cache in
  the paralegal's home folder. Nothing committed to the repo.

First-run safety:
- Read-only on the case management side (CSV export only, no
  write-back).
- All work happens on a copy of the export, the original stays in
  `inbox/`.
- The first three weekly runs upload to a sandbox Drive folder,
  not the live outreach folder. Jen confirms the output looks
  right before flipping the destination.

---

## Why not a skill or an MCP

- Skill: the input is a file, not a conversational prompt. A skill
  would add overhead with no benefit. Slash command plus python
  script is lighter.
- MCP: the case management software has no MCP. Google Sheets does,
  but the `gws` CLI is already on the paralegal's machine, so the
  CLI is the cheaper reliable path.
- Two-tool chain (case management plus Sheets): the case management
  side is file-only (no live connection), so this is really
  one-tool. The CSV-to-XLSX step in the middle is local pandas, no
  account.

## What would change the decision

- If the case management software added an API, we would still keep
  the CSV-export path on the first build. Live API integration is
  the next iteration, not the first ship.
- If Lin Law had no `gws` CLI configured, we would write the
  .xlsx to disk and the paralegal would drag-upload manually for
  the first month, while we get the script proven.
