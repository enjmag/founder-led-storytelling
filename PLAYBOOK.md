# Founder-led storytelling reels · Playbook

For an agent working with Enjo (creative director) on any founder, story or campaign. Built from the Adrian Tan handover (six IG reels, May 2026 brief).

**Who decides**

- **AGENT** means the agent proceeds alone and reports what it did.
- **ENJO** means the agent drafts options with a recommendation, then stops until Enjo picks.
- Enjo keeps the final call and the polish on every reel, "so it won't look like AI edit like everyone else."

---

## 1. Standing rules (apply to every project)

1. **Sound effects:** use only the SFX library Enjo uploaded. Never generate or use AI sound effects. If an effect is missing, flag it. Old prompts that ask for a whoosh or game sounds describe the intended sound, not a source.
2. **Music:** search for free-to-download tracks that fit the audience, tone, pacing and campaign goal. Keep the VO easy to hear. Record the title, download link, licence link, credit, and whether paid ads are allowed before using any track.
3. **The founder's recording sets the timing.** Cut to their pauses and phrasing. Generated clips carry no speech unless a clip is a lip-sync shot fed the real line as an audio reference. VO and music go in during the edit.
4. **Generated footage has no text in it.** Hook overlays and subtitles go on in the edit, so they can be timed to the moment the viewer hears the idea.
5. **Subtitles:** correct the words against the script and keep every timestamp and the cue order. If a line has no cue, flag it and listen to the VO. Never force a match.
6. **Each line needs a specific picture.** Show the thing only this founder's story has (a pail up to a 10-year-old's chin, a light switch across the room). Avoid generic stand-ins like a stressed face.
7. **Real material comes first.** Use the founder's photos, real footage and the B-roll bank where they exist. Use AI for missing moments, and treat it as illustration.
8. **References:** use separate references for identity (character sheet), location and composition, and reuse them across connected shots. Note the room layout, light source, props and starting positions. Frame natively in 9:16.
9. **Fix what an action means before adding effects.** Give actions a motivation. One example from the archive: the room starts dim so the mother has a reason to brighten it.
10. **Structure:** three hooks, then one bridge, then a shared body, then the organic close. The ad cut is the same reel with the founder's recorded CTA added. Keep the founder's own cadence and local expressions.
11. **Nothing gets generated before a gate.** Plan first, and mark the plan "nothing generated." List slop risks, estimated credits and open questions, then wait for Enjo.
12. **Premiere:** use the Premiere Pro MCP instead of computer use. Work on a copy or a new sequence and never touch Enjo's original. Rendered motion pieces stay in HyperFrames or ffmpeg.
13. **Naming:** name each export by reel, hook and ending. Add the tracking code when one is supplied.

**Treat these as project-specific, not standing:** lip sync only on the last line (that was the Price Tag hook); the 4 s and 7 s cut points; the iPhone look for showroom scenes against cinematic childhood scenes; Jack Neo-style heartland comedy (Reel 5); background characters shown only as hands (Reel 6); specific tracks such as "QKThr"; "20 seats only." Bring any of them back only if the new brief calls for it.

---

## 2. Three starting points

