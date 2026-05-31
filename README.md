# Oak Ops Kits

Open-source Claude Code kits for the lead acquisition, discovery, pricing,
delivery, and pipeline workflows I use to sell automation builds.

Built by [Kevin Hoversen](https://kevhov.ai). Enterprise SaaS background,
$25M to $50M ATVs. These are the same playbooks I run, stripped of the
client-specific noise.

## What this repo is

Three things:

1. **`kits/`** — 11 self-contained Claude Code kits. 10 are tactical (one
   workflow each: niche, cold email, reply handler, pipeline tracker,
   discovery, pricing, delivery, monthly maintenance, first automation,
   content engine offer sheet). 1 is `sales-os`, the macro-kit that
   orchestrates the tactical kits into a 12-week scaling plan for operators
   with 1-3 clients moving to 5-10. Each kit interviews you, integrates into
   your CLAUDE.md, then runs.
2. **`skills/`** — 13 Claude Code skills I use daily (lead scraping, cold
   email setup, browser automation, content production, client onboarding).
   Drop into `~/.claude/skills/` and Claude picks them up automatically.
3. **`lead-acquisition/`** — the 9-lesson Lead Acquisition Playbook. Read
   it like a book, jump to the kit for whichever step you're stuck on.

### Kit structure

A kit is a small, self-contained directory with:

- `CLAUDE.md` — a coach that interviews you, integrates into your workspace,
  and runs the system
- `resources/` — the templates, rubrics, criteria the coach reads
- `outputs/` — where your generated files land (your work, not committed)
- `README.md` — install + use in two minutes

Drop any kit folder into your Claude Code workspace, open it, tell Claude
"run the kit". The first thing Claude does is the Setup Interview: where am
I living, do you have a CLAUDE.md, what tools do you have on PATH, what's
your business in one paragraph. After the interview Claude writes a
`KIT-CONFIG.md` snapshot and a 3-line "Installed kits" section into your
root `CLAUDE.md`, then runs the kit.

## Lead Acquisition Playbook

The headline. The 9-lesson sequence I teach paid students. Lives in
`lead-acquisition/`. Read it like a book or jump to the kit for whichever
step you're stuck on.

| Lesson | Topic | Kit |
|---|---|---|
| 1 | Lock the niche | `kits/niche-icp/` |
| 2 | ICP scoring | `kits/niche-icp/` |
| 3 | Scale from 25 to 200 targets | `kits/niche-icp/` |
| 4 | Source leads (Apollo + Google Maps) | included in niche-icp |
| 5 | Prospect research brief | `kits/niche-icp/` |
| 6 | 3-sentence cold email | `kits/cold-email/` |
| 7 | Follow-up sequence | `kits/cold-email/` |
| 8 | Decision tree per reply type | `kits/reply-handler/` |
| 9 | Pipeline tracker | `kits/pipeline-tracker/` |

## All kits

| Kit | What it does |
|---|---|
| `niche-icp` | Picks a niche, scores 25 to 200 targets, sources leads |
| `cold-email` | 3-sentence email + 3-touch follow-up sequence |
| `reply-handler` | Decision tree per reply type, drafts the response |
| `pipeline-tracker` | Daily standup, weekly review, "pipeline status" |
| `discovery-call` | Pre-call brief, live script, post-call summary email |
| `pricing-retainer` | Setup fee and retainer pricing tree, scope control |
| `delivery-handoff` | Build delivery + handoff doc + monitoring |
| `monthly-maintenance` | Retainer rhythm, monthly review template |
| `claude-code-first-automation` | First production automation, from scratch |
| `content-engine-offer-sheet` | Personal brand content engine for inbound |
| `sales-os` | Macro-kit. 12-week scaling plan, scaling diagnostic, retainer scaling, first setter hire, capacity planning, cash flow model. For operators with 1-3 clients moving to 5-10. |

## Install

You need [Claude Code](https://claude.com/claude-code).

```bash
git clone https://github.com/Khoversen1083/oak-ops-kits.git
cd oak-ops-kits/kits/<the-kit-you-want>
claude
> run the kit
```

The kit's first move is the Setup Interview. Answer in your own words. Then
it runs.

## Want me to run these with you

The paid layer is the Oak Ops Skool community, where I:

- Walk you through the Lead Acquisition Playbook live with feedback
- Add the Apollo-scaling deep-dive, advanced pipeline-tracker features,
  closer-call script
- Weekly group Q&A
- 1:1 access

Apply: [https://kevhov.ai/oak-ops](https://kevhov.ai/oak-ops)

## License

MIT. Use them, fork them, build on them. Attribution appreciated, not
required.

## Voice

Plain. Direct. No emojis. No em dashes. Builder to builder.
