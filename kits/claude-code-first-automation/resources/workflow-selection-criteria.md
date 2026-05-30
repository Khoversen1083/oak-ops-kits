# Workflow selection criteria

The rubric for picking the first automation. Score each candidate
workflow against these. Pick the highest score with the lowest blast
radius. Boring beats clever for the first ship.

## The 6 criteria

1. **Real and recurring.** The client already does this every week
   or more often. Not a hypothetical, not a someday-want. Something
   that happened in the last 7 days, by hand.
2. **At least 30 minutes per occurrence.** Anything shorter is not
   worth automating, and the client will not feel the payoff. If it
   is 30 minutes a week, that is 26 hours a year back, that lands.
3. **Inputs that already exist in a readable shape.** A folder of
   files, a CSV, an inbox, a spreadsheet, a CRM with an export.
   Skip workflows where you would have to build the data pipeline
   before the automation.
4. **Output you can describe in one sentence.** "A clean weekly
   report in this format" is shippable. "Better client
   communication" is not.
5. **Low blast radius if the first run is wrong.** No sending real
   client emails on run 1, no deleting originals, no touching
   billing data, no production database writes. Read-only first.
6. **Touches one tool or account, not four.** The first automation
   takes one input source and writes one output destination. If it
   needs four tools chained together, it is four automations, not
   one.

## Red flags that mean pick a different workflow

- The client has never actually done it manually, they just wish
  they had a tool for it
- It depends on data the client does not have ready (would require
  building a tracker first)
- It writes to a production system on the first run
- The output is subjective ("better answers", "more engaging
  content") and you cannot tell if it ran correctly
- It needs a tool connection the client has never set up and the
  user has never configured
- It is really three workflows wearing a trench coat. Pick one
  piece.

## Good first picks (patterns that ship)

- Reformat a weekly client export into the shape they actually use
- Summarize a folder of meeting notes into one action-items doc
- Draft a repetitive outbound email from a short input, saved to a
  file, not sent
- Pull all the links or names or invoices out of a folder of
  documents into a clean list
- Rename and sort a folder of incoming files by a consistent rule
- Generate a weekly status doc from a tracking spreadsheet

## What to do if all candidates fail the test

Send the user back to the client for an hour of workflow
observation. The first automation cannot be picked at a desk. It
gets picked while watching the client click through their week. If
they say "ugh, this part again", that is the candidate. Come back
with that and re-score.

## How the coach scores

Build a 6-row table per candidate, one row per criterion, yes or no
plus a one-line reason. The candidate with the most yeses AND the
lowest blast radius wins. If two are tied, pick the one with the
shortest input-to-output path.

If the winning candidate scores below 4 of 6, do not ship it. Send
the user back to the workflow-observation step.
