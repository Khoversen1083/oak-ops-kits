# Daily Standup Prompt

The prompt the coach (or the global `pipeline` skill) runs against
`outputs/pipeline.csv` to produce `outputs/today-<today>.md`.

## What the standup answers

Three questions, in this order:

1. Who gets touched today, and what do I send?
2. Which replies do I respond to, and what do I say?
3. Which deals are dead and should I stop carrying?

## How to compute it

Read `outputs/pipeline.csv`. For each row, compute
`days_since_last_touch` as today minus the latest of `first_send_date`,
`fu1_date`, `fu2_date`, `fu3_date`, `reply_date`.

Apply the transitions in `stage-definitions.md`:

- `awaiting_reply` + `days_since_last_touch >= 3` → flag for FU1 today
- `awaiting_fu1` + `days_since_last_touch >= 5` → flag for FU2 today
- `awaiting_fu2` + `days_since_last_touch >= 6` → flag for FU3 today
- `awaiting_fu3` + `days_since_last_touch >= 14` → auto move to
  `closed_no_response`
- `status=replied` and no follow-up logged → flag for reply branch
- `status=soft_no` and `next_action_date <= today` → flag for re-engage

Sort the "Follow up today" section by `icp_score` descending.

## Output template

```markdown
# Pipeline Today, YYYY-MM-DD

## Follow up today (N rows)

For each row, list:
- **{company} ({owner}, ICP {score})**, last touch {N} days ago, status:
  {status}
  - Next email (draft inline, voice rules apply):
    > Subject: ...
    > Body...

## Replies to handle (N rows)

- **{company} ({owner})**, reply_type: {type}
  - Suggested branch: {branch}
  - Draft response inline.

## Dead deals to kill (N rows)

- **{company}**, 14+ days no reply. Auto-moved to closed_no_response.

## What changed today

- N rows added
- N replies received
- N booked
- N closed
```

## Stuck signal

If the CSV has 50+ rows and zero have reached `booked`, prepend this
block at the very top of the standup, above "Follow up today":

```
## Stuck signal

50+ rows in pipeline, zero booked. Stop adding rows. Either the cold
email hook is broken or the niche is wrong. Re-run the cold-email kit
or the niche-icp kit before adding another row.
```

## CSV writes the standup is allowed to make

- Move `awaiting_fu3` rows past day 14 to `closed_no_response`.
- Set `next_action` and `next_action_date` on every row in "Follow up
  today" so manual editing later does not lose the suggestion.

Nothing else. All other CSV edits are the student's job.
