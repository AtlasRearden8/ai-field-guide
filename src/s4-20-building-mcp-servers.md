# 4.20 Building MCP servers
<!-- original: ch. 42 -->

Using MCP servers is fun. Building them is a superpower. Any API, script, database, or gadget you can talk to with code can become a tool that every AI app can use. This chapter takes you from a first server in five minutes to a remote, authenticated server that you can publish for others to use.

You met MCP in Chapter 2.20. It is a standard plug that lets AI use your tools. Think of it as USB-C, but for AI apps. This chapter is the deep dive for builders who want to make the plug themselves.

## Step 0: Decide what your server should do

Before you write any code, answer three questions. What is the one job this server does? Who will use it? And what tools does it need to offer?

A good first server does one small job, with one to three tools. A server that checks the weather in a city. A server that searches your notes. A server that adds a row to a spreadsheet. Small servers are easy to test, easy to explain, and easy to trust.

Write down the tools before you code. For each tool, write its name, one sentence that says what it does, and the inputs it needs. That list is your plan. If you cannot write the list, the server is not ready to build yet.

> NOTE: A server with three clear tools beats a server with twenty vague ones. AI apps choose tools by reading their descriptions. Clear descriptions are the whole game.

## Step 1: Your first server in five minutes

You need Python 3.10 or newer, or Node.js 20 or newer. Pick the language you are most comfortable with. Both have an official MCP SDK, which is a toolkit that turns your functions into MCP tools.

Start from a tested starter kit. The MCP project publishes starter kits in both Python and TypeScript. Copy one, and run it. Confirm it starts without errors. Then connect it to an AI app, such as Claude Desktop, and ask the AI to use it.

Here is the smallest Python server, using the official SDK. Read it line by line. The comments explain what each part does.

```
from mcp.server.fastmcp import FastMCP

  # Make a server, and give it a name.
mcp = FastMCP("hello")

  # Turn this function into a tool the AI can call.
@mcp.tool()
def say_hello(name: str) -> str:
    """Say hello to a person, by name."""
    return f"Hello, {name}!"

  # Run the server.
if __name__ == "__main__":
    mcp.run()
```

Line one loads the toolkit. Line four makes a server called hello. Line seven marks the function below it as a tool. Lines eight to ten define the tool: it takes a name, and returns a greeting. The short sentence in quotes is the description the AI reads. Lines thirteen and fourteen run the server when you start the file.

That is a working MCP server. It does one tiny job. But it proves the whole idea: write a function, describe it clearly, and any AI app can call it.

## Step 2: Write tools the AI will use well

A tool is a promise. It says "I can do this one thing, and here is what I need." Write the promise well, and the AI will use the tool well.

Use clear names. `get_weather` is good. `do_thing` is not. Write descriptions in plain words. Say what the tool does, when to use it, and what it returns. "Get the current weather for a city. Use it when the user asks about the weather. Returns the temperature and a short description." That is a good description.

Keep inputs simple. A city name is a good input. A list of ten options with codes is not. If a tool needs a complicated input, split it into two simpler tools, or give the complicated part a sensible default.

Return short, useful results. A tool that returns a page of text forces the AI to read a page. A tool that returns three facts is easy to use. If the result is long, summarise it before you return it.

## Step 3: Structured output and errors

Sometimes a tool should return data, not prose. That is **structured output**. Instead of returning a sentence, return JSON with fixed labels, like `{"temperature": 18, "condition": "sunny"}`. The AI can read those labels directly, and pass them to another tool without guessing.

Errors matter just as much. When a tool fails, it should say why, in words the AI can act on. "No city with that name was found. Try a larger nearby city." is a good error. "Error 500" is not. A good error tells the AI what went wrong, and what to try next.

Test your errors. Call each tool with a bad input, on purpose. Read the error it returns. If a person could not act on it, rewrite it.

> TRY IT: Take the hello server above. Add a second tool called `add_numbers` that takes two numbers and returns their sum. Give it a clear description. Run the server, connect it to an AI app, and ask the AI to add two numbers. You have just extended an MCP server.

## Step 4: Resources and prompts

Tools are not the only thing a server can offer. It can also offer **resources** and **prompts**.

A resource is a piece of information the AI can read, like a file, a page, or a record. For example, a notes server might offer each note as a resource, so the AI can read it directly, without calling a tool.

A prompt is a saved instruction the AI can use, like a template. For example, a writing server might offer a prompt called "summarise this note in three bullets." The user picks the prompt, and the AI fills in the details.

