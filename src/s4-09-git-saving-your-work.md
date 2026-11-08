# 4.9 Git: saving your work
<!-- original: ch. 61 -->

Git is an undo button for your whole project. When a coding agent rewrites twenty files and something breaks, Git lets you rewind with one command. When an idea does not work out, Git lets you throw it away and go back to the version that did work.

You need no account to use Git. You need no website. Everything in this chapter works on your own computer, in your own folders. Git is free, and it is already the standard tool that every professional uses. Learn it now, and every build in this book gets safer.

## Why AI builders need Git

AI builders change a lot of files very fast. That speed is wonderful until it is not. An agent can delete a file you needed. It can rewrite a page that was working fine. It can make ten changes, and you cannot remember which one broke everything.

Git solves that. Every time you save a snapshot, Git records the exact state of every file. Later, you can look at what changed, go back to any snapshot, or try an idea on a safe side copy while the good version stays untouched.

Think of Git as a time machine for your project, plus a safety net. You take a snapshot when things work. You try something new. If it works, you take another snapshot. If it fails, you rewind. No fear. No lost work.

> NOTE: Save a snapshot before you ask an AI agent to make a big change. That one habit will save you more time than any other skill in this chapter.

## The ten ideas that explain all of Git

Git has a small set of ideas. Learn these ten, and the rest is detail.

A **repository** is a project folder that Git watches. People call it a repo for short. One folder, one repo.

A **commit** is a snapshot. It is a saved state of your project, with a short message that says what changed. "Add login page" is a good message. "Stuff" is not.

The **working directory** is the files as they are right now, on your disk. The **staging area** is a waiting room. You put files there to say "include these in the next snapshot." The **history** is the list of all your snapshots, in order.

A **branch** is a parallel copy of your project. The main branch is usually called **main**. It holds the version that works. You make a new branch when you want to try an idea safely. If the idea works, you merge it back into main. If it fails, you delete the branch, and main is untouched.

A **merge** is joining one branch back into another. A **conflict** is what happens when two branches changed the same lines in different ways. Git asks you to pick which version to keep. Conflicts sound scary. They are normal, and they are fixable.

**HEAD** is Git's way of saying "you are here." It points to the snapshot you are looking at right now. You rarely need to think about it, but you will see the word in messages.

A **remote** is a copy of your repo that lives somewhere else, like on a server. A **code host** is a website that stores remotes for you, such as GitHub, GitLab, or Codeberg. A remote is optional. Git works perfectly well with no remote at all. This book never requires you to make an account on any code host. If you want a backup online one day, you can add a remote then. Until then, everything here is local.

## Setup in ten minutes

First, install Git. On a Mac, open the terminal and type `git --version`. If Git is missing, your Mac will offer to install it. On Windows, download Git from its official website and run the installer. On Linux, use your system's package manager. All of these are free.

Next, tell Git who you are. Open the terminal and type these two commands, using your own name and email:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

The first line sets your name. The second sets your email. Git writes these into each snapshot you make, so you can see who saved what.

Now make your first repo. Go into a project folder in the terminal, and type `git init`. That one command turns the folder into a repo. Git creates a hidden folder to store its records. You will not see it, and you do not need to touch it.

> TRY IT: Make a practice folder on your Desktop called `git-practice`. Open the terminal, go into that folder, and type `git init`. Then type `git status`. Git will tell you it is watching an empty folder. You have just made your first repo.

## Your daily loop: save, check, share

You will use four commands, every day. Learn them in order.

First, **check**. Type `git status`. Git tells you which files changed, which files are new, and which files are waiting in the staging area. Run this command often. It is your dashboard.

Second, **stage**. Type `git add .` to put all changed files in the waiting room. The dot means "everything in this folder." Or type `git add filename` to stage one file only. Staging says "include this in the next snapshot."

Third, **commit**. Type `git commit -m "Your message here"`. The `-m` means the message follows. Write messages that a future you will understand. "Add shopping list page" is good. "Fix the bug where the total was wrong" is good. "Update" is not.

Fourth, **look back**. Type `git log --oneline` to see your snapshots as a short list. Each line shows a short code and a message. That list is your project's memory.

That is the whole daily loop: status, add, commit, log. Four commands. Use them every time you finish a piece of work, and you will never lose good work again.

```
git status
git add .
git commit -m "Add shopping list page"
git log --oneline
```

Line one checks what changed. Line two stages everything. Line three saves a snapshot with a message. Line four shows your list of snapshots.

