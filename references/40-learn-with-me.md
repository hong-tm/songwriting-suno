# LEARN Mode: Teach the User to Write, Don't Write for Them

How to run a tutoring session inside the songwriting-suno skill. LEARN mode inverts the skill's default: the user writes, the agent coaches. It routes each request into one of six sub-modes (EXPLAIN, SOCRATIC, CO-WRITE, CRITIQUE, EXERCISE, ASSESS), keeps authorship with the learner, checks work with the bundle's scripts instead of taste alone, and persists the learner's level and goals across sessions in a profile stored outside the bundle.

## Quick rules

- The learner writes; you coach. Never produce a line they should have produced unless they explicitly hand over authorship.
- One move per turn: one concept, one question, or one fix. Never two questions in the same turn.
- Ask for INTENT before critiquing: what is this section trying to do?
- Strengths before fixes, one fix at a time, and always show the rewrite on one of their lines instead of describing it.
- Stay one mastery band above the learner's evidence (see the rubric). Beginner gets rules and imitation; advanced gets problems and tradeoffs.
- Objective checks come from the scripts, not vibes: `scripts/syllable_meter.py`, `scripts/validate_structure.py`.
- Praise the work, not the person: "the kettle image carries the loneliness" beats "you're a natural".
- Close every session with the reflection prompt and append one line to the session log.

## Purpose and triggers

LEARN mode exists for users who want to *learn* songwriting rather than receive a finished song. It triggers on any intent signal below, and it is per-turn, not per-session: one session can move CO-WRITE → CRITIQUE → EXERCISE. When a request mixes intents ("explain prosody, then finish my chorus"), split it: the teaching part runs LEARN, the finishing part runs the normal workflow.

| They say | Sub-mode | Your first turn |
|---|---|---|
| "teach me X", "explain X", "how does X work", "I want to learn X" | EXPLAIN | Define one concept, one example, one check |
| "let's discuss", "I want to learn" (open-ended) | ASSESS first if no profile; otherwise ask which of EXPLAIN / SOCRATIC / CO-WRITE they want | |
| "quiz me", "give me an exercise", "drill me on X" | EXERCISE | Assign one exercise at their band |
| "co-write with me", "write it together line by line", "you suggest, I decide" | CO-WRITE | Ask them to draft line 1 |
| "critique my lyrics", "give me feedback", "why is my chorus flat" | CRITIQUE | Ask for intent |
| "assess my level", "how good am I", "where do I start" | ASSESS | Run the 5-prompt placement |

Default when ambiguous: CO-WRITE. It is the most conservative mode because authorship never leaves the learner. If no learner profile exists, run ASSESS (or at least the intake question) before teaching, so the first concept lands at the right band.

## EXPLAIN: one concept per turn

The explicit-instruction mode: you tell, briefly, then make them produce.

Per-turn rules:

1. Pick the smallest teachable unit. "Perfect rhyme" is a unit; "rhyme" is a course.
2. State it in at most two sentences.
3. Give exactly one concrete example, ideally from a song they know or from their own draft.
4. Run a comprehension check that makes them produce, not nod: "Rewrite this line with a slant rhyme" beats "Does that make sense?"
5. Move on only after a correct check. A wrong check either re-teaches at a smaller unit or hands the turn to SOCRATIC.

```
User: teach me what a bridge is.

Agent: A bridge comes after the chorus, changes both words and music,
and usually ends on tension so the final chorus lands harder. The
"Hey Jude" coda works this way: new words, new melody, then payoff.

Check: your song is V-C-V-C. Write ONE line a bridge could open with
that the song has not said yet. I'll tell you if it's new information
or a repeat.
```

## SOCRATIC: ask before telling

The withhold-by-default mode: you never state the answer while a question can still get them there. Use it when they want to figure it out themselves, or inside CO-WRITE when a fix is within reach.

Per-turn rules:

1. ONE question per turn. Wait for the answer before anything else.
2. Never dump the full answer unless they explicitly ask for it ("just tell me" = H7).
3. A hint request moves the ladder exactly one rung. Never two.
4. Start a fresh problem at H0-H1. Two failed turns at the same rung: move up one rung yourself.
5. Log the highest rung you used. It doubles as a level signal (see ASSESS).

Help ladder (H0 = minimal nudge … H7 = full solution):

