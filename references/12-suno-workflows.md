# Suno Advanced Workflows: Extend, Cover, Stems, Personas, and Alternatives

How to run Suno beyond one-shot generation: the full feature ladder (extend, cover, remaster, personas/voices, stem separation, Song Editor surgery, uploads, mashups, Studio 2.0), the credit/download economy that constrains it, community-tested recipes, failure-mode fixes, competitor tools, and the legal picture. Facts dated October 2026; Suno changes fast, so re-verify on help.suno.com.

## Quick rules

- Work the ladder instead of re-rolling: generate, repair with **Replace Section** (10-30 s inpainting), transform with **Cover/Remaster**, split **stems**, finish in **Studio 2.0**. Never regenerate a whole song to fix one part.
- **Always Extend from the full song**, never from a partial section. The model only "knows" the fragment you extend from, so partial extends drift.
- Every generation makes **2 songs for 10 credits**. Budget accordingly.
- The real constraint is **downloads**, not credits: Free 7 lifetime, Pro 20/mo, Premier 60/mo (since Sep 3 2026, applies to your whole back catalogue). **Studio 2.0 workflows are exempt from download limits**, which makes Premier the de facto production tier.
- Songs made **while subscribed** are yours commercially, and you keep commercial rights after cancelling, but you must **download them while subscribed** for the license to attach. Free-plan songs are Suno's.
- v6 (Sep 9 2026) retired every pre-v6 model. The three live models are `v6`, `v6-wild` (Pro/Premier) and `v6-mini` (all plans), all up to 8 minutes per generation. v6 mix quality is genuinely contested: see the honesty flag in section 5.
- No official seed control and no "phone trick" exist. Community workarounds (Extend from 0:00/0:01, Reuse Prompt) are lore, not reproducible features.
- Suno is the best default for vocal-forward songs you can actually export, but Mureka is ~25x cheaper per kept song, Udio beats it on pure instrumentals yet cannot export at all, and Stable Audio 3.0 is instrumental-only.

## 1. Model landscape and field limits

| When | What happened |
|---|---|
| Sep 9 2026 | **v6 family** launches: `v6`, `v6-wild`, `v6-mini`. All pre-v6 models retired. v6 was built with WMG, BMG and Believe. |
| Sep 3 2026 | New Terms of Service plus **download caps** (Free 7 lifetime / Pro 20/mo / Premier 60/mo). |
| Aug 13 2026 | **Studio 2.0**: MIDI, effects, wavetable synth, chat bar. |
| Oct 1 2026 | **Speech (beta)**: speech plus soundtrack in one take. |
| Oct 5 2026 | **Albums** publishing. |
| Oct 2 2026 | News reports Suno "far beyond" 2m subscribers and roughly $300m annual revenue. |

Models: `v6` is the flagship (Pro/Premier), `v6-wild` is the experimental variant (Pro/Premier), `v6-mini` is the free-tier model. All three generate up to **8 minutes** in one pass. Field limits are community-measured, never officially documented: Style **1,000** chars, Exclude **1,000**, Lyrics **5,000** (practical sweet spot around 3,000), title 100 (unverified).

## 2. The feature ladder

### 2.1 Extend (lengthen or re-end a song)

1. Find the song, open `...`, choose **Remix/Edit**, then **Extend**.
2. Drag the white arrow to pick how much of the song to keep.
3. Add lyrics and style direction, then Create.
4. Open `...` again, choose Create, then **Get Whole Song** to stitch the parts.
5. In the Song Editor, the **+** at the right of the track gives **Quick Extend** for a seamless continuation.

Use it when a song cuts short, you want a new ending, or you are building a long track. Community rule (consistency guide): always extend from the **full song**, not a partial section.

### 2.2 Cover

Transforms the style of an existing song while keeping the melody. `...` then Create, then **Cover Song**. You can only cover **songs you created**. The help article describes it as a Pro/Premier beta (200 free covers, then 10 credits each); the current pricing page lists cover under "remix songs (extend, cover, adjust speed)" more broadly, so the tier gate is ambiguous now. Cover means a *significant* transformation (vocalist, style, timing); Remaster means *subtle* mix polish. Classic uses: genre change, instrumental to vocal, hearing the same melody as a different act.

### 2.3 Remaster

