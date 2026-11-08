# 2.22 The big MCP server catalog
<!-- original: ch. 40 -->

There are thousands of MCP servers. This is a guided tour of the ones worth knowing. They are grouped by what you would use them for. Every entry has a "try this" prompt so you can go straight from reading to doing.

How to read this catalog: **official** means made or maintained by the vendor. **Community** means built by volunteers, so check the project's activity first. **Remote** means paste a URL and log in. **Local** means it runs on your machine. Install from the vendor's remote server, from npm or PyPI, or from the official registry. Endpoints and package names change, so when in doubt, click through to the vendor's docs or search the official registry. New to installing servers? Read chapter 2.20 first.

## The starter pack

These come from the MCP project's official reference servers. Install them from npm. No account is needed.

| Server | Type | What it does | Try this |
|---|---|---|---|
| Filesystem | Local | Read, write, and search files in folders you allow | "Organise my screenshots folder into subfolders by month." |
| Fetch | Local | Grabs a web page and turns it into clean text | "Fetch these three articles and tell me where they disagree." |
| Memory | Local | A lasting knowledge graph of facts about you and your projects | "Remember that my cat is Pixel and I am allergic to cilantro." |
| Git | Local | Read and search code history, diffs, and branches | "What changed in this repo last week, in plain English?" |
| Time | Local | Time and timezone conversions | "It is 3 p.m. here. What time is it for my team in Tokyo?" |
| Sequential Thinking | Local | A scratchpad for step-by-step reasoning | "Plan a three-city Japan trip, revising the plan as you go." |
| Everything | Local | A demo server that exercises every MCP feature | Great for testing apps or learning the protocol |

Some early reference servers were archived when official vendor servers and better community versions took over. That is a sign of a healthy ecosystem, not a broken one.

> NOTE: Start with the starter pack. One server you understand beats ten you installed and forgot.

## Developer and DevOps

| Server | Type | What it does | Try this |
|---|---|---|---|
| GitHub | Remote | Repos, issues, pull requests, actions, code search | "Summarise open issues labelled bug and draft a triage plan." |
| GitLab | Remote | Projects, merge requests, issues, pipelines | "Why did the last pipeline on the main branch fail?" |
| Playwright | Local | Drives a real browser: click, type, screenshot | "Go to my website, fill out the contact form, and tell me if anything breaks." |
| Chrome DevTools | Local | Performance traces, console, network inspection | "Why is this page slow? Record a trace and explain it." |
| Context7 | Remote | Pulls current library docs into context | "Show me the current way to do login in Next.js." |
| DeepWiki | Remote | Ask questions about any public code repo's design | "How does routing work in this open-source project?" |
| Sentry | Remote | Errors, stack traces, issues | "What is the most common error this week, and where is the bug?" |
| Datadog | Remote | Metrics, logs, monitors, incidents | "What changed right before yesterday's slowdown?" |
| Vercel | Remote | Deployments, logs, projects | "Why did my last deploy fail?" |
| Cloudflare | Remote | Workers, DNS, analytics, docs | "Show me traffic to my site over the last seven days." |
| Docker MCP Toolkit | Local | A catalog of containerised servers, one-click installs | Run untrusted servers safely inside containers |
| AWS | Remote | A family of AWS servers: docs, costs, and more | "What is costing me the most on AWS this month?" |
| Desktop Commander | Local | Terminal commands and file editing from Claude Desktop | Powerful, so scope it carefully |

## Productivity, docs, and project management

| Server | Type | What it does | Try this |
|---|---|---|---|
| Notion | Remote | Search, read, create, and update pages and databases | "Turn this meeting transcript into a Notion page with action items." |
| Linear | Remote | Issues, projects, cycles | "Create issues for each bug in this list, with priorities." |
| Atlassian (Jira + Confluence) | Remote | Tickets, pages, search | "Write release notes from tickets closed this sprint." |
| Asana | Remote | Tasks, projects, portfolios | "What is overdue across my projects? Draft nudges to the owners." |
| Todoist | Remote | Tasks and projects | "Break 'plan my sister's birthday party' into tasks with due dates." |
| Slack | Remote | Search messages, read channels, send messages | "Catch me up on the product channel from this week in five bullets." |
| Gmail, Calendar, Drive | Remote | Mail, events, docs | "Find a 30-minute slot next week and draft the invite." |
| Microsoft 365 | Remote | Outlook, Teams, SharePoint, OneDrive | "Summarise the Teams thread I missed." |
| Airtable | Remote | Bases, tables, records | "Add these 20 leads to my CRM base, without duplicates." |
| DocuSign | Remote | Envelopes, agreements, status | "Which contracts are still waiting on signatures?" |
| Obsidian | Local | Your local vault via a plugin | "Find notes about habits and build a page linking them." |
| Basic Memory | Local | AI memory stored as plain text files you own | Build a second brain that both you and AI can edit |

## Business, sales, support, and payments

| Server | Type | What it does | Try this |
|---|---|---|---|
| HubSpot | Remote | CRM contacts, deals, companies | "Which deals have not been touched in two weeks?" |
| Salesforce | Remote | Accounts, opportunities, records | "Prep me for my call with Acme: open deals, recent activity." |
| Intercom | Remote | Conversations, contacts, help centre | "What are customers asking about most this week?" |
| Stripe | Remote | Customers, payments, invoices, docs | "Create a payment link for my $25 workshop." |
| Square | Remote | Payments, catalog, orders | "What were my best-selling items last month?" |
| PayPal | Remote | Invoices, transactions, disputes | "Send an invoice to this client for last month's work." |
| Shopify | Remote | Dev docs and API help, plus storefront tools | "Help me build a Shopify app that tags VIP customers." |
| Webflow | Remote | Sites, CMS collections, pages | "Add these five blog posts to my CMS as drafts." |

