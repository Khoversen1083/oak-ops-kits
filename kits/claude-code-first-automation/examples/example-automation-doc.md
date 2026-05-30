# Example: automation-doc-2026-05-30.md (worked example output)

Generated for the example intake (`example-intake-filled.md`). Client:
Lin Law Group, estate-planning practice. The workflow chosen was
candidate A: the weekly export-clean-paste for clients due for an
annual review. All names and numbers below are fictional.

---

# Annual Review List Cleaner

## What it does

Takes the weekly CSV export from the case management software and
produces a clean two-tab Google Sheet ready for the paralegal to
start outreach. Cuts the prep from 90 minutes to about 5.

## How to run it

1. Friday morning, export the "Annual Reviews Due, Next 30 Days"
   CSV from the case management software, save it to
   `~/lin-law/inbox/`.
2. Open Claude Code in `~/lin-law/`, type `run weekly review`.
3. The cleaned sheet lands at `~/lin-law/outbox/reviews-<date>.xlsx`,
   ready to upload to the shared Drive folder.

## Where it lives

Folder: `/Users/jen/lin-law/`
Triggered by: typing `run weekly review` inside Claude Code
Runs on: Jen's MacBook, locally, no cloud upload

## When it breaks

Common failure: the CSV export has a new column the practice
manager turned on in the case management software, the automation
flags the new column instead of guessing.

What to do: open the CSV in Numbers, confirm the new column is
expected, run the automation again with the same file. It will
ask whether to include or skip the new column. Pick one, it
remembers for next week. If it still fails, email the builder.

## In scope

- Cleaning the weekly review-due export
- Deduplicating against last week's run (no client appears two
  weeks in a row)
- Formatting the Address column the way the letter template expects
- Sorting by review-due date ascending

## Out of scope

- Sending the outreach emails. The automation prepares the list.
  The paralegal still drafts and sends in Gmail.
- Updating the case management software. Read-only on that side.
- Pulling intake-form data (that is a separate automation, planned
  for week 3).

## Owner

Built by: Jordan Mills, jordan@millsautomation.com
Owned by: Jen at Lin Law Group
Last updated: 2026-05-30

---

## Post-delivery checklist

- Handoff call booked with Jen for next Friday morning, watch her
  run it once, hand over ownership
- Doc lives at `~/lin-law/README.md` next to the automation, not
  in a separate Drive folder Jen will forget about
- Next workflow scoped: candidate B (the annual review reminder
  letter draft) is queued for week 3
- Pilot status note: at end of week 2, ask Mara for the
  testimonial and case study commitment described in the pilot
  agreement

## Skool submit block

```
First Automation Shipped
Client: Lin Law Group (pilot, no money)
Workflow automated: weekly annual-review-due CSV clean and format
Time saved: 90 minutes per week, ~78 hours per year
Build pick: python script with the Google Sheets CLI
Real-data test: passed, 47 rows in, 47 rows out, 3 duplicates dropped vs last week
Delivered: 2026-05-30, doc next to the script in the client folder
```
