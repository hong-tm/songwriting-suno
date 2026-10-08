# Suno Prompt Engineering: Style Prompts, Version Differences, Templates

> Research basis: official Suno docs (help.suno.com, release notes, blog) cross-checked against community field reports (r/SunoAI, HookGenius, SongSmith, ToneDraft, sunomarket, Suno.bi, mttkllr and zarlor GitHub guides). Fact flags: **OFFICIAL** = Suno states it. **VENDOR** = a guide reporting its own tests. **COMMUNITY** = multiple independent users. **ANECDOTAL** = one report.

## Quick rules

- Write the Style of Music field as an **ordered list**: identity first (genre / subgenre / era), then mood, instruments, vocals, production, tempo. The first 20 to 30 words carry the most weight; the first ~200 characters are the "critical zone". **[COMMUNITY, multi-source]**
- On v6, use the **production-brief shape**: Genre, then Vocals, Drums, Guitars, Bass, Other instruments, Arrangement, Production, Ending. **[COMMUNITY]**
- Negatives backfire in Style: `no drums` tends to produce drums, because the model keeps the noun and drops the "no". Put exclusions in the **Exclude** field. **[OFFICIAL for Exclude]**
- BPM numbers are soft conditioning. Pair a number with feel words (`driving mid-tempo`, `half-time feel`), or demote it to a hint (`~140 feel`). **[COMMUNITY, conflicted]**
- Cut conflicting descriptors (`warm` + `cold`, `dreamy` + `aggressive`). Keep 2 to 3 genres max and roughly 5 to 15 tags; fewer and sharper on v5.5/v6. **[COMMUNITY]**
- Structure tags belong in **Lyrics only**. Style takes plain descriptors. (One community guide disagrees; official docs are silent. See Conflicts.)
- Artist names are filtered. Decompose an artist into technique tags instead. **[OFFICIAL]**
- Since 2026-09-09, **v6 is the only model family that generates**; pre-v6 recipes still inform style but expect different behavior. **[OFFICIAL]**

## 1. What Suno officially documents

Official documentation is thin on prompt grammar. Suno documents:

- **Exclude** as the negative control, not inline "no X". (help 3161921)
- **Creative Sliders**: *Weirdness* (Safe to Chaos, 50% = normal) and *Style Influence* (Loose to Strong). (help 6141377)
- A **music glossary** of vocabulary terms. (help 9010177)
- That **v4.5 and later accept more detailed, even conversational style instructions**; the official example moved from `deep house, emotional, melodic` to a full sentence brief. (help 5782849)

Suno does **not** publish a weight or emphasis syntax, a field-ordering rule, a tag-count limit, a comma-vs-period rule, or character limits in help articles. One community reference (zarlor) reviewed help.suno.com and found no official article stating the character limits. Nearly everything below about *structure* is reverse-engineered community practice.

## 2. Descriptor order

### 2.1 Consensus order

Suno tokenizes left to right and the **first tokens carry the most weight** ("token priority: left wins"). Multiple independent guides converge on genre-first ordering:

| Rank | Slot | Example tokens | Sources |
|---|---|---|---|
| 1 | **Genre / subgenre / era** (identity) | `neo-soul, alt-r&b`, `dark synthwave, 80s` | ToneDraft, SongSmith, HookGenius, zarlor |
| 2 | **Mood / energy** | `sensual, laid-back`, `melancholic, nostalgic` | ToneDraft, SongSmith, HookGenius |
| 3 | **Instrumentation** (2 to 3 defining) | `warm rhodes, analog bass, gated-reverb drums` | SongSmith, HookGenius, mttkllr |
| 4 | **Vocal (type + delivery)** | `male falsetto, vocal runs`, `breathy female, close-mic` | ToneDraft, sunomarket, usesuno |
| 5 | **Production / texture** | `vintage tape, lo-fi, wide stereo` | ToneDraft, mttkllr, usesuno |
| 6 | **Tempo / era** | `78 BPM`, `driving mid-tempo`, `late-night` | ToneDraft, HookGenius |

