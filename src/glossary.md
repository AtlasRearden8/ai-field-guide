# Glossary

Every jargon term in this book, in plain words. Terms are listed A to Z. Each entry ends with the chapter where the term first shows up.

**.env file** — A small text file in a project folder that holds secrets and settings as NAME=value lines, such as API keys. Programs read it when they start, so keys never have to be written into code. *First seen in Chapter 4.14.*

**.gitignore** — A file in a Git project that lists files Git should never track, such as .env files with secrets or folders of downloaded models. Putting .env in .gitignore stops you from accidentally publishing your keys. *First seen in Chapter 4.20.*

**A2A (Agent2Agent)** — An open standard that lets AI agents built by different companies or tools talk to each other and hand off work. For example, your travel agent could pass the hotel search to a hotel company’s own agent and bring the results back to you. *First seen in Chapter 4.17.*

**AAC** — Augmentative and alternative communication: tools that help people who cannot rely on speech to communicate, increasingly with AI-generated voices. A speech app that turns typed or tapped phrases into a natural-sounding voice is one example. *First seen in Chapter 5.11.*

**Access token** — A short-lived secret code an app shows to prove it is allowed to act on your behalf, usually obtained through OAuth. It is like a hotel key card: it opens only certain doors, and it stops working when it expires. *First seen in Chapter 2.21.*

**Accuracy** — How often an AI’s answers are right, measured against answers that are already known to be correct. It is one of the simplest scores used in evals, though it says nothing about how the model handles tricky or unusual cases. *First seen in Chapter 1.7.*

**Adaptive thinking / effort** — A setting that lets a model decide how much to think before answering, or lets you turn its thinking up or down. Choose low effort for a quick rewrite and high effort for a hard planning problem. *First seen in Chapter 2.16.*

**ADK (Agent Development Kit)** — Google’s toolkit for building AI agents in Python or Java, with ready-made pieces for tools, memory and multi-agent teamwork. It is one of the agent frameworks compared in this manual. *First seen in Chapter 4.17.*

**Agent** — An AI system that works in a loop — think, use a tool, look at the result, repeat — until a goal is finished. Claude Code fixing a bug this way reads the files, edits the code, runs the tests and repeats until they pass. *First seen in Chapter 1.1.*

**Agent framework** — A ready-made kit for building agents, giving you the loop, the tool handling, the memory and the way agents talk to each other instead of making you write all of it from scratch. LangGraph, CrewAI and the OpenAI Agents SDK are examples. *First seen in Chapter 4.17.*

**Agent loop** — The think–act–observe cycle an agent repeats until it finishes or hits a limit. Search the web, read a page, decide another source is needed, search again, then write the answer. *First seen in Chapter 1.17.*

**Agent mode** — A mode in ChatGPT (and similar assistants) where the assistant stops just chatting and starts doing multi-step work for you, such as researching options and filling in forms. It plans the steps, uses tools and reports back when it is done. *First seen in Chapter 1.4.*

**Agent SDK (Claude Agent SDK)** — A library that gives your own apps the same agent machinery that powers Claude Code. You can build a research or support agent in Python or TypeScript with file access, tools and MCP support already built in. *First seen in Chapter 4.8.*

**Agentic RAG** — RAG where an agent is in charge: it decides what to search, searches several times and checks the results before answering. An assistant might search your docs, notice a gap, rephrase the query and search again. *First seen in Chapter 3.3.*

**AGENTS.md / CLAUDE.md** — Markdown files kept in a project folder that coding agents read automatically as standing instructions. They typically list the test command, the coding style and any files the agent must never touch. *First seen in Chapter 4.10.*

**AGI** — Artificial general intelligence: a hypothetical AI as capable as humans across most kinds of work. The term appears in headlines and lab mission statements, but there is no agreed test for when it has been reached. *First seen in Chapter 1.1.*

**AI (artificial intelligence)** — Software that does things that normally need human thinking, such as understanding language, recognising images, making plans or creating new text, pictures and music. The AI in this manual is almost always a large language model or a system built around one. *First seen in Chapter 1.1.*

**AI companion** — An AI designed mainly to keep you company and chat, rather than to complete tasks. Some assistants offer companion modes with a personality and a memory of past conversations. *First seen in Chapter 1.11.*

**AI Revival** — A name used in this book for the wave of new AI tools and models arriving in late 2026. It is a label for the current moment, not a single product. *First seen in Chapter 2.1.*

**AI voice (writing style)** — The flat, generic style AI writing often falls into: over-polished sentences, the same stock phrases and an even, slightly formal tone. The manual teaches you to spot it and to steer the model toward writing that sounds like you. *First seen in Chapter 3.6.*

**Airtable** — A friendly online tool that works like a spreadsheet crossed with a database, used to organise information in tables. AI features can summarise, categorise and fill in its rows, and automations can read and write it. *First seen in Chapter 4.33.*

**Alexa+** — Amazon’s rebuilt, generative-AI version of Alexa: conversational, able to remember preferences, and able to book, order and control your smart home. It is included with Prime in the US. *First seen in Chapter 1.12.*

**Algorithm** — A step-by-step recipe for solving a problem or doing a calculation, written precisely enough for a computer to follow. Search rankings, recommendations and the training of AI models are all built from algorithms. *First seen in Chapter 1.18.*

**Alignment (AI safety)** — The work of making AI systems behave the way people actually want: helpful, honest and safe, even when instructions are vague or conflicting. It covers training methods such as RLHF as well as rules and checks around the model. *First seen in Chapter 5.13.*

**Allowlist / denylist** — A list of things explicitly allowed (an allowlist) or explicitly blocked (a denylist), used to control what an AI, a user or a program may reach. An agent might be allowlisted to read only one folder, for example. *First seen in Chapter 2.24.*

**Alt text** — A short text description of an image, written for people using screen readers and for places where the image cannot load. Good alt text says what the image shows, such as a bar chart showing sales doubling between March and June. *First seen in Chapter 4.28.*

**Anki** — A popular flashcard app that uses spaced repetition, showing you each card again just before you would forget it. The manual uses it as an example of studying with AI-generated cards. *First seen in Chapter 5.1.*

**ANN** — Approximate nearest neighbour search: a fast way to find vectors that are nearly the closest to a query, without comparing every single one. It is how a vector database can search millions of embeddings in milliseconds. *First seen in Chapter 3.4.*

**Answer engine** — A search tool that writes an answer with numbered sources instead of giving you a list of links. Perplexity is the best-known example: ask it for the best budget e-reader and you get a written comparison with clickable citations. *First seen in Chapter 2.7.*

**API** — A way for programs to talk to each other. AI APIs let your code send prompts to a model and get answers back, usually billed per token: a script might send 500 product descriptions to a model and save the rewritten versions to a spreadsheet. *First seen in Chapter 4.2.*

**API key** — A secret string that identifies you — and your bill — when your code calls an API. It is stored in a .env file or a secrets store, never pasted into code or shared in a screenshot. *First seen in Chapter 4.15.*

**Apple Intelligence** — Apple’s AI features on iPhone, iPad and Mac, including the rebuilt Siri, Writing Tools and Visual Intelligence. Highlighting an email on iPhone and choosing Writing Tools, then Proofread, is one example. *First seen in Chapter 1.12.*

**Apple Silicon** — Apple’s own family of computer chips (M1, M2, M3, M4 and later) used in Macs, where the processor, graphics and memory share one design. They are popular for local AI because their unified memory lets them run large models. *First seen in Chapter 2.30.*

**Artifact** — A generated, often interactive piece of content — an app, a document or a chart — shown in a panel beside a Claude chat. Asking Claude for a habit tracker can produce a working, clickable app in that panel. *First seen in Chapter 1.4.*

**ASR** — Automatic speech recognition, also called speech-to-text: turning spoken words into written text. It is the engine behind dictation, live captions and meeting transcripts. *First seen in Chapter 4.25.*

**Astro** — A fast framework for building websites that ships very little JavaScript by default. It appears in this manual as one of the tools vibe-coding apps can be built with. *First seen in Chapter 4.13.*

**ATS** — Applicant tracking system: software employers use to collect and filter job applications. It is why résumés should use standard headings and include the job ad’s key skills in plain text. *First seen in Chapter 5.4.*

**Audio Overview** — A Gemini Notebook (NotebookLM) feature that turns your uploaded sources into a two-host podcast-style discussion. A stack of lecture PDFs can become a 15-minute conversation to listen to on a commute. *First seen in Chapter 1.9.*

**AutoHotkey** — A free Windows tool that lets you automate keystrokes, clicks and small desktop tasks with short scripts. The manual mentions it alongside Power Automate as a Windows automation option. *First seen in Chapter 4.6.*

**Automation** — Work that happens on its own once you have set it up, triggered by an event or a schedule instead of by you doing it by hand. An automation might watch for new invoice emails, summarise them with AI and add rows to a spreadsheet. *First seen in Chapter 4.1.*

**Autonomy levels** — How much an AI does on its own, on a scale from only suggesting, to drafting, to acting with your approval, to acting fully automatically. An email agent that drafts replies for approval is less autonomous than one that sends them itself. *First seen in Chapter 4.16.*

**AWS** — Amazon Web Services: Amazon’s huge cloud platform, offering rented computers, storage, databases and AI services by the hour. It is one of the places you can host an app or a remote MCP server. *First seen in Chapter 4.14.*

**Background agent** — A coding agent that works in the cloud on its own branch while you do other things. You might assign it “add dark mode” before lunch and review its pull request afterwards. *First seen in Chapter 4.8.*

**Backpropagation** — The method used in training to work out how much blame each part of a model deserves for a wrong answer, so its parameters can be nudged in the right direction. It is the maths behind learning from mistakes, and you never need to do it by hand. *First seen in Chapter 1.18.*

**Backup** — A copy of your files, settings or data kept somewhere safe so you can restore them if something is deleted, broken or lost. Good habits are automatic, regular backups and occasionally checking that a restore actually works. *First seen in Chapter 4.34.*

**Bandwidth** — How much data a connection can carry in a given time, usually measured in megabits per second. It decides how quickly large files, video calls and model downloads move, while latency decides how quickly the first bit arrives. *First seen in Chapter 4.14.*

**Barge-in** — Interrupting a voice agent while it is still talking. Good agents stop and listen, so you can say “actually, make it Thursday” while it is still reading out available times. *First seen in Chapter 4.25.*

**Batch API** — A way to send many non-urgent requests at once for a big discount, with the results delivered later. Classifying 50,000 support tickets overnight can cost roughly half the normal price this way. *First seen in Chapter 4.15.*

**Benchmark** — A standard test set used to compare models on the same tasks. SWE-bench tests coding ability, and public leaderboards compare models on reasoning and maths tests. *First seen in Chapter 2.16.*

**Beta** — A version of software that is mostly finished and being tested by real users before its official release. Beta features can still change or have rough edges, and an earlier, rougher stage is sometimes called alpha. *First seen in Chapter 2.26.*

**Bias (AI)** — Unfair patterns a model learned from its training data, which can then show up in its outputs about people. A résumé screener that rates otherwise identical candidates differently based on their names is one example. *First seen in Chapter 1.10.*

**BM25** — A classic keyword-ranking algorithm, often combined with vector search in hybrid search. It is good at finding an exact part number or error code that pure meaning-based search would miss. *First seen in Chapter 3.3.*

**Body doubling** — Working alongside someone — or a voice AI — to stay focused on a task. Keeping a voice assistant session open while you work through something you have been avoiding is one version of it. *First seen in Chapter 5.5.*

**Bolt** — An AI app builder (from StackBlitz) that turns a text description into a working web app in the browser, which you can then refine by chatting. It is one of the vibe-coding tools in this manual. *First seen in Chapter 4.13.*

**Bot** — A program that does a job automatically, often by chatting or by acting inside another app. A Telegram bot that answers questions, a support bot on a website and a bot that posts scheduled messages are all bots. *First seen in Chapter 2.29.*

**Branch (Git)** — A separate line of work inside a Git repository, used to try a change without disturbing the main version. You branch off, make your changes, then merge the branch back when the work is ready. *First seen in Chapter 4.9.*

**Breaking change** — A change to an API, tool or file format that stops older ways of using it from working. When a provider announces one, code that relied on the old behaviour must be updated. *First seen in Chapter 4.34.*

**Browser agent** — An agent that drives a web browser the way a person would: opening pages, clicking, filling in forms and reading what comes back. It can do research or routine web tasks, but it needs strict limits because a browser can spend money and reach private accounts. *First seen in Chapter 4.19.*

**Build-along** — A chapter where you build a real project step by step, following along as you go. You finish with something that works. *First seen in Chapter 6.3.*

**Byte / gigabyte (GB)** — Units of digital size: a byte is one character of text, roughly, and a gigabyte is about a billion bytes. A phone photo is a few megabytes, a laptop drive holds hundreds of gigabytes, and model files are usually measured in gigabytes. *First seen in Chapter 2.11.*

**C2PA / content credentials** — A standard for attaching tamper-evident “how this was made” information to images and videos. The “CR” label on an image can show which AI tool created or edited it. *First seen in Chapter 4.22.*

**Caching (prompt caching)** — Reusing the processed beginning of a prompt to make repeated calls cheaper and faster. A 50-page manual sent with every question costs a fraction of the price after the first request, because the model does not re-read it from scratch. *First seen in Chapter 4.20.*

