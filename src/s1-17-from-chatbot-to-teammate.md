# 1.17 From chatbot to teammate
<!-- original: ch. 32 -->

You already know how to chat with an AI. This chapter is about the next step, the one that makes everything else click. It is the step from a chatbot that answers to a teammate that acts.

Once you grasp this idea, every advanced tool in this book makes sense. Automation, connectors, coding agents, and research agents are all variations on the same simple idea.

## From brain in a jar to teammate

A plain chatbot is a brain in a jar. It knows a remarkable amount. But it can only work with what you paste in, and it can only hand text back to you. You still have to copy, paste, click, file, send, and remember everything yourself.

Everything advanced in AI right now is about giving that brain four superpowers.

1. **Tools.** The ability to use other apps: search the web, read your calendar, send an email, look at a file.
2. **Data.** The ability to read your stuff: your notes, your documents, your messages.
3. **Memory.** The ability to remember background facts about you and your work, across chats.
4. **Steps.** The ability to keep working, step by step, until a task is done, instead of stopping after one answer.

Put all four together and you have an **agent**. An agent is an AI that takes a goal, works out the steps, uses tools, looks at the results, and repeats until it is done.

> NOTE: The words matter less than the picture. Chatbot: answers. Agent: acts. Teammate: acts, remembers, and works with you over time.

## The agent loop, demystified

Every agent you will ever meet runs roughly the same loop. It looks like this.

1. **Think.** What is the next step toward the goal?
2. **Act.** Call a tool to take that step.
3. **Look.** Read the result. Did it work? What did I learn?
4. **Repeat.** Pick the next step, until the goal is reached. Then tell the human.

Watch it work on a small goal: "Find out when my next dentist appointment is, and add a reminder the day before."

- Step 1: The model thinks: "Appointments are usually in the calendar. Let me search." It calls the calendar search tool.
- Step 2: The tool returns: "Dr. Lee, October 14, 9:00."
- Step 3: The model thinks: "Found it. Now I need a reminder on October 13." It calls the reminder tool.
- Step 4: The tool returns: "Reminder set." The model tells you: "Your dentist appointment is October 14 at 9:00. I added a reminder for the evening of October 13."

Three steps. Two tools. Zero clicks from you. Now picture the same loop with thirty steps. That is how a coding agent builds a feature, or how a research agent writes a ten-page report.

## What "tools" really are

A **tool** is an action an app offers the AI, with a name, a description, and a list of inputs. Think of it like a button on a machine, with a label that says what it does.

"Search my calendar" is a tool. It takes a search phrase. "Send an email" is a tool. It takes a recipient, a subject, and a message. "Read a file" is a tool. It takes a file name.

The big insight is this: when an agent "does something", the model itself never touches your calendar. It writes a structured request, like calendar.search("dentist"). Your software runs it. The result is fed back in. The model is the planner. The tools do the doing.

That is why the app you use, called the **host**, is in charge of permissions. It decides which tools the AI may use, and it asks you before anything risky happens. Good hosts ask first. Bad hosts do not. Choose good hosts.

## Where all the buzzwords fit

The AI world is full of buzzwords. Most of them describe the same picture you now have. Here is a quick map.

| Word | What it means, in plain words |
|---|---|
| Agent | AI with a goal, tools, and a loop |
| Tool | One action an app offers the AI |
| Host | The app the AI lives in, like ChatGPT or Claude |
| MCP | A standard plug that lets AI use tools, like USB-C for AI apps |
| Connector | A built-in link between your assistant and an app |
| Automation | A fixed set of steps that runs on its own, like "when X happens, do Y" |
| Workflow | The steps themselves, in order |

You do not need to memorise this table. You need to know that these words all point at the same idea: AI plus tools plus steps.

> TRY IT: Give your assistant a two-step job that needs a tool. For example: "Search the web for the current weather in [your town], then tell me whether I need a coat tomorrow." Watch it search, then answer. You just watched the agent loop run.

## Autonomy levels: from autocomplete to autopilot

Not every agent works alone. **Autonomy** means how much the AI does without asking you. It comes in levels. Match the level to how much you trust the setup.

- **Level 1: Suggest.** The AI suggests. You do it. Like autocomplete for an email.
- **Level 2: Draft.** The AI drafts. You check and send. Like a first draft you approve.
- **Level 3: Act with approval.** The AI does the work, but asks you before each risky step. Like booking a table after you say yes.
- **Level 4: Act alone, within rules.** The AI works on its own inside limits you set. Like sorting your inbox every morning.
- **Level 5: Full autopilot.** The AI works alone, for hours, on a big goal. This exists, but it is for experts, with strong safety checks.

Start at Levels 1 and 2. Move up slowly. Never give Level 4 or 5 to a setup you have not tested.

## What AI is great at, and where it still trips

Agents are great at jobs with clear steps and checkable results: research, drafting, sorting, summarising, planning, and coding small features.

They still trip on vague goals, on jobs where a mistake is expensive, and on tasks that need real-world judgement. "Book me the best flight" is risky. "Find three flight options under £200 and show me, then I will choose" is safe.

The rule is simple. The more the task matters, the more you stay in the loop.

## A day in the life with an AI teammate

Picture a normal Tuesday, with a teammate.

Morning: your assistant reads your calendar and your inbox, and gives you a three-line brief: your meetings, your deadlines, and one email that needs a reply today.

Midday: you ask it to draft a report from your notes. It drafts. You edit. It fixes the numbers you flag.

Afternoon: it watches a price you care about, and tells you when it drops. It files your receipts into a folder, and adds them to a spreadsheet.

Evening: it plans tomorrow, from your calendar and your task list, and reminds you about the dentist.

None of this is science fiction. Each piece exists today. The skill is putting the pieces together, one at a time, and staying in charge.

## Three principles that will save you hours

1. **Give it the background it needs.** An agent is only as good as what you give it. Context first, task second.
2. **Describe tools and tasks clearly.** "Search my email for the invoice from Acme, dated last week" beats "find that invoice".
3. **Use plain automation for steps that never change.** If a step is always the same, do not waste an agent on it. Use a simple rule: "when X happens, do Y". Save the agent for the steps that need judgement.

> NOTE: You do not need to build agents today. You need to understand the picture. When you meet MCP, connectors, and automation later in this book, you will recognise them. They are all the same loop, with different tools.

## Check yourself

1. What is the difference between a chatbot and an agent?
**Answer:** A chatbot can only reply with text. An agent can also take action, using tools, data, memory, and steps, until a task is done.

2. What are the four superpowers that turn a chatbot into a teammate?
**Answer:** Tools, data, memory, and the ability to work step by step.

3. Describe the agent loop in four steps.
**Answer:** Think about the next step, act by calling a tool, look at the result, and repeat until the goal is reached.

4. What is a tool, in plain words?
**Answer:** One action an app offers the AI, with a name, a description, and a list of inputs, like searching a calendar or sending an email.

5. Why should you start at low autonomy levels?
**Answer:** Because higher levels let the AI act without asking you. Start with suggestions and drafts, and move up only when you trust the setup.

## In short

- A chatbot answers. An agent acts. A teammate acts, remembers, and works with you.
- Agents need four superpowers: tools, data, memory, and steps.
- Every agent runs a loop: think, act, look, repeat.
- The model plans. The tools do the doing. The host controls permissions.
- Match autonomy to trust. Start low. Stay in the loop for important tasks.
- Give background first, describe tasks clearly, and use plain automation for fixed steps.
