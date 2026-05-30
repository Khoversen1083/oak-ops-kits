# Resources

Source-of-truth files the coach reads while running the kit. Read-only,
not student-editable. If you need to change a template, fork the repo.

| File | What it is |
|---|---|
| `delivery-checklist.md` | Pre-handoff verification. Build, credentials, docs, walkthrough, launch day, first 7 and 30 days, what-to-do-when-it-breaks. |
| `handoff-doc-template.md` | The one-page owner-facing handoff. WHAT IT DOES, HOW TO RUN IT, WHO TO CALL, WHEN TO ESCALATE. |
| `monitoring-setup-checklist.md` | Failure alerts to the student inbox, heartbeat for silent no-run, output sanity checks, rate limits. |
| `demo-script-template.md` | The 15-minute walkthrough call. Input, live trigger, output, failure path demo, scope close. |
| `voice-rules.md` | The hard and soft voice rules. Owner-facing for the handoff doc, builder for the checklists. |

The coach reads these in this order during a run:

1. `voice-rules.md` at Step 1
2. `delivery-checklist.md` at Step 2
3. `handoff-doc-template.md` at Step 3
4. `monitoring-setup-checklist.md` at Step 4
5. `demo-script-template.md` at Step 5