**Calendly** — A scheduling service that lets other people book time with you through a link, without the back-and-forth of emails. It can connect to your calendar and to automations that prepare for each meeting. *First seen in Chapter 4.33.*

**Canva** — A popular design tool for making social posts, slides, posters and videos from templates, now with AI features for generating images and text. It appears in this manual’s design chapter as a quick way to make things look good. *First seen in Chapter 4.28.*

**Canvas** — A side-by-side writing and editing space inside ChatGPT (and similar tools) where you can draft, revise and preview a document with the AI, instead of scrolling through one long chat. It is handy for essays, code and long edits. *First seen in Chapter 2.2.*

**CapCut** — A widely used video-editing app, from the makers of TikTok, with AI features such as automatic captions, background removal and generated clips. It is one of the video tools in the creative chapters. *First seen in Chapter 4.23.*

**Chain / workflow** — A fixed sequence of steps, some of which use AI. Every new form submission is summarised by AI and the summary is posted to Slack, for example. *First seen in Chapter 4.1.*

**Chain-of-thought (CoT)** — A way of getting better answers by having a model reason step by step, out loud in its own working notes, instead of jumping straight to an answer. Reasoning models do this internally, and prompting a model to “think step by step” does it on the surface. *First seen in Chapter 2.16.*

**Changelog** — A dated list of what changed in each version of a piece of software, usually written for the people who use it. Reading a changelog is the quickest way to learn what a new release fixes or breaks. *First seen in Chapter 2.17.*

**Chatbot / AI assistant** — An app you talk to in plain language, like ChatGPT, Gemini, Claude, Copilot or Grok. You might type “plan a three-day trip to Lisbon” and get a full itinerary back. *First seen in Chapter 1.2.*

**ChatGPT (OpenAI)** — OpenAI’s assistant and the world’s most-used AI app, with voice, images, projects, agents and more. You can use voice mode on a walk, Canvas for writing, or agent mode to research hotels. *First seen in Chapter 2.2.*

**Checkpoint** — A saved state you can roll back to, so a mistake does not cost you everything after it. In Claude Code you can rewind to before a change went wrong, and in model training a checkpoint is a saved copy of the model’s weights at one point in training. *First seen in Chapter 4.10.*

**Chroma** — A small, open-source vector database that is easy to run on your own computer, popular for first RAG projects. It stores embeddings and finds the passages closest in meaning to a question. *First seen in Chapter 3.5.*

**Chunking** — Splitting documents into passages before turning them into embeddings for RAG. A 200-page manual might be split into passages of a few hundred words so that search can find the right section. *First seen in Chapter 3.3.*

**CI / CD** — Continuous integration and continuous delivery: the practice of automatically testing, and often deploying, code every time a change is pushed. GitHub Actions is the version of this you will meet most in this manual. *First seen in Chapter 4.9.*

**Classification / regression** — The two classic kinds of machine-learning prediction: classification sorts things into categories (spam or not spam), while regression predicts a number (the price of a house). *First seen in Chapter 2.16.*

**Claude (Anthropic)** — Anthropic’s assistant, known for natural writing, long documents, Artifacts and Claude Code. You might upload a long contract and ask for its unusual clauses, with quotes. *First seen in Chapter 2.4.*

**Claude Code** — Anthropic’s AI coding agent that works in your terminal, reading, editing, running and testing code on your own machine. It reads CLAUDE.md files for project instructions and can work with skills, subagents and MCP servers. *First seen in Chapter 4.10.*

**Claude Desktop** — Anthropic’s desktop app for chatting with Claude on Mac or Windows. It is also where many people first install MCP servers, and it can install them as packaged .mcpb extensions. *First seen in Chapter 2.20.*

**CLI** — Command-line interface: a program you use by typing commands in a terminal. Typing claude or ollama run gemma4 in a terminal window are both examples. *First seen in Chapter 4.10.*

**Clone (Git)** — Making your own local copy of a Git repository, usually from GitHub, so you can work on it on your machine. Cloning copies the files and their full history. *First seen in Chapter 4.9.*

**Closed model** — A model you can only use through the company that built it, usually through its app or API, because its weights are not shared. Most flagship assistants, including ChatGPT and Claude, are closed models. *First seen in Chapter 2.16.*

**Cloud** — Computing that runs on someone else’s computers, reached over the internet, instead of on your own machine. Storing files in Google Drive or chatting with a hosted model are both using the cloud. *First seen in Chapter 1.5.*

**Cloudflare** — A company that sits between websites and the internet to make them faster and safer, and that also offers hosting, serverless functions and tunnels. Its tunnel service is one way to reach a home server securely from anywhere. *First seen in Chapter 4.14.*

**Cloudflare Tunnel** — A free service that gives a server on your home network a secure web address without opening ports on your router. It is one of the ways the manual suggests reaching a home lab or a remote MCP server from outside. *First seen in Chapter 2.32.*

**Clustering** — Grouping similar things together without being told the groups in advance. Embeddings make it possible to cluster thousands of support tickets or notes into topics automatically. *First seen in Chapter 3.4.*

**Code execution** — A sandbox where the AI writes and runs code (often Python) to analyse data or check its own work. Upload a spreadsheet and ask for a chart, and the assistant writes and runs the Python to make it. *First seen in Chapter 4.15.*

**Coding agent** — An AI that reads, writes, runs and fixes code on its own, such as Claude Code, Codex or a Copilot agent. You might say “add a login page and tests for it” and then review the changes it made. *First seen in Chapter 2.1.*

**Comet** — Perplexity’s free AI web browser, with an assistant that can read and act on the pages you visit. You can ask its sidebar assistant to compare the prices in your three open shopping tabs. *First seen in Chapter 1.4.*

**Command center** — One place, usually a Notion page, where you can see and run your most important jobs. It brings your tasks, notes, and automations together. *First seen in Chapter 4.31.*

**Commit (Git)** — A saved snapshot of your project with a short message describing the change. Running git commit -m “Add recipe search” creates a save point you can return to. *First seen in Chapter 1.5.*

**Compaction** — Summarising the older parts of a long conversation to free up context, so the model can keep working without forgetting the important bits. Running /compact in Claude Code does this for a long session before the next task. *First seen in Chapter 3.6.*

**Component** — A reusable building block of an app or a design, such as a button, a card or a form, that is defined once and used in many places. Vibe-coding tools generate apps out of components. *First seen in Chapter 4.13.*

**Computer use** — AI controlling a mouse, keyboard and screen (or a browser) like a human would. An agent might open a website, fill in a form and take a screenshot to check its work. *First seen in Chapter 1.12.*

**Configuration (config)** — The settings that tell a program how to behave, usually kept in a file or in environment variables rather than in the code itself. A config file might hold the model name, the port and the API keys for an app. *First seen in Chapter 4.14.*

**Connector** — A ready-made integration inside an AI app (often MCP under the hood) that links it to a service such as Gmail. You connect it in settings, then ask “what did my landlord say last week?” *First seen in Chapter 1.4.*

**Consent (AI)** — Permission from a person before their face, voice, writing or data is used to train a model or to make something with AI. The manual treats consent as the first check before using anyone’s likeness or work. *First seen in Chapter 5.13.*

**Context (AI)** — Everything a model can see while it works on your request: your message, the conversation so far, any attached files, the system prompt and the results of tools it has used. Most AI failures are really context problems, not intelligence problems. *First seen in Chapter 2.18.*

**Context engineering** — Deliberately choosing what goes into a model’s context: instructions, examples, documents and tools. Giving the AI your style guide, two example emails and the relevant thread before asking for a reply is context engineering. *First seen in Chapter 2.15.*

**Context rot** — The slow loss of quality in a long session as the context fills up with old, irrelevant or contradictory material and the model starts forgetting or confusing details. Starting a fresh chat, or compacting the conversation, fixes it. *First seen in Chapter 2.18.*

**Context window** — How much text (in tokens) a model can consider at once: its working memory. A very long chat starts “forgetting” details from the beginning once the window fills up. *First seen in Chapter 1.2.*

**Copilot (Microsoft)** — Microsoft’s assistant in Windows, Edge and Microsoft 365 apps such as Word, Excel and Outlook. You might ask Copilot in Excel to add a column that flags overdue invoices. *First seen in Chapter 2.5.*

**Copilot Studio** — Microsoft’s tool for building custom Copilot agents for a team or business, without writing much code. It connects an agent to company data and to Power Automate flows. *First seen in Chapter 2.26.*

**Copyright (AI)** — The law that gives creators control over copying and reuse of their work, which matters for AI in two directions: what models were trained on, and who owns what a model makes. The practical rule in this manual is to check the licence before using generated work commercially. *First seen in Chapter 5.13.*

**Cosine similarity** — A measure of how closely two vectors point in the same direction, from -1 to 1. It is how RAG finds similar text: a score near 1.0 means two passages mean nearly the same thing. *First seen in Chapter 3.4.*

**CPU** — Central processing unit: the main chip in a computer, good at general-purpose work done one step at a time. AI work usually runs on a GPU instead, because the maths there can be split across thousands of small cores at once. *First seen in Chapter 2.31.*

**Crew (multi-agent)** — A team of agents with different roles working together on one job, as in the CrewAI framework. One agent might research, another write and a third check the result, coordinated by a lead agent. *First seen in Chapter 4.4.*

**CrewAI** — A popular framework for building teams of AI agents, each with its own role, goal and tools, that collaborate on a task. It is one of the four frameworks compared in the agent frameworks tour. *First seen in Chapter 4.17.*

**CRM** — Customer relationship management: software (or a spreadsheet) for tracking contacts and their deals. HubSpot is a well-known CRM, and a simple sheet tracking each client, last contact date and next step is a small one. *First seen in Chapter 2.19.*

**Cron** — A scheduler built into most computers and servers that runs commands at times you set, such as every night at 2 a.m. or every weekday at 7. A nightly agent run or a weekly report is often just a cron job. *First seen in Chapter 4.3.*

**CRUD** — Create, read, update, delete: the four basic things apps do with data. A recipe app’s add, view, edit and delete buttons are its CRUD operations. *First seen in Chapter 4.8.*

**CSV** — Comma-separated values: a plain-text file format for tables, where each line is a row and commas separate the columns. Spreadsheets, databases and data-analysis tools all read and write CSV files. *First seen in Chapter 5.12.*

**CUDA** — NVIDIA’s platform that lets programs use its graphics cards for general computing, including AI. Most local-AI tools on NVIDIA hardware run on CUDA, which is why an NVIDIA card is the usual choice for a local AI machine. *First seen in Chapter 2.31.*

**Cursor** — An AI-first code editor, built on VS Code, where the assistant can read your whole project, edit several files at once and run in agent mode. It is one of the main AI IDEs in this manual, alongside VS Code with GitHub Copilot. *First seen in Chapter 4.12.*

**Custom Agent (Notion)** — A Notion feature that lets you build a small AI agent inside a workspace, with its own instructions and access to chosen pages and databases. The manual uses one to triage tasks and run a weekly review. *First seen in Chapter 3.1.*

**Custom connector** — A remote MCP server you add to an AI app by pasting its URL. Pasting an MCP server address into Claude’s custom connector dialog is how you add one. *First seen in Chapter 2.4.*

**Custom GPT** — A custom version of ChatGPT with saved instructions, files and optionally actions, built for one job and shareable with others. A “grant-writing helper” that already knows your organisation’s rules is one example. *First seen in Chapter 2.2.*

**Custom instructions** — Standing notes about you and how you like answers, which the assistant includes in every chat. “I’m a nurse in Ohio. Keep answers short and use bullet points” is a typical example. *First seen in Chapter 1.5.*

**DALL-E** — OpenAI’s image-generation model, built into ChatGPT, known for following detailed prompts and editing images by description. It is one of the image tools in the creative chapters. *First seen in Chapter 1.18.*

**Dashboard** — A single screen that pulls together the numbers and updates you care about, such as tasks due, money spent or workflow errors. A Notion dashboard fed by n8n, or a small-business sales dashboard, are both examples. *First seen in Chapter 4.31.*

**Data retention** — How long a service keeps your data before deleting it, and what it does with it in the meantime. It is worth checking before you paste private material into a new AI tool. *First seen in Chapter 1.5.*

**Data source (Notion)** — A table of rows inside a Notion database, with its own set of properties. Since API version 2025-09-03, one database can hold several data sources. *First seen in Chapter 3.9.*

**Database** — An organised store for information that programs can search, filter and update, such as a list of customers or a collection of documents. Notion databases, vector databases and the database behind a web app are all databases. *First seen in Chapter 3.9.*

**Database automation (Notion)** — A Notion rule that runs actions when a row is added or a property changes, or on a schedule. On paid plans it can also send webhooks: when a deal’s status becomes Won, a webhook to n8n might start client onboarding. *First seen in Chapter 3.9.*

**Dataset** — A collection of data gathered for one purpose, such as training or testing a model, or practising analysis. A folder of 10,000 labelled customer reviews is a dataset; so is a CSV of house prices used in a tutorial. *First seen in Chapter 5.12.*

**DAW** — Digital audio workstation: software for recording, editing and mixing music and audio, such as Ableton Live, Logic Pro or GarageBand. The manual shows Claude talking to a DAW through MCP to help make music. *First seen in Chapter 4.24.*

