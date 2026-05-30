# Build decision tree

How to pick what kind of automation to build: skill, slash command,
python script, CLI wrapper, or MCP. Ask the questions in order.
Stop at the first yes.

## The decision questions

1. Does the task only touch files on disk (rename, reformat,
   summarize, extract from documents the client already has)?
   **Use a python script.** No tool connection, no auth, no
   credentials. The cleanest first automation. File in, file out.

2. Will the user run this same prompt-pattern across many different
   client projects, in Claude Code, with their own data each time?
   **Use a skill.** Lives in `~/.claude/skills/<name>/`. The user
   types the trigger phrase, Claude loads the skill, runs it.
   Good when the pattern is reusable and the input is conversational.

3. Will the user run this from inside Claude Code with a specific
   short command like `/weekly-report`?
   **Use a slash command.** Lives in `~/.claude/commands/<name>.md`.
   Good when the user wants a fast trigger for a known
   instruction-block. Lighter than a skill, no resources folder.

4. Does the task talk to a tool or account the client owns (Gmail,
   Sheets, a CRM), and is there an existing CLI for that tool?
   **Use the CLI from inside a python script or slash command.**
   Pre-existing CLIs (`gws`, `notion-oak`, `pp-firecrawl`, etc) are
   the cheapest reliable way to touch live accounts. The CLI handles
   auth once, your script just calls it.

5. Does the task talk to a tool the client owns, no CLI exists, and
   an MCP exists for that tool?
   **Use the MCP, called from a skill or a slash command.** Apollo,
   Calendly, Stripe, HubSpot, Microsoft 365 all have MCPs. The MCP
   handles auth, you write the prompt-side logic.

6. None of the above (the task needs a tool with no CLI and no MCP)?
   **Stop. This is not a good first automation.** Pick a different
   workflow that fits one of the first 5 patterns. Build the
   CLI-or-MCP for this tool later, not on the first ship.

## Quick reference

| Situation | Pick |
|---|---|
| File in, file out, no account | Python script |
| Reusable prompt pattern, conversational input | Skill |
| Fast trigger for a known instruction block | Slash command |
| Live account, CLI exists | CLI called from script or command |
| Live account, no CLI, MCP exists | MCP called from skill or command |
| Live account, no CLI, no MCP | Not a first automation, pick again |

## Rules for the first build

- One tool per first automation. If it seems to need two, it is two
  automations. Split it.
- Read-only first. Do not give the first run write access to
  anything that matters.
- Never store API keys or tokens in the repo. .env files locally,
  excluded by .gitignore.
- Build locally on a copy of the client's real data, never on the
  only original.
- If you cannot describe the build choice in one sentence ("python
  script, because the client emails me a CSV every Monday and wants
  it reformatted"), the task is not yet small enough.

## What to write to the decision log

Write `outputs/build-decision-<today>.md` with:

```
# Build decision

Chose: <python script | skill | slash command | CLI wrapper | MCP>
For: <the task in one sentence>
Because: <one or two sentences, which question above triggered the pick>

Inputs: <where they live, the shape>
Output: <where it goes, the shape>
Tool touched: <none | name of CLI | name of MCP>
Auth handling: <none | .env file path | CLI handles it>
First-run safety: <read-only, copy of real data, sandbox folder>
```

One paragraph. The decision log is for the user 6 months from now
when they have forgotten why they picked the thing they picked.
