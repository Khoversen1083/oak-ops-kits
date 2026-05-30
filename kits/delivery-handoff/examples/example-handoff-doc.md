# Example: handoff-doc-2026-05-30.md (worked example output)

Generated for the example intake (`example-intake-filled.md`). Fake
client [acme-distribution], daily order summary build.

---

```
ACME-DISTRIBUTION AUTOMATION HANDOFF
Prepared by Mills Automation
Effective Date: 2026-06-08

WHAT IT DOES

Every weekday morning, the new orders from the orders spreadsheet are
summarized into one clean email to Dana. No manual lookup, no tab
scanning. Three sections: new orders, orders waiting on stock, orders
ready to ship.

HOW TO RUN IT

It runs every weekday at 7am Eastern. Dana does not need to do
anything. Saturdays and Sundays it does not run. If a federal holiday
falls on a weekday, it still runs.

WHAT YOU SHOULD SEE

An email in Dana's inbox by 7:15am with the subject "Daily Order
Summary, [date]". Three sections: new orders this morning, orders
waiting on stock, orders ready to ship. Numbers reflect everything
posted since the previous business day at 5pm Eastern.

WHAT 'BROKEN' LOOKS LIKE

If the email does not hit Dana's inbox by 7:30am on a weekday,
something has gone wrong. Do nothing. I am alerted before you are,
will have it fixed and explained to you by 9am. If the email arrives
but the order count looks wrong (zero orders on a normal weekday, or
last week's numbers showing instead of this week's), reply to that
email, I will check it the same day.

WHO TO CALL

Jordan Mills
Mills Automation
jordan@millsautomation.com
I check this address daily. For anything urgent, email is fastest,
reply inside 4 hours during business days.

WHEN TO ESCALATE

- To pause the automation: email me, paused within 4 hours, no work
  on your end.
- To change what is in the email (add a column, change the sections,
  change the time it lands): email me, most adjustments are 30
  minutes of work, included in the monthly.
- To change the recipient list (add the owner, remove Dana, route to
  someone else): email me with the new addresses.
- If you do not hear back within 24 hours, text 612-555-0142.

WHAT THE MONTHLY COVERS

- Monitoring (I get the alerts, not you)
- Fixes when something breaks
- Adjustments when your order categories change
- A 15 to 30 minute monthly check-in
- Priority response within 24 hours

WHAT IT DOES NOT COVER (without separate scope)

- The Phase 2 invoicing automation we discussed (separate build)
- Integration to your shipping carrier
- Major redesigns of the order summary email
```

---

## Send-day email (sent same day as the walkthrough)

```
Subject: Daily order summary handoff document

Hey Dana (and owner cc'd),

Attached: a one-page handoff doc for the order summary automation we
just walked through. Save this somewhere you can find it. Explains
how to use it, what to do if something looks wrong, and what is
covered in the monthly.

First scheduled run is Monday, June 8, 7am Eastern.

Talk first week of July for the monthly check-in.

Jordan
```

---

## DEMO SCRIPT (use on the walkthrough call)

15-minute screen-share, run on real data.

1. THE INPUT (2 min): "This is your orders spreadsheet. Automation
   reads it every morning at 6:55am, pulls the new rows."
2. LIVE TRIGGER (3 min): trigger it manually, narrate, let them
   watch.
3. THE OUTPUT (3 min): show the test email landed, walk the three
   sections, ask if format works.
4. FAILURE PATH (3 min): trigger a real error (point to a missing
   field), show the alert email landing in Jordan's inbox.
5. SCOPE CHECK AND CLOSE (3 min): confirm Monday 7am go-live, confirm
   handoff doc send, state the scope check out loud.

---

## Skool submit block

```
Delivery and Handoff Check-in
Build: daily order summary email, weekday mornings
Client: [acme-distribution]
When it runs: weekdays 7am Eastern
What 'broken' looks like: summary does not arrive by 7:30am, or order count looks off
Retainer covers: monitoring, fixes, small adjustments, monthly check-in
Setup / retainer: 1,800 / 400 per month
One line I stole from the owner's words: "I just want one email instead of scanning the whole tab"
```
