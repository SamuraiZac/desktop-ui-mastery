#!/usr/bin/env bash
#
# Desktop UI Mastery — universal installer.
#
#   curl -fsSL https://raw.githubusercontent.com/SamuraiZac/desktop-ui-mastery/main/install.sh | bash
#
# Clones the library once to ~/.desktop-ui-mastery, then wires it into every
# AI coding tool it can find. Re-run any time to update (git pull + re-link).
#
# Targets (auto-detected; override with flags or DUIM_TOOLS=claude,codex):
#   --claude   Claude Code   -> ~/.claude/skills (auto-invoked skill)
#   --codex    OpenAI Codex  -> ~/.codex/prompts + ~/.codex/AGENTS.md
#   --agents   Any AGENTS.md tool (Cursor, Gemini CLI, Amp, ...) -> ./AGENTS.md
#   --all      All of the above
#
set -euo pipefail

REPO_URL="${DUIM_REPO_URL:-https://github.com/SamuraiZac/desktop-ui-mastery.git}"
CLONE_DIR="${DUIM_HOME:-$HOME/.desktop-ui-mastery}"
SKILL_REL="skills/desktop-ui-mastery"

BOLD=$'\033[1m'; DIM=$'\033[2m'; GRN=$'\033[32m'; YEL=$'\033[33m'; RST=$'\033[0m'
say()  { printf '%s\n' "$*"; }
ok()   { printf '%s✓%s %s\n' "$GRN" "$RST" "$*"; }
warn() { printf '%s!%s %s\n' "$YEL" "$RST" "$*"; }
step() { printf '\n%s%s%s\n' "$BOLD" "$*" "$RST"; }

# --- parse args --------------------------------------------------------------
TOOLS=""
for a in "$@"; do
  case "$a" in
    --claude) TOOLS="$TOOLS claude" ;;
    --codex)  TOOLS="$TOOLS codex" ;;
    --agents) TOOLS="$TOOLS agents" ;;
    --all)    TOOLS="claude codex agents" ;;
    -h|--help)
      grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) warn "unknown flag: $a" ;;
  esac
done
[ -z "$TOOLS" ] && [ -n "${DUIM_TOOLS:-}" ] && TOOLS="${DUIM_TOOLS//,/ }"

# Auto-detect when nothing was requested.
if [ -z "$TOOLS" ]; then
  [ -d "$HOME/.claude" ] && TOOLS="$TOOLS claude"
  [ -d "$HOME/.codex" ]  && TOOLS="$TOOLS codex"
  if [ -z "$TOOLS" ]; then
    warn "No Claude Code or Codex install detected."
    say  "Installing the library only. Re-run with --claude, --codex, or --agents to wire a tool."
  fi
fi

command -v git >/dev/null 2>&1 || { warn "git is required."; exit 1; }

# --- clone / update ----------------------------------------------------------
step "Fetching Desktop UI Mastery"
if [ -d "$CLONE_DIR/.git" ]; then
  git -C "$CLONE_DIR" pull --ff-only --quiet && ok "Updated $CLONE_DIR"
else
  git clone --depth 1 --quiet "$REPO_URL" "$CLONE_DIR" && ok "Cloned to $CLONE_DIR"
fi
SKILL_SRC="$CLONE_DIR/$SKILL_REL"
[ -f "$SKILL_SRC/SKILL.md" ] || { warn "SKILL.md missing at $SKILL_SRC"; exit 1; }

# --- Claude Code -------------------------------------------------------------
install_claude() {
  step "Claude Code"
  local dir="$HOME/.claude/skills"
  mkdir -p "$dir"
  local dest="$dir/desktop-ui-mastery"
  if [ -e "$dest" ] || [ -L "$dest" ]; then rm -rf "$dest"; fi
  ln -s "$SKILL_SRC" "$dest"
  ok "Skill linked: $dest"
  say "${DIM}  Auto-invokes on desktop-UI requests in your next session.${RST}"
  say "${DIM}  For the /ui-critique /ui-deslop /ui-envision commands + auto-lint hook,${RST}"
  say "${DIM}  install as a plugin instead:${RST}"
  say "${DIM}    /plugin marketplace add SamuraiZac/desktop-ui-mastery${RST}"
  say "${DIM}    /plugin install desktop-ui-mastery${RST}"
}

# --- Codex -------------------------------------------------------------------
install_codex() {
  step "Codex"
  local pdir="$HOME/.codex/prompts"
  mkdir -p "$pdir"
  # Turn each Claude command into a Codex prompt: resolve the plugin-root token
  # to the real clone path and pin relative reference reads to the skill dir.
  for f in "$CLONE_DIR"/commands/*.md; do
    [ -e "$f" ] || continue
    local name; name="$(basename "$f")"
    {
      printf 'The Desktop UI Mastery library lives at %s. Read files there as needed; relative paths like references/... and scripts/... are under that directory.\n\n' "$SKILL_SRC"
      sed -e "s#\${CLAUDE_PLUGIN_ROOT}/skills/desktop-ui-mastery#$SKILL_SRC#g" \
          -e "s#\${CLAUDE_PLUGIN_ROOT}#$SKILL_SRC#g" "$f"
    } > "$pdir/$name"
  done
  ok "Prompts installed: $pdir/ui-*.md  (use /ui-critique, /ui-deslop, /ui-envision)"
  write_agents_block "$HOME/.codex/AGENTS.md"
  ok "Pointer added to ~/.codex/AGENTS.md"
}

# --- Generic AGENTS.md (Cursor, Gemini CLI, Amp, Cline, ...) ------------------
install_agents() {
  step "AGENTS.md (generic)"
  write_agents_block "$PWD/AGENTS.md"
  ok "Pointer added to $PWD/AGENTS.md"
  say "${DIM}  Any agent that reads AGENTS.md will now load the skill for UI work.${RST}"
}

# Idempotently insert a marked block that points the agent at the skill.
write_agents_block() {
  local file="$1"
  local begin="<!-- BEGIN desktop-ui-mastery -->"
  local end="<!-- END desktop-ui-mastery -->"
  mkdir -p "$(dirname "$file")"
  [ -f "$file" ] || : > "$file"
  # Strip any previous block, then append a fresh one.
  if grep -qF "$begin" "$file" 2>/dev/null; then
    sed -i.bak "/$begin/,/$end/d" "$file" && rm -f "$file.bak"
  fi
  {
    printf '%s\n' "$begin"
    printf '## Desktop UI Mastery\n\n'
    printf 'When the user wants to design, build, redesign, critique, deslop, or imagine a\n'
    printf 'desktop app UI (app shell, dashboard, data table, command palette, settings,\n'
    printf 'Electron/Tauri app), read and follow the skill at:\n\n'
    printf '    %s/SKILL.md\n\n' "$SKILL_SRC"
    printf 'It routes to reference files, exemplars, and scripts in that directory.\n'
    printf '%s\n' "$end"
  } >> "$file"
}

# --- run ---------------------------------------------------------------------
for t in $TOOLS; do
  case "$t" in
    claude) install_claude ;;
    codex)  install_codex ;;
    agents) install_agents ;;
  esac
done

step "Done"
ok "Library: $CLONE_DIR"
say "Update any time by re-running this installer."
