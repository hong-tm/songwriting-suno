# 07 — Worked Examples (BUILD mode, end to end)

Two complete song deliverables, built the way BUILD mode builds them. The rest
of the bundle is principle-dense; use these as the few-shot model when the user
asks for "a song" and you need to see the finished artifact.

**Framing:** both songs are original works written for this skill. Style prompts
are generic, hand-built genre descriptions assembled by
`scripts/format_style_prompt.py` — not official Suno strings, and no Suno limit,
price, or feature here is stated as fact. The bundle's checker scripts are the
source of truth: every syllable count, character count, and PASS below is real
script output, re-verified before this file was written. Parenthesized cues
like `(instrumental …)` and the final `(the last train home)` echo are
instructions/ad-libs, not metered lyric lines.

---

## Example 1 — "Paper Lanterns" (English, acoustic wedding ballad)

**Raw brief:** "Song for my sister's wedding. From the family's point of view.
She's leaving the house; we're happy for her, it still hurts a little.
Acoustic, slow, singable by actual relatives."

**Interpreted brief:** speaker is the family ("we", "us"), not the bride. Last
night before a garden send-off; the yard is lit. Arc: nostalgia (v1) →
ceremony's cusp (pre-chorus) → celebration with an undertow (chorus) →
empty-room reframe (bridge) → bittersweet release. 72 BPM acoustic ballad from
the `acoustic-ballad` preset (`assets/persona-presets.json`), whose note says
keep chorus lines short so relatives can sing them. Rhyme: ballad scheme ABCB
(`04-lyric-craft.md`).

**Style prompt** (built with the preset as base; single-line command, real output):

    $ python3 scripts/format_style_prompt.py --genre "acoustic ballad" --mood "tender, celebratory" --tempo 72 --vocal "warm lead vocal, occasional falsetto" --instruments "fingerpicked guitar, warm strings" --exclude "electronic drums, autotune, heavy distortion"
    acoustic ballad, tender, celebratory, 72 BPM, warm lead vocal, occasional falsetto, fingerpicked guitar, warm strings
    EXCLUDE: electronic drums, autotune, heavy distortion

Style string = **117 chars** (`echo -n … | wc -c` = 117). Order is genre → mood
→ tempo → vocal → instruments, genre-first per `11-suno-prompting.md`; no
negative wording inside the Style line.

**BPM & Key:** 72 BPM; D major (open-position guitar).

**Structure plan** (template order, `assets/song-template.md`): Intro / V1 / PC
/ C / V2 / PC / C / Bridge / Final C / Outro; 8-bar intro + 16-bar verse puts
the chorus inside the first minute at 72 BPM. Energy: piano-and-voice verses,
strings at the pre-chorus, fingerpicking-only bridge, full strings under the
final chorus.

**Lyrics — full tagged sheet:**

```
[Intro]
(instrumental, fingerpicked guitar)
[Verse 1]
The garden gate still creaks at night
I hung a lantern by the door
Last night you wore your mother's pearls
and danced alone across the floor
[Pre-Chorus]
Dad's polishing the speech
Mom keeps humming through the hall
[Chorus]
Paper lanterns in the yard
we light one for each year
Little sister, walk the aisle
and all of us are here
[Verse 2]
You would rehearse across the hall
bare feet and counting one, two, three
but tonight the band will take you out
and after that you will dance with me
[Pre-Chorus]
Dad's polishing the speech
Mom keeps humming through the hall
[Chorus]
Paper lanterns in the yard
we light one for each year
Little sister, walk the aisle
and all of us are here
[Bridge]
The house will quiet when you're gone
the porch light stays on after dawn
[Final Chorus]
Paper lanterns in the yard
we light one for each year
Little sister, walk the aisle
and all of us are here
[Outro]
(instrumental, fading hum)
```

(Blank lines between sections are omitted in these compact sheets to save
space; a pasted Suno sheet can restore them — the validator skips blank lines,
with or without.)

