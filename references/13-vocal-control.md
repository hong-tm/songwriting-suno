# Vocal Control: Steering the Suno Voice with Lyrics and Meta-Tags

How to control who sings and how they sing it: the two control surfaces (Style field vs lyrics box), punctuation-as-performance symbols, delivery tags and their measured reliability, ad-libs, harmonies and vocal stacking, pronunciation surgery, non-English vocals, phrasing and breath, and keeping one vocalist across a song or an album.

**Read this first:** Suno's official documentation does not document bracket `[ ]` tags, parentheses `( )`, ALL CAPS, tildes, or any ad-lib syntax. The help center covers Custom mode, the lyrics box, the Vocal Gender selector, the Style field, Exclude, Personas/Voices, Covers, Extend, Add Vocals, the Song Editor and stems, but contains no article on lyric formatting or meta-tags. Everything bracket-related below is **community-derived and reverse-engineered**. Model caveat: the official v6 FAQ (edited 2026-09-09) states all pre-v6 models are retired and new generations use the v6 family (v6 / v6-wild / v6-mini), yet most field experiments below ran on v4.5-v5.5, so version-bound claims may be stale.

Confidence labels used here: **verified** (official doc, or 2+ independent field reports agreeing), **community** (multiple credible reports, undocumented), **conflict** (sources directly contradict; behavior is version- and context-dependent), **placebo** (tested as having no effect).

**v6 field correction (2026-10-21, verified on a real v6 clip).** On v6 (`chirp-goose`) parenthetical **director notes** were understood as instructions and **not sung**: `(Vocal 1: Soft Spoken)`, `(Vocal 2: Fast Flow / Aggressive)`, `(Vocal 1: Weak Voice)` and even a pinyin aid `(Ru Xian Zeng Sheng)` all behaved correctly — the model read them as staging/pronunciation guidance and sang the intended pinyin. So the older "parentheses are always sung" rule is a **pre-v6** generalization. On v6, the risk is not the bracket but the **content**: `(weak voice)` / `(soft spoken)` will be obeyed and produce exactly that. Use parentheses for direction if you like, but never put a descriptor there that you do not want performed.

## Quick rules

- **Style sets the voice globally; lyrics meta-tags steer it per section.** Put identity in Style, moment-to-moment delivery in the lyrics box, and never contradict one with the other.
- Square brackets on their own line are structural direction and are **never sung** (as long as they sit alone). Inline parentheses that echo the lead (a repeated word/phrase) are still sung as a backing voice. But on **v6**, parentheses holding a *director note* (`(Vocal 1: Soft Spoken)`, `(whispered)`, `(Ru Xian Zeng Sheng)`) are read as instructions, not lyrics — verified. The bracket does not decide; the **content** does.
- Trust tiers: `male vocals`, `female vocals`, `[Whispered]`, `[Spoken Word]`, `[Rap]`, `[Belting]`, `raspy`, `breathy` are load-bearing (>80%); `[Falsetto]` and mid-song voice switches are coin flips (50-80%); numeric mixing tags like `[Reverb: 30%]` are **placebo**. Delete them.
- Suno sings by spelling, not meaning: no dictionary, no IPA. Fix pronunciation with respelling and hyphens **before** generating; it cannot be fixed afterwards.
- Emotion words beat technical words (`desperate` steers better than `minor key with reverb`), but mood words like `quiet` or `soft` are ignored as technique. Use physical descriptors: `restrained, breathy, close-mic, low dynamic range, no belting`.
- There is no "same singer" guarantee. Each generation re-rolls the voice from your text; consistency comes from Personas/Voices plus a byte-identical vocal anchor line, re-pasted on every Extend.
- Non-English songs: lyrics in the target language and native script; Style, Exclude, section tags and vocal tags in English; name the language and accent explicitly; plan 4-6 takes.
- Officially verified controls: Custom-mode lyrics, the **Vocal Gender** toggle ("a nudge, not a switch"), the Style field ("gritty/soft"), **Exclude**, Personas/Voices/Custom Models.

## 1. The two control surfaces

