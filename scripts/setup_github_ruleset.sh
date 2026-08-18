#!/usr/bin/env bash
# Sets up GitHub Repository Ruleset on 'main' using gh CLI
set -e

REPO="mrxsierra/mrxsierra.github.io"
RULESET_FILE=".github/rulesets/main-protection.json"

if ! command -v gh >/dev/null 2>&1; then
    echo "Error: gh CLI is not installed. Visit https://cli.github.com/"
    exit 1
fi

echo "Configuring GitHub Ruleset for '$REPO'..."
gh api --method POST -H "Accept: application/vnd.github+json" \
  "/repos/$REPO/rulesets" \
  --input "$RULESET_FILE"

echo "✔ GitHub Ruleset successfully configured on '$REPO' for 'main' branch."
