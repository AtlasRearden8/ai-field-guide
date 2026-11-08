# 4.11 Claude Code power-ups
<!-- original: ch. 63 -->

Out of the box, Claude Code is brilliant. Set up your way, it is a whole team. This chapter covers the power-user layer: custom slash commands, skills, subagents, hooks, MCP servers, plugins, output styles, headless mode, scheduled automation, and the Agent SDK.

You do not need any of these to use Claude Code well. Each one solves a specific pain. Learn them when the pain appears. If you catch yourself giving the same instruction for the fifth time, that is the moment to reach for this chapter.

## The power-up map

Here is the map, in one table. Each row is one power-up, and the pain it solves.

| Power-up | It solves | When to use it |
| --- | --- | --- |
| Slash command | Typing the same prompt again | A prompt you use every week |
| Skill | Teaching a whole way of working | A repeatable job with rules |
| Subagent | One long task that needs focus | Research, review, or a big search |
| Hook | A rule you always want enforced | "Always run the tests first" |
| MCP server | Reaching apps outside the folder | Your notes, your calendar, your data |
| Plugin | Sharing a set of power-ups | A setup you want to reuse or share |
| Headless mode | Running Claude Code from a script | Automation, not chat |
| Agent SDK | Building Claude Code into your own app | You are building software for others |

Read the rows that match a pain you feel. Skip the rest for now.

## Custom slash commands

A **slash command** is a saved prompt you can run with a short command. Instead of typing "Review this code for bugs, check the error handling, and list what you find, in plain words" for the tenth time, you type `/review` and it runs.

To make one, create a file in the `.claude/commands` folder inside your project, named after the command. A file called `review.md` becomes the command `/review`. Inside the file, write the prompt, in plain words. You can leave blanks for the agent to fill in, like "Review this file: $ARGUMENTS", where the words you type after the command fill in the blank.

Start with three commands. One for reviewing code. One for writing tests. One for explaining a file in plain words. Those three alone will save you hours.

> NOTE: Keep slash commands short. A command that is a page long is hard to remember and hard to fix. If a command grows, it probably wants to be a skill instead.

## Skills: packaged expertise

A **skill** is a small package of instructions that loads only when the job needs it. Think of it as a recipe card. The agent does not read every recipe before it cooks. It pulls out the card for the dish it is making.

A skill has three parts. A short description, so the agent knows when to use it. A set of instructions, which is the body of the skill. And sometimes helper files, like templates or examples. Skills live in a folder, and Claude Code finds them when the job matches their description.

Here is a skill worth building first: a "write a blog post" skill. Its description says "Use this when the user asks for a blog post." Its instructions say the tone you like, the length you want, and the structure you prefer. From then on, every blog post comes out in your voice, without you repeating the rules each time.

Skills are also how teams share good practice. One person writes a skill for "how we review code here." Everyone else installs it. The whole team gets better at once.

## Subagents: your specialist team

A **subagent** is a helper agent that the main agent can send work to. It has its own task, its own memory, and its own focus. When it finishes, it reports back with a summary.

Use subagents when one job needs deep focus, or when you want two jobs done at the same time. Good examples: "Search the whole project for every place we handle passwords, and report what you find." Or "Read these ten documents and summarise the disagreements." The main agent keeps working on your feature, while the subagent does the research.

Subagents are also good for review. Ask a subagent to review the main agent's work, as if it were a careful colleague. It will catch things the main agent missed, because it reads the work with fresh eyes.

Keep subagents focused. One job, clearly stated. A subagent with a vague job will wander, just like a person would.

## Hooks: automatic guardrails

A **hook** is a rule that runs automatically at a set moment. For example, a hook can run every time Claude Code is about to edit a file, or every time it finishes a task. It can check something, block something, or just log what happened.

Useful hooks for beginners: a hook that runs the tests after every change, and blocks the finish until the tests pass. A hook that stops Claude Code from editing files with secrets in them. A hook that writes a short log of what changed, so you can read it later.

Hooks are small scripts, and you can ask Claude Code to write them for you. Say: "Write me a hook that runs the tests after every code change, and tells me if they fail." It will write the hook, explain it, and install it. You do not need to write the script by hand.

> TRY IT: Ask Claude Code to write you one hook: "After every change, check that no file contains the words password or API key in plain text, and warn me if one does." Test it by adding a fake secret to a test file, and watch the hook catch it.

## MCP in Claude Code

**MCP** is a standard plug that lets AI use your tools, which you met in Chapter 2.20. In Claude Code, MCP servers add tools that reach outside your project folder.

For example, an MCP server for your notes app lets Claude Code search your notes. An MCP server for your database lets it ask questions of your data. An MCP server for a web browser lets it fetch pages and check them.