| Control | Where it lives | What it reliably controls | Confidence |
|---|---|---|---|
| Structure tags `[Verse] [Chorus] [Bridge]` | Lyrics box, own line | Section boundaries, energy curve, instrumental breaks | verified |
| Delivery tags `[Whispered] [Belted] [Falsetto]` | Lyrics box, own line or in section header | Delivery for that section; coin flip for subtle ones | community / conflict |
| Vocal character descriptors (`raspy`, `breathy`, `smoky`, gender) | **Style** field, plain words, no brackets | Global singer casting and identity | verified-ish (official endorses gender plus "gritty/soft") |
| **Vocal Gender** selector | Advanced Options (UI) | Raises the probability of male or female; a nudge, not a switch | verified (official) |
| **Exclude** / negative tags | Advanced Options | Removes unwanted elements (choir, autotune, ad-libs) | verified (official) |
| Persona / Voice / Custom Model | UI | Locks voice identity across songs | verified (official) |
| Percentage and numeric tags `[Reverb: 30%]` | Lyrics box | **Nothing** | placebo |

Cross-source finding: several guides state independently that **lyrics-field direction is stronger per-section than the same words in Style**. One vendor claims roughly 10x stronger; that number is unaudited, so mark it community. Also note the field guide warning on "lyric bleed": ALL-CAPS or quoted phrases in the **Style** prompt can get sung, so keep Style dense and technical, and always put something in the lyrics box.

## 2. Symbols in the lyrics box: punctuation as performance

| Technique | Example | What it does | Confidence |
|---|---|---|---|
| Parentheses `( )` inline, echoing the lead | `Rise up (rise up) we're not done yet (oh yeah)` | Second/backing voice sung under or after the lead, often quieter, sometimes harmonized. | community (strong); still holds on v6 |
| Parentheses holding a director note | `(Vocal 1: Soft Spoken)`, `(whispered)`, `(Ru Xian Zeng Sheng)` | **v6: read as instruction, not sung** (verified 2026-10-21). Pre-v6: inconsistent, often sung. | v6 verified |
| Square brackets `[ ]` | `[Chorus]` on its own line | Structural/production direction; never sung when alone on its line | verified (strong) |
| Tilde `~` | `free-dom~` | Hold the final note with vibrato ("the closest thing to a vibrato button") | community (single source) |
| Dash `-` | `al-most`, `G-A-L-A-X-Y` | Stretch a syllable; dashes between letters spell the word out letter-by-letter | community |
| ALL CAPS | `We rise TOGETHER`, `HOLD ON` | Louder, more forceful delivery. Best on 1-3 words per line; a whole-caps line becomes a shout | community (strong) |
| Quotation marks `" "` | `she whispered "let go"` | Spoken or whispered quality for one phrase, more granular than `[Spoken Word]` | community (single source) |
| Ellipsis / dots | `Whispers................` | Slow trailing pause; more dots means longer sustain (outros, transitions) | community |
| Vowel elongation | `lo-o-o-ove`, `yeaaah`, `ne-e-ed` | Melisma or sustained note; repeated letters extend the vowel | community (strong) |
| Period / comma / line break / blank line | see section 6 | Breath and phrasing: period = full breath plus pitch reset; comma = short pause; line break = longer breath; blank line = vocal stops while music continues | community |
| Exclamation marks | `HOLD ON!` | Energy burst, but too many make the whole song yell | community |
| Repeated line | write the line twice | Sung in a loop; reinforces a melody. Do not rely on `(x2)` | community |

Rules that recur across sources (high consensus):

- Brackets on their **own line**; never put lyrics on the same line as a tag, or Suno may sing the tag.
- No blank line between a tag and its lyrics. A blank line **below** a bracketed cue signals an instrumental section.
- Repeat the chorus **verbatim** under every `[Chorus]`, or the melody changes.
- Keep lines short: 4-12 words, 6-12 syllables. Long lines get rushed.
- Suno reads both fields together; contradicting them lowers compliance.

## 3. Delivery tags: reliability tiers and verdicts

One guide ran 400+ generations to build a tier list; another publishes a technical tag reference; a third study rates 333 style tags. Synthesis:

