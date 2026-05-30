# Resources

Source-of-truth files the coach reads while running the kit. Read-only,
not student-editable. If you need to change the template, fork the
repo.

| File | What it is |
|---|---|
| `voice-rules.md` | The hard and soft voice rules the coach enforces when drafting replies. Includes 5 worked bad-vs-good examples. |
| `decision-tree-replies.md` | The 5 reply types (interested, not now, send info, remove me, hostile) with one response template each, the canonical Oak Ops pattern. |
| `objection-bank.md` | 12 common objections that land after a cold email, one response template per objection. |
| `reply-triage-prompt.md` | The master prompt the coach uses to classify a pasted reply and pick the right template. The decision logic. |

The coach reads these in this order during a run:

1. `voice-rules.md` at Step 1
2. `decision-tree-replies.md` plus `objection-bank.md` at Step 2 (to
   build the triage card)
3. `reply-triage-prompt.md` at Step 3 (every time the user pastes a
   reply)
