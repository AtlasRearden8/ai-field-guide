# 6.12 Build-along: your AI command center
<!-- original: ch. 127 -->

This is the big one. Notion plus n8n as a single command center. Everything from the power stack, built in one place.

You will create four Notion databases and five n8n workflows. You will capture anything, with AI triage. You will plan with AI. You will get a daily briefing. You will let Claude manage your tasks over MCP. You will log every error.

Time: about three hours. Level: intermediate. New to n8n? Do the n8n masterclass first. It takes 30 minutes and covers the basics used here.

## What you will build

Four Notion databases and five n8n workflows.

**Databases:** Inbox, Tasks, Daily Briefings, and Automation Log.

**Workflows:** 1, Capture plus AI triage. 2, AI plan. 3, Daily briefing. 4, Error logger. 5, Task tools over MCP.

The flow is simple. Anything you capture lands in Inbox. AI triages it into Tasks. You plan your day from Tasks. Each morning, a briefing tells you what matters. Claude can manage your tasks when you ask. Every error lands in the Automation Log.

## Before you start

You need five things.

- **n8n**, on n8n Cloud, or self-hosted with a public HTTPS address. The public address is needed for Notion buttons and your phone.
- **A Notion workspace.** The "Process with AI" button needs a paid plan. A free alternative is included in step 4.
- **An Anthropic API key**, with a monthly spending cap set.
- Optionally, **a Telegram bot token and your chat ID**, if you want to capture from Telegram. Chapter 6.3 shows how to get both.
- **About three hours**, in chunks. You can stop after any step and come back later.

The n8n screenshots in the original book were captured by importing the starter kit into n8n 2.41.6, from October 2026. Your version may look slightly different. The steps are the same.

## Step 1: create the four Notion databases, 20 minutes

Fast way, two minutes: if you have Notion AI, or Claude connected to Notion, open a new page and paste a prompt like this:

> Create a page called "Command Center" with four databases: Inbox, Tasks, Daily Briefings, and Automation Log. Inbox has Title, Source, and Status. Tasks has Title, Status, Priority, Due, and Project. Daily Briefings has Title, Date, and Summary. Automation Log has Workflow, Time, and Error.

Check what it made. Fix any missing properties by hand.

Slow way, twenty minutes: create each database by hand. Add the properties listed above. Add a Status for each: Inbox rows start as New. Tasks use To do, In progress, and Done. Automation Log rows are just a record.

Create the Command Center page. Put all four databases on it. This page is your front door. Open it every morning.

## Step 2: create a Notion integration for n8n, 5 minutes

Go to notion.so/profile/integrations. Create a new integration called "n8n command center." Copy the secret. Add it as a Notion credential in n8n. Share all four databases with the integration: open each database, click the three dots, then Connections, then add the integration.

Test it. Add a Notion node in n8n, choose Database Page, then Get Many, and open the database dropdown. If all four databases appear, the link works.

## Step 3: import the error logger first, 10 minutes

Import the error logger workflow before anything else. It is workflow 4 in the kit. It uses the Error Trigger node, which fires when any workflow fails. It writes a row to the Automation Log with the workflow name, the time, and the error message.

Test it. Make a small workflow that fails on purpose. Watch the error appear in your Automation Log. Then delete the test workflow.

This step takes ten minutes. It saves you hours later. Every failure in every other workflow becomes visible in Notion.

> NOTE: Always build the error logger first. A system that fails silently is worse than a system that does not exist. You trust what you can see.

## Step 4: capture anything, with AI triage, 30 minutes

Workflow 1 is the heart of the system. It has four parts.

1. **Webhook in.** A phone shortcut, a form, or Telegram sends a message to a webhook. The message can be text or a voice note.
2. **AI triage.** Claude reads the message and returns a title, a type, a priority, and a project. Ask for JSON with those four fields. **JSON** is a simple data format with named fields.
3. **Clean-up.** The workflow tidies the result. It checks the priority is one of High, Medium, or Low. It checks the project exists.
4. **Notion row and reply.** It creates an Inbox row with the triage results. It replies to you with the title and the priority.

Add a "Process with AI" button on the Inbox database. The button sends a webhook to n8n with the page ID. n8n reads the row, asks AI to plan it into tasks, and writes the tasks to the Tasks database. The button needs a paid Notion plan.

No paid plan? Use a checkbox instead. Add a "Process" checkbox. A scheduled workflow finds Inbox rows where the box is checked and Status is not Done, processes them, and unchecks the box.

