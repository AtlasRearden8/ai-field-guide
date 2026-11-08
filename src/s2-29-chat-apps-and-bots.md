# 2.29 Chat apps and bots
<!-- original: ch. 59 -->

Chat apps are where people already hang out. That makes them the perfect home for AI. Build a bot that answers team questions from your docs. A Discord game master for your friends. A Telegram assistant in your pocket. A Slack helper that summarises channels. This chapter covers built-in AI in chat apps, then shows three ways to build your own bot, from no-code to code.

A **chat bot** is an AI assistant that lives in Slack, Discord, Telegram, or WhatsApp. People message it like a colleague. You can build one without code, using n8n. Or with a short Python program. Or by asking a coding agent to write it for you.

## Built-in AI in chat apps

Check built-in AI first. You may not need to build anything.

| App | Built-in AI | Also… |
|---|---|---|
| Slack | Channel recaps, thread summaries, AI search across conversations and connected apps, agents | An official MCP server lets other AIs use Slack |
| Microsoft Teams | Copilot recaps, "what did I miss," meeting notes | Copilot Studio agents can live in Teams |
| Discord | Varies by server, mostly via bots and apps | A huge bot ecosystem |
| Telegram | Bots are first-class citizens, created via @BotFather | Perfect for personal assistants |
| WhatsApp | Meta AI built in, plus business bots via the official business platform | Official APIs for business use |

Slack and Teams already sum up conversations and answer questions. Try those features for a week before you build a bot. Building is fun. Not building is faster.

> NOTE: A bot that reads a channel can see private messages. Tell members it is there. Transparency is not optional.

## Three ways to build your own bot

| Way | Tools | Best for |
|---|---|---|
| No-code | n8n with Telegram, Slack, or Discord triggers plus an AI agent step; also Zapier and Make | Personal assistants, team helpers, quick prototypes |
| Low-code | Bot frameworks like discord.py, Slack Bolt, or python-telegram-bot, plus an AI service | Custom behaviour, games, community bots |
| AI-built | Claude Code or Cursor writes the bot for you | Anything, fast, and you learn by reading the code |

No-code is the fastest start. You connect a chat trigger to an AI step, add memory, add tools, and you are done. Low-code gives you full control over behaviour. AI-built is the shortcut: describe the bot, let the coding agent write it, then read the code to learn how it works.

## Build one: a Telegram assistant with n8n

Telegram is the easiest home for a personal assistant. Bots are built into the platform. You create one with @BotFather, which gives you a token. Then you build a workflow in n8n: a Telegram trigger, an AI agent step, memory, and tools like calendar, tasks, and weather.

Lock it down first. Add a check on the sender's user ID so it only responds to you. A public bot can rack up API bills fast. Then give it one fun personality: a pirate, a cheerful coach, a wise owl. Use it for a week. Then add one real tool. You will never want to go back to plain chat apps.

The full build, step by step, is in chapter 6.3. The agent patterns come from the n8n AI agent chapters in Section 4.

## Build two: a Slack "ask our docs" helper

The idea is simple. Someone mentions @DocsBot: "How do we request time off?" The bot searches your docs. It answers with a link. Grounded answers beat confident guesses. If the answer is not in the docs, the bot should say so and point to a human. Confident wrong answers destroy trust.

Level it up with a daily channel digest, an "unanswered questions" report, or a /summarise slash command. Each addition is small. Together they turn a helper into a teammate.

## Build three: a Discord game-master bot

For custom behaviour, a small Python bot goes a long way. The classic example is a fantasy game master. You write a short program with discord.py, a Python library for building Discord bots. It listens for messages starting with !gm. It keeps per-channel conversation history. It sends the history to an AI service with a system prompt: "You are a cheerful, fair fantasy game master. Keep replies under 120 words. Describe scenes vividly. Ask players what they do next. Never decide actions for them." The AI replies. The bot posts it to the channel.

Then type "!gm We enter the misty tavern." Let the adventure begin. The same pattern works for trivia hosts, movie-night pickers, riddle bots, and choose-your-own-adventure games. More game ideas are in Section 4's storytelling chapter.

