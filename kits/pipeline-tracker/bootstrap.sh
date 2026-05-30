#!/bin/bash
# Copy the pipeline-tracker kit skills to the global ~/.claude/skills/ directory.
# Bash 3.2 compatible. No associative arrays, no mapfile, no [[ -v ]].
# Fail-safe: never overwrites existing files, never deletes anything.

set -e

KIT_ROOT="$(cd "$(dirname "$0")" && pwd)"
TARGET="$HOME/.claude/skills"

if [ ! -d "$TARGET" ]; then
  mkdir -p "$TARGET"
fi

echo "Installing pipeline-tracker kit skills to $TARGET ..."

# Copy skill files. The 'pipeline' skill ships in $KIT_ROOT/skills/.
# Each file is copied with -n equivalent (manual existence check) so an
# existing file is never overwritten.
SKILLS_DIR="$KIT_ROOT/skills"
if [ -d "$SKILLS_DIR" ]; then
  for f in "$SKILLS_DIR"/*; do
    [ -e "$f" ] || continue
    name=$(basename "$f")
    if [ -e "$TARGET/$name" ]; then
      echo "skip, already exists: $TARGET/$name"
    else
      cp -R "$f" "$TARGET/$name"
      echo "installed: $TARGET/$name"
    fi
  done
else
  echo "No global skills to install in this kit yet. Run \`claude\` in this folder."
fi

echo "Done."
echo ""
echo "To use the pipeline skill from any folder, open Claude Code and say:"
echo "  pipeline status"
