# Example: monitoring-setup-2026-05-30.md (worked example output)

Generated for the example intake. Fake client [acme-distribution],
daily order summary build.

---

```
MONITORING SETUP, [acme-distribution] / daily-order-summary

PRINCIPLE
Dana never sees a failure. I am first to know, always. If Dana notices
before I do, monitoring failed, not the build.

1. FAILURE ALERT
[x] Failure handler configured on the project
[x] Failure email goes to jordan@millsautomation.com, NOT Dana
[x] Subject line: "[daily-order-summary] FAILED [timestamp]"
[x] Body includes: timestamp, error type, last successful run, log link
[x] Test passed: triggered a real error 2026-06-05, email arrived in
    Jordan's inbox in under 2 minutes
    Recipients:
    - Primary: jordan@millsautomation.com
    - Backup: 612-555-0142 SMS via Twilio
    - Client: NEVER on this list

2. HEARTBEAT
[x] Every successful run logs to the runs sheet
[x] Jordan checks the heartbeat every Friday
[x] No heartbeat for 24+ hours fires an alert
    Catches: the case where the cron job did not error, it just did
    not run (schedule misconfigured, runner offline, project disabled)

3. OUTPUT SANITY CHECKS, tuned to this build
[x] Order count must be greater than zero on weekdays
    Threshold: a normal weekday is 8 to 60 orders. Alert if 0 on
    Mon to Fri. Skip the check Sat and Sun.
[x] Newest order date is within 24 hours
    Freshness window: orders older than yesterday 5pm = stale feed,
    alert
[x] Every row has customer, order number, amount populated
    Required fields: customer_name, order_id, total_amount,
    stock_status
[x] Summary email timestamp current
    Latest acceptable arrival: 7:30am Eastern

4. RATE LIMITS
[x] Google Sheets API documented, 100 reads per 100 seconds per user
[x] SendGrid API documented, 100 emails per day on this plan
[x] Backoff and retry on 429 responses
[x] Separate alert for rate-limit errors, distinct from retries
    APIs in this build:
    - Google Sheets: limit 100 reads / 100 sec, current usage ~3 per
      run = 15 per week
    - SendGrid: limit 100 / day, current usage 5 per week

PROMOTION WALK
   Development
   [x] Ran locally with sample data, output correct
   [x] Fed bad input (empty rows, malformed dates), error handling
       fired correctly

   Staging
   [x] Deployed with real read access to the orders sheet
   [x] Ran on schedule June 1 to 5, watched every run land
   [x] One failure caught (bad date format), fix verified

   Production
   [x] Promoted June 8
   [x] First 7 runs watched by hand
   [x] Triggered one real error June 9, alert email arrived
```

---

## Alert recipient list (frozen)

```
Dev:        jordan@millsautomation.com only
Staging:    jordan@millsautomation.com only
Production: jordan@millsautomation.com (primary)
            612-555-0142 SMS (backup)
            Dana: NEVER on the alert list
```

---

## What is monitored

- Daily 7am scheduled run
- The output email send step
- The Google Sheets read step
- The SendGrid send step

## What is not monitored

- The Phase 2 invoicing build (separate project, separate monitoring
  when it ships)
- One-off manual runs Jordan triggers for debugging
- The dev environment
