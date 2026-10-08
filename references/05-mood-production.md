# 05 · Mood, Vibe, Timbre & Production Aesthetics

Reference for setting a song's emotional color and sonic identity. Pair with the Suno docs (10-13) for prompting.

## Quick rules / TL;DR

- Emotion is encoded by six cues in order of power: **mode > tempo > register > dynamics > articulation > timbre** (Eerola 2013). They act additively and explain 77-89% of listener ratings.
- Bright sounds read as happy, dull as sad, sharp as angry, soft as fearful/tender. Harmonic brightness correlates with valence at r = -0.74.
- Minor keys are powerful but not absolute: fast minor themes don't sound sad (Mozart 40). Tempo and dynamics can override mode.
- Instruments are "emotionally typecast" by acoustic capacity: something capable only of high, loud, quick notes (banjo, xylophone) physically can't carry sadness.
- Dry = intimate/close; reverb = farther, bigger, dreamier. Louder = closer; darker (low-passed) = farther.
- Lo-fi = dust, wobble, detune, band-limiting; hi-fi = clean, full range, pristine. Analog = tape/tube saturation warmth; digital = transparency.
- Match predicted listener emotion against the cue table first, then decorate with genre and production adjectives; contradictions average into mush.

## 1. The science: cue → emotion

The strongest empirical base is Eerola, Friberg & Bresin (2013), isolating six cues across happy/sad/peaceful/scary, plus Micallef Grimaud & Eerola (2022) with seven cues (adds pitch, brightness, instrumentation) across seven emotions (sadness, joy, calmness, anger, fear, power, surprise). Dynamics and instrumentation carry the most variance; cues behaved similarly in 32 of 49 cue-emotion combos.

Concrete cue levels actually manipulated in the 2013 study:

| Cue | Levels used | Note |
|---|---|---|
| Mode | major vs minor | Single strongest cue |
| Tempo | 1.2 / 2 / 2.8 / 4.4 / 6 notes per second | NPS stays stable across time signatures |
| Dynamics | -10 to +10 dB (pp → ff) | Also changes timbre |
| Articulation | 1.0 / 0.75 / 0.5 / 0.25 (legato → staccatissimo) | |
| Register | MIDI 53, 59, 65, 71, 77, 83 (F3 → B5) | |
| Timbre | flute (bright) / horn / trumpet (brightest) | Spectral energy < 1500 Hz, r = -0.74 with valence |

Characteristic performance values per intended emotion (Bresin & Friberg 2000, the precursor study):

| Intended emotion | Tempo | Level | Articulation | Note timing | Ending |
|---|---|---|---|---|---|
| Anger | very rapid | +8 dB loud | non-legato | long/short contrast increased | abrupt |
| Happiness | fast | +3 dB | airy | IOI shortened 20% | none/short |
| Sadness | slow | -6 dB soft | legato | IOI lengthened 30% | final ritardando |
| Tenderness | slow | -6 dB soft | legato | contrast diminished, +30% | final ritardando |
| Fear | irregular | -6 dB low | staccato | huge deviations, IOI +80% | sometimes accelerates |

Caveat from the same listening tests: anger identifies at 91%, happiness 63-97%, sadness 59-69%, but **fear only 44-47%, regularly confused with tenderness** (and tenderness at 9% on one piece, confused with sad). Fear and tenderness share the slow/soft/legato space and split mainly on articulation and regularity. Cue combos are probabilistic, not diagnostic.

## 2. Master mood → parameters table

