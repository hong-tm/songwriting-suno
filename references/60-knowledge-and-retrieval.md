# 60 — Knowledge, Retrieval, and Freshness of Ideas

Three jobs: (1) keep lyrics **sane** (plausible, not weird); (2) keep them
**fresh** (not the same scaffold every time); (3) do both while spending as few
**tokens** as possible. Read this before writing a lyric that leans on facts,
culture, or concrete detail — and whenever output starts to feel samey.

---

## 1. Offline-first: the bundled knowledge base (no network)

Default to what is already here. It is instant and free:

| Asset | Use it for | Read cost |
|---|---|---|
| `assets/imagery-lexicon.json` | **Index** of the imagery bank — theme → file | ~250 tok |
| `assets/imagery/<theme>.json` | Concrete sensory material for **one** theme (rain, night, city, home, leaving-farewell, first-love, heartbreak, wedding, childhood, road-journey, sea-coast, winter, summer, morning, drinking-bar, work) | ~600 tok |
| `assets/plausibility-checks.md` | Pre-ship reality audit (seasons, light, geography, era, culture, POV) | ~2k tok |
| `assets/power-words.json` | Concrete swaps for generic/clichéd language (power verbs, sensory words, blacklists) | ~1k tok |
| `assets/persona-presets.json` | Genre/persona starting points | small |
| `references/04`, `06` | Object writing, show-don't-tell, subtext | on demand |

**Token rule:** read the **index**, then **one theme file** — never the whole
bank. `jq '.sight' assets/imagery/rain.json` is even cheaper than reading the file.

---

## 2. When to go online (and when not to)

Go online **only** for things the offline KB cannot know:

- a **real** place, brand, event, person, product, or statistic the lyric leans on;
- **current** slang, a recent release, or a dated cultural moment;
- a cultural/religious custom you are unsure about;
- verifying a load-bearing claim before it ships.

Do **not** search for: generic imagery, emotions, rhyme, structure, or prosody —
those are covered offline. Search is expensive (network + tokens) and returns
volatile text; treat it as a last resort for *facts*, not for *inspiration you
already have material for*.

Tools: the `firecrawl-*` skills, `librarian`, or `webfetch`. Rules:

- Prefer primary sources; cite the URL.
- If a claim cannot be verified, **cut it or make it vague** — never assert it as fact.
- Never fabricate a source, quote, or statistic.
- Cache-friendly: if you looked something up once and it is stable, note it in the
  learner profile rather than re-searching next session.

---

## 3. The plausibility gate

Before shipping, scan the lyric against `assets/plausibility-checks.md`:
hemisphere/seasons, light sources and era, sun/moon/tide, geography and bearings,
units and currency, body physics, timeline/POV consistency, and cultural
etiquette (Chinese and Malay contexts included). If a real-world detail is
**load-bearing and unverified**, verify it or remove it. Prefer universal imagery
unless a verified specific earns its place.

---

## 4. Anti-sameness: a variation discipline

**The failure mode:** every song comes out with the same skeleton — same rhyme
scheme, same image domain, same POV, same tempo, same chorus shape. Competent but
monotonous, and it reads as "AI".

**Rule: vary at least three axes versus your last song.** Axes to vary:

- structure (e.g. verse-chorus vs AABA vs through-composed)
- rhyme scheme (ABAB / AABB / ABCB / monorhyme / slant-only)
- point of view & tense (I / you / we / third person; past / present)
- image domain (use a **different** lexicon theme: if last song lived in `rain`,
  this one lives in `work` or `sea-coast`)
- tempo & feel (ballad vs groove; straight vs swung)
- hook position (first line vs last line vs title-drop)
- line-length profile (long-lined vs clipped)

**Forcing functions:** open the imagery index, pick a theme you have *not* used
recently; choose an uncommon rhyme scheme on purpose; move the hook. Keep a short
**variation ledger** (below) so you can see what you have already spent.

```
## Variation ledger (recent songs)
| date | title | structure | rhyme | POV/tense | image theme | tempo | hook pos |
|------|-------|-----------|-------|-----------|-------------|-------|----------|
|      |       |           |       |           |             |       |          |
```

Within one song, also avoid internal sameness: verse 2 must **advance** the story,
not re-tell verse 1; contrast sections (energy, register, line length).

---

## 5. What "good" means — an operational rubric

Before shipping, the lyric should pass:

- **Hook:** one memorable phrase, simplest wording in the song, repeated.
- **Concrete:** several concrete images; few or no emotion labels (show, don't tell).
- **Prosody:** stressed syllables land on strong beats; meter counted with
  `scripts/syllable_meter.py`.
- **Fresh:** no built-in clichés (`scripts/lyric_lint.py`); at least one image that
  is not generic.
- **Varied:** differs from recent work on **>= 3 axes** (§4).
- **Plausible:** passes the reality audit (§3).
- **Singable:** lines you can actually say at tempo; end chorus lines on open vowels.

---

## 6. Token discipline (spend little, get more)

- Read **one** reference or **one** theme, not the whole bundle.
- **Run scripts** instead of reading them — deterministic, cheap, no token cost for output you don't need.
- Do not re-paste context that a bundled file already holds; point to the file.
- Keep `SKILL.md` a thin router; push detail into files read only when needed.
- Keep the prompt prefix stable (tool/system/message order) so provider KV caching
  can hit — see `references/50-self-update.md` for the freshness side.

---

## 7. Honest ceiling (what this cannot do)

This skill encodes music as **language**: structure, prosody, harmony vocabulary,
production terms, and craft rules. It **cannot hear**. It cannot audition a Suno
render, judge groove, or certify that a melody is good. It raises the floor and
removes obvious failure modes (cliché, nonsense, unsingable meter, monotony); the
ceiling is set by the generator model and by a **human ear in the loop**. Good
songs are *iterated and listened to*, not declared good on paper.

## Sources

Internal guidance for this bundle; no external URLs. Concrete material lives in
`assets/imagery/`; the reality audit is `assets/plausibility-checks.md`. Craft
references: `04-lyric-craft.md`, `06-meaning-subtext.md`.
