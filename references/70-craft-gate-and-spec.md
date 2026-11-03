# 70 — Craft Gate, Spec Sheet, and the Companion Libraries

This file upgrades the quick workflow with the two strongest ideas from the
companion craft libraries (`lw-*` and `mc-*`, see §5): a **pre-writing gate**
that forces an actual choice, and a **spec sheet** you can check a draft
against. It also routes deep craft work to those libraries instead of
reinventing it here.

Source: the companion libraries by `jtydhr88` (MIT). The 12 most useful skills
are installed at `~/.agents/skills/` (auto-surfaced); the other 35 are parked at
`~/.agents/skills-library/` (not in the menu — read them by path when needed,
see §5). Their method is "trade time for quality": a full pass is 20+ minutes.
Use this file for the quick path; hand off to them when the user wants
professional depth.

## 1. The pre-writing gate (answer before writing a line)

Five questions. Each catches a specific failure. Do not start drafting until
they are answered — or written down as a deliberate "unknown".

1. **Which kind of lyric is this?** *attitudinal* (a stance, said to "you"), *
   situational* (one moment, anchored to an object, no plot), *narrative*
   (events advancing), or *expository* (arguing a point). **The default is NOT
   narrative** — if unspecified, most pop is situational.
2. **What is the one thing this song says?** One sentence. If it takes two,
   you have two songs.
3. **Who is it said to?** A person, an absent other, the self.
4. **At what moment?** The minute it is being said in.
5. **What is the anchor?** One photographable object that runs through the
   song and changes meaning each time it returns — or, for attitudinal lyrics,
   the one sentence that opens every chorus.

**The stranger test (the real gate).** Strip the title and proper nouns; hand
the lyric to someone who knows nothing; ask them to name the one specific
thing it is about. If they cannot, the gate failed.

Failure modes this prevents: a lyric that is pleasant but about nothing, a
verse that is scenery with no stance, a chorus that states a topic ("love")
instead of an angle ("the cost of a dream that came true").

## 2. The spec sheet (one artifact, four uses)

The companion libraries' core move: do not emit only lyrics — emit a **spec**
that the lyrics and the arrangement both answer to. Same document, four uses:
**handoff** (to the generator), **controlled A/B** (change one field, re-run),
**compile source**, **acceptance baseline**.

**LYR-SPEC (lyric side)** — fields: the one thing; addressee; moment; the
through-line anchor; per-line syllable count and stress position; rhyme scheme;
the deliberate asymmetries; language-layer check results (tone-melody, morae,
stress, batchim as applicable).

**ARR-SPEC (music side)** — fields: key; tempo; bar-accurate section map; chord
letters **and** roman numerals; who enters and leaves when; the energy curve;
vocal delivery; mix intent.

**The six must-agree fields** (when both exist): key, tempo, section map, bar
counts, per-line syllable counts, stress positions. Either side changes one →
the other must follow.

When to use it here: offer the spec sheet as an optional deliverable in BUILD
mode — it is the difference between a one-shot prompt and a re-runnable
artifact. Keep it lightweight for short requests; use it when the user iterates.

## 3. AI-tell audit (before shipping)

Two questions, never confused: **did the backend do what the brief said?** and
**does the result carry machine fingerprints?** A track can pass the first and
fail the second.

**Lyric tells to count** (from the companion `lw-ai-tell-audit`, eight
enumerable tells, each owned by a craft skill):

- a fully resolved emotional arc (too tidy to be human);
- generic imagery — nothing you could photograph;
- emotion labels stated instead of evoked;
- perfect symmetry / no deliberate asymmetry;
- the first-reach rhyme (the obvious one);
- telling instead of showing;
- drifting point of view or tense;
- cliché / dead metaphor.

Plus the **stranger test** (§1).

**Music tells** live in the companion `mc-ai-tell-audit` (fourteen tells).
Read that skill rather than reproduce it here — it also keeps apart "spec was
followed" vs "sounds like AI".