**Rule from the field: priority follows position.** If the vocal matters most, move it to slot 1. If tempo matters most (DJ set), lead with it. (SongSmith, sunomarket)

### 2.2 v6's revised order

For the current v6 family, the working order shifts from a tag list to a **production direction**:

```
Genre → Vocals → Drums → Guitars → Bass → Other instruments → Arrangement/Energy → Production Quality → Ending instruction → Sliders
```

Source: Unofficial Suno v6 Prompting Guide (r/SunoAI 1wcyryw), corroborated by zarlor's model-prompt-strategies (graded COMMUNITY there: "the mechanism is unproven, and the order costs nothing").

The v6 converter rules (r/SunoAI 1wgb1yl) formalize: **`identity → pulse → voice → instruments → arc → mix → emotion → exclude`**, max 1,000 characters.

### 2.3 How word order and specificity change output

- **Front-loading dominates.** "The first 20-30 words carry the most weight" (r/SunoAI master doc); "the first ~200 chars are the critical zone" (zarlor).
- **Specificity beats adjectives.** `Distorted Electric Guitar` beats `Guitar`; `Fender American Tele, G major` beats `electric guitar` (mttkllr). v5.5 resolves fine detail like `1980s DX7 electric piano`, `lo-fi tape hiss` (Suno.bi).
- **Verbs beat adjectives on v6.** Describe instrument *activity*: `continuous foreground guitar riffs`, `rapid double bass, ghost notes`, not just instrument names (r/SunoAI v6 guide).
- **Conversational descriptions are allowed since v4.5 (OFFICIAL).** Suno's own v4.5 style article shows a full-sentence brief replacing a comma list.

## 3. Descriptor vocabulary that works

Synthesized from HookGenius's 60-tag cheat sheet, SongSmith templates, sunomarket's vocal guide, Suno.hk's vocal encyclopedia, the mttkllr field guide, and the r/SunoAI master doc.

| Category | Strong, working tokens |
|---|---|
| **Genre / subgenre** | neo-soul, alt-R&B, dark R&B, dream pop, shoegaze, indie folk, midwest emo, synthwave/outrun/darksynth, deep house, liquid DnB, boom-bap, trap, phonk, metalcore, deathcore, easycore, post-hardcore, barroom rock, reggaeton (dembow), cinematic orchestral |
| **Era / decade** | `70s funk`, `80s synthpop`, `90s alt rock`, `2000s indie`, `2010s trap`, `2010s bedroom pop`, `1980s retrofuturism`, `modern hyperpop` |
| **Instruments** | Rhodes/electric piano, Juno pads, Moog bass, 808 sub, trap hi-hats, gated-reverb drums, fingerpicked acoustic, pedal steel, fiddle, mellotron, cello legato, pizzicato strings, brushed drums, distorted guitars, FM/wavetable bass |
| **Vocal: register/gender** | female/male vocal, male tenor/baritone/bass, female soprano/mezzo/alto, duet, choir, gospel choir, children's choir, boy soprano, androgynous vocal, robotic/vocoder vocal |
| **Vocal: timbre** | breathy, raspy, smoky, warm, nasal, gritty, airy, honeyed, gravelly, velvety, brittle, weathered baritone |
| **Vocal: delivery** | falsetto, belted, whispered, spoken word, crooning, staccato rap, melismatic runs, deadpan, conversational, close-mic, call-and-response, gang vocals, stacked harmonies |
| **Production** | lo-fi, tape saturation, vinyl crackle, cassette warmth, analog warmth, gated reverb, reverb-heavy, dry signal, wide stereo, mono/narrow image, bit-crushed, sidechain pumping, polished, minimal mix, punchy, mastered, polyphonic |
| **Realism (acoustic)** | small-room acoustics, close-mic presence, proximity effect, one-take, natural timing drift, breath detail, pick noise, fret squeak, room bleed, worn tube amps |
| **Mood adjectives** | melancholic, euphoric, menacing, serene, wistful, triumphant, feral, haunting, tender, dreamy, urgent, bittersweet, longing, defiant, sultry, nocturnal |
| **Tempo words** | driving, laid-back, uptempo, half-time feel, four-on-the-floor, frantic, mellow, walking pace, rubato, swung/shuffled, syncopated, behind-the-beat |
| **Structure/meta (Lyrics box)** | [Intro] [Verse] [Pre-Chorus] [Chorus] [Post-Chorus] [Bridge] [Breakdown] [Build] [Drop] [Break] [Instrumental] [Solo] [Outro] [End] [Fade Out] [Key Change] [Half-Time]/[Double-Time] |