> TRY IT: Build the Telegram assistant above and give it one fun personality. Use it for a week. Then add one real tool, like your calendar. Private pair programming in your pocket.

## Designing a bot people love

| Principle | In practice |
|---|---|
| One clear job | "Answers HR questions" beats "does everything" |
| Personality | A name, a friendly voice, and emoji if it fits the community |
| Short replies | Chat is conversational. Long answers go in threads or files |
| Honest limits | "I don't know. Try the help channel" beats a confident wrong answer |
| Discoverability | A /help command and a pinned intro message |
| Memory with care | Per-channel or per-user memory, and never remember sensitive info |
| Feedback loop | Reactions logged to a sheet to improve prompts |

Short replies matter most. Chat is a conversation, not a document. If the answer needs length, put it in a thread or a file, and post a short summary in the channel.

## Safety, privacy, and etiquette

Lock it down. Allowlist, which means approve a list of, user IDs or channels. Public bots can rack up API bills fast. Keep secrets safe. Bot tokens and API keys go in environment variables or credentials, never in code you share. Tell people. Members should know a bot reads messages in a channel. Follow the platform's rules and your community's norms. Request only the scopes and intents you need. That is least privilege again.

Set rate limits and spending limits. Cap messages per user per hour. Set API spending limits. And remember prompt injection. In shared channels, anyone can type instructions to your bot. Keep powerful tools behind approvals. A bot that anyone can talk to should not be able to send money or delete files.

## Twenty bot ideas

| For work | For friends and family | For fun |
|---|---|---|
| Docs Q and A bot | Shared grocery list bot | Game master |
| Daily standup collector | Family calendar reminders | Trivia host |
| Meeting notes to channel summary | Chore rotation announcer | Movie night picker |
| "Who is on vacation?" bot | Group trip planner | Daily riddle bot |
| Customer feedback digest | Recipe and meal ideas bot | Song-lyric guessing game |
| Onboarding buddy for new hires | Plant watering reminders | Choose-your-own-adventure |
| Incident summary bot | Homework helper in learning mode | Pet photo caption contest |

> NOTE: Start with one bot and one job. A bot that does one thing well gets used daily. A bot that does ten things badly gets muted.

## What to do when your bot misbehaves

Bots misbehave. It will happen. The bot answers a question it should not. It replies in the wrong channel. It loops, sending the same message again and again. Stay calm. First, stop it: pause the workflow or revoke its token. Second, read the logs. What did it receive? What did it do? Third, find the cause. A vague prompt is the usual suspect. A missing allowlist is second. A tool with too much power is third. Fix the cause, not the symptom. Add the missing rule. Tighten the allowlist. Remove the risky tool. Then test it in a private channel before you let it back into the group. A bot that broke once and was fixed is a bot you understand. A bot that never broke is a bot you have not tested enough.

> NOTE: Every bot needs an off switch that a human can reach in seconds. If you cannot stop it fast, do not launch it.

## Check yourself

1. What is the first thing to check before building a bot?
**Answer:** Whether the chat app's built-in AI already does the job.

2. What are the three ways to build a bot?
**Answer:** No-code with n8n or similar, low-code with a bot framework, or AI-built with a coding agent.

3. Why should a bot only respond to approved user IDs?
**Answer:** A public bot can rack up API bills fast, and anyone could use it.

4. Why should a docs bot admit when it does not know?
**Answer:** Confident wrong answers destroy trust. Admitting gaps and pointing to a human builds it.

5. What is the biggest risk of a bot in a shared channel?
**Answer:** Prompt injection: anyone in the channel can type instructions to the bot, so powerful tools must stay behind approvals.

## In short

- Try built-in AI in Slack and Teams first. Build a bot when you need a specific job done.
- n8n gets you a Telegram or Slack bot with memory and tools in under an hour, with no code.
- For custom behaviour, a small Python bot plus an AI service goes a long way.
- Great bots have one job, short replies, honest limits, and a locked-down setup.
- Tell people the bot is there, protect its tokens, and cap its spending.
