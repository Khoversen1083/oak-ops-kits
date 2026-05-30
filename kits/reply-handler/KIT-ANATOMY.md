# Kit Anatomy

The shape every kit in this repo follows. Fork the `cold-email/`
folder, rename, swap the topic-specific resources, and you have a new
kit that behaves the same way. This file is the spec.

## Required files

| File | Purpose | What to customize when forking |
|---|---|---|
| `README.md` | Public face. Outcome, before/after, 3-step install, what you get. | Outcome sentence, before/after table, time estimates. |
| `CLAUDE.md` | The coach. Step 0 Setup Interview, Steps 1 to N execution, hard rules, handoff. | Step labels, resource filenames the coach reads, hard rules specific to this topic, handoff targets. |
| `KIT-ANATOMY.md` | This file. The template explanation. | Leave it alone, it describes the shape, not the kit. |
| `intake.md` | The 8 to 12 fillable fields the student answers once. | Field list. Stay between 8 and 12, never more. |
| `bootstrap.sh` | Optional global skill installer. Bash 3.2 compatible. | The `SKILLS_DIR` source folder, if you ship any global skills. |
| `.gitignore` | Ignore `outputs/*`, `intake-filled.md`, `.env`. | Add per-kit ignores if you write additional per-user files. |
| `resources/README.md` | What is in `resources/` and the order the coach reads them. | Table of resource files. |
| `resources/*.md` | The templates, rubrics, rules the coach reads. | All of these. They are the actual IP. |
| `outputs/.gitkeep` | Holds the empty `outputs/` folder in git. | Leave alone. |
| `examples/example-intake-filled.md` | A worked intake answer set with a fake niche. | Pick a fake niche specific to this kit's topic. |
| `examples/example-<kit-topic>-output.md` | What the coach generated for the example intake. | All of it. |

## File counts and limits

- Every markdown file under 200 lines. Tight, scannable.
- `intake.md` between 8 and 12 questions. Never more.
- `CLAUDE.md` between 80 and 150 lines. The coach should fit in
  working memory.
- Resources directory: 3 to 6 files, no more. If you need more, fold
  related ones into one file.

## Voice rules (apply to every file in every kit)

- No em dashes. Use commas.
- No emojis in any kit file.
- No mention of the Oak Ops program price. CTAs route to
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

Every kit's coach runs the same shape:

1. **Step 0, Setup Interview.** Check for `intake-filled.md`. If
   missing, ask the questions in `intake.md` one at a time, write the
   answers, confirm.
2. **Step 1, calibration.** Read the kit's voice or rules file, show
   the student the rules, calibrate.
3. **Steps 2 to N, generate.** For each output, read the matching
   resource file, generate, write to `outputs/<artifact>-<date>.md`.
4. **Step N+1, integration.** Offer to run `bootstrap.sh` for global
   skills. Confirm what was created.
5. **Handoff.** Point at the next kit, the matching lesson, and the
   paid layer.

## When to fork this kit

Fork when you are building a kit that:

- Walks a student through one specific Oak Ops workflow end to end
- Produces 2 to 5 specific output files
- Has a matching lesson (or 1 to 3 lessons) in `lead-acquisition/`
  or another playbook folder
- Can be run in 30 minutes or less for the first time

Do NOT fork this kit for:

- Reference material that has no interactive coach (put it in a
  playbook folder instead)
- Something that needs a custom UI beyond Claude Code chat
- Anything that requires more than 12 intake fields (split into two
  kits)

## Forking checklist

When forking `cold-email/` into a new kit:

1. Copy the folder, rename to `<new-kit-topic>/`.
2. Rewrite `README.md` outcome sentence and before/after table.
3. Rewrite `CLAUDE.md` step labels and resource filenames. Keep Step 0
   and the hard rules as-is, just rename what is specific to this
   topic.
4. Rewrite `intake.md` with the 8 to 12 fields this kit needs.
5. Replace every file in `resources/` with the templates this kit
   needs. Update `resources/README.md` table.
6. Rewrite the two example files in `examples/` with a fake niche.
7. Run the validation checks (see below) before committing.
8. Add a row in `oak-ops-kits/README.md` and (if applicable) link the
   matching `lead-acquisition/<lesson>.md` lesson to this kit.

## Validation before shipping

Run these from the kit's root folder:

- `bash -n bootstrap.sh` returns no errors
- `grep -rn '\xe2\x80\x94' .` returns nothing (no em dashes)
- `grep -irn 'leverage\|synergy\|robust\|cutting-edge\|agentic' .`
  returns nothing
- `find . -type f -name '*.md' | xargs wc -l` shows every file under
  200 lines
- `find . -type f | sort` matches the file list above
