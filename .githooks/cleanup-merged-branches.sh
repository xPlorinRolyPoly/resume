#!/usr/bin/env bash
# Cleanup local branches whose PRs are merged or tracking branch is gone

set -e

# Ensure git repo
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

current_branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "")
default_branch=$(git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || echo "")
[ -z "$default_branch" ] && default_branch="main"

# Prune remote tracking references
git fetch -p origin >/dev/null 2>&1 || true

# Gather candidate branches to delete
branches_to_delete=()

# 1. Check branches whose upstream remote tracking branch is [gone]
while IFS= read -r branch; do
    [ -n "$branch" ] && branches_to_delete+=("$branch")
done < <(git branch -vv | grep ': gone]' | awk '{print $1}' | sed 's/^[ *+]*//')

# 2. Check branches with merged PRs via GitHub CLI (gh) if available
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
    while IFS= read -r branch; do
        [ -n "$branch" ] && branches_to_delete+=("$branch")
    done < <(gh pr list --state merged --limit 100 --json headRefName --jq '.[].headRefName' 2>/dev/null || true)
fi

# 3. Check branches fully merged into default_branch
while IFS= read -r branch; do
    [ -n "$branch" ] && branches_to_delete+=("$branch")
done < <(git branch --merged "$default_branch" 2>/dev/null | sed 's/^[ *+]*//' || true)

# Protected branches that must never be deleted
protected_branches=("main" "master" "dev" "development" "staging" "production" "$current_branch")

# Deduplicate branches
if [ ${#branches_to_delete[@]} -gt 0 ]; then
    unique_branches=($(printf "%s\n" "${branches_to_delete[@]}" | sort -u))

    for branch in "${unique_branches[@]}"; do
        [ -z "$branch" ] && continue
        is_protected=0
        for prot in "${protected_branches[@]}"; do
            if [ "$branch" = "$prot" ]; then
                is_protected=1
                break
            fi
        done
        [ $is_protected -eq 1 ] && continue

        # Check if branch exists locally
        if git show-ref --verify --quiet "refs/heads/$branch"; then
            echo "[git-hook] PR for '$branch' is merged. Deleting local branch..."
            git branch -D "$branch" 2>/dev/null || git branch -d "$branch" 2>/dev/null || true
            echo "[git-hook] Successfully deleted local branch '$branch'."
        fi
    done
fi
