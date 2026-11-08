# 4.8 Agents and AI coding tools: become a builder
<!-- original: ch. 60 -->

Here is the secret this whole section is built on. You no longer need to be a programmer to build software. Coding agents write, run, test, and fix code for you. Even if you never plan to "code", these tools are the fastest way to build your own automations, websites, and small apps.

This chapter maps the whole tool landscape. You will meet the four kinds of AI building tools. You will learn how to pick one. And you will learn how to work with a coding agent like a professional, even if you have never written a line of code.

## The spectrum of AI building tools

AI building tools sit on a spectrum. At one end, you describe what you want, and the tool builds it. At the other end, you work side by side with the AI, inside real code. Neither end is better. They fit different jobs.

At the easy end are **chat-to-app builders**. You type a description in your browser. The tool builds a working app, with buttons and pages, in a minute or two. You do not see the code unless you want to. These are the best first step for a complete beginner.

Next come **AI code editors**. These are real code editors with AI built in. You see the files. You see every change the AI makes. You can accept or reject each change. These are best for learning, and for precise work where you want to see what is happening.

Then come **self-running coding agents**. These are AI helpers that take on whole tasks. You give them a job, like "add a login page", and they read your project, make the changes, run the tests, and fix their own errors. They work in your terminal, or in the cloud. Claude Code is the best-known example, and Chapter 4.10 is a full masterclass on it.

Last come **agent frameworks**. These are starter kits for building your own agents, in code. You do not need them yet. Chapter 4.17 tours them for when you are ready.

> NOTE: You do not need to learn code before you build. You learn by building. The AI writes the code. Your job is to describe what you want, check the result, and say what to fix.

## Chat-to-app builders: no code needed

These tools need only a browser and an idea. You describe the app. It appears.

**Claude Artifacts** is the simplest start. Inside a Claude chat, you ask for something interactive, like a quiz, a calculator, or a small game. Claude builds it in a panel beside the chat. You can use it at once, and share it with a link.

**Lovable** builds full web apps from a description. Type "a recipe app that saves my favourite meals", and it builds the pages, the buttons, and the storage. It is very good at making things look nice. It has a free tier to start, with paid plans for more builds, so check the current price.

**Bolt** is similar, with a strong focus on speed and on apps that need a database. **v0** is best when design matters most, because it is made by the team behind a popular design system, and its output looks polished by default. **Replit** is a full workspace in your browser, where you can build, run, and share apps, with AI help at every step.

All of these tools share one habit. They work best when you describe one small app, clearly. "A to-do list with three columns" beats "a productivity platform for teams". Start small. Grow later.

## AI code editors

An **IDE** is the application where code is written. It stands for Integrated Development Environment, but you can just think of it as a smart text editor for code. An **AI IDE** is an IDE with an assistant built in.

**Cursor** is the best-known AI IDE. It looks like a normal editor, but the AI sits beside your code. It can finish a line as you type. It can rewrite a highlighted section. It can chat about your project, and make changes across many files at once. Chapter 4.12 tours it in full.

**VS Code with Copilot** is the same idea from Microsoft. VS Code is free, and Copilot is its AI helper. It is a solid choice if you already use Microsoft tools, or if you want the biggest community to learn from.

**Zed** is a fast, light editor with AI built in. **JetBrains** tools are the choice for large, professional projects. **Devin Desktop**, formerly called Windsurf, is another AI-first editor worth a look.

The big difference from a chat-to-app builder is visibility. In an editor, you see the files. You see each change. You can open any file and read it. That makes editors better for learning how software really works, and for fixing things precisely.

## Self-running coding agents

A **coding agent** is an AI that can do a whole job by itself. You give it a task in plain words. It plans the work. It reads the files it needs. It writes the code. It runs the code to check it works. If it fails, it reads the error and tries again.

**Claude Code** is the leading example. It lives in your terminal, and also in editors, on the web, and on your phone. It is not just for code. People use it to organise files, study data, write documents, and automate their computers. Chapter 4.10 covers it from first install to real projects.

**Codex** is OpenAI's coding agent, and **Gemini CLI** is Google's. They follow the same idea, with different strengths. **Devin** is a cloud agent that works on tasks while you do something else, and reports back when it is done.

Coding agents feel strange at first. You are not typing code. You are managing a very fast junior colleague. Your job is to set the goal, give it a way to check its own work, and review what it makes. That is a skill, and it is learnable. This chapter teaches it.