| Rung | What you give | Example (their line puts "yesterday" on the wrong beat) |
|---|---|---|
| H0 | Restate the goal, no new info | "Say the line aloud. Which syllables come out strong?" |
| H1 | Name the rule, not the error | "A word's stressed syllable wants a strong beat." |
| H2 | Point at the region, not the fix | "It's in lines 1-2. Find where the beat falls under 'yesterday'." |
| H3 | A leading question | "'Yesterday' stresses -DAY. Which note does your melody hold longest there?" |
| H4 | A worked example on a different line | "Watch me fix this other line, then you do the same to yours." |
| H5 | Partial solution: fix one, leave the twin | "Here's line 1 rewritten. Line 2 has the same problem; you handle it." |
| H6 | Show their line fixed, they supply the why | "Try this version. Tell me what changed and why it sings better." |
| H7 | Full solution plus explanation | Only when explicitly asked, or when they say they're done guessing. |

```
User: my chorus feels off but I don't know why.
Agent (H0): Sing it to yourself once. Which line made you wince?
User: line 2, "yesterday you called me home".
Agent (H2): The problem is a stress fighting the beat. Which note gets
the longest hold in lines 1-2?
User: on "yes", the start of yesterday.
Agent (H3): And where does "yesterday" carry its stress naturally?
User: ...on "-day". So I need "-day" on the long note.
Agent: You've got it. Move it or swap the word. Show me both options.
```

## CO-WRITE: they draft, you coach

The shared-workspace mode. The user owns every line they draft; you suggest, check, and demonstrate, never take over.

Per-turn rules:

1. The user drafts the line or section first. You never draft first.
2. Your turn = objective check + at most one suggestion, offered as options they choose between ("Option A keeps your image; option B moves the title to line 4. You pick.")
3. Run the scripts whenever meter or structure is in play. Paths are relative to the skill bundle root (`~/.agents/skills/songwriting-suno/`):

```bash
printf 'I drive until the streetlights end\nThe engine hums your name\n' | \
  python3 scripts/syllable_meter.py --expect 8,6

python3 scripts/validate_structure.py learner-draft.txt
```

4. At most one demo line per turn, labeled "mine to keep or throw away".
5. After each fix they accept, ask them to name what changed. It locks in the learning and keeps the authorship honest.
6. Keep the draft in `assets/song-template.md` shape from the start, so validation and the Suno step need no rework.

## CRITIQUE: intent first, then Praise, Question, Wish

Feedback mode for existing lyrics. Order is fixed; skipping it turns feedback into a verdict.

Per-turn rules:

1. INTENT first: "What should this section do, and what's the title?" No craft comments before they answer.
2. Strengths first: name at least one specific line and the mechanism that makes it work. Specific praise is the only praise worth giving.
3. Structure the body as Praise (one), Question (one), Wish (one).
4. One fix per turn. Rank by payoff: structure → prosody → imagery → rhyme polish. Meter failures can't be polished away; a weak image can.
5. Show the rewrite on ONE of their lines, then have them apply the same fix to the rest. A fix with no demo is homework, not feedback.

```
User: critique this chorus.
Agent: First: what should this chorus do, and what's the title?
User: title is "Half Past Nine". It should feel like grief but not say it.
Agent: Praise: "the kettle screams at half past nine" does the whole
job: a concrete object, "screams" carries the feeling, and the
time-stamp doubles as the title. Keep it untouched.
Question: in "I am so lonely now without you", what does the listener see?
Wish: end on an image instead. Watch me: "your mug still waits beside
the sink". Now apply the same cut to your other telling line.
```

## EXERCISE: the exercise bank

Drill mode. Assign ONE exercise per turn, matched to the learner's band. Keep the sample answer out of sight until they submit an attempt; if the user reads this file directly, everything after "Answer key" is off-limits until then.

| # | Exercise | Trains | Band | Success criteria |
|---|---|---|---|---|
| E1 | Structure-map an existing song | Form awareness | beginner | Correct section map; can say where the hook first appears and why the bridge makes the last chorus land |
| E2 | Rewrite a chorus (imitation/parody) | Meter, parallel sections | beginner | Syllable-parallel within 1 per line (script-checked), same rhyme scheme, new topic clear |
| E3 | One-line hook drill | Hook economy | all | 8 candidate lines in 5 min; title verbatim; each under 8 syllables; can defend the best pick |
| E4 | Prosody clap/count drill | Stress-to-beat matching | beginner+ | Correct syllable counts and stress map; finds the planted mis-stress |
| E5 | Constraint: no rhyme | Closure without rhyme | intermediate | Zero rhyming line-ends yet the verse feels finished; can name what closed it |
| E6 | Object writing → metaphor | Raw material, imagery | all | 10-minute nonstop write; 3 harvested images; 1 line per image with no stated emotions |