**Deep learning** — Machine learning done with large neural networks that have many layers, which lets a system learn complicated patterns from huge amounts of data. Modern language, image and voice models are all deep learning. *First seen in Chapter 1.18.*

**Deep research** — An assistant mode that runs a multi-step, multi-source investigation and writes a cited report. Ask for a comparison of heat pumps for cold climates and you get a report minutes later, with sources. *First seen in Chapter 1.4.*

**Deepfake** — Realistic fake video, audio or images of real people made with AI. A fake video of a celebrity endorsing an investment scheme is the classic example, and the same technology powers harmless dubbing and accessibility tools. *First seen in Chapter 1.11.*

**DeepSeek (assistant)** — A Chinese AI lab and its free assistant, known for strong open-weight reasoning models. Note that its app data is stored in China, which matters for privacy. *First seen in Chapter 2.9.*

**DeepThink** — Mistral’s reasoning mode in Le Chat, which shows the model thinking through a problem step by step before it answers. It is the equivalent of a “thinking” mode in other assistants. *First seen in Chapter 2.10.*

**Dependency** — A piece of software your project relies on, usually a library or package installed from a registry. Listing dependencies lets anyone else install exactly the same versions and get the same result. *First seen in Chapter 2.24.*

**Deploy (deployment)** — Putting software you built onto a server or hosting service so other people can actually use it. Deploying a vibe-coded app to Vercel turns a project on your laptop into a public web address. *First seen in Chapter 4.14.*

**Deprecated** — Officially discouraged and on the way out: the maker still supports it for now, but it may be removed in a future version. Older MCP transports and old API versions are often deprecated rather than switched off at once. *First seen in Chapter 2.20.*

**Descript** — An audio and video editor that lets you edit a recording by editing its transcript, with AI voices and filler-word removal built in. It is one of the production tools in the video and audio chapter. *First seen in Chapter 4.23.*

**Diff** — The list of changes between two versions of files. Green and red lines show exactly what a coding agent added and removed, so you can review a change before accepting it. *First seen in Chapter 4.9.*

**Discord** — A chat app built around servers and channels, popular with gaming, hobby and developer communities. AI bots can answer questions, moderate and summarise conversations inside a Discord server. *First seen in Chapter 2.29.*

**Distillation** — Training a smaller model on a bigger model’s outputs, so the small one keeps much of the big one’s quality at a fraction of the size and cost. It is how many small, fast models get as good as they are. *First seen in Chapter 2.34.*

**DNS** — Domain name system: the internet’s address book, turning names like example.com into the numeric addresses computers use. When you buy a domain, you edit its DNS records to point it at your hosting. *First seen in Chapter 4.14.*

**Docker / container** — A way to package an app with everything it needs so it runs the same everywhere, isolated from the rest of the machine. Starting the home lab’s Ollama, Open WebUI and n8n with one docker compose up -d command is a typical use. *First seen in Chapter 2.32.*

**Docker Compose** — A Docker tool that starts several containers together from one short configuration file. One file can define your n8n, database and local model services and bring them all up with a single command. *First seen in Chapter 2.32.*

**Domain (web)** — The human-readable address of a website or service, such as example.com, which the domain name system translates into a computer address. Buying a domain is one of the steps in launching a web app. *First seen in Chapter 4.14.*

**DuckDB** — A tiny, fast database that runs SQL directly on CSV and Parquet files, with no server to set up. Running SELECT category, SUM(amount) FROM 'bank.csv' GROUP BY 1 is a typical use. *First seen in Chapter 5.12.*

**Edge function** — A small piece of server code that runs close to users, on demand, instead of on one central server. A small server route that sends a user’s ingredients to Claude without exposing your API key is one example. *First seen in Chapter 4.14.*

**ElevenLabs** — An AI voice company whose tools turn text into realistic speech and clone voices from short recordings. It is the text-to-speech engine behind many voice agents and narrated videos in this manual. *First seen in Chapter 2.13.*

**Elicitation** — An MCP feature where a server asks you a question mid-task, instead of guessing or failing. A booking server might pause to ask “which of these three times works for you?” *First seen in Chapter 2.20.*

**Embedding** — A list of numbers that represents the meaning of text (or an image), where similar meanings get similar numbers. Turning each note into a vector lets “dentist appointment” find a note about “teeth cleaning.” *First seen in Chapter 3.4.*

**Embedding model** — A model whose only job is to turn text (or images) into embeddings. You choose it separately from your chat model, and smaller, cheaper embedding models are usually fine for a personal RAG system. *First seen in Chapter 3.4.*

**Embeddings** — The plural of embedding: lists of numbers that capture the meaning of many pieces of text, used to power search by meaning. RAG systems store embeddings for every passage and compare them with the embedding of your question. *First seen in Chapter 3.4.*

**Encryption** — Scrambling data so only someone with the right key can read it. Messages sent over HTTPS are encrypted in transit, and end-to-end encryption means even the service carrying the messages cannot read them. *First seen in Chapter 2.36.*

**Endpoint (API)** — One specific address in an API that does one job, such as creating a chat reply or listing your files. Calling an endpoint means sending a request to its URL and getting a structured response back. *First seen in Chapter 1.6.*

**Endpointing** — Deciding when a speaker has finished their turn, in voice agents. It is why a good voice agent waits for you to finish a sentence instead of cutting in mid-pause. *First seen in Chapter 4.25.*

**Environment variable** — A named setting (like an API key) given to a program when it runs, instead of being written in the code. export OPENAI_API_KEY=... sets one for a terminal session. *First seen in Chapter 2.21.*

**Epoch** — One full pass through the training data during training. A model might train for three epochs, meaning it has seen every example three times. *First seen in Chapter 2.34.*

**Error handling** — What a program or workflow does when something goes wrong, instead of just crashing. Good error handling retries a failed step, logs what happened and tells a human if it cannot recover. *First seen in Chapter 4.5.*

**Error workflow (n8n)** — A workflow that starts with an Error Trigger and runs whenever another workflow that names it fails. Every failed workflow might add a row to a Notion automation log with a link to the failed execution. *First seen in Chapter 4.3.*

**Eval (evaluation)** — A repeatable test set for measuring AI quality on your own tasks. Twenty real support questions with known good answers, rerun after every prompt change, is a simple eval. *First seen in Chapter 1.8.*

**Event (automation)** — Something that happens and can start an automation, such as a form being submitted, an email arriving or a file being added to a folder. Triggers listen for events, and workflows run in response to them. *First seen in Chapter 4.1.*

**Exfiltration** — Getting data out of a place it should not leave, usually secretly. In AI security it is the danger in the lethal trifecta: an agent that can read your private data and reach the internet could be tricked into sending that data to an attacker. *First seen in Chapter 2.24.*

**Facebook** — Meta’s social network, where Meta AI appears inside Messenger, groups and the main app. The manual mentions it mainly as a place Meta’s assistant lives and as a source of AI-generated content to spot. *First seen in Chapter 1.8.*

**Fallback** — A backup plan a system switches to when its first choice fails. If a fast model returns an error, a workflow might fall back to a slower model rather than giving up. *First seen in Chapter 4.2.*

**Few-shot prompting** — Including a few examples in the prompt to show the pattern you want. Showing two sample product descriptions, then asking for ten more in the same style, is few-shot prompting. *First seen in Chapter 1.6.*

**Field exercise** — A hands-on task in Section 6 of this book. You learn by building something real, not just by reading. *First seen in Chapter 6.1.*

**Field guide** — This book itself. A field guide is a small, practical book you carry with you and use while you do the thing it teaches. *First seen in Chapter 1.1.*

**Figma** — A popular collaborative design tool for interfaces and graphics, used to design apps and websites. The manual shows AI turning a Figma design into working code through MCP. *First seen in Chapter 4.28.*

**Fine-tuning** — Further training a model on your own examples. It is great for style and format, not for facts: training a small model on 300 of your emails teaches it to draft in your voice. *First seen in Chapter 2.16.*

**Firebase** — Google’s platform for building apps, offering a database, logins, hosting and serverless functions in one place. It appears as an option for giving a vibe-coded app a real backend. *First seen in Chapter 6.6.*

**Flux** — A family of open image-generation models from Black Forest Labs, known for realistic images and strong text rendering. It is one of the image models you can run locally or through an API. *First seen in Chapter 4.22.*

**Fly.io** — A hosting service that runs apps in small containers close to users around the world, with a generous free tier. It is one of the deployment options in the hosting chapter. *First seen in Chapter 4.20.*

**Fork (GitHub)** — Your own copy of someone else’s GitHub repository, made so you can change it freely and propose your changes back. Forking is how most open-source contributions start. *First seen in Chapter 4.9.*

**Framework** — A ready-made skeleton for building a kind of software, giving you the common structure and rules so you only write the parts that are unique to your app. LangGraph is a framework for agents; Next.js is one for websites. *First seen in Chapter 4.17.*

**Free tier** — A no-cost level of a service with limits on use, offered so you can try it or run small projects for free. Many AI APIs, hosting services and automation platforms have a free tier. *First seen in Chapter 1.4.*

**Frontier model** — The most capable models available at a given time. They are the top tier of each lab’s lineup, used for the hardest reasoning and coding tasks, and they cost the most per token. *First seen in Chapter 2.16.*

**Function calling / tool use** — The model outputting a structured request to run a tool, which your software then executes. The model might return get_weather(city=“Lisbon”); your code runs it and sends the forecast back. *First seen in Chapter 2.16.*

**Gamma** — An AI presentation tool that turns a short prompt or an outline into slides. It appears in the manual as a quick way to make a deck without designing each slide by hand. *First seen in Chapter 5.2.*

**GDPR** — The European Union’s data-protection law, giving people rights over their personal data. You can request a copy of everything a company stores about you, or ask it to delete your data. *First seen in Chapter 2.10.*

**Gem** — A custom version of Gemini with saved instructions (and optional files) for a specific job. A “Meal Planner” Gem that already knows your household’s diet and budget is one example. *First seen in Chapter 2.3.*

**Gemini (Google)** — Google’s assistant and model family, built into Android, Chrome, Gmail and Docs. Asking Gemini “when is my flight?” gets the answer from your Gmail. *First seen in Chapter 2.3.*

**Gemini Live** — Gemini’s real-time voice conversation mode, with camera and screen sharing. You can point your phone camera at the back of a TV and ask which HDMI port to use. *First seen in Chapter 1.4.*

**Gemini Notebook (formerly NotebookLM)** — Google’s source-grounded research notebook with Audio and Video Overviews, renamed in July 2026. Upload a course’s readings and get cited answers, flashcards and quizzes. *First seen in Chapter 1.9.*

**Gemma** — Google’s family of open-weight models, free to download and run locally. Gemma models are a popular first choice for a private local assistant on a laptop. *First seen in Chapter 2.16.*

**Generative AI** — AI that creates new text, images, audio, music or video instead of only sorting or predicting. Writing a speech, creating a logo or composing a song from a short description are all generative AI. *First seen in Chapter 1.1.*

**GGUF** — A file format for quantised local models, used by llama.cpp, Ollama and LM Studio. Downloading model-Q4_K_M.gguf from Hugging Face to run in LM Studio is a typical use. *First seen in Chapter 2.30.*

**Git** — A version-control system that saves the history of your project. It lets you undo a broken change with git restore . and get back to the last working version. *First seen in Chapter 4.9.*

**GitHub** — The website where most open-source code lives, built around Git. You host repositories there, review pull requests, run GitHub Actions and publish pages from it. *First seen in Chapter 4.9.*

**GitHub Actions** — Automations that run on GitHub when things happen, such as a push, a schedule or a comment. They can automatically run tests on every push, or build and deploy a website. *First seen in Chapter 4.20.*

**GitHub Copilot** — GitHub’s AI coding assistant, built into VS Code and other editors. It suggests code as you type, answers questions about your codebase and can run as an agent that makes changes for review. *First seen in Chapter 2.1.*

**GitHub Pages** — Free hosting from GitHub for simple static websites, served straight from a repository. It is the quickest free way to put a small site on the internet. *First seen in Chapter 4.9.*

**Gmail** — Google’s email service, which AI can connect to through connectors, MCP servers and automations. Connected Gmail lets an assistant search your mail or draft replies in your voice. *First seen in Chapter 2.27.*

**Google Assistant** — Google’s voice assistant on Android phones and Google Home speakers, now being rebuilt around Gemini. It answers questions, controls smart-home devices and runs routines by voice. *First seen in Chapter 2.12.*

**Google Calendar** — Google’s calendar service, which AI assistants and automations can read and write to check availability, create events and prepare for meetings. *First seen in Chapter 1.4.*

**Google Cloud** — Google’s cloud platform, offering rented computers, storage, databases and AI services. It is where Gemini’s API and many hosted AI services run. *First seen in Chapter 2.17.*

**Google Colab** — Google’s free service for running Python notebooks in the browser, with access to GPUs for AI work. It is a quick way to try data analysis or fine-tuning without installing anything. *First seen in Chapter 2.34.*

**Google Docs** — Google’s online word processor, where Gemini can draft, summarise and edit documents. AI writing help is built into Docs, and automations can create documents from templates. *First seen in Chapter 2.26.*