| Target mood | Mode / harmony | Tempo feel | Dynamics / register | Instruments | Vocal style |
|---|---|---|---|---|---|
| Happy / joyful | Major, I-IV-V | fast (120-170) | loud, high | bright leads (flute/trumpet-like), ukulele, bright synths | belting, bright twang, staccato |
| Sad / melancholic | Minor, m7/m9/m11 | slow (60-90) | soft, low, legato | felt piano, cello/strings, nylon guitar, mellow pad | breathy, cry/sob, sparse vibrato |
| Peaceful / calm | Major, maj7/sus2/add9 | slow-moderate | soft, mid | pads, warm Rhodes, acoustic guitar, flute | breathy, head voice, no belt |
| Scary / tense | minor + chromatic/atonal, tritone | unstable or very fast tremolo | low building to loud | dissonant strings, detuned synths, sub-drones | whisper/distortion extremes |
| Angry / aggressive | minor, diminished, power chords | fast (140+) | loud, mid-high | distorted guitar, hard drums, brass stabs | grit/rasp, overdrive, shout |
| Romantic / tender | major with maj7 / m7 mixture | slow (60-80) | soft, mid | strings, electric piano, lush pad | breathy, cry, vibrato, close mic |
| Nostalgic / bittersweet | major with borrowed bVII; Dorian | mid (80-110) | moderate | Rhodes, tape-saturated keys, lo-fi textures | breathy + gentle melisma |
| Dreamy / ethereal | Lydian, maj9, sus2 | slow, often beatless | soft, high shimmer | washed reverb pads | falsetto, breathy, stacked layers |
| Triumphant / anthemic | major, I-V-vi-IV | mid-fast (110-130) | loud, wide | supersaw leads, big drums, choir | belting, group shouts |
| Intimate / confessional | simple major or minor | slow | very soft, close | one acoustic guitar or piano | whisper, breathy, speak-singing |
| Playful / quirky | major, added 6/9 | fast | bouncy staccato | plucky synths, pizzicato, toy instruments | twang, glottal-stop jauntiness |

Cross-checks: major = "gay and lively" vs minor = "sad and languid" (Zarlino 1558, via Bowling 2013); major-key pieces run ~a major second higher and 29% faster than minor (Poon & Schutz, via Eerola 2017); Bowling's vocal-prosody theory says mode-emotion links aren't arbitrary, they mirror speech prosody of affective states.

## 3. Vocal qualities → what they convey

Registers:

| Register | Character | Conveys | Examples |
|---|---|---|---|
| Chest voice | rich, warm, thick | groundedness, authority, intimacy | Johnny Cash, Adele verses, Amy Winehouse |
| Head voice | lighter but resonant, clear ring | uplift, purity, projection | Freddie Mercury, Whitney Houston |
| Mixed voice | chest power + head range | "money notes," power without strain | Beyoncé, Ariana Grande, Chris Cornell |
| Falsetto | breathy, airy, flute-like, hollow | detachment, vulnerability, ethereality | Bee Gees, Jeff Buckley, Thom Yorke, Prince |
| Vocal fry | creaky, lowest | casualness, menace, stylistic onset | Billie Eilish, Ke$ha |
| Whistle | piercing extreme highs | virtuosic thrill | Mariah Carey, Minnie Riperton |

Techniques:

| Technique | Character | Conveys | Examples |
|---|---|---|---|
| Belting | loud, bright, controlled shout | emotional peak, triumph | Whitney, Celine Dion, Idina Menzel |
| Twang | bright, nasal-but-good | cutting through a band without strain | Steven Tyler, Dolly Parton, AC/DC |
| Breathy | air leak, soft, ASMR | intimacy, vulnerability, dreaminess | Billie Eilish, Norah Jones, Sade, Lana Del Rey |
| Grit / rasp | gravelly, smoky, raw | emotional intensity, rock texture | Rod Stewart, Janis Joplin, Adele |
| Distortion / overdrive | false-fold buzz, aggressive | rage, catharsis | Chester Bennington, James Hetfield |
| Growl | short bark at note onset | attitude, punch | Christina Aguilera, James Brown, Tina Turner |
| Cry / sob | tilted larynx, "lump in throat" | pleading, heartbreak | Sam Smith, Sinéad O'Connor |
| Vibrato | pitch oscillation ~5-7 Hz | warmth, aliveness, maturity | Whitney, Pavarotti |
| Runs / melisma | rapid cascading notes | virtuosity, gospel/R&B soulfulness | Mariah, Stevie Wonder |
| Pitch bend | slide/scoop/fall | bluesy, human | B.B. King, Ray Charles |
| Glottal stop | tiny click before a note | emphasis, attitude | Adele's signature |
| Messa di voce | one-breath crescendo→decrescendo | supreme control, drama | Pavarotti, Jeff Buckley |
| Dynamic contrast | whisper verse → belt chorus | the emotional "explosion" | Nirvana, Radiohead, Hozier |

