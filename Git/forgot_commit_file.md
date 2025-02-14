## Forgot to commit the file
> For example, I forgot to commit the `settings.py` file in Django project when I created a Cart app.

### 1️⃣ **Amend the last commit (if not pushed yet)**

If I haven't pushed my commit yet, I can **amend it** to include the `settings.py` change:

```
git add django_project/settings.py
git commit --amend --no-edit
```

✅ This updates the last commit without changing the commit message.

### 👉 Step-by-step breakdown:

▶ `git add django_project/settings.py`

- This stages the `settings.py` file (just like a normal commit).

▶ `git commit --amend --no-edit`

- This takes the last commit and adds the newly staged changes to it.
- `--no-edit` keeps the existing commit message.
- The result is one commit that now contains both the original files (Cart app setup) and the missing `settings.py` change.

👉 The end result:

- Instead of two commits (`1: Initial Cart app setup` and `2: Register cart in settings`), I'll have only one commit that includes both changes.
- Since I haven't pushed yet, there are no complications—my history stays clean! 🚀

---

### 2️⃣ **Rebase Interactive (if already pushed but still want a clean history)**

If I've **already pushed** the commit but still want a single commit, I can:

```
git add django_project/settings.py
git commit --amend --no-edit
git push --force
```

⚠️ **Be careful with `--force`**, especially if working with others—it rewrites history!

---

### 3️⃣ **Soft Reset & Recommit (if I've made multiple commits)**

If I've already made the second commit but want to **combine them into one**, I can:

```
git reset --soft HEAD~1
git add .
git commit --amend --no-edit
```

✅ This takes my last commit and the new change, merges them, and keeps everything clean in a single commit.

### 👉 Step-by-step breakdown:

▶ `git reset --soft HEAD~1`

- This removes the last commit but keeps all the changes in my working directory and staging area.
- My files are still there, just not committed anymore.

▶ `git add .`

- The dot (`.`) stages all modified and new files, including `settings.py`.

▶ `git commit -m "Initial Cart app setup"`

- Now I have a fresh commit that correctly includes all files related to setting up the Cart app.
- The previous incorrect commit is gone and replaced with this new one.

👉 The end result:

- I still have only one commit, and it correctly contains everything related to the initial Cart app setup.
