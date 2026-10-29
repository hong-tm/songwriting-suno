#!/usr/bin/env python3
"""Source-URL validation for the freshness checker (see check_freshness.py).

A source is a "reference URL" recorded in an entry's `sources` array. This
module is a deliberately conservative *linter* for obviously-broken URLs —
the bug class seen in practice: pasted/garbled text such as
`https://www.retrievalpractice.orgPooja` — not a full RFC 3986 validator.
A source is INVALID when it is:

- not a non-empty string, or contains whitespace
- missing a scheme, or the scheme is not http / https
- missing a host, or the host has characters outside [a-z0-9.-]
- hosting no dot, or a host label that is empty or longer than 63 chars
- containing an ellipsis (`…` or `...`) — truncated-paste signature
- glue signature: any uppercase letter in the host
  (e.g. `...orgPooja`; the `com|edu|gov|int|net|org` + `CapitalizedWord`
  variant is a special case of this)
"""

from __future__ import annotations

import re
from urllib.parse import urlsplit

ALLOWED_SOURCE_SCHEMES = frozenset({"http", "https"})

_HOSTNAME_RE = re.compile(r"[a-z0-9.-]+")
_UPPER_RUN_RE = re.compile(r"[A-Z]{2,}")
_GLUED_SUFFIX_RE = re.compile(r"(?:com|edu|gov|int|net|org)[A-Z][a-z]+$")
_ELLIPSIS_RE = re.compile(r"…|\.\.\.")


def invalid_source_reason(source: str) -> str | None:
    """Reason string if `source` looks broken, None if acceptable."""
    if not isinstance(source, str) or not source:
        return "not a non-empty string"
    if any(char.isspace() for char in source):
        return "contains whitespace"
    if _ELLIPSIS_RE.search(source):
        return "contains an ellipsis"
    try:
        parsed = urlsplit(source)
    except ValueError:
        return "not a parsable URL"
    if parsed.scheme not in ALLOWED_SOURCE_SCHEMES:
        return f"scheme is not http(s): {parsed.scheme!r}"
    host = parsed.netloc.rpartition("@")[2].partition(":")[0]
    if not host:
        return "no host"
    if not _HOSTNAME_RE.fullmatch(host):
        return f"host has characters outside [a-z0-9.-]: {host!r}"
    labels = host.split(".")
    if "." not in host or any(not label for label in labels):
        return f"host has no dot or an empty label: {host!r}"
    if any(len(label) > 63 for label in labels):
        return f"host label exceeds 63 chars: {host!r}"
    if _UPPER_RUN_RE.search(host) or _GLUED_SUFFIX_RE.fullmatch(labels[-1]):
        return f"host looks glued onto a domain: {host!r}"
    return None


def source_findings(rows: list[dict]) -> list[dict]:
    """One {'path', 'source', 'reason'} dict per invalid source across rows."""
    findings: list[dict] = []
    for row in rows:
        findings.extend(
            {"path": row["path"], "source": source, "reason": reason}
            for source in row["sources"]
            if (reason := invalid_source_reason(source)) is not None
        )
    return findings
