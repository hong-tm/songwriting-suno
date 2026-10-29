#!/usr/bin/env bash
# Install this skill into an agent skills directory.
#   ./install.sh                 -> ~/.agents/skills/songwriting-suno
#   ./install.sh /path/to/skills -> /path/to/skills/songwriting-suno
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_ROOT="${1:-$HOME/.agents/skills}"
DEST="$DEST_ROOT/songwriting-suno"

mkdir -p "$DEST_ROOT"
rm -rf "$DEST"
cp -R "$SRC" "$DEST"

# drop caches that may have been copied
find "$DEST" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true

echo "installed -> $DEST"
echo "restart opencode for the skill to load."
