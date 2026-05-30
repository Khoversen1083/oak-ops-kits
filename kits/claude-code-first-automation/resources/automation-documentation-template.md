# Automation documentation template

Two docs, one shape. The as-is workflow doc captures how the client
does the work today, before the automation. The 1-page client doc
captures how the automation does it after, plus what the client does
when something breaks.

## As-is workflow doc (Step 2 output)

Write this to `outputs/workflow-as-is-<today>.md`.

```
# Workflow: <one-line name>

## Frequency
How often: <daily, weekly, monthly>
Trigger: <what kicks it off, a scheduled time, an incoming file, an email>

## Owner today
Who runs it: <client name, assistant name, contractor>
Time per occurrence: <minutes>

## Inputs
What comes in: <source, format, where it lives>
Example: <a real-but-redacted example, or a link to one>

## Manual steps
Numbered, in the order the operator does them today.
1. <step>
2. <step>
3. <step>

## Output
What goes out: <destination, format, who receives it>
Done looks like: <one sentence>

## What breaks
What goes wrong today: <missed appointments, late report, customer complaint>
How often: <weekly, monthly, rarely>
```

Keep it to one page. If it does not fit, the workflow is too big
for a first automation.

## 1-page client doc (Step 5 output)

Write this to `outputs/automation-doc-<today>.md`. This is the
deliverable. The client reads it, not the user.

```
# <Automation name>

## What it does
<One sentence. No jargon. The client should understand it in 10 seconds.>

## How to run it
<Exact steps. The client follows these. Three steps max.>

## Where it lives
Folder: <absolute path on the client's machine>
Triggered by: <a command, a scheduled run, a file drop>

## When it breaks
Common failure: <the most likely thing to go wrong>
What to do: <the one action the client takes, who to call if that does not work>

## In scope
- <what this automation handles>
- <what it does not handle but you might think it does>

## Out of scope
- <things the client might ask for that this version does not do>

## Owner
Built by: <user name, email>
Owned by: <client point of contact>
Last updated: <YYYY-MM-DD>
```

No mention of the kit, no mention of Claude Code internals, no
mention of `https://kevhov.ai/oak-ops`. The client doc is for the
client, not a marketing surface.

## Voice

- Plain language. Read it back to a 12-year-old, if they freeze,
  rewrite.
- No "leverages", no "agentic", no "AI-powered". Just say what it
  does.
- The client doc should fit on one printed page if they print it.
  No one prints it. They should still be able to.
