# Kit Anatomy (sales-os variant)

This is a macro-kit. It does not produce a single tactical artifact like a cold email or a discovery script. It composes the tactical kits, adds the strategic content the tactical kits skip, and writes a 12-week scaling plan. The shape is similar to the tactical kits but has more steps and more resource files.

## How sales-os differs from a tactical kit

| Dimension | Tactical kit (e.g. cold-email) | Macro-kit (sales-os) |
|---|---|---|
| Intake fields | 8 to 12 | 15 to 20 |
| Steps in CLAUDE.md | 5 | 9 (Step 0 through Step 8) |
| Resource files | 3 to 6 | 11 |
| Output files per run | 2 to 5 | 7 to 9 |
| Routes to other kits | No | Yes, 5 of them |
| First-run time | 30 minutes | 60-90 minutes |
| Re-run cadence | Per niche | Quarterly |

## Required files (this kit, 20 total)

| File | Purpose |
|---|---|
| `README.md` | Public face. Outcome, before/after, install, what you get. |
| `CLAUDE.md` | The coach, 9 steps, 140-160 lines. |
| `KIT-ANATOMY.md` | This file. Describes the macro-kit shape. |
| `intake.md` | 18 fillable fields covering current state and target. |
| `bootstrap.sh` | Optional global skill installer. Bash 3.2. |
| `.gitignore` | Ignore outputs and intake-filled. |
| `resources/README.md` | Table of resource files and the order the coach reads them. |
| `resources/scaling-diagnostic.md` | 20-question diagnostic, scores 8 chapters 1-5. |
| `resources/niche-validation-5-tests.md` | The 5 tests, pass or fail per test. |
| `resources/retainer-scaling-playbook.md` | Raise, hold, drop framework per client. |
| `resources/first-setter-hire-guide.md` | Comp, recruiting, week 1 spec for first setter. |
| `resources/capacity-planning-worksheet.md` | Hours-per-client real numbers. |
| `resources/cash-flow-model.md` | Real formulas, runway math. |
| `resources/repeatable-delivery-blueprint.md` | The 80 percent template structure. |
| `resources/pricing-power-playbook.md` | When and how to raise prices. |
| `resources/productize-decision-tree.md` | When to stop customizing. |
| `resources/12-week-scaling-plan-template.md` | Week-by-week structure with checkpoints. |
| `resources/voice-rules.md` | Voice rules with sales-os specific examples. |
| `outputs/.gitkeep` | Holds empty outputs folder in git. |
| `examples/example-intake-filled.md` | Worked intake for vet clinic operator. |
| `examples/example-scaling-diagnostic-output.md` | Scored diagnostic for the example operator. |
| `examples/example-12-week-plan.md` | The 12-week plan generated for the example. |
| `examples/example-first-setter-hire-spec.md` | Setter spec generated for the example. |

## File counts and limits

- Every markdown file under 200 lines
- `intake.md` between 15 and 20 questions (macro-kit allows more than tactical)
- `CLAUDE.md` between 140 and 160 lines (more flow than tactical)
- Resources directory: 11 files, fixed (one per strategic chapter plus diagnostic plus 12-week template plus voice rules)

## Voice rules (apply to every file in every kit)

- No em dashes. Use commas.
- No emojis.
- No mention of the $3K Oak Ops program price. CTAs route to https://kevhov.ai/oak-ops.
- Builder to builder voice. Plain, direct, lowercase-comfortable.
- No "leverage", "synergy", "robust", "cutting-edge", "I hope this finds you well", "circling back", "touching base", "just following up", "agentic", "AI-powered".
- "playbook" as a noun no more than once per file.
- Never invent past clients. Never claim numeric results that are not documented.
- All bash scripts bash 3.2 compatible. No `declare -A`, no `mapfile`, no `[[ -v ]]`, no `local -n`.

## The coach pattern (this kit's variation)

The standard tactical kit pattern is Step 0 setup, Step 1 calibrate, Steps 2-N generate, Step N+1 integrate, handoff. This kit follows that shape but adds two macro-specific moves:

1. Step 1 is a diagnostic, not voice calibration. The diagnostic decides which subsequent steps run in full and which skim.
2. Step 8 is a synthesis, not just an artifact. It pulls Step 1-7 outputs into a single 12-week plan.

## When NOT to fork this kit

Do not fork sales-os for a new tactical use case. Fork `cold-email/` instead. The macro-kit shape is specific to "operator scaling from 1-3 to 5-10 clients" and should not be cloned for other strategic moments without rewriting the diagnostic.

## Validation before shipping (run from kit root)

- `bash -n bootstrap.sh` returns no errors
- `grep -rn '\xe2\x80\x94' .` returns nothing (no em dashes)
- `grep -irn '\$3,\?000\|\$3K' .` returns nothing (no program price)
- `grep -irn 'leverage\|synergy\|robust\|cutting-edge\|agentic' .` returns nothing
- `find . -type f -name '*.md' | xargs wc -l` shows every file under 200 lines
- `find . -type f | sort` matches the file list above
