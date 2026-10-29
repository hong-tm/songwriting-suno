#!/usr/bin/env python3
"""Freshness report for the songwriting-suno skill.

Reads <skill_root>/assets/freshness.json (schema:1) and reports, per registered
entry, how long ago its documented facts were last verified. The default
registry path is resolved from this script's own location (skill root = parent
of scripts/), so the CLI is cwd-independent. Entry paths in the registry are
relative to the skill root (the registry file's grandparent directory).

Two-tier status model — thresholds come from the entry's tier (volatility):

    OK       age <= warn_days
    WARNING  warn_days < age <= stale_days
    STALE    age > stale_days

where age = (today - last_verified).days and today = date.today().

Source checking (--check-sources, implied by --check-coverage):

    Every `sources` string of every entry must be a syntactically
    well-formed absolute http(s) URL. This is a deliberately conservative
    linter for obviously-broken URLs (the bug class seen in practice:
    pasted/garbled text like `https://www.retrievalpractice.orgPooja`),
    not a full RFC 3986 validator. A source is INVALID when it is:

    - not a non-empty string, or contains whitespace
    - missing a scheme, or the scheme is not http / https
    - missing a host, or the host has no dot in it
    - containing an ellipsis (`…` or `...`) — truncated-paste signature
    - glue signature: any run of >= 2 uppercase letters inside the host
      (e.g. `...orgPOOJA`), or the host ends in a known domain suffix
      (com/edu/gov/int/net/org) followed by a capitalized word
      (e.g. `...orgPooja`)
    - host fails `[a-z0-9.-]+`, has any empty or > 63-char label

Exit codes:
    0  no findings (no STALE entries, nothing unregistered, no bad sources)
    1  at least one STALE entry, or -- with --check-coverage -- at least one
       references/*.md file under the skill root missing from the registry,
       or, with source checking on, at least one invalid source URL
    2  registry missing / not valid JSON / unknown schema / an entry path does
       not exist on disk / registry otherwise unusable
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from source_check import source_findings

SCHEMA_VERSION = 1
DEFAULT_REGISTRY = Path(__file__).resolve().parent.parent / "assets" / "freshness.json"

OK = "OK"
WARNING = "WARNING"
STALE = "STALE"


class RegistryError(Exception):
    """The registry is missing, unreadable, or inconsistent with its contract."""


def load_registry(path: Path) -> dict:
    """Read and schema-check the registry (boundary parse; callers trust it)."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RegistryError(f"registry not readable: {path} ({exc})") from exc
    try:
        registry = json.loads(text)
    except json.JSONDecodeError as exc:
        raise RegistryError(f"registry is not valid JSON: {path} ({exc})") from exc
    if not isinstance(registry, dict) or registry.get("schema") != SCHEMA_VERSION:
        raise RegistryError(f"unknown schema in {path}: expected {SCHEMA_VERSION}")
    if "updated" not in registry:
        raise RegistryError(f"registry missing 'updated': {path}")
    for key in ("tiers", "entries"):
        if not isinstance(registry.get(key), dict):
            raise RegistryError(f"registry missing/invalid {key!r}: {path}")
    for tier, thresholds in registry["tiers"].items():
        if not isinstance(thresholds, dict) or not {
            "warn_days",
            "stale_days",
        } <= thresholds.keys():
            raise RegistryError(f"tier {tier!r} lacks warn_days/stale_days")
    return registry


def status_for_age(age_days: int, volatility: str, tiers: dict) -> str:
    """Map an entry's age onto the two-tier status model."""
    thresholds = tiers.get(volatility)
    if thresholds is None:
        raise RegistryError(f"unknown volatility tier {volatility!r}")
    if age_days <= thresholds["warn_days"]:
        return OK
    if age_days <= thresholds["stale_days"]:
        return WARNING
    return STALE


def build_rows(registry: dict, skill_root: Path, today: date) -> list[dict]:
    """One report row per registry entry; raises RegistryError on bad entries."""
    rows: list[dict] = []
    for rel_path, meta in registry["entries"].items():
        entry_file = skill_root / rel_path
        if not entry_file.exists():
            raise RegistryError(f"entry path does not exist on disk: {entry_file}")
        if not isinstance(meta, dict):
            raise RegistryError(f"entry {rel_path!r} is not an object")
        try:
            last_verified = date.fromisoformat(meta["last_verified"])
        except (KeyError, TypeError, ValueError) as exc:
            raise RegistryError(f"bad last_verified for {rel_path!r}: {exc}") from exc
        volatility = meta.get("volatility", "")
        age_days = (today - last_verified).days
        rows.append(
            {
                "path": rel_path,
                "volatility": volatility,
                "last_verified": last_verified.isoformat(),
                "age_days": age_days,
                "status": status_for_age(age_days, volatility, registry["tiers"]),
                "sources": meta.get("sources", []),
            }
        )
    return rows


