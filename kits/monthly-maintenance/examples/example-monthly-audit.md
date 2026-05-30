# Example: audit-lakeside-2026-05.md (worked example output)

Generated for the example intake (`example-intake-filled.md`). Client:
Lakeside Animal Hospital. Month covered: May 2026. Fictional, for
calibration only.

## Section 1, Uptime and incidents

- Up the whole month except for 2 short windows tied to the same root
  cause.
- 2 incidents, both under 1 hour, both during business hours.
- Client was not aware of either incident before I told them, I
  caught both via the Slack alert and fixed before the front desk
  noticed.
- Both incidents triggered by the same renamed field in the PIMS data
  export, pattern is clear.

## Section 2, Automations run count

- 1,240 runs in May.
- Up from 980 in April, roughly 25 percent.
- Spike maps to the dental month campaign Sarah launched on May 5.
  Run count tracked the campaign daily volume.

## Section 3, Errors and failed runs

- 4 failed runs total in May.
- 2 caused by the PIMS field rename (Section 1).
- 2 caused by a transient timeout on the messaging provider, retried
  on the next run and recovered.
- The PIMS field issue should be turned into a permanent guard, not
  a one-off patch. Workaround is in place but the fix is 2 hours of
  work.

## Section 4, Time saved estimate

- Rough estimate, 26 hours saved in May versus the manual baseline.
- Baseline was 6 hours a week, May had 4.3 weeks of operation, and
  the campaign added some volume on top.
- Sarah has not given a fresh measured number, so this is a rough
  estimate based on the original baseline. Note that in the email.

## Section 5, Value delivered

- The workflow kept running cleanly through the dental campaign launch
  even with a 25 percent volume jump, the front desk never had to
  step in.
- Sarah said in a Slack message on May 18: "honestly the dental month
  would have been chaos without this." Worth surfacing in the email.

## Section 6, What broke

- 2 short windows from the PIMS field rename. Cause: their PIMS
  vendor renamed `last_visit_date` to `previous_visit_date` without
  notice. Fix: updated the connector mapping. Recovery time: 35
  minutes for the first one, 15 minutes for the second.
- The almost-broke: a messaging provider quota warning at 80 percent
  on May 22, caught by a monitor, raised the quota before any send
  was dropped.

## Section 7, What improved

- Shipped a no-show flag on May 9. Workflow now skips the automated
  reminder for any patient with a no-show in the last 30 days and
  flags them for a personal call instead.
- In plain words: fewer robocalls to patients who are already
  drifting, the front desk gets a short list each morning of the
  people worth calling personally.

## Section 8, What is on the horizon

- June is still dental month according to Sarah, expect run count to
  stay high.
- Sarah asked twice in May about whether a post-visit survey could be
  added to the workflow. Once on May 11 in a Slack message, again on
  May 24 in person.
- No team changes, no tool migrations, no renewal date in the next
  60 days.
- Planned on my side: build the permanent PIMS field guard in the
  first week of June.

## Audit summary

- 1,240 runs, up 25 percent month over month
- 4 failed runs, all recovered, root cause identified and patched
- Roughly 26 hours saved, rough estimate
- One improvement shipped (no-show flag)
- Two upsell triggers fired: client asked for a second workflow
  (post-visit survey, Trigger 1) and the team referred another
  clinic in April (Trigger 5)
