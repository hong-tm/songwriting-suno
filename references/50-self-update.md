# Self-Update Protocol: Keeping the Bundle's Suno Facts Fresh

> Maintainer-facing reference. A skill agent reading this knows when the
> bundle's factual content must be refreshed, how to refresh it, and how to
> record what changed. Craft content (songwriting references 01-06, 30) is
> stable and rarely needs touching; Suno content (10-13, 20) drifts.

## Quick rules

- Triggers: explicit "update/refresh" command, a stale check before any Suno
  limits/pricing/features answer, or a live contradiction with a documented claim.
- Thresholds: high = warn 30d / stale 60d; medium = warn 90d / stale 180d;
  low = warn 365d / stale 730d. Unsure of tier? Use the FASTER one.
- Rewrite only changed fact sections; never restructure craft prose.
- Every update = bump `last_verified` + add a CHANGELOG entry + re-run evals.
- The updater agent MAY use the network. The bundled scripts never do.
- Never write to or delete `~/.agents/learner-profiles/`.
- A skill cannot self-trigger on a schedule; scheduled checks need a host hook
  (see APPENDIX, optional and not shipped by default).

## 1. Purpose

Suno facts change fast: model families are born and retired in a day (v5.x and
below all retired 2026-09-09 when v6 shipped), character limits stay unpublished
and measurable only by experiment, pricing and credit rules move, and feature
names get relabeled (Custom → Advanced). The mechanics file is already dated on
purpose: SKILL.md frontmatter warns that "references/10-13 are dated" and says
to verify on `help.suno.com` before relying on limits or pricing.

That warning alone is not enough, because nothing tells the agent *when* the
bundle was last verified or *how* to refresh it. This file is that protocol.
It gives three triggers, hard staleness thresholds backed by a registry, a
7-step update workflow, registry maintenance rules, and a changelog format.

The core idea: separate the *date of last verification* from the *quality of
the writing*. A well-written fact from 2024 is still well-written today, but it
is no longer safe to repeat without a check. So the workflow never rewrites the
whole bundle; it re-verifies the facts and patches only what moved.

## 2. The three update triggers

### (a) Explicit command

The user says any of: "update the skill", "refresh the Suno docs", "check
freshness", "is this skill up to date".

Behavior:

1. Run the full 7-step workflow (§4) with the registry check as step 1.
2. Report a diff of what changed, file by file.
3. If everything is fresh, say so in one sentence, with the oldest
   `last_verified` date and its age. Do not rewrite anything fresh.

### (b) Proactive check before answering

Before answering any question about Suno limits, pricing, model versions, or
feature availability:

- IF a freshness check has already run in THIS session AND no high/medium
  entry was stale, skip and answer normally.
- OTHERWISE run `python3 scripts/check_freshness.py` (offline; reads
  `assets/freshness.json` only).

If ANY high or medium entry is STALE:

1. Flag once, with exactly this style of phrasing (fill real date/N and file count):

   > Heads-up: the Suno facts in this skill were last verified 2026-09-01
   > (36 days ago) — want me to refresh before answering?

2. Then answer the question anyway, using the bundled content with the
   "as of" date attached. Never block. Never repeat the flag in the same
   session (once-per-session guard; track it in session state or a plain
   variable — a skill has no memory between sessions, which is another reason
   the check re-runs each session).

If only LOW entries are stale, do not interrupt; answer and optionally note
the date inline ("community-measured, last verified 2026-06").

### (c) Live contradiction

If Suno's live behavior or docs differ from a documented claim — the UI shows
different character limits, a model name changed, a feature is gone:

1. Record the observation immediately in `CHANGELOG.md` under the
   **Unverified reports** section (format: date, file + section affected,
   what was observed, what the doc claims).
2. Offer a targeted refresh: "The live docs now say X; the bundle says Y.
   Want me to verify and update?"
3. If the user declines, the Unverified report stands as the audit trail. Do
   not overwrite the doc on one unconfirmed observation.

## 3. Staleness thresholds

| Tier | Warn | Stale | Applies to | Tier rule |
|---|---|---|---|---|
| **high** | 30d | 60d | `10-suno-mechanics.md`, `20-tools-and-projects.md` | model versions, limits, pricing, feature UI, live tool links |
| **medium** | 90d | 180d | `11-suno-prompting.md`, `12-suno-workflows.md`, `13-vocal-control.md`, `00-index.md`, `SKILL.md` workflow prose | community tag catalogues, feature workflows, tool ecosystem |
| **low** | 365d | 730d | `01`–`06`, `30` (craft) | musical craft knowledge changes glacially |

