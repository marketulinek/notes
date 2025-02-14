## Forgot to commit the file

### 1️⃣ **Amend the last commit (if not pushed yet)**

If you haven't pushed your commit yet, you can **amend it** to include the `settings.py` change:

```
git add django_project/settings.py
git commit --amend --no-edit
```

✅ This updates the last commit without changing the commit message.

---

### 2️⃣ **Rebase Interactive (if already pushed but still want a clean history)**

If you've **already pushed** the commit but still want a single commit, you can:

```
git add django_project/settings.py
git commit --amend --no-edit
git push --force
```

⚠️ **Be careful with `--force`**, especially if working with others—it rewrites history!

---

### 3️⃣ **Soft Reset & Recommit (if you've made multiple commits)**

If you've already made the second commit but want to **combine them into one**, you can:

```
git reset --soft HEAD~1
git add .
git commit --amend --no-edit
```

✅ This takes your last commit and the new change, merges them, and keeps everything clean in a single commit.