You do not need resources and prompts in your first server. Add them when a tool feels like the wrong shape for the job. If the AI needs to read something, that is a resource. If the user needs a reusable instruction, that is a prompt. If the AI needs to do something, that is a tool.

## Step 5: Test like a pro

Test your server in three ways. First, run it and watch it start without errors. Second, connect it to an AI app and ask the AI to use each tool, including with bad inputs. Third, use the **MCP Inspector**, which is a tool that lets you inspect a server: it lists the tools, lets you call them by hand, and shows you exactly what goes in and out.

The Inspector is the best debugging tool for MCP. If a tool does not work in the Inspector, it will not work in an AI app. Fix it there first.

Also write a **smoke test**. That is a tiny script that starts your server, calls each tool once, and checks that the answers look right. Run it after every change. It takes minutes to write, and it catches most breakages before your users do.

## Step 6: Go remote with Streamable HTTP

So far, your server runs on your own computer, and an AI app on the same computer connects to it. That is called a **local** server. It is private, fast, and simple.

A **remote** server runs on a host, and AI apps connect to it over the internet. To go remote, your server needs to speak **Streamable HTTP**, which is the way MCP servers talk over the web. The official SDK supports it. You change how the server starts, from a local connection to an HTTP one, and you deploy it to a host, as Chapter 4.14 showed you.

A remote server needs a public address. It also needs to stay on. Use a host that runs code all the time, such as Railway, Render, or Fly.io. Deploy the server, copy its address, and connect an AI app to that address. If it works, your server is now available to anyone with the address.

## Step 7: Authentication

A local server on your own computer needs little security, because only you can reach it. A remote server needs **authentication**, which is a way to check who is calling, before you let them in.

The common way is a token, which is a secret pass that the caller must send with each request. You give a token to each person or app you trust. If someone does not have a token, the server refuses them.

Keep tokens secret, like passwords. Give each user their own token, so you can take one away without breaking the others. And never put a token in code, in a screenshot, or in a public place. Store it in an environment variable, as Chapter 4.14 explained.

Also think about **scopes**, which are limits on what a token may do. A token that can only read is safer than a token that can read and write. Give each token the smallest scope that lets its owner do their job.

## Step 8: Publish it

When your server works, and you are ready to share it, you can publish it to the official MCP registry. The registry is a public list of MCP servers, where people can find servers to use.

Before you publish, check three things. Does the server do what its description says? Does it handle bad inputs gracefully? And have you removed any secrets from the code? If yes to all three, publish it, and write a short description that says what it does, in plain words.

Publishing is optional. Many good servers are never published. They serve one person, or one team, and that is enough. Publish when you want others to find and use your work.

## Step 9: Level up

Once you have a published server, you can grow it in several directions. Add more tools, one at a time. Add resources for data the AI should read. Add prompts for jobs users repeat. Add better logging, so you can see how people use it. Add tests that run automatically, so changes do not break it.

You can also connect your server to other systems. A server that reads a database can answer questions about your data. A server that talks to an API can give AI apps access to that API. Each new connection makes the server more useful, and more worth keeping safe.

> NOTE: A server that can change things, like deleting files or sending messages, needs more care than a server that only reads. Add authentication, add scopes, and add a human check before any action that reaches outside the server.

## Check yourself

1. What is an MCP server, in plain words?
**Answer:** A program that offers tools, resources, or prompts to AI apps, through the MCP standard plug, so any AI app can use them.

2. What are the three things a server can offer?
**Answer:** Tools, which do things; resources, which are information the AI can read; and prompts, which are saved instructions.

3. Why should tool descriptions be written in plain words?
**Answer:** Because AI apps choose tools by reading their descriptions, so a clear description leads to the tool being used correctly.

4. What is the MCP Inspector?
**Answer:** A tool that lists a server's tools, lets you call them by hand, and shows exactly what goes in and out, for testing and debugging.

5. What is authentication for a remote server?
**Answer:** A way to check who is calling, usually with a secret token, before letting them use the server.

## In short

- Decide the server's one job and its tools before you write any code.
- Start from a tested starter kit, and confirm it runs.
- Write tools with clear names, plain descriptions, simple inputs, and helpful errors.
- Return structured data when another program will read the result.
- Test with the MCP Inspector and a smoke test after every change.
- Go remote with Streamable HTTP, add authentication, and publish only when you are ready to share.
