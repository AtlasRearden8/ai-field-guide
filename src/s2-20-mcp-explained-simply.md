# 2.20 MCP, explained simply
<!-- original: ch. 38 -->

**MCP** stands for Model Context Protocol. It is the open standard that lets any AI app plug into any tool or data source. Think USB-C, but for AI apps. Before USB-C, every gadget had its own charger. Now one cable charges your phone, laptop, and headphones. MCP does the same for AI. One standard plug. Endless things to connect.

This is one of the most important ideas in this book. Once it clicks, you will see how AI grows hands and eyes. You will be able to give your own AI new superpowers in minutes.

## The problem MCP solves

Before late 2024, connecting an AI app to a tool meant writing a custom integration for that exact pair. Claude needed its own code-host integration. ChatGPT needed its own. Cursor needed its own. If there are M AI apps and N tools, that is M times N integrations. Nobody could keep up.

MCP flips that to M plus N. Each AI app implements MCP once. Each tool implements MCP once. Then everything works with everything. Anthropic introduced MCP as an open standard in November 2024. It spread fast. By 2026 it is supported by Claude, ChatGPT, Gemini, Microsoft Copilot, Cursor, VS Code, n8n, Zapier, Notion, and hundreds of others. In December 2025, Anthropic donated MCP to the Agentic AI Foundation, part of the Linux Foundation. It is now governed as a neutral open project, with a public specification and an official server registry.

The USB-C analogy even covers the downside. A cheap cable from a sketchy shop can fry your laptop. The same goes for random MCP servers. Safety gets its own chapter later. For now, know the rule: install from trusted sources.

> NOTE: MCP is a standard, not a product. Nobody owns it. Any app can speak it, and any tool can offer it.

## The three roles: host, client, server

MCP has three roles. Learn them once and the whole system makes sense.

- **Host.** The AI app you actually use. Claude Desktop, Claude Code, ChatGPT, Cursor, VS Code, n8n. The host is built by the app makers.
- **Client.** The connection manager inside the host, one per server. It is built into the host and invisible to you.
- **Server.** A small program that exposes a service in MCP's format. A GitHub server, a Notion server, a Filesystem server, or your own server. Servers are built by service vendors, the community, or you.

Here is the key insight. The model never talks to GitHub directly. The model says, "I would like to call create_issue with these details." The host's client passes that to the GitHub server. The server calls GitHub's service. The result flows back. The server is the translator. The host is the security guard that decides what is allowed.

## What a server can offer

A server can offer three kinds of things.

- **Tools.** Actions the model decides to call. Create an issue. Send a message. Search files. Roll dice. Tools are about 90 percent of what people use day to day.
- **Resources.** Read-only data the AI can use as context. A file. A database schema. Your notes. You or the app choose to attach them.
- **Prompts.** Reusable templates with arguments. A daily standup template. A code-review template. A meeting-summary template. Many apps show them as slash commands.

Newer extras exist too. A server can ask you a question mid-task, like "Which calendar should I add this to?" A server can return an interactive screen, like a form or a chart, that renders right in the chat. A server can start a long job and let you check on it later. And servers can mark tools as read-only or destructive, so apps know when to ask you first. You do not need any of these on day one. It is good to know they exist.

## Local versus remote servers

Servers come in two flavours. **Local** servers run on your computer. The app launches them with a command. They are great for your files, local apps, dev tools, and private experiments. They usually need Node.js or Python installed. A Filesystem server pointed at one folder only sees that folder. That scoping matters a lot.

**Remote** servers run on a server somewhere else. You reach them by pasting a URL, then logging in. They are great for online services like Notion, Linear, GitHub, and Stripe. Setup is usually one click and a login. You trust the vendor's server and the permissions you approve.

The 2026 trend is clear. Most big online services now run official remote servers with one-click login. Local servers remain king for anything on your own machine.

