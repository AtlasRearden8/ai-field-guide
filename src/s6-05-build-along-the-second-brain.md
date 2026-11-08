# 6.5 Build-along: the second brain
<!-- original: ch. 114 -->

By the end of this build, you will have a second brain that tidies itself. Ideas land in an inbox from your phone. AI sorts them into the right folders with tags and links. A weekly review writes itself. You can ask your notes questions like "What have I learned about sleep?"

Everything is plain Markdown files you own. **Markdown** is a simple text format with marks for headings and lists. Your notes work with any AI, today and in ten years.

Time: about two hours. Level: beginner-friendly.

## What you will build

A vault in Obsidian, with an inbox, folders, and AI rules. **Obsidian** is a free notes app that stores your notes as plain files on your computer. A **vault** is a folder of notes that Obsidian manages.

The flow is simple. You capture a note. It lands in the Inbox. AI triages it: it picks the right folder, adds tags, and links it to related notes. You ask questions across all your notes. Once a week, AI writes a review of what you learned.

## Before you start

You need three things.

- **Obsidian**, free, installed on your computer.
- **Claude Code or Claude Desktop**, to do the AI work. The vault works with any coding agent that reads Markdown.
- Optionally, **n8n or a phone shortcut** for voice capture.

Download the starter vault from the book's kit page if you have it. If not, you can build the folders by hand in ten minutes.

## Step 1: set up the vault, 10 minutes

Open Obsidian. Create a new vault. Call it "Second Brain." Pick a folder on your computer to store it in.

Inside the vault, create these folders.

- `Inbox` for new, unsorted notes.
- `Notes` for finished notes.
- `Projects` for active work.
- `Areas` for ongoing parts of life, such as health or money.
- `Resources` for reference material.
- `Journal` for daily notes.
- `Templates` for note templates.

Create a home page called `Home`. Link to each folder. This page is your front door. Open it every morning.

## Step 2: meet your vault's AI rules, 5 minutes

Open the file called `AGENTS.md` or `CLAUDE.md` in the vault. This file holds the AI rules for your vault. It tells the AI how to sort notes, how to tag them, and how to link them.

Read the rules. Change them to fit you. Add a rule about your tag style. Add a rule about how links should work. Add a rule that says "Never delete a note. Move it to the right folder instead."

The rules are the brain of the system. Good rules mean good sorting. Spend five minutes making them yours.

## Step 3: capture ten real things, 15 minutes

A second brain is useless without real notes. Capture ten real things right now.

Write a note about a book you read. Save a link to an article. Write down an idea for a project. Note a question you want to answer. Save a recipe. Write a meeting note. Capture a quote you like. List three things you learned this week. Save a travel idea. Write a note about a problem you are solving.

Put them all in the Inbox. Do not sort them yet. Messy is fine. The Inbox is supposed to be messy.

## Step 4: AI triage, 20 minutes

Open Claude Code in the vault folder. Say: "Triage the Inbox using the rules in AGENTS.md. Move each note to the right folder, add tags, and add links to related notes. Show me what you changed before you move anything."

Claude reads the rules. It reads each note. It proposes moves, tags, and links. Review the plan. If a move looks wrong, say so. Then let it run.

Check the result. Open a moved note. Does it have tags? Does it link to related notes? Does it sit in the right folder? Fix the rules when the AI gets something wrong. The rules get better each time you correct them.

> NOTE: Always ask the AI to show its plan before it moves files. Moving files is easy. Undoing a bad move is not. A plan you can review keeps you in charge.

## Step 5: ask your notes questions, 15 minutes

Now the fun part. Ask questions across your whole vault.

- "What have I learned about sleep?"
- "Summarise my notes on gardening."
- "What ideas have I saved about starting a business?"
- "Find any contradictions in my notes about diet."

Claude reads your notes and answers from them, with links to the source notes. This is your second brain talking back. It is the moment the system earns its name.

If an answer is thin, your notes are thin. Capture more. The brain only knows what you feed it.

## Step 6: one-tap voice capture, 30 minutes

Typing is slow. Voice is fast. Set up one-tap capture on your phone.

Option one: a phone shortcut. Tap it, speak your note, and the shortcut sends the text to your vault's Inbox. It can send through n8n, or save to a synced folder.

Option two: a voice memo. Record a memo, then ask AI to transcribe it and save it as a note. This takes longer but needs no setup.

Option three: message your Telegram bot, if you built Pip in chapter 6.3. Pip can save your message to the Inbox for you.

Pick one option. Test it with three real notes. If it takes more than ten seconds from tap to saved note, simplify it. Capture must be effortless, or you will stop doing it.

## Step 7: the self-writing weekly review, 10 minutes

Set up a weekly review that writes itself.

Ask Claude: "Write a weekly review from my Journal and Notes folders. Include three things I learned, three things I finished, and one thing to focus on next week. Save it as a note in the Journal folder, dated today."

Run it every Friday. Read it. Edit it. Over months, the reviews become a diary of your growth. You can ask questions across them too. "What have I focused on most this year?"

Automate it if you like. A scheduled n8n workflow can run the review every Friday and save it to your vault. Start by hand. Automate once the format is right.

## Step 8, optional: make it private and permanent

Your vault is plain files on your computer. That is already private. Make it permanent with two habits.

**Version history.** Put the vault in Git, or use Obsidian Sync, or back it up to cloud storage every day. **Git** is a system that tracks every change to your files. A backup means a lost laptop is an annoyance, not a disaster.

**Export regularly.** Once a month, export your vault as plain Markdown files to a backup folder. Your notes should survive any app, any company, and any decade.

## Troubleshooting

- **AI moves notes to the wrong folder.** Your rules are unclear. Add examples to AGENTS.md. Show the AI three notes and where each one belongs.
- **Links are missing.** Ask the AI to add links as part of triage. "Link each note to at least two related notes, or say why there are none."
- **The vault feels empty.** Capture more. Ten notes a day for a week fills a vault fast. A second brain needs food.
- **You stop capturing.** Your capture step is too hard. Simplify it to one tap. Remove every extra step.
- **Sync conflicts.** If you use cloud sync, let one device finish syncing before you open another. Conflicts come from editing the same note on two devices at once.

> TRY IT: Capture ten real notes today, then run the triage step. Tomorrow, ask your vault one question: "What have I learned this week?" Read the answer. That is your second brain, talking back.

## Check yourself

1. What is the Inbox for?
**Answer:** New, unsorted notes land there first, and AI sorts them later.

2. Why should AI show its triage plan before moving files?
**Answer:** Because moving files is easy and undoing a bad move is not, and a plan you can review keeps you in charge.

3. Why are plain Markdown files a good choice for a second brain?
**Answer:** Because they are files you own, and they work with any AI or app, today and in ten years.

4. What makes capture work in the long run?
**Answer:** It must be effortless, ideally one tap, or you will stop doing it.

## In short

- Set up an Obsidian vault with an Inbox, folders, and a home page.
- Write AI rules in AGENTS.md and make them yours.
- Capture ten real notes, then let AI triage them with a plan you review.
- Ask your notes questions and get answers with links to sources.
- Add one-tap voice capture so ideas never get lost.
- Let a weekly review write itself, and back the vault up.
