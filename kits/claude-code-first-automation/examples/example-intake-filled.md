# Example: intake-filled.md (worked example)

Fake client: a 2-attorney solo law practice handling estate planning.
Used in `example-automation-doc.md` and `example-build-decision.md`.

## Your client

1. **Who is the client?** Mara Lin, owner of Lin Law Group, a
   2-attorney estate-planning practice in suburban Denver. Pilot
   relationship, no money yet, agreed to a 4-week unpaid build in
   exchange for testimonial and case study if it works.

2. **What do they do?** Estate planning for higher-net-worth
   families. Wills, trusts, and the annual review motion that
   re-checks beneficiary designations and asset titling.

3. **What does the workflow touch?** A folder of client intake
   forms exported from their case management software, plus a
   Google Sheet the paralegal uses to track which clients are due
   for an annual review.

## The workflow

4. **Candidate workflows.**
   - A) Every Friday, the paralegal exports a CSV of clients whose
     annual review is due in the next 30 days, hand-cleans it,
     pastes it into the outreach tracker. About 90 minutes weekly.
   - B) Drafting the standard annual review reminder letter for
     each due client, currently copy-paste from a template doc
     with manual mail-merge. About 2 hours weekly.
   - C) Pulling the trust-funding status from each client's most
     recent intake form into a status doc for the partner. About
     45 minutes weekly.

5. **Who runs it today?** The paralegal, Jen. She owns A, B, and C.
   The partner, Mara, only reviews the output of C.

6. **What breaks?** When A is late, the outreach goes out late and
   they miss the 30-day window, the client renews with whoever
   else they spoke to first. Maybe two missed reviews per quarter,
   roughly 4K in annual review revenue per miss.

## Your starting point

7. **Terminal comfort.** A little. Has run Claude Code maybe 5
   times, mostly for drafting emails.

8. **Claude Code installed?** Yes, installed and running on the
   user's MacBook. Will build there, then move to the paralegal's
   machine for delivery.

9. **Tools the client uses.** Their case management software is a
   custom on-prem app with a CSV export only, no API. Gmail for
   email. Google Sheets for the tracker. Google Docs for the
   letter template.

## Your operating preferences

10. **Anything else?** Real client data has PII (names, addresses,
    asset values). The pilot agreement says no data leaves the
    practice network unencrypted. So the automation runs locally
    on Jen's machine, no cloud uploads, no external APIs that
    receive client data.
