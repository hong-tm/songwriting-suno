# Songwriting + Suno — Reference Index

Annotated index of every reference file in this skill. Read the file that
matches the task; do not read them all at once.

## Craft

| File | Covers | Read when |
|---|---|---|
| `01-song-structure.md` | Section types (intro/verse/pre-chorus/chorus/bridge/outro), section orders and templates, bar counts, how structure creates tension and payoff. | Designing or repairing a song's form. |
| `02-rhythm-groove.md` | Tempo/BPM by genre, time signatures, meter, groove, swing, syncopation, rhythmic devices. | Choosing tempo/feel or fixing a limp groove. |
| `03-melody-harmony.md` | Melodic contour, motif, hook writing, range, tension/release, chord progressions, cadences, reharmonization. | Writing a melody, hook, or chord progression. |
| `04-lyric-craft.md` | Prosody, stressed syllables, rhyme schemes, syllable density, imagery, show-don't-tell, cliché traps. | Writing or repairing lyrics. |
| `05-mood-production.md` | Mood/genre taxonomy, instrumentation, timbre vocabulary, arrangement, production techniques, valence mapping. | Setting a song's sound and emotional colour. |
| `06-meaning-subtext.md` | Theme, subtext, implication, ambiguity, symbolism, motif, double meaning, literary devices. | Adding depth/meaning; making lyrics say more with less. |

## Examples

| File | Covers | Read when |
|---|---|---|
| `07-worked-examples.md` | Two complete BUILD-mode deliverables end to end — an English acoustic wedding ballad and a Mandarin + English city-pop song — each with a real Style prompt, tagged sheet, verified meter and structure output, an iteration log, and meaning/subtext. | You want a finished few-shot model of a song artifact. |

## Suno / AI music

| File | Covers | Read when |
|---|---|---|
| `10-suno-mechanics.md` | How Suno works: modes, model versions, field limits, features, credits/pricing, copyright/ownership. | You need to know what Suno can actually do. |
| `11-suno-prompting.md` | Style-prompt formula, style-tag vocabulary, meta-tags ([Verse], [Chorus]…), negative prompting, copy-paste recipes. | Building or improving a Suno prompt. |
| `12-suno-workflows.md` | Advanced workflows: extend, cover, remix, personas, stem separation; competitor tools (Udio, Riffusion, etc.). | Going beyond one-shot generation. |
| `13-vocal-control.md` | Steering vocal gender, range, delivery, ad-libs, harmonies, stacking; lyric-level control of the voice. | Controlling how the AI sings. |

## Meta

| File | Covers | Read when |
|---|---|---|
| `20-tools-and-projects.md` | Real GitHub projects, Suno API clients, MIR/audio libraries, datasets, awesome-lists, alternatives. | You want code/tools to build with. |
| `30-multilingual.md` | How songwriting differs by language (English, Chinese, Cantonese, Japanese, Korean, Malay/Indonesian, Spanish, …): tone–melody matching, syllable vs mora, rhyme conventions, structure norms, pitfalls, and Suno's handling of non-English. | Writing lyrics in any non-English language. |

## Learning

| File | Covers | Read when |
|---|---|---|
| `40-learn-with-me.md` | LEARN mode: six sub-modes (EXPLAIN / SOCRATIC / CO-WRITE / CRITIQUE / EXERCISE / ASSESS), the 3×3 level rubric, an exercise bank with hidden answers, feedback protocol, and the durable learner-profile protocol. | The user wants to learn, co-write, be critiqued, or be assessed. |

## Knowledge & retrieval

| File | Covers | Read when |
|---|---|---|
| `60-knowledge-and-retrieval.md` | Offline-first knowledge base vs online retrieval (when/what/how, citation and no-fabrication rules), the plausibility gate, the anti-sameness/variation discipline and ledger, an operational "what good means" rubric, token discipline, and the honest ceiling. | Before writing anything fact- or culture-laden, when output is getting samey, or when deciding whether to search. |

## Skill maintenance

| File | Covers | Read when |
|---|---|---|
| `50-self-update.md` | UPDATE mode: three triggers, the 7-step re-verify workflow, staleness thresholds, registry rules, changelog format, and the optional host-hook appendix. | Refreshing the skill's facts or checking freshness. |
| `CHANGELOG.md` (skill root) | Log of factual updates to this skill, newest-first. | Seeing what changed and when. |

## Assets & scripts

| Path | Purpose |
|---|---|
| `assets/song-template.md` | Standard output skeleton for a finished song. |
| `assets/persona-presets.json` | Reusable style/persona presets. |
| `assets/learner-profile.md` | Template for the LEARN-mode learner profile (copied to `~/.agents/learner-profiles/songwriting-suno.md`). |
| `assets/freshness.json` | Freshness registry: one entry per fact-bearing file (tier, last_verified, sources). |
| `assets/imagery-lexicon.json` | Index of the offline imagery bank (theme → file). Read one theme, not all. |
| `assets/imagery/<theme>.json` | Concrete sensory material for one theme (16 themes: rain, night, city, home, leaving-farewell, first-love, heartbreak, wedding, childhood, road-journey, sea-coast, winter, summer, morning, drinking-bar, work). |
| `assets/plausibility-checks.md` | Pre-ship reality audit: seasons/hemisphere, light/era, geography, units, body physics, timeline/POV, cultural etiquette. |
| `assets/power-words.json` | Concrete replacements for generic language: power verbs, sensory adjectives, polysensate words, generic + dead-metaphor blacklists, cliché rhyme pairs. |
| `scripts/format_style_prompt.py` | Assemble a Suno style + exclude prompt from flags. |
| `scripts/syllable_meter.py` | Count syllables per line; check against a target meter. |
| `scripts/lyric_lint.py` | Approximate rhyme scheme, near-rhyme, repetition, line-spread, and cliché lint. |
| `scripts/validate_structure.py` | Validate section tags and basic song shape. |
| `scripts/check_freshness.py` | Report per-file staleness from `assets/freshness.json` (exit 0 fresh / 1 stale / 2 registry problem); `--check-sources` flags broken source URLs. |
| `scripts/selftest.py` | One command that runs the whole bundle's self-checks (must exit 0). |
| `scripts/source_check.py` | Source-URL validation helper imported by `check_freshness.py` (not run directly). |
| `evals/evals.json` | Sample prompts to test trigger + output quality. |

## Provenance

Compiled 2026-10-07 from a multi-agent web research pass. Each reference file
keeps its own `## Sources`. Suno-specific facts (limits, pricing, features)
change frequently — treat them as dated and re-verify on `help.suno.com`.

Extended 2026-10-07 with LEARN mode (`40-learn-with-me.md`), UPDATE mode
(`50-self-update.md`), the freshness registry (`assets/freshness.json`) and its
checker (`scripts/check_freshness.py`). See `CHANGELOG.md`.

Extended again 2026-10-07 with the source-URL validator (`scripts/source_check.py`),
the one-command self-test (`scripts/selftest.py`), the lyric linter
(`scripts/lyric_lint.py`), and two worked examples (`07-worked-examples.md`).

Extended once more 2026-10-07 with an offline knowledge base
(`assets/imagery-lexicon.json` + `assets/imagery/` + `assets/plausibility-checks.md`)
and `60-knowledge-and-retrieval.md` (offline-vs-online retrieval, plausibility
gate, anti-sameness discipline, token discipline).
