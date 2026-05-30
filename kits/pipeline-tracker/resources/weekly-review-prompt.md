# Weekly Review Prompt

The prompt the coach (or the global `pipeline` skill) runs on Sundays,
or any time the student says "weekly review", to produce
`outputs/weekly-review-<week-of-date>.md`.

## What the weekly review answers

Two questions, in this order:

1. What moved this week (rows in, replies, booked, closed)?
2. What is the one thing to change next week?

Not three things. Not five. One.

## How to compute it

Read `outputs/pipeline.csv`. Filter to rows where any of
`first_send_date`, `fu1_date`, `fu2_date`, `fu3_date`, `reply_date`,
`next_action_date` falls inside the last 7 days.

Compute conversion per stage across the full pipeline (not just this
week's rows), because small weekly samples are noisy:

- Sent to replied: replies / total sent
- Replied to booked: booked / replied
- Booked to discovered: discovered / booked
- Discovered to pilot_scoped: pilot_scoped / discovered
- Pilot_scoped to closed_won: closed_won / pilot_scoped

## Output template

```markdown
# Pipeline Weekly Review, Week of YYYY-MM-DD

## Movement this week

- New rows added: N
- Replies received: N (interested: X, info_request: Y, soft_no: Z,
  hard_no: Z, do_not_contact: Z)
- Booked calls: N (who: list, source: list)
- Discoveries run: N
- Pilots scoped: N
- Closed won: N (deal_value rollup: $X)

## Conversion (full pipeline, not just this week)

- Sent to replied: N%
- Replied to booked: N%
- Booked to discovered: N%
- Discovered to pilot_scoped: N%
- Pilot_scoped to closed_won: N%

## The one thing to change next week

One concrete change. Based on where the funnel narrowed most.

- If sent to replied is below 3%, rewrite the cold email hook.
- If replied to booked is below 50%, tighten the Calendly reply.
- If booked to discovered is below 70%, send a confirmation email 24
  hours before the call.
- If discovered to pilot_scoped is below 60%, your discovery is not
  quantifying the dollar pain, re-run the discovery kit.
- If pilot_scoped to closed_won is below 30%, the scope is too big or
  the price is wrong, re-run the pricing-retainer kit.
```

## What the weekly review never does

- Never edits `pipeline.csv`. It is read-only on Sunday.
- Never lists more than one change to make next week. One.
- Never compares this week to last week (the kit does not store week
  snapshots yet, future version).
