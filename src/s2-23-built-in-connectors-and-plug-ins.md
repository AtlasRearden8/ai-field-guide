# 2.23 Built-in connectors and plug-ins
<!-- original: ch. 41 -->

MCP is the engine. Connectors are the polished, click-to-install version inside the big AI apps. If you want results today with zero config files, start here. You will learn what each major assistant offers, how connectors differ from skills and plug-ins, the best combos, and how to keep permissions tidy.

A **built-in connector** is a ready-made link between your assistant and another app. Choose an app from a directory. Sign in. The assistant can now work with it. No config files. No code.

## Connectors versus MCP versus skills versus plug-ins

These four words get mixed up. Here is the difference.

| | Built-in connector | Raw MCP server | Skill | Plug-in or bundle |
|---|---|---|---|---|
| What it is | A ready-made link to one service | Any MCP server you configure | Packaged instructions for a task | A bundle of connectors, skills, and commands |
| Setup | Click, then log in | Config file or URL | Upload or install | One install |
| Under the hood | Usually MCP | MCP | Files the AI loads when relevant | A mix of the above |
| Best for | Everyday apps like Gmail, Drive, Notion, Slack | Niche tools, local files, your own code | Repeatable workflows | A whole role or workflow at once |

The rule of thumb is simple. Use the connector if one exists. Drop to raw MCP when it does not, or when you want something local or custom. Add skills when you keep explaining the same process over and over.

> NOTE: A connector gives the AI access to an app. A skill gives it know-how for doing a task well. You often need both.

## Claude

Claude's connectors live in Settings, under Connectors. One click connects Google Workspace, Notion, Slack, GitHub, Linear, Asana, Atlassian, Canva, Figma, Stripe, DocuSign, and many more. Custom connectors let you paste any remote MCP server URL. Desktop Extensions are one-click local servers for Claude Desktop.

Claude also has **skills**. These are packaged instructions and scripts that Claude loads on demand. "Make a deck in our brand style" is a skill. "Fill in this PDF form" is a skill. You can write your own. **Plug-ins** bundle connectors, skills, and commands for a whole role or workflow. **Projects** hold standing instructions and files per project, plus memory across chats. **Artifacts** let Claude build live mini apps, documents, and dashboards you can share. **Research** runs multi-step research across the web and your connectors, with citations.

## ChatGPT

ChatGPT connects to remote MCP servers through **plugins** and Developer Mode, where you can add any remote MCP server. Full read-and-write access depends on your plan. Check the current price and plan details before you rely on it. Connectors cover Drive, Gmail, Calendar, SharePoint, GitHub, and more. They work in chat and in deep research.

**Agent mode** is a browser and terminal agent for multi-step web tasks. **Projects** are workspaces with instructions and files. **Skills** inside plugins replace custom GPTs, which retire on December 11, 2026. Build on plugins instead. Scheduled tasks run recurring jobs. Memory remembers preferences across chats. You can view and edit what it remembers.

## Google Gemini and Microsoft Copilot

Gemini is deeply tied to Google's apps. **Personal Intelligence**, if you opt in, lets Gemini use your Gmail, Calendar, Drive, Photos, YouTube, and Maps to answer questions about your life. **Gems** are custom assistants with standing instructions. **Deep Research** writes long, cited reports from the web and your files. **Canvas** is a live document or code editor beside the chat. **Gemini Notebook** is grounded research on your chosen sources, with audio overviews. The **Gemini CLI** is an open-source terminal agent that speaks MCP.

Microsoft Copilot comes in two forms. The Copilot app connects to your Microsoft 365 files and email. Microsoft 365 Copilot works across Outlook, Teams, Word, Excel, PowerPoint, and SharePoint using your work data. **Copilot Studio** lets organisations build agents with connectors, actions, and MCP tools. **Power Platform** connectors plug into Power Automate flows. GitHub Copilot brings agents and MCP to coding.

## Others worth knowing

