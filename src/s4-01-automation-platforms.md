# 4.1 Automation platforms: AI that works while you sleep
<!-- original: ch. 45 -->

Imagine a helper who never sleeps. You teach it a job once. Then it does that job again and again, day and night. It never gets bored. It never forgets a step. That is what an **automation platform** does. It is a tool that runs small jobs for you, on its own.

A chatbot waits for you to type. An automation does not wait. It watches for something to happen. Then it acts. A new email arrives, and it files it. A form is filled in, and it sends a reply. It is 7 in the morning, and it sends you a summary of the news.

Add AI to the middle of that job, and it gets clever. The AI can read an email and decide how urgent it is. It can sum up a long message in one line. It can write a friendly reply in your voice. The platform does the moving. The AI does the thinking.

This chapter maps the whole landscape. You will learn the pattern behind every automation. You will meet the three big platforms. Then you will build your first one in about 15 minutes.

## The pattern behind every automation

Almost every automation follows the same five steps. Learn this pattern once, and you can read any automation, in any tool.

First comes the **trigger**. A trigger is the event that starts the job. It might be a new email. It might be a form someone fills in. It might be a time, like every Monday at 9 in the morning. Nothing happens until the trigger fires.

Next comes gathering. The automation collects the facts it needs. It might read the email. It might fetch a web page. It might look up a row in a spreadsheet.

Then comes the AI step. This is the clever part. The AI reads what was gathered. It decides something, or writes something, or sums something up. For example, it reads a customer email and decides if the customer is angry, curious, or ready to buy.

Then comes the route. The automation sends the result to the right place. Angry emails go to a human. Simple questions get an automatic reply. Urgent items go to the top of your list.

Last comes the action. The automation does the thing. It sends the email. It adds the row. It posts the message. It updates the calendar.

Trigger, gather, AI, route, act. That is the whole pattern. Every workflow in this section is a version of it.

> NOTE: Start with jobs you already do by hand. If you do the same steps three times a week, that job is a good first automation. If you do it once a year, leave it alone.

## The building blocks

Automation tools share a small set of words. Learn them now, and every tool will feel familiar.

A **workflow** is one whole automation, from trigger to final action. People also call it a flow, a Zap, or a scenario, depending on the tool. They all mean the same thing: a job that runs itself.

A **node** is one box in a workflow. Each box does one job. One box watches your inbox. Another box calls the AI. Another box sends a message. You join the boxes with lines. Data flows along the lines, from left to right.

An **app connection** is permission for the tool to talk to one of your apps. You sign in once to your email, your calendar, or your notes app. After that, the tool can act in that app for you. You can remove the permission any time.

A **run** is one single time the workflow does its job. If ten emails arrive, the workflow runs ten times. Most paid plans count runs, or count the steps inside runs. Free plans give you a small number of runs each month.

A **schedule** is a trigger based on time. It might run every hour, every day, or every Monday. Use a schedule when there is no single event to watch for. For example, check the news every morning at 7.

> TRY IT: Pick one boring job from your week. Write it down as five steps: trigger, gather, AI, route, act. Do not open any tool yet. Just write the steps on paper. If you cannot write the steps, the job is not ready to automate. If you can, you already have a plan.

## The three big platforms

Three tools dominate this world. They do the same job in different ways. None of them is best for everyone. Pick the one that fits how you think.

**n8n** is the tinkerer's favourite. It shows your workflow as a map of boxes joined by lines. You can see the data move through it. It is open source, which means its code is public and free to run on your own computer. You can also pay for a hosted version, called n8n Cloud, where they run it for you. It has an AI Agent node that can make its own decisions. It is the most flexible of the three. It is also the one that asks the most of you at the start. Chapter 4.3 builds your first n8n workflow, click by click.

**Zapier** is the easiest to start with. It has the biggest list of apps it can connect to. Its workflows are simple lists of steps, one after another. You pick a trigger, then you pick what happens next. There is no server to run. You work in your browser, and it just works. It has AI built in, plus Zapier Agents that can handle whole jobs on their own. It costs more as you run more jobs, so check the current price before you build something big.

