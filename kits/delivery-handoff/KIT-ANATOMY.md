# Kit Anatomy

This file describes the shape of the Delivery and Handoff kit. The same
shape is used by every kit in this repo (see `../cold-email/KIT-ANATOMY.md`
for the canonical spec). This is a local copy with the file list for
this kit.

## Required files

| File | Purpose |
|---|---|
| `README.md` | Public face. Outcome, before/after, 3-step install, what you get. |
| `CLAUDE.md` | The coach. Step 0 Setup Interview, Steps 1 to 6 execution, hard rules, handoff. |
| `KIT-ANATOMY.md` | This file. The template explanation. |
| `intake.md` | The 10 fillable fields the student answers once. |
| `bootstrap.sh` | Global skill installer. Bash 3.2 compatible. |
| `.gitignore` | Ignores `outputs/*`, `intake-filled.md`, `.env`. |
| `resources/README.md` | What is in `resources/` and the order the coach reads them. |
| `resources/delivery-checklist.md` | The pre-handoff verification checklist. |
| `resources/handoff-doc-template.md` | The owner-facing one-pager template. |
| `resources/monitoring-setup-checklist.md` | Failure alerts, heartbeat, sanity checks, rate limits. |
| `resources/demo-script-template.md` | The 15-minute walkthrough call script. |
| `resources/voice-rules.md` | The hard and soft voice rules the coach enforces. |
| `outputs/.gitkeep` | Holds the empty `outputs/` folder in git. |
| `examples/example-intake-filled.md` | A worked intake answer set with a fake build. |
| `examples/example-handoff-doc.md` | What the coach generated for the example intake. |
| `examples/example-monitoring-setup.md` | The monitoring plan generated for the example. |

## File counts and limits

- Every markdown file under 200 lines. Tight, scannable.
- `intake.md` between 8 and 12 questions. This kit has 10.
- `CLAUDE.md` between 80 and 150 lines.
- Resources directory: 3 to 6 files. This kit has 5 plus the index.

## Voice rules (apply to every file in every kit)

- No em dashes. Use commas.
- No emojis in any kit file.
- No mention of the $3K Oak Ops program price. CTAs route to
  `https://kevhov.ai/oak-ops`.
- Builder to builder voice. Plain, direct, lowercase-comfortable.
- No "leverage", "synergy", "robust", "cutting-edge", "I hope this
  finds you well", "circling back", "touching base", "just following
  up", "agentic", "AI-powered".
- Never invent past clients. Never claim numeric results that are not
  documented.
- All bash scripts must be bash 3.2 compatible. No `declare -A`, no
  `mapfile`, no `[[ -v ]]`, no `local -n`.

## The coach pattern (every CLAUDE.md follows this)

1. **Step 0, Setup Interview.** Check for `intake-filled.md`. If
   missing, ask the questions in `intake.md` one at a time, write the
   answers, confirm.
2. **Step 1, calibration.** Read the kit's voice rules file, show
   the student the rules, calibrate.
3. **Steps 2 to N, generate.** For each output, read the matching
   resource file, generate, write to `outputs/<artifact>-<date>.md`.
4. **Step N+1, integration.** Offer to run `bootstrap.sh` for global
   skills. Confirm what was created.
5. **Handoff.** Point at the next kit, the matching lesson, and the
   paid layer.

## What this kit produces

Three output files, one per phase of delivery:

1. `outputs/delivery-checklist-<date>.md`, the verification checklist
   the student runs before saying "it's done"
2. `outputs/handoff-doc-<date>.md`, the one-page owner-facing handoff
   plus the demo script for the walkthrough call
3. `outputs/monitoring-setup-<date>.md`, the failure alert, heartbeat,
   sanity check, and rate limit configuration tuned to the build

## Validation before shipping

Run these from the kit's root folder:

- `bash -n bootstrap.sh` returns no errors
- `grep -rn '\xe2\x80\x94' .` returns nothing (no em dashes)
- `grep -irn '\$3,\?000\|\$3K' .` returns nothing (no program price)
- `grep -irn 'leverage\|synergy\|robust\|cutting-edge\|agentic' .`
  returns nothing
- `find . -type f -name '*.md' | xargs wc -l` shows every file under
  200 lines
- `find . -type f | sort` matches the file list above
