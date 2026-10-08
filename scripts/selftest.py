#!/usr/bin/env python3
"""Selftest for the whole songwriting-suno skill bundle.

One cwd-independent command that proves the bundle still works after any
self-update: script help responses, unit tests, freshness coverage, the
lyric tools on built-in fixtures, and JSON sanity of the asset files.

All paths are resolved from this script's own location (skill root =
parent of scripts/), so it runs from any working directory. Runs no
network, writes no files, and only ever reports — check failures are
evidence, never auto-fixed.

Checks (in order):
  1. help        every scripts/*.py except selftest.py and anything under
                 scripts/tests/ answers --help with exit code 0; scripts
                 are auto-discovered with Path.glob so future scripts are
                 covered automatically
  2. unittest    python3 -m unittest discover over scripts/tests (and any
                 nested tests/ dir) — all tests must pass
  3. freshness   check_freshness.py --check-coverage exits 0
  4. structure   validate_structure.py exits 0 on the built-in fixture
                 '[Verse]\nline one\n[Chorus]\nbig hook\n'
  5. meter       syllable_meter.py --expect 5,6 exits 0 on the built-in
                 fixture 'Hello world tonight\nI feel the city light\n'
  6. lyric_lint  lyric_lint.py exits 1 on a built-in cliche fixture
                 ('reach for the stars' / 'dance in the rain'), proving the
                 linter is wired end to end; SKIP if the script is absent
  7. json        evals/evals.json, assets/freshness.json and
                 assets/persona-presets.json each parse with json.load

Exit codes:
    0  no FAIL verdicts (SKIP allowed)
    1  at least one check FAILED
    2  usage error (argparse)

Usage:
  python3 selftest.py [--verbose] [--json]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

PASS = "PASS"
FAIL = "FAIL"
SKIP = "SKIP"
Verdict = str  # one of PASS/FAIL/SKIP; kept a plain str alias for json output

SCRIPTS_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPTS_DIR.parent

LYRIC_LINT = "lyric_lint.py"
STRUCTURE_FIXTURE = "[Verse]\nline one\n[Chorus]\nbig hook\n"
METER_FIXTURE = "Hello world tonight\nI feel the city light\n"
JSON_PATHS = (
    "evals/evals.json",
    "assets/freshness.json",
    "assets/persona-presets.json",
)


@dataclass(frozen=True, slots=True)
class CheckResult:
    """One verified property of the bundle; verdict in {PASS, FAIL, SKIP}."""

    name: str
    verdict: Verdict
    detail: str


def run_tool(
    args: list[str], stdin_text: str | None = None
) -> subprocess.CompletedProcess[str]:
    """Run a subprocess with captured output; never raises on nonzero exit."""
    return subprocess.run(
        [sys.executable, *args],
        capture_output=True,
        text=True,
        input=stdin_text,
    )


def describe(proc: subprocess.CompletedProcess[str]) -> str:
    first = (proc.stdout or proc.stderr).strip().splitlines()
    head = first[0][:80] if first else "(no output)"
    return f"exit={proc.returncode} | {head}"


def check_help(script: Path) -> CheckResult | None:
    """Check 1: one script answers --help with exit 0; None = not a target."""
    if script.name == "selftest.py":
        return None
    proc = run_tool([str(script), "--help"])
    verdict = PASS if proc.returncode == 0 else FAIL
    return CheckResult(f"help:{script.name}", verdict, describe(proc))


def script_help_checks() -> list[CheckResult]:
    return [r for r in map(check_help, sorted(SCRIPTS_DIR.glob("*.py"))) if r]


def tests_dirs() -> list[Path]:
    """scripts/tests itself plus any tests/ dir one level below scripts/."""
    candidates = {SCRIPTS_DIR / "tests"}
    candidates.update(SCRIPTS_DIR.glob("*/tests"))
    return sorted(d for d in candidates if d.is_dir())


def check_unittest(tests_dir: Path) -> CheckResult:
    """Check 2: unittest discovery over one tests dir (start == top-level
    so test modules import without scripts/tests/__init__.py)."""
    rel = tests_dir.relative_to(SCRIPTS_DIR).as_posix()
    proc = subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            str(tests_dir),
            "-t",
            str(tests_dir),
        ],
        capture_output=True,
        text=True,
    )
    verdict = PASS if proc.returncode == 0 else FAIL
    return CheckResult(f"unittest:{rel}", verdict, describe(proc))


def check_freshness_coverage() -> CheckResult:
    """Check 3: the freshness registry covers every references/*.md."""
    proc = run_tool(
        [str(SCRIPTS_DIR / "check_freshness.py"), "--check-coverage"]
    )
    verdict = PASS if proc.returncode == 0 else FAIL
    return CheckResult("freshness:coverage", verdict, describe(proc))


def check_lyric_lint_fixture() -> CheckResult:
    """Check 6: lyric_lint.py flags its built-in cliche fixture (exit 1)."""
    script = SCRIPTS_DIR / LYRIC_LINT
    if not script.is_file():
        return CheckResult("fixture:lyric_lint", SKIP, "script not present")
    proc = run_tool(
        [str(script), "--text", "[Chorus]\nwe reach for the stars\ndance in the rain"]
    )
    verdict = PASS if proc.returncode == 1 else FAIL
    return CheckResult("fixture:lyric_lint", verdict, describe(proc))


def check_json_file(rel_path: str) -> CheckResult:
    """Check 7: one JSON asset parses (or FAIL if missing/invalid)."""
    path = SKILL_ROOT / rel_path
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return CheckResult(f"json:{rel_path}", FAIL, str(exc))
    try:
        json.loads(text)
    except json.JSONDecodeError as exc:
        return CheckResult(f"json:{rel_path}", FAIL, str(exc))
    return CheckResult(f"json:{rel_path}", PASS, "parsed")


def run_checks() -> list[CheckResult]:
    checks: list[CheckResult] = []
    checks.extend(script_help_checks())
    checks.extend(check_unittest(d) for d in tests_dirs())
    checks.append(check_freshness_coverage())

    structure = run_tool(
        [str(SCRIPTS_DIR / "validate_structure.py")], STRUCTURE_FIXTURE
    )
    checks.append(
        CheckResult(
            "fixture:validate_structure",
            PASS if structure.returncode == 0 else FAIL,
            describe(structure),
        )
    )

    meter = run_tool(
        [str(SCRIPTS_DIR / "syllable_meter.py"), "--expect", "5,6"],
        METER_FIXTURE,
    )
    checks.append(
        CheckResult(
            "fixture:syllable_meter",
            PASS if meter.returncode == 0 else FAIL,
            describe(meter),
        )
    )

    checks.append(check_lyric_lint_fixture())
    checks.extend(check_json_file(rel) for rel in JSON_PATHS)
    return checks


def render(checks: Iterable[CheckResult], verbose: bool) -> list[str]:
    lines: list[str] = []
    for check in checks:
        lines.append(f"{check.verdict} {check.name}")
        if check.verdict == FAIL or verbose:
            lines.append(f"    {check.detail}")
    return lines


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="selftest.py",
        description="Run the full self-check suite for the songwriting-suno skill bundle.",
        epilog=(
            "Exit code: 0 = no failures, 1 = at least one check failed.\n"
            "Example:\n"
            "  python3 %(prog)s --verbose\n"
            "  python3 %(prog)s --json"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--verbose", action="store_true", help="show captured output for all checks"
    )
    parser.add_argument("--json", action="store_true", help="emit results as JSON")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    checks = run_checks()
    passed = sum(c.verdict == PASS for c in checks)
    failed = sum(c.verdict == FAIL for c in checks)
    skipped = sum(c.verdict == SKIP for c in checks)
    summary = f"{passed} passed, {failed} failed, {skipped} skipped"
    exit_code = 1 if failed else 0

    if args.json:
        print(
            json.dumps(
                {
                    "results": [
                        vars_check(c) for c in checks
                    ],
                    "summary": {
                        "passed": passed,
                        "failed": failed,
                        "skipped": skipped,
                    },
                    "exit_code": exit_code,
                },
                indent=2,
            )
        )
        return exit_code

    for line in render(checks, args.verbose):
        print(line)
    print(summary)
    return exit_code


def vars_check(check: CheckResult) -> dict:
    return {
        "name": check.name,
        "verdict": check.verdict,
        "detail": check.detail,
    }


if __name__ == "__main__":
    sys.exit(main())