**Make** sits in the middle. Its workflows are visual maps, like n8n, but in your browser with nothing to install. It is very good at complex flows. It can split one path into many branches. It can loop, which means it can repeat a step for each item in a list. It can handle tricky data, like lists inside lists. If your job has many "if this, then that" branches, Make is often the nicest tool for it.

There are others too. **IFTTT** is the simplest of all. It connects one trigger to one action. It is good for home gadgets, like turning on a light when you arrive home. **Microsoft Power Automate** is the natural choice if your work lives in Microsoft tools. **Pipedream** is for people who like a little code mixed in with their boxes. **Relay** and **Activepieces** are newer tools worth a look. You do not need to learn them all. Learn one well first.

| Tool | Best for | Watch out for |
| --- | --- | --- |
| n8n | Flexibility, AI agents, running it yourself | Takes more setup at first |
| Zapier | Easiest start, most apps | Costs grow with use |
| Make | Complex flows with branches and loops | More to learn than Zapier |
| IFTTT | One simple trigger, one action | Too simple for big jobs |

> NOTE: Do not pay for a tool until you have built something real on its free plan. Free plans are enough to learn. They are enough to prove an idea works. Pay only when a workflow you love runs out of free runs.

## When to automate, and when not to

Automation is tempting. It is also easy to overdo. Here is a simple test. Automate a job when it repeats, it follows the same steps, and a mistake would be small. Do not automate a job when it is rare, when every case is different, or when a mistake would be costly.

Good first jobs: save email attachments to a folder. Send a daily summary of your calendar. Turn form answers into a tidy spreadsheet row. Watch a web page and tell you when it changes.

Bad first jobs: anything that spends money on its own. Anything that deletes things. Anything that sends messages to customers without a human checking first. Anything with private health or money details, until you understand where the data goes.

Start small. Automate one job. Watch it run for a week. Fix the small surprises. Then automate the next job. People who try to automate ten jobs on day one usually finish none of them.

## Your first automation in 15 minutes

Here is a simple first build. It works on Zapier, Make, or n8n. Pick whichever tool you already have open. The steps are the same in all three.

First, make a trigger. Choose your email inbox. Set the trigger to fire when a new email arrives with the word "receipt" in the subject. That is your trigger.

Next, add an AI step. Ask the AI to read the email and pull out three facts: who sent it, how much money it mentions, and what it was for. Tell the AI to answer in a simple list. This is the gather and AI part of the pattern.

Then add an action. Send the three facts to a spreadsheet. Each email becomes one new row. The columns are sender, amount, and what for.

Now test it. Send yourself a test email with "receipt" in the subject. Write something like "Your order totals $24 for books." Run the workflow. Check the spreadsheet. Did a new row appear? Did the AI pull out the right facts?

If it worked, turn the workflow on. If it did not, look at what each box received. Most failures are simple. The trigger watched the wrong folder. The AI was given the wrong field. The spreadsheet columns did not match. Fix one thing, and test again.

That is your first automation. It is small. It is real. And it saves you a little time every single week, forever.

> TRY IT: Build the receipt workflow above, in any tool, right now. Give yourself 15 minutes. If you get stuck, simplify it: skip the AI step, and send the whole email subject line to the spreadsheet instead. A simple workflow that works beats a clever one that does not.

## Check yourself

1. What is a trigger, in plain words?
**Answer:** A trigger is the event that starts an automation, such as a new email, a filled-in form, or a set time of day.

2. What are the five steps of the automation pattern?
**Answer:** Trigger, gather, AI, route, act.

3. Which platform has the biggest list of apps it can connect to?
**Answer:** Zapier.

4. Which platform is open source and can run on your own computer?
**Answer:** n8n.

5. Name one job you should not automate first.
**Answer:** Any job that spends money on its own, deletes things, or sends messages to customers without a human check.

## In short

- An automation is a job that runs itself when something happens.
- Most automations follow one pattern: trigger, gather, AI, route, act.
- A workflow is the whole job; a node is one box inside it; a run is one single execution.
- n8n is the most flexible, Zapier is the easiest to start, and Make is best for complex branching flows.
- Automate jobs that repeat and follow the same steps, and start with one small win.
- Build on a free plan first, and pay only when a workflow you love runs out of free runs.