Create menu, then **Remaster**. Pick **Variation strength**:

- **Subtle**: cleaner mix, clearer pronunciation.
- **Normal**: default; same duration and style.
- **High**: noticeable vocal and arrangement changes.

Remaster is not intended for lyric changes or drastic style shifts. Use it when you love the take but want a cleaner master.

### 2.4 Personas and Voices

- **Personas** (Oct 2024) capture a song's vocals, style and vibe. Create from a song: `...`, Create, **Make Persona**. Apply via the Personas area above the lyrics box in Custom mode. Personas now live inside the **Voices** menu; Style Personas are still available.
- **Voices** (v5.5, Mar 2026) replaced Personas in the Create menu: record or upload 15 s to 4 min of audio, pick the best 2 minutes, read a phrase to **verify identity**, then sing in your own voice. Turn the **Audio Influence** slider up. 18+, region-limited.

Use both for a consistent artist identity. Community tip: reuse the style prompt plus Persona plus Exclude for consistent vocals across tracks.

### 2.5 Stems and split modes

| Mode | What it does | Cost | Tier |
|---|---|---|---|
| **Auto Split** | Up to 12 stems (drums, bass, guitar, keys, woodwinds...) | 50 credits | Paid |
| **Split from Mix** | Pull one instrument or vocal plus its complement | 10 credits (20 for both) | Pro+ |
| **Advanced Split** | Choose from roughly 100 instruments, custom stems | 10 credits per stem | Premier only |

Official caveat: asking for a stem that is not present can still burn credits and return nothing. In **Studio v1.1, Stem Cover** turns a stem into a new instrument while keeping the rhythm; **Cover** references the original source audio, **Recreate** references the currently selected audio.

### 2.6 Song Editor: Replace Section, Crop, Fade

This is Suno's inpainting and the single most useful "don't regenerate everything" tool (Pro/Premier):

1. Open the song in the **Song Editor**.
2. Highlight a **10-30 s** span.
3. **Replace Section**: edit the lyrics, or type an instrumental direction such as `[drum break]`, then **Recreate Section**.
4. Preview **2 versions**, pick one with **Select**; a Whole Song regenerates with your fix spliced in.

Also in the editor: **Quick Replace** (instant audition of a new section version), **Edit Lyrics** (highlight, replace, audio regenerates), **Move/Split/Crop** sections (drag the grab tool to reorder), **Delete**, and **Fade In/Out** on first and last sections. v6 adds plain-language section editing ("change the chorus so it's sung by a gospel choir") and single-lyric changes without rebuilding.

### 2.7 Audio uploads

Upload audio free up to **8 minutes**, Pro/Premier up to **30 minutes**; the button sits next to Create. Uploads pass a safeguard screen for unauthorized use. Feed it hummed melodies, demos or voice memos; uploads then feed Extend, Cover and Add Vocals.

### 2.8 Mashup and Sample

Right-click any sound and choose **Mashup** (blend two songs) or **Use as Sample** (Jan 20 2026). v6 does this in natural language: "Take the vocals from x, drums from y, add new lyrics... 80s synthwave."

### 2.9 Inspire, Suno Sounds, My Taste, Custom Models

- **Inspire**: generate in the style of a playlist of your own songs. Short playlists (3-5 tracks) give the most control.
- **Suno Sounds**: generate SFX, samples and loops as One Shot or Loop, with BPM and key.
- **My Taste**: personalization for all users; thumbs up/down trains it.
- **Custom Models**: Pro/Premier. Train up to 3 model variants on at least 6 of your own tracks; takes 2-5 minutes. Since Oct 15 2026 Premier users can **share custom models** with collaborators, with 2x the inputs [OFFICIAL, release notes 2026-10-15].
- **Workspaces**: invite-only shared song library for a team; Pro and Premier only (Oct 15 2026) [OFFICIAL, release notes 2026-10-15].

### 2.10 Add Vocals / Add Instrumental

Upload or generate an instrumental, then `...`, **Add Vocals**, enter lyrics, and tune the **Audio Strength** slider. Add Instrumental is the reverse. Conflict flag: the help article describes Add Vocals as a Pro and Premier beta, but the current pricing page lists "Add new vocals or instrumentals" only under **Premier**. Likely a tier change since the help article; verify on your plan.

