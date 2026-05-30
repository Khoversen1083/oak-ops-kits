# Example: summary-email-lakeside-2026-05.md (worked example output)

Generated for the example audit (`example-monthly-audit.md`). Goes to
the buyer, Dr. Sarah Pham at Lakeside Animal Hospital. Casual
relationship per intake.

---

```
Subject: May recap, Lakeside reminder workflow

Hey Sarah,

This month the reminder workflow ran 1,240 times, up from 980 in
April with the dental campaign. Two short pauses both caused by a
data field your PIMS vendor renamed without notice, caught both via
the alert and fixed inside an hour. Rough estimate is the front desk
got back about 26 hours this month versus the old manual flow.

Shipped a small change on May 9, the workflow now skips the automated
reminder for any patient with a no-show in the last 30 days and flags
them for a personal call instead. Should mean fewer reminder calls
going to patients who are already drifting, and a short morning list
of the ones worth a real conversation.

Next month I will harden the PIMS field guard so the rename pattern
cannot cause another pause, and June is still dental month so the
volume should stay where it is. Will plan to circle on the post-visit
survey idea you mentioned, happy to put together a quick scope if
that is still on your mind.

Jordan
```

---

## Pre-send checklist

- Three sections, under 5 sentences each. Confirmed.
- No tool names beyond "PIMS" which Sarah uses daily. Confirmed.
- No jargon, no em dashes, no emojis. Confirmed.
- Run count (1,240) and incident count (2) match the audit doc.
- Subject line includes the month.
- BCC the internal tracker. Sent date logged.

## Skool submit block

```
Monthly Maintenance, May 2026
Client: Lakeside Animal Hospital
Retainer: 400 per month, month 7 of relationship
Runs: 1,240 (up 25 percent MoM)
Failures: 4 (all recovered, root cause patched)
Time saved (rough): 26 hours
Improvement shipped: no-show flag
Upsell triggers fired: 2 (post-visit survey ask, referral last month)
Email sent: 2026-05-30
```
