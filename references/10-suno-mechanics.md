# Suno Platform Mechanics: Fields, Models, Tags, and Controls

> Research basis: official Suno help center, release notes, and blog, cross-checked against community guides (r/SunoAI, HookGenius, SongSmith, ToneDraft, AceTagGen, sunometatagcreator, docs.sunoapi.org). Each fact below is flagged **[OFFICIAL]** (Suno states it directly) or **[COMMUNITY]** (user-discovered, no Suno statement). Sources at the end.

## Quick rules

- Current era is **v6** (launched 2026-09-09, with v6 / v6-wild / v6-mini plus Custom Models). Every pre-v6 model was retired that same day. Existing songs stay playable, and Extend/Cover/Remaster of them now run on v6. **[OFFICIAL]**
- Suno documents the **fields, sliders, and Exclude**. It does **not** document the bracket meta-tag system: Suno's own help-center search for "metatags" returns "No results". The tag vocabulary is community-discovered.
- Only two bracket usages are officially acknowledged: `[female vocals]` in the Exclude Styles release note, and "Verse" / "Outro" structure labels in the July 2026 lyrics-improvements note.
- Put global style in **Style of Music** (plain descriptors, no brackets), section cues in **Lyrics** (brackets on their own line), and negatives in **Exclude**, never as "no X" in Style.
- `[Square brackets]` are instructions and are **never sung**. `(Parentheses)` are backing vocals and are **always sung**, even instructions like `(whispered)`.
- Character limits are unpublished. Measured values (v6): Style 1,000 / Exclude 1,000 / Lyrics 5,000 / Title ~100 (third-party API says 80). **[COMMUNITY, measured]**
- Tags are probabilistic hints, not commands. Keep 2 to 4 tags per section; the leftmost tag in a line has priority.
- **Exclude Styles requires Pro or Premier.** Excluded items show up in the preview with a leading `-` (for example `-piano`).

## 1. Models and modes

### 1.1 Current model family

- **v6, v6-wild, v6-mini**, plus user-trained **Custom Models**. Released **2026-09-09**. **[OFFICIAL]** (v6 FAQ)
- All pre-v6 models (v2 through v5.5) were **retired on 2026-09-09**. They can no longer generate. Old songs remain playable; any Extend, Cover, or Remaster of them now runs on v6. **[OFFICIAL]**

### 1.2 Mode naming: Simple / Advanced / Sounds

The current create-page tabs are **Simple, Advanced, and Sounds**. Older help articles still say **"Custom mode"**; "Advanced" is the current label for the same thing. **[OFFICIAL]** (help article 10625537)

| Mode | Fields you get | Notes |
|---|---|---|
| **Simple** | One description box ("write a description of what you want to hear"; historically called "Song Description") | Accepts a natural-language idea, genre, instrumentation, even song structure. Measured limit about 3,000 characters. Official instrumental example: *"an ethereal electro hypnotic instrumental with sweeping pads"* |
| **Advanced** (old Custom) | Lyrics box, **Style of Music**, Title, Instrumental toggle, **Advanced Options** menu (Exclude is the first item), Personas slot directly above the lyrics field, model picker top-right | The mode you use for full control |
| **Sounds** | A "describe the sound you want" box | Measured limit 500 characters **[COMMUNITY]** |

## 2. Field-by-field reference

| Field | Where | What it accepts | Status |
|---|---|---|---|
| Simple-mode description | Simple tab, one box | Natural-language idea, genre, instrumentation, even song structure | **[OFFICIAL]** mechanics; 3,000-char limit **[COMMUNITY, measured]** |
| Style of Music | Advanced mode | Genre, instrumentation, vocal type, mood, BPM, production, era descriptors, comma or space separated, **no brackets** | **[OFFICIAL]** field name confirmed in Exclude/Persona/Cover help articles |
| Lyrics | Advanced mode | Sung text plus bracketed meta-tags plus parenthetical backing vocals | Field is official; the tag system is unofficial |
| Title | Advanced mode | Song name only; per community it "doesn't significantly affect the musical output" | **[OFFICIAL]** field |
| Instrumental toggle | Advanced mode | Hides the lyrics field; generates no vocals | **[OFFICIAL]** (Custom Mode article 3726721) |
| Exclude (Exclude Styles) | **Advanced Options** menu, first item | Instruments, styles, vocal styles you do not want | **[OFFICIAL]** (help 3161921 + release note); Pro/Premier |
| Personas | Directly **above the lyrics field** | Saved vocals + style; selecting one auto-populates Style of Music | **[OFFICIAL]** (help 3484161) |
| Voices / Custom Models / My Taste | v5.5+ personalization | Clone a voice (verified); train a model on 6+ of your tracks; passive taste signal | **[OFFICIAL]** (v5.5 blog / release notes) |
| Weirdness / Style Influence / Audio Influence | Advanced Options sliders | Weirdness: Safe to Chaos, 50% is "normal". Style Influence: Loose to Strong. Audio Influence: only active with an upload | **[OFFICIAL]** (help 6141377) |
| Variety slider / Max Mode | v6 | Variety at 0 retains full control of your style tags; Max Mode is a higher-credit fidelity mode used for long songs, covers, and consistency | **[OFFICIAL]** (v6 FAQ) |
| Duration slider | v5.5 web (added 2026-07-20) | Pick song length | **[OFFICIAL]** release note |

