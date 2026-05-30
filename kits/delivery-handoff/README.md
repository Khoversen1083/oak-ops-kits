# Delivery and Handoff Kit

A pre-handoff delivery checklist, a one-page owner-facing handoff doc,
and a monitoring plan, written for your specific build, ready to use.
Turns a working automation into a delivered, retained client.

## What this kit does

You open it in Claude Code, answer 10 intake questions about the build
you just shipped, and walk out with a verification checklist for the
walkthrough call, a plain-English handoff doc the owner can keep, and a
monitoring setup so you know something broke before they do.

## Before / After

| Without kit | With kit |
|---|---|
| "It works on my machine" delivery | 3 clean runs on real data before you call it done |
| Vague handoff in a Loom that gets lost | One-page doc the owner keeps in their inbox |
| Client tells you the automation broke | You see the alert first, fix it before they notice |
| Retainer feels mysterious to the client | Plain list of what is and is not covered |

## Install in 3 steps

```bash
git clone https://github.com/Khoversen1083/oak-ops-kits.git
cd oak-ops-kits/kits/delivery-handoff
claude
```

Then type: `run the kit`

## What you'll have when you're done

- A filled delivery checklist in `outputs/delivery-checklist-<date>.md`,
  tuned to your build's schedule and output
- A one-page owner-facing handoff doc in `outputs/handoff-doc-<date>.md`,
  plain English, no tool names
- A monitoring setup checklist in `outputs/monitoring-setup-<date>.md`,
  with failure alerts pointed at your inbox and heartbeat checks for the
  silent no-run case
- A 15-minute demo script you can run on the walkthrough call

## What you need

- [Claude Code](https://claude.com/claude-code) installed
- One client build that runs end-to-end on real data (test runs do not
  count)
- A schedule for the build (day, time, timezone) or a trigger
- 30 minutes for the first run

## How long does it take

- First delivery checklist: 15 minutes
- Handoff doc draft: 10 minutes
- Monitoring setup checklist: 10 minutes
- Re-run for the next build: 20 minutes total, intake is already filled

## Want me to run this with you

If you want me live with you, walking the delivery call, watching the
monitoring fire on a real failure, calibrating the handoff doc to your
client's voice, that's the paid layer.

[Apply at https://kevhov.ai/oak-ops](https://kevhov.ai/oak-ops)
