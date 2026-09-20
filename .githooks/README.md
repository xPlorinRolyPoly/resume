# Git Hooks (`.githooks`)

Custom Git hooks to automate repository maintenance, keep the **Graphify** knowledge graph updated, and automatically delete local feature branches once their Pull Request (PR) is merged.

---

## 🚀 Quick Setup (For New Clones)

Git does not automatically execute hooks from custom directories by default. When you clone this repository, run this one-time command from the repository root:

```bash
# 1. Tell Git to use this directory for hooks
git config core.hooksPath .githooks

# 2. Ensure all hook scripts are executable
chmod +x .githooks/*
```

That's it! Git will now run these hooks automatically.

---

## 📋 Included Hooks

### 1. `pre-push`
* **Trigger**: Runs automatically before `git push`.
* **Actions**:
  - Automatically runs `graphify update .` to re-extract and refresh the knowledge graph in `graphify-out/` before code is pushed to GitHub.
  - Runs merged branch cleanup.
  - If Graphify is not installed on the machine, it prints a friendly warning and allows the push to proceed.

### 2. `post-merge`
* **Trigger**: Runs automatically after `git pull` or `git merge`.
* **Actions**:
  - Prunes deleted remote branches (`git fetch -p origin`).
  - Detects local branches whose PR was merged and automatically deletes them to keep your local branch list clean.

### 3. `post-checkout`
* **Trigger**: Runs automatically when switching branches (e.g. `git checkout main` or `git switch main`).
* **Actions**:
  - Checks if the branch you just left was merged on GitHub, and automatically deletes it locally.

### 4. `cleanup-merged-branches.sh`
* **Purpose**: The shared engine script called by the hooks.
* **How it detects merged PRs**:
  1. Checks for remote-tracking branches marked `[gone]` after `git fetch -p`.
  2. Queries GitHub CLI (`gh pr list --state merged`) if `gh` is installed.
  3. Checks `git branch --merged main`.
* **Safety**: Never deletes protected branches (`main`, `master`, `dev`, `staging`, `production`, or the currently checked-out branch).

---

## 🛠️ Prerequisites (Optional but Recommended)

* **Graphify**: For updating the knowledge graph (`brew install graphify` or via python/pip).
* **GitHub CLI (`gh`)**: For direct PR status querying (`brew install gh` and `gh auth login`).

---

## 🧪 Manual Testing

You can test the hooks manually at any time:

```bash
# Test pre-push checks (Graphify update + branch cleanup)
./.githooks/pre-push

# Test merged branch cleanup directly
./.githooks/cleanup-merged-branches.sh
```

---

## 💡 Tips

* **Bypass hooks**: If you ever need to push without running the `pre-push` hook, use the `--no-verify` flag:
  ```bash
  git push --no-verify
  ```
* **Disable hooks**: To revert Git back to standard default hooks:
  ```bash
  git config --unset core.hooksPath
  ```