## Branches: safe experiments

Branches are how you try ideas without fear. Here is the pattern.

You are on main, and everything works. You want to try a dark mode for your app. Type `git branch dark-mode` to make a new branch called dark-mode. Then type `git checkout dark-mode` to switch to it. Or use one command that does both: `git checkout -b dark-mode`.

Now make your changes. Commit them. The main branch is untouched. Your dark-mode work lives only on its own branch. If you decide you love it, switch back to main and merge it in:

```
git checkout main
git merge dark-mode
```

If you decide you hate it, just delete the branch and carry on:

```
git branch -d dark-mode
```

The main branch never knew it existed. That is the power of branches. Try anything. Keep what works. Throw away the rest.

Branches are also how you run coding agents safely. Give each agent its own branch. Let it work there. Review the changes. Merge only what is good. Some people run several agents at once, each on its own branch, and pick the best result. Git makes that possible.

## Git and coding agents: the perfect partnership

Here is the workflow the professionals use, and you can use it from day one.

Before the agent starts, commit your work. Now you have a clean snapshot. Tell the agent to work on a new branch. Let it make its changes. When it finishes, run `git status` and `git diff` to see what changed. The `diff` command shows you the exact lines that were added and removed.

Read the agent's summary. Test the app. If it works, commit the changes with a clear message. If it does not work, you can rewind with one command: `git checkout .` throws away all unsaved changes, and `git reset --hard` takes you back to the last snapshot. Both are powerful. Both deserve care, because they throw work away. Only use them when you have a snapshot to go back to.

> NOTE: `git checkout .` and `git reset --hard` throw away unsaved work for good. Use them only when you are sure, and only when you have a snapshot saved. When in doubt, commit first, then experiment.

## The rescue guide

Things go wrong. Here is how to fix the four most common problems.

You committed too early, and you want to change the message. Type `git commit --amend -m "Better message"`. This rewrites the last snapshot. Only do this before you have shared the snapshot with anyone.

You changed a file and you regret it. Type `git checkout -- filename` to put that one file back to its last snapshot. Or type `git checkout .` to put all files back. Remember, this throws away unsaved work.

You committed something and you want to undo the whole snapshot, but keep the files. Type `git reset --soft HEAD~1`. That moves the history back one snapshot, but leaves your files as they are. You can then commit again, better.

You saved a secret by mistake, like a password or an API key. This one needs care. First, remove the secret from the files. Then commit the fix. But the secret is still in the history, so anyone with the history can find it. You must also change the secret itself, so the old one stops working. Get a new API key, or change the password. And add the file that held the secret to a file called `.gitignore`, which tells Git to never save that file. The rule is simple: secrets never go in Git, and a leaked secret must be replaced, not just deleted.

## Optional extras from an online host

You do not need any of this. But one day, you may want it, so here is what it is.

A code host stores a copy of your repo online. That copy is a backup. It is also a way to share your work, or to work with other people. To use one, you make an account, make an empty repo on the site, and link it to your local repo with one command. Then `git push` sends your snapshots up, and `git pull` brings new ones down.

Some hosts add extras. They can run checks on your code every time you save. They can host a simple website for free. They can take **review requests**, which are formal asks for another person to look at your changes before they are merged. These are called pull requests on GitHub, and merge requests on GitLab. They are how teams review AI-made changes: the agent opens a request, a human reads the changes, and only then does the work go into main.

All of this is optional. Git itself needs no account, no website, and no internet. Start local. Add a host only when you have a reason.

## Check yourself

1. What is a commit?
**Answer:** A commit is a snapshot of your project, saved with a short message that says what changed.

2. What is a branch?
**Answer:** A branch is a parallel copy of your project where you can try an idea safely without touching the main version.

3. What does `git status` do?
**Answer:** It shows which files changed, which are new, and which are staged for the next snapshot.

4. Do you need an account on a code host to use Git?
**Answer:** No. Git works fully on your own computer, with no account and no internet. A host is an optional extra.

5. What should you do if you save a secret in Git by mistake?
**Answer:** Remove it from the files, commit the fix, replace the secret itself with a new one, and add its file to .gitignore so it never gets saved again.

## In short

- Git is an undo button and a time machine for your whole project.
- The daily loop is status, add, commit, log.
- Save a snapshot before you ask an AI agent to make a big change.
- Branches let you try ideas safely, and merge only what works.
- Git needs no account and no internet; a code host is an optional backup.
- Secrets never go in Git, and a leaked secret must be replaced.