**Google Drive** — Google’s cloud storage for files, which AI tools connect to so they can search and read your documents. An assistant with Drive access can answer questions from your own files. *First seen in Chapter 2.2.*

**Google Sheets** — Google’s online spreadsheet, where Gemini can write formulas, summarise tables and build charts. Automations often use Sheets as a simple, shareable database. *First seen in Chapter 1.13.*

**GPU** — Graphics processing unit: a chip built to do thousands of small calculations at the same time, which is exactly the maths AI needs. An NVIDIA graphics card with 16 GB of VRAM can run a mid-size local model quickly. *First seen in Chapter 1.18.*

**Granola** — An AI meeting notetaker that transcribes calls and turns them into clean notes and summaries. It is one of the meeting tools in the AI-at-work chapters. *First seen in Chapter 2.13.*

**GraphRAG** — RAG that first builds a knowledge graph of entities and relationships, so it can answer questions about connections. It can answer “which suppliers are connected to the delayed projects?” across many documents. *First seen in Chapter 3.3.*

**Grok (xAI)** — The assistant from xAI (part of SpaceX), built into X, known for real-time posts and Grok Imagine. Tapping Grok on a viral X post and asking for the background and what is confirmed is a typical use. *First seen in Chapter 2.6.*

**Grok Imagine** — Grok’s image and short-video generator. Turning “a fox running through snow at dusk” into a short video clip with sound is one example. *First seen in Chapter 1.9.*

**Groq** — A company that runs models on specialised chips for extremely fast responses, and the API that gives you access to them. It is one of the hosted options for fast, cheap inference on open models. *First seen in Chapter 2.17.*

**Grounding** — Making a model answer from specific sources (documents, search results) and cite them. Telling the model “answer only from these documents and cite the page” is grounding. *First seen in Chapter 4.15.*

**Guardrails** — Rules, checks and limits that keep AI systems safe and on-task. An agent might be free to read files but required to ask before deleting or sending anything. *First seen in Chapter 1.14.*

**Hallucination** — The model confidently stating something false. Grounding it in sources and verifying important claims reduces it: a chatbot might cite a court case or research paper that does not exist. *First seen in Chapter 1.10.*

**Handoff** — One agent passing a conversation or task to another agent (or to a human). A support bot might transfer a billing question to a human agent together with a summary of the conversation so far. *First seen in Chapter 2.18.*

**Harness** — The software around a model that turns it into something useful: the loop, the tools, the memory, the prompts and the rules. Claude Code is a harness around Claude; an agent framework is a kit for building harnesses. *First seen in Chapter 2.16.*

**Hash** — A short, fixed-length fingerprint computed from a piece of data, used to check that data has not changed or to look things up quickly. Passwords are usually stored as hashes rather than as readable text. *First seen in Chapter 2.36.*

**Headless mode** — Running an agent (like Claude Code) from scripts or scheduled jobs without an interactive chat. A nightly cron job might run claude -p “summarize today’s errors” < log.txt on its own. *First seen in Chapter 4.11.*

**HeyGen** — An AI video tool that creates talking-head videos from a script, including avatars and voice cloning. It is one of the video-generation tools in the creative chapters. *First seen in Chapter 4.21.*

**HNSW** — A graph-based index that makes vector search fast. It is the index type you will see in vector database settings, trading a tiny bit of accuracy for a large gain in speed. *First seen in Chapter 3.4.*

**Home Assistant** — Free, open-source software for running a smart home locally, controlling lights, sensors and devices without relying on a cloud service. The manual uses it as the hub for a private home assistant. *First seen in Chapter 2.32.*

**Home lab** — A small setup of computers at home — often an old PC, a mini PC or a Raspberry Pi — used to run services such as local AI, automations and storage for yourself instead of paying for cloud services. *First seen in Chapter 2.32.*

**Hook** — An automatic script that runs when an agent does something, such as after each file edit. A hook might run the code formatter after every edit, or block the agent from reading .env files. *First seen in Chapter 4.11.*

**Host / client / server (MCP)** — The three roles in MCP: the host is the AI app, the client is its connection manager, and the server is the program exposing tools and data. Claude Desktop (host) connects to the GitHub MCP server (server) through its own client. *First seen in Chapter 1.3.*

**Hosting** — Paying for (or running) the computers that keep a website or app available on the internet. Vercel, Netlify and Render are hosting services; a home server is self-hosting. *First seen in Chapter 1.4.*

**HTTP** — Hypertext transfer protocol: the set of rules browsers and apps use to ask servers for things and receive answers. Every web page load and every API call is an HTTP request followed by an HTTP response. *First seen in Chapter 4.2.*

**HTTP method (GET / POST)** — The verb in an HTTP request that says what you want to do: GET reads something, POST creates or sends something, PUT updates it and DELETE removes it. A REST API is built from these verbs applied to URLs. *First seen in Chapter 4.2.*

**HTTP status code** — The three-digit number in an HTTP response that says what happened: 200 means success, 404 means not found, 401 means unauthorised, 403 means forbidden, 429 means too many requests and 500 means the server had an error. *First seen in Chapter 4.2.*

**HTTPS** — The encrypted version of HTTP, shown by the padlock in your browser. It scrambles the data between you and a website so nobody in between can read or change it. *First seen in Chapter 4.2.*

**Hugging Face** — The main hub for open AI models and datasets, where you can download models, read their documentation and try them in your browser. Most open-weight models are published there first. *First seen in Chapter 2.30.*

**Human-in-the-loop** — A step where a person approves or edits before the AI’s output is used. An automation might draft a refund email and wait in Slack for your approval before sending it. *First seen in Chapter 4.1.*

**Hybrid search** — Combining keyword and vector search for better retrieval. Combining BM25 and embeddings lets a search find both an exact error code and a passage that means the same thing in different words. *First seen in Chapter 3.3.*

**IDE** — Integrated development environment: a code editor with extras built in, such as debugging, Git and AI help. VS Code, Cursor and JetBrains editors are IDEs. *First seen in Chapter 4.8.*

**Idempotency** — Designing an operation so running it twice has the same effect as running it once, which matters for webhooks and retries. A capture workflow that updates the existing row for an email instead of creating a second one is idempotent. *First seen in Chapter 4.2.*

**IFTTT** — If This Then That: a simple automation service that connects apps with one-trigger, one-action recipes. It is an older, simpler alternative to Zapier or n8n. *First seen in Chapter 4.1.*

**Image-to-video** — Animating a still image with a video model. Turning a product photo into a slow, rotating video clip for social media is one example. *First seen in Chapter 4.23.*

**Imagen** — Google’s image-generation model family, used inside Gemini and other Google tools for creating and editing pictures from text descriptions. *First seen in Chapter 4.22.*

**Index (search)** — A data structure that makes searching fast by organising information in advance, rather than scanning everything each time. A vector database builds an index (such as HNSW) over embeddings so similar items can be found in milliseconds. *First seen in Chapter 3.4.*

**Inference** — Running a model to get output, as opposed to training it. Every chat message you send triggers inference, and API pricing is for inference, not training. *First seen in Chapter 2.16.*

**Inkling 2 Small** — A thinking model from Thinking Machines Lab, released on November 5, 2026. A thinking model spends extra time working through a hard question before it answers. *First seen in Chapter 2.1.*

**Inpainting / outpainting** — Editing part of an image, or extending it beyond its edges. You might remove a stranger from a photo’s background (inpainting) or extend a portrait into a landscape (outpainting). *First seen in Chapter 4.22.*

**Input / output tokens** — The two sides of an API bill: input tokens are what you send (your prompt, files and tool results), and output tokens are what the model writes back. Output tokens usually cost several times more than input tokens. *First seen in Chapter 4.15.*

**Interpreter** — A program that runs code line by line instead of compiling it first. Python is usually run by an interpreter, which is why you can test a few lines of Python instantly in a terminal. *First seen in Chapter 4.15.*

**Jailbreak** — A trick that tries to get a model to ignore its safety rules, for example by hiding instructions in a story or a role-play. Jailbreaks are a security concern for agents, and a reason to keep agents away from untrusted content. *First seen in Chapter 2.35.*

**JavaScript** — The programming language of the web, used in browsers and, through tools like Node.js, on servers too. Many web apps, browser extensions and n8n code steps are written in JavaScript. *First seen in Chapter 4.20.*

**Jira** — Atlassian’s popular tool for tracking work in software teams, organising issues into boards and sprints. Automations can create or update Jira issues from AI triage. *First seen in Chapter 4.33.*

**JSON** — The universal text format for structured data, written as pairs of names and values in braces. {"name": "Pixel", "species": "cat", "age": 4} is a small JSON object. *First seen in Chapter 4.2.*

**JSON Schema** — A description of what valid JSON should look like. Tools use it to define their parameters: a tool definition might state that city is a required string and days is an optional number. *First seen in Chapter 2.16.*

**JSON-RPC** — A simple standard for sending requests and replies as JSON, used by MCP for messages between clients and servers. It is why MCP traffic looks like short JSON objects with a method name and parameters. *First seen in Chapter 2.21.*

**Jupyter notebook** — A document that mixes notes, code and charts, run step by step. A sales analysis you can rerun each month on new data is a typical notebook. *First seen in Chapter 5.12.*

**Kaggle** — A Google-owned community for data science, with free datasets, competitions and notebooks you can run in the browser. It is a good source of practice datasets for the data-analysis chapter. *First seen in Chapter 2.34.*

**Keyword search** — Searching by matching the exact words in a query, as a search engine has traditionally done. It is fast and precise for codes and names, and it is the “keyword” half of hybrid search. *First seen in Chapter 3.4.*

**Kimi** — The assistant from Chinese lab Moonshot AI, known for very long context windows and strong document work. It appears in the global assistants chapter alongside Qwen. *First seen in Chapter 2.11.*

**Kling** — A video-generation model from Kuaishou, known for realistic motion and longer clips. It is one of the video models in the creative AI chapters. *First seen in Chapter 4.23.*

**Knowledge base** — A collection of documents an AI can search to answer questions. A folder of company policies that an HR chatbot searches before answering is a knowledge base. *First seen in Chapter 2.4.*

**Knowledge cutoff** — The date a model’s training data ends. It does not know later events unless it is given tools or documents, which is why a model without web search cannot tell you last night’s game score. *First seen in Chapter 1.2.*

**Knowledge graph** — A web of facts stored as things and the relationships between them, such as people, companies and the deals connecting them. GraphRAG builds one from documents so it can answer questions about connections. *First seen in Chapter 3.5.*

**Knowledge ladder** — The manual’s own sequence for making AI know your stuff, from weakest to strongest: just paste it in the chat, use a long context window, build a RAG system, or give an agent memory. Each rung handles more material than the last. *First seen in Chapter 3.3.*

**LangChain** — A popular open-source framework for building applications with language models, providing ready-made pieces for prompts, tools, memory and retrieval. It is one of the agent frameworks in the frameworks tour. *First seen in Chapter 4.17.*

**LangGraph** — A framework from the LangChain team for building agents as graphs of steps, where the flow can branch, loop and pause for approval. It is one of the four frameworks compared in the agent frameworks tour. *First seen in Chapter 4.17.*

**Latency** — The delay before a response arrives. It matters most for voice: an agent that takes three seconds to reply feels awkward on a phone call. *First seen in Chapter 4.25.*

**Le Chat (Mistral)** — The assistant from French lab Mistral AI: fast, with memories, connectors and European privacy rules. It can transcribe and clean up a scanned handwritten recipe, for example. *First seen in Chapter 2.10.*

**Leaderboard** — A public ranking of models or systems on a shared set of tests. Leaderboards are a quick way to compare models, though they only measure what their tests measure. *First seen in Chapter 2.16.*

**Learning rate** — A training setting that controls how big a step the model takes when correcting its mistakes. Too high and learning becomes unstable; too low and training takes forever. *First seen in Chapter 2.34.*

**Least privilege** — The security habit of giving each person, app or agent only the access it actually needs, and nothing more. An agent that only reads one folder cannot delete or leak anything else. *First seen in Chapter 2.23.*

**Lethal trifecta** — Private data plus untrusted content plus a way to send data out, in one AI setup: a recipe for prompt-injection harm. An agent that reads your email, browses the web and can send messages is one malicious page away from leaking your inbox. *First seen in Chapter 2.24.*

**Library (code)** — A collection of ready-made code for one kind of job, such as handling dates or calling an API, that you add to your own program instead of writing from scratch. An SDK is a library made for one service. *First seen in Chapter 4.15.*

**Light usage** — A low or light plan tier on some AI services. It gives you a smaller amount of use each month, usually for a lower price. *First seen in Chapter 2.1.*

**Linear** — A fast, popular tool for tracking software work, used by many AI-era startups as an alternative to Jira. Automations and agents can create and triage Linear issues. *First seen in Chapter 4.33.*

**Linter / formatter** — Tools that check your code for mistakes and style problems (a linter) and rewrite it into a consistent layout (a formatter). Coding agents often run both automatically after each edit. *First seen in Chapter 4.8.*

**Llama** — Meta’s family of open-weight models, free to download and run locally. Llama models are the most widely used open models, and many local AI setups start with one. *First seen in Chapter 2.30.*

**llama.cpp** — A free, efficient engine for running large language models on ordinary computers, including laptops without a powerful graphics card. Ollama and LM Studio both build on llama.cpp, and GGUF is its model file format. *First seen in Chapter 2.30.*