## 3. The meta-tag system: what is official

**Suno does not publish a meta-tag reference.** Evidence:

- A direct query to Suno's own help-center search (`help.suno.com/en/search?q=metatags`) returns **"No results"**. `site:help.suno.com "meta tags"` returns zero results.
- The largest community references state it plainly: *"Suno does not publish an official list"* (sunometatagcreator.com/metatags-guide).
- The official Music Glossary documents structure terms (Verse, Chorus, Bridge, Pre-Chorus, Intro, Outro, Hook, Refrain, Break, Drop) as **musical vocabulary to use in prompts**, not as bracket syntax.

The two official acknowledgements that do exist:

1. **Exclude Styles release note (2024-09-19):** *"Try prompting specific vocals (eg: female vocals) by including `[female vocals]` in the Lyrics section and excluding 'male vocals' in Exclude Styles."* This is the one official bracket-in-lyrics example.
2. **Lyrics improvements release note (2026-07-09):** *"Song structure labels: Add labels like 'Verse' and 'Outro' to organize your lyrics [and] tell Suno how you want the song to flow."*

So: the *concept* of structure labels is officially acknowledged; the full bracket vocabulary and its syntax are community-discovered.

## 4. Tag catalogue

Flag key: **OFF** = Suno states it directly. **UNOFF** = community-discovered, no Suno statement.

| Tag | Type | Flag | Source |
|---|---|---|---|
| `[female vocals]` | Vocal | **OFF** | release-notes/exclude-styles |
| "Verse", "Outro" labels | Structure | **OFF** | release-notes/lyrics-improvements-on-web |
| Verse / Chorus / Bridge / Pre-Chorus / Intro / Outro / Hook / Refrain / Break / Drop | Structure (as vocabulary, not bracket syntax) | **OFF** (as glossary) | help 9010177 |
| `[Intro]` `[Verse]` `[Verse 1/2/3]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Bridge]` `[Outro]` | Structure | UNOFF | reddit 1mym1dm, HookGenius, SongSmith, sunometatagcreator |
| `[Hook]` `[Refrain]` | Structure | UNOFF | reddit 1hsoo5t, sunometatagcreator guide |
| `[Break]` `[Breakdown]` `[Interlude]` | Structure | UNOFF | SongSmith structure cheat sheet, jackrighteous |
| `[Drop]` `[Build]` `[Build-Up]` | Energy | UNOFF | reddit 1mym1dm, tagasong |
| `[Instrumental]` `[Instrumental Break]` `[Instrumental Outro]` | Instrumental | UNOFF | HookGenius, reddit v6 guide |
| `[Guitar Solo]` `[Piano Solo]` `[Solo]` `[Solo Section]` | Instrumental | UNOFF | HookGenius, sunometatagcreator, reddit 1hsoo5t |
| `[Whispered]` `[Spoken Word]` / `[Spoken]` `[Belted]` `[Falsetto]` `[Harmonized]` | Vocal delivery | UNOFF | SongSmith, reddit 1hsoo5t |
| `[Ad-lib]` `[adlib hey]` `[Growl]` `[Screams]` | Vocal ad-lib | UNOFF | SongSmith ad-lib guide, sunometatagcreator |
| `[Male Vocal]` `[Female Vocal]` `[Choir]` `[Gang Vocals]` `[Harmonies]` | Vocal | UNOFF | HookGenius, sunometatagcreator |
| `[End]` `[Fade Out]` `[Hard Stop]` `[Silence]` | End / utility | UNOFF | reddit tagsproper, tagasong, reddit v6 guide |
| `[Big Finish]` `[Sting]` `[Final Chorus]` | Utility | UNOFF | reddit 1hsoo5t, reddit v6 guide |
| `[Acapella]` `[Vocals Only]` | Utility | UNOFF | reddit tagsproper |
| Colon syntax `[Chorus: big, anthemic]` / `[Parameter: Value]` | Combo | UNOFF | AceTagGen, tagasong, reddit 1mym1dm |
| Curly braces `{tag}` = emphasis | Bracket type | UNOFF (low confidence, about 50%) | AceTagGen |
| `[Hyper-Realistic]`, `[Heavy Stomp and Clap]` and similar "quality unlock" tags | Fabricated / freeform | UNOFF, **explicitly debunked** | roo.beehiiv, "The Tag That Doesn't Exist" |
| `[Emotional Moment]`, `[Dubstep Drop]` as fixed tags | None | UNOFF, "aren't standard tags" | HookGenius lyrics formatting |

