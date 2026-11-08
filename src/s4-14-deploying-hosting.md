# 4.14 Deploying and hosting
<!-- original: ch. 66 -->

An app on your laptop is a hobby. An app with a link is a gift to the world. **Deploying** means moving your project to a server that is always online, so anyone with the link can use it. **Hosting** is the service that keeps it online for you.

Deploying used to be the scary part. Today it is often a single click, and most hobby projects host for free. This chapter shows you where to host each kind of project, how to handle secrets and domains, and how to let your AI helper do the fiddly bits.

## What are you deploying?

Not all projects need the same kind of hosting. Match the host to the project, and everything gets easier.

A **static site** is a set of pages that do not change for each visitor. A personal page, a simple tool, a landing page. These are the easiest to host, and they are free on many services.

A **full-stack app** has pages plus a server that does work, like saving data or signing users in. A shopping list that syncs, a blog with comments, an app with accounts. These need a host that runs code, not just pages.

An **always-on app** needs to run all the time, even when nobody is visiting. A chat bot, a scheduled automation, a server that listens for webhooks. These need a host that never sleeps.

An **MCP server** is a plug that AI apps connect to, as you learned in Chapter 2.20. A remote MCP server needs a host that runs code all the time, and a public address so AI apps can reach it.

Work out which kind yours is before you pick a host. If you are unsure, ask your AI helper: "What kind of project is this, and where should I host it?"

## Hosting vocabulary in 60 seconds

A **server** is a computer that stays on and answers requests. A **host** is a company that runs servers for you. **Deploy** is the act of putting your project on a host. A **domain** is a human-friendly address, like `myapp.com`, that points to your project. **DNS** is the system that turns a domain into the right server address, like a phone book for the internet.

**Uptime** is how often your app is available. Good hosts promise high uptime. **Bandwidth** is how much data your app sends to visitors. Small apps use very little. **Logs** are the records your host keeps of what happened, such as errors and visits. When something breaks, the logs are the first place to look.

> NOTE: You do not need to memorise these words. You need to recognise them when a host's dashboard shows them to you. Come back to this list when a word confuses you.

## The one-click path: Vercel and Netlify

For most beginner projects, the answer is Vercel or Netlify. Both are hosts built for modern web apps. Both have generous free tiers. Both deploy with a few clicks.

The usual flow is the same on both. Make a free account. Click "Add new project" or "Deploy". Choose your project folder, or connect the code host where your project lives, if you use one. The host reads your project, builds it, and gives you a link. That link works at once.

If your project is a plain set of pages, you can also use **Netlify Drop**: drag your folder onto the web page, and it gives you a link. No account setup, no commands. It is the fastest deploy in the world for a simple site.

**Cloudflare Pages** is another strong free choice, especially for simple sites. It is fast, it is free for hobby projects, and it connects well with Cloudflare's other tools.

Pick one. Learn its dashboard. The dashboard is where you will see your link, your logs, and your settings. You do not need to learn all three hosts. One is enough.

> TRY IT: Take any small project you have, even a single web page. Drag it onto Netlify Drop, or deploy it with Vercel. Open the link it gives you on your phone. You have just deployed a website.

## Free static hosting and friends

If your project is a plain site, you have many free choices. Netlify Drop and Cloudflare Pages are the simplest. GitHub Pages is free if you use GitHub, but this book never requires a GitHub account, so treat it as optional. Any static host will do. The idea is the same: upload your files, get a link.

The rule for free tiers is simple. They are generous for small projects, and they are honest about their limits. Read the limits before you launch something you expect hundreds of people to use. If your app grows past the free tier, the host will tell you, and you can decide whether to pay or to slim the app down.

## Always-on apps, bots, and backends

Some projects need a computer that never sleeps. A Telegram bot that must answer at once. A scheduled job that runs every hour. A server that holds data and answers requests all day.

For these, look at hosts that run code all the time. **Railway**, **Render**, and **Fly.io** are popular choices for beginners. They all have free tiers or low-cost plans, so check the current price. They all let you deploy from a project folder, and they keep your app running.

The flow is similar to Vercel: make an account, add a project, point it at your folder, and press deploy. The difference is that the host keeps your code running, instead of just serving pages. Your app gets a public address, and it stays awake.

For a remote MCP server, the same hosts work. The server needs a public address, and it needs to stay on. Deploy it like any always-on app, then share its address with the AI apps that should use it.

## Secrets and environment variables

