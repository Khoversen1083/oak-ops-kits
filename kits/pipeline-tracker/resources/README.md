# Resources

Source-of-truth files the coach reads while running the kit. Read-only,
not student-editable. If you need to change a template, fork the repo.

| File | What it is |
|---|---|
| `pipeline-csv-schema.md` | The 23-column header row plus column definitions for `outputs/pipeline.csv`. |
| `stage-definitions.md` | The 14 legal status values, what each one means, and the day-3 / day-8 / day-14 transition rules. |
| `daily-standup-prompt.md` | The prompt the coach runs against the CSV to write `outputs/today-<date>.md`. |
| `weekly-review-prompt.md` | The prompt the coach runs Sundays (or on demand) to write `outputs/weekly-review-<date>.md`. |
| `voice-rules.md` | The hard and soft voice rules the coach enforces in every drafted email. |
| `pipeline-skill-template.md` | Mirror of `../skills/pipeline.md` for reference. The bootstrap script installs from `../skills/`, not here. |

The coach reads these in this order during a run:

1. `voice-rules.md` and `stage-definitions.md` at Step 1
2. `pipeline-csv-schema.md` at Step 2
3. `daily-standup-prompt.md` at Step 3
4. `weekly-review-prompt.md` at Step 4