### 2.11 Studio 2.0 (Premier)

A browser DAW: MIDI, chat bar, audio effects, wavetable synth, automation; exports stems, MP3 and MIDI. Late-Oct 2026 releases add clip timestretching, shaped fade curves, semitone/cents pitch adjustment, a clip info panel, track show/hide and grid density controls [OFFICIAL, release notes 2026-10-08 and 2026-10-29]. **Studio workflows are exempt from download limits**, so heavy iteration belongs here.

### 2.12 Sliders and other controls

**Creative Sliders**: Weirdness (Safe to Chaos), Style Influence (Loose to Strong), Audio Influence. **Duration slider** on web (changelog ties it to v5.5; unclear whether v6 honors it). **Vocal Gender** selector on web and mobile. Plus Hooks (short videos), Scenes (photo to song), Speech (beta), Albums. **Suno MCP (beta, Oct 28 2026)** drives create, Cover, Extend, Mashup, Speech and audio upload from Claude, ChatGPT, Claude Code or another MCP client; it works on every plan and spends your credits [OFFICIAL, help.suno.com 14551361 and release notes 2026-10-28].

## 3. Plans, credits, and downloads

| | Free | Pro | Premier |
|---|---|---|---|
| Price | $0 | $10/mo ($8 annual) | $30/mo ($24 annual) |
| Credits | **50/day** (~10 songs/day) | **2,500/mo** (+50/day after exhaustion) | **10,000/mo** (+50/day after exhaustion) |
| Models | v6-mini | v6, v6-wild, v6-mini | v6, v6-wild, v6-mini |
| Downloads | 7 lifetime (personal only) | **20/mo** | **60/mo** |
| Commercial rights | No | Yes | Yes |
| Stems | No | Auto + Split from Mix | + Advanced Split |
| Upload length | 8 min | 30 min | 30 min |
| Queue | shared | priority, 10 at once | priority, 10 at once |
| Studio / Add vocals / Add instrumentals | No | No (per pricing page) | Yes |
| Voices / Custom Models | preview | Yes (3 custom models) | Yes |

Economy details: re-downloading the same song or a different format costs nothing extra; stems ride along with the song's download; failed downloads don't count. Subscription credits **don't roll over**; purchased top-ups don't expire but need an active subscription. Third parties report extra songs at $2.99 each (unofficial).

## 4. Community recipes

Community advice is folklore plus practical heuristics, not official documentation.

### Recipe 1: instrumental first (best-rated workflow)

1. Generate an **instrumental only** (no Persona, no Cover).
2. Run **Covers** of it, changing the prompt, mood and instruments **each time**; always use **Exclude Styles**.
3. Pick the best take, then **edit structure**: rearrange, copy, delete, move a section to the end, then Extend.
4. Write lyrics **to the finished structure**.
5. **Cover** that version with a **Persona**, reusing the prompt and style, and paste the lyrics.
6. Expect roughly **10-12 generations** to a finished track. Use thumbs up/down to train the model.

### Recipe 2: section-by-section build

Generate and Extend piece by piece, always extending from the **full song**. Fix weak parts with Replace Section rather than re-rolling.

### Recipe 3: fix a bad chorus

Song Editor, highlight 10-30 s, **Replace Section**, adjust lyrics or add `[drum break]`, preview the 2 versions, Select. This is the canonical "fix the chorus without losing the song" move.

### Recipe 4: add vocals to an instrumental

Either use native **Add Vocals**, or upload the instrumental and **Cover** it while pasting lyrics (the older workaround).

### Recipe 5: meta-tag discipline

- Put structural tags `[Intro][Verse][Chorus][Bridge][Outro]` **in the lyrics**, and descriptors in both Style and lyrics.
- Stack with `|` or commas: `[Chorus | anthemic | stacked harmonies | modern pop polish]`.
- **4-7 tags per section max**; most important tags first.
- Heavy bracketed tags can break Song Editor section detection.

### Recipe 6: Weirdness slider settings ("Dirty Tricks #19")

Covers and tributes 10-20%; radio pop 20-30%; **avoid 45-55% (generic dead zone)**; creative indie 55-70%; experimental 70-85%; fusions 75-95%. Single-source community table.

### Recipe 7: prompt structure beats wording

