# Delivery checklist

The list you run before you tell a client "it's done." Catches the
easy mistakes that ruin a launch. Build, credentials, docs,
walkthrough, launch day, and the first 30 days are all delivery. Not
just the code working once on your machine.

## Rules

- Start it the moment the build runs end-to-end on real data. If the
  automation cannot finish one clean run, you are not at delivery yet.
- Run the automation 3 times on the client's real credentials and
  real data. Watch every run land.
- Do not check a box you did not actually verify. If you did not watch
  it happen, it is not checked.
- Confirm output matches the signed proposal exactly. If it drifts,
  fix or rescope, do not ship the drift.

## Template

```
DELIVERY CHECKLIST, [Client placeholder]
Build: [one-line description of the automation]
Go-live target: [day, time, timezone]
Setup / retainer: [setup] / [retainer] per month

PRE-LAUNCH, THE BUILD
[ ] Automation runs end-to-end on real (not test) data, no manual steps
[ ] Outputs match the signed proposal exactly
[ ] No hardcoded paths, secrets, or test values left in the code
[ ] Scheduled job runs on the schedule in the proposal ([day, time])
[ ] Retry logic exists for transient failures (rate limits, temp API errors)
[ ] Failure path emails YOU, not the client, on error
[ ] Logs land somewhere you can query later

PRE-LAUNCH, CREDENTIALS AND ACCESS
[ ] All credentials live in a secrets manager, not in the repo
[ ] OAuth tokens refresh automatically if the platform requires it
[ ] Client will revoke any temporary admin access used during build
[ ] Build README lists every credential and where it came from

PRE-LAUNCH, DOCUMENTATION
[ ] Build README is filled in completely
[ ] Handoff document is drafted (owner-facing, plain English)
[ ] Monitoring setup is documented
[ ] Client folder contains: discovery notes, signed agreement,
    proposal, build README, handoff document, any shared materials

PRE-LAUNCH, WALKTHROUGH PREP
[ ] You have run the automation 3+ times and watched the real output
[ ] You know what "good" output and "broken" output each look like
[ ] You can demo the failure path live (trigger an error so they see
    the alert flow work)
[ ] You have screenshots or a recording of the output for the doc

THE WALKTHROUGH CALL (15 min, screen-share)
1. Show the input. "Here is where the automation reads from."
2. Trigger it live. "Watch, I am running it now. It pulls the data,
   processes it, drops the output here."
3. Show the output. "This is what you will see [day, time], in your
   inbox."
4. Show the failure path. "If it breaks, this email goes to me, not
   you. You will not get woken up."
5. Confirm. "Does this look right? Anything you want changed before
   it goes live?"
   If "looks great," schedule go-live.
   If "can it also...," name it as a 10-minute add or a separate
   scope, up front.

LAUNCH DAY
[ ] First scheduled run executes successfully on the real schedule
[ ] You watch the first run land
[ ] You email the client: "Just landed. Did you receive it on your end?"
[ ] You log the launch in the build README deploy history

POST-LAUNCH, FIRST 7 DAYS
[ ] Watch every run for the first week, do not just trust monitoring
[ ] Note any quirks the client mentions in their first uses
[ ] Send a Day 7 check-in: "Quick first-week check, anything weird?"
[ ] Log any tweaks in the deploy history with dates

POST-LAUNCH, FIRST 30 DAYS
[ ] First monthly check-in scheduled
[ ] Case study capture started (quotes are useful even on a paid client)
[ ] First retainer invoice sent (300 to 600 per month, per proposal)
[ ] Update target list: Status "Live, retainer active"

WHEN SOMETHING BREAKS IN THE FIRST WEEK
1. Email the client within 30 min: "Hey, automation hit an error this
   morning. Already on it, will follow up by [time] with the fix."
2. Fix it.
3. Email when fixed: "Sorted. Cause was [one-line plain-English
   explanation]. Adding a check so this specific scenario does not
   happen again."
4. Update the build README "Known issues / watch list."
   The retainer is what they are paying for. Calm, fast, clear.
```

## Anti-patterns

- "It works on my machine." Doesn't matter. Test on the production
  runner with the client's real credentials.
- Silent rollout. Never go live without a walkthrough call. They
  should see it run before they trust it.
- Skipping the failure-path demo. Something will break eventually.
  They should have already seen the alert flow.
- Marking "done" before 7 days of real runs. The first week is part
  of delivery. Watch it.