| Tier | ~Compliance | Tags |
|---|---|---|
| **Tier 1 (load-bearing)** | >80% | `male vocals`, `female vocals`, `[Whispered]`, `[Spoken Word]`, `[Rap]`, `[Belting]`, `raspy`, `breathy`, negative prompting like `no autotune` |
| **Tier 2 (coin flip)** | 50-80% | `[Male Vocal]`/`[Female Vocal]` **in lyrics**, `[Build]`, `[Drop]`, `[Instrumental Break]`, character adjectives (smooth/gritty/silky), `[Intro]`, age descriptors, mid-song voice switches, **`[Falsetto]` (~60%)** |
| **Tier 3 (probabilistic)** | 30-50% | Long descriptive brackets (`[Ethereal synth build with rising tension]`), `androgynous`, bare register tags (`[Soprano]`, `[Alto]`) without Style backup, complex duets |
| **Tier 4 (placebo)** | ~0% | `[Reverb: 30%]`, `[Stereo Width: Wide]`, `[Bass: 80%]`, `[Compression: Medium]`, any numeric mixing parameter (explicitly tested) |

Verdicts on the specific tags that matter most:

| Tag | Verdict | Notes |
|---|---|---|
| `[Whispered]` | Reliable (>80%) but **reduces overall track energy** | Use strategically |
| `[Belted]` / `belt` | Reliable | Put it in the chorus section tag, **not** the global anchor, or the whole song shouts |
| `[Falsetto]` | Inconsistent (~60%) | Reinforce in both Style (`falsetto vocals`) and lyrics (`[Falsetto]`); expect to regenerate 4-6 times |
| `[Spoken Word]` / `[Spoken]` | Very reliable, Tier 1 | Whole sections work far better than single lines |
| `[Rap]` / `[Rapped]` / `[Melodic Rap]` / `[Fast Rap]` | Reliable | Cadence is not controlled by mix words; name the flow instead (section 4.2) |
| `[Harmony]` / `[Harmonies]` | Works; sometimes just doubles the vocal | "layered harmonies" rated Medium in the style-tag study |
| `[Choir]` / `[Gospel Choir]` | High; great right before the final chorus | Add to Exclude if unwanted |
| `[Ad-lib]` | Works; placement matters | `[adlib hey]` between lines vs `(oh yeah)` inline (section 4.1) |
| `[Duet]` | Hit or miss; often averages the voices | You must name who sings each section |
| `[Call and Response]` | Works when paired with `[Male]`/`[Female]` per line | Complex duets without per-line labels fall to Tier 3 |
| `[Female Vocal]` / `[Male Vocal]` | Reliable | More reliable in the Style field than in lyrics |
| `[Vocal Run]` / `[Melisma]` / `[Vibrato]` | Valid delivery tags; low-to-medium reliability | "Melisma" appears in the official glossary as a technique word |
| `[Screaming]` / `[Scream]` / `[Growl]` | Works in metal context; unreliable elsewhere | `[Scream]` is documented as Level-3 "aggressive, loud (Metal/Punk)" |
| `[Humming]` / `[Hum]` | Works, but also a frequent **unwanted** artifact | Add to Exclude to stop random "hmm/yeah" |
| `[Backing Vocals]` | Listed in catalogues | Use inline parentheses instead for reliability |
| `[Oh]` | **Not a documented tag** | Use `(oh)`, `(oh-oh)` or `[adlib whoa]`; absent from all five tag catalogues checked |
| `[Reverb: 30%]` and friends | Placebo | Delete |

Two more field-guide findings worth internalizing: **emotion beats technique** (`desperate` out-steers `minor key with reverb`), and **`[Chorus]` often overrides its own modifiers**, so do not expect a chorus-header qualifier to win against the chorus default.

## 4. Ad-libs, rap cadence, and vocal stacking

### 4.1 The three ad-lib formats

| Format | Example | Use for | Genres |
|---|---|---|---|
| **Bracket hit** `[adlib X]` | `[adlib boom]`, `[adlib hey]`, `[adlib whoa]`, `[adlib ayy]`, `[adlib uh]` | A separate percussive hit between lines | trap, drill, hip-hop, anthemic pop |
| **Inline parentheses** | `Rise up (rise up) ... (oh yeah)`, `(hey!)`, `(woo!)`, `(mmm)`, `(yeah-yeah)` | A second voice singing with or after the lead | pop, R&B, soul, gospel, rock |
| **Stretched CAPS** | `AAAAAH WE WILL NEVER BOW`, `RAAAAH` | A held scream or shout where the voice breaks; more vowel letters means longer and harder | metal, punk, hardcore |

Rules: don't mix all three formats in one section; don't pair `[adlib hey]` with `(hey!)` in the same section (echo or mistake effect); for metal, the vowel stretch (`AAAAH`) beats choosing the right word.