**LLM** — Large language model: an AI trained on huge amounts of text to predict and generate language. It is the model behind ChatGPT, Gemini, Claude and other chat assistants. *First seen in Chapter 1.1.*

**LLM-as-judge** — Using a model to grade other models’ outputs against a rubric. You might ask a model to score 100 chatbot replies against a five-point rubric, then spot-check its grades yourself. *First seen in Chapter 2.37.*

**LM Studio** — A friendly desktop app for finding, downloading and chatting with open models on your own computer, without using the terminal. It is one of the main tools in the local AI chapters, alongside Ollama. *First seen in Chapter 2.30.*

**Local MCP server** — An MCP server that runs on your own computer and is launched by the AI app when needed, using the stdio transport. It is the usual setup for servers that read your local files or run local programs. *First seen in Chapter 2.20.*

**Local model** — A model running on your own device instead of the cloud. Running ollama run gemma4 and chatting with no internet connection is using a local model. *First seen in Chapter 2.30.*

**Localhost** — The name for your own computer as a network address (127.0.0.1), used when a program talks to another program on the same machine. An API at http://localhost:11434 is running on your computer, not on the internet. *First seen in Chapter 4.20.*

**LoRA** — Low-rank adaptation: a small add-on trained to teach a model a style, character or skill, without retraining the whole model. Training an image model on 20 photos of your dog lets you generate it in new scenes. *First seen in Chapter 2.34.*

**Loss (training)** — A single number that says how wrong a model’s answers are during training, which the training process tries to drive down. When loss stops falling, the model has learned about as much as it can from that data. *First seen in Chapter 2.16.*

**Lovable** — An AI app builder that turns a text description into a working web app, which you can refine by chatting and publish with one click. It is one of the vibe-coding tools in this manual. *First seen in Chapter 4.13.*

**Luma** — A company behind the Dream Machine video generator and the Genie world model, known for turning text or images into video. It appears in the video and world-model sections of the creative chapters. *First seen in Chapter 4.26.*

**Machine learning** — A way of building software by letting a computer find patterns in examples, instead of a person writing every rule by hand. Spam filters, recommendations and language models are all machine learning. *First seen in Chapter 1.18.*

**Make (automation)** — A visual automation platform (formerly Integromat) where you connect apps in scenarios of modules. It is one of the three automation platforms in this manual, alongside n8n and Zapier, and is known for powerful data handling. *First seen in Chapter 4.1.*

**Markdown** — A plain-text way of writing formatted documents, using simple marks such as # for headings and ** for bold. AI chats, READMEs and note apps all use Markdown, and coding agents read it as instructions. *First seen in Chapter 2.19.*

**Max tokens** — The largest reply (or input) a model is allowed to produce in one call, set as a number of tokens. A reply that stops mid-sentence has usually hit its max tokens. *First seen in Chapter 4.7.*

**MCP** — Model Context Protocol: the open standard for connecting AI apps to tools and data. Installing the GitHub MCP server lets Claude, Cursor and ChatGPT all read your issues through the same connection. *First seen in Chapter 2.20.*

**MCP Apps** — An MCP extension that lets servers show interactive interfaces inside the chat. A booking server might show an interactive calendar right inside the conversation. *First seen in Chapter 2.20.*

**MCP Inspector** — A web tool for testing MCP servers by hand: list their tools, call them and read the raw messages. You might run npx @modelcontextprotocol/inspector python server.py and then click List Tools. *First seen in Chapter 2.20.*

**MCP Registry** — The official public list of MCP servers that clients and catalogs can discover. Searching registry.modelcontextprotocol.io is how you find an official Notion or Stripe server. *First seen in Chapter 2.20.*

**MCP server** — A small program that exposes tools, data or prompts to AI apps through the Model Context Protocol. It can run on your computer (a local server) or on the internet (a remote server), and the AI app connects to it to gain new abilities. *First seen in Chapter 2.20.*

**Memory (AI)** — Facts and preferences an assistant keeps across conversations. Telling it “remember that I’m vegetarian” means it can keep that in mind in future chats. *First seen in Chapter 3.6.*

**Merge (Git)** — Combining a branch back into the main line of a project, bringing its changes with it. A pull request is reviewed and then merged when it is ready. *First seen in Chapter 4.9.*

**Merge conflict** — What happens when Git cannot combine two versions of the same lines, because both sides changed them differently. You resolve it by choosing which version to keep, or by combining them by hand. *First seen in Chapter 4.9.*

**Meta AI** — Meta’s assistant inside WhatsApp, Instagram, Messenger, Facebook and Ray-Ban Meta glasses. Typing “@Meta AI suggest a restaurant for eight” in a WhatsApp group chat is one way to use it. *First seen in Chapter 2.8.*

**Metric** — A number you track to judge how well something is working, such as accuracy, cost per task or average reply time. Evals are built from metrics, and a good metric is one you can measure the same way every time. *First seen in Chapter 2.37.*

**Microsoft Azure** — Microsoft’s cloud platform, offering rented computers, storage, databases and AI services. It is where many businesses run OpenAI models through Azure’s hosted service. *First seen in Chapter 2.17.*

**Microsoft Teams** — Microsoft’s chat and meetings app for workplaces, where Copilot can summarise meetings and answer questions from your documents. *First seen in Chapter 1.13.*

**Midjourney** — A popular AI image generator, used through Discord or its website, known for artistic and photographic images. It is one of the main image tools in the creative chapters. *First seen in Chapter 4.22.*

**Milvus** — An open-source vector database built for large-scale similarity search, used when collections grow into the millions of vectors. It appears in the vector database comparison in this manual. *First seen in Chapter 3.4.*

**Mistral** — A French AI lab whose open-weight models (Mistral, Mixtral) and assistant Le Chat are known for speed and European data rules. Its models are a common choice for local AI in Europe. *First seen in Chapter 2.10.*

**Mixture of experts** — A model design where only some “expert” sub-networks run for each token, giving big-model quality at small-model speed. It is often written “MoE”, and it is why some large open models run surprisingly fast on a Mac with enough memory. *First seen in Chapter 2.16.*

**MLX** — Apple’s machine-learning framework, fast on Apple Silicon. It is used to fine-tune or run models on a MacBook, for example with mlx-lm. *First seen in Chapter 2.30.*

**Mockup** — A realistic-looking preview of an app or web page, more finished than a wireframe but not yet working code. Vibe-coding tools often generate a mockup first so you can approve the design. *First seen in Chapter 4.10.*

**Model (AI)** — A trained AI program that takes an input and produces an output, such as text, an image or a decision. ChatGPT, Claude and Gemini are each powered by one or more models, and a model is the “brain” that an agent, an app or a workflow calls on. *First seen in Chapter 1.1.*

**Model routing** — Sending easy tasks to cheap models and hard ones to frontier models. A small model might triage support emails, with only the complex ones going to the flagship model. *First seen in Chapter 2.38.*

**Multi-agent system** — A setup where several AI agents work together on one job, each with its own role, tools or expertise. One agent might research, another write and a third check the result, coordinated by an orchestrator. *First seen in Chapter 4.18.*

**Multimodal** — Handling more than text: images, audio and video as well. Uploading a photo of a broken part and asking what it is and how to fix it is a multimodal task. *First seen in Chapter 1.9.*

**Music generation (AI)** — AI that composes songs or instrumental music from a text description, a hum or a set of choices. Suno and Udio are the best-known tools, and they can produce a finished-sounding track in under a minute. *First seen in Chapter 4.24.*

**n8n** — An open-source, self-hostable visual automation platform with strong AI features. A self-hosted workflow might email you an AI summary of new RSS articles every morning. *First seen in Chapter 4.1.*

**Nano Banana** — The nickname for Google’s Gemini image generation and editing models. Asking Gemini to put you and a friend on a beach while keeping both faces recognisable is a typical use. *First seen in Chapter 1.9.*

**Netlify** — A hosting service for websites and web apps, with a generous free tier and one-click deploys from Git. It is one of the deployment options in the hosting chapter. *First seen in Chapter 2.22.*

**Neural network** — A computer program loosely inspired by the brain, made of layers of simple units that learn patterns from examples. Large language models are neural networks with billions of adjustable parameters, called transformers. *First seen in Chapter 1.18.*

**Next-token prediction** — The core job a language model is trained to do: guess the most likely next piece of text, one token at a time. A chat reply is just this prediction repeated hundreds of times, which is also why hallucinations happen. *First seen in Chapter 2.16.*

**Next.js** — A popular framework for building React websites and web apps, with hosting built in on Vercel. It is one of the frameworks vibe-coding tools often generate. *First seen in Chapter 4.13.*

**Node (n8n / Make)** — One step in a visual workflow. A “Gmail Trigger” node might feed an “AI Agent” node, which then feeds a “Slack” node. *First seen in Chapter 4.3.*

**Notion** — A flexible workspace app for notes, documents, wikis and databases, used throughout this manual as the place where information lives. Its AI features, databases and API make it half of the n8n + Notion power stack. *First seen in Chapter 3.1.*

**Notion AI** — The AI features built into Notion: writing help, summaries, translations and Q&A over your workspace. It can summarise a page, draft from your notes or answer questions using your databases. *First seen in Chapter 3.1.*

**Notion integration** — A connection that gives external software (like n8n) access to the Notion pages and databases you share with it, using a secret token or OAuth. Creating an “n8n automations” integration and sharing your Tasks database with it is how you set one up. *First seen in Chapter 4.30.*

**NPU** — Neural processing unit: a chip in newer laptops and phones built for efficient AI tasks. It runs on-device features such as live captions and photo search without waking the main processor. *First seen in Chapter 2.31.*

**OAuth** — The “Log in with…” flow that grants an app limited access without sharing your password. Clicking “Sign in with Google” when connecting an AI app to your Drive is OAuth. *First seen in Chapter 2.20.*

**Obsidian** — A note-taking app that stores your notes as plain Markdown files on your own computer, popular for local-first second brains. Its community plugins, graph view and AI connections are covered in the second-brain chapter. *First seen in Chapter 3.2.*

**OCR** — Optical character recognition: turning images of text into actual text. Extracting the words from a photo of a receipt so they can be added to a spreadsheet is OCR. *First seen in Chapter 2.10.*

**Ollama** — A popular tool for running open models locally with one command. ollama pull qwen3 downloads a model, and ollama run qwen3 starts a chat with it. *First seen in Chapter 2.30.*

**On-device AI** — AI that runs entirely on your phone, laptop or other device, with no data sent to the cloud. It is private and works offline, and it is what the NPU in newer devices is built for. *First seen in Chapter 2.12.*

**One-shot prompting** — Giving the model exactly one example of what you want, then asking it to do the same thing for a new input. It sits between zero-shot (no examples) and few-shot (several examples). *First seen in Chapter 1.6.*

**Open model** — A model whose weights are published so anyone can download, run, study or build on it, such as Llama, Qwen or Gemma. Open models are the basis of local AI, and an open-weight model is the usual form they take. *First seen in Chapter 2.16.*

**Open source (software)** — Software whose code is public and free for anyone to use, study and change, under a licence that spells out the terms. n8n, Ollama and many local-AI tools are open source. *First seen in Chapter 1.1.*

**Open WebUI** — A friendly web interface for chatting with local models, with file uploads, RAG and image generation built in. It usually runs in Docker next to Ollama in a home lab. *First seen in Chapter 2.32.*

**Open-weight model** — A model whose weights you can download and run yourself, such as Gemma, Qwen or Llama. Downloading one and running it privately on your own computer is the core of local AI. *First seen in Chapter 2.30.*

**OpenAI Agents SDK** — OpenAI’s toolkit for building agents in Python or TypeScript, with ready-made pieces for tools, handoffs between agents and guardrails. It is one of the four frameworks compared in the agent frameworks tour. *First seen in Chapter 4.17.*

**OpenAI-compatible API** — An API that copies OpenAI’s format, so tools built for one work with many others, including local models. Pointing a tool built for OpenAI at http://localhost:11434/v1 lets it use your local model instead. *First seen in Chapter 2.30.*

**OpenRouter** — A service that lets you call many different models through one API key and one bill, including open-weight models hosted by others. It is a convenient way to try models without opening an account with every provider. *First seen in Chapter 2.13.*

**Opt-in / opt-out** — Choosing to join something (opt in) or choosing to leave it (opt out). AI features that use your data are often opt-in, while training on your chats is something you may need to actively opt out of in settings. *First seen in Chapter 2.3.*

**Orchestrator** — In multi-agent systems, the lead agent that plans the work and delegates to worker agents. A lead research agent might assign three subtopics to worker agents and merge their findings. *First seen in Chapter 4.4.*

**Overfitting** — When a model learns the quirks of its training examples so closely that it does worse on new, unseen examples. It is a common failure in fine-tuning, and the fix is usually more varied data or stopping training earlier. *First seen in Chapter 2.34.*

**Package** — A bundle of reusable code, distributed as one unit that you can install into a project. Installing a package with a package manager is how you add a library such as the Anthropic SDK to your code. *First seen in Chapter 2.4.*

**Package manager (npm / pip)** — A tool that installs and updates packages for a programming language: npm for JavaScript and pip for Python. pip install anthropic adds the Anthropic library to a Python project. *First seen in Chapter 4.9.*