**Meter check** (counts the script printed against `--expect`):

    $ python3 scripts/syllable_meter.py <the 16 counted lines above> \
        --expect 8,8,9,9,7,7,7,6,8,6,8,8,9,9,8,8
    Summary: 16/16 lines match expected meter.   (exit 0 — all PASS)

| Section | Counted lines: script syllables | Result |
|---|---|---|
| Verse 1 | The garden gate still creaks at night: 8 · I hung a lantern by the door: 8 · Last night you wore your mother's pearls: 9 · and danced alone across the floor: 9 | PASS ×4 |
| Pre-Chorus | Dad's polishing the speech: 7 · Mom keeps humming through the hall: 7 | PASS ×2 |
| Chorus | Paper lanterns in the yard: 7 · we light one for each year: 6 · Little sister, walk the aisle: 8 · and all of us are here: 6 | PASS ×4 |
| Verse 2 | You would rehearse across the hall: 8 · bare feet and counting one, two, three: 8 · but tonight the band will take you out: 9 · and after that you will dance with me: 9 | PASS ×4 |
| Bridge | The house will quiet when you're gone: 8 · the porch light stays on after dawn: 8 | PASS ×2 |

Counts are the heuristic's approximations (no pronunciation dictionary). Verse 1
= verse 2 at 8/8/9/9 (syllable-parallel), chorus at 7/6/8/6 inside the preset's
6-8 band on every repeat.

**Structure check:**

    $ python3 scripts/validate_structure.py <full tagged sheet>
    Sections found: 10 | Lyric lines: 28 | Est. length @3.5s/line: 98s (~1:38)
    Result: PASS    (exit 0; 2 [Verse] vs 2 [Chorus], no empty sections)

The ~1:38 estimate is the script's rough local default, not a Suno figure.

**Iteration log:**