## 4. What confuses Suno

| Problem | Symptom | Fix | Source |
|---|---|---|---|
| **Conflicting descriptors** | `warm` + `cold`, `dreamy` + `aggressive`, `lo-fi` + `crisp hi-fi` cancel out into grey mush | Resolve contradictions; keep 2 to 3 genres max | sunomarket mistakes; r/SunoAI conflict thread 1tw1nhc |
| **Too many instruments/tags** | More than ~15-20 tags: the model averages and drops half | 5 to 15 tags (v5.5/v6: fewer, sharper); one job per instrument | ToneDraft; mttkllr |
| **Negative phrasing in Style** | `no drums` produces drums (the noun survives, "no" is dropped) | Put exclusions in the **Exclude** field (OFFICIAL) | official Exclude; freesongwritingtools |
| **BPM numbers** | `140 bpm` ignored or rounded | Pair genre + feel words; demote the number to a hint like `~140 feel` | sunomarket BPM; SongSmith BPM |
| **Unusual characters / non-English** | Descriptors in your native language underperform; trailing spaces inside brackets break parsing | Write descriptors in **English**; keep brackets tight | sunomarket mistakes; ToneDraft metatags |
| **Artist names** | Filtered/scrubbed for rights reasons | Decompose the artist into technical tags | ToneDraft; Suno responsibility blog ("we've never allowed prompts for specific artists") |
| **Structure tags in the Style box** | `[Verse]` / `[Chorus]` in Style get ignored or sung | Structure tags belong in **Lyrics** only | ToneDraft; mikefluff conventions |

**Weights / emphasis syntax:** Suno documents none. Community reverse-engineered, *unverified* heuristics: double quotes `"word"` and a `#` prefix as emphasis nudges; `|` pipe to stack qualifiers; `:` to separate a label from values; `~` vibrato hold; ALL CAPS intensity; `()` backing vocals (always sung); `{}` sound effects. Treat all of these as A/B tests, not rules. (sunomarket hidden syntax, SongSmith symbols, AceTagGen bracket guide)

## 5. The Lyrics box and the Style field

The two fields have distinct jobs. Community principle: **"Style defines what the track is; Lyrics defines what happens when."**

| Field | Holds | Rules |
|---|---|---|
| **Style** | Global DNA: genre, mood, instruments, production, vocal type | Plain descriptors; no structure tags; first tokens dominate |
| **Lyrics** | Sung words + `[bracketed]` section/vocal cues + `(ad-libs)` | One tag per line; tag goes *before* its section; brackets are instructions and never sung; parentheses are always sung |

Cross-checked in mikefluff's lyrics conventions, ToneDraft's metatags guide, and usesuno's prompting guide.

**Keeping a style consistent across generations:**

1. **Pin the vocal in two places.** Put a vocal anchor line at the **top of Lyrics** in brackets (`[raspy male lead, close-mic, weary]`) *and* the same descriptor in Style. Doing only one lets the voice drift by the chorus. (sunomarket vocal control)
2. **Duplicate the prompt exactly; change one variable at a time** (A/B protocol). (usesuno; r/SunoAI Style Prompt Guide 2.0)
3. **Save proven recipes verbatim**, for example "Recipe 12" becomes "Recipe 12 - v6". (r/SunoAI v6 guide)
4. **Lock BPM + key in Style** across all generations of a project so spliced sections align. (mttkllr)
5. **Use Personas / Voices / Custom Models** for cross-song identity: the only reliable vocal lock. (zarlor)
6. **For long songs, set Style Influence high and Variety = Exact** so the model does not rewrite your prompt. (zarlor)

