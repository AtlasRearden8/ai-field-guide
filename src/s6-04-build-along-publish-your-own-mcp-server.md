# 6.4 Build-along: publish your own MCP server
<!-- original: ch. 113 -->

In this build you will take a real MCP server from "works on my machine" to "anyone in the world can install it." **MCP** is a standard plug that lets AI use outside tools. An **MCP server** is a small program that offers tools to an AI through that plug.

You will run and test Weather Buddy, a server that gives live weather, forecasts, and packing advice. It uses the free Open-Meteo API. Open-Meteo is free for non-commercial use, needs no key, and allows up to 10,000 calls a day. You will make it yours with a new tool, connect it to Claude, publish it to npm, and list it in the official MCP Registry.

Time: about three hours. Level: intermediate, copy-paste friendly.

## What you will build

Weather Buddy offers three tools to any AI that connects to it.

- `get_weather`: the current weather for a place.
- `get_forecast`: the forecast for the next few days.
- `packing_advice`: what to pack, based on the forecast.

By the end, anyone can install your server with one line of settings. You will be an MCP author.

## Before you start

You need four things.

- **Node.js 24 or newer.** Node 18 and 20 no longer get security fixes as of November 5, 2026. Node 26 is the current long-term-support version. Check yours with `node --version` in a terminal.
- **An npm account.** **npm** is the place where JavaScript programs are shared. You need an account to publish.
- **A domain name you control**, for your registry name. No GitHub account is needed.
- **Claude Code or Claude Desktop**, to test the server with a real assistant.

Keep a terminal open. Most steps are one or two commands.

## Step 1: run and test the kit, 15 minutes

Download the starter kit from the book's kit page. No account is needed. Unzip it and open a terminal in the folder.

Install the pieces and start the server.

```
npm install
npm start
```

Line by line: `npm install` downloads the pieces the server needs. `npm start` runs the server. If both work, the server starts without errors. If `npm install` fails, check your Node version first. An old Node is the most common cause.

Test it by hand. Ask for the weather in Paris. You should get a real answer with a temperature and a condition. If you get an error, check your internet connection and try again. Open-Meteo is a free service. It is usually fast.

## Step 2: explore it in the MCP Inspector, 15 minutes

The **MCP Inspector** is a tool that shows you what a server offers. It lists the tools, lets you call them, and shows the results.

Start the Inspector and point it at your server. You should see three tools: `get_weather`, `get_forecast`, and `packing_advice`. Call `get_weather` with "Paris." Read the result. Call `get_forecast` with "Tokyo." Read the result.

The Inspector is your debugging friend. If a tool fails here, it will fail in Claude too. Fix it here first.

## Step 3: make it yours, 30 minutes

Open the server code. Find the tool list. Add a fourth tool of your own. Here is a simple one: `what_to_wear`. It takes a place and a day, reads the forecast, and suggests clothes.

The pattern for a tool is always the same: a name, a description, a list of inputs, and a function that returns text. Copy the `get_weather` tool. Change the name and the description. Change what it returns. Keep the shape the same.

Rename the server too. Change "weather-buddy" to your own name, such as "weather-buddy-dylan." Change the description to say what makes yours different.

Test your new tool in the Inspector. If it works there, it will work everywhere.

## Step 4: connect it to Claude, 15 minutes

Connect the server to Claude Code or Claude Desktop. The settings file needs one entry: the command to run your server and the folder it lives in.

A typical entry looks like this:

```
{
  "mcpServers": {
    "weather-buddy": {
      "command": "node",
      "args": ["/path/to/weather-buddy/index.js"]
    }
  }
}
```

Line by line: the first line opens the settings. The second line names your server. The third line says to run it with Node. The fourth line says where the server file lives. Replace the path with your real path.

Restart Claude. Ask: "What is the weather in Paris, and what should I pack?" Claude should call your server, read the forecast, and answer with packing advice. If Claude says it has no weather tool, check the path in the settings file. A wrong path is the most common error.

## Step 5: test with real questions, 15 minutes

Ask Claude five real questions through your server. "Will it rain in London on Saturday?" "What should I wear in Rome tomorrow?" "Compare the weather in Paris and Berlin this weekend."

Watch which tools Claude calls. It should pick the right tool for each question. If it picks the wrong one, improve the tool descriptions. A clear description is how Claude chooses. "Gives the current weather for a city" is clearer than "Weather tool."

## Step 6: publish to npm, 10 minutes

Publishing puts your server where anyone can install it.

Log in to npm in your terminal with `npm login`. Follow the prompts. Then run `npm publish` in your server folder. npm checks the name. If the name is taken, rename your server and try again.

When it succeeds, your server has a public page on npm. Anyone can install it with one command. Test the install yourself in a fresh folder. If it installs and runs, your publish worked.

## Step 7: list it in the MCP Registry, 15 minutes

The **MCP Registry** is the official list of MCP servers. Listing yours makes it easy to find.

Follow the registry's instructions to submit your server. You will need your npm page, your domain name, and a short description. The registry checks that your server works. When it passes, your server appears in the list.

Congratulations. Anyone in the world can now find and install your server.

## Step 8, optional: host it as a remote server

So far your server runs on your machine. A **remote server** runs on the internet, so people can use it without installing anything.

Hosting is optional and adds work. You need a server, a domain, and a way to keep it running. Start with the local version. Host remotely only when people ask for it.

If you do host it, add a simple health check. A **health check** is a page that says "I am alive." It lets you know the server is still running. Add logging too, so you can see what tools people call.

## Maintaining your server

A published server is a small responsibility. Keep it healthy.

- **Versioned releases.** When you change something, bump the version number and publish again. A **version number** such as 1.2.0 tells users what changed. Small fixes bump the last number. New tools bump the middle number.
- **Changelog.** Keep a short list of what changed in each version. Users read it before they update.
- **Respond to issues.** People will report bugs. Thank them. Fix the easy ones fast. A server with a living author is a server people trust.
- **Keep dependencies fresh.** Update your libraries every few months. Old libraries can have security holes.

> NOTE: Never put secrets in a published server. No API keys, no passwords, no tokens. If your server needs a key, ask the user to provide their own. A secret in published code is public forever.

> TRY IT: Add your fourth tool today, even a simple one. Connect the server to Claude. Ask Claude a weather question that uses your new tool. When Claude calls it and answers well, you have built and shipped a real MCP server.

## Check yourself

1. What does an MCP server offer to an AI?
**Answer:** Tools the AI can call, such as getting the weather or a forecast, through the MCP plug.

2. Why should you test a tool in the MCP Inspector before Claude?
**Answer:** Because if a tool fails in the Inspector, it will fail in Claude too, and the Inspector shows you the error clearly.

3. How does Claude choose which tool to call?
**Answer:** From the tool descriptions, so clear descriptions matter.

4. Why must you never put secrets in a published server?
**Answer:** Because published code is public, and a secret in it is public forever.

## In short

- Weather Buddy gives live weather, forecasts, and packing advice from free Open-Meteo data.
- Test in the MCP Inspector first, then connect to Claude.
- Add your own tool by copying an existing one and changing it.
- Publish to npm, then list the server in the official MCP Registry.
- Maintain it with versioned releases, a changelog, and fresh dependencies.
- Never publish secrets; ask users to provide their own keys.
