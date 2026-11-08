# 2.33 Local AI for coding
<!-- original: ch. 81 -->

Can you get AI coding help without sending a single line of code to the cloud? Yes, and it is getting better fast. Local models now power autocomplete, chat, and even agent tools. This chapter shows you the setups, which models work best, how to size context, and where local agents still struggle, so you can mix local and cloud wisely.

Local models can power coding assistants and agents so your code and data never leave your computer. That matters for private projects, offline work, and avoiding per-request costs. Local models are less capable than the strongest cloud models on large, complex tasks. Many developers combine the two.

## Local versus cloud for coding: the honest picture

| Task | Local models today | Frontier cloud models |
|---|---|---|
| Autocomplete | Excellent with small, fast models | Excellent |
| "Explain this code" chat | Very good with mid-size models | Excellent |
| Small edits and refactors | Good with 14B or larger models | Excellent |
| Multi-step agent tasks: edit, run, fix, repeat | Good with large models, weaker below | Best |
| Big features across many files | Possible on big hardware, less reliable | Best |
| Privacy, offline, no per-use cost | Total | Your code goes to a provider |

The hybrid habit: local for autocomplete, explanations, private code, and bulk chores. Cloud frontier models for hard, multi-step agent work. Many tools let you switch per task with one setting.

> NOTE: Be honest about the gap. A local model is a great junior partner. A frontier cloud model is a great senior partner. Use each for what it is good at.

## Choosing coding models

| Your memory | Try | Good for |
|---|---|---|
| 8 to 16 GB | Small Qwen-Coder or Gemma models | Autocomplete, quick questions |
| 24 to 32 GB | Mid-size coding models around 20 to 27B | Solid chat and edits, light agent work |
| 48 to 64 GB | Larger mixture-of-experts coding models | Real agent sessions on small projects |
| 128 GB or more | The largest open coding models | The closest thing to frontier agents at home |

What makes a good local coding model? Three things. It was trained for code. It supports **tool calling**, which is essential for agents. And it handles a long context, because agents read lots of files. Check the model page in the Ollama library for the "tools" capability before you download.

**Context length** matters for agents. Coding agents need big context windows, 64,000 tokens or more. Longer context uses more memory, so a model that fits at 8,000 tokens might not fit at 64,000. Set Ollama's context length in the app settings, and leave memory headroom.

## Setup one: autocomplete and chat in your editor

The winning combo is a tiny, fast model for autocomplete plus your biggest comfortable model for chat. Autocomplete runs on every keystroke, so it must be fast. Chat benefits from a smarter, larger model.

| Tool | Editor | Setup |
|---|---|---|
| Cline | VS Code | API provider set to Ollama or LM Studio, pick the model |
| Zed | Zed | Settings, then AI, then Ollama or LM Studio |
| JetBrains AI | IntelliJ family | Supports local models via Ollama or LM Studio in settings |
| Cursor and VS Code Copilot | Their editors | Mostly cloud-first; local support is limited or via custom endpoints |

One note: Continue was acquired by Cursor in June 2026 and is no longer maintained. Pick Cline for new setups. Old guides still mention Continue. They are out of date.

## Setup two: local coding agents

| Agent | Where it runs | Connect to local |
|---|---|---|
| Cline, Roo Code, Kilo Code | VS Code | API provider set to Ollama or LM Studio |
| Aider | Terminal, Git-native | A command with the Ollama model name and local address |
| OpenCode, Goose | Terminal or desktop | Configure an Ollama or OpenAI-compatible provider |
| Claude Code | Terminal | Via Ollama's Anthropic-compatible API, see below |
| Open WebUI plus tools | Browser | Code interpreter and tools with local models |

**Aider** is worth a special mention. It works in the terminal and speaks Git natively. It edits files, runs tests, and commits changes. It pairs well with local models because it keeps tasks small and focused.

## Setup three: Claude Code on local models

