# songwriting-suno

A portable **Agent Skill** for writing songs and controlling AI music generation
(primarily Suno), with an offline knowledge base, objective checker scripts, a
teaching mode, and a self-update/freshness protocol.

Plain files — no build step. Clone it into an agent skills directory and it works.

## Install

```bash
# recommended: clone into the auto-loaded external skills dir
git clone <REPO_URL> ~/.agents/skills/songwriting-suno

# or, from an existing checkout:
./install.sh            # copies into ~/.agents/skills/songwriting-suno
```

Then **restart opencode** (skills load at startup).

Compatible skill locations:

| Agent | Auto-loaded path |
|---|---|
| opencode + AGENTS-style | `~/.agents/skills/<name>/SKILL.md` |
| Claude Code | `~/.claude/skills/<name>/SKILL.md` |
| opencode native | `.opencode/skills/<name>/SKILL.md`, `~/.config/opencode/skills/<name>/SKILL.md` |

## Three modes

- **BUILD** (default) — write a song or a Suno prompt end to end.
- **LEARN** — teach, co-write, critique, and drill (`references/40-learn-with-me.md`).
- **UPDATE** — refresh facts and re-verify sources (`references/50-self-update.md`).

## Layout

```
SKILL.md                 entry point: modes, routing, workflow, rules
references/              topic files, read on demand
  00-index.md            router — which file for which task
  01..06                 craft: structure, rhythm, melody, lyrics, mood, meaning
  07-worked-examples.md  two complete BUILD deliverables (few-shot)
  10..13                 Suno: mechanics, prompting, workflows, vocal control
  20                     tools & projects
  30                     multilingual (zh / en / ms / ja ...)
  40-learn-with-me.md    LEARN mode
  50-self-update.md      UPDATE mode
  60-knowledge-and-retrieval.md  offline KB + online retrieval protocol
scripts/                 runnable tools (prefer running over reading)
  format_style_prompt.py assemble a Suno style + exclude prompt
  syllable_meter.py      count syllables / check a target meter
  lyric_lint.py          rhyme scheme / repetition / cliche lint
  validate_structure.py  section tags + basic song shape
  check_freshness.py     staleness report from assets/freshness.json
  selftest.py            one command that runs every check
assets/                  templates, presets, registries, offline data
  imagery-lexicon.json   index of the offline imagery bank (read one theme)
  imagery/<theme>.json   16 themes of concrete sensory material
  plausibility-checks.md pre-ship reality audit
  persona-presets.json   genre/persona presets
  song-template.md       output template
  freshness.json         what to re-verify and when
  learner-profile.md     learner profile template (copy outside the repo)
```

## Verify

```bash
python3 scripts/selftest.py        # must exit 0
python3 scripts/check_freshness.py --check-coverage
```

## Data & privacy

The learner profile is stored **outside** this repo at
`~/.agents/learner-profiles/songwriting-suno.md`, so updates to the skill never
touch your learning history. No secrets or credentials are stored here.

## Notes

- Facts about Suno change; `scripts/check_freshness.py` tracks staleness.
- License: TBD by the repository owner.
