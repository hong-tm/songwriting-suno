# Changelog — songwriting-suno

Facts in this skill are **dated**. Newest entry first, one entry per update
session. Format: date — label; **Touched:** files; **Facts changed:** what and how
verified; **Sources:** URLs; **Freshness:** which registry entries were re-dated.

See `references/50-self-update.md` for the full update protocol.

---

## 2026-10-08 — craft gate + spec sheet, and companion-library routing

- **Touched:** `references/70-craft-gate-and-spec.md` (new),
  `references/00-index.md`, `SKILL.md`, `assets/freshness.json`,
  `evals/evals.json`, `README.md`
- **Facts changed:** none about Suno — this adds craft method + routing.
  - Added `references/70-craft-gate-and-spec.md`: the five-question
    pre-writing gate + stranger test, the LYR-SPEC/ARR-SPEC spec sheet,
    the AI-tell audit, and the routing table to the companion libraries.
  - Wired in the two MIT companion libraries by `jtydhr88`
    (`lw-*` = lyric, `mc-*` = composition): **12 kept active** in
    `~/.agents/skills/` (auto-trigger) and **35 parked** in
    `~/.agents/skills-library/` (read by path, zero always-on cost).
  - This bundle stays the quick Suno pipeline; deep craft is delegated to the
    companion libraries rather than duplicated.
- **Sources:** https://github.com/jtydhr88/lyric-writing-skills ,
  https://github.com/jtydhr88/music-composition-skills
- **Freshness:** `references/70-craft-gate-and-spec.md` registered (low,
  2026-10-08)

## 2026-10-07 — knowledge base: offline imagery, plausibility, retrieval & variation

- **Touched:** `references/60-knowledge-and-retrieval.md` (new),
  `assets/imagery-lexicon.json` (new index), `assets/imagery/*.json` (16 new theme
  files), `assets/plausibility-checks.md` (new), `assets/power-words.json` (new),
  `references/04-lyric-craft.md` (evidence-enriched), `references/00-index.md`,
  `SKILL.md`, `assets/freshness.json`, `evals/evals.json`, `README.md`,
  `install.sh`, `.gitignore` (packaging)
- **Facts changed:** none about Suno — this is offline knowledge + packaging.
  - Added an **offline imagery bank**: an index plus 16 per-theme files so an
    agent reads ~600 tokens (one theme) instead of ~15k (the whole bank).
  - Added `assets/plausibility-checks.md`, a pre-ship reality audit (seasons,
    light/era, geography, units, body physics, timeline/POV, cultural etiquette).
  - Added `references/60-knowledge-and-retrieval.md`: offline-first vs online
    retrieval rules, the plausibility gate, the anti-sameness/variation discipline
    with a ledger, an operational quality rubric, token discipline, and an honest
    statement of the skill's ceiling.
- **Sources:** n/a — offline, self-authored knowledge and packaging
- **Freshness:** `references/60-knowledge-and-retrieval.md`,
  `assets/imagery-lexicon.json`, `assets/plausibility-checks.md` registered (low,
  2026-10-07)

## 2026-10-07 — tooling: source checks, self-test, lyric lint, worked examples

- **Touched:** `scripts/source_check.py` (new), `scripts/check_freshness.py`,
  `scripts/selftest.py` (new), `scripts/lyric_lint.py` (new),
  `scripts/tests/test_check_freshness.py`, `scripts/tests/test_lyric_lint.py` (new),
  `references/07-worked-examples.md` (new), `references/04-lyric-craft.md`,
  `references/00-index.md`, `SKILL.md`, `assets/freshness.json`, `evals/evals.json`
- **Facts changed:**
  - Fixed 6 garbled `sources` URLs in the `40-learn-with-me.md` registry entry
    (the prose Sources had been de-concatenated, the registry rows had not) and
    2 ellipsis placeholders in `50-self-update.md`; the registry now parses clean
    under `check_freshness.py --check-coverage`
  - Added `--check-sources` (implied by `--check-coverage`) plus helper module
    `scripts/source_check.py`, so a broken source URL now fails the check (exit 1)
  - Added `scripts/selftest.py`: one cwd-independent command running script help
    checks, unit tests, freshness coverage, and lyric-tool fixtures
  - Added `scripts/lyric_lint.py` (+ 25 tests): approximate rhyme scheme,
    near-rhyme, repetition, line-spread, and built-in cliché detection
  - Added `references/07-worked-examples.md`: two verified end-to-end BUILD
    deliverables (English acoustic ballad; Mandarin + English city-pop)
  - Fixed `selftest.py`'s meter fixture (`--expect 5,6`, not `5,5`)
- **Sources:** n/a — tooling and self-authored examples; no external Suno facts changed
- **Freshness:** `references/07-worked-examples.md` registered (low, 2026-10-07);
  all other entries unchanged at `last_verified: 2026-10-07`

## 2026-10-07 — extension: LEARN + UPDATE modes

- **Touched:** `SKILL.md`, `references/00-index.md`, `references/40-learn-with-me.md`,
  `references/50-self-update.md`, `assets/learner-profile.md`,
  `assets/freshness.json`, `scripts/check_freshness.py`,
  `scripts/tests/test_check_freshness.py`, `evals/evals.json`
- **Facts changed:** none of the Suno facts were corrected — this entry adds
  capability, not corrected facts:
  - Added **LEARN mode** (teaching, Socratic dialogue, line-by-line co-writing,
    critique, exercise bank, level assessment) → `references/40-learn-with-me.md`
  - Added **UPDATE mode** (three triggers, 7-step re-verify workflow, staleness
    thresholds, changelog discipline) → `references/50-self-update.md`
  - Added the freshness registry `assets/freshness.json` + checker
    `scripts/check_freshness.py` (exit 0 fresh / 1 stale / 2 registry error)
  - Learner profile stored OUTSIDE the bundle at
    `~/.agents/learner-profiles/songwriting-suno.md`
- **Sources:** https://agentskills.io/ , https://code.claude.com/docs/en/skills
- **Freshness:** all registry entries set to `last_verified: 2026-10-07`

## 2026-10-07 — initial build (baseline)

- **Touched:** initial bundle — `SKILL.md`, `references/01`–`06`, `10`–`13`,
  `20`, `30`, `00-index.md`, `scripts/*`, `assets/*`, `evals/evals.json`
- **Facts changed:** initial compilation of songwriting craft + Suno mechanics +
  multilingual songwriting knowledge (each reference carries its own `## Sources`)
- **Sources:** see each reference's `## Sources`
- **Freshness:** registry seeded; `last_verified: 2026-10-07` for every entry
