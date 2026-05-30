# Monthly audit checklist

The structured audit you run per client at month end. Fills the audit
doc that feeds the client summary email and the internal next-month
plan. Walk through it section by section, do not batch the questions.

## Section 1, Uptime and incidents

- Was the automation up the whole month? Yes or no.
- If no, how many incidents and how long was each one down? Rough
  numbers are fine.
- Was the client aware of any incident before you told them? Yes or
  no.
- Any pattern in when the incidents happened? (Time of day, after a
  deploy, after a data source changed.)

## Section 2, Automations run count

- How many runs did the automation do this month? Rough number is
  fine. Pull from logs, the dashboard, or a quick query.
- Is the run count up, down, or flat versus last month?
- Any spikes or drops that map to a real business event? (Client
  launched a campaign, hit a busy season, paused a process.)

## Section 3, Errors and failed runs

- How many runs failed this month?
- What were the top 2 or 3 failure causes? One line each.
- Were any failures caused by an upstream change the client made? Yes
  or no, what change.
- Anything that should be turned into a permanent fix versus a
  workaround patch?

## Section 4, Time saved estimate

- Rough estimate of hours saved this month versus the manual baseline
  the automation replaced. If the baseline was 6 hours a week, this
  month is roughly 24 hours saved.
- If the client has shared a fresh estimate, use theirs. If not, use
  the original baseline times 4.
- Note whether this is a rough estimate or a measured number. Do not
  pretend it is measured if it is not.

## Section 5, Value delivered

- What is the single biggest thing this automation did for the client
  this month? One sentence. (Examples: kept the reminder workflow
  running through the launch, caught a data quality issue before it
  hit billing, gave the team back a half day on Mondays.)
- Any direct quote from the client this month? Worth surfacing in the
  email if so.

## Section 6, What broke

- Did anything break this month, even briefly? Yes or no.
- For each break, what was the cause, what was the fix, and how long
  did it take to recover?
- Anything that almost broke and got caught by a monitor or by you?

## Section 7, What improved

- Any improvement shipped this month? (New step in the workflow, a
  cleaner output, a faster run, a new alert.)
- What does the improvement do for the client in plain words? One
  sentence the buyer would understand.

## Section 8, What is on the horizon

- Anything you know about coming up in the next 30 days that touches
  this client? (Their busy season, a tool migration, a team change,
  a renewal date, a planned upgrade on your side.)
- Anything the client asked for that has not been built yet?

## Output

When all 8 sections are filled, the coach writes the audit doc to
`outputs/audit-<client>-<YYYY-MM>.md` with these 8 section headers and
the user's answers under each. The audit doc is the source for both
the summary email and the internal next-month plan.