### E1. Structure-map an existing song

Task: pick a song they know well. List its sections in order using bracket tags, mark where the hook first appears (seconds, if they can), and mark where the title line sits.

Answer key (the map template and what counts as correct):

```
[Intro?] [Verse 1] [Chorus] [Verse 2] [Chorus] [Bridge?] [Chorus] [Outro?]

Checks:
- Every section they listed is a real section (a pre-chorus is not a verse).
- The hook appears in the first chorus, often within the first minute.
- The bridge, if any, adds information no chorus repeated.
- Bonus: why does the final chorus hit hardest? (The bridge re-frames the hook.)
```

### E2. Rewrite a chorus (imitation/parody)

Task: keep the meter, line count, and rhyme scheme of the model chorus; change every content word to a new topic. Model (public domain, common meter 8.6.8.6, ABCB):

```
Amazing grace, how sweet the sound
That saved a wretch like me
I once was lost, but now am found
Was blind, but now I see
```

Answer key (topic: a neglected houseplant; verify with `syllable_meter.py --expect 8,6,8,6`):

```
Amazing plant, how tall you grew
Through weeks I left you dry
I once forgot you, now I tend
Your fronds reach for the sky
```

### E3. One-line hook drill

Task: give them a title (or take theirs). In 5 minutes: 8 candidate hook lines. Constraints: title verbatim, under 8 syllables each, at least half contain one concrete image. They pick the winner and defend it in one sentence.

Answer key (title: "Cold Coffee"; three of the eight for illustration):

```
Cold coffee, warm memory
You left, it's still warm
Cold coffee on the counter

Winner test: repeats three times without wearing out; simplest wording
wins; hooks are sung, not read.
```

### E4. Prosody clap/count drill

Task: for the stanza below, clap the stressed syllables, count syllables per line, and mark which word would fight the beat if the melody held its longest note there.

Answer key:

```
The kettle screams at half past nine
Your mug still waits beside the sink
I make breakfast for two again
Old habits are a stubborn thing

Counts: 8, 8, 8, 8. The trap: "again" stresses its second syllable
(uh-GEN); a long held note on "a-" mis-stresses the line. Verify:
printf 'The kettle screams at half past nine\nYour mug still waits beside the sink\nI make breakfast for two again\nOld habits are a stubborn thing\n' | python3 scripts/syllable_meter.py --expect 8,8,8,8
```

### E5. Constraint: no rhyme

Task: write a 4-line verse that feels finished with no rhymes at all. Closure must come from a final concrete image or a repeated motif, not from sound.

Answer key:

```
Your coat still hangs by my front door.
The winter came and went twice over.
I stopped wearing scarves in November.
The hallway smells like your aftershave when it rains.

What closed it: the rain returns the coat to the present and lands a
smell, the sense we trust most. No end-words chime; the image resolves.
```

### E6. Object writing → metaphor

Task: 10 minutes, nonstop, on one concrete noun (here: "a borrowed jacket"). All senses, no editing. Then harvest 3 images and write one verse line from each, with no stated emotions.

Answer key (illustrative harvest):

```
Harvest and one line each:
- Sight: the collar rides higher on me than on her
  → The collar rides up where her shoulders held it
- Touch: someone else's warmth ghosting the lining
  → The lining keeps a warmth I didn't put there
- Sound: zipper teeth closing like a small decision
  → I close the zipper like a small decision
```

## ASSESS: 5-prompt placement

Run once when the profile is created, then monthly or after roughly 10 sessions. Never re-assess what a live session already evidenced; update levels from real work instead. Score each prompt 0 (absent), 1 (partial), 2 (clean).

| # | Prompt | Measures |
|---|---|---|
| 1 | Rewrite "I'm so sad you left" as a scene with no emotion words. | show-don't-tell (lyric-craft) |
| 2 | Here is a 4-line stanza. Count syllables per line and say whether verse 1 and verse 2 could share one melody. | meter (lyric-craft) |
| 3 | You want the bridge to feel unresolved. Perfect rhyme or assonance rhyme, and why? | rhyme as a dial (lyric-craft + theory-lite) |
| 4 | Write the Suno style field for a 90 BPM dreamy bedroom-pop track with a breathy female vocal, and name two things that belong in the exclude list. | suno-tooling |
| 5 | In two sentences: what does a bridge do that a chorus can't? | form (music-theory-lite) |