The per-file authoritative assignment lives in `assets/freshness.json`; this table summarizes it — when the two disagree, the registry wins and this table gets fixed.

**Tie-break rule:** if unsure of a file's tier, pick the FASTER (more
volatile) tier. Over-verifying is cheap; serving a dead fact is not.

### The registry and the checker

- `assets/freshness.json` holds **one entry per fact-bearing file**:
  `{ "path": "references/10-suno-mechanics.md", "volatility": "high",
  "last_verified": "2026-10-07", "sources": ["https://help.suno.com/…"],
  "notes": "v6 era; char limits measured" }`. The `sources` list names the
  canonical URLs the facts came from; the updater re-verifies against that
  exact list (§4 step 3) so verification is reproducible.
- `scripts/check_freshness.py` enforces the registry:
  - **exit 0** — every registered file fresh (warn counts as fresh);
  - **exit 1** — at least one stale entry, OR (with `--check-coverage`) a
    `references/*.md` file that has no registry row;
  - **exit 2** — registry problem itself (missing file, bad JSON, unknown
    volatility tier).
- The script computes ages from `last_verified` vs today, reads files only if
  needed for the coverage check, and **never touches the network**. Verifying
  content freshness by dated URLs is the agent's job. (Why track the date and
  not the bytes: a file can be stale while unchanged — the *knowledge* expires,
  not the text.)

## 4. The 7-step UPDATE workflow

Run in order. Steps 1-2 are cheap and mechanical; 3-4 are judgment; 5-7 are
bookkeeping that must never be skipped.

1. **Run the checker.** `python3 scripts/check_freshness.py --check-coverage`.
   Note exits 1 and 2 separately: exit 2 must be fixed before anything else
   (a broken registry makes all ages meaningless). The coverage check lists
   fact-bearing files with no row — register them (§5) even if content looks
   fine.
2. **Pick the stale targets.** Sort stale files by volatility (high first).
   If the update was prompted by a specific question or contradiction,
   prioritize that file and its layers: changes to 10 usually leak into 11-13.
3. **Re-verify each file against its registry `sources`.** Read the live pages
   listed in the entry (and walk one hop: a release-notes index may reveal a
   newer note than the ones cited). Prefer official help.suno.com pages over
   community pages; keep the OFFICIAL/COMMUNITY flags honest. If a source URL
   is dead, find its replacement and record the new URL in the entry.
4. **Rewrite ONLY the changed fact sections.** Read the file, diff the facts
   against what you just verified, patch those sections. Preserve craft prose,
   examples, structure, and tone. Never break the OFFICIAL/COMMUNITY flagging
   discipline: attach a new flag and a dated source to every changed fact. If
   whole sections of user-supplied craft text would need rewriting, stop and
   ask.
5. **Bump the dates.** Update the entry's `last_verified` for every file you
   actually re-verified (a failed verification is a fact change too), update
   `sources` if they moved, and bump `metadata.updated` in SKILL.md's
   frontmatter — that date is today's real date, not a hoped-for one.
6. **Append a CHANGELOG entry** (format in §7). Newest-first, always at the
   top of the file.
7. **Re-run the evals.** `python3 -m json.tool evals/evals.json` to prove the
   eval file still parses, then re-run `scripts/check_freshness.py` (must be
   exit 0). If a fact changed that an eval exercises (e.g. a style-field cap),
   update that eval case in the same commit. Report the diff of everything
   that changed to the user, in §7's file-list format.

## 5. Registry maintenance rules

- **Every fact-bearing file gets a row.** Adding `references/40-api-economics.md`
  later? Add its `freshness.json` entry in the same change. The
  `--check-coverage` flag catches strays; treat its output as a task, not a note.
- **On rename, migrate in place.** Update the `path`, keep `last_verified`
  (a rename is not a re-verification), and note the rename in the changelog.
- **Never delete a row without a changelog note** saying the file was deleted
  or demoted to pure-lore. Silent deletions leave the coverage check lying.
- **A stale `last_verified` expires even if the file is unchanged.** The date
  is the thing that expires, not the text. If a file has not changed but its
  date is old, do the verification pass and bump the date — do not invent a
  content change just to "earn" the bump.
- **Do not expire the registry itself.** `freshness.json` has no row of its
  own; it is maintained, not re-verified.

## 6. Hard rule: user state is untouchable