| | Local server | Remote server |
|---|---|---|
| Runs | On your computer | On a server somewhere, reached by URL |
| Setup | A command in a config file | Paste a URL, then log in |
| Great for | Your files, local apps, dev tools | Online services like Notion and Linear |
| Needs | Usually Node.js or Python | Nothing but a browser to log in |
| Trust | Runs code on your machine, so install carefully | You trust the vendor and the scopes you approve |

## How a tool call actually flows

Here is what happens when you ask your AI to file a bug report. First, you type your message. The app sends your message plus the list of tools to the model. The model picks a tool and fills in the details. Then the app asks you: allow this call? You say yes. The client passes the call to the server. The server does the real work. The result flows back. The model writes you a reply: "Done! I filed the issue."

Notice the approval step. It lives in the host, not the model. That is why good apps let you set each tool to always allow, ask every time, or never. Keep "ask every time" on for anything that sends, deletes, shares, or spends.

## Installing servers, app by app

In Claude, the easiest path is Settings, then Connectors. Browse the directory, click, log in. Done. For a custom remote server, paste its URL. For a local server on Desktop, add it to the config file and fully restart the app. Desktop Extensions are one-click installable local servers. Double-click and go.

In Claude Code, use commands in the terminal to add servers, list them, and check status. Inside a session, a built-in command shows status and handles logins. In Cursor, use Settings, then MCP, or edit the config file. Many vendor docs have an "Add to Cursor" button. In VS Code, use the Command Palette to add a server, or edit the config file. ChatGPT connects to remote servers through plugins and Developer Mode. Full read-and-write access depends on your plan, so check the current price and plan details.

Everywhere else, the shape is nearly the same. Codex, Windsurf, Zed, LM Studio, Goose, n8n, Raycast. Learn it once and use it everywhere.

> TRY IT: In your AI app, open Settings and find Connectors. Connect one app you use daily, like your calendar or notes. Then ask: "What can you do with this connection now?" Fifteen minutes, one new superpower.

## Debugging MCP like a pro

Things go wrong sometimes. Here are the common fixes.

- **Server does not appear at all.** Quit the app completely, not just close the window. Check the config file for a typo. One trailing comma breaks everything.
- **"Command not found."** Desktop apps often cannot see your terminal's tools. Use the full path to the command instead.
- **Connects, then disconnects instantly.** The server crashes on startup. A missing API key is the usual cause. Run the command in a terminal to see the error.
- **No tools listed.** The server printed junk to its output stream. Local servers must log to a separate channel, never the main output.
- **Login loop for remote servers.** Allow pop-ups. In Claude Code, use the built-in status command. Ask your admin if it is a work account.
- **The AI ignores the tools.** Too many tools, or a vague request. Mention the tool by name. Disable servers you are not using.

A free tool called the **MCP Inspector** lets you call any server's tools by hand in a web page. Ten minutes with it, and MCP stops feeling like magic.

> NOTE: More servers does not mean a smarter AI. Every tool description eats context and gives the model more chances to get confused. Enable what the task needs.

## Check yourself

1. What does MCP stand for, and what does it do?
**Answer:** Model Context Protocol. It is an open standard that lets any AI app plug into any tool or data source.

2. What are the three roles in MCP?
**Answer:** Host (the AI app), client (the connection inside the host), and server (the program that exposes a service).

3. What is the difference between a tool, a resource, and a prompt?
**Answer:** A tool is an action the model calls. A resource is read-only data you attach. A prompt is a reusable template you choose.

4. When should you pick a local server over a remote one?
**Answer:** For things on your own machine, like files, local apps, and dev tools. Remote servers suit online services.

5. A server does not appear after you add it. What do you check first?
**Answer:** Did you fully restart the app, and is the config file valid, with no trailing commas?

## In short

- MCP turns M times N custom integrations into M plus N plug-and-play connections.
- Hosts contain clients that talk to servers. The host enforces permissions.
- Servers offer tools, resources, and prompts, plus newer extras like interactive screens.
- Remote servers mean paste a URL and log in. Local servers mean running a command.
- Scope tightly, keep approvals on for risky tools, and install from trusted sources.
