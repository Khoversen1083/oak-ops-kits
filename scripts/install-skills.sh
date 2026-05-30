#!/usr/bin/env bash
# install-skills.sh — copy all Oak Ops skills into ~/.claude/skills/.
# Idempotent. Safe to re-run. Backs up any pre-existing skill with same name.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$REPO_ROOT/skills"
SKILLS_DST="$HOME/.claude/skills"
BACKUP_DIR="$HOME/.claude/skills/_oak-ops-backup-$(date +%Y%m%d-%H%M%S)"

mkdir -p "$SKILLS_DST"

echo "Installing Oak Ops skills from $SKILLS_SRC to $SKILLS_DST"
echo ""

installed=0
backed_up=0

for skill_dir in "$SKILLS_SRC"/*/; do
  name=$(basename "$skill_dir")
  dst="$SKILLS_DST/$name"

  if [[ -d "$dst" ]]; then
    mkdir -p "$BACKUP_DIR"
    mv "$dst" "$BACKUP_DIR/$name"
    backed_up=$((backed_up + 1))
    echo "  backup: $name -> $BACKUP_DIR/$name"
  fi

  cp -R "$skill_dir" "$dst"
  installed=$((installed + 1))
  echo "  install: $name"
done

echo ""
echo "Done. Installed $installed skills."
if [[ $backed_up -gt 0 ]]; then
  echo "Backed up $backed_up pre-existing skills to $BACKUP_DIR"
fi
echo ""
echo "Restart Claude Code to pick up the new skills."
echo "Invoke by saying what you want, e.g. \"scrape google maps for concrete contractors in austin\"."
