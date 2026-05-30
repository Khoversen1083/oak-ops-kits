# Monitoring setup checklist

The retainer's whole job is "I catch it first." Monitoring wires up
alerts so the system tells you it broke before the client notices. A
build that works on day one is the one that fails silently in month
three.

## Principle

The client pays you so they never see a failure. You are first to
know, always. If they notice before you do, monitoring failed, not
the build.

## Four layers, set them all up before launch

```
MONITORING SETUP, [Client placeholder] / [Automation name]

1. FAILURE ALERT (required for every automation)
[ ] Failure handler configured on the project
[ ] Failure email goes to MY inbox, not the client's
[ ] Subject line includes [Automation name] + "FAILED" so it filters
[ ] Body includes: timestamp, error type, last successful run,
    link to logs
[ ] Test: trigger a real error, confirm the email lands within 5 min
    Recipients to confirm:
    - Primary: [student email]
    - Backup: [phone or second email]
    - Client: NEVER on this list

2. HEARTBEAT (catches the silent no-run case)
[ ] Every successful run logs to a sheet or metrics store
[ ] You check the heartbeat once a week
[ ] No heartbeat for 24+ hours fires an alert
    Catches the case where the job did not error, it just did not
    run (schedule misconfigured, project disabled, runner offline).

3. OUTPUT SANITY CHECKS (per automation that produces output)
[ ] Row count is non-zero, alert if zero
    Threshold for this build: [from intake Q5]
[ ] Values inside expected range, alert if anomalous
    Range for this build: [from intake Q5]
[ ] Output timestamp is current, alert if stale
    Freshness window: [from intake Q4 plus a buffer]
[ ] All required fields populated
    Required fields: [list from intake Q3]

4. RATE LIMITS
[ ] Each external API in the stack has its rate limit documented
[ ] Backoff and retry on known transient failures
[ ] Separate alert for rate-limit errors, distinct from retries
    APIs in this build:
    - [API 1]: limit [X], current usage [Y per day]
    - [API 2]: limit [X], current usage [Y per day]

PROMOTION WALK, dev to staging to production
   Development
   [ ] Run locally, see output, confirm it works
   [ ] Feed intentional bad input, confirm error handling fires

   Staging
   [ ] Deploy with the client's REAL credentials, not mocks
   [ ] Run on schedule 3 to 5 days, watch every run

   Production
   [ ] Promote after staging is clean for 3+ runs
   [ ] Watch the first 7 production runs by hand
   [ ] Trigger one real error, confirm the failure email lands
```

## Alert recipient list (per environment)

```
Dev:        student email only
Staging:    student email only
Production: student email primary, student phone backup
            Client: NEVER on the alert list
```

## What gets monitored, what does not

Monitored: every scheduled job, every event-triggered job, every
output the client depends on, every API in the stack.

Not monitored: one-off manual runs, dev environment, exploratory
scripts. If you find yourself running one of those into production,
add monitoring before the next run.

## Anti-patterns

- Failure email goes to the client. You already lost the retainer.
- "It just works" so no monitoring. Means a silent 3-week outage
  later, the client tells you instead of the system telling you.
- Setting up monitoring after delivery. Too late, you missed the
  first failures.
- Faking the failure test. The test is not "I think the email would
  send", it is "I triggered an error and the email arrived." If you
  did not see the email arrive, the check is not done.
- One zero-row check is not enough. Stale data and missing fields
  fail silently too. All four layers, every build.

## When the alert fires

Inside business hours:
1. Acknowledge to yourself, open the logs
2. Email the client within 30 min: "Hey, automation hit an error
   this morning. Already on it, will follow up by [time]."
3. Fix
4. Email when fixed, plain-English cause, what you added to prevent
   the same scenario

Outside business hours:
1. If the build is non-critical (overnight job, not real-time), fix
   first thing in the morning, email then
2. If the build is real-time (order routing, customer-facing), fix
   now, email when fixed

The retainer pays for fast, calm, clear, in that order.
