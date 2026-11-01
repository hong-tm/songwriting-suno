#!/usr/bin/env bash
# Install this skill into an agent skills directory.
#   ./install.sh                 -> ~/.agents/skills/songwriting-suno
#   ./install.sh /path/to/skills -> /path/to/skills/songwriting-suno
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_ROOT="${1:-$HOME/.agents/skills}"
DEST="$DEST_ROOT/songwriting-suno"

mkdir -p "$DEST_ROOT"

# Guard the removal: only replace nothing, or a previous install of this skill.
if [ -e "$DEST" ] && [ ! -f "$DEST/SKILL.md" ]; then
  echo "refusing to rm -rf $DEST: not empty and has no SKILL.md (not a songwriting-suno install); move it aside first" >&2
  exit 1
fi
rm -rf "$DEST"
mkdir -p "$DEST"

# Copy the bundle, skipping repo-dev artifacts.
tar -C "$SRC" -cf - --exclude=./.git --exclude=./.omo --exclude=__pycache__ . \
  | tar -C "$DEST" -xf -

# drop caches that may have been copied
find "$DEST" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true

echo "installed -> $DEST"
echo "restart opencode for the skill to load."