Modern pop/R&B production defaults to stacked doubles, harmonies, ad-libs around the lead; rap delivery is characteristically dry, folk vocals wetter (TA note: belting done as "pure chest pushed high" carries genuine vocal-health risk; NCVS also documents pressed, strained, wobble, ventricular/"Louis Armstring" voice as affect-bearing categories).

## 4. Instrumentation as mood signifier

| Instrument / texture | Timbre | Typical mood use |
|---|---|---|
| Soft/felt piano | warm, intimate, decaying | sadness, intimacy, nostalgia |
| Bright grand piano | percussive, wide | cinematic drama, classic pop |
| Rhodes / Wurlitzer | warm, bell-like, analog | soul, R&B, neo-soul, nostalgia |
| Acoustic guitar (fingerpicked) | woody, intimate | folk, singer-songwriter |
| Clean single-coil / 12-string | jangly, shimmering | indie/jangle, nostalgia |
| Distorted electric | aggressive, dense | rock, metal, power |
| Strings / cello | lush, cinematic, weeping | sadness, romance, tension |
| Synth pad | ethereal, floating, wide | dreamy, ambient, cinematic |
| Supersaw lead | anthemic, huge | EDM drops, triumph |
| 808 sub bass | deep, physical | trap power, modernity |
| Synth bass / Moog | warm, filtered | disco, R&B, funk |
| Hammond organ | soulful, gospel | soul, rock |
| Horns / brass | bright, declarative | triumph, funk, retro pop |
| Flute | breathy bright-pure | peacefulness, innocence |
| Pedal steel / fiddle / banjo | twang | country authenticity, nostalgia |
| Marimba | mellow, resonant | warmth (vs xylophone) |
| Lo-fi textures | dusty, nostalgic | bedroom pop, lo-fi |

The key rule behind these stereotypes: sadness judgments track an instrument's capacity to play **low, quiet, and with small pitch movements** (Huron 2014, Schutz 2008). Banjo and xylophone are physically ill-suited to sadness; marimba can sustain it. Choose instruments whose constraints permit the cue direction you want.

Timbre physics you can actually manipulate: positive valence follows lower spectral slopes, stronger partials, sharper attack + earlier decay; energy arousal follows brightness/spectral centroid; tension follows brightness plus gentler attacks. So attack envelope and brightness are the real levers behind "warm/soft" vs "bright/punchy."

## 5. Production & arrangement vocabulary

### 5a. Space

| Tool | Effect on vibe | Key facts |
|---|---|---|
| Reverb | pushes element back; bigger = dreamier/farther | keep one long reverb per element; others short/dry |
| Plate | dense, shimmering | 80s records |
| Spring | drippy, wet | guitar amps, dub |
| Hall / chamber | huge, stadium/cathedral | small doses powerful, large = muddy |
| Convolution / IR | models real rooms | "sound of a space" ties to emotional memory |
| Delay | space without smearing | 1/8 and 1/4-note on pop/hip-hop vocals; tape delay = vintage/dub |

Front-back depth rules: louder = closer; darker = farther (low-pass 2-8 kHz); drier = closer; early reflections create depth. Small-club reverb feels warm/comforting, cathedral feels cool/airy.

### 5b. The five vibe axes

| Axis | Pole A | Pole B | Mechanism |
|---|---|---|---|
| Warm ↔ Bright | rounded, soft top, low-mid weight | presence, sparkle, air | EQ tilt + saturation |
| Lo-fi ↔ Hi-fi | dust, wobble, detune, band-limited | clean, full-range | vinyl crackle, bitcrush, tape compression, pitch drift |
| Analog ↔ Digital | tape/tube/console coloration | transparent, pristine | saturation, crosstalk, head bump |
| Dry ↔ Wet | in-your-ear intimate | spacious, distant | reverb/delay send level |
| Mono ↔ Wide | focused, punchy | expansive, immersive | panning, double-tracking, mid/side |

### 5c. Arrangement = emotional architecture

- EDM builds on energy (build → drop → breakdown); pop on verse/pre-chorus/chorus tension-release; hip-hop hook-first.
- The breakdown paradox: removing elements (kick/bass) builds more tension than adding.
- Max Martin's recent hits front-load multiple short hooks before the first chorus (as late as 0:57-1:27).
- Dynamic contrast is the core device: quiet verse → loud chorus. "If everything is loud, nothing is loud."