```text
[Verse 1]
I can hear the drums (the drums) coming up the street (oh yeah)
[Pre-Chorus]
Everybody move (move!) hands up (woo!)
[Chorus]
HOLD ON, we're going ALL NIGHT LONG
```

### 4.2 Rap cadence: name the flow, not the vibe

One vendor measured 1,142 real rapped cues and found **96% named no cadence term**, which is why different rap references all sound like the same person. The fix is to name flow mechanics per section (vendor research, unaudited):

```text
[Verse 1 | conversational density, dragging behind the beat, end-stopped lines]
[Verse 2 | packed triplets, pushing ahead of the beat, running over the bar line]
```

### 4.3 Stacking a pro-sounding chorus

The vocal-stack vocabulary: **double-tracked, octave stack, layered harmonies, gang vocals, call-and-response, ad-libs**; effect colors: **autotune, vocoder, talkbox, reverb-drenched, slapback delay, whisper layer**. Limits: stack at most about **3** layers, and the pro move is a **dry verse into a stacked chorus** so the contrast does the work.

## 5. Pronunciation and phonetics

Core mechanism (community, consistent): Suno sings by spelling, not meaning. It has no dictionary and no IPA, so fixes must be applied **before** generation.

| Technique | Example |
|---|---|
| Phonetic respelling | `through` to `thru`, `enough` to `enuff`, `tough` to `tuff`, `cough` to `koff`, `colonel` to `kernel`, `knight` to `nite` |
| Hyphenate syllables | `tonight` to `to-night`, `forever` to `for-ever`, `everything` to `ev-ree-thing` |
| Homograph disambiguation | `read` to `red` (past) or `reed`; `live` to `laiv`; `lead` to `led`; `bass` to `bayss`; `wind` to `wynd`; `tear` to `teer` or `tare` |
| Acronyms and numbers spelled out | `AI` to `A-I` or `ay-eye`, `DJ` to `dee-jay`, `24/7` to `twenty four seven`, `2024` to `twenty twenty-four`; never raw digits |
| Names: test first, respell, stay consistent | `Siobhan` to `Shi-vawn`, `Evie` to `Ee-vee`, `Leicester` to `Lester`, `Worcestershire` to `Wuster-shur` |
| Pronounce letters individually | `G-A-L-A-X-Y` |
| Clarity tags (delivery, not pronunciation fixes) | `[Staccato]` (best enunciation), `[Spoken Word]` (clearest), `[Operatic]`, `[Crisp]`; `[Airy]`/`[Breathy]` can blur words |
| Accent by respelling plus accent name | `Russian accent`, `Jamaican accent`, `Southern drawl` plus a phonetic rewrite of the lyrics |
| Upload-audio feedback loop (advanced) | Upload your vocal as a WAV, read what Suno "heard", adjust the lyrics to offset |

## 6. Phrasing, breath, and timing

| Goal | Technique |
|---|---|
| Breath and phrasing | Periods = full breath plus pitch reset; commas = short pause; line breaks = longer breath; a blank line = vocal drops out while music continues |
| Stop rushed vocals | Shorten lines (under 10-12 words), add line breaks, insert `[Short Pause]`, `[Musical Interlude]`, `[Beat Transition]` |
| Dramatic pause | `I... need... you` |
| Bar-length control | `[Instrumental, 4 bars]`, `[Buildup, 8 bars]`; blank lines roughly signal length |
| Energy | `!` gives a burst, but overuse turns the song into yelling |
| Groove alignment | Put the stressed syllable on the beat |
| Melody stability | Repeat chorus lyrics verbatim to keep the melody |

## 7. Language, bilingual, and accent control

**Language tier list (v5.5 field guide, June 2026):**

- **Strong:** English, Spanish, Portuguese, French, Italian, German, Japanese (Japanese improves when written with kana).
- **Decent:** Mandarin, Korean, Indonesian, Tagalog. Mandarin articulation clearly improved in v5.5 but **tones still drift**.
- **Inconsistent:** Cantonese, Vietnamese, Thai, Arabic, Hindi (tonal or complex orthography).
- **Weak:** most African, indigenous and regional-dialect languages.

A 48-line Chinese comparative test (Aug 2026) found Suno v5.5 produced **10 noticeable issues in 48 lines**: 4 tone inversions, 2 idiom splits, dialect mispronunciations, awkward mixed-language transitions, but the best arrangement and mix of the tools tested.

**Working rules (multi-source consensus):**