A **secret** is a password, a key, or a token that your app needs to work, but that nobody else should see. An API key is a secret. A database password is a secret. A bot token is a secret.

Never write a secret in your code. Anyone who can read the code can read the secret. Instead, store secrets in **environment variables**. An environment variable is a named value that lives outside your code, in the place where the code runs. Your code reads it by name, like `process.env.API_KEY`, and the value itself stays hidden.

Locally, on your own computer, store secrets in a file called `.env`. That file holds lines like `API_KEY=your-secret-here`. Your code reads the file when it runs. And you add `.env` to your `.gitignore` file, which tells Git to never save it. That way, your secrets never end up in your saved snapshots, and never leak if you share your project.

On a host, do the same thing in the dashboard. Every host has a settings page for environment variables. You add the name and the value there. The host gives them to your app when it runs, and never shows them to visitors.

| Place | Where secrets live |
| --- | --- |
| On your computer | A `.env` file, listed in `.gitignore` |
| On your host | The dashboard's environment variables page |
| In your code | Only the name, like `process.env.API_KEY`, never the value |

> NOTE: If a secret ever leaks, replace it. Delete it from the code, save a fix, and get a new key from the service. A leaked secret that still works is still a risk.

## Custom domains

A host gives you a free address, like `my-app.vercel.app`. That works fine. But you may want your own address, like `myapp.com`. That is a **custom domain**.

To get one, buy a domain from a registrar, which is a shop that sells web addresses. Then tell the registrar to point the domain at your host. The host's docs will show you exactly what to set. It usually takes two steps: add the domain in the host's dashboard, and add a record at the registrar. The change can take a few hours to spread across the internet. That is normal.

You do not need a custom domain to ship. Ship with the free address first. Add a custom domain later, when the app deserves one.

## Costs and free tiers

Most hobby projects host for free. The free tiers on Vercel, Netlify, Cloudflare Pages, Railway, and Render cover small apps with room to spare. Check the current price and limits on each host before you launch, because free tiers change.

Two costs catch beginners by surprise. The first is AI API use: if your app calls an AI model, you pay for those calls, and a popular app can use a lot of them. Set a spending limit on your API account, so a surprise cannot become a big bill. The second is a database that charges by use. If your app stores a lot of data, or reads it very often, check the database's pricing too.

## Let your agent do the deploying

You do not have to do this by hand. Ask your coding agent to deploy for you. "Deploy this project to Vercel, and give me the link." It will read the host's docs, run the commands, and report back. Watch what it does, so you learn the steps. Check the link yourself when it finishes.

If the deploy fails, ask the agent to read the logs. Logs are the host's record of what happened, and they usually say what went wrong. "Read the deploy logs and tell me, in plain words, why it failed." That one prompt fixes most deploy problems.

## After launch: logs, monitoring, and updates

Launching is not the end. It is the start of looking after your app.

Check the logs when something breaks. They are in the host's dashboard, usually under "Logs" or "Deployments". Look for red lines and error messages. Copy an error into your AI helper and ask it to explain the fix.

Update your app by changing the code, testing it, and deploying again. Most hosts redeploy automatically when you push a new version. If yours does not, press deploy again. Small, frequent updates are safer than rare, big ones.

And keep a backup. Your code lives in Git, as Chapter 4.9 taught you. Your data lives in your database, so export it now and then. If the host ever has a bad day, your work is safe somewhere else.

## Check yourself

1. What is the difference between deploying and hosting?
**Answer:** Deploying is putting your project on a server. Hosting is the service that keeps it online for you.

2. Which kind of project is easiest to host for free?
**Answer:** A static site, which is a set of pages that do not change for each visitor.

3. What is an environment variable, in plain words?
**Answer:** A named secret value that lives outside your code, in the place where the code runs, so your code can read it without the secret being written in the code itself.

4. Why should `.env` be in `.gitignore`?
**Answer:** So Git never saves your secrets, and they cannot leak if you share your project.

5. What should you check first when a deploy fails?
**Answer:** The logs in the host's dashboard, which record what happened and usually say what went wrong.

## In short

- Match the host to the project: static sites, full apps, and always-on bots need different homes.
- Vercel, Netlify, and Cloudflare Pages cover most beginner projects, often for free.
- Always-on apps need a host that never sleeps, such as Railway, Render, or Fly.io.
- Store secrets in environment variables, never in your code, and keep `.env` out of Git.
- Ship with the free address first; add a custom domain later.
- After launch, read the logs, update in small steps, and keep a backup of your code and data.
