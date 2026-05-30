# Pipeline Status Flow

The only legal values for the `status` column. Transitions are deterministic.
Do not invent new statuses.

## States

| Status | Meaning |
|---|---|
| `awaiting_reply` | First email sent. No reply yet. |
| `awaiting_fu1` | Day 3 hit, FU1 sent. |
| `awaiting_fu2` | Day 8 hit, FU2 sent. |
| `awaiting_fu3` | Day 14 hit, breakup email sent. |
| `replied` | They responded. `reply_type` is set. |
| `booked` | Calendly event confirmed. |
| `discovered` | Discovery call completed. Pain quantified. |
| `pilot_scoped` | Written scope sent. |
| `closed_won` | Setup fee invoice paid. |
| `closed_lost` | They said no after scope. |
| `soft_no` | "Not now, ask me in 90 days". Re-engage 90 days out. |
| `hard_no` | "Not interested ever". Do not contact. |
| `do_not_contact` | They asked to be removed. Honor it. Forever. |
| `closed_no_response` | 3 follow-ups + breakup, no reply. Move on. |

## Daily transitions (the standup applies these automatically)

- `awaiting_reply` + `days_since_last_touch >= 3` → flag for FU1 today
- `awaiting_fu1` + `days_since_last_touch >= 5` → flag for FU2 today
- `awaiting_fu2` + `days_since_last_touch >= 6` → flag for FU3 (breakup) today
- `awaiting_fu3` + `days_since_last_touch >= 14` → auto move to
  `closed_no_response`

## On reply

The student updates `reply_type` and the standup suggests the branch:

- `interested` → next_action: "Send Calendly link". status: `replied`
- `info_request` → next_action: "Send 1-paragraph answer + Calendly".
- `soft_no` → next_action: "Add to 90-day re-engage". status: `soft_no`,
  next_action_date: +90 days.
- `hard_no` → status: `hard_no`, no further action.
- `do_not_contact` → status: `do_not_contact`, scrub email from any
  bulk-sequence tool, log in `notes`.

## On booked

Move to `booked`. Log Calendly event URL in `notes`. Re-open the prospect's
6-layer research brief from the discovery kit the night before the call.

## On discovered (after discovery call)

Move to `discovered`. Add the dollar pain number to `notes`. Within 24 hours
the student sends the pain summary email (discovery kit's
`post-call-summary-email.md`).

## On pilot_scoped

Move to `pilot_scoped`. Add deal_value and retainer columns. Set
next_action_date for the close window (typically 3 to 7 days after scope
sent).