## 6. Version comparison (v2 through v6)

| Version | Official release | Max first-gen length | Style control style | Key features added |
|---|---|---|---|---|
| **v2** | Fall 2023 | 1:20 | n/a | Discord era |
| **v3** | Spring 2024 (blog Mar 21, 2024) | 2:00 | Simple descriptors | First "radio-quality" model; better prompt adherence |
| **v3.5** | Summer 2024 (release May 30, 2024) | 4:00 (+ 2-minute extends) | Simple descriptors | Better song structure and vocal flow |
| **v4** | Nov 2024 (blog Nov 19, 2024) | 4:00 | Simple descriptors (200-char style cap) | Cleaner audio; Extend, Cover, Persona, Remaster, ReMi |
| **v4.5** | May 1, 2025 | 8:00 | **Conversational, detailed sentences** | Expanded genres/mashups, better prompt adherence, Enhance helper |
| **v4.5+** | July 2025 | 8:00 | Conversational | Add Vocals / Add Instrumental |
| **v5** | Sept 2025 (blog Sep 23; help Sep 25) | 8:00 | Crisp descriptors; emotional beats technical | Cleanest audio, authentic vocals, composition architecture, pro control suite |
| **v5.5** | **Mar 26, 2026** | 8:00 | Crisp film-brief; most expressive; Duration slider 10 to 360 s (added Jul 20, 2026, web) | **Voices, Custom Models, My Taste**; finer descriptor resolution |
| **v6 / v6-wild / v6-mini** | **Sep 9, 2026** | 8:00 | **Ordered production direction**, sentence-shaped, longer | Plain-language section edit, mashups, multimodal inputs (text/audio/image/video), **Max Mode**, **Variety** slider, **Duration 0:10 to 6:00**; **all prior models retired** |

Official sources: Model Timeline (help 5782721), Song length (help 2409473), the v3/v3.5/v4/v4.5/v5/v5.5/v6 blogs and release notes, v6 FAQ (help 13924481), Duration slider release note.

**Model-specific prompt diagnostics (COMMUNITY):** nwp's model-comparison rates v4.5 as the reliable workhorse (heavy genres, 8-minute songs), v5 as the cleanest with the best vocals but "insists on addition of intro vocals", v4.5+ as creative/unstable, v4 as chaotic. mttkllr rates v5.5 as most expressive but **more sensitive to vague prompts**, and reports mid-track degradation plus pop reversion (workaround: generate on v4.5/v5, then Cover on v5.5).

**Stems and timing:**

- **Auto Split** = 12 stem categories; **Split from Mix** = one instrument + the rest; **Advanced Split** = ~100 instruments, Premier only. Updated 2026-06-11. **[OFFICIAL]**
- **Duration slider** launched 2026-07-20 on web using v5.5 **[OFFICIAL]**; third-party spec = 10 to 360 seconds (Dolly); v6 Duration control = 0:10 to 6:00 (zarlor), with generation up to 8 minutes.
- **A prompt cannot set exact timestamps.** Metatags are "signal weights, not hard switches"; structure labels do not control timestamps (jackrighteous, ToneDraft). A timestamped-lyrics API exists for post-generation analysis.

## 7. Prompt formulas on record

| Formula | Structure | Source |
|---|---|---|
| **5-part** | `[Genre + Era] + [Mood] + [Key Instruments] + [Vocal Style] + [Production]` | SongSmith |
| **6-part** | `[genre] + [mood] + [instrumentation] + [vocal] + [production texture] + [tempo/era]` | HookGenius |
| **7-element** | `[GENRE] + [TEMPO] + [MOOD] + [INSTRUMENT] + [VOCAL] + [ERA] + [REFERENCE]` | mttkllr / r/SunoAI master doc |
| **v5.5 4-layer vector** | `[Primary+subgenre] → [instruments+timbre] → [mood/atmosphere] → [BPM, time sig, key]` | Suno.bi |
| **v6 production brief** | `Genre → Vocals → Drums → Guitars → Bass → Other → Arrangement → Production → Ending` | r/SunoAI v6 guide |
| **v6 converter** | `PRIMARY IDENTITY + GENRE2(role) + GENRE3(role), BPM, time sig, feel, VOICE, INSTRUMENTS+behavior, ARC, MIX, emotion, -Exclude` | r/SunoAI v4.5-to-v6 |

