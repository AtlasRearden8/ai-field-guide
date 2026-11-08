# 4.10 The Claude Code masterclass
<!-- original: ch. 62 -->

Claude Code is an AI coding agent. It reads your project, runs commands, edits files, tests its own work, and ships features. It lives in your terminal, in code editors, in a desktop app, on the web, and on your phone. And it is not just for code. People use it to organise files, study data, write documents, tend their notes, and automate their computers.

This chapter takes you from first install to a confident daily workflow. Chapter 4.11 covers the power-ups that come after. You do not need coding experience to start. You need a clear goal, and the habit of checking the result.

## Install and first launch

Claude Code is included in paid Claude plans, not the free plan. As of November 5, 2026, the paid plans were Pro at $20 a month, Max at $100 a month, and the newer Ultra plan at $200 a month. Check the current price on the Claude website before you buy. You can also use Claude Code with an API key, which charges you for what you use instead of a flat monthly price.

To install it, open your terminal and run the install command from the Claude Code website. Then type `claude` and press Enter. The first time it runs, it will ask you to sign in. Follow the prompts. It takes about two minutes.

Now open it inside a project folder. In the terminal, go to your project folder, and type `claude`. You will see a welcome screen and a prompt. That prompt is where you talk to Claude Code. Type in plain words, like you would to a colleague.

Your first message can be simple: "Look at this project and tell me what it does, in plain words." Claude Code will read the files, and answer. That first answer tells you a lot. If it understands your project, you are ready to build.

> NOTE: Claude Code works in the folder you open it in. It can read and change files in that folder, and in folders below it. Open it in the right folder, and keep unrelated projects in separate folders.

## Essential controls

You talk to Claude Code by typing. A few keys make life easier.

Press Enter to send a message. Press Escape to stop Claude Code while it is working. That is the most important key to learn. If it starts doing something you do not want, press Escape, and it stops.

Use the slash key to see commands. Typing `/` shows a menu of built-in commands, like `/help` for help, `/clear` to start a fresh conversation, and `/compact` to shrink a long conversation so it uses less memory.

You can also press Tab to switch between modes. The normal mode asks you before it changes files. There are modes that ask less, and modes that act more freely. Start in the normal mode. It asks before anything risky, and that is exactly what a beginner wants.

Claude Code can also show you pictures, run commands, and use tools you connect. You will learn those as you go. For now, remember Enter to send, Escape to stop, and slash for commands.

## The workflow that works: explore, plan, code, check, commit

Every good Claude Code session follows five steps. Learn them, and you will get good results from your first day.

**Explore.** Ask Claude Code to look at the project before it changes anything. "What files are here? What does this app do? Where does the login code live?" A few minutes of exploring saves an hour of fixing.

**Plan.** Ask for a plan, and wait for it before you say go. "Write a short plan for adding a search box. List the files you will change. Do not write any code yet." Read the plan. Fix the parts that are wrong. A plan you agree on is worth more than fast code.

**Code.** Say go. Let Claude Code write the code. Watch what it does. It will tell you which files it changed, and why.

**Check.** Ask it to check its own work. "Run the app and test the search box. Fix any errors you find." Then test it yourself. Click the button. Try the feature. Trust, but check.

**Commit.** Save a snapshot with Git, as you learned in Chapter 4.9. A short message, like "Add search box", is enough. Now the work is safe, and you can start the next feature.

Explore, plan, code, check, commit. Say it to yourself before each session. It is the whole masterclass in five words.

> TRY IT: Open Claude Code in any folder, even an empty one. Ask it: "Make me a simple web page that shows today's date and a random encouraging message, with a button to get a new message." Then follow the five steps: read its plan, let it build, ask it to check the page, and save a snapshot with Git.

## CLAUDE.md: your project's memory

Claude Code reads a special file called **CLAUDE.md** every time it starts in a folder. That file is your project's memory. It holds the facts Claude Code should always know.

Put four kinds of things in it. First, what the project is, in one paragraph. Second, how to run it, in one or two commands. Third, the rules you care about, like "use plain words in the interface" or "never delete a file without asking." Fourth, the things that are easy to get wrong, like "the login code lives in this file, not that one."

Keep it short. Ten to twenty lines is enough. Update it when you learn something new. A good CLAUDE.md makes every future session smarter, because Claude Code starts each time already knowing what matters.

