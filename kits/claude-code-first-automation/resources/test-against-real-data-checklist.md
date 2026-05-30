# Test against real data checklist

The synthetic input is for the build loop. The real client data is
for sign-off. Do not ship before this checklist clears.

## Before you get the sample

- The client knows you are running it on real data and gave
  permission, in writing if you can (email, Slack, anything text)
- You have an exact named example the client agrees represents the
  normal weekly run, not an edge case
- You have agreed which fields, if any, need to be redacted before
  you take the file off their machine
- Your automation is working clean on the synthetic input you used
  during the build loop

## When you get the sample

- Copy the file. Work on the copy. The original stays where the
  client put it.
- Put the copy in `outputs/automation-<today>/test-input/`
- Confirm the file shape matches what the automation expects (same
  columns, same headers, same encoding)
- If anything is off, do not patch it manually. The automation must
  handle real data, not the version you pre-cleaned

## Run the automation

- Run it once, end to end, on the real-data copy
- Capture the output in `outputs/automation-<today>/test-output/`
- Run it a second time, same input, confirm output is identical
  (deterministic) or explainably different (a timestamped log
  changed, fine)

## Score the run

Build a 5-row table in `outputs/test-log-<today>.md`:

| Check | Pass / Fail | Note |
|---|---|---|
| Output shape matches the as-is workflow doc | | |
| All input rows accounted for (kept count + dropped count = input count) | | |
| No PII leaked to a file outside the project folder | | |
| No writes to live accounts on this run | | |
| Output is correct enough to hand to the client right now | | |

If any row is Fail, fix it and re-run. Do not move to Step 5.

## Common things that go wrong on the first real-data run

- Encoding (the client's export is UTF-8 with BOM, your code reads
  UTF-8 without)
- Date format (the synthetic data was YYYY-MM-DD, the real data is
  M/D/YY)
- Hidden whitespace in spreadsheet cells (real exports come with
  trailing spaces, synthetic does not)
- One row is malformed (a column shifted because of an unescaped
  comma in a free-text field)
- The "normal week" sample turned out to be a quiet week, the
  automation has not seen volume yet

Add a row to the test log for each thing you found and what you
changed. The log is also the artifact you show the client at
handoff.

## Sensitivity handling

- The real-data copy stays in the project folder. Do not commit
  the test-input or test-output folders, they are in `.gitignore`
  by the `outputs/*` rule.
- API keys, OAuth tokens, anything secret, lives in `.env` files
  excluded by `.gitignore`.
- If the client's data includes PII (names, emails, addresses,
  health info), do not paste it into a chat window with anything
  other than Claude Code running locally. Do not upload it to
  external services.

## When to ship to the client

Only when:

1. The test run on real data passed all 5 checks
2. The test log is written and saved
3. The build decision log is written
4. The 1-page client doc is drafted
5. The handoff call is booked

Until then, this is a working demo, not a shipped automation.
