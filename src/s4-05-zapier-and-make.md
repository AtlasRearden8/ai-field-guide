# 4.5 Zapier and Make
<!-- original: ch. 49 -->

n8n is the tinkerer's tool. Zapier and Make are the fastest paths from an idea to a working automation. Both run in your browser. There is no server to set up. There is no code to write. You sign up, you connect your apps, and you build.

This chapter walks through real builds in both tools. You will build an AI lead responder in Zapier, try Zapier's MCP and Agents, then build a social media repurposer and an invoice extractor in Make. At the end, you will know which tool to reach for, and when.

## Zapier concepts in two minutes

Zapier calls a workflow a **Zap**. A Zap has a trigger and one or more actions. The trigger is the event that starts it. The actions are the steps that follow.

A Zap runs in a straight line, top to bottom. Step one happens, then step two, then step three. That simplicity is Zapier's strength. You can read a Zap in seconds. You can explain it to a colleague in one sentence.

Zapier connects to more apps than any other tool. If an app exists, Zapier probably connects to it. Each connection is called an account. You sign in once, and Zapier can act in that app for you.

Zapier has AI in two places. First, **AI steps** inside a Zap: a step that reads text, writes text, or makes a decision. Second, **Zapier Agents**: small AI helpers that can handle a whole job, such as watching an inbox and answering routine questions on their own.

Zapier also offers **Zapier MCP**. MCP is a standard plug that lets AI use your tools, which you met in Chapter 2.20. Zapier MCP gives you one web address that opens up thousands of Zapier apps to any AI that speaks MCP. One connection, and your assistant can act across your whole stack.

> NOTE: Zapier charges by tasks, and a task is one action that runs. A Zap with five actions uses five tasks each time it runs. Check the current price and your plan's task limit before you build a Zap that runs hundreds of times a day.

## Walkthrough 1: AI lead responder in Zapier

This build takes about 15 minutes. When a new lead fills in a form on your website, the AI writes a friendly first reply, and Zapier sends it by email.

First, make a new Zap. Pick the trigger. Choose your form tool, such as Google Forms or Typeform. Set the trigger to fire when a new form answer arrives. Connect your form account. Pick the form.

Next, add an AI step. Choose the AI action, often called "ChatGPT" or "AI by Zapier". Write a prompt like this: "Write a short, friendly first reply to a new lead. Thank them. Ask one question about their project. Keep it under 80 words." Then pull the lead's name and message into the prompt, using the fields from the form step.

Then add the final action: send an email. Choose your email app. Put the lead's email address in the "To" field. Put the AI's reply in the body. Add a subject line, like "Thanks for getting in touch".

Test the Zap. Fill in the form yourself. Watch the Zap run. Did the email arrive? Did it read well? If the reply sounds stiff, change one line in the prompt and test again. Prompts are the cheapest thing to fix.

When it works, turn the Zap on. Every new lead now gets a fast, friendly reply, even at midnight.

## Walkthrough 2: Zapier MCP, one address for thousands of apps

This one is short, and it is powerful. Go to the Zapier MCP page in your Zapier account. It will show you a single web address, your MCP address. Copy it.

Now open your AI assistant, such as Claude. Find its MCP settings. Add a new MCP server, and paste the Zapier address. Choose which apps the assistant may use. Be careful here. Only switch on the apps you actually need. If you switch on everything, the assistant can reach everything.

Once it is connected, try it. Ask your assistant to do something simple, like "Add a row to my leads spreadsheet." The assistant will use Zapier MCP to do it. You just gave your chatbot hands across thousands of apps, with one connection.

> TRY IT: Connect Zapier MCP to your assistant, but switch on only one app to start. Try one small task with that app. Add a second app only when the first one works well.

## Walkthrough 3: a Zapier Agent

A Zapier Agent is different from a Zap. A Zap follows fixed steps. An Agent decides what to do. You give it a job, some tools, and some rules. It handles the rest.

To make one, open Zapier Agents and click to create a new agent. Give it a job, such as "Answer routine support questions from the inbox." Give it tools: your email, your help pages, and your order list. Write rules: "Never promise a refund. Never share a customer's address. If you are unsure, ask a human."

Then test it. Send it a few questions. Watch what it does. Agents make mistakes more often than Zaps, because they decide for themselves. So start with a small job, where a mistake is cheap. Grow the job only when the agent proves itself.

## Make concepts in two minutes

Make calls a workflow a **scenario**. A scenario is a map, not a list. Boxes sit on a canvas, joined by lines. Data flows along the lines.

