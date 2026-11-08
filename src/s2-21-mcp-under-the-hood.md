# 2.21 MCP under the hood
<!-- original: ch. 39 -->

What actually travels between your AI app and an MCP server? This chapter opens the hood. The messages. The conversation flow. How tools, resources, and prompts are described. How data moves locally and over the internet. How login works. And what changed in the big 2026 update. You will finish able to read MCP traffic and debug servers like a pro.

You do not need to code to follow this chapter. But if you ever build a server, this is the map you will use.

## Two layers: the letters and the mail truck

MCP has two layers. The **data layer** defines the messages: what you can ask, and what comes back. The **transport layer** defines how messages travel: locally or over the network.

Because these are separate, the same server logic can run locally or remotely. You just switch transports. That is a neat design. The messages stay the same. Only the delivery changes.

The two transports are **stdio** and **Streamable HTTP**. Stdio is for local servers. The app launches the server as a child process and talks to it through text streams. Streamable HTTP is for remote servers. The app sends web requests to one endpoint, and the server can stream results back.

> NOTE: Stdio is short for "standard input and output." It is just the way programs on your computer talk to each other through text.

## JSON-RPC in 60 seconds

MCP messages use **JSON-RPC 2.0**. That is a tiny, decades-old convention. JSON is a plain way to write structured data. RPC means "remote procedure call," which is a fancy way of saying "ask another program to do something." There are only three message shapes.

First, a **request**. It has an ID number and expects a reply. For example: "Call the tool roll_dice with the argument 2d6."

Second, a **response**. It carries the same ID number, plus a result or an error. For example: "2d6 gave 3 and 5, which totals 8."

Third, a **notification**. It has no ID and expects no reply. For example: "My list of tools just changed."

That is it. Every MCP feature is built from these three shapes. If you can read JSON, you can read MCP traffic.

## The conversation, step by step

A typical session goes like this. The app asks the server, "What tools do you have?" The server replies with a list, plus a description of each tool. The model sees those tools alongside your message. When you ask for something, the model picks a tool and fills in the arguments. The app calls the tool. The server runs it and sends back the result. The model writes your reply.

The app can also read **resources**. It asks for a list, then reads one by its address. And it can fetch **prompts**. It lists the templates, then fills one in with your arguments.

Older versions of MCP started every connection with an initialize handshake, to agree on a version and capabilities. The 2026-07-28 specification removed that. Requests are now stateless and self-describing. Every request carries what it needs. That lets remote servers scale like normal web services. The software libraries handle version details for you, so you rarely think about it.

| Method | Direction | Purpose |
|---|---|---|
| tools/list | App to server | "What tools do you have?" |
| tools/call | App to server | "Run this tool with these arguments." |
| resources/list, resources/read | App to server | Browse and read data the server exposes |
| prompts/list, prompts/get | App to server | Discover and fill in prompt templates |
| notifications | Server to app | "My list of tools, resources, or prompts changed." |

## Tools up close

A tool definition is what the model actually reads. It has a name, a title, a description, and an **input schema**. The schema is a formal description of the arguments: their types, which are required, and any defaults. For example, a save_note tool might take text (required) and a tag (optional, default "general").

The description is the model's only manual. It explains when to use the tool and what it returns. That is why writing clear descriptions matters so much. A vague description leads to vague behaviour. A clear one leads to correct calls.

Tools can also carry **annotations**. These are hints like read-only, destructive, or idempotent. Idempotent means running it twice has the same effect as running it once. Apps use these hints to decide when to ask you before running something.

Errors are results too. A tool that fails returns an error flag with a helpful message. The model can then adapt. "File not found, so let me list the folder first." The whole conversation does not crash.

> TRY IT: Open the MCP Inspector and connect it to any server you use. Find the tools/list reply. Read one tool description as if you were the model. Is it clear enough to use correctly? If not, you have found a bug worth reporting.

## Resources and prompts up close

