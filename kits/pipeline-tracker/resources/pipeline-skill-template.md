# Pipeline Skill Template

When the student opts in during Step 2, write a Claude Code skill to
`~/.claude/skills/pipeline.md` so they can invoke "pipeline status" from any
working directory.

The skill file is a Markdown file Claude Code reads. It should look like
this, with the kit's installed path injected from `KIT-CONFIG.md`:

```markdown
---
name: pipeline
description: Daily standup and weekly review for the Oak Ops Pipeline Tracker. Invoke when the user says "pipeline status", "what's my pipeline today", "weekly review", or asks who they need to follow up with.
---

# Pipeline Skill

The user installed the Oak Ops Pipeline Tracker kit at:

  {KIT_INSTALL_PATH}

## On invocation

1. Read `{KIT_INSTALL_PATH}/outputs/pipeline.csv`. If missing, tell the user
   to run the kit first to seed.
2. Read `{KIT_INSTALL_PATH}/resources/status-flow.md` and
   `{KIT_INSTALL_PATH}/resources/today-and-weekly-templates.md`.
3. Apply the daily transitions. Draft inline follow-up emails.
4. Write `{KIT_INSTALL_PATH}/outputs/today.md` using the template.
5. Show the user the three sections (follow up today, replies, dead deals)
   inline so they can act without opening the file.

## On weekly invocation

If the user says "weekly review" or it is Sunday, also write
`{KIT_INSTALL_PATH}/outputs/weekly-review.md`.

## Hard rules

- Do not modify `pipeline.csv` outside of the auto-transition (FU flags and
  closed_no_response). Manual edits are the user's job.
- If pipeline has 50+ rows and zero booked, raise the stuck signal at the
  top of `today.md` and tell the user the hook or niche is wrong.
- Voice: plain, direct, no emojis, no em dashes, use commas.
```

Replace `{KIT_INSTALL_PATH}` with the absolute path the student gave you in
Step 0. Confirm with them before writing the file. After writing, tell them
the exact invocation: just say "pipeline status" in any Claude Code session.