| # | Change | Why | Result |
|---|--------|-----|--------|
| 1 | Chorus line 2: "we light one for **every** year" (8 by the script's count) → "we light one for **each** year" (6) | Hook singability at 72 BPM; preset asks for 6-8-syllable chorus lines | Kept |
| 2 | Chorus line 3 counted 8, not the eyeballed 7 (`aisle` scans as 2 units: "ai" + kept "-le") | Trust the script over the hand count | Target corrected to 8; line kept |

**Meaning & subtext:** surface: yard lanterns lit one per year; the family
watches the youngest walk the aisle. Beneath: a house losing a person while
refusing to grieve the wedding. The creaking gate and rehearsed waltz are
memory props; Dad's speech and Mom's humming are two ways of not saying
goodbye; the bridge's porch light says *the door is never locked for you*
without saying it. The lantern = one lit year is the private image the song
hangs on, and the chorus never says "proud" or "sad" — the yard scene carries
both.

---

## Example 2 — "末班车 / The Last Train Home" (Mandarin + English, city pop)

**Raw brief:** "City-pop song about leaving home for my move to another city.
I want it in Chinese but I always hum the hook in English. Groovy, 80s feel."

**Interpreted brief:** speaker is the one leaving, present tense on the
platform. Luggage packed, the 10:30 last train, Mom on the balcony, the city
glowing through one window seat. Arc: leaving (v1) → platform moment
(pre-chorus) → night-drive melancholy with lift (chorus) → what home actually
is (bridge reframe) → quiet closeout. `city-pop` preset, 104 BPM, funk bass +
electric piano; its note says the style suits bilingual CJK + English toplines.
Per `30-multilingual.md`: verses in 汉字 (not pinyin), one language per section
block, rhymes by 十三辙 rhyme families, chorus/hook in English.

**Style prompt** (single-line command, real output):

    $ python3 scripts/format_style_prompt.py --genre "city pop" --era "80s japanese pop groove" --mood "nostalgic, night-drive" --tempo 104 --vocal "female, smooth, lightly jazzy" --instruments "funk bass, electric piano, warm brass stabs" --exclude "trap beats, aggressive vocals"
    city pop, 80s japanese pop groove, nostalgic, night-drive, 104 BPM, female, smooth, lightly jazzy, funk bass, electric piano, warm brass stabs
    EXCLUDE: trap beats, aggressive vocals

Style string = **142 chars** (`echo -n … | wc -c` = 142).

**BPM & Key:** 104 BPM; major verses, minor-tonic bridge feel (mode stated, not
a sheet key).

**Structure plan:** same template order as Example 1 (Intro / V1 / PC / C / V2
/ PC / C / Bridge / Final C / Outro); chorus identical on every appearance.
The bridge reframes "home" in the narrative language, so the English hook's
final return reads as arrival, not escape. Vocal-anchor line bracketed at the
top of the lyrics field, echoed by the Style field's vocal descriptor
(`11-suno-prompting.md`).

**Lyrics — full tagged sheet:**

```
[Intro]
(instrumental, funk bass and electric piano)
[Verse 1]
行李箱塞满旧照片
站台风比夜里更凉
妈妈在阳台没说话
楼道灯陪我到街上
[Pre-Chorus]
出发之前，别回头看
look back no more, look back no more
[Chorus]
The last train home is leaving now
one window seat, the city glows
midnight neon lights below
home is a word I know
[Verse 2]
十点半的月台很挤
广播叫不到我的名
妈妈把脸贴着雨衣
月亮陪我二十公里
[Pre-Chorus]
出发之前，别回头看
look back no more, look back no more
[Chorus]
The last train home is leaving now
one window seat, the city glows
midnight neon lights below
home is a word I know
[Bridge]
家是那趟不晚点的车
it never leaves, it waits for me
[Final Chorus]
The last train home is leaving now
one window seat, the city glows
midnight neon lights below
home is a word I know
[Outro]
夜色里有一张车票
(the last train home)
```

**Meter check** — Chinese lines use the bundle's CJK mode: **one unit per
character**, punctuation not counted; counts are the script's own output:

    $ printf '<the 27 metered lyric lines from the sheet>' | python3 scripts/syllable_meter.py \
        --expect 8,8,8,8,8,8,8,8,6,6,8,8,8,8,8,8,8,8,6,6,9,9,8,8,6,6,8
    Summary: 27/27 lines match expected meter.   (exit 0 — all PASS)

| Section | Counted lines: script units (CJK = 1/char) | Result |
|---|---|---|
| Verse 1 | 行李箱塞满旧照片: 8 · 站台风比夜里更凉: 8 · 妈妈在阳台没说话: 8 · 楼道灯陪我到街上: 8 | PASS ×4 |
| Pre-Chorus | 出发之前，别回头看: 8 · look back no more, look back no more: 8 | PASS ×2 |
| Chorus | The last train home is leaving now: 8 · one window seat, the city glows: 8 · midnight neon lights below: 6 · home is a word I know: 6 | PASS ×4 |
| Verse 2 | 十点半的月台很挤: 8 · 广播叫不到我的名: 8 · 妈妈把脸贴着雨衣: 8 · 月亮陪我二十公里: 8 | PASS ×4 |
| Bridge | 家是那趟不晚点的车: 9 · it never leaves, it waits for me: 9 (heuristic; approximate) | PASS ×2 |
| Outro | 夜色里有一张车票: 8 | PASS ×1 |

Chorus repeats are identical lines, also PASS. Rhyme: verse lines 2/4 share
十三辙 families (江阳: 凉/上 in v1; 里有: 挤/衣/里 in v2), the English chorus
rhymes glows / below / know, and the code-switch pre-chorus is 8/8 so meter
stays parallel across the language boundary.

**Structure check:**

    $ python3 scripts/validate_structure.py <full tagged sheet>
    Sections found: 10 | Lyric lines: 29 | Est. length @3.5s/line: 102s (~1:41)
    Result: PASS    (exit 0)

**Vocal direction (with code-switch note):** warm alto, lightly jazzy,
behind-the-beat phrasing; vocal anchor bracketed at the top of the lyrics
field: `[smooth female lead, lightly jazzy]`.

- `[Verse – Mandarin]` — verses stay entirely Chinese (汉字, never pinyin).
- **Code-switch note:** the switch happens only in the Pre-Chorus, on one fixed
  unit — Chinese line 1 → English line 2 ("look back no more, look back no
  more"). One language per section block is the safe default; this single
  switch position is identical on both appearances so the melody stays
  consistent.
- `[Chorus – English]` — the hook is pure English. Expect a few re-rolls; keep
  the best take for Mandarin pronunciation in the verses.
- If a Mandarin word mispronounces, add a pronunciation metatag for that word
  only, e.g. `[Pronunciation: 雨衣 = yǔ yī]`, and regenerate the smallest
  affected section.

**Iteration log:**

| # | Change | Why | Result |
|---|--------|-----|--------|
| 1 | Bridge line 2: English draft ("the train that never runs late is home") → paired unit 家是那趟不晚点的车 / it never leaves, it waits for me | The reframe belongs in the narrative language, English as its echo; the final English chorus then lands as arrival | Kept |
| 2 | Chorus line 3 was expected at 7 units; the script printed 6 (`neon` scans as 1 vowel group) | Trust the script's count | Target corrected to 6; line kept |

**Meaning & subtext:** surface: the narrator boards the 10:30 train; on the
balcony Mom said nothing, and the silence is what she said. Subtext: "home"
stops being an address and becomes the train that never runs late — the
bridge's private image for parents who wait no matter the hour. Verse 1 gives
the departure in props (suitcase, old photos, the corridor light that walks the
narrator to the street); verse 2 denies it gently (the name never called over
the PA, Mom's face against the raincoat, the moon riding along for twenty
kilometers), and "home is a word I know" admits the word has just started to
mean something else. The night-drive suggestiveness lives in the sound, not the
lyric.

---

## What to copy from these examples

- **Tight style prompt.** One comma-separated string, genre first, built by
  `scripts/format_style_prompt.py`, well under 200 chars (117 / 142 here);
  negatives go on the EXCLUDE line, never inside Style.
- **Parallel sections.** Verse 1 and verse 2 share a syllable profile; the
  chorus is verbatim on every appearance so the melody repeats cleanly.
- **One concrete image per chorus.** Paper lanterns; the last train. No emotion
  labels in a chorus — the image carries the feeling.
- **Meter verified, not eyeballed.** Every printed count is real
  `syllable_meter.py` output; where hand count and script disagreed (`aisle`,
  `neon`), the target was corrected and the mismatch logged.
- **Plan structure before writing.** Tag order fixed first
  (`01-song-structure.md`); line counts are the length control.
- **One revision logged, honestly.** A deliverable without an iteration log is
  an unaudited draft.
- **Match language to craft.** Bilingual songs: native script, one language per
  section, a single fixed code-switch position, 十三辙 rhyme for Chinese lines
  (`30-multilingual.md`).

## Sources

Both songs ("Paper Lanterns" and 末班车 / "The Last Train Home") are **original
works written for this skill bundle** — no external recordings, lyrics, or pages
are quoted, and no external URLs are cited. No Suno facts are claimed; style
prompts are generic, hand-built descriptions produced by this bundle's own
script.

Craft references these songs illustrate:

- `references/01-song-structure.md` — template section order, energy curve,
  chorus inside the first minute
- `references/04-lyric-craft.md` — show-don't-tell, ABCB ballad rhyme,
  stress-to-beat matching, parallel-section meter
- `references/11-suno-prompting.md` — Style/EXCLUDE split, genre-first prompt
  ordering, vocal anchor in Lyrics + Style
- `references/30-multilingual.md` — CJK one-character-per-unit meter, 十三辙
  rhyme, 汉字 not pinyin, one language per section block, pronunciation
  metatags, code-switch handling
