# Pipeline Tracker Kit

One CSV that owns every prospect across every stage, a daily standup that
tells you who to touch today, a weekly review that tells you what to cut.
Operationalizes lesson 9 of the Lead Acquisition Playbook.

## What this kit does

You open it in Claude Code, answer 10 intake questions once, point it at
whatever prospect data you already have (spreadsheet, Notion, inbox, or
nothing), and walk out with a working `pipeline.csv`, a daily standup
file, and a global `pipeline status` command you can run from any folder.

## Before / After

| Without kit | With kit |
|---|---|
| Track prospects in your head, lose half | One CSV, every prospect, every stage |
| Forget who needs FU2 today | Standup tells you, sorted by ICP score |
| Notice a dead deal three weeks late | Auto-killed at day 14, no reply |
| Guess where the funnel is leaking | Weekly review prints conversion per stage |

## Install in 3 steps

```bash
git clone https://github.com/Khoversen1083/oak-ops-kits.git
cd oak-ops-kits/kits/pipeline-tracker
claude
```

Then type: `run the kit`

## What you'll have when you're done

- A seeded `outputs/pipeline.csv` with the canonical 23-column schema
- A daily standup template that writes `outputs/today.md` on demand
- A weekly review template that writes `outputs/weekly-review.md` Sundays
- An optional global `pipeline` skill at `~/.claude/skills/pipeline.md` so
  you can ask any Claude Code session "pipeline status" from any folder
- Stage definitions so you stop arguing with yourself about what counts
  as Contacted vs Replied

## What you need

- [Claude Code](https://claude.com/claude-code) installed
- A locked niche (one industry, one buyer profile)
- A calendar link (Calendly, Cal.com, anything that books a meeting)
- 20 minutes for the first run

## Daily use

From any folder where Claude Code is running:

> `pipeline status`

Reads your CSV, applies the day-3 / day-8 / day-14 transitions, drafts
your next-touch emails inline, writes `outputs/today.md`.

## Weekly use

> `weekly review`

Writes `outputs/weekly-review.md` with conversion per stage and the one
thing to change next week.

## Want me to run this with you

If you want me live with you, watching your screen, calibrating the
stages to how you actually sell, troubleshooting the pipeline that has
50 rows and zero booked, that's the paid layer.

[Apply at https://kevhov.ai/oak-ops](https://kevhov.ai/oak-ops)