Machine-check what can be machine-checked: `scripts/lyric_lint.py` (cliché,
rhyme, repetition, line-spread), `scripts/syllable_meter.py` (meter),
`scripts/validate_structure.py` (shape). The rest is judged by ear.

## 4. Where this fits the workflow

- Run the **gate** (§1) right after clarifying the brief — it is cheap and
  catches the most expensive failure.
- Offer the **spec sheet** (§2) when the user will iterate.
- Run the **AI-tell audit** (§3) at step 12 (Iterate), before the final answer.

## 5. Companion libraries — route deep craft here

Two MIT skill libraries by `jtydhr88`, written in Chinese (source books are
Chinese originals/translations), agent-neutral. **Do not duplicate their content
here — route to them.**

- **Active** (12): installed at `~/.agents/skills/`, so they auto-trigger.
- **Parked** (35): at `~/.agents/skills-library/`, NOT in the menu (zero
  always-on token cost). To use one, read its `SKILL.md` by path, e.g.
  `~/.agents/skills-library/lw-cantonese/SKILL.md`; to activate permanently,
  move it back into `~/.agents/skills/`.

| Library | Prefix | Active | Parked | Basis |
|---|---|---|---|---|
| lyric-writing-skills | `lw-*` | 7 | 11 | 29 books (Pattison, Sheila Davis, 王力, 黄志华, Sondheim…) |
| music-composition-skills | `mc-*` | 5 | 24 | 50 books + 62 measured multitrack arrangements |

**Active — lyric (auto-trigger):** `lw-workflow` (entry/router),
`lw-song-intent` (the gate), `lw-structure`, `lw-imagery`, `lw-mandarin`
(Mandarin rhyme/count/caesura), `lw-tone-check` (tone-melody risk),
`lw-ai-tell-audit`.

**Active — music (auto-trigger):** `mc-workflow` (owns ARR-SPEC + style
fusion), `mc-arrangement-arch`, `mc-vocal-direction`, `mc-render-compile`
(compile to Suno), `mc-ai-tell-audit`.

**Parked — read by path only when the task needs them:**
- lyric: `lw-rhyme`, `lw-narrative`, `lw-cantonese`, `lw-english`, `lw-japanese`,
  `lw-korean`, `lw-chinese-style`, `lw-musical-theatre`, `lw-rap`,
  `lw-suno-interface`, `lw-case-studies`
- music: `mc-melody`, `mc-harmony`, `mc-progressions`, `mc-modulation`,
  `mc-rhythm-groove`, `mc-form`, `mc-counterpoint`, `mc-development`,
  `mc-orchestration`, `mc-texture-layering`, `mc-rhythm-section`,
  `mc-sound-design`, `mc-mix-intent`, `mc-style-jpop`, `mc-style-citypop-rnb`,
  `mc-style-jazz`, `mc-style-latin`, `mc-style-chinese-pop`, `mc-style-edm`,
  `mc-style-rock-band`, `mc-style-cinematic`, `mc-style-hiphop`,
  `mc-symbolic-score`, `mc-case-studies`

**Division of labour.** This skill = the quick, executable Suno pipeline +
tooling + self-update. The companion libraries = the deep, book-sourced craft
spec. When a request needs professional depth (a full LYR-SPEC/ARR-SPEC, a
style breakdown, a tone-melody audit, arrangement architecture), hand off to
`lw-*`/`mc-*` and use this bundle for the Suno compile/verify tail. If the companion libraries are absent on this host (`ls ~/.agents/skills/` shows no `lw-*`/`mc-*` and `~/.agents/skills-library/` is missing or empty), skip the handoff: run the gate, spec sheet, audit, and compile steps from §1–§4 of this file alone — the quick path stays complete without them.

## Sources

Companion libraries (MIT): https://github.com/jtydhr88/lyric-writing-skills and
https://github.com/jtydhr88/music-composition-skills — their READMEs and
`lw-workflow` / `mc-workflow` modules. All routing facts above are from those
READMEs; the gate and spec-sheet concepts are theirs, summarised for the quick
path.
