# Example: intake-filled.md (worked example)

Fake build: a daily order summary email for a regional distributor.
Used in `example-handoff-doc.md` and `example-monitoring-setup.md`.

## The build

1. **What did you build?** Every weekday morning the new orders from
   the spreadsheet get summarized into one clean email to the ops
   lead, no manual lookup, no copy-paste, no tab-scanning.

2. **Who is it for?** [acme-distribution], a 40-person regional
   distributor in the Midwest. Family-owned, 22 years old.

3. **How will they use it?** The ops lead opens one email each
   morning instead of scanning the orders tab by hand. Three sections
   in the email: new orders, orders waiting on stock, orders ready to
   ship. About 90 seconds to read instead of 15 minutes to assemble.

## How it runs and how it fails

4. **When does it run?** Every weekday at 7am Eastern. Skips
   Saturdays and Sundays. If a federal holiday falls on a weekday,
   it still runs.

5. **What could break, how would the client notice?** The summary
   email does not arrive by 7:30am, or the order count looks wrong
   (showing zero orders on a normal weekday means the query broke,
   showing last week's numbers means the feed stalled).

## Handoff and operations

6. **Client contact.** Dana, the ops lead. She is the one who reads
   the email. The owner is copied on the handoff doc but does not
   want daily emails.

7. **What the retainer covers.** Monitoring, fixes when something
   breaks, small adjustments when their order categories change, a
   15 minute monthly check-in. Not covered: a separate automation
   for invoicing (already discussed as a Phase 2 build), any
   integration to their shipping carrier.

8. **Handoff timeline.** Setup invoice cleared Monday this week.
   Walkthrough call with Dana and the owner on Friday at 2pm
   Eastern. Goes live the following Monday at 7am Eastern.

## Money and access

9. **Setup / retainer.** 1,800 setup, 400 per month.

10. **Access still needed.** Read access to the orders spreadsheet
    (shared from the owner Tuesday), a sample of last week's orders
    (Dana attached to email Wednesday), confirm Dana as the alert
    fallback if her email bounces.
