#!/usr/bin/env bash
# Install this skill into an agent skills directory.
#   ./install.sh                 -> ~/.agents/skills/songwriting-suno
#   ./install.sh /path/to/skills -> /path/to/skills/songwriting-suno
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_ROOT="${1:-$HOME/.agents/skills}"
DEST="$DEST_ROOT/songwriting-suno"

mkdir -p "$DEST_ROOT"

# Guard the removal: refuse the source tree itself, and replace only an
# empty target or a previous install of THIS skill.
if [ "$DEST" = "$SRC" ]; then
  echo "refusing to install into the source tree itself: $DEST" >&2
  exit 1
fi
if [ -e "$DEST" ] && [ ! -f "$DEST/SKILL.md" ]; then
  echo "refusing to rm -rf $DEST: it exists without a SKILL.md (not a skill install); move it aside first" >&2
  exit 1
fi
if [ -f "$DEST/SKILL.md" ] && ! grep -q '^name: songwriting-suno$' "$DEST/SKILL.md"; then
  echo "refusing to rm -rf $DEST: SKILL.md is a different skill (name is not songwriting-suno); move it aside first" >&2
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