## 8. Pitfalls and fixes

1. **Numeric BPM instead of felt tempo.** Use `driving mid-tempo`, `half-time feel`; demote numbers to `~N feel` hints. (sunomarket)
2. **Negatives inside Style.** Move them to Exclude. (freesongwritingtools; OFFICIAL)
3. **A 30-tag Style string.** Cut to 8 to 12 load-bearing tags, genre first. (ToneDraft)
4. **No vocal anchor.** Add a 5-axis vocal anchor at the top of Lyrics plus a Style echo. (sunomarket)
5. **No section tags.** Add `[Verse]` / `[Chorus]` / `[Bridge]`; it ends the "one long blur". (ToneDraft)
6. **Non-English descriptors.** Write tags in English. (sunomarket)
7. **Vague adjectives** (`epic`, `professional`). Use concrete, playable tags instead. (sunomarket)
8. **Instructional collapse** (8+ commas inside one bracket). Pipe-stack instead, 3 to 5 elements per tag. (freesongwritingtools)
9. **Stage directions in Lyrics.** They will be sung. Use `[tag]` or `(ad-lib)` formatting. (wowhow)
10. **v6 "great chorus, dead verse."** State `full-band energy throughout, foreground riffs during verses`. (r/SunoAI v6 guide)
11. **Song ends mid-lyric.** Add an `[Instrumental Outro] [Hard Stop] [End]` buffer. (r/SunoAI v6 guide)
12. **Random intro hum.** Use a dense Exclude list plus `[START_ON]` or immediate lyrics. (mttkllr; `[START_ON]` is ANECDOTAL/community)

## 9. Known conflicts (flag before relying on any of these)

| Claim | Side A | Side B | Verdict |
|---|---|---|---|
| **BPM is respected** | ToneDraft: "platform respects BPM when stated"; SongSmith: "single most reliable tag" | sunomarket / mttkllr / SongSmith-BPM: numbers are weak, feel words win | **Conflict.** Suno lists BPM as vocabulary but never guarantees it. Treat BPM as soft conditioning |
| **Tag count** | 8 to 15 (ToneDraft, HookGenius) | 4 to 7 (SongSmith, wowhow); 3 to 5 simple / 8 to 15 detailed (mttkllr) | **Conflict by model era.** Consensus: fewer, sharper on v5.5/v6; more room on v4.5 |
| **Commas vs periods/pipes** | Comma-separated is standard in most templates | mttkllr: use periods + "and/with"; sunomarket: commas are "optional, ignored" | **Community-only, unverified.** No official grammar exists |
| **Brackets in the Style box** | mikefluff: brackets in lyrics, plain prose in Style | sunomarket comma-free guide: wrap Style layers in `[Genre: ...]` brackets | **Direct conflict, community.** Official docs do not address it |
| **Character limits** | API resellers: Style 1,000 / Lyrics 5,000 (v4.5+); ToneDraft: Style 1,000 | mikefluff: Lyrics 3,000 on v5.5; zarlor: numbers are "community-attested, not officially documented" | **Conflict.** Treat as working limits, not documented facts |
| **Exclude reliability** | OFFICIAL + freesongwritingtools: use it | heho: "most disputed control"; users report it ignores them | **Conflict.** Official says use it; efficacy unmeasured |
| **v5 adds intro vocals** | COMMUNITY (nwp, mttkllr) | Not in official release notes | **Community-only** |
| **MAX Mode syntax `[IS_MAX_MODE: MAX]`** | Community hack (mttkllr, Reddit) | OFFICIAL v6 Max Mode is a **toggle** costing extra credits (one source reports roughly 2x) | **Distinct things.** Do not conflate |