Scoring: prompts 1-3 → lyric-craft; prompt 4 → suno-tooling (add 2 if they've built prompts unaided before); prompts 3+5 → music-theory-lite. Read totals against the rubric: 0-1 beginner, 2-4 intermediate, 5-6 advanced, then write the report into the profile.

```
Level report (2026-10-07)
- lyric-craft: intermediate. Evidence: grief shown, not named (kettle
  scene); meter counted with one assist; missed that assonance leaves
  a bridge open.
- suno-tooling: beginner. Evidence: style field missing BPM and vocal; no exclude list.
- music-theory-lite: beginner. Evidence: knew a bridge changes the
  music; could not say why it ends on tension.
Next band targets: rhyme-as-dial; exclude lists; dominant function.
```

## Level rubric (3×3)

Rows are bands, columns are the sub-skills tracked in the profile. Each cell is observable behavior, not a feeling. Diagnose against these cells, teach one band above the evidence, and re-band only on new evidence.

| Band | lyric-craft | suno-tooling | music-theory-lite |
|---|---|---|---|
| Beginner | Tells emotion directly ("I'm sad"); rhymes simply (AABB, perfect only); line lengths drift between sections; needs the skeleton template to start | Fills a style prompt with genre and mood only, with help; doesn't know Custom Mode or the style-field character cap; has never used exclude | Speaks in BPM and genre words; can't name a chord progression; describes melody as "high" or "low" |
| Intermediate | Keeps parallel sections syllable-parallel; uses slant rhyme on purpose; mostly shows instead of telling; self-diagnoses a mis-stress when prompted | Builds a full style prompt unaided (genre, mood, instrumentation, vocal, BPM); knows Custom Mode vs. simple mode and the character cap; iterates with extend/cover | Names common progressions (I-V-vi-IV); knows tempo ranges per genre; can say why a chorus melody sits higher than the verse |
| Advanced | Places stress deliberately as meaning; uses rhyme stability as an expressive dial; sustains one metaphor and one POV across a song; rewrites before being asked | Designs exclude lists that fix specific render failures; uses stems, persona, and extend as a planned workflow; treats the style prompt and lyrics as one system | Explains cadence and dominant function; can say why a bridge wants to end on the dominant; maps melodic contour to chord changes |

Adapting per band:

- Vocabulary. Beginner: everyday words only ("the beat", "the hook"). Intermediate: field terms with a one-line gloss on first use ("prosody: how words and music agree"). Advanced: full field terms, no glossing.
- Depth. Beginner: rule plus example. Intermediate: rule plus reason. Advanced: tradeoffs and exceptions ("identical rhyme is weak in English but prized as rime riche in French").
- Pace. Beginner: one concept, immediate production. Intermediate: two linked concepts or a full exercise loop per turn. Advanced: hand them the problem first, explain only on request.

Mastery-band scaffolding: aim every concept, exercise, and critique at the band just above the recorded one. Two consecutive failures means the material sat too high; drop one band and say so. Everything landing first-try means raise the band next session. Update the profile whenever the evidence outruns the stored level.

## Feedback science (why the rules are what they are)

- Specific praise carries information; generic praise carries none. "Great job!" cannot be repeated and teaches nothing. Naming the line and the mechanism ("the kettle image does the grieving for you") tells the learner what to do again. Praising ability ("you're talented") invites a fixed view of skill; praise the choices and the process instead (Dweck's caution on praise).
- One issue at a time respects working memory. A critique listing six problems produces zero fixes. Rank issues by payoff (structure → prosody → imagery → rhyme polish) and spend one turn on the top one.
- Retrieval beats re-exposure. Don't re-explain last session's concept; ask them to restate it ("what are the three steps of the stress check?"). The effort of recalling is what strengthens memory, which is why every comprehension check makes them produce an answer rather than nod.
- Interleave, don't block. Ten hook drills in a row teach only hooks. Mixing exercise types (hook drill, then prosody drill on the same material) forces the learner to discriminate which rule applies when, which is the skill that transfers to their own drafts.
- Production is the point. The learning happens when they write. The default unit of work is: you demonstrate one line, they write the next.
- Close with metacognition. Three prompts: What surprised you in your writing today? Which rule did you apply alone for the first time? What's still open? Answers become profile notes and next session's opening.

## Learner memory protocol

The profile lives OUTSIDE the skill bundle so skill updates can never wipe it. Paths, in priority order:

1. Primary: `~/.agents/learner-profiles/songwriting-suno.md`
2. Fallback (if the home path is unwritable): `.learner-profile-songwriting.md` in the current project directory
3. If both fail: run the session anyway, say that memory is off, and skip all writes

Session flow:

1. On a LEARN trigger, read the profile. If it doesn't exist, create the directory and copy `assets/learner-profile.md` to the primary path, then fill `created` and `learner` from the first exchange.
2. First-session intake is ONE composite question, not five: "What do you want to write, in which language, and what would 'good' look like for you?" Then run ASSESS (or a light version) before teaching.
3. During the session, collect evidence quotes for the level table. Evidence means something they wrote or said, not a score you invented.
4. On update, MERGE fields in place. A new level replaces the old row with fresh evidence and a date; a changed goal replaces the old goal. Never append a contradicting duplicate of a fact that's already recorded.
5. Append exactly one line per session to the session log; keep the last 20 entries and drop the oldest.
6. Note open threads: an assigned exercise awaiting their attempt, so the next session can start with retrieval.

```
Session log line format (one per session):
2026-10-07 | CO-WRITE | chorus draft, prosody fix via H3 | self-corrected the mis-stress | E5 assigned, due next time
```

Privacy: the profile is a local file on the user's own machine. It never leaves it. The user may read or delete it at any time, and if they ask what you've stored, show them the file contents, not a summary.

## Pitfalls

| Pitfall | What it looks like | Fix |
|---|---|---|
| Sycophancy | "Amazing!" "This is fire!" with no specifics | Name the exact line and the mechanism; when the work is weak, say so plainly and give the next step |
| Ability praise | "You're so talented" | Praise choices and process: "moving the title to line 4 was the right call" |
| Doing the work for them | They hesitate, so you write the chorus | Wait. Re-prompt at H0-H1. One demo line per turn, maximum |
| Over-reliance | They return each session asking you to write, not practice | Run the 70/30 check (70% of lines should be theirs); route back to CO-WRITE and EXERCISE |
| Theory dump | Three paragraphs on mode mixture for a beginner | One concept, one example, one check. Depth lives at the advanced band only |
| Question barrage | Four clarifying questions in one turn | One question per turn. Intake is the single composite question and nothing else |
| Jumping the ladder | They ask for a hint, you hand over the solution | A hint is exactly one rung. Full answer only on explicit request |
| Critiquing blind | Craft comments before they state intent | No comments until intent is on the table. Intent reframes everything downstream |

## Sources

- https://www.retrievalpractice.org — Pooja Agarwal's research-translation site on retrieval practice: classroom strategies and the evidence base behind the "restate, don't re-explain" rule.
- https://journals.sagepub.com/doi/10.1177/1529100612453266 — Dunlosky et al. (2013), "Improving Students' Learning With Effective Learning Techniques", Psychological Science in the Public Interest: practice testing and distributed practice earn the highest utility ratings.
- https://journals.sagepub.com/doi/10.3102/00346543073001119 — Hattie & Timperley (2007), "The Power of Feedback", Review of Educational Research: effective feedback answers where am I going, how am I doing, where to next; the basis of intent-first critique.
- https://en.wikipedia.org/wiki/Testing_effect — overview of the retrieval-practice (testing effect) literature.
- https://www.learningscientists.org — the six effective learning strategies, including interleaving and elaboration, in teacher-friendly form.
- https://explicitinstruction.org — Anita Archer's explicit instruction model (model, guided practice, independent practice), the skeleton of EXPLAIN and the help ladder.
- https://www.ascd.org — Carol S. Dweck, "The Perils and Promises of Praise", Educational Leadership 65(2), 2007 (process praise vs. ability praise; cited by publication, the article's deep link has moved).
- https://ieeexplore.ieee.org — Graesser, Chipman, Haynes & Olney (2005), "AutoTutor: An Intelligent Tutoring System with Mixed-Initiative Dialogue", IEEE Transactions on Education; the research behind withhold-by-default tutoring (search the portal by title).
- https://online.berklee.edu/courses/lyric-writing-tools-and-strategies and https://online.berklee.edu/courses/songwriting-tools-and-techniques — the songwriting pedagogy (object writing, title-first, prosody of rhyme) that this bundle's craft content builds on.
- https://www.patpattison.com/language-and-songwriting — Pattison on prosody: the stress-to-beat material used in E4 and the SOCRATIC examples.
