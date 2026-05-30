# Internal next-month plan template

The plan you write for yourself after every monthly audit. Never sent
to the client. Candid. Lists what to monitor, what to fix proactively,
what to ship small, and any upsell triggers that fired.

## Structure

- Client name and month covered at the top
- Section 1, monitor list, things to watch in the next 30 days
- Section 2, proactive fixes, what to ship before it becomes a problem
- Section 3, small improvements, one or two ship-this-month items
- Section 4, upsell triggers fired, from
  `upsell-trigger-checklist.md`, with the one-line pitch
- Section 5, risk notes, any churn signals or relationship issues

## Example (anonymized)

```
Client: Lakeside Animal Hospital
Month covered: May 2026

## Monitor list
- PIMS data field rename caused 2 failures this month. Watch for a
  third, escalate the fix from a workaround to a permanent guard if
  it happens again.
- Run count jumped 25 percent with the dental campaign. Confirm with
  Sarah whether June is still a dental push, scale the schedule if so.

## Proactive fixes
- Add a guard for renamed fields in the PIMS connector. Two hours of
  work, prevents the entire failure mode going forward.
- Move the daily logs to a rolling weekly digest, current setup is
  loud and the front desk has stopped reading the alerts.

## Small improvements
- Weekly summary email for Sarah, mentioned in the client email.
- No-show flag improvement is in, watch the front desk response in
  the first 2 weeks.

## Upsell triggers fired
- Trigger 2 fired: client asked twice this month about a post-visit
  survey workflow. Draft a one-line pitch for a second automation
  build, send 5 days after the recap. Pitch: "Sarah, the post-visit
  survey workflow we talked about, I can scope a build for it next
  week if you want a quick proposal." Setup 1,800, added retainer 200
  per month.

## Risk notes
- None. Sarah has been responsive, paid invoice on time, mentioned
  Lakeside is referring out to other clinics in the area.
```

## How to use it next month

- Pull this file open before running the next month's audit. The
  monitor list and proactive fixes are the questions you ask first.
- If an upsell trigger has been sitting unactioned for 60 days, either
  send the pitch or remove it. Stale triggers age out.
- If the risk notes show churn signals, escalate to a real
  conversation, do not let it ride.

## Rules

- This file is internal. Never paste it into a client email.
- Be specific. "Monitor the PIMS connector for renamed fields" beats
  "watch the system."
- Tie every upsell pitch to a real trigger from the checklist. No
  pitching for the sake of pitching.
- If the risk section is non-empty, address it in the next 7 days, not
  the next monthly cycle.