## Copy-paste prompt templates

### Formula skeletons

```
# 5-part (SongSmith)
[Genre + Era], [Mood], [Key Instruments], [Vocal Style], [Production]

# 6-part (HookGenius)
[genre], [mood], [instrumentation], [vocal], [production texture], [tempo/era]

# 7-element (mttkllr / master doc)
[GENRE] + [TEMPO] + [MOOD] + [INSTRUMENT] + [VOCAL] + [ERA] + [REFERENCE]

# v5.5 4-layer vector (Suno.bi)
[Primary+subgenre] -> [instruments+timbre] -> [mood/atmosphere] -> [BPM, time sig, key]

# v6 converter (r/SunoAI 1wgb1yl, max 1000 chars)
PRIMARY IDENTITY + GENRE2(role) + GENRE3(role), BPM, time sig, feel,
VOICE, INSTRUMENTS+behavior, ARC, MIX, emotion, -Exclude
```

### Genre recipes (comma-separated, front-loaded; tested on v5.5 per HookGenius / SongSmith)

```
indie pop, wistful, jangly electric guitars, tambourine, warm female vocals, analog reverb, summer drive, 115 bpm
```

```
dark r&b, sultry, rhodes keys, deep 808 sub, airy male falsetto, tape reverb, nocturnal, 88 bpm
```

```
synthwave, nostalgic, juno pads, gated reverb snare, arpeggiated sequences, male baritone vocals, neon highway, 108 bpm
```

```
lo-fi hip-hop, chill and nostalgic, Rhodes piano, tape-saturated drums, vinyl crackle, warm analog bass, no vocals, lo-fi tape hiss, 75 BPM
```

```
Cinematic orchestral, epic and triumphant, no vocals, full symphony orchestra, soaring strings, French horns, timpani, building from quiet to massive, film score quality, 85 BPM
```

```
Phonk, dark and aggressive, Memphis rap influence, pitched-down vocal samples, cowbell, heavy 808, distorted bass, tape-saturated drums, lo-fi crunch, 130 BPM
```

### ToneDraft alt-R&B (order: genre, mood, vocal, instruments, tempo)

```
alt-r&b, neo-soul, sensual, moody, male falsetto, vocal runs, rhodes, warm analog bass, vintage tape, intimate bedroom production, 78 BPM
```

### v5.5 "directing a band" prose brief (r/SunoAI 1s73tgz)

```
Barroom rock, loose and ragged, loud swagger, late-night energy.
Fuzzy overdriven guitars playing crooked blues riffs.
Brash, slightly off-kilter horn stabs.
Rhythm section heavy and slightly behind the beat.
Verse: talk-sung, restrained, conversational.
Chorus: louder, sloppier, controlled unraveling.
Weathered male baritone, narrow range, close-mic, slight overload.
Raw, early-era analog feel, minimal processing.
no glossy production / no modern vocal polish / no bright digital shimmer
```

### v6 production-direction brief (r/SunoAI 1wcyryw)

```
Genre: Modern pop-punk, melodic post-hardcore, easycore.
Vocals: gritty mature male baritone cleans, raspy melodic hooks.
Drums: aggressive punk drums, continuous double bass accents.
Guitars: bright interlocking lead guitars, fast driving power chords.
Bass: active melodic bass.
Arrangement/Energy: full-band energy throughout, foreground guitar riffs during verses, huge anthemic chorus.
Production Quality: high-fidelity studio production, close-mic vocals, crisp transients, layered instruments with clear separation, stable tonal balance.
Ending Instruction: complete every written lyric before a short instrumental outro and final hard stop.
```

## Sources

Official (suno.com / help.suno.com):

