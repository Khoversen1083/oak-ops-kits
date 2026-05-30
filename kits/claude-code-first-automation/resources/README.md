# Resources

Source-of-truth files the coach reads while running the kit.
Read-only, not student-editable. If you need to change the template,
fork the repo.

| File | What it is |
|---|---|
| `workflow-selection-criteria.md` | The rubric for picking a good first automation. 6 criteria, the red flags, examples of good first picks. |
| `automation-documentation-template.md` | The shape of the as-is workflow doc and the 1-page client doc. |
| `build-decision-tree.md` | How to pick skill vs slash command vs python script vs CLI wrapper vs MCP. The decision questions in order. |
| `test-against-real-data-checklist.md` | What to do with a real client sample before delivery. Copy-only, read-only first, log what happened. |
| `voice-rules.md` | The hard and soft voice rules the coach enforces while drafting the client doc and handoff messages. |

The coach reads these in this order during a run:

1. `voice-rules.md` and `workflow-selection-criteria.md` at Step 1
2. `automation-documentation-template.md` at Step 2
3. `build-decision-tree.md` at Step 3
4. `test-against-real-data-checklist.md` at Step 4
5. `automation-documentation-template.md` again at Step 5 for the
   client-facing 1-pager