## 5. Tag mechanics

Community consensus on how brackets behave:

- **Placement.** Tags go on their **own line above** the section they govern. Inline placement between lyric lines "confuses the parser".
- **Stacking.** Combine several cues inside one bracket with `|` or commas: `[anthemic chorus | stacked harmonies | bass drop]` (reddit 1mym1dm). One commenter reports `|` behaves the same as a comma.
- **Combine style + structure into one tag.** `[Powerful Chorus]`, `[Stripped Bridge]` reportedly outperform two separate tags because they read as a single instruction (AceTagGen).
- **Priority runs left to right:** section identity, then vocal delivery, then instrumentation, then effects. Later tags get dropped first. Practical cap: **2 to 4 tags per section** (AceTagGen; corroborated by reddit reports that 6+ confuses the model).
- **Probabilistic, not deterministic.** Every community source stresses tags are "hints, not commands" (sunometatagcreator FAQ, reddit megathread).

A lyrics-box layout assembled from the attested fragments above:

```
[female vocals]                      <- official: pair with Exclude "male vocals"
[Intro: sparse drums]                <- colon syntax (community)

(hey!) (oh-oh)                       <- parentheses: always sung, backing vocals
[Verse 1]
I keep the receipts of every summer...
[Pre-Chorus: building]               <- style + structure in one tag

[Chorus: big, anthemic | stacked harmonies]
...
[Instrumental Break]
[Outro] [Fade Out]
```

## 6. Style of Music field mechanics

- **Accepts:** genre + subgenre, instrumentation, vocal type, mood, tempo/BPM, production terms, era. The official glossary explicitly recommends combining tempo + genre, dynamics, instrumentation, structure terms, production effects, and genre blends. **[OFFICIAL]**
- **No brackets here.** Community sources are unanimous: tags belong in Lyrics; the Style box takes bracket-free, comma-separated descriptors (tagasong, sunometatagcreator).
- **Length.** Concise wins: roughly 130 characters is efficient, and **4 to 7 descriptors** is the consensus sweet spot (roo, HookGenius). Suno weighs the **earliest terms most** (HookGenius, roo).
- **Recommended ordering** (reddit 1wcyryw): Genre, then Vocals, Drums, Guitars, Bass, Other instruments, Arrangement/Energy, Production Quality, Ending, then slider notes.
- **Official note:** "Simple genre tags can expand into detailed descriptions" (v4.5 release note, the prompt-enhancement helper).

Example style line (front-loaded, comma-separated):

```
dark r&b, sultry, rhodes keys, deep 808 sub, airy male falsetto, tape reverb, nocturnal, 88 bpm
```

## 7. Exclude Styles

| Aspect | Fact | Flag |
|---|---|---|
| Where | Create, Advanced mode, **Advanced Options**, Exclude | **OFF** |
| Who | Pro / Premier plans | **OFF** |
| What to put | Instruments, styles, **vocal styles** ("male vocals", "autotune", "drums") | **OFF** |
| UI feedback | Excluded items shown in the preview and song page with a leading **`-`** (for example `-piano`) | **OFF** |
| Official trick | Put `[female vocals]` in Lyrics and exclude "male vocals" | **OFF** |
| Learning signal | Thumbs up / thumbs down on results helps Suno improve Exclude | **OFF** |
| Reliability | Reports range from "never excludes, always includes" to "works 90%+ of the time". Mixed. | COMMUNITY |
| Length | Measured `maxlength="1000"` on v5.5 | COMMUNITY |

Sources: help 3161921; release-notes/exclude-styles; reddit 1j5jq43, 1mvo9vx; HookGenius limits.

## 8. Character limits

Suno has **never published** these numbers. All values below are measured from the live composer (HookGenius) or mirrored by third-party API docs (docs.sunoapi.org).