Test it with ten real captures. Voice notes, emails, ideas, chores. Check each Inbox row. Is the title right? Is the priority right? Fix the triage prompt when it guesses wrong.

## Step 5: the AI plan, 20 minutes

Workflow 2 turns Inbox rows into a plan. It runs when you click "Process with AI," or on a schedule each evening.

It reads your Inbox rows. It asks Claude to turn each one into one or more Tasks rows, with a due date and a priority. It moves the Inbox row to Done. It links each task back to its source row, so you can always see where a task came from.

The prompt matters. Tell Claude: "Turn each Inbox item into clear, single actions. One action per task. Use the due date from the item if it has one. Otherwise suggest a sensible date. Never invent a deadline the item does not imply."

Test it with five Inbox rows. Read the tasks it creates. Are they clear? Are they single actions? Fix the prompt until they are.

## Step 6: the daily briefing, 20 minutes

Workflow 3 runs every weekday at 7am. It reads today's Tasks and your calendar. It asks Claude to write a short briefing: what is due today, what is overdue, and one suggestion for the day. It creates a Daily Briefings row and sends the briefing to you by Telegram or email.

Keep the briefing short. Five lines is enough. A briefing you read beats a briefing you skim. Ask Claude for: three top tasks, one overdue item, and one suggestion. No more.

Test it by running it by hand once. Read the briefing. Does it pick the right tasks? Does it sound like a helpful assistant? Fix the prompt until it does.

## Step 7: let Claude manage your tasks over MCP, 30 minutes

Workflow 5 exposes your tasks as MCP tools. **MCP** is a standard plug that lets AI use outside tools.

Create three tools: find tasks, create task, and update task. Each one is a small n8n workflow that Claude can call. Fix the database in each tool. Let Claude fill in the filter, the title, or the new status.

Connect Claude to these tools through MCP. Then ask Claude in plain words: "What is due today?" "Add a task to call the dentist tomorrow." "Move the report to Done." Claude calls your workflows. The workflows update Notion. Claude reports the result.

Set the rules in the system prompt: always search before creating, to avoid duplicates. Confirm before marking anything Done. Never delete a page. Keep replies under 80 words.

Test it with five real requests. Check Notion after each one. Did the right row change? Did anything unexpected happen? Narrow the tools if it does too much.

## Troubleshooting

- **Databases do not appear in n8n.** They are not shared with the integration. Share each one in Notion under Connections.
- **The button does nothing.** Check the webhook URL and the secret header. Click the button once and inspect the payload in n8n.
- **Triage is wrong.** Your prompt is vague. Add examples. Show Claude three messages and the triage you want for each.
- **The briefing is empty.** The workflow ran before any tasks existed, or the filter is wrong. Run it by hand and check the filter.
- **Claude creates duplicates.** The find-tasks tool is not being used first. Add to the prompt: "Always search before creating."
- **Errors do not appear in the log.** The error logger is not imported, or it is not published. Import it, publish it, and test it with a deliberate failure.

## Level-ups

- **Voice capture.** Add voice transcription to workflow 1. Talk to your phone and watch tasks appear.
- **Calendar sync.** Add a workflow that turns Tasks with a Scheduled time into calendar events.
- **Weekly review.** Add a Friday workflow that writes a review from the week's completed tasks.
- **Team mode.** Share the Command Center with your team. Add an Owner property and a per-person briefing.

> TRY IT: Build steps 1 to 3 today. Four databases, one integration, one error logger. That is under 40 minutes. Tomorrow, add capture. By the end of the week, your command center will be running your life.

## Check yourself

1. What are the four databases in the command center?
**Answer:** Inbox, Tasks, Daily Briefings, and Automation Log.

2. Why should you import the error logger first?
**Answer:** So every failure in every other workflow becomes visible in Notion from the start.

3. How can you run the "Process with AI" button on Notion's free plan?
**Answer:** Use a checkbox instead, picked up by a Notion Trigger or a scheduled query.

4. What should Claude do before creating a task?
**Answer:** Search first, to avoid creating a duplicate.

5. What does the daily briefing include?
**Answer:** What is due today, what is overdue, and one suggestion for the day.

## In short

- Four databases: Inbox, Tasks, Daily Briefings, Automation Log.
- Five workflows: capture with triage, AI plan, daily briefing, error logger, and MCP task tools.
- Build the error logger first, so failures are always visible.
- Capture anything, triage with AI, plan into tasks, and brief each morning.
- Let Claude manage tasks over MCP, with rules: search first, confirm before Done, never delete.
- Test each workflow with real data before you trust it.