A controlled v5.5 test (one tester, unverified) found a fully structured prompt with named categories (vocal, genre, structure, anti-prompt) scored 10/11 on mix metrics versus 4/11 for a flat tag list. The same author claims output degrades at peak server load, so generate early in the morning CET. Unaudited.

### Seed and continuation lore

Suno exposes **no official seed**. The community workaround is to **Extend from 0:00/0:01** or use **Reuse Prompt** to approximate the same generation. Reliability is low; treat it as lore. **"The phone trick": targeted searches found no established Suno "phone trick"** (results were phone-scam content). The closest real lore is the hum-or-beat into Upload Audio to get an instrumental, and the contested "quality drops at peak load" theory.

## 5. Failure modes and fixes

| Failure | Likely cause | Fix |
|---|---|---|
| Tags ignored | Style compressed into a lossy vector; later tags truncated | Genre and key tags **first**; 4-7 descriptors; use **both** style and lyrics; move unwanted items to **Exclude** |
| Wrong pronunciation | Sings by spelling, not meaning | Phonetic respelling before generating (`through` to `thru`, `colonel` to `kernel`, `tonight` to `to-night`, `AI` to `A I`, `24/7` to `twenty four seven`); can't fix after the fact |
| Abrupt ending | Missing ending tags | `[Outro: descriptors]` plus `[End]`; keep the outro 15-25 s; add "resolve, no restart"; or **Crop + Fade** in the editor |
| Genre drift | Vague or conflicting tags; genre listed last | **Genre first**, add BPM, remove conflicting instruments, use **Exclude**, lower Style Influence |
| Unwanted male/female vocal, or mid-song switch | Gender is a probabilistic hint | **Vocal Gender** selector plus style terms ("gritty male vocal"); Exclude the other; regenerate; Replace Section; Studio has gender-change tools |
| Muddy mix, buried vocal (v6 complaint) | Dense low-mids, vocal buried | **Thin the arrangement under the vocal**; instruct "in front of the band, close and dry, loudest element"; **Remaster**; if it's a dull render, regenerate or try v6-wild; master to a target LUFS |
| Repetitive sections, song loops | No structure direction; flat energy | Add `[Verse 1]/[Verse 2]/[Bridge]/[Final Chorus]`, variation descriptors ("evolving", "building"); avoid "hypnotic/looping" |
| Over-running, rushing, skipped sections | Too many lyrics; duration and load pressure | Cut lyrics to roughly **30-40 lines** (under ~3,000 chars); multi-section tags; Duration slider; Extend; Replace Section for the missing part |
| Instruments "compete" or sound synthetic | v6 rendering character | Thin the arrangement or use v6-wild; even v6 defenders report instruments "sound like they're coming from a synth" |

**v6 honesty flag:** Suno markets v6 as faster, more expressive and higher quality; a vocal subset of creators call it muffled, buried and repetitive, with some cancellations. Evidence is split and **no representative survey exists**. Fidelity went up; "feel" is contested.

## 6. Alternatives (October 2026)

| Tool | Entry price | Kept-song cost | Export | Strengths | Weaknesses vs Suno |
|---|---|---|---|---|---|
| **Suno (v6)** | $10 ($8 annual) | **$0.50** | 20-60/mo downloads | Best vocals, full song workflow, Studio, rights-to-release; 2m+ subs | Download-gated; v6 mix backlash; Sony/UMG suit |
| **Udio** (v1.5 Allegro) | $10 ($8) | n/a, no export | **Downloads disabled since 29 Oct 2025** | Excellent 48kHz instrumentals, fast iteration | Cannot export or release anything; UMG/WMG deals; walled garden |
| **Mureka** (V9.5) | $10 ($8) | **~$0.02** | Unlimited MP3; WAV/stems on Premier | Very cheap, MIDI export, DAW session, 12 stems | Vocals behind Suno; less polished English vocals |
| **ElevenLabs Music** (v2.5) | $6 to $22 | $0.33-0.65 | Lossless WAV on Creator+ | Spotify/Apple release from Creator tier; strong voice tech; 10 min songs | Minute-based billing; self-serve excludes film/TV/games; no artist names in prompts |
| **Google Flow Music** (Lyria 3.5) | $8 ($6) | **~$0.013** | Downloads plus stems on every plan | Cheapest per kept song; stems everywhere | **SynthID watermark** on every track; ~3 min; licensed-data unclear |
| **Stable Audio 3.0** | $12 | ~$0.07 | Within credits | **Best instrumentals**, open-weight, licensed data | **Instrumental only**, no vocals |
| **AIVA** | €11 | ~€0.11 (Pro) | 15-300/mo | Pro tier: **copyright owned by you**; MIDI export | Instrumental and scores only; monetization limits on lower tiers |
| **Soundraw / Beatoven / Mubert** | $9.99+ | varies | Limited | Background and library music | No streaming release (Beatoven/Mubert terms), mostly instrumental |
| **Riffusion / Producer.ai** | Free tier | ~$0 | varies | Free, FUZZ models, community favourite for some genres | Uncertain current branding (see section 8); below Suno on vocals |

