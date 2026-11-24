# Lessons

The playbook's memory. The agent adds entries at the end of every round. Enjo approves any promotion to the playbook.

**How it works**
1. At the end of each review round, the agent reads the revision notes and the hook scoreboard, then adds one entry per lesson below.
2. Each entry gets tagged **STANDING?** (it might apply to every project) or **ONE-OFF** (it belongs to this story).
3. When a STANDING? lesson shows up in **2 projects**, or Enjo states it as a rule, the agent proposes the exact wording for PLAYBOOK.md and waits.
4. After Enjo says yes, the agent edits PLAYBOOK.md, marks the entry `PROMOTED <date>`, and commits it with the reason.
5. Actual credits and hours go here too, so `tools/estimate.py` can be recalibrated.

| Date | Project | Lesson (what Enjo changed and why) | Tag | Seen in | Status |
|---|---|---|---|---|---|
| 2026-11-21 | All | Uploaded SFX only. Never use AI SFX; flag any that are missing | STANDING | Enjo rule | PROMOTED (rule 1) |
| 2026-10-07 | Adrian R2 | Open close on the face plus the number, then reveal wider; the wide shot must add information | STANDING? | Adrian R2 | Watching |
| 2026-10-07 | Adrian R2 | Lip sync only on the final line of the Price Tag hook | ONE-OFF | Adrian R2 | – |
| 2026-10-05 | Adrian R2 | Move scenes from generic places to the founder's real location | STANDING? | Adrian R2 | Watching |
| 2026-10-07 | Adrian R2 | Prefers one prompt per sequence over separate shot prompts | STANDING? (confirm) | Adrian R2 | Ask Enjo |
| 2026-10-01 | Adrian R1 | Give light changes a motivation (start dim, then brighten) | STANDING? | Adrian R1, R6 | Propose |
| 2026-11-24 | Kakis sample | Business-intro beats should set up a rule the turning point breaks ("speed is how we win" → "truck waiting"), not just sell | STANDING? | Kakis sample | Watching |
| 2026-11-24 | Kakis sample | The ad CTA reuses a line from the story ("we'll just carry it") so the offer doesn't break the emotion | STANDING? | Kakis sample | Watching |
| 2026-11-24 | Kakis sample | Pay off a side character's object in the ending montage (the uncle's box) | ONE-OFF | Kakis sample | – |

## Actuals (for the estimator)
| Project | Est. credits | Actual credits | Est. hours | Actual hours | Note |
|---|---|---|---|---|---|