Money tools deserve extra care. Anything that moves money, sends invoices, or refunds should always ask before acting. Use test modes while you experiment.

> NOTE: Start read-only with money and customer tools. Let the AI explore and explain before you ever give it write access.

## Web search, research, and data

| Server | Type | What it does | Try this |
|---|---|---|---|
| Brave Search | Remote | Web, news, and image search | "What launched in AI this week? Cite sources." |
| Exa | Remote | Semantic search built for AI | "Find ten indie blogs about home automation." |
| Tavily | Remote | Search and extraction tuned for agents | "Research the top five note-taking apps and build a comparison." |
| Perplexity | Remote | Perplexity's answer engine as a tool | "Ask Perplexity for the latest on X, then critique its sources." |
| Firecrawl | Remote | Crawl whole sites and extract structured data | "Crawl this docs site and make me a study guide." |
| Apify | Remote | Thousands of ready-made scrapers | "Find the top-rated coffee shops near me into a table." |
| PubMed | Remote | Biomedical literature search | "Find five recent studies on sleep and memory, explained simply." |
| arXiv | Remote | Search and read research preprints | "What are the newest papers on small language models?" |
| Supabase | Remote | Tables, SQL, migrations | "Design a schema for a habit tracker and create it." |
| Neon | Remote | Serverless Postgres with branching | "Branch my database, try this change, and show me the diff." |
| MongoDB | Remote | Query and manage MongoDB | "What is the shape of the documents in orders?" |
| Snowflake | Remote | Search, analysis, and SQL | "Which region's revenue grew fastest last quarter?" |
| MotherDuck / DuckDB | Local and remote | SQL on local files and the cloud | "Query these three CSVs together and chart the trend." |

## Creative, design, and media

| Server | Type | What it does | Try this |
|---|---|---|---|
| Figma | Remote | Gives coding agents your designs and tokens | "Build this Figma frame as a component matching our tokens." |
| Canva | Remote | Create, search, and edit designs | "Make three Instagram post options for my bake sale." |
| Blender MCP | Local | Claude controls Blender: models, materials, scenes | "Build a low-poly island with a lighthouse at sunset." |
| ElevenLabs | Remote | Text-to-speech, voices, sound effects | "Narrate my blog post in a warm storyteller voice." |
| Hugging Face | Remote | Search models, datasets, papers, and demos | "Find a good open model for transcribing Spanish audio." |
| Replicate | Remote | Run thousands of open image, video, and audio models | "Generate four logo concepts for my plant shop." |
| fal | Remote | Fast media generation models | "Turn this photo into a short looping animation." |

## Life, home, health, and fun

| Server | Type | What it does | Try this |
|---|---|---|---|
| Home Assistant | Local | Your smart home as tools | "Movie mode: dim the living room to 20 percent." |
| Spotify | Remote | Search, play, and build playlists | "Make a 90-minute focus playlist with no lyrics." |
| Google Maps | Remote | Places, directions, distances | "Plan a walking route between these five cafes." |
| Weather | Remote | Forecasts | "Should I bike to work tomorrow?" |
| Strava | Remote | Your workouts | "How has my running pace trended this year?" |
| Apple apps | Local | Notes, Reminders, Calendar, Messages on a Mac | "Add everything from this email to my Reminders." |

Health and money tools inform. They do not decide. They are great for understanding and preparing questions. Big medical or financial decisions still belong with qualified humans.

## Meta-servers and where to find more

**Meta-servers** are servers that unlock thousands of apps at once. Zapier MCP exposes actions from thousands of apps. You pick exactly which ones the AI may use. Pipedream offers thousands of APIs with managed login. Composio offers hundreds of toolkits with login handled. n8n can turn any workflow into an MCP tool. Make can expose its scenarios as tools.

To find more servers, use the official MCP Registry, the canonical community-owned registry. Browse your AI app's built-in directory. Check the GitHub MCP Registry, the Docker MCP Catalog, and community lists. Searchable directories with usage stats also exist.

> TRY IT: Pick one server from three different categories above. Give your AI a task that needs all three. For example: research five new servers, then save a ranked page to Notion. That is a real multi-tool agent run.

## Judging a random server in 30 seconds

Before you install a server you have never heard of, run this check. Is the source official, the registry, or a reputable maintainer? Is the project active, with recent updates and real users? Do the requested permissions match the job? Open it in the MCP Inspector and read the tool descriptions. Anything weird, pushy, or instructing the AI to do extra things? Is the version pinned to an exact number? Can it run in Docker or with read-only credentials? The full checklist is in chapter 2.24.

## Check yourself

1. What is the difference between an official server and a community server?
**Answer:** Official servers are made or maintained by the vendor. Community servers are built by volunteers and need a quick trust check first.

2. Which server drives a real browser to click and type?
**Answer:** Playwright, or Chrome DevTools for performance traces and inspection.

3. Which server pulls current library documentation into context?
**Answer:** Context7.

4. What is a meta-server?
**Answer:** A server that exposes thousands of apps at once, like Zapier MCP or Pipedream, so one connection unlocks many tools.

5. What is the first step before installing an unknown server?
**Answer:** Check its source, activity, permissions, and tool descriptions, ideally in the MCP Inspector.

## In short

- There is an MCP server for almost everything: code, docs, business, data, creative work, home, and life.
- Prefer official servers. Treat community ones with a quick trust check.
- Meta-servers unlock thousands of apps at once.
- Use the official registry and trusted directories to discover more.
- Start read-only, keep approvals on for money and messages, and enable only what you need.