## Customising agents: the power-user layer

Once you are comfortable, you can teach your agent how you like to work. There are four tools for this, and Chapter 4.11 covers each one in depth.

**Slash commands** save prompts you use often, so you can run them with a short command. **Skills** are small packages of instructions that load only when the job needs them, like a recipe card the agent pulls out at the right moment. **Subagents** are specialist helpers the main agent can send work to, each with its own focus. **Hooks** are automatic rules that run at set moments, like "always run the tests before you finish."

You do not need any of these on day one. Know they exist. When you catch yourself giving the same instruction for the fifth time, that is the moment to turn it into a command or a skill.

## Which tool should you start with?

Here is a simple guide. If you have never built anything, start with a chat-to-app builder. Build one tiny app this week. If you want to learn how software works, move to Cursor or VS Code next, and open the files your builder made. If you want to build bigger things, learn Claude Code. It is the tool that scales with you, from tiny scripts to real projects.

If you already have a project, start with the tool that fits it. A website idea belongs in Lovable or Bolt. A script to tidy your files belongs in Claude Code. A project you want to understand deeply belongs in an AI IDE.

| Tool type | Best first step | Try it when |
| --- | --- | --- |
| Chat-to-app builder | Lovable, Bolt, v0, Claude Artifacts | You have an idea and want to see it fast |
| AI code editor | Cursor, VS Code with Copilot | You want to see and learn the code |
| Coding agent | Claude Code, Codex, Gemini CLI | You want whole tasks done for you |
| Framework | See Chapter 4.17 | You want to build your own agents |

> TRY IT: Open a chat-to-app builder right now. Ask it to build a tip calculator: an amount, a percentage, and a total, with a clean design. Use it. Then ask it to add a button that splits the bill between three people. You have just built and improved an app, with no code.

## Working with coding agents like a pro

Good results come from good direction. Here are the habits that separate happy builders from frustrated ones.

First, **plan before you build**. Write a short description of what you want, in plain words. Say what the app does, who it is for, and what success looks like. A five-line plan saves an hour of fixing.

Second, **build in small steps**. Ask for one feature at a time. Check it. Then ask for the next one. Agents that build ten features at once make ten mistakes at once.

Third, **give the agent a way to check its work**. Say "run the app and check that the button works" or "run the tests and fix any errors." An agent that can check itself will fix its own mistakes before you ever see them.

Fourth, **review what it makes**. Open the files. Read the summary the agent gives you. Try the app yourself. You do not need to read every line of code, but you do need to test the thing it built.

Fifth, **use Git**. Git is a safety net that saves snapshots of your work, so you can always go back. Chapter 4.9 teaches it, and it needs no account at all. Always save a snapshot before you ask an agent to make a big change.

## What coding agents are great at, and not

Coding agents are great at starting projects, writing routine code, fixing errors, explaining code, and doing boring repetitive work. They are fast, tireless, and happy to try again.

They are not great at knowing what you really want when you have not said it clearly. They are not great at big, vague goals like "make it better." They are not great at security, unless you ask them to think about it. And they sometimes sound confident about code that does not work. That is why you test everything.

The rule is simple. The agent writes. You decide. You are the boss. The agent is the builder. Keep that order, and you will build things you are proud of.

> NOTE: Never let a coding agent handle real passwords, real money, or real customer data until you understand what it is doing. Practice on toy projects first. The skills transfer, and the stakes stay low.

## Check yourself

1. What is a chat-to-app builder?
**Answer:** A tool in your browser that builds a working app from a plain-words description, with no code needed from you.

2. What is an AI IDE?
**Answer:** A code editor with an AI assistant built in, where you can see the files and every change the AI makes.

3. What does a self-running coding agent do?
**Answer:** It takes a whole task, plans it, writes the code, runs it, checks it, and fixes its own errors.

4. Why should you build in small steps?
**Answer:** Because an agent that builds ten features at once makes ten mistakes at once, while one feature at a time is easy to check and fix.

5. What should you do before asking an agent to make a big change?
**Answer:** Save a snapshot with Git, so you can go back if the change goes wrong.

## In short

- You can build software now, even if you have never coded.
- Chat-to-app builders are the fastest start; AI editors show you the code; coding agents do whole tasks.
- Plan first, build one feature at a time, and give the agent a way to check its work.
- Review what the agent makes, and test it yourself.
- Use Git as a safety net before big changes.
- You are the boss; the agent is the builder.