Make is built for complex flows. One path can split into many branches. A branch can loop, which means it repeats a step for each item in a list. A step can wait, filter, or combine data from several paths.

Make calls each box a **module**. Each module does one job, in one app. A trigger module starts the scenario. Action modules do the work. There are also tools for shaping data: filters that let only some items through, routers that split a path, and aggregators that join many items into one.

Make counts **operations**, and an operation is one module that runs once. A scenario with ten modules uses ten operations per run. Like Zapier, check the current price and your plan's limit before you build something that runs all day.

## Walkthrough 4: social media repurposer in Make

This build takes about 30 minutes. It turns one blog post into several social media posts, with AI doing the rewriting.

Start a new scenario. The trigger is a new row in a spreadsheet, or a new post in your blog. That row holds the link and the title of the post.

Add an HTTP module to fetch the post. That module reads the web page and returns its text. Then add an AI module. Give it a prompt like: "Turn this article into three short social posts. One for X, one for LinkedIn, one for Facebook. Keep each under 100 words. Keep the tone friendly." Pull the article text into the prompt.

The AI will answer with three posts. That answer is one block of text, so you need to split it. Use a text parser module, or ask the AI to answer in JSON, with one label per post. JSON is easier for the next steps to read.

Then add a router. A router splits one path into many. One branch sends the X post to your X account. Another branch sends the LinkedIn post to LinkedIn. A third sends the Facebook post to Facebook. Each branch is a module that posts to one app.

Test the scenario with one real post. Read all three outputs before you let them publish. AI can write a post that sounds fine but says something wrong. Check the facts, then publish.

## Walkthrough 5: invoice extractor in Make

This build turns a pile of invoice emails into tidy spreadsheet rows. It is one of the most useful automations a small business can own.

The trigger is a new email with an attachment. Add a filter, so only emails with the word "invoice" in the subject get through. Then add a module that reads the attachment. Many email tools can pull the text out of a PDF for you.

Add an AI module. Ask it to pull out four facts: the seller, the invoice number, the date, and the total. Tell it to answer in JSON, with those four labels. Then add a spreadsheet module that adds one row per invoice, with one column per fact.

Run it on five old invoices first. Check every row against the real invoice. If the AI gets the total wrong on one of them, fix the prompt. A common fix is to add: "The total is the number next to the words Total Due, not the subtotal."

When it is right five times in a row, turn it on. Your invoices now file themselves.

> NOTE: Never let an invoice extractor pay anything on its own. Filing is safe to automate. Paying is a human decision. Keep those two jobs apart.

## Zapier vs. Make vs. n8n: when to use which

Here is the honest guide. Pick Zapier when you want the fastest start, the biggest app list, and simple step-by-step flows. Pick Make when your flow has branches, loops, or tricky data, and you want a visual map. Pick n8n when you want the most control, AI agents inside your workflows, or the freedom to run it yourself.

Many people use two of them. They use Zapier for quick business jobs, and n8n for the clever AI builds. That is fine. You do not have to marry one tool.

| Tool | Shape | Best for | Watch out for |
| --- | --- | --- | --- |
| Zapier | Straight list of steps | Fastest start, most apps | Costs grow with tasks |
| Make | Visual map with branches | Complex flows, loops, data shaping | More to learn |
| n8n | Visual map, self-hosted option | AI agents, full control | Most setup at first |

## Check yourself

1. What is a Zap?
**Answer:** A Zap is a workflow in Zapier: a trigger followed by one or more actions, in a straight line.

2. What is a scenario in Make?
**Answer:** A scenario is a workflow in Make, shown as a visual map of modules joined by lines.

3. What does Zapier MCP give you?
**Answer:** One web address that lets an AI assistant use thousands of Zapier apps through MCP.

4. When is Make a better pick than Zapier?
**Answer:** When the flow has branches, loops, or tricky data that needs shaping.

5. Why should you test an invoice extractor on five old invoices first?
**Answer:** So you can check its answers against real invoices and fix the prompt before it files anything wrong.

## In short

- Zapier is the fastest start, with the biggest app list and simple step-by-step Zaps.
- Make is a visual map built for branches, loops, and tricky data.
- Zapier Agents decide for themselves, so start them on small jobs and grow slowly.
- Zapier MCP gives your assistant one connection to thousands of apps.
- The repurposer and the invoice extractor both follow the same shape: trigger, AI, act.
- Pick the tool that fits the job, and check the current price before you build something that runs all day.