**Honest assessment of "Suno is best".** For vocal-forward, full-song creation with an end-to-end workflow and export rights on a paid plan, the claim largely holds: Suno has the strongest vocals, the deepest editing suite (Replace Section, Studio, stems) and, unlike Udio, you can actually download and release. Caveats: (a) cost-per-kept-song is roughly **25-40x higher** than Mureka or Flow Music because of download caps; (b) Udio arguably wins pure instrumentals but is export-crippled; (c) Stable Audio 3.0 is better for instrumentals and licensing; (d) v6 mix quality is genuinely contested, and some creators prefer v5.5-era output; (e) ElevenLabs and Google are closing the gap on vocals. "Best default for songs with vocals" is defensible; "best at everything" is not.

## 7. Rights, copyright, and legal picture

**Suno's own policy:**

- Free plan: **Suno owns** the songs; personal, non-commercial use only, no monetization.
- Pro/Premier: **you own** songs made while subscribed and keep commercial-use rights **even after cancelling**, but songs must be **downloaded while subscribed** to carry the commercial license.
- No retroactive rights: subscribing does not retroactively license free-plan songs.
- Monetizing remixes of **other people's** songs is not allowed; your own remixes can qualify via a paid download credit.
- Suno grants **commercial use**, not **copyright**. Registration is a separate, harder question.

**Terms-of-service reality (Aug 2026 analysis):** Suno's TOS grants Suno a **"perpetual, irrevocable"** license over your submissions and outputs, including monetization and model training "without compensation"; you **waive moral rights**; Suno makes **no warranty that copyright vests** in the output; and output **"may not be unique across users."** The Sep 3 2026 update added download limits (applying to your whole back catalogue) and clarified rights and arbitration. For commercial users the single most important nuance: **you get a contractual right to monetize, not a guaranteed copyright**.

**US Copyright Office position:** copyright protects **human authorship**; material generated 100% by AI is not protectable, and writing the prompt does not make you the author. Anchored by the March 2023 registration guidance, the **Part 2: Copyrightability** report, and the *Thaler v. Perlmutter* line of cases (D.C. Circuit affirmed refusal to register AI-only works; cert denied). Practical takeaway: you can register your lyrics if 100% self-authored, and full-work registration may be possible where human contribution is sufficient, but the AI-generated audio itself is on shaky ground.

**Litigation and licensing timeline (news):**

- **Nov 25 2025**: Warner Music Group settles with Suno and strikes a first-of-its-kind partnership; WMG had joined the original 2024 suit.
- **Sep 9 2026**: v6 built with WMG, BMG and Believe.
- **Sep 18 2026**: UMG and Sony file a **second lawsuit** over v6, alleging v6 inherits unlicensed training (60,202 sound recordings) via user-interaction and distillation. Suno says v6 was trained on licensed content plus user creations and preference signals.
- **Udio**: settled with UMG (Oct 29 2025) and WMG (Nov 19 2025), then **disabled all downloads**.

**Bottom line:** a Suno paid plan gives a contractual commercial license (distribute, monetize, keep royalties) but no warranty of copyright. Distributors increasingly screen for AI and some reject non-copyrightable works. Document your human contributions, register lyrics separately where possible, and read the current TOS at suno.com/terms-of-service.

## 8. Known conflicts and uncertainty