| App | Connector story |
|---|---|
| Perplexity | Search-first AI with connectors for Gmail, Calendar, Notion, GitHub, and more, plus local MCP in its desktop app |
| Mistral Vibe | 20-plus MCP connectors and custom MCP connectors on every plan |
| Grok | Web and X search built in; fewer third-party connections so far |
| Meta AI | Lives inside WhatsApp, Instagram, and Facebook; limited outside connections |
| Alexa+ | Connects to smart home devices and services like groceries, rides, and reservations |
| Notion AI | Its own agents plus MCP connections to other tools |
| Slack | AI features and agents inside Slack, plus an official MCP server |
| Raycast | System-wide AI on Mac and Windows, with extensions and MCP |
| Apple | The rebuilt Siri, with personal context and app actions, ChatGPT integration, and Shortcuts that call AI models |

## Ten connector combos that feel like magic

Cross-app prompts create the biggest wins. One connector is useful. Two or three together feel like magic.

| Combo | Prompt |
|---|---|
| Gmail + Calendar | "Find emails where someone asked to meet and I have not replied. Propose times that fit my calendar and draft replies." |
| Drive + Notion | "Read my last five meeting-notes docs and build a Notion project tracker from the action items." |
| Slack + Linear | "Scan the bugs channel this week and file Linear issues for anything not already tracked." |
| GitHub + Slack | "Write a friendly weekly changelog from merged pull requests and post it to updates." |
| Canva + Drive | "Take the stats from my Q3 doc and make an infographic in Canva." |
| Calendar + web search | "For each external meeting this week, research the company and give me three talking points." |
| Gmail + Sheets | "Find every receipt email from last month and list vendor, date, and amount in a sheet." |
| Notion + Research | "Research the best beginner telescopes under $500 and save a comparison page to Notion." |
| DocuSign + Gmail | "Which contracts are waiting on signatures? Draft polite nudges to each signer." |
| Drive + a skill | "Using our brand-deck skill, turn this strategy doc into a ten-slide deck." |

> TRY IT: Connect two apps you use daily and run one combo from the table above. Cross-app tasks are where the time savings really show up, often 30 minutes or more on the very first try.

## Permissions and approvals

Most apps let you set each tool to always allow, ask first, or never. Ask first for anything that sends, deletes, buys, shares, or posts publicly. When a connector asks for scopes, prefer read-only if that is all you need. That is called **least privilege**: give only the access the job needs.

Revoke anytime. Disconnect in the AI app. Also remove access in the service's security settings, like your Google account's third-party access page. Turn off unused connectors. Fewer tools means a more focused AI and a smaller risk.

At work, admins often choose which connectors are available and who can use them. Company data policies may restrict connecting personal accounts to work assistants, and vice versa. If a connector you need is not available, ask IT. Explain the task and the data involved. That makes a "yes" more likely. Many companies route MCP through gateways that log and control access.

## Connector, MCP server, or automation?

| You want… | Use |
|---|---|
| To ask your AI about your email, docs, or tasks, when you feel like it | Connector |
| A tool no connector covers, like local files or a niche app | MCP server |
| Something to happen automatically, on a schedule or trigger | Automation |
| A repeatable multi-step process done the same way every time | Skill or automation |
| A whole team setup in one go | Plug-in |

> NOTE: Connectors are for when you ask. Schedules and triggers belong to automation platforms. Mixing them up is how surprise actions happen.

## Check yourself

1. What is the difference between a connector and a skill?
**Answer:** A connector gives the AI access to an app or data source. A skill gives it packaged know-how for doing a task well.

2. When should you use raw MCP instead of a built-in connector?
**Answer:** When no connector exists for the tool you need, or when you want something local or custom.

3. What approval setting should sending, deleting, and paying use?
**Answer:** Ask first, or never, until you trust the setup.

4. What is least privilege?
**Answer:** Giving only the access the job needs, such as read-only when that is all you need.

5. When should you use an automation instead of a connector?
**Answer:** When something should happen on its own, on a schedule or trigger, rather than when you ask.

## In short

- Connectors are click-to-install MCP inside AI apps, and the fastest path to value.
- Claude, ChatGPT, Gemini, and Copilot all have connector ecosystems, plus skills and plug-ins.
- Cross-app prompts with two or three connectors create the biggest wins.
- Keep ask-first on for risky actions, grant least privilege, and revoke what you do not use.
- Connectors are for asking. Automations are for schedules and triggers.