Resources are identified by **URIs**. A URI is like a web address, but for any kind of data. A file might be file:///Users/you/notes/todo.md. A notes collection might be notes://all. A template might be recipes://42, which gets recipe 42. A database schema might be postgres://db/schema.

Apps usually let you attach resources to a conversation, often with an @ menu. Clients can also subscribe to changes on a resource, so they notice when it updates.

Prompts are named templates with arguments. A daily_standup template might take a focus argument. Many apps show prompts as slash commands. When you pick one, the app fetches the filled-in messages and sends them as your prompt.

## Transports: local and remote

| | Stdio | Streamable HTTP |
|---|---|---|
| How | The app launches the server and writes text lines to it | The app sends web requests to one endpoint |
| Best for | Local tools, files, dev machines | Online services, shared team servers |
| Login | Inherits your local permissions, plus API keys in settings | OAuth 2.1 or tokens in headers |
| Gotcha | Never print to the main output stream, because it corrupts the protocol | Needs HTTPS, login, and rate limiting |

What the 2026 spec changed for HTTP: no session IDs, so servers scale behind ordinary load balancers. Routing headers carry the method and tool name, so gateways can route and authorise without reading the message body. Lists can include cache hints. And when a tool needs your input mid-call, the server returns a request for more information, and the client calls back with your answer. The old HTTP-plus-SSE transport is officially deprecated.

## Authorization in one page

Remote MCP servers use **OAuth 2.1**. That is the same family of standards behind every "Sign in with Google" button. Here is the flow. Your app tries a request without a token. The server replies, "Log in here." A browser window opens. You log in and approve the permissions, called **scopes**. The app gets an access token with limited scopes. It sends that token with future requests.

Key ideas: scopes limit what the token can do. Read-only is different from write access. Tokens expire. You can revoke them from the service's settings. The app never sees your password. The spec now prefers Client ID Metadata Documents over dynamic client registration, with stricter checks on who issued the token. For you as a user, all of this happens behind one "Connect" button. Local servers usually use API keys in environment variables instead. Keep them out of shared files.

## Extensions and the spec timeline

The spec keeps growing. **Tasks** let you start a long job and check on it later. **MCP Apps** let tools return interactive screens that render in the chat. **Enterprise Managed Authorization** lets companies control which servers and scopes employees may use. Older features like sampling, roots, and logging are deprecated but still work during a transition window.

The timeline in brief: November 2024 brought the original public release. March 2025 added Streamable HTTP, OAuth, and tool annotations. June 2025 added asking the user and structured tool output. November 2025 added Tasks and auth improvements. July 2026 made the core stateless and formalised Tasks and MCP Apps as extensions. Specs are published at the protocol's official site. Clients and servers negotiate versions, and libraries usually support several at once.

> NOTE: You never need to memorise version numbers. If a server and an app both speak MCP, they will agree on a version between them.

## Check yourself

1. What are the two layers of MCP?
**Answer:** The data layer (JSON-RPC messages) and the transport layer (stdio or Streamable HTTP).

2. What are the three JSON-RPC message shapes?
**Answer:** Request (has an ID, expects a reply), response (same ID, has a result or error), and notification (no ID, no reply).

3. Why must a local server never print to its main output stream?
**Answer:** Because that stream is the protocol channel. Extra text corrupts the message stream and the client disconnects. Log to the error stream instead.

4. How should a tool report a failure?
**Answer:** Return a tool result with an error flag and a helpful message, so the model can recover instead of crashing.

5. What changed in the July 2026 specification?
**Answer:** A stateless core with no handshake or session IDs, so remote servers scale like normal web services.

## In short

- MCP is JSON-RPC messages over stdio or Streamable HTTP.
- The core loop is tools/list, then tools/call, plus resources and prompts.
- Tool descriptions and schemas are what the model actually reads.
- Errors are results too, so the model can recover gracefully.
- Remote servers use OAuth 2.1 with scopes. Local servers use API keys in settings.
- The 2026 spec made MCP stateless, cache-friendly, and gateway-friendly.
