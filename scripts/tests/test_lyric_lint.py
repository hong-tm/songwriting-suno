"""Tests for scripts/lyric_lint.py (pinned contract).

CLI cases drive the real script through subprocess so exit codes are real:
0 = no actionable findings, 1 = cliche hit or repetition count above
--min-repeat, 2 = usage problem. Scheme/pair cases call analyze()
directly for precise assertions. The script must stay cwd-independent
(it resolves its sibling syllable_meter.py via __file__), which the
other-cwd cases pin down.
"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "lyric_lint.py"
sys.path.insert(0, str(SCRIPT.parent))

import lyric_lint  # noqa: E402


def run_cli(
    *args: str, cwd: Path | None = None, stdin: str | None = None
) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        input=stdin,
        cwd=None if cwd is None else str(cwd),
    )


class RhymeSchemeTests(unittest.TestCase):
    # --- scheme 1: perfect rhymes -> AABB ---------------------------------
    def test_perfect_rhymes_aabb(self) -> None:
        res = lyric_lint.analyze(
            "[Verse]\nchasing the light\ninto the night\nthe road to home\nwe walk alone\n"
        )
        verse = res["groups"][1]
        self.assertEqual(verse["scheme"], "AABB")
        self.assertEqual(verse["perfect_pairs"], [[2, 3], [4, 5]])
        self.assertEqual(verse["near_pairs"], [])

    # --- scheme 2: same vowel, different coda -> near rhyme a' ------------
    def test_near_assonance_gets_prime_symbol(self) -> None:
        res = lyric_lint.analyze("[Verse]\ncity light\nsky so high\n")
        verse = res["groups"][1]
        self.assertEqual(verse["scheme"], "Aa'")
        self.assertEqual(verse["near_pairs"], [[2, 3]])
        self.assertEqual(verse["perfect_pairs"], [])
        self.assertEqual(verse["lines"][1]["symbol"], "a'")
        self.assertTrue(verse["lines"][1]["symbol"].endswith("'"))

    # --- scheme 3: perfect and near mixed, letters stay stable ------------
    def test_mixed_perfect_and_near(self) -> None:
        res = lyric_lint.analyze("[Verse]\ninto the night\nsky so high\ncity light\n")
        verse = res["groups"][1]
        self.assertEqual(verse["scheme"], "Aa'A")
        self.assertEqual(verse["perfect_pairs"], [[2, 4]])
        self.assertEqual(verse["near_pairs"], [[2, 3], [3, 4]])
        self.assertEqual(verse["near_desc"], ["(2,3), (3,4) vowel 'i'"])

    # --- scheme 4: no rhymable word -> '-' --------------------------------
    def test_no_rhymable_word_gets_dash(self) -> None:
        res = lyric_lint.analyze("[Verse]\n2024\nsky so high\n")
        verse = res["groups"][1]
        self.assertEqual(verse["lines"][0]["symbol"], "-")
        self.assertIsNone(verse["lines"][0]["rhyme_key"])

    # --- scheme 5: TAG_RE is the shared validate_structure.py convention ---
    def test_tag_re_matches_validate_structure_convention(self) -> None:
        self.assertEqual(lyric_lint.TAG_RE.pattern, r"^\s*\[([^\[\]]+)\]\s*$")

    # --- scheme 6: lines before the first tag form the preamble group ------
    def test_preamble_group(self) -> None:
        res = lyric_lint.analyze("just a stray line\n[Verse]\nla la la la\n")
        self.assertEqual(res["section_count"], 1)
        self.assertEqual(res["preamble_count"], 1)
        self.assertEqual(res["groups"][0]["tag"], "(preamble)")
        self.assertEqual(res["groups"][0]["line_count"], 1)

    # --- scheme 7: sections letter independently ---------------------------
    def test_sections_use_independent_letters(self) -> None:
        res = lyric_lint.analyze(
            "[Verse]\nsome day\nsome way\n[Verse 2]\nwe play\nwe say\n"
        )
        self.assertEqual(res["groups"][1]["scheme"], "AA")
        self.assertEqual(res["groups"][2]["scheme"], "AA")

    # --- scheme 8: the approximation disclaimer is pinned ------------------
    def test_docstring_disclaims_approximation(self) -> None:
        doc = (lyric_lint.__doc__ or "").lower()
        self.assertIn("approximat", doc)
        self.assertIn("not ground truth", doc)


class ClicheTests(unittest.TestCase):
    # --- cliche 1: hit -> exit 1 with line number --------------------------
    def test_cliche_hit_exit_1_with_line_number(self) -> None:
        proc = run_cli("--text", "[Verse]\nhello world\nyou got a broken heart\n")
        self.assertEqual(proc.returncode, 1, proc.stdout)
        self.assertIn("line 3: matched 'broken heart'", proc.stdout)

    # --- cliche 2: case-insensitive ----------------------------------------
    def test_cliche_case_insensitive(self) -> None:
        proc = run_cli("--text", "YOU GOT A BROKEN HEART\n")
        self.assertEqual(proc.returncode, 1, proc.stdout)
        self.assertIn("matched 'broken heart'", proc.stdout)

    # --- cliche 3: --no-cliche disables the scan ---------------------------
    def test_no_cliche_disables_scan(self) -> None:
        proc = run_cli("--text", "you got a broken heart\n", "--no-cliche")
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertIn("(scan disabled by --no-cliche)", proc.stdout)

    # --- cliche 4: tag lines are structure, not lyrics ---------------------
    def test_tags_are_not_scanned_for_cliches(self) -> None:
        proc = run_cli("--text", "[Chorus: broken heart]\nla la la\n")
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertNotIn("matched", proc.stdout)

    # --- cliche 5: the built-in list is documented and >= 25 entries -------
    def test_cliche_list_has_at_least_25_entries(self) -> None:
        self.assertGreaterEqual(len(lyric_lint.CLICHE_LIST), 25)
        for entry in lyric_lint.CLICHE_LIST:
            self.assertIsInstance(entry, str)
            self.assertTrue(entry.strip(), entry)


class RepetitionTests(unittest.TestCase):
    # --- repeat 1: 2x == chorus-normal, informational, exit 0 --------------
    def test_double_repeat_informational_exit_0(self) -> None:
        text = "[Chorus]\nla la la la\nother line here\nla la la la\n"
        proc = run_cli("--text", text)
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertIn("2x | informational", proc.stdout)

    # --- repeat 2: 3x is above --min-repeat 2 -> actionable, exit 1 --------
    def test_triple_repeat_actionable_exit_1(self) -> None:
        text = "[Chorus]\nla la la la\nother line here\nla la la la\nla la la la\n"
        proc = run_cli("--text", text)
        self.assertEqual(proc.returncode, 1, proc.stdout)
        self.assertIn("3x | above --min-repeat 2", proc.stdout)

    # --- repeat 3: lowering --min-repeat makes 2x actionable ---------------
    def test_min_repeat_lowers_threshold(self) -> None:
        text = "[Chorus]\nla la la la\nother line here\nla la la la\n"
        proc = run_cli("--text", text, "--min-repeat", "1")
        self.assertEqual(proc.returncode, 1, proc.stdout)

    # --- repeat 4: normalization ignores case, punctuation, extra spaces ---
    def test_normalization_ignores_case_and_punctuation(self) -> None:
        text = "[Verse]\nLa La La La!\nnothing else here\nla  la la la\n"
        proc = run_cli("--text", text)
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertIn("2x | informational", proc.stdout)

    # --- repeat 5: section tags are not counted as repeated lyric lines ----
    def test_section_tags_not_counted_as_repeats(self) -> None:
        proc = run_cli("--text", "[Chorus]\nla la\n[Chorus]\nla la\n", "--json")
        self.assertEqual(proc.returncode, 0, proc.stdout)
        data = json.loads(proc.stdout)
        self.assertEqual([r["normalized"] for r in data["repeats"]], ["la la"])


class ExitCodeTests(unittest.TestCase):
    # --- exit 1: empty --text -> usage problem ------------------------------
    def test_empty_text_exit_2(self) -> None:
        proc = run_cli("--text", "")
        self.assertEqual(proc.returncode, 2)
        self.assertTrue(proc.stderr.strip())

    # --- exit 2: piped empty stdin -> usage problem -------------------------
    def test_no_input_exit_2(self) -> None:
        proc = run_cli(stdin="")
        self.assertEqual(proc.returncode, 2)
        self.assertTrue(proc.stderr.strip())

    # --- exit 2: --min-repeat below 1 ---------------------------------------
    def test_bad_min_repeat_exit_2(self) -> None:
        proc = run_cli("--min-repeat", "0", "--text", "la la\n")
        self.assertEqual(proc.returncode, 2)

    # --- exit 2: unreadable file --------------------------------------------
    def test_missing_file_exit_2(self) -> None:
        proc = run_cli("/nonexistent/lyrics/ghost.txt")
        self.assertEqual(proc.returncode, 2)
        self.assertTrue(proc.stderr.strip())

    # --- --warn-only forces exit 0 for findings ------------------------------
    def test_warn_only_forces_zero(self) -> None:
        proc = run_cli("--text", "you got a broken heart\n", "--warn-only")
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertIn("Result: PASS (--warn-only", proc.stdout)

    # --- stdin is a valid input path -----------------------------------------
    def test_stdin_input(self) -> None:
        proc = run_cli(stdin="[Chorus]\nyou got a broken heart\n")
        self.assertEqual(proc.returncode, 1, proc.stdout)

    # --- cwd independence: file by absolute path, other cwd ------------------
    def test_file_positional_from_other_cwd(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            lyric_file = tmp_path / "song.txt"
            lyric_file.write_text(
                "[Verse]\nchasing the light\ninto the night\n", encoding="utf-8"
            )
            proc = run_cli(str(lyric_file), cwd=tmp_path)
            self.assertEqual(proc.returncode, 0, proc.stderr)

    # --- input precedence: positional file wins over --text ------------------
    def test_file_wins_over_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            lyric_file = Path(tmp) / "clean.txt"
            lyric_file.write_text(
                "[Verse]\nchasing the light\ninto the night\n", encoding="utf-8"
            )
            proc = run_cli(str(lyric_file), "--text", "you got a broken heart\n")
            self.assertEqual(proc.returncode, 0, proc.stdout)


class JsonTests(unittest.TestCase):
    # --- json 1: pinned shape, same exit code as text mode ------------------
    def test_json_shape_and_exit_code(self) -> None:
        proc = run_cli(
            "--text", "[Verse]\nhello world\nyou got a broken heart\n", "--json"
        )
        self.assertEqual(proc.returncode, 1, proc.stdout)
        data = json.loads(proc.stdout)  # stdout must be pure, valid JSON
        self.assertEqual(
            set(data),
            {
                "tool",
                "approximate",
                "min_repeat",
                "warn_only",
                "total_lines",
                "section_count",
                "preamble_count",
                "groups",
                "repeats",
                "cliche_matches",
                "cliche_scan_disabled",
                "actionable",
            },
        )
        self.assertTrue(data["approximate"])
        self.assertTrue(data["actionable"])
        self.assertFalse(data["warn_only"])
        self.assertEqual(data["min_repeat"], 2)
        self.assertEqual(data["total_lines"], 3)
        verse = data["groups"][1]
        self.assertEqual(
            set(verse),
            {
                "index",
                "tag",
                "line_count",
                "lines",
                "scheme",
                "perfect_pairs",
                "near_pairs",
                "near_desc",
                "syllables",
            },
        )
        self.assertEqual(verse["tag"], "Verse")
        self.assertEqual(
            set(verse["lines"][0]), {"n", "text", "symbol", "rhyme_key", "syllables"}
        )
        self.assertEqual(
            data["cliche_matches"],
            [{"line": 3, "text": "you got a broken heart", "cliche": "broken heart"}],
        )

    # --- json 2: clean run -> actionable false, exit 0 -----------------------
    def test_json_clean_run_actionable_false(self) -> None:
        proc = run_cli("--text", "[Verse]\nla la la la\n", "--json")
        self.assertEqual(proc.returncode, 0, proc.stdout)
        data = json.loads(proc.stdout)
        self.assertFalse(data["actionable"])
        self.assertEqual(data["repeats"], [])
        self.assertEqual(data["cliche_matches"], [])


class SpreadTests(unittest.TestCase):
    # --- spread 1: min/max/median(3.5)/spread on a known pair ---------------
    def test_spread_values_and_half_median(self) -> None:
        res = lyric_lint.analyze("[Verse]\nla la la la la\nhello\n")
        self.assertEqual(
            res["groups"][1]["syllables"], {"min": 2, "max": 5, "median": 3.5, "spread": 3}
        )

    # --- spread 2: whole-number median (6, 8 -> 7) ---------------------------
    def test_spread_whole_median(self) -> None:
        res = lyric_lint.analyze(
            "[Verse]\nI drive until the streetlights end\nI whisper it again\n"
        )
        syl = res["groups"][1]["syllables"]
        self.assertEqual(syl["min"], 6)
        self.assertEqual(syl["max"], 8)
        self.assertEqual(syl["median"], 7)
        self.assertEqual(syl["spread"], 2)


class DeterminismTests(unittest.TestCase):
    # --- deterministic: identical input -> identical report ------------------
    def test_analyze_is_deterministic(self) -> None:
        text = (
            "[Verse]\ncity light\nsky so high\n[Chorus]\nla la la la\nla la la la\n"
        )
        self.assertEqual(lyric_lint.analyze(text), lyric_lint.analyze(text))


if __name__ == "__main__":
    unittest.main()