1. **Voices model requirement**: the Voices FAQ says v5.5 must be selected, but all pre-v6 models were retired Sep 9 2026. The FAQ is stale; Voices now runs on v6.
2. **Add Vocals tier**: help article says Pro and Premier; current pricing page implies Premier only. Likely tier change.
3. **Cover tier**: help article says Pro/Premier beta; pricing page lists cover under remix more broadly. Ambiguous.
4. **v6 quality**: Suno's "higher quality" claim versus a vocal creator minority reporting muffled, repetitive output. No representative survey; treat both as claims.
5. **Riffusion branding**: one source claims "Riffusion Is Now Google Flow Music"; others call it "Producer.ai / FUZZ-2.0". Unverified; Riffusion's current ownership was not confirmed.
6. **Character limits**: measured by community, never documented by Suno, may change silently.
7. **"Phone trick" and "seed trick"**: no established phone trick found; no official seed control exists. Community workarounds are not reproducible.
8. **Custom models shared**: the Oct 15 2026 release notes let Premier share custom models; the Custom Models help article (v5.5, edited Sep 9 2026) still says models "cannot be shared amongst users". Treat the release note as current.

## How to apply this

- Default to the repair ladder: generate, Replace Section for local fixes, Remaster Subtle for polish, Cover for transformation. Re-rolling the whole song is the expensive path.
- Budget in downloads, not credits: a Pro month buys 1,250 songs' worth of generation but only 20 keepers, so mass-generate and keep ruthlessly.
- For a release-quality track, follow Recipe 1 (instrumental first, cover with a Persona) and expect around 10-12 generations.
- Put heavy iteration in Studio 2.0 on Premier; Studio work bypasses the download cap, and stems/MIDI export live there.
- If a competitor fits better, reach for Mureka or Flow Music when cost-per-kept-song dominates, Stable Audio 3.0 for instrumental licensing work, and remember Udio currently has no export at all.
- Before commercial release: download while subscribed, keep proof of your human contributions (lyrics, edits, arrangement), and plan to register lyrics separately.
- Re-verify tier gates, caps and model behavior on help.suno.com and suno.com/pricing before committing a project; everything in this doc is dated October 2026.

## Sources