You can also ask Claude Code to write the first version for you. Say: "Look at this project, then write a CLAUDE.md file that explains what it is, how to run it, and what to be careful about." Then read what it wrote, fix the mistakes, and keep it.

## Permissions and safety

Claude Code asks before it does risky things. That is by design. It will ask before it runs a command that changes files, before it installs something, and before it talks to the internet. Say yes when you understand the action. Say no, or ask for an explanation, when you do not.

You can set rules for what is always allowed and what is always blocked. For example, you can allow reading files, but block deleting them. You can allow running tests, but block sending email. Set these rules early, in plain words, and Claude Code will follow them.

Three safety rules to live by. First, never let Claude Code run in a folder with private files you would not want changed, like your whole Documents folder. Work in a project folder, not your whole computer. Second, never paste a password or an API key into the chat. Use a secrets file, as Chapter 4.14 explains. Third, check anything that leaves your computer, like an email or a published page, before it goes out.

## Context management: the hidden skill

Claude Code has a working memory, called its **context**. It holds your conversation, the files it has read, and the work it has done. That memory is limited. When it fills up, Claude Code starts to forget, and its work gets worse.

You can see how full the memory is. Watch the indicator in the interface. When it gets high, use the `/compact` command. That command shrinks the conversation into a short summary, and frees up room. It keeps the important facts and drops the detail.

Three habits keep the memory healthy. First, start a fresh conversation for each new feature, with `/clear`. Second, keep your CLAUDE.md short, because it loads every time. Third, do not paste huge files into the chat. Ask Claude Code to read the file itself, so it takes only what it needs.

## Non-coding superpowers

Claude Code is called a coding tool, but it is really a computer helper that happens to be good at code. Here are jobs people use it for that have nothing to do with programming.

Organise a messy folder. "Sort these 200 photos into folders by month." Study a spreadsheet. "Read this CSV file and tell me the three biggest trends, in plain words." Write and edit documents. "Turn these notes into a one-page summary." Tend a notes vault. "Find all my notes about gardening, and list the open questions." Automate your computer. "Write me a small script that backs up this folder every day."

Try one of these this week, in a copy of your files, not the originals. You will see that Claude Code is a general helper, not just a code tool.

> NOTE: Always try non-coding jobs on a copy of your files first. It is easy to make a copy. It is hard to un-sort a folder you did not mean to sort.

## Twenty pro tips, in short

You do not need to memorise these. Skim them, and come back when you need one.

1. Start each feature with a fresh conversation.
2. Ask for a plan before you say go.
3. Give the agent one job at a time.
4. Tell it how to check its work.
5. Use Escape to stop it at any time.
6. Use `/compact` when the memory gets full.
7. Keep your CLAUDE.md short and current.
8. Commit with Git before big changes.
9. Let it read files itself, instead of pasting them.
10. Ask it to explain code you do not understand.
11. Ask it to write tests for new features.
12. Say what "done" looks like, in plain words.
13. Give it examples of what you like.
14. Name things clearly, so the agent can find them.
15. Keep your project folder tidy.
16. Review the diff before you commit.
17. Try the app yourself, every time.
18. Save good prompts as slash commands, as Chapter 4.11 shows.
19. If it gets stuck, ask it to explain what it tried, then start fresh.
20. When in doubt, make the task smaller.

## Check yourself

1. What is the five-step workflow for working with Claude Code?
**Answer:** Explore, plan, code, check, commit.

2. What is CLAUDE.md?
**Answer:** A special file in your project folder that Claude Code reads every time it starts, holding the facts and rules it should always know.

3. What does pressing Escape do?
**Answer:** It stops Claude Code while it is working.

4. Why should you use `/compact`?
**Answer:** Because it shrinks a long conversation into a summary, freeing up working memory so Claude Code keeps working well.

5. Why should you work in a project folder, not your whole Documents folder?
**Answer:** Because Claude Code can read and change files in the folder you open it in, so a narrow folder limits what it can touch.

## In short

- Claude Code is an AI coding agent that reads, writes, runs, and checks work in your project folder.
- Follow the five steps: explore, plan, code, check, commit.
- Write a short CLAUDE.md so every session starts with the facts that matter.
- Let it ask before risky actions, and keep it in a project folder, not your whole computer.
- Watch the memory, use `/compact` when it fills up, and start fresh for each feature.
- It is not just for code: it can organise files, study data, and write documents too.