| You have | Agent does first | Timing label |
|---|---|---|
| **A · Rough story idea** | Interviews the founder or Enjo for the source material, fills the Story Brief, and drafts the script: 3 hooks, bridge, body in 3–4 beats, organic close, CTA. **ENJO** picks the arc, the hook set and the ending. Then the agent asks for the VO to be recorded. | Every timecode is **EST**, at about 2.2 words per second (Adrian's scripts ran ~125 words in 60 s and ~200 in 90 s). |
| **B · Finished script** | Checks the structure and flags anything missing (no bridge, CTA not written, hook with no visual direction). Fills the Story Brief from the script. | **EST** until the VO arrives. |
| **C · Recorded VO** | Transcribes with word timestamps, compares against the script, and flags possible mishearings without "fixing" them. Builds the timing map, one clip per VO file. | **ACTUAL** timings in seconds, from the word stamps. |

When the recording arrives on a project that started from A or B, replace every EST with ACTUAL and re-check the cut points before generating.

---

## 3. Stages

| # | Stage | Agent needs | Agent does | Delivers to Enjo | Who decides |
|---|---|---|---|---|---|
| 1 | **Story brief** | Script, idea or VO; founder photos; brand facts; campaign goal; answers to [founder intake](library/founder-intake.md) | Fills the Story Brief. Proposes the turning point and the visual anchor. Flags what has no real footage. | Story Brief, with 2–3 options for turning point, anchor and ending | **ENJO** picks the arc, turning point, anchor and ending (gate 1) |
| 2 | **Timing map** | VO files (hook 1–3, bridge, body 1–n, organic close, CTA) | Transcribes, stamps words, sets clip lengths (the VO length rounded up, max 30 s per generation), flags mishearings | Timing table plus audio flags | **AGENT** builds it. **ENJO** decides whether a doubtful VO line gets re-recorded |
| 3 | **Edit plan** | Brief, timing map, B-roll bank | Fills the Edit Plan line by line: what the viewer sees, the asset, the cut or sound cue. Marks the shots that need generation. Lists slop risks (check [slop-risks](library/slop-risks.md)) and estimated credits (run [the estimator](library/estimating.md)). | Edit Plan marked "nothing generated" | **ENJO** approves shots, hook concepts and spend (gate 2) |
| 4 | **References and prompts** | Approved plan, character and location sheets | Builds or fixes the reference sheets and writes the prompts. Order: duration and aspect → reference assignments → timed shots and cuts → camera, action, expression → audio and lip sync → continuity → exclusions | Prompts (start from the [prompt library](library/prompt-library.md)), reference sheets, and keyframes when a concept needs a look check | **AGENT** writes them. **ENJO** signs off on keyframes and the look |
| 5 | **Generate and review** | Credits and prompts | Generates the approved shots, then checks face, age, wardrobe, hands, room layout, light, and whether the action reads on a phone. Regenerates obvious failures within budget. | Picks, plus a short note for each shot that fails | **AGENT** handles technical regenerations. **ENJO** makes any change of story or action |
| 6 | **Assemble** | Selected clips, VO, B-roll | Cuts the shared body to the VO, attaches the 3 hooks and the bridge, builds the organic and ad (CTA) endings, places overlays where the idea is heard | Rough cut of each variant, on a copied sequence | **AGENT** builds the rough cut. **ENJO** handles pacing, polish and the final cut |
| 7 | **Subtitles and sound** | SRT, script, SFX library | Corrects the SRT (timings locked), places SFX from the library only, shortlists 2–3 free tracks with licence details, keeps the VO clear | Corrected SRT, SFX cue list (with any missing SFX flagged), music shortlist with licences | **AGENT** handles SRT and SFX placement. **ENJO** picks the track and the music drops |
| 8 | **Review, revise, deliver** | Enjo's notes, client feedback, tracking codes | Runs the Revision and Delivery checklist, applies notes, exports, names files, makes thumbnails | Exports, the filled checklist and the [delivery log](logs/delivery-log.csv) | **ENJO** approves before upload. The agent never marks anything approved itself |

**Escalate to Enjo whenever:** the story's meaning changes, a shot would cost more credits than planned, the founder's footage contradicts the script, a licence is unclear, or the VO seems to say something other than the script.

---

## 4. After each round: learn, then track results

- **Learn:** add each lesson from Enjo's notes to [LESSONS.md](LESSONS.md), tagged STANDING? or ONE-OFF. When the same lesson shows up in two projects, propose the exact rule wording for this playbook. Edit the rules only after Enjo says yes, then commit with the reason.
- **Actuals:** log real credits and hours in LESSONS.md, and recalibrate `tools/estimate.py` when they drift.
- **After posting:** fill in the [hook scoreboard](logs/hook-scoreboard.csv) about 3 and 7 days after posting. Note which hook type won and why. Use that to recommend hooks on the next brief, and say how much evidence is behind the recommendation.

## 5. Templates and library

- [Story brief](templates/story-brief.md)
- [Edit plan](templates/edit-plan.md)
- [Revision and delivery checklist](templates/revision-delivery-checklist.md)
- [Prompt library](library/prompt-library.md) · [Slop risks](library/slop-risks.md) · [Founder intake](library/founder-intake.md) · [Estimating](library/estimating.md)
- [Delivery log](logs/delivery-log.csv) · [Hook scoreboard](logs/hook-scoreboard.csv) · [LESSONS.md](LESSONS.md)

Worked example (fictional founder): [examples/tahi-repair-co.md](examples/tahi-repair-co.md)
Reel traced from the handover: [case-studies/adrian-reel-2-trace.md](case-studies/adrian-reel-2-trace.md)
