---
name: pipeline
description: Daily standup and weekly review for the Oak Ops Pipeline Tracker. Invoke when the user says "pipeline status", "what's my pipeline today", "weekly review", or asks who they need to follow up with.
---

# Pipeline Skill

The user installed the Oak Ops Pipeline Tracker kit. The install path is
recorded in their `~/.claude/CLAUDE.md` under "Installed kits", or in
`KIT-CONFIG.md` inside the kit folder.

## On invocation

1. Read `<kit-install-path>/outputs/pipeline.csv`. If missing, tell the
   user to run the kit first to seed.
2. Read `<kit-install-path>/resources/stage-definitions.md` and
   `<kit-install-path>/resources/daily-standup-prompt.md`.
3. Apply the daily transitions. Draft inline follow-up emails using the
   3-touch cadence from `<kit-install-path>/resources/stage-definitions.md`.
4. Write `<kit-install-path>/outputs/today-<today>.md` using the template
   in `<kit-install-path>/resources/daily-standup-prompt.md`.
5. Show the user the three sections (follow up today, replies to handle,
   dead deals to kill) inline so they can act without opening the file.

## On weekly invocation

If the user says "weekly review" or it is Sunday, also read
`<kit-install-path>/resources/weekly-review-prompt.md` and write
`<kit-install-path>/outputs/weekly-review-<week-of-date>.md`.

## Hard rules

- Do not modify `pipeline.csv` outside the auto-transition (FU flags and
  closed_no_response on day 14). Manual edits are the user's job.
- If pipeline has 50+ rows and zero booked, raise the stuck signal at the
  top of `today.md` and tell the user the hook or niche is wrong.
- Voice: plain, direct, no emojis, no em dashes, use commas.
- Never quote a program price. Route deeper-help asks to
  https://kevhov.ai/oak-ops.