**Pandas** — A popular Python library for working with tables of data, used for cleaning, filtering and analysing spreadsheets and CSV files. It appears in the data-analysis chapter. *First seen in Chapter 2.28.*

**PARA** — A note-organising method: Projects, Areas, Resources, Archive. Folders with those four names in Obsidian or Notion are a PARA setup. *First seen in Chapter 1.2.*

**Parameters (model)** — The learned numbers inside a model. More usually means more capable (and hungrier): a “7B” model has about seven billion parameters and needs roughly 4–5 GB of memory at 4-bit. *First seen in Chapter 2.16.*

**pause_turn** — An API stop reason meaning a long server-side tool turn paused, and you should continue the conversation. When a response ends with this stop reason, send the conversation back to let the model continue. *First seen in Chapter 6.7.*

**Pay-as-you-go** — A billing style where you pay only for what you use, usually per token or per request, with no monthly fee. Most AI APIs bill this way, which is why a spend limit is worth setting. *First seen in Chapter 2.1.*

**Payload** — The actual data carried in a request or message, as opposed to the headers and wrapping around it. The JSON body of a webhook call is its payload. *First seen in Chapter 2.26.*

**Permission** — A grant that lets a person, app or agent do a specific thing, such as read a folder or send a message. Agents work under permissions, and good setups grant as little as possible. *First seen in Chapter 1.4.*

**Perplexity** — An AI answer engine that shows numbered sources for every answer, and also makes the Comet browser. Asking “which cordless vacuum is best for pet hair?” returns a sourced comparison table. *First seen in Chapter 2.7.*

**Persona** — A character or role you ask the AI to take on, such as “a patient maths tutor” or “a sceptical editor”. Giving a model a persona is one of the simplest ways to change the style and stance of its answers. *First seen in Chapter 1.1.*

**Personal Intelligence** — Gemini’s opt-in feature that uses your Gmail, Calendar, Photos and other Google apps to answer questions about your own life. Asking Gemini “what time is my dentist appointment?” gets the answer from your Calendar. *First seen in Chapter 2.3.*

**Personal knowledge management (PKM)** — The practice of collecting, organising and reusing what you learn, so your notes become a second brain instead of a pile. Notion, Obsidian and Gemini Notebook are the tools this manual uses for PKM. *First seen in Chapter 2.25.*

**Personalization** — Tailoring an AI’s answers to you, using your instructions, memory and files. It is why two people can ask the same question and get usefully different answers. *First seen in Chapter 1.3.*

**pgvector** — An extension that turns the PostgreSQL database into a vector database, so it can store embeddings and search by similarity. It is the vector store used in several of this manual’s RAG projects. *First seen in Chapter 3.5.*

**Phishing** — Scam messages that trick you into clicking links or sharing passwords or codes, now often written flawlessly by AI. A perfectly written “your account is locked” email with a link to a fake login page is phishing. *First seen in Chapter 1.11.*

**PII (personally identifiable information)** — Any information that can identify a person, such as a name, email address, phone number or home address. It is the kind of data to keep out of prompts and training sets, and the focus of privacy laws such as the GDPR. *First seen in Chapter 2.36.*

**Pinecone** — A hosted vector database, popular for production RAG systems, where you send embeddings over an API instead of running the database yourself. It is one of the vector databases compared in this manual. *First seen in Chapter 3.4.*

**Pipeline** — A series of processing steps where the output of one step feeds the next, such as a video pipeline that writes a script, generates clips and edits them together. CI pipelines do the same for testing and deploying code. *First seen in Chapter 4.23.*

**Plan mode** — A Claude Code mode where it researches and proposes a plan without changing anything. You can press Shift+Tab and ask for a plan before any files change. *First seen in Chapter 4.8.*

**Playground (AI)** — A web page where you can try a model directly, changing settings such as temperature and max tokens and seeing the effect immediately. Providers offer playgrounds for testing prompts before you build anything. *First seen in Chapter 4.15.*

**Playwright** — A tool for automating real web browsers from code, used to test websites and to let agents click through pages. The manual builds a price-watcher with Playwright MCP. *First seen in Chapter 4.19.*

**Plugin** — A bundle of skills, commands, subagents, hooks and MCP servers that you install at once. Installing one package can add a team’s review commands, skills and MCP servers to Claude Code. *First seen in Chapter 4.11.*

**Pocket assistant** — A small AI assistant that lives in a chat app on your phone, such as Telegram. You can message it from anywhere. *First seen in Chapter 6.3.*

**Polling** — Checking something again and again on a schedule, such as asking an API every minute whether a job has finished. It is the simple alternative to webhooks, which push updates to you instead. *First seen in Chapter 4.2.*

**Port (network)** — A numbered doorway on a computer that a service listens on, so other programs know where to reach it. A local model API often runs on port 11434, and a web server usually on port 80 or 443. *First seen in Chapter 4.14.*

**PostgreSQL (Postgres)** — A powerful, free, open-source database used by many web apps, including Supabase. With the pgvector extension it can also store embeddings and act as a vector database. *First seen in Chapter 2.21.*

**Power Automate** — Microsoft’s automation service for Windows and Microsoft 365, used to connect apps and automate desktop and office tasks. It is the Microsoft counterpart to Shortcuts and Zapier in the phone and desktop automation chapter. *First seen in Chapter 4.6.*

**Power stack** — The pair of tools at the heart of Section 4: n8n, which moves work along, and Notion, which holds your notes and data. Together they can run a whole household or small business. *First seen in Chapter 4.29.*

**Power Stack (n8n + Notion)** — The manual’s name for combining n8n (the automation engine) with Notion (the workspace where information lives). Together they can run almost any personal or small-business system, which is why Part XIV is devoted to them. *First seen in Chapter 4.29.*

**Pre-training** — The first, biggest stage of making a model, where it learns language by reading huge amounts of text and predicting what comes next. Everything after that — fine-tuning, RLHF and instruction training — builds on pre-training. *First seen in Chapter 2.16.*

**Precision / recall** — Two scores used to judge search and classification: precision is how many of the results you got were actually relevant, and recall is how many of the relevant results you managed to find. A good system balances both. *First seen in Chapter 5.12.*

**Production** — The live version of software that real people actually use, as opposed to a test or development copy. Running n8n in production means it must keep working, back itself up and handle errors without you watching. *First seen in Chapter 4.34.*

**Progressive disclosure** — Loading only a short summary (like a skill’s description) until the full content is needed. Claude sees a one-line skill description and loads the full instructions only when the task needs them. *First seen in Chapter 4.11.*

**Project (AI assistant)** — A workspace that groups chats with shared instructions and files, in ChatGPT, Claude, Le Chat and others. A “Kitchen renovation” project might hold your floor plan, budget and contractor quotes. *First seen in Chapter 2.2.*

**Prompt** — The instructions and content you give a model. “Write a 100-word birthday message for my grandmother, who loves gardening. Warm, not cheesy” is a prompt. *First seen in Chapter 1.6.*

**Prompt engineering** — The craft of writing prompts so a model reliably gives you what you want: clear roles, examples, constraints and the right amount of context. It also covers testing and improving prompts rather than guessing each time. *First seen in Chapter 1.6.*

**Prompt injection** — Malicious instructions hidden in content the AI reads, such as a web page or a document. Hidden text on a web page might tell an AI agent to email the user’s files to an attacker. *First seen in Chapter 2.20.*

**Prompt template (MCP prompt)** — A reusable prompt a server offers, often shown as a slash command. Typing /weekly-review might run a server’s ready-made review prompt. *First seen in Chapter 2.20.*

**Property (Notion)** — One column of a Notion database, with a type such as text, date, select or person. Automations see properties by type, so choosing the right type matters for workflows. *First seen in Chapter 3.9.*

**Prototype** — A quick, rough version of an app or idea, built to test whether it works and how it feels before you invest in the real thing. Vibe coding is often used to build a prototype in an evening. *First seen in Chapter 4.13.*

**Pull request (PR)** — A proposed set of changes on GitHub for review before merging. You review the diff a coding agent proposed before merging it into the main branch. *First seen in Chapter 4.9.*

**Push / pull (Git)** — The two ways code moves between your computer and a remote repository: push sends your commits up, and pull brings new commits down. Coding agents usually push to a branch so you can review the result as a pull request. *First seen in Chapter 4.9.*

**Python** — A friendly, widely used programming language, and the language of most AI work. The manual’s scripts, API examples and agent code are mostly Python, and it is the first language the book recommends learning. *First seen in Chapter 4.15.*

**Qdrant** — An open-source vector database, available self-hosted or as a cloud service, popular for RAG systems that need filtering as well as similarity search. *First seen in Chapter 3.4.*

**Quantization** — Compressing a model (for example to 4-bit) so it fits on smaller hardware. A 4-bit version of a 30B model fits in 24 GB instead of 60 GB. *First seen in Chapter 2.30.*

**Queue** — A waiting line for work to be done, where tasks are added at one end and processed in order at the other. Automation platforms and AI services use queues so a burst of work does not overwhelm the system. *First seen in Chapter 4.5.*

**Quick tour** — The fastest way through this book. You read the short path first, then go back for the detail when you need it. *First seen in Chapter 1.1.*

**Qwen** — Alibaba’s family of open-weight models, strong at coding and reasoning and widely used for local AI. Qwen models are a common choice for running a capable assistant on your own machine. *First seen in Chapter 2.11.*

**RAG** — Retrieval-augmented generation: fetch relevant snippets from your own documents first, then have the model answer using them. A support bot that searches the help centre and answers with links to the articles it used is RAG. *First seen in Chapter 3.3.*

**Railway** — A hosting service that deploys apps and databases from a Git repository with little configuration. It is one of the deployment options in the hosting chapter. *First seen in Chapter 4.20.*

**RAM** — Random-access memory: a computer’s short-term working memory, fast but wiped when the power goes off. More RAM lets a machine hold larger models and more open apps at once. *First seen in Chapter 2.31.*

**Raspberry Pi** — A small, cheap computer the size of a credit card, popular for home projects. A Raspberry Pi can run a home lab, a Home Assistant hub or a small local AI setup. *First seen in Chapter 2.32.*

**Rate limit** — A cap on how many requests you can make in a time window, with HTTP 429 returned when you exceed it. An automation might fail with “429 Too Many Requests” until you add a wait between calls. *First seen in Chapter 2.21.*

**Raycast** — A fast Mac launcher and command palette that can run commands, search and trigger automations with a keystroke. The manual mentions it as a desktop automation tool alongside Shortcuts and Tasker. *First seen in Chapter 4.6.*

**README** — A file named README (usually in Markdown) that explains what a project is, how to install it and how to use it. It is the first thing people read in a GitHub repository, and coding agents read it too. *First seen in Chapter 4.9.*

**Readwise** — A service that collects your highlights from books, articles and PDFs into one searchable library. It is used in the research and learning chapters as a source of material for a second brain. *First seen in Chapter 5.1.*

**Realtime / speech-to-speech model** — A model that listens and speaks directly, for low-latency voice agents. A phone agent that responds in under a second and handles interruptions naturally uses one. *First seen in Chapter 4.25.*

**Reasoning** — The step-by-step thinking a model does before answering, either internally (a reasoning model) or out loud in its working notes (chain-of-thought). More reasoning usually means better answers on hard problems, at the cost of time and tokens. *First seen in Chapter 1.1.*

**Reasoning model** — A model that “thinks” step by step before answering, improving its results on hard problems. You might choose “Thinking” mode for a tax calculation or a complex scheduling problem. *First seen in Chapter 1.2.*

**Rebase (Git)** — Rewriting a branch’s history so it sits cleanly on top of the latest main branch, instead of merging. It keeps history tidy, but it rewrites commits, so it is best used on branches only you are working on. *First seen in Chapter 1.14.*

**Recipe book** — A set of ready-made workflows in this book that you can copy and change. Each recipe says what it does and what you need. *First seen in Chapter 6.1.*

**Redis** — A very fast in-memory data store, often used as a cache or a message queue behind web apps and agents. It appears in the manual’s app-building material as shared memory between services. *First seen in Chapter 6.6.*

**Remote MCP server** — An MCP server reached over the internet (Streamable HTTP) instead of launched locally. Connecting to Notion’s hosted MCP server by URL, with nothing installed on your computer, is one example. *First seen in Chapter 2.20.*

**Render** — A hosting service for web apps, APIs and databases with a free tier, popular for putting small projects on the internet. It is one of the deployment options in the hosting chapter. *First seen in Chapter 2.20.*

**Replit** — An online platform for writing, running and publishing code in the browser, with an AI agent that can build whole apps from a description. It is one of the vibe-coding and app-building tools in this manual. *First seen in Chapter 4.13.*

**Repository (repo)** — A project folder tracked by Git, often hosted on GitHub. A repository such as github.com/your-name/recipe-box contains your code and its full history. *First seen in Chapter 1.3.*

**Reranking** — A second pass that re-orders retrieved results by relevance. A RAG system might retrieve the top 50 passages, then use a reranker to keep the best five for the answer. *First seen in Chapter 3.3.*

**Resource (MCP)** — Data a server exposes for the app or user to attach as context. Attaching notes://all from a notes server lets the AI read your notes as context. *First seen in Chapter 2.21.*