1. **Mirror split:** sung lines in the target language; the Style string, Exclude, section tags and vocal tags all in **English**.
2. **Name the language explicitly:** `native Russian male vocal, clear Russian diction`, or `[Vocal: mature female alto, husky, chest voice only, sung in Russian]`.
3. **Native script, not romanization:** Han characters (`我等你`, not `wo deng ni`), hangul for Korean, kanji plus kana for Japanese. All-katakana Japanese sounds mechanical. Suno infers the main language from the **script used most**, so a mixed-script lyric can flip the accent of the whole song.
4. **Stress and tone:** mark stress with combining accents on stubborn words (Russian `окно́`); for tonal languages add tone marks only on failing lines, since diacritics sometimes hurt.
5. **Sub-genre plus accent beats generic:** `Mandopop, native Beijing accent, clear tones, no English influence` far outperforms `Chinese music`.
6. **Generate 4-6 takes:** pronunciation is the most run-to-run random attribute.
7. **Chinese specifics:** check phonemes before every Extend (one wrong character can re-sample a whole line) and watch for homophone swaps.

**Bilingual songs work when the switch is structural, never mid-line.** A Mandarin or Spanish verse into an English chorus is fine; `I'll wait 等你` inside one line breaks phoneme handling and causes drift. Tag both sides (`[Verse 1 - Spanish]` ... `[Chorus - English]`, style `bilingual, Spanish verse, English chorus`) and add `all lyrics in [language], no English` to Style to stop mid-song reversion to English. Accent is a plain Style descriptor plus a phonetic rewrite (`Castilian accent` vs `neutral Latin American accent`, `French-accented English vocal`). Honest ceiling: you cannot always get a flawless native who would fool a Moscow listener.

```text
Style:  Mandopop, native Beijing accent, clear tones, no English influence,
        warm female alto, breathy
Exclude: autotune, English vocals
Lyrics: [Verse 1 - Mandarin]
        (native-script lyric lines here)
        [Chorus - Mandarin]
        ...
```

## 8. Style vs lyrics: interaction and conflict rules

- **Right field, right job:** overall voice and identity in Style; section-specific changes in lyrics. Wrong field means ignored or unpredictable.
- **Reinforce, don't contradict.** `breathy female` in Style plus `[Male Vocal][Aggressive]` in lyrics means the model picks one and you don't know which. Contradiction pairs that break output: `male vocals` + `female vocals`, `no vocals` + `whispered vocals`, `auto-tuned` + `raw acoustic`.
- **Mood is not technique.** `quiet`, `soft`, `calm` describe listener feeling, so Suno ignores them as delivery instructions. Write the physical technique instead: `restrained, breathy, close-mic, low dynamic range, no belting`.
- **To stop runaway belting or screaming:** delete escalation words (`powerful, epic, explosive, anthemic, soaring, build, climax, riffs and runs`) and write `still restrained | no belting | no melisma` into the chorus header.
- **No brackets in the Style field:** brackets there can cause the model to ignore genre or glitch. Style takes plain words.
- **v6 caution:** meta-tags "don't do nothing; they're being asked to do the wrong job." Treat them as structured guidance, not secret syntax, and change one cue at a time so you can attribute the result.

```text
Style (plain words): smoky female alto, breathy, close-mic, restrained,
                     no belting, no melisma
Exclude:             autotune, gang vocals, choir

Lyrics:
[Verse 1] (dry, conversational)
...
[Chorus | double-tracked, layered harmonies | still restrained]
...
```

## 9. Keeping one vocalist across a song or album