## 6. Genre conventions

| Genre | Tempo | Mode / harmony | Signature sound | Rhythm / feel | Production | Vocal |
|---|---|---|---|---|---|---|
| Pop | 100-130 | major, I-V-vi-IV | synths, drum machine | four-on-floor / driving 8ths | polished, loud, arrangement economy | upfront, stacked + ad-libs |
| Rock / Indie | 80-180 (sweet 110-130) | Mixolydian bVII | double-tracked guitars, live drums | driving | room mics, DI→amp | belting, grit |
| Jangle pop | 100-145 | major | 12-string electric | 60s arpeggios | clean, shimmering, DIY | bright, light |
| Shoegaze / dream pop | 90-130 | modal | fuzz + reverb + chorus wall | washed | guitars drowned, vocals buried in mix | buried, ethereal |
| R&B / Soul | 60-130 (typ ~90) | ext. 7/9/11ths, chromatic voice leading | Rhodes, B3, clean guitar | swing 58%, snare 10-30 ms behind | warm, centered vocal, wide instruments | centerpiece, runs |
| Neo-soul | 65-100 | m9/maj9/m11, ii-V-I minor | Rhodes, upright bass | J Dilla "drunk" feel, unquantized | soft room reverb, lo-fi texture | expressive, melisma |
| Hip-hop / Trap | 60-100 (trap 130-150 half-time ≈ 70 feel) | modal minor | 808 sub, sampled chops, hi-hat rolls | half-time, boom-bap or trap rolls | sparse, sample-centric | dry rap, ad-libs |
| House | 118-130 | minor/modal | supersaw, drum machine | four-on-floor | sidechain pump, big builds/drops | vocal chops |
| Techno | 125-150 | minimal/modal | 909, TB-303 | hypnotic | dub reverb, distortion | mostly instrumental |
| Dubstep / DnB | 138-150 HT / 170-180 | minor | wobble or Reese bass | half-time / breakbeat | drops, sub-dominant | sparse chops, MC |
| Folk | 60-120 | diatonic | acoustic guitar, harmonica | loose, lyric-driven | natural, moderate reverb, wide dynamic | intimate, storytelling |
| Country | 70-160 | I/IV/V, Mixolydian bVII | Telecaster, pedal steel, fiddle, banjo | boom-chicka, train beat | warm, slapback echo, live room | front-and-center |
| Metal | 100-200 | minor/phrygian | down-tuned distorted guitars | double-kick | double-tracked + phase-aligned, gated | scream/growl |
| K-pop | 100-130 | EDM/R&B borrowings, bright even in minor | synths, dense percussion | 4-on-floor, reggaeton | hyper-produced, dense layers | group leads, stacked harmonies |
| City pop / J-pop | 90-120 | jazz/fusion: maj7, sus4, ii-V-I, tritone subs | Rhodes, poly synths, chorus guitar | laid-back Steely Dan grooves | glossy 80s sheen | smooth, melodic |
| Lo-fi hip-hop | 60-90 | jazzy VI-i-V7 with extensions | detuned keys, vinyl crackle, tape wobble | relaxed, space between drums | bitcrush, chorus; 1-3 min loops | instrumental |
| Ambient | none / buried | Lydian, Dorian, whole-tone, open | pads, drones, bells | beatless | attack 1-8 s, reverb RT60 4-15 s, -20 LUFS, 3 layers (sub/mid/shimmer) | wordless |

Genre-contract rule: a track reads as a genre if it hits at least 3 of 5 markers — tempo range, harmonic language, transient profile, arrangement density, vocal-production approach.

## 7. Mixing / mastering for vibe

Streaming targets: Spotify -14 LUFS (user-adjustable -19/-11), Apple Music -16, YouTube/Amazon/Tidal -14, Deezer -15, Pandora none. True peak: leave ≥ -1 dBTP for lossy, ≤ -0.3 dBTP for lossless.

