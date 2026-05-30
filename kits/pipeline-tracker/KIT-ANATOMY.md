# Kit Anatomy

The shape every kit in this repo follows. This kit was forked from
`cold-email/`. Read the canonical anatomy at
`../cold-email/KIT-ANATOMY.md`, this file is a thin mirror so the
pipeline-tracker kit is self-contained.

## Required files

| File | Purpose |
|---|---|
| `README.md` | Public face. Outcome, before/after, 3-step install. |
| `CLAUDE.md` | The coach. Step 0 Setup Interview, Steps 1 to 5. |
| `KIT-ANATOMY.md` | This file. The template explanation. |
| `intake.md` | The 10 fillable fields the student answers once. |
| `bootstrap.sh` | Optional global skill installer. Bash 3.2 compatible. |
| `.gitignore` | Ignore `outputs/*`, `intake-filled.md`, `KIT-CONFIG.md`. |
| `resources/README.md` | What is in `resources/` and the read order. |
| `resources/*.md` | The templates, rubrics, rules the coach reads. |
| `outputs/.gitkeep` | Holds the empty `outputs/` folder in git. |
| `outputs/pipeline.csv.template` | The 23-column header row, no data. |
| `examples/example-intake-filled.md` | Worked intake with a fake niche. |
| `examples/example-pipeline-csv.md` | 15 fake prospects across stages. |
| `examples/example-daily-standup-output.md` | Worked daily standup. |
| `examples/example-weekly-review-output.md` | Worked weekly review. |

## File counts and limits

- Every markdown file under 200 lines. Tight, scannable.
- `intake.md` between 8 and 12 questions. This kit has 10.
- `CLAUDE.md` between 80 and 150 lines.
- Resources directory: 3 to 6 files, this kit has 6.

## Voice rules (apply to every file in every kit)

- No em dashes. Use commas.
- No emojis in any kit file.
- No mention of the $3K Oak Ops program price. CTAs route to
  `https://kevhov.ai/oak-ops`.
- Builder to builder voice. Plain, direct, lowercase-comfortable.
- No "leverage", "synergy", "robust", "cutting-edge", "I hope this finds
  you well", "circling back", "touching base", "just following up",
  "agentic", "AI-powered".
- Never invent past clients. Never claim numeric results that are not
  documented.
- All bash scripts must be bash 3.2 compatible. No `declare -A`, no
  `mapfile`, no `[[ -v ]]`, no `local -n`.

## The coach pattern (every CLAUDE.md follows this)

1. Step 0, Setup Interview. Check for `intake-filled.md`. If missing, ask
   the questions in `intake.md` one at a time.
2. Step 1, calibration. Read the kit's voice and stage rules.
3. Steps 2 to N, generate. For each output, read the matching resource
   file, generate, write to `outputs/`.
4. Step N+1, integration. Offer to run `bootstrap.sh` for the global
   skill.
5. Handoff. Point at the next kit, the matching lesson, and the paid
   layer.

## Validation before shipping

Run these from the kit's root folder:

- `bash -n bootstrap.sh` returns no errors
- `grep -rn $'\xe2\x80\x94' .` returns nothing (no em dashes)
- `grep -irn '\$3,\?000\|\$3K' .` returns only KIT-ANATOMY banlist hits
- `grep -irn 'leverage\|synergy\|robust\|cutting-edge\|agentic' .`
  returns only KIT-ANATOMY banlist hits
- `find . -type f -name '*.md' | xargs wc -l` shows every file under
  200 lines
