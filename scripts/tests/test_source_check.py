"""Tests for scripts/source_check.py (pinned contract).

source_check is a module, not a CLI (imported by check_freshness.py), so
these cases call the two stable internals directly: invalid_source_reason
returns a reason string for obviously-broken source URLs and None for
acceptable ones; source_findings aggregates those reasons across registry
rows. The pinned rules are the bug class seen in practice — pasted/garbled
URLs such as `https://www.retrievalpractice.orgPooja` — not RFC 3986.
"""

import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "source_check.py"
sys.path.insert(0, str(SCRIPT.parent))

from source_check import invalid_source_reason, source_findings  # noqa: E402


class InvalidSourceReasonTests(unittest.TestCase):
    def test_plain_https_url_is_acceptable(self) -> None:
        self.assertIsNone(invalid_source_reason("https://example.com/page"))

    def test_subdomain_and_port_and_userinfo_are_acceptable(self) -> None:
        self.assertIsNone(
            invalid_source_reason("http://user@sub.example.co.uk:8080/path")
        )

    def test_glued_word_in_host_is_rejected(self) -> None:
        # The original bug this linter was written for: the glued capital
        # fails the host charset rule first (the glue regexes further down
        # are unreachable for uppercase hosts) — either way it is invalid.
        self.assertEqual(
            invalid_source_reason("https://www.retrievalpractice.orgPooja"),
            "host has characters outside [a-z0-9.-]: 'www.retrievalpractice.orgPooja'",
        )

    def test_uppercase_host_is_rejected(self) -> None:
        self.assertEqual(
            invalid_source_reason("https://EXAMPLE.com"),
            "host has characters outside [a-z0-9.-]: 'EXAMPLE.com'",
        )

    def test_missing_scheme_is_rejected(self) -> None:
        self.assertEqual(
            invalid_source_reason("example.com/page"),
            "scheme is not http(s): ''",
        )

    def test_non_http_scheme_is_rejected(self) -> None:
        self.assertEqual(
            invalid_source_reason("ftp://example.com/file"),
            "scheme is not http(s): 'ftp'",
        )

    def test_whitespace_is_rejected(self) -> None:
        self.assertEqual(
            invalid_source_reason("https://example.com/a b"),
            "contains whitespace",
        )

    def test_unicode_ellipsis_is_rejected(self) -> None:
        self.assertEqual(
            invalid_source_reason("https://example.com/long…"),
            "contains an ellipsis",
        )

    def test_ascii_ellipsis_is_rejected(self) -> None:
        self.assertEqual(
            invalid_source_reason("https://example.com/long..."),
            "contains an ellipsis",
        )

    def test_dotless_host_is_rejected(self) -> None:
        self.assertEqual(
            invalid_source_reason("https://localhost/x"),
            "host has no dot or an empty label: 'localhost'",
        )

    def test_empty_label_is_rejected(self) -> None:
        self.assertEqual(
            invalid_source_reason("https://example..com/x"),
            "host has no dot or an empty label: 'example..com'",
        )

    def test_overlong_label_is_rejected(self) -> None:
        label = "a" * 64
        self.assertEqual(
            invalid_source_reason(f"https://{label}.example.com/x"),
            f"host label exceeds 63 chars: '{label}.example.com'",
        )

    def test_empty_string_is_rejected(self) -> None:
        self.assertEqual(invalid_source_reason(""), "not a non-empty string")


class SourceFindingsTests(unittest.TestCase):
    ROWS = [
        {
            "path": "references/10-suno-mechanics.md",
            "sources": ["https://example.com/ok", "https://example.orgPooja/x"],
        },
        {"path": "references/13-vocal-control.md", "sources": []},
        {"path": "references/20-tools-and-projects.md", "sources": ["bad url"]},
    ]

    def test_one_finding_per_invalid_source(self) -> None:
        findings = source_findings(self.ROWS)
        self.assertEqual(len(findings), 2)
        self.assertEqual(findings[0]["path"], "references/10-suno-mechanics.md")
        self.assertEqual(findings[0]["source"], "https://example.orgPooja/x")
        self.assertEqual(
            findings[0]["reason"],
            "host has characters outside [a-z0-9.-]: 'example.orgPooja'",
        )
        self.assertEqual(findings[1]["path"], "references/20-tools-and-projects.md")
        self.assertEqual(findings[1]["source"], "bad url")
        self.assertEqual(findings[1]["reason"], "contains whitespace")

    def test_clean_rows_yield_no_findings(self) -> None:
        rows = [
            {
                "path": "references/00-index.md",
                "sources": ["https://a.example.com", "http://b.example.org/x"],
            }
        ]
        self.assertEqual(source_findings(rows), [])

    def test_empty_input_yields_no_findings(self) -> None:
        self.assertEqual(source_findings([]), [])


if __name__ == "__main__":
    unittest.main()