**Official mechanisms:** Personas (save a song's essence including vocals; apply in Custom mode, now inside the Voices menu), Voices (clone your own voice from 15 s to 4 min of audio, with a verification step; needs the Audio Influence slider high; 18+), Custom Models (Pro/Premier, up to 3 variants trained on at least 6 of your own tracks), Cover, Add Vocals, Replace Section/Extend for local fixes, and stems for isolating vocals.

**Community technique (persona alone is not enough):**

1. Write a **vocal anchor as line #1 in the lyrics box** plus the same descriptor in Style: `[breathy female vocal, smoky, close-mic, conversational delivery]`. Repeat the anchor in any section bracket where casting drifts: `[Chorus: same breathy female vocal]`.
2. Pin **five axes**: timbre, delivery, texture, age, pitch. Example: `[Vocal: warm male baritone, breathy, no vibrato, slight rasp on high notes]`, repeated **byte-for-byte** in every section and every track.
3. Build a **character dossier** in four layers: demographic plus timbre, technical delivery, emotional context, and a real-world "sonic anchor". Naming real artists is filtered and legally risky, so decompose into traits instead.
4. **Re-paste the full anchor on every Extend**: each new generation is a fresh casting, so re-paste the complete style tags plus BPM every time.
5. **Album cohesion levers:** lock the Persona plus a verbatim vocal description, a BPM band kept within 20-25, a related key family, one recurring instrument, and a lyrical thread.

**Voice-clone caveat:** guides conflict on whether to keep gender/vocal descriptors when using a cloned Voice. Songaifarm and HookGenius say **drop them** because the clone already carries them and stacking causes conflicts; SunoMarket says put them in **both** fields for text-to-voice casting. This is not a real contradiction: it's clone mode vs text-to-voice mode. And the honest limit stands either way: **Suno has no real "same singer" guarantee**; each generation re-rolls the voice from your text.

## 10. Known conflicts and uncertainty

1. **Parentheses semantics.** Pre-v6 reports split: SongSmith, Paddy, tagasong and Reddit say parentheses are sung as backing vocals; Maketunes says they are usually **not** sung and suit performance instructions. **Resolved for v6 (field test 2026-10-21):** parentheses holding a *director note* (`(Vocal 1: Soft Spoken)`, `(whispered)`, `(Ru Xian Zeng Sheng)`) are read as instructions and **not sung**; parentheses that *echo the lead* (`(rise up)`) are still sung as a second voice. The split is **content-based**, not bracket-based. On older models, test before trusting.
2. **`[Falsetto]` and delivery-tag reliability.** HookGenius rates Tier 1-2 (>50-80%); another guide says treat a single attempt as a coin flip and plan to regenerate. Both agree: reinforce in both fields.
3. **Gender descriptors with a cloned Voice.** See section 9: drop them for clones, keep them for text-to-voice. Different modes, easy to misapply.
4. **Style-prompt vocal descriptors "redundant" in v5.5** per one guide, while another treats them as primary. Likely a Voice-clone artifact.
5. **Version drift.** Blogger claims that v5.5 changed BPM/tag-order behavior have no official basis, and v6 (Sep 2026) retired pre-v6 models entirely, so version-specific findings may already be stale.
6. **`[Oh]`** is not a real tag in any catalogue checked; use `(oh)` or `[adlib whoa]`.
7. **Single-source techniques** (tilde vibrato, quoted whispers, multi-dot sustain, the 10x lyrics-field claim, the 96% rap-cue stat): plausible but unreplicated.

## How to apply this

- Cast the singer once in Style (gender, timbre, texture, age, range), then steer per section with lyrics tags; keep the two consistent and change one cue at a time.
- Use the tier table to decide what to prompt for and what to fix by regeneration: demand Tier 1 effects from the prompt, budget multiple takes for Tier 2 (falsetto, duets, mid-song switches), and delete every numeric mixing tag.
- Write ad-libs by genre: `[adlib X]` hits for trap and drill, inline parentheses for pop and R&B, stretched CAPS for metal, and never mix formats within one section.
- Pre-flight every lyric for pronunciation: respell homographs, acronyms and names, hyphenate hard syllables, and remember nothing pronunciation-related can be fixed after generation.
- For non-English songs, mirror-split the fields (native-script lyrics, English tags), name the language and accent, and plan 4-6 takes; check phonemes again before each Extend.
- Build a per-project vocal anchor block (five axes, byte-identical) and paste it into every generation and Extend; layer a Persona on top for cross-song identity.
- Before trusting any technique on a new model version, run a one-line A/B (with and without the tag) since v6 may have shifted bracket and parenthesis behavior.

## Sources

- https://help.suno.com/en/categories/550017-making-music
- https://help.suno.com/en/articles/2415873 (can I use my own lyrics)
- https://help.suno.com/en/articles/10153473 (gender of the singer)
- https://help.suno.com/en/articles/9010177 (music glossary)
- https://help.suno.com/en/articles/3484161 (Personas)
- https://help.suno.com/en/articles/11362433 (Voices FAQ)
- https://help.suno.com/en/articles/11362369 (Voices: use your voice)
- https://help.suno.com/en/articles/2872257 (Cover)
- https://help.suno.com/en/articles/3161921 (Exclude elements)
- https://help.suno.com/en/articles/13924481 (v6 FAQ)
- https://help.suno.com/en/articles/6882817 (Add Vocals)
- https://help.suno.com/en/articles/6141505 (Song Editor)
- https://help.suno.com/en/articles/12702337 (Advanced Stem Separation)
- https://help.suno.com/en/articles/2417409 (change voice or lyrics)
- https://help.suno.com/en/articles/13924801 (what's new in v6)
- https://hookgenius.app/learn/suno-vocal-prompts/
- https://hookgenius.app/learn/suno-style-tag-research/
- https://hookgenius.app/learn/suno-metatags-complete-list/
- https://hookgenius.app/learn/fix-suno-pronunciation/
- https://hookgenius.app/learn/suno-lyrics-formatting/
- https://songsmith.studio/blog/suno-lyric-formatting-symbols
- https://songsmith.studio/blog/suno-punctuation-is-rhythm
- https://songsmith.studio/blog/suno-ad-lib-placement
- https://songsmith.studio/blog/suno-vocal-control-cheat-sheet
- https://songsmith.studio/blog/suno-vocal-stack-cheat-sheet
- https://songsmith.studio/blog/suno-personas-guide
- https://songsmith.studio/blog/suno-album-cohesion-cheat-sheet
- https://paddystudio.com/blog/suno-song-structure-and-vocal-tags/
- https://sunomarket.com/blog/suno-vocal-control-guide
- https://sunomarket.com/guides/stop-screaming-vocals
- https://sunomarket.com/guides/lock-vocal-persona
- https://sunomarket.com/blog/suno-songs-other-languages
- https://blakecrosley.com/guides/suno
- https://tagasong.com/suno-lyrics-tags-square-brackets-prompts/
- https://maketunes.io/blog/to-keep-your-songs-from-sounding-messy-remember-to-add-these-tags
- https://musci.io/blog/suno-tags
- https://sunoarchitect.com/en/guide/suno-meta-tags/scream
- https://roo.beehiiv.com/p/complete-list-of-prompts-styles-for-suno-ai-music-2026
- https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/why-your-suno-v6-meta-tags-arent-working
- https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/duet-harmony-theme-meta-tags-suno
- https://suno.skin/en/blog/multilingual-lyrics-tips/
- https://aitoolsguidebook.com/en/articles/suno-vocal-language/
- https://songwritter.org/guides/test-chinese-ai-music-generators
- https://www.songaifarm.com/blog/suno-prompts-v5-5
- https://sunoaipromptguide.org/suno-vocal-prompts/
- https://versify.ca/suno-guide
- https://medium.com/@aitooldiscovery/suno-ai-lyric-prompts-complete-template-guide-with-section-tags-and-vocal-cues-2026-d5a87bcdd032
- https://aiunfiltered.beehiiv.com/p/best-suno-ai-prompts
- https://www.votemyai.com/blog/suno-ai-lyrics-tags-guide.html
- https://sunoai-music.ai/blog/suno-tags
- https://github.com/schwepps/skills/blob/main/suno-music-creator/references/metatags.md
- https://github.com/madziaar/SUNO-AI-Music-Skills-codex/blob/main/reference/suno/pronunciation-guide.md
- https://github.com/mttkllr/suno-field-guide
- https://github.com/stayen/suno-reference/blob/main/tag-reference.md
- https://www.reddit.com/r/SunoAI/comments/1mym1dm/ (meta-tag guide)
- https://www.reddit.com/r/SunoAI/comments/1sj0wvg/ (duet structure)
- https://www.reddit.com/r/SunoAI/comments/1egna68/ (background oohs and aahs)
- https://www.reddit.com/r/SunoAI/comments/1ktnwk7/ (spoken word)
- https://www.reddit.com/r/SunoAI/comments/1u2dkra/ (shaping a vocal)
- https://www.reddit.com/r/SunoAI/comments/1t62ipd/ (phonetic spelling)
- https://www.reddit.com/r/SunoAI/comments/1byoqva/ (language switching)
- https://www.reddit.com/r/SunoAI/comments/1v0o08v/ (stopping random hmm/yeah)
- https://www.reddit.com/r/SunoAI/comments/1fulb92/ (male/female verses)
- https://www.reddit.com/r/SunoAI/comments/1h2usr0/ (meta tags)