- Loudness normalization killed the loudness war's reward: a crushed -6 LUFS master gets turned down anyway, minus the dynamics it lost. Target dynamics, not a number.
- Sidechain pump: kick ducks bass in the 40-120 Hz overlap; match release to tempo. Also used subtly as low-end housekeeping outside EDM.
- Saturation = analog warmth, harmonics, glue. EQ tilt is the fastest macro for dark/soft vs bright/airy, and low-pass filtering creates front/back depth.
- Dynamic range (LRA) is the vibe variable: wide range gives emotional peaks; over-compression sounds flat and fatiguing.
- Genre space conventions: rap vocals dry, folk vocals wetter, EDM loud/wide/sub-heavy, ambient around -20 LUFS, country mid-range intelligibility for earbuds and cars.

## 8. Describing a target vibe

The 5-question method: What does it feel like? How does it move? What sound palette? Where would you hear it? What makes it stand out?

| Category | Adjectives |
|---|---|
| Mood | dark, euphoric, tense, dreamy, warm, melancholic, triumphant, playful, aggressive, introspective, cinematic, ethereal, intimate, anthemic, nostalgic, bittersweet |
| Energy | relaxed, steady, driving, high-energy, explosive, restrained, urgent, laid-back, pumping, atmospheric |
| Texture | gritty, polished, lush, dry, spacious, dense, glossy, lo-fi, crisp, shimmering, airy, saturated |
| Motion | pulsing, rolling, swelling, marching, floating, cascading, chugging, bouncing, evolving |

Producer-glossary decoding: warm = rounded/vintage; analog = tape flavor; polished = radio-ready clean; lo-fi = hazy/dusty imperfection; gritty = rough edges kept; spacious = air and echo; dry = intimate, no echo; cavernous = reverb at eleven; punchy = rhythmic snap; tight = controlled, no flab; driving = relentless forward motion; gated drums = chopped 80s hits; deep/sub bass = chest-felt low end; layered = stacked thickness; shimmering = glittering top; airy = light breathy top.

Pair words into one coherent vision: `warm analog`, `punchy tight drums`, `dry intimate vocals`, `spacious dreamy synths`. Contradictory stacks (`polished lo-fi cavernous dry`) average into nothing. Note BPM sources conflict by era/subgenre (Ableton hip-hop 60-100 vs trap 130-150 half-time): report tempo as a feel, not a single correct number.

## How to apply this in Suno

- Anchor the mood in the main style prompt using two aligned adjective families, e.g. `melancholic slow ballad, felt piano, breathy female vocal, soft dynamics` — the vibes page of the Suno docs (reference 10) has prompt-slot syntax.
- Specify vocal character explicitly: `breathy whisper delivery`, `belting chorus`, `raspy baritone` — Suno responds to vocal adjectives better than to singer names.
- Use production texture words in the style prompt to shift sonics without changing mood: `tape saturation`, `vinyl crackle`, `gated drums`, `supersaw lead`, `sidechain pumping`.
- Keep one "space" descriptor at most (`dry and close` vs `cavernous hall reverb`); stacking space words fights itself.
- For a verse/chorus dynamic arc, note it in the lyric with `[Verse]` / `[Chorus]` tags plus a line in the style prompt like `quiet intimate verses exploding into a loud anthemic chorus`.
- Point Suno at a tempo *with the feel*, e.g. `80 BPM halftime trap` rather than bare `trap`.
- For genre authenticity, include the specific chord/harmony markers (`maj7 Rhodes, jazzy ii-V-I`) plus the general Suno note that genre + mood + instrumentation covers most of the sonic contract.
- Verify with the persona/style-reference feature against a reference track when a specific production sheen matters more than the mood itself.

## Sources