To add one, you tell Claude Code the server's name and how to start it. Many servers are one command to install. Once it is connected, the tools appear in Claude Code's toolbox, and the agent can use them like any other tool.

Be careful about which MCP servers you connect. A server can act in the app it connects to. Only connect servers you trust, from sources you recognise. Chapter 2.24 covers MCP safety in full, and it is worth reading before you connect a powerful server.

## Plugins and marketplaces

A **plugin** is a bundle of power-ups: slash commands, skills, subagents, and hooks, packed together so you can install them in one step. A **marketplace** is a place where people share plugins.

If you build a good setup for your team, turn it into a plugin. Then your whole team can install it with one command, instead of copying files by hand. If you find a plugin that matches your work, install it, try it for a week, and keep only the parts you use.

## Output styles, status line, and other comforts

Small settings make long sessions nicer. **Output styles** change how Claude Code talks to you. You can ask for short answers, or for detailed ones. You can ask it to explain its thinking, or just to show the result.

The **status line** is the small bar that shows what Claude Code is doing, and how full its memory is. Keep an eye on it. When the memory gets full, use `/compact`, as Chapter 4.10 explained.

You can also set a default mode for how much Claude Code asks before it acts. Start strict, and loosen it only when you trust the setup. A strict tool that asks is better than a loose tool that surprises you.

## Headless mode and scripting

**Headless mode** means running Claude Code without the chat window. You give it a task as a command, it does the task, and it prints the result. No conversation. No waiting.

This is useful for automation. A script can run Claude Code every night to tidy a folder, summarise a file, or check a project for errors. You write the task once, and the computer runs it on a schedule.

To try it, run Claude Code from the terminal with a prompt as an argument, and the flag that tells it to print the answer and exit. Test it on a small, safe job first, like summarising a file. When it works, you can put it in a scheduled task, as the next section shows.

## Claude Code in scheduled automation

You can run Claude Code on a schedule, from your own computer. This is called **host-based** automation, because it runs on a host, which is just a computer that stays on.

A simple setup: a scheduled task on your computer runs a command each morning. That command runs Claude Code in headless mode, with a task like "Read the notes from yesterday, and write a three-line summary." The summary goes into a file, or into your inbox.

Keep scheduled jobs small and safe. Let them read and write files in one project folder. Do not let them send email, spend money, or delete things without a human check. A scheduled agent that can act freely is a risk, not a helper.

## The Claude Agent SDK

The **Agent SDK** is a toolkit for people who build software. It lets you put Claude Code's abilities inside your own app. Your app can then use Claude Code's agent, its tools, and its way of working, as part of something bigger.

You do not need the SDK to use Claude Code. You need it when you are building a product for other people, and you want that product to have an agent inside it. If that day comes, the SDK is the way in. Until then, know it exists, and move on.

## Parallel and cloud sessions

Sometimes one agent is not enough. You can run several Claude Code sessions at once, each on its own branch, as Chapter 4.9 explained. That is **parallel** work. Each session has its own memory and its own job. You review each one, and merge the best.

There are also **cloud sessions**, where Claude Code runs on a remote computer instead of yours. That is useful when you want a long task to run while your laptop is closed. Check the current price and availability for cloud sessions, as they change often.

## A power-user setup in 15 minutes

Here is a starter kit. Build it in one sitting, and you will feel the difference at once.

1. Write a short CLAUDE.md for your project.
2. Make three slash commands: review, test, and explain.
3. Make one skill for a job you repeat, like writing a blog post.
4. Add one hook that runs the tests after every change.
5. Connect one MCP server for an app you use every day.

Five steps. Fifteen minutes. A setup that grows with you.

> TRY IT: Build the starter kit above for a real project, even a tiny one. Use it for a week. Notice which power-up you reach for most. That is the one to deepen next.

## Check yourself

1. What is a slash command?
**Answer:** A saved prompt you can run with a short command, such as /review, instead of typing the full prompt each time.

2. What is a skill?
**Answer:** A small package of instructions that loads only when the job needs it, like a recipe card the agent pulls out at the right moment.

3. What is a subagent?
**Answer:** A helper agent the main agent sends work to, which does one focused task and reports back with a summary.

4. What is a hook?
**Answer:** A rule that runs automatically at a set moment, such as running the tests after every change.

5. What is headless mode?
**Answer:** Running Claude Code without the chat window, where you give it a task as a command and it prints the result and exits.

## In short

- Slash commands save prompts you use often.
- Skills package a way of working that loads only when needed.
- Subagents handle focused tasks, like research or review, in parallel.
- Hooks enforce rules automatically, such as running the tests.
- MCP servers let Claude Code reach apps outside your project folder.
- Build the 15-minute starter kit, and deepen the power-up you reach for most.