**REST API** — The common style of web API, using HTTP methods (GET, POST and so on) on URLs. GET /v1/forecast?city=London returning weather data as JSON is a REST API call. *First seen in Chapter 2.22.*

**Retrieval** — Finding the relevant pieces of information from a collection, so a model can use them to answer. In RAG, retrieval is the search step that happens before generation. *First seen in Chapter 3.3.*

**Retry** — Trying a failed step again, usually after a short wait, in case the failure was temporary. A workflow that retries an API call three times before giving up is more reliable than one that fails on the first error. *First seen in Chapter 4.3.*

**RLHF** — Reinforcement learning from human feedback: training models using people’s ratings of their outputs. It is part of why assistants follow instructions politely instead of just continuing your text. *First seen in Chapter 2.16.*

**RLS** — Row-level security: database rules so each user only sees their own rows, for example in Supabase. A Supabase policy can ensure users only ever see recipes they created. *First seen in Chapter 2.16.*

**Role (message role)** — The label on each message in a conversation with a model: system (standing instructions), user (your messages) and assistant (the model’s replies). Tools also add their own results as messages, and the model treats each role differently. *First seen in Chapter 1.6.*

**Roots (MCP)** — The folders or locations a host tells an MCP server it is allowed to work with. Roots are how a client says “you may look here” without handing over the whole computer. *First seen in Chapter 2.21.*

**RSS** — Really simple syndication: a standard way for websites to publish a feed of new items, which readers and automations can follow. An n8n workflow might watch an RSS feed and send you an AI summary of new articles every morning. *First seen in Chapter 4.20.*

**Rubric** — A list of specific criteria for scoring outputs. “1 point each: answers the question, cites a source, under 100 words, friendly tone” is a rubric. *First seen in Chapter 5.8.*

**Rug pull (MCP)** — When an MCP server quietly changes what it does after you have installed it, for example by adding new behaviour to a tool you already trusted. It is one of the security risks in the MCP security chapter, and a reason to install servers only from sources you trust. *First seen in Chapter 2.24.*

**Runtime** — The environment a program runs in, including the language, libraries and services around it. Saying “it works in my runtime” usually means the code, its dependencies and its settings are all present and correct. *First seen in Chapter 4.20.*

**Runway** — An AI company known for its video-generation models (Gen-4 and earlier) and creative tools. It is one of the video tools in the creative AI chapters. *First seen in Chapter 4.23.*

**Sampling (MCP)** — An MCP feature that lets a server ask the host app to call a model on its behalf, instead of the server calling a model directly. The host stays in control of which model is used and how much it costs. *First seen in Chapter 2.21.*

**Sandbox** — An isolated environment where code or agents run without touching the rest of your system. Running an untrusted MCP server in a Docker container with no access to your files is running it in a sandbox. *First seen in Chapter 2.35.*

**Scaffolding** — Generating the starting skeleton of a project — folders, files and boilerplate — so you begin from a working base instead of a blank page. Claude Code can scaffold a new web app before you describe what it should do. *First seen in Chapter 4.13.*

**Scope (OAuth / API)** — The specific permissions an OAuth login or an API key is granted, such as read-only access to one folder. Scopes are why “Sign in with Google” asks you to approve exactly what the app may do. *First seen in Chapter 2.20.*

**Scraping (web scraping)** — Automatically collecting information from web pages, such as prices or listings, usually with a script or an automation. The manual covers the polite and legal rules first: check for an API, respect robots.txt and do not hammer the site. *First seen in Chapter 4.7.*

**SDK** — Software development kit: a library that makes a service easy to use from a programming language. Running pip install anthropic and then calling client.messages.create(...) from Python is using Anthropic’s SDK. *First seen in Chapter 2.20.*

**Second brain** — A personal system of notes that you can search and ask questions of, so what you have learned stays findable. Notion, Obsidian and Gemini Notebook are the tools this manual builds second brains with. *First seen in Chapter 3.8.*

**Secret** — A private value a program needs to work, such as an API key, a password or a token. Secrets live in a .env file or a secrets store in a hosting dashboard, never in code or in a chat message. *First seen in Chapter 4.14.*

**Seed** — A starting value that makes random processes repeatable. In image generation the same seed and prompt give the same picture, and in training a fixed seed makes results reproducible. *First seen in Chapter 2.17.*

**Self-hosting** — Running software on your own computer or server instead of paying someone else to run it for you. Self-hosting n8n or Ollama gives you privacy and control, at the cost of looking after updates and backups yourself. *First seen in Chapter 2.10.*

**Semantic search** — Searching by meaning (with embeddings), not just exact words. Searching your notes for “ways to sleep better” and finding a note titled “evening routine” is semantic search. *First seen in Chapter 3.4.*

**Semantic versioning** — A numbering scheme for software versions (major.minor.patch) where a higher major number means breaking changes, a minor number means new features and a patch means fixes. *First seen in Chapter 6.4.*

**Server** — A computer (or a program) that provides a service to other programs, such as a website, a database or an MCP server. Your laptop can act as a server when it runs Ollama, and a hosted MCP server is a server running on someone else’s machine. *First seen in Chapter 2.20.*

**Server tool** — A tool the AI provider runs for you, such as web search, web fetch or code execution. Enabling web search in an API request without writing any search code yourself is using a server tool. *First seen in Chapter 4.15.*

**Serverless function** — Code that runs on demand in the cloud, with no server to manage. An API route on Vercel that runs only when your app calls it is a serverless function. *First seen in Chapter 4.14.*

**Session** — One continuous period of working with a program, such as a chat conversation or a logged-in visit to a website. A session ends when you close the chat or log out, and anything the program remembered only for that session is forgotten. *First seen in Chapter 3.6.*

**Shadowing (MCP)** — A security trick where a malicious MCP server imitates a trusted one — copying its name or tools — so an AI or a user picks the wrong one. It is one of the risks in the MCP security chapter, alongside tool poisoning and rug pulls. *First seen in Chapter 2.24.*

**Shortcuts (Apple)** — Apple’s automation app for iPhone, iPad and Mac, which chains actions together into shortcuts you can run with a tap or a voice command. An iPhone shortcut can post dictated text to an n8n webhook, creating a note. *First seen in Chapter 4.6.*

**Signal** — A private messaging app with end-to-end encryption, recommended in the manual for sensitive conversations. It is the secure alternative to WhatsApp or Telegram mentioned in the privacy chapters. *First seen in Chapter 2.36.*

**Siri** — Apple’s voice assistant, rebuilt in 2026 with Apple Intelligence, on-screen awareness and Gemini-based models. “Siri, send the photos from last weekend to Mom” uses its on-screen awareness and app actions. *First seen in Chapter 2.12.*

**Skill** — A folder of instructions (and optional scripts) an agent loads on demand for a specific task. An “inbox-triage” folder with instructions and a script is a skill that Claude loads when you ask it to sort notes. *First seen in Chapter 4.11.*

**Slack** — A chat app for teams, organised into channels, where AI can summarise conversations, draft replies and run automations. The manual connects Slack to n8n workflows and to agents. *First seen in Chapter 2.29.*

**Slash command** — A saved prompt you trigger by typing /name. Typing /standup might send your saved daily-update prompt. *First seen in Chapter 2.20.*

**Small language model (SLM)** — A language model small enough to run on a laptop or phone, usually under about 14 billion parameters. SLMs are fast, private and cheap, and they handle everyday tasks well even though they cannot match frontier models on hard problems. *First seen in Chapter 2.30.*

**SOP** — Standard operating procedure: step-by-step instructions for a recurring task. A written step-by-step process for onboarding clients is an SOP that an AI agent can follow. *First seen in Chapter 4.17.*

**Space (Perplexity)** — A Perplexity research folder with its own instructions and files. A “Buying our first home” Space might hold your budget, preferred areas and mortgage documents. *First seen in Chapter 2.7.*

**Spend limit** — A hard cap on API spending, set in the provider’s console. Setting a $20 monthly cap means a runaway loop cannot cost you more than that. *First seen in Chapter 2.38.*

**SQL** — Structured query language: the standard language for asking questions of databases. SELECT category, SUM(amount) FROM 'bank.csv' is a SQL query, and DuckDB runs SQL directly on files. *First seen in Chapter 5.12.*

**SQLite** — A tiny database stored in a single file, with no server to install, used inside apps and small projects. It is the simplest real database you can use, and a common choice for local tools. *First seen in Chapter 5.12.*

**SSE** — Server-sent events: a way for servers to stream updates to clients. It was the older MCP remote transport; newer servers use Streamable HTTP instead. *First seen in Chapter 2.21.*

**SSL / TLS** — The encryption layer that makes HTTPS work, scrambling data between your browser and a website. A site with a valid TLS certificate shows a padlock, and browsers now warn about sites without it. *First seen in Chapter 2.36.*

**Stable Diffusion** — A family of open image-generation models from Stability AI, free to download and run locally. It is the open alternative to Midjourney and DALL-E, and the basis of many local image tools. *First seen in Chapter 1.18.*

**STAR method** — Situation, task, action, result: a structure for interview stories. “Our launch was delayed (S), I owned the fix (T), I rebuilt the pipeline (A), we shipped a week early (R)” is a STAR answer. *First seen in Chapter 5.4.*

**Starter plan** — A simple day-by-day plan for your first month with AI. It gives you one small job a day so you learn by doing. *First seen in Chapter 1.16.*

**Stateless** — Not remembering anything between requests: each request must carry everything the program needs. API calls are stateless by default, which is why chat apps resend the conversation history with every message. *First seen in Chapter 1.18.*

**stdio / Streamable HTTP** — The two MCP transports: local (the app launches the server) and remote (connect over a URL). A filesystem server running on your laptop uses stdio, while a hosted Notion server at a URL uses Streamable HTTP. *First seen in Chapter 2.20.*

**Stop reason** — Why the model stopped: it finished, hit max tokens, wants to use a tool, paused, or refused. The API reports this so your code knows whether to show the answer, run a tool or continue. *First seen in Chapter 4.15.*

**Streaming** — Receiving the model’s output word by word as it is generated. Text appearing word by word in a chat app instead of all at once after a delay is streaming. *First seen in Chapter 4.15.*

**Streamlit** — A Python library for turning a data script into a shareable web app with a few lines of code. It appears in the data-analysis chapter as a quick way to publish a dashboard. *First seen in Chapter 5.12.*

**Stripe** — The most widely used service for taking payments online, handling cards, subscriptions and invoices through an API. Several build-alongs use Stripe when an app needs to charge for something. *First seen in Chapter 2.4.*

**Structured output** — Forcing a model’s reply to match a schema, such as valid JSON with specific fields. Getting back {"title": "...", "date": "2026-10-01", "priority": "High"} instead of a paragraph is structured output. *First seen in Chapter 2.16.*

**STT / TTS** — Speech-to-text (transcription) and text-to-speech (voice generation). Whisper transcribing a voice memo is STT; ElevenLabs reading a script aloud is TTS. *First seen in Chapter 4.11.*

**Subagent** — A helper agent with its own context, which a main agent delegates tasks to. The main agent might send a “code reviewer” subagent to check its work and receive only the summary back. *First seen in Chapter 2.16.*

**Subscription (AI plan)** — A monthly plan for an AI service, such as ChatGPT Plus or Claude Pro, that buys you higher limits and extra features for a flat fee. It is the alternative to paying per token through the API. *First seen in Chapter 1.3.*

**Suno** — An AI music service that turns a text description into a finished song with vocals and instruments. It is one of the main music-making tools in the creative chapters. *First seen in Chapter 4.24.*

**Supabase** — An open-source backend platform built on PostgreSQL, giving an app a database, logins, storage and an API with little setup. It is the database used in several of the manual’s build-alongs. *First seen in Chapter 6.6.*

**Sycophancy** — When an AI agrees with you or flatters you instead of being honest. An AI might call a weak business plan “brilliant” until you ask it to be critical. *First seen in Chapter 1.10.*

**Synthesia** — An AI video tool that turns a script into a video presented by a realistic avatar. It is used for training videos and presentations without filming anyone. *First seen in Chapter 4.21.*

**System prompt** — Standing instructions that set the model’s role, rules and style for a conversation. For example, a maths tutor’s system prompt might say to give hints, not answers, and to check understanding before moving on. *First seen in Chapter 2.16.*

**Tailscale** — A private network (VPN) that connects your devices securely without opening ports. It lets you open your home AI server on your phone from anywhere, without exposing it to the internet. *First seen in Chapter 2.32.*

**Tasker** — An Android automation app that can react to almost anything on a phone — location, time, notifications — and run actions in response. It is the Android counterpart to Apple Shortcuts in the phone automation chapter. *First seen in Chapter 4.6.*

**Telegram** — A messaging app popular for bots, channels and groups, and the platform for the manual’s pocket-assistant build-along. Its bot API makes it easy to give an AI assistant a chat front door. *First seen in Chapter 2.29.*

**Temperature** — A randomness setting for a model. Lower is more predictable and higher is more creative: 0.2 for consistent data extraction, 0.9 for brainstorming names. *First seen in Chapter 2.16.*

**Temporary chat / incognito chat** — A chat that is not saved to history or memory, and usually is not used for training. It is the right choice for a sensitive health question you do not want kept. *First seen in Chapter 1.3.*