Ollama speaks Anthropic's Messages API, so Claude Code's workflow, file editing, commands, skills, hooks, and subagents, can drive an open model. The one-line setup needs Ollama version 0.15 or newer. It sets everything up and launches Claude Code for you. Or you can configure it yourself: point the Anthropic base URL at Ollama's local address, set the auth token to "ollama," and pick a model.

What to expect: the same workflow you learned in the Claude Code chapters, with quality depending on the model you pick. Bigger local models handle real tasks. Small ones get lost in long agent loops. Ollama also offers cloud models through the same setup if you want a bigger open model without the hardware.

Check what "local" means. Models with a :cloud tag run on Ollama's servers, not your machine. For truly private work, stick to models you have downloaded. Double-check with the command that shows what is loaded right now.

> TRY IT: Install Cline, point it at Ollama, and ask the local model to explain what a script in your project does, then add a docstring to every function. Turn off your Wi-Fi halfway through. Private pair programming, achieved.

## Making local agents work better

| Tip | Why |
|---|---|
| Smaller, well-defined tasks | "Add input validation to signup.py" beats "build auth" |
| A great CLAUDE.md or AGENTS.md | Clear commands and conventions matter even more for smaller models |
| Tests as the finish line | "Make the signup tests pass" keeps agents on track |
| Plan with a big model, execute locally | A frontier model writes the plan; the local agent does the steps |
| Fewer MCP tools | Every tool definition eats context |
| Enough context | 32,000 to 64,000 or more tokens for agent work |
| Commit often | Rewinding is your friend; local Git is enough |
| Measure | Run the same five tasks on a few models and keep a scorecard |

A **CLAUDE.md** file is a standing instruction file that lives in your project. It tells the agent your commands, conventions, and rules. For smaller models, it matters even more than for big ones. Write it well. Keep it short. Update it when the agent makes the same mistake twice.

## Local agents beyond coding

Local agents are not only for code. A file organiser renames files with Claude Code or Goose plus a local model. Email triage on private mail runs in n8n with Ollama. Document Q and A runs in Open WebUI Knowledge or a local document-search system. Smart home control runs through Home Assistant's local AI integration. Receipt and invoice extraction runs with a vision model plus structured output through the local API. Your homemade agent from Section 4 can run locally too: point the SDK at Ollama's local URL and pick a tool-capable model.

> NOTE: The pattern is always the same. Point the tool at your local address. Pick a model your machine can run. Give it small tasks and clear rules.

## A first week with local coding

Day one: install Cline and point it at Ollama. Ask it to explain one file. Day two: ask for autocomplete on a small task and notice the speed. Day three: ask it to write tests for one function. Day four: ask it to refactor one small file, then review every change yourself. Day five: try a bigger model for one chat task and compare the quality. Day six: turn off your Wi-Fi and work for an hour. Notice what still works. Day seven: write down what local did well and what it did badly. That list is your hybrid plan. Local for the wins. Cloud for the gaps.

> NOTE: Review every change a local agent makes, just as you would review a cloud agent's changes. Local does not mean safer code. It means private code.

## Check yourself

1. What is local AI best at for coding?
**Answer:** Autocomplete, quick questions, and small, well-defined tasks.

2. Why use two different models for autocomplete and chat?
**Answer:** Autocomplete runs on every keystroke, so it must be fast. Chat benefits from a smarter, larger model.

3. How can Claude Code run on local models?
**Answer:** Through Ollama's Anthropic-compatible API, with a one-line launch command or manual settings.

4. What three things make a good local coding model?
**Answer:** Trained for code, supports tool calling, and handles a long context.

5. How do you tell a truly local model from a cloud one in Ollama?
**Answer:** Models with a :cloud tag run on Ollama's servers. Check what is loaded, and stick to downloaded models for private work.

## In short

- Local models are excellent for autocomplete and chat, and increasingly capable as agents on big hardware.
- Pick code-trained, tool-calling, long-context models, as big as your memory allows.
- Cline or Zed for editor help. Cline, Aider, or OpenCode for agents. Claude Code via Ollama for its workflow on open models.
- Give local agents small tasks, clear rules, and tests, and plan with a big model when needed.
- Cloud-tagged models are not local. Check before trusting privacy.