def unregistered_references(
    registry: dict, skill_root: Path, registry_path: Path
) -> list[str]:
    """references/*.md files under the skill root absent from registry entries."""
    references_dir = skill_root / "references"
    if not references_dir.is_dir():
        return []
    known = set(registry["entries"])
    unregistered: list[str] = []
    for md_file in sorted(references_dir.rglob("*.md")):
        rel_path = md_file.relative_to(skill_root).as_posix()
        if rel_path in known:
            continue
        if md_file.resolve() == registry_path.resolve():
            continue  # never flag the registry itself
        unregistered.append(rel_path)
    return unregistered


def summarize(rows: list[dict]) -> dict:
    counts = {OK: 0, WARNING: 0, STALE: 0}
    for row in rows:
        counts[row["status"]] += 1
    return counts


def render_rows(rows: list[dict], stale_only: bool) -> list[str]:
    """Aligned 'STATUS | tier | age(d) | last_verified | path' lines."""
    shown = [row for row in rows if not stale_only or row["status"] in (WARNING, STALE)]
    if not shown:
        return []
    status_w = max(len(row["status"]) for row in shown)
    tier_w = max(len(row["volatility"]) for row in shown)
    age_w = max(len(str(row["age_days"])) for row in shown)
    return [
        f"{row['status']:<{status_w}} | {row['volatility']:<{tier_w}} | "
        f"{row['age_days']:>{age_w}} | {row['last_verified']} | {row['path']}"
        for row in shown
    ]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report freshness of the songwriting-suno skill's registered docs."
    )
    parser.add_argument("--json", action="store_true", help="emit the report as JSON")
    parser.add_argument(
        "--stale-only", action="store_true", help="print only WARNING/STALE rows"
    )
    parser.add_argument(
        "--check-coverage",
        action="store_true",
        help=(
            "also flag references/*.md files missing from the registry "
            "(implies --check-sources)"
        ),
    )
    parser.add_argument(
        "--check-sources",
        action="store_true",
        help=(
            "also flag invalid source URLs in every entry's `sources` array "
            "(conservative heuristic, see module docstring)"
        ),
    )
    parser.add_argument(
        "--registry", type=Path, default=DEFAULT_REGISTRY, help="path to freshness.json"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    registry_path = args.registry
    skill_root = registry_path.resolve().parent.parent
    today = date.today()
    try:
        registry = load_registry(registry_path)
        rows = build_rows(registry, skill_root, today)
        unregistered = (
            unregistered_references(registry, skill_root, registry_path)
            if args.check_coverage
            else []
        )
    except RegistryError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    # --check-coverage implies --check-sources (contract, see module docstring)
    check_sources = args.check_sources or args.check_coverage
    bad_sources = source_findings(rows) if check_sources else []
    counts = summarize(rows)
    exit_code = 1 if (counts[STALE] or unregistered or bad_sources) else 0

    if args.json:
        print(
            json.dumps(
                {
                    "schema": SCHEMA_VERSION,
                    "updated": registry["updated"],
                    "checked_date": today.isoformat(),
                    "entries": rows,
                    "summary": {
                        "ok": counts[OK],
                        "warning": counts[WARNING],
                        "stale": counts[STALE],
                        "unregistered": unregistered,
                        "bad_sources": bad_sources,
                    },
                    "exit_code": exit_code,
                },
                indent=2,
            )
        )
        return exit_code

    for line in render_rows(rows, args.stale_only):
        print(line)
    for rel_path in unregistered:
        print(f"UNREGISTERED: {rel_path}")
    for finding in bad_sources:
        print(f"BAD-SOURCE: {finding['path']} :: {finding['source']} :: {finding['reason']}")
    print(
        f"{len(rows)} entries: {counts[OK]} OK, {counts[WARNING]} warning, "
        f"{counts[STALE]} stale"
    )
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
