# Claude Code First Automation Kit

Your first shipped automation in Claude Code. You open this folder,
answer a short intake, pick one boring workflow your client already
does manually, and walk out with a working automation pushed to the
client plus a one-page doc of what it does.

## What this kit does

You open it in Claude Code, answer 10 intake questions once, name one
manual workflow your client repeats at least weekly, and the coach
walks you through five steps: pick, document, build, test, deliver.
The output is a working automation in your client's hands, not a
toy demo.

## Before / After

| Without kit | With kit |
|---|---|
| Stare at Claude Code, freeze on what to build | One candidate workflow chosen in 10 minutes |
| Build a clever thing nobody asked for | Replace a real 30-plus minute task the client already pays someone to do |
| Ship the demo, never the real run | Tested against real client data before delivery |
| Forget what it does the next morning | A 1-page doc lives next to the automation |

## Install in 3 steps

```bash
git clone https://github.com/Khoversen1083/oak-ops-kits.git
cd oak-ops-kits/kits/claude-code-first-automation
claude
```

Then type: `run the kit`

## What you'll have when you're done

- A working automation in your client's workspace, in `outputs/automation-<date>/`
- A 1-page documentation file explaining what it does, in
  `outputs/automation-doc-<date>.md`
- A build-decision log showing why you picked skill vs slash command
  vs python script vs CLI vs MCP, in `outputs/build-decision-<date>.md`
- A real-data test log so you can show the client it ran clean
  before handoff

## What you need

- [Claude Code](https://claude.com/claude-code) installed
- One paying or pilot client (the automation goes to them, not a
  fake test account)
- One client workflow you have watched them do at least once,
  takes 30 minutes or more per occurrence, repeats weekly
- 60 to 90 minutes for the first run, including the build and
  the test pass

## How long does it take

- Step 1 pick the workflow: 10 minutes
- Step 2 document it: 15 minutes
- Step 3 build in Claude Code: 30 to 45 minutes
- Step 4 test against real data: 10 to 15 minutes
- Step 5 deliver to the client: 10 minutes
- Re-run for the next workflow: 45 minutes total, intake is filled

## Want me to run this with you

If you want me live with you on a call, watching you build the
first one, helping you pick the workflow that will land, that is
the paid layer.

[Apply at https://kevhov.ai/oak-ops](https://kevhov.ai/oak-ops)