**Terminal** — A text window where you type commands to your computer instead of clicking. Developers and local-AI users live in the terminal: installing tools, running servers and talking to coding agents all happen there. *First seen in Chapter 2.3.*

**Test set** — A set of examples with known correct answers, kept aside to check how well a system works. An eval is a test set for AI quality, and a training set is the equivalent set the model learned from. *First seen in Chapter 2.37.*

**Text-to-3D** — AI that turns a text description (or an image) into a 3D model you can view, print or use in a game. It is one of the creative techniques in the 3D and games chapter. *First seen in Chapter 4.26.*

**Text-to-image** — AI that creates a picture from a written description. Midjourney, DALL-E, Stable Diffusion and Gemini’s image models are all text-to-image tools. *First seen in Chapter 4.22.*

**TF-IDF** — A classic way to turn text into vectors by weighting rare, meaningful words more heavily. It is the simple search method in this manual’s rag-from-scratch kit, which needs no API key. *First seen in Chapter 3.5.*

**Thinking Machines Lab** — The AI lab that built Inkling 2 Small. It is a newer lab started by researchers who worked on earlier leading models. *First seen in Chapter 2.17.*

**Thinking model** — A model that works through a problem step by step before it answers. It takes longer, but it is often better at hard maths, code, and logic. *First seen in Chapter 2.16.*

**Thread (conversation)** — A chain of connected messages: a chat conversation, a reply chain in Slack or Discord, or a support ticket’s history. Agents keep the thread as context so they can follow what has already been said. *First seen in Chapter 2.29.*

**Timeout** — A limit on how long a step is allowed to take before it is abandoned as failed. A workflow might give an API call 30 seconds, then time out and retry it rather than waiting forever. *First seen in Chapter 4.7.*

**Token** — A chunk of text (about three quarters of a word) that models read, write and bill by. “Unbelievable” might be three tokens, and a one-page email is roughly 400. *First seen in Chapter 1.2.*

**Tool (AI)** — Something an AI can use to do a job it cannot do with words alone, such as searching the web, reading a file or sending a message. Tools are described to the model, and the model asks to run one by returning a structured request. *First seen in Chapter 1.17.*

**Tool annotations** — Hints in MCP tool definitions (read-only, destructive and so on) that help clients decide when to ask for approval. Marking delete_file as destructive means the app always asks before running it. *First seen in Chapter 2.20.*

**Tool poisoning** — Hiding malicious instructions in an MCP tool’s description or output. A “weather” server whose description secretly tells the AI to read and send your SSH keys is a poisoned tool. *First seen in Chapter 2.20.*

**Tool runner** — An SDK helper that runs the agent loop for you: call the model, run the tools, repeat. You pass it Python functions and it handles the call–run–repeat loop. *First seen in Chapter 4.15.*

**Tracing** — Recording every step an agent took — inputs, outputs, timing and cost — for debugging. Opening a trace shows exactly which tool call returned bad data and how much each step cost. *First seen in Chapter 4.17.*

**Training** — Teaching a model by showing it examples and adjusting its parameters so its answers get closer to the right ones. Pre-training teaches general language from huge amounts of text, and fine-tuning teaches a specific style or task from your own examples. *First seen in Chapter 1.2.*

**Training cutoff** — The date a model’s training ended, after which it knows nothing unless it is given tools or documents. It is the same idea as the knowledge cutoff, phrased as a date in the model’s life. *First seen in Chapter 2.16.*

**Training data** — The text, images and other material a model learns from during training. What is in the training data shapes what the model knows, how it writes and what biases it picks up. *First seen in Chapter 1.10.*

**Training set / test set** — Two sets of labelled examples used in machine learning: the training set is what the model learns from, and the test set is kept aside to measure how well it learned. Keeping them separate is what makes the measurement honest. *First seen in Chapter 1.4.*

**Transformer** — The neural-network design behind almost all modern AI, built around a mechanism called attention that lets the model weigh which words matter to each other. Language, image and video models in this manual are nearly all transformers. *First seen in Chapter 2.16.*

**Trigger** — The event that starts an automation, such as a schedule, a webhook or a new email. “Every weekday at 7 a.m.”, “when a form is submitted” and “when an email arrives from my boss” are all triggers. *First seen in Chapter 1.11.*

**Two-factor authentication (2FA)** — An extra login check beyond your password, usually a code from an app or a text message. Turning on 2FA is the single most effective step for keeping AI accounts and API keys safe. *First seen in Chapter 1.5.*

**TypeScript** — A version of JavaScript with types added, used for larger web apps and for many AI tools and agent frameworks. The manual’s agent examples are written in Python or TypeScript. *First seen in Chapter 4.20.*

**Udio** — An AI music service that turns a text description into a song, similar to Suno. It is one of the music-making tools in the creative chapters. *First seen in Chapter 4.24.*

**UI (user interface)** — The visible parts of a program you interact with: buttons, menus, text boxes and screens. A graphical user interface (GUI) is a UI built from windows and icons rather than typed commands. *First seen in Chapter 4.28.*

**Unified memory** — A design (for example Apple Silicon) where the CPU and GPU share one big memory pool, which is great for local AI. A Mac with 64 GB of unified memory can run models that would need several graphics cards on a PC. *First seen in Chapter 2.31.*

**Upsert** — Update a record if it exists, otherwise create it, usually matching on an ID. Searching Notion for a GitHub issue number, then updating that row or creating a new one, is an upsert. *First seen in Chapter 4.30.*

**URL** — Uniform resource locator: the address of something on the web, such as a page, an image or an API endpoint. A webhook URL is an address that runs an automation when data is sent to it. *First seen in Chapter 1.3.*

**v0** — Vercel’s AI tool for generating user interfaces from text descriptions, which produces React code you can refine and deploy. It is one of the vibe-coding tools in this manual. *First seen in Chapter 4.13.*

**VAD** — Voice activity detection: noticing when someone starts and stops speaking. It is how a voice agent knows you have started talking so it can stop and listen. *First seen in Chapter 4.7.*

**Validation** — Checking a system’s work against examples it has not seen before, to see whether it generalises or has just memorised its training data. Eval scores are a form of validation. *First seen in Chapter 2.37.*

**Variable** — A named box that holds a value a program can use and change, such as a name, a count or an API key. An environment variable is a variable set outside the program, by the system that runs it. *First seen in Chapter 2.21.*

**Vector** — A list of numbers, such as an embedding. A typical vector looks like [0.12, -0.48, 0.91, …], often with hundreds or thousands of numbers. *First seen in Chapter 3.4.*

**Vector database** — A database built to find embeddings that are “near” each other, meaning similar in meaning. Chroma, pgvector and Pinecone are vector databases used for document search bots. *First seen in Chapter 3.4.*

**Veo** — Google’s video-generation model, available in Gemini, which makes short clips with sound. Asking Gemini for an eight-second clip of a lighthouse at sunrise, with wave sounds, uses Veo. *First seen in Chapter 1.9.*

**Vercel** — A hosting service built for web apps, especially Next.js, that deploys a site from a Git repository with one click. Several of the manual’s build-alongs deploy to Vercel. *First seen in Chapter 4.14.*

**Version control** — The practice of tracking every change to a project so you can review, undo and collaborate safely. Git is the version-control system used throughout this manual. *First seen in Chapter 4.13.*

**Vibe coding** — Building software by describing what you want and letting AI write the code. Describing a family chore-chart app to Lovable or Claude Code and refining it through chat is vibe coding. *First seen in Chapter 4.13.*

**Video generation** — AI that creates moving video from a text description, an image or both. Veo, Runway, Kling and Grok Imagine are video-generation tools, used for clips from a few seconds to a minute long. *First seen in Chapter 4.23.*

**Virtual machine (VM)** — A whole computer simulated in software, running inside another computer. A VM can run a different operating system or an isolated test environment without affecting the host machine. *First seen in Chapter 2.24.*

**Vishing** — Voice phishing: a scam call in which an AI-cloned voice pretends to be a relative, a boss or a bank to get you to share codes or money. It is the phone version of phishing, made convincing by voice cloning. *First seen in Chapter 1.11.*

**Vision model** — A model that understands images. Uploading a chart screenshot and asking what trend it shows is a job for a vision model. *First seen in Chapter 4.3.*

**Vite** — A fast tool for starting and building modern web apps, popular with React and Vue projects. Vibe-coding tools often use Vite as the base for the apps they generate. *First seen in Chapter 2.22.*

**vLLM** — An open-source engine for serving language models fast, built for production use on servers with GPUs. It appears in the manual’s material on running models for apps rather than for chatting. *First seen in Chapter 2.30.*

**Voice agent** — An AI you talk to out loud that can also act for you, such as booking an appointment over the phone. A voice agent combines speech recognition, a language model and speech synthesis, and it must handle interruptions gracefully. *First seen in Chapter 4.25.*

**Voice banking** — Recording your voice so AI can create a personal synthetic voice, for example before losing speech. Someone might record a few hours of speech after an ALS diagnosis to preserve a personal synthetic voice. *First seen in Chapter 5.11.*

**Voice cloning** — AI copying someone’s voice from a short recording. It is useful for accessibility and dubbing, and misused in phone scams. *First seen in Chapter 1.11.*

**Voice mode** — Talking with an assistant out loud instead of typing, often with the ability to interrupt. Brainstorming out loud with ChatGPT, Gemini Live or Claude while cooking or walking is voice mode. *First seen in Chapter 1.4.*

**Voice receptionist** — An AI that answers phone calls for you. It greets the caller, asks what they need, and takes a message. *First seen in Chapter 4.25.*

**VPS** — Virtual private server: a slice of a real server rented by the month, where you install and run whatever you like. A VPS is a common home for self-hosted n8n or a remote MCP server. *First seen in Chapter 4.20.*

**VRAM** — Video RAM: the memory on a graphics card. It decides which models fit on a GPU: a 12 GB card comfortably runs models up to about 12–14B parameters at 4-bit. *First seen in Chapter 2.30.*

**VS Code** — Visual Studio Code: Microsoft’s free, popular code editor, and the base for Cursor. With GitHub Copilot it becomes an AI pair-programming environment, and it can also host MCP servers. *First seen in Chapter 4.12.*

**WCAG** — Web Content Accessibility Guidelines: the standard for making websites usable by everyone. Checking that text has at least a 4.5:1 contrast ratio against its background is one WCAG check. *First seen in Chapter 4.28.*

**Weaviate** — An open-source vector database with built-in support for hybrid search and for generating embeddings. It appears in the vector database comparison in this manual. *First seen in Chapter 3.4.*

**Webhook** — A URL that runs something when data is sent to it. It is how apps poke automations: an iPhone shortcut might post dictated text to an n8n webhook URL, creating a note. *First seen in Chapter 1.17.*

**WhatsApp** — Meta’s messaging app, where Meta AI can be called into group chats and where businesses run support bots. The manual uses WhatsApp as one of the chat apps an AI can live in. *First seen in Chapter 2.29.*

**Whisper** — OpenAI’s open speech-recognition model, widely used for transcription. It turns voice memos, meeting recordings and audio files into accurate text. *First seen in Chapter 4.21.*

**Windsurf** — An AI-first code editor from Codeium, similar to Cursor, with an agent that can plan and carry out multi-file changes. It is one of the AI IDEs in the coding-tools chapters. *First seen in Chapter 4.12.*

**Wireframe** — A rough, skeletal sketch of an app or web page, showing where the pieces go without any visual design. Vibe-coding tools often start from a wireframe before generating the finished design. *First seen in Chapter 4.28.*

**Worker** — A program (or part of one) that carries out jobs in the background, such as processing a queue of tasks. In multi-agent systems, worker agents do the delegated work while an orchestrator coordinates them. *First seen in Chapter 4.18.*

**Workflow** — A sequence of automated steps, often visual in n8n, Zapier or Make. A Zapier Zap or an n8n workflow that turns invoice emails into spreadsheet rows is a workflow. *First seen in Chapter 2.15.*

**Workspace** — A shared area that groups related work: a team’s chats and files in an AI assistant, or a company’s pages and databases in Notion. Projects are workspaces for one job; a Notion workspace holds everything. *First seen in Chapter 1.5.*

**Worktree (Git)** — An extra working folder of the same repo on its own branch, great for parallel agents. You can run two Claude Code sessions on two features at once, each in its own worktree folder. *First seen in Chapter 1.14.*

**World model** — An AI that generates or simulates an interactive environment you can move through. Google DeepMind’s Genie research, which generates an explorable scene from a single image, is a world model. *First seen in Chapter 4.26.*

**Zap** — Zapier’s name for one automation: a trigger plus the actions that follow it. A Zap might watch for a new form response and add a row to a spreadsheet. *First seen in Chapter 4.5.*

**Zapier** — The biggest automation platform by app catalogue, connecting thousands of apps with no-code workflows called Zaps. It is one of the three automation platforms in this manual, alongside n8n and Make. *First seen in Chapter 4.1.*

**Zed** — A fast, open-source code editor with AI features built in, written in Rust. It appears alongside Cursor and VS Code in the AI editors section. *First seen in Chapter 4.12.*

**Zero-shot** — Asking a model to do a task without giving examples. “Classify this review as positive, neutral or negative”, with no examples given, is zero-shot. *First seen in Chapter 1.6.*