- Eerola, Friberg & Bresin 2013, cue study — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00487/full
- Micallef Grimaud & Eerola 2022 — https://pmc.ncbi.nlm.nih.gov/articles/PMC9803112/
- Bowling 2013, vocal basis of mode — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00464/full
- Affective qualities of instrument sounds — https://pmc.ncbi.nlm.nih.gov/articles/PMC5296353/
- Eerola & Schutz 2017, acoustic constraints — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.01402/full
- Bresin & Friberg 2000 characteristic values — https://continuum-hypothesis.com/music/FULLTEXT01.pdf
- Juslin & Laukka 2003 meta-analysis — https://brainmusic.org/EducationalActivitiesFolder/Juslin_emotion2003.pdf
- NCVS Voice Qualities — https://ncvs.org/tutorials/voice-qualities/
- Vocal register — https://en.wikipedia.org/wiki/vocal_register
- Belting — https://en.wikipedia.org/wiki/belting_(music)
- Jesper Ordrup Vocal Guide — https://jesperordrup.github.io/vocal-guide/llms-full.txt
- iZotope — Mixing for Atmosphere — https://www.izotope.com/community/blog/tips-mixing-for-atmosphere
- iZotope — Mix Depth — https://www.izotope.com/community/blog/what-is-mix-depth-how-to-create-front-back-space
- iZotope — Reverb on vocals — https://www.izotope.com/community/blog/essential-tips-for-using-reverb-on-vocals
- Attack Magazine — Delay & Reverb — https://www.attackmagazine.com/technique/tutorials/adding-atmosphere-with-delay-and-reverb/
- Attack Magazine — Ambient Techno Pads — https://www.attackmagazine.com/technique/synth-secrets/crafting-ambient-techno-pads/
- Waves — 4 Mix Tips to Create Emotion — https://www.waves.com/mix-tips-to-create-emotion-in-your-music
- Sound on Sound — Sympathetic Mixing — https://www.soundonsound.com/techniques/sympathetic-mixing-how-set-good-mix
- Universal Audio — Basics of Reverb — https://www.uaudio.com/blogs/ua/the-basics-of-reverb
- Native Instruments — Emotional melodies — https://blog.native-instruments.com/emotional-melodies/
- MasteringBox — Psychoacoustics — https://www.masteringbox.com/fr/learn/psychoacoustics-for-music-production
- Music Production Authority — genres — https://musicproductionauthority.com/music-production-genres-and-styles/
- Veena Studio — song structure by genre — https://www.veena.studio/blog/song-structure-by-genre
- Baby Audio — What is City Pop — https://babyaud.io/blog/what-is-city-pop
- UJAM — How to Make K-Pop — https://www.ujam.com/tutorials/how-to-make-k-pop/
- Native Instruments — Lo-fi hip hop — https://blog.native-instruments.com/lo-fi-hip-hop-beats/
- BeatKey — Indie Rock — https://beatkey.app/how-to-make-indie-rock-music
- BeatKey — Ambient — https://beatkey.app/how-to-make-ambient-music
- BeatKey — Neo Soul — https://beatkey.app/how-to-make-neo-soul-music
- Audiotool — R&B Lexicon — https://www.audiotool.com/genres/lexicon/rnb
- Audiotool — Country Lexicon — https://www.audiotool.com/genres/lexicon/country
- Jangle pop — https://en.wikipedia.org/wiki/jangle_pop
- Sound on Sound — Making Modern Metal Pt 3 — https://www.soundonsound.com/techniques/making-modern-metal-part-3
- MusicProductionWiki — EDM tension & drops — https://musicproductionwiki.com/articles/how-to-build-tension-and-drops-in-edm
- Max Martin hook arrangement — https://www.hitsongsdeconstructed.com/hsd_wire/max-martins-new-take-on-hook-arrangement/
- Mixgraph — BPM for every genre — https://www.mixgraph.io/bpm-for
- Ableton Learning Music — Tempo & genre — https://learningmusic.ableton.com/make-beats/tempo-and-genre.html
- iZotope — Mastering for streaming — https://shopify.izotope.com/community/blog/mastering-for-streaming-platforms
- gearnews — Loudness War 2026 — https://www.gearnews.com/loudness-war-studio/
- MasteringBox — Loudness & Dynamics — https://www.masteringbox.com/se/learn/dynamic-range-and-loudness
- Maxim Schunk — Sidechain in EDM — https://maximschunk.com/news/sidechain-compression-edm-guide
- Your Ghost Production — Describe music in words — https://yourghostproduction.com/content/how-do-you-describe-music-in-words
- tinystudio — Production words decoded — https://tinystudio.fm/guides/production-words-decoded/
- Berklee — Harmonic progressions — https://online.berklee.edu/takenote/harmonic-progressions-for-songwriters/
- Berklee — Searching for a song's emotional arc — https://www.berklee.edu/berklee-now/news/searching-for-a-song-s-emotional-arc