- https://suno.com/pricing
- https://suno.com/release-notes
- https://suno.com/blog/introducing-v6
- https://suno.com/blog/suno-updates-tos
- https://suno.com/blog/v5-5
- https://suno.com/blog/covers
- https://suno.com/terms-of-service
- https://help.suno.com/en/articles/13924481 (v6 FAQ)
- https://help.suno.com/en/articles/13924737 (current models)
- https://help.suno.com/en/articles/13924801 (what's new in v6)
- https://help.suno.com/en/articles/13924929 (song length)
- https://help.suno.com/en/articles/13926145 (what counts as a download)
- https://help.suno.com/en/articles/13926209 (downloads per plan)
- https://help.suno.com/en/articles/2410049 (plan types)
- https://help.suno.com/en/articles/2409601 (Extend)
- https://help.suno.com/en/articles/2872257 (Cover)
- https://help.suno.com/en/articles/8105281 (Remaster)
- https://help.suno.com/en/articles/3484161 (Personas)
- https://help.suno.com/en/articles/11362369 (Voices)
- https://help.suno.com/en/articles/11362433 (Voices FAQ)
- https://help.suno.com/en/articles/14551361 (Suno MCP beta)
- https://help.suno.com/en/articles/12702337 (Advanced Stem Separation)
- https://help.suno.com/en/articles/9819905 (Stem Cover)
- https://help.suno.com/en/articles/6141505 (Song Editor)
- https://help.suno.com/en/articles/3271873 (Replace Section)
- https://help.suno.com/en/articles/3166529 (Crop)
- https://help.suno.com/en/articles/6141569 (Audio Uploads)
- https://help.suno.com/en/articles/6882817 (Add Vocals)
- https://help.suno.com/en/articles/6882753 (Inspire)
- https://help.suno.com/en/articles/6141377 (Creative Sliders)
- https://help.suno.com/en/articles/11362497 (Custom Models)
- https://help.suno.com/en/articles/10625537 (Suno Sounds)
- https://help.suno.com/en/articles/10153473 (vocal gender)
- https://help.suno.com/en/categories/550145-rights-ownership
- https://help.suno.com/en/articles/9601665 (paid-plan rights)
- https://help.suno.com/en/articles/9604993 (monetizing remixes)
- https://help.suno.com/en/articles/9601985 (commercial use)
- https://help.suno.com/en/articles/2746945 (do I have copyrights)
- https://help.suno.com/en/articles/2430081 (registration)
- https://help.suno.com/en/articles/2410177 (distribution)
- https://help.suno.com/en/articles/2425729 (retroactive rights)
- https://www.copyright.gov/ai/
- https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf
- https://www.musicbusinessworldwide.com/warner-music-group-settles-with-suno-strikes-first-of-its-kind-deal-with-ai-song-generator/
- https://www.musicbusinessworldwide.com/suno-confirms-v6-model-was-trained-on-creations-from-users-as-it-blasts-latest-sony-and-universal-lawsuit/
- https://www.latimes.com/entertainment-arts/business/story/2025-11-25/warner-music-group-suno-ai-lawsuit-settlement
- https://www.hollywoodreporter.com/music/music-industry-news/umg-sony-music-file-second-lawsuit-against-suno-1236705369/
- https://variety.com/2026/music/news/sony-music-universal-music-sue-suno-label-backed-model-1236866921/
- https://www.digitalmusicnews.com/2026/09/18/universal-music-suno-lawsuit-second/
- https://musically.com/2026/10/02/suno-is-far-beyond-2m-subscribers-and-300m-of-annual-revenue/
- https://www.theverge.com/ai-artificial-intelligence/1003925/suno-speech-ai-voice-feature-beta-availability
- https://artists.artyfile.com/blog/does-suno-own-your-music-terms-of-service-2026
- https://undetectr.com/blog/best-ai-music-generators-2026
- https://undetectr.com/blog/suno-v6-muffled-vocals
- https://www.chartlex.com/blog/marketing/suno-vs-udio-2026
- https://www.tldl.io/blog/suno-vs-udio-comparison
- https://www.musicwave.ai/blog/suno-vs-mureka
- https://suno.bi/en/blog/stable-audio-3-vs-suno-licensed-ai-music-comparison-2026
- https://help.udio.com/en/articles/12683565-changes-associated-with-the-universal-music-group-umg-partnership
- https://www.universalmusic.com/universal-music-group-and-udio-announce-udios-first-strategic-agreements-for-new-licensed-ai-music-creation-platform/
- https://www.reuters.com/legal/litigation/warner-music-settles-with-ai-firm-udio-plans-joint-platform-2025-11-19/
- https://acltracks.com/2026/09/adrian-cole/suno-says-v6-is-better-some-creators-say-it-sounds-worse/
- https://www.gearnews.com/suno-v6-problems-tech/
- https://hookgenius.app/learn/suno-character-limits/
- https://hookgenius.app/learn/fix-suno-pronunciation/
- https://hookgenius.app/learn/fix-suno-repetition/
- https://hookgenius.app/learn/fix-suno-wrong-genre/
- https://songsmith.studio/blog/suno-song-endings-cheat-sheet
- https://songsmith.studio/blog/five-common-suno-mistakes
- https://jackrighteous.com/blogs/guides-using-suno-ai-music-creation/suno-v6-skipping-repeating-changing-lyrics-long-song-fix
- https://www.reddit.com/r/SunoAI/comments/1mym1dm/ (meta-tag guide)
- https://www.reddit.com/r/SunoAI/comments/1he744i/ (meta megathread)
- https://www.reddit.com/r/SunoAI/comments/1l6pde9/ (tips of the week, CuznJay)
- https://www.reddit.com/r/SunoAI/comments/1hz944v/ (consistency guide, MR1933)
- https://www.reddit.com/r/SunoAI/comments/1w86hwj/ (dirty tricks #19, weirdness table)
- https://www.reddit.com/r/SunoAI/comments/1tvsu6u/ (controlled v5.5 prompt tests)
- https://www.reddit.com/r/SunoAI/comments/1bruise/ (seed reuse)
- https://www.reddit.com/r/SunoAI/comments/1ug99du/ (hum to instrumental trick)
- https://www.reddit.com/r/SunoAI/comments/1p6gx2x/ (unwanted vocal gender)
- https://aitoolsguidebook.com/en/articles/suno-style-descriptors-ignored/