| Model | Style | Exclude | Lyrics | Title |
|---|---|---|---|---|
| **v6 / v6-wild / v6-mini** | 1,000 | 1,000 | 5,000 | ~100 (no `maxlength` observed on v6; unverified) |
| v4.5 / v5 / v5.5 | 1,000 | 1,000 | 5,000 | 100 |
| v4 and older | 200 | n/a | 3,000 | 80 |
| Simple-mode description | 3,000 | n/a | n/a | n/a |
| Sounds "describe the sound" box | 500 | n/a | n/a | n/a |

Notes:

- **Title discrepancy:** docs.sunoapi.org says 80 characters for all models; HookGenius measured no maxlength on v6. Treat these as planning numbers.
- The third-party API enforces: v6 style 1,000 / lyrics 5,000 / negativeTags 1,000; v4.5 to v5.5 prompt 5,000 / style 1,000; v4 prompt 3,000 / style 200.
- Practical lyrics sweet spot: about 3,000 characters before Suno starts rushing the material **[COMMUNITY]**.

## 9. Instrumental controls

- **Instrumental toggle (official).** Advanced-mode step: "Toggle Instrumental if you prefer not using lyrics." In Simple mode, describe the instrumental directly, for example *"an ethereal electro hypnotic instrumental with sweeping pads"* (help 3726721).
- **Instrumental tags (unofficial).** Community warns that `[Instrumental]` mid-song "can sometimes cause the AI to stop singing for the rest of the clip". The recommended double-lock is `[Instrumental]` at the start and `[No Vocals]` at the end (reddit tagsproper, roo).

```
[Instrumental]
... (intro section) ...
[No Vocals]
```

## 10. Sliders and advanced controls

- **Weirdness** (Safe to Chaos): 50% is "normal". **[OFFICIAL]**
- **Style Influence** (Loose to Strong): how hard Suno follows the Style field. **[OFFICIAL]**
- **Audio Influence**: only active when you upload audio. **[OFFICIAL]**
- **Variety** (v6): reduce to 0 to retain full control of your style tags. **[OFFICIAL]** (v6 FAQ)
- **Max Mode** (v6): a toggle that costs extra credits; used for long songs, covers, and consistency. **[OFFICIAL]** (v6 FAQ)
- **Duration slider** (v5.5 web, added 2026-07-20). **[OFFICIAL]**
- Third-party API parameters that mirror these controls: `styleWeight`, `weirdnessConstraint`, `audioWeight`, `variety`, `vocalGender`, `negativeTags`, `personaId`, `personaModel`, `duration` (10 to 360 seconds). **[COMMUNITY, third-party API]**

## 11. Personas, Voices, Custom Models

- **Personas:** save the essence of a song (vocals + style) and reuse it. Created from an existing song, **public by default**, applied in Advanced mode from the slot **above the lyrics field**; the persona's style details auto-populate Style of Music. **[OFFICIAL]** (help 3484161)
- **Voices:** verified voice cloning (v5.5+). **[OFFICIAL]**
- **Custom Models:** train a model on 6+ of your own tracks (v5.5+). **[OFFICIAL]**
- **My Taste:** a passive personalization signal (v5.5+). **[OFFICIAL]**

## 12. Lyrics formatting: how Suno reads your text

| Syntax | Interpreted as | Flag |
|---|---|---|
| `[Square brackets]` | Instruction or cue; **never sung**; own line above the section | UNOFF (except the official `[female vocals]` example) |
| `(parentheses)` | **Backing vocal / ad-lib / echo, ALWAYS sung.** Instructions inside get sung literally: `(whispered)` makes Suno sing the word "whispered" | UNOFF (strong consensus) |
| Line breaks | Single break = within a section; blank line = section break; each line is roughly one breath | UNOFF |
| ALL CAPS | Louder / more forceful; use on 1 to 3 words | UNOFF |
| `~` | Sustain with vibrato | UNOFF (SongSmith) |
| `-` / `G-A-L-A-X-Y` | Stretch a syllable / spell out letters | UNOFF |
| `"quotes"` | Spoken or whispered phrase | UNOFF |
| `....` | Longer sustain than tilde | UNOFF |
| `(x2)` / `(repeat)` | Unreliable; physically repeat the line instead | UNOFF |

## 13. Post-generation features and plan gating

Facts present in the sources:

- **v4 added** Extend, Cover, Persona, Remaster, and the ReMi lyrics tool. **[OFFICIAL]**
- **v3.5** supported 2-minute extends; **v4.5+** added Add Vocals / Add Instrumental. **[OFFICIAL]**
- **v6** adds plain-language section editing and mashups; all post-hoc operations on pre-v6 songs now run on v6. **[OFFICIAL]**
- **Stems:** Auto Split = 12 stem categories; Split from Mix = one instrument plus the rest; **Advanced Split** (~100 instruments) is **Premier only** (updated 2026-06-11). **[OFFICIAL]**
- **Plan gating:** Exclude Styles is **Pro/Premier**; Advanced Split is Premier; Max Mode costs extra credits. **[OFFICIAL]**
- Personas are **public by default**; artist-name prompts are filtered ("we've never allowed prompts for specific artists", Suno responsibility blog). **[OFFICIAL]**
- Not covered by this research: full pricing tables, credit costs per generation, and Suno's copyright/ownership terms. Inpainting / "Replace Section" was not documented in the sources reviewed.

## 14. Official vs community lore, at a glance

**OFFICIAL:** field names and positions; Instrumental toggle; Exclude mechanics (`-` prefix, Pro/Premier, thumbs feedback); Personas above the lyrics field; Creative Sliders; v6 Variety and Max Mode; Duration slider; Voices / Custom Models / My Taste; the lone `[female vocals]` example; the "Verse / Outro labels" line; the Music Glossary's vocabulary.

**COMMUNITY LORE (no Suno confirmation):** the entire bracket-tag catalogue and placement rules; stacking with `|`; colon syntax; curly braces; the 2 to 4 tags per section cap; all character-limit numbers; the `[Instrumental]` + `[No Vocals]` double-lock; "4 to 7 descriptors" in Style; reliability percentages (90/70/50%); the `[Hyper-Realistic]` "quality unlock" (explicitly debunked).

## Sources

Official (suno.com / help.suno.com):

- v6 FAQ: https://help.suno.com/en/articles/13924481
- Exclude Styles: https://help.suno.com/en/articles/3161921
- Personas: https://help.suno.com/en/articles/3484161
- Android Create: Custom Mode: https://help.suno.com/en/articles/3726721
- iOS Create: Custom Mode: https://help.suno.com/en/articles/3197377
- Android Create: Simple Mode: https://help.suno.com/en/articles/3726657
- Simple mode (current): https://help.suno.com/en/articles/2462273
- Simple, Advanced, and Sounds naming: https://help.suno.com/en/articles/10625537
- Music Glossary: https://help.suno.com/en/articles/9010177
- Creative Sliders: https://help.suno.com/en/articles/6141377
- Can I use my own lyrics?: https://help.suno.com/en/articles/2415873
- Song Editor: https://help.suno.com/en/articles/6141505
- What is a Cover?: https://help.suno.com/en/articles/2872257
- Can I change the voice or lyrics?: https://help.suno.com/en/articles/2417409
- How do I make my song longer?: https://help.suno.com/en/articles/2409601
- Add Vocals: https://help.suno.com/en/articles/6882817
- Making Music category: https://help.suno.com/en/categories/550017-making-music
- Release notes index: https://suno.com/release-notes
  - exclude-styles, lyrics-improvements-on-web, creative-control, introducing-v5-5, duration-slider, introducing-personas
- v5.5 blog: https://suno.com/blog/v5-5
- Suno responsibility blog: https://suno.com/blog/building-the-future-of-music-responsibly

Community:

- reddit r/SunoAI: metatags guide 1mym1dm; meta tag megathread 1he744i; exclude threads 1j5jq43, 1mvo9vx; brackets list 1hsoo5t; how to use tags properly 1od1cll; v6 prompting guide 1wcyryw; song section tags 1pap675; where tags go 1jpe2un (all under https://www.reddit.com/r/SunoAI/comments/)
- sunometatagcreator.com/metatags-guide
- hookgenius.app/learn/suno-character-limits/ and hookgenius.app/learn/suno-lyrics-formatting/
- songsmith.studio/blog/suno-structure-tags-cheat-sheet, songsmith.studio/blog/suno-ad-lib-placement, songsmith.studio/blog/suno-lyric-formatting-symbols
- acetaggen.com/blog/bracket-tags-directors-language-suno
- tagasong.com (square-brackets tag guide)
- musci.io/blog/suno-tags
- jackrighteous.com, article "Why Your Suno v6 Meta Tags Aren't Working" (slug: why-your-suno-v6-meta-tags-arent-working)
- stokemctoke.com, complete Suno meta tags guide
- roo.beehiiv.com, "Suno V5.5 Best Practices: The Tag That Doesn't Exist"
- docs.sunoapi.org/suno-api/generate-music (third-party API limits)
- suno.com/style/suno-will-usually-treat-text-in-parentheses-as-a-backing-vocal-or-a- (user-created style page, not official docs)
