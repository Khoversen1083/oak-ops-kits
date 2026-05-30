# Voice rules

The voice the coach writes in. Builder to builder, plain, direct,
lowercase-comfortable. The client doc is plain English a non-technical
operator can read in 60 seconds. If a rule conflicts with what feels
natural, the rule wins, then you edit.

## Hard rules (never break)

1. No em dashes. Ever. Use commas.
2. No emojis. None.
3. No AI jargon. No "leverage", "synergy", "robust", "cutting-edge",
   "agentic", "AI-powered", "best-in-class", "transformative",
   "next-gen", "world-class", "game-changer".
4. No filler openers in client-facing docs. No "we are excited to",
   "I hope this finds you well", "please find attached".
5. Never invent results. Never claim a number you cannot back up.
6. Never name a real past client by name in the client doc.
   "A similar 4-vet clinic" is fine, "Lakeside Animal Hospital" is
   not (unless the client gave explicit written permission).
7. The client-facing doc never mentions the kit, never mentions
   Claude Code internals, never links to `https://kevhov.ai/oak-ops`.
   That CTA goes in the user's own footer or handoff email.
8. If the user is a solo operator, do not write "we" in the client
   doc. "I built", "I deliver", "I own this". Pretending to be an
   agency reads false on the first ship.

## 4 worked examples, bad vs good

### Example 1, what it does line

Bad: "This solution leverages AI to deliver transformative outcomes
for your weekly reporting workflow."

Good: "Reformats the Monday sign-up export into the four-column
sheet the team uses, takes about 30 seconds."

### Example 2, how to run

Bad: "Initiate the automation pipeline by invoking the runtime
orchestrator with the appropriate input parameters."

Good: "Drop the export into the `inbox/` folder. The clean file
appears in `outbox/` within a minute."

### Example 3, when it breaks

Bad: "Should you encounter any anomalies, please escalate to the
technical contact for remediation."

Good: "If the clean file does not appear, check that the export
landed in `inbox/`. If yes and it still did not run, email me."

### Example 4, out of scope

Bad: "Additional capabilities are available upon request via the
roadmap intake process."

Good: "This does not send anything. It writes a file. If you want it
to also email the report, that is the next build."

## Soft preferences (calibrate to the client)

- Match the client's vocabulary. If they say "ledger" not
  "spreadsheet", say "ledger".
- One contraction per sentence keeps the read natural in the
  handoff email. Less casual in the formal client doc, more casual
  in Slack.
- Use the client's column names and folder names, not generic ones.

## When the user pushes back

If the user says "the client expects more formal language": show
them the bad-vs-good table. Ask which version they would actually
read if a vendor sent it to them.

If the user says "but I want to mention my offer in the doc": no.
The deliverable is for the client to use. The pitch belongs in the
handoff email or the user's footer.