- Model Timeline: https://help.suno.com/en/articles/5782721
- Song length: https://help.suno.com/en/articles/2409473
- v4.5 detailed style instructions: https://help.suno.com/en/articles/5782849
- Introducing v5: https://help.suno.com/en/articles/8105153
- v5 release note: https://www.suno.com/release-notes/introducing-v5-the-world-s-best-music-model
- v5.5 blog: https://www.suno.com/blog/v5-5
- v6 blog: https://suno.com/blog/introducing-v6
- v6 FAQ: https://help.suno.com/en/articles/13924481
- Exclude: https://help.suno.com/en/articles/3161921
- Music glossary: https://help.suno.com/en/articles/9010177
- Creative Sliders: https://help.suno.com/en/articles/6141377
- v3 blog: https://suno.com/blog/v3 ; v3.5 release: https://www.suno.com/release-notes/v3-5-is-available-to-everyone ; v4 blog: https://suno.com/blog/v4 ; v4.5 blog: https://suno.com/blog/introducing-v4-5
- Release notes index: https://suno.com/release-notes ; Stems: https://suno.com/release-notes/advanced-stems ; Duration slider: https://suno.com/release-notes/duration-slider-on-web
- Suno responsibility blog: https://suno.com/blog/building-the-future-of-music-responsibly

Community / vendor:

- mttkllr field guide: https://github.com/mttkllr/suno-field-guide
- zarlor platform reference: https://github.com/zarlor/suno-band-manager/blob/main/src/skills/suno-agent-band-manager/references/SUNO-REFERENCE.md
- zarlor model-prompt strategies: https://github.com/zarlor/suno-band-manager/blob/main/src/skills/suno-style-prompt-builder/references/model-prompt-strategies.md
- nwp model comparison: https://github.com/nwp/suno-song-creator-plugin/blob/master/skills/suno-song-creator/references/model-comparison.md
- mikefluff lyrics conventions: https://github.com/mikefluff/skills/blob/main/skills/music-prompt/references/lyrics-conventions.md
- r/SunoAI: master prompting doc 1ryouzb; v5.5 prompt structure 1s73tgz; v6 prompting guide 1wcyryw; v4.5-to-v6 converter 1wgb1yl; analyzed 100+ prompts 1rv8q37; v3.5 tips 1dwqexa; character prompt method 1ouiswb; Style Prompt Guide 2.0 1n8lq6u (blocked, snippet only); conflict thread 1tw1nhc (all under https://www.reddit.com/r/SunoAI/comments/)
- sunomarket: guides/suno-prompts; guides/hidden-control-syntax; guides/comma-free-suno-prompts; guides/control-bpm-tempo; blog/suno-vocal-control-guide; blog/suno-prompt-mistakes (https://sunomarket.com)
- ToneDraft: suno-ai-prompt-guide-2026 and suno-metatags-guide (https://www.tonedraft.com/en/blog/)
- HookGenius cheat sheet: https://hookgenius.app/suno-cheat-sheet/
- SongSmith: suno-style-prompt-formula, suno-genre-style-prompt-templates, suno-lyric-formatting-symbols, suno-bpm-cheat-sheet (https://songsmith.studio/blog/)
- Lumiere v5.5 guide: https://lumiereprompt.com/en/blog/suno-v55-prompt-guide-2026
- Suno.bi v5.5 templates: https://suno.bi/en/blog/suno-v5-5-prompt-engineering-advanced-techniques-2026
- wowhow 3-field method: https://wowhow.cloud/blogs/suno-prompt-guide-style-of-music-tags-2026
- freesongwritingtools "why Suno ignores your prompt": https://freesongwritingtools.com/blog/why-suno-ignores-your-prompt/
- heho Exclude field: https://heho.ai/blog/suno-exclude-field
- usesuno prompting: https://usesuno.com/guide/prompting/
- AceTagGen bracket guide: https://acetaggen.com/blog/suno-ai-bracket-syntax-complete-guide
- Blake Crosley guide: https://blakecrosley.com/guides/suno
- Dolly v5.5 specs: https://withdolly.com/models/suno-v5.5
- jackrighteous duration guide: https://jackrighteous.com/de/blogs/guides-using-suno-ai-music-creation/suno-duration-slider-song-length-guide
