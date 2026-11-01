# Changelog — songwriting-suno

Facts in this skill are **dated**. Newest entry first, one entry per update
session. Format: date — label; **Touched:** files; **Facts changed:** what and how
verified; **Sources:** URLs; **Freshness:** which registry entries were re-dated.

See `references/50-self-update.md` for the full update protocol.

---

## 2026-10-31 — mass-ulw optimization pass: fact refresh, verification layer, packaging

- **Touched:** `references/10-suno-mechanics.md`, `references/11-suno-prompting.md`, `references/12-suno-workflows.md`, `references/20-tools-and-projects.md` (fact refresh), `references/13-vocal-control.md` (verified, unchanged), `SKILL.md`, `references/00-index.md`, `references/50-self-update.md`, `references/70-craft-gate-and-spec.md`, `assets/freshness.json`, `scripts/selftest.py`, `scripts/check_evals.py` (new), `scripts/tests/test_check_evals.py` (new), `scripts/tests/test_validate_structure.py` (new), `scripts/tests/test_syllable_meter.py` (new), `README.md`, `CONTRIBUTING.md`, `install.sh`, `.github/workflows/ci.yml`, `.gitignore`, this changelog (count fix below)
- **Facts changed:**
  - 10 (3 spots): parentheses rule corrected to the v6 behavior — a director note like `(whispered)` is performed as vocal direction, NOT sung; inline echoes like `(hey!)` stay backing vocals [COMMUNITY, v6 field test 2026-10-21; pre-v6 reports split]. Removes the contradiction with 13 §2.
  - 10: stems/Replace-Section/Custom-Models citations re-verified against live help articles; limits table re-confirmed still unpublished.
  - 11: §1 v4.5 style-instruction bullet re-sourced (dead citation replaced); third Creative Slider (Audio Influence) added [OFFICIAL].
  - 12: §2.9 Custom Models — Premier collaboration + 2x inputs (Oct 15 2026 release note) [OFFICIAL]; §2.9 Workspaces (Pro/Premier, invite-only) [OFFICIAL]; §2.11 Studio 2.0 clip-editing additions (Oct 8+ 2026) [OFFICIAL].
  - 20: full GitHub survey re-run (63 repos); Suno's own beta MCP added [OFFICIAL, 2026-10-28]; star counts and staleness rows updated; survey date bumped to 2026-10-31.
  - Verification layer added: `scripts/check_evals.py` (structural contract for evals/evals.json: unique ids, required fields, script/asset path refs resolve) wired into selftest as check group 8 (`evals:structure`); three new test files (+55 tests, 52 -> 107 total; each mutation-proven to fail).
  - Packaging: `install.sh` destination-guarded (refuses to rm -rf a non-skill dir), excludes `.git/`/`.omo/`/`__pycache__`, made executable; `ci.yml` triggers on master too and runs only the two real entrypoints; CONTRIBUTING/README drift removed (selftest.sh / make / npm / secrets.d never existed; Layout now lists source_check.py, scripts/tests/, evals/, .github/).
  - Companion-library routing made host-relative: the 12-active/35-parked counts are the author's setup; when `lw-*`/`mc-*` are absent the bundle runs the full pipeline alone (70 §5 fallback).
  - Corrected history: the 2026-10-07 tooling entry said "+ 25 tests" for lyric_lint; the file has 31.
- **Sources:** https://help.suno.com/en/articles/13924481 , 13924737 , 13924801 , 13924929 , 3161921 , 3484161 , 10625537 , 6141377 , 9010177 , 12702337 , 3271873 ; https://suno.com/release-notes (incl. suno-mcp-beta, Oct 15 2026 collaboration note); https://suno.com/blog/introducing-v4-5 ; https://suno.com/pricing ; GitHub REST survey of 63 repos 2026-10-31
- **Freshness:** 10, 11, 12, 13, 20 re-verified -> 2026-10-31 (13 unchanged, bump only); SKILL.md, 00-index, 50-self-update, 70-craft-gate -> 2026-10-31; registry `updated` -> 2026-10-31

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
  - Added `scripts/lyric_lint.py` (+ 31 tests): approximate rhyme scheme,
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