**Never write to or delete `~/.agents/learner-profiles/`.** That directory is
user state outside the bundle; it must survive every self-update verbatim.
The bundle's own update touches only files inside
`~/.agents/skills/songwriting-suno/` plus the registry entry list. If any
update step appears to require touching user profile data to proceed, the step
is wrong — redesign it, do not reach. Also never copy profile content into the
bundle during an update (that clones user state into a synced artifact).

## 7. CHANGELOG format

Keep `CHANGELOG.md` in the skill root. Newest-first. One entry per update
session. Fixed fields:

```markdown
## 2026-10-07 — proactive refresh
- **Touched:** references/10-suno-mechanics.md, assets/freshness.json, evals/evals.json
- **Facts changed:**
  - 10 §1.1: noted v6-wild now supports Lose-the-Endings flagging (verified on help.suno.com v6 FAQ)
  - 10 §2: Sounds-mode box limit updated 500 → 800 chars [COMMUNITY, re-measured]
- **Sources:** https://help.suno.com/ (v6 FAQ), https://sunhelp.zendesk.com/… (Exclude Styles note)
- **Freshness:** 10: last_verified → 2026-10-07; 13: verified, unchanged, bumped 2026-10-07
```

Fields, in order: date, files touched, facts changed (each as "file §section:
fact, verified where"), sources actually consulted, freshness bumps. A pure
verification pass with no fact change still gets an entry, with
"**Facts changed:** none (verification only)". Contradiction observations from
§2(c) go under a separate heading at the top until resolved:

```markdown
## Unverified reports
- 2026-10-05: user reports style field rejects >800 chars in the iOS app;
  bundle says 1,000 [COMMUNITY, measured 2026-10-01]. Needs re-measure.
```

## 8. What cannot be automated by a pure skill

A skill is a prompt plus files. It has no cron, no scheduler, and no way to
wake itself up. So:

- Trigger (a) needs the user. Trigger (b) is best-effort inside a session.
- Trigger (c)'s *recording* is possible; its *discovery* only happens when a
  session is actually running.
- Genuine scheduled/automatic checks (e.g. weekly whole-bundle refresh) require
  a host-level hook or cron that runs `scripts/check_freshness.py` and passes
  the result into the session. The bundle ships no such hook. If the host has
  one, stand up the integration; if it doesn't, document the gap here rather
  than pretending the skill handles it.

An agent whose facts age silently is an agent that quotes retired limits with confidence. The protocol keeps the bundle honest; the host hook keeps it maintained.

---

## APPENDIX — host-hook sketch (OPTIONAL, NOT SHIPPED)

Not part of the skill bundle. Provided only as a starting sketch for someone
who wants scheduled freshness checks. Claude Code example (`SessionStart`
hook, from the hooks docs pattern at code.claude.com/docs):

```json
{ "hooks": { "SessionStart": [
  { "command": "python3 ~/.agents/skills/songwriting-suno/scripts/check_freshness.py || echo 'SUNO SKILL STALE (exit '?')'" } ] } }
```

opencode would need a plugin listening on `session.created` (or equivalent
session-start event) that runs the same script and surfaces a one-line warning
into message context. Defaults everywhere are "off": the protocol works
without these, via triggers (a)-(c) only. If you wire one up, keep the hook
read-only about the bundle and never let it auto-edit files — automated
updates by rule follow §4 with a human-aware diff summary.

---

## Note on what NOT to change

Never renumber the references (10-13 are the "Suno facts at risk" lane; craft
files 01-06 stay as-is): the reference map, registry paths, and the lane
boundary must stay stable. Adding a new file is fine.

## Sources

- Suno help center — facts, limits, modes, features:
  https://help.suno.com/
- Suno release notes (what changed, exactly the thing this protocol watches):
  https://suno.com/blog/
- Suno AI Music API docs (community price/limit cross-check endpoint):
  https://docs.sunoapi.org/
- Anthropic Agent Skills spec (bundle format frontmatter, `metadata.updated`):
  https://agentskills.io/
- Claude Code hooks (for the APPENDIX SessionStart sketch):
  https://code.claude.com/docs/en/hooks
- Write the Docs — ongoing content maintenance:
  https://www.writethedocs.org/guide/writing/best-practices/
- Google technical-writing style guidance (why "facts have dates" matters):
  https://developers.google.com/tech-writing
- Windows/macOS docs-lifecycle guidance, similar maintenance framing:
  https://learn.microsoft.com/en-us/style-guide/
- Suno product root (current-era cross-check):
  https://suno.com/

Note: deep article-level links change on Suno's site; this list stays at canonical
roots per house style — walk from the release-notes index on each update, and confirm
any item you bring in for a refreshed source list.
