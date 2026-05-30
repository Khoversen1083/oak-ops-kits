# Monthly Maintenance Kit

A monthly review per retainer client. Audit what ran, what broke, what
improved, what to upsell. Produces a monthly review doc, a
client-facing summary email, and an internal next-month plan. Run it on
the last business day of each month, one client at a time.

## What this kit does

You open it in Claude Code, answer 10 intake questions once (your
client list and their retainer scope), then run the monthly cycle per
client. For each client, the coach walks you through an audit, writes
the client-facing summary email, and generates the internal next-month
plan with upsell triggers flagged.

## Before / After

| Without kit | With kit |
|---|---|
| End of month hits, no record of what ran | Audit doc per client, scoped to their retainer |
| "What did we even do this month" client call | Plain summary email sent before they ask |
| Retainers churn quietly after month 3 | Value made visible every 30 days |
| Upsells get missed when the moment is hot | Trigger checklist surfaces the next sale |

## Install in 3 steps

```bash
git clone https://github.com/Khoversen1083/oak-ops-kits.git
cd oak-ops-kits/kits/monthly-maintenance
claude
```

Then type: `run the kit`

## What you'll have when you're done

- A monthly audit doc per client in `outputs/audit-<client>-<month>.md`
- A client-facing summary email per client in
  `outputs/summary-email-<client>-<month>.md`
- An internal next-month plan per client in
  `outputs/next-month-<client>-<month>.md`
- Upsell triggers flagged for the clients showing buying signals
- A rhythm you can run in 20 minutes per client by month 2

## What you need

- [Claude Code](https://claude.com/claude-code) installed
- At least one paying retainer client
- Access to whatever you use to track automation runs (logs, a sheet, a
  dashboard, even rough notes)
- 30 minutes for the first client, 20 minutes per client after that

## How long does it take

- First-time setup interview: 10 minutes
- First monthly cycle for one client: 30 minutes
- Each additional client in the same cycle: 20 minutes
- Re-run next month: 20 minutes per client, intake is already filled

## Want me to run this with you

If you want me live with you, watching your screen, walking through a
real client audit, calibrating the summary email to that buyer, that
is the paid layer.

[Apply at https://kevhov.ai/oak-ops](https://kevhov.ai/oak-ops)
