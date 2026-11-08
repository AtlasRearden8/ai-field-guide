# 4.4 n8n AI agents, deep dive
<!-- original: ch. 48 -->

Chapter 4.3 gave you a workflow with fixed steps. The AI did one job, in one place. This chapter gives the AI the wheel. An **AI Agent node** in n8n is a model that decides for itself which tools to use, in which order, to finish a job.

A normal workflow is a recipe. Follow step one, then step two, then step three. An agent is a cook. You tell it the goal. It looks in the kitchen, picks the tools it needs, and works out the order itself. The same request can take a different path each time, because the agent chooses as it goes.

That freedom is powerful. It is also why agents need clear rules. This chapter shows you every piece of the AI Agent node, how to design one well, and how to build a personal assistant you can text from your phone.

## Anatomy of the AI Agent node

The AI Agent node has four inputs. Learn them, and you understand the whole node.

First, the **chat model**. This is the brain. It is the AI that does the thinking, such as Claude. A stronger model makes better decisions, but it costs more and answers more slowly. A smaller model is cheaper and faster, but it may pick the wrong tool. Start with a good middle model, and change it only when you see a real problem.

Second, the **memory**. Memory is what the agent remembers from earlier in the conversation. Without memory, the agent treats every message as the first one. With memory, it can say "you mentioned that yesterday" and mean it. The simplest memory in n8n is a window that keeps the last few messages. That is enough for most personal assistants.

Third, the **tools**. Tools are the things the agent can do. Each tool is a small action, like "check the calendar," "send an email," or "search the web." The agent reads the list of tools, picks the ones that fit the job, and uses them. An agent with no tools can only chat. An agent with good tools can get real work done.

Fourth, the **system message**. This is the instruction you write for the agent. It says who the agent is, what it can do, and what rules it must follow. It is the most important part of the whole node. A vague system message gives you a vague agent. A clear one gives you a reliable helper.

The node also has an output. After the agent finishes, it sends back its answer. That answer flows to the next box in your workflow, just like any other data.

> NOTE: Give the agent as few tools as it needs, not as many as you have. Ten tools it understands beat fifty tools it guesses about. Add a tool only when a real job needs it.

## Choosing the chat model

The model is the brain, so pick it with care. Three things matter: how well it decides, how fast it answers, and how much it costs.

A strong model is better at picking the right tool, and at recovering when a tool gives a strange result. Use a strong model when the agent handles money, messages to other people, or anything where a mistake is costly.

A fast, cheap model is fine for simple jobs. Sorting notes, answering easy questions, and drafting replies do not need the biggest brain. If the agent only has two or three tools, a smaller model will usually do fine.

Watch the cost. Every time the agent thinks, it uses the model. Every tool it calls adds more thinking. An agent that loops ten times costs ten times as much as one that answers at once. Set a limit on how many steps the agent may take. In n8n, that limit is a setting on the node. A limit of five to ten steps is a good start.

## Memory: remembering the conversation

There are two kinds of memory, and they do different jobs.

**Short-term memory** is the current chat. It holds the last few messages, so the agent can follow a conversation. In n8n, the Window Buffer Memory node does this. You set how many messages it keeps. Ten is a good number. More than that costs more, and the agent may get confused by old messages.

**Long-term memory** is facts that last between chats. Your name. Your time zone. The fact that you hate morning meetings. n8n does not keep this for you by itself. You store it somewhere, like a file or a database, and you load it into the system message each time. Chapter 3.6 covers memory for agents in more depth.

A simple rule: keep short-term memory in the node, and keep long-term facts in a short list you write yourself. Do not let the agent remember everything. Let it remember what matters.

## Tools: what the agent can do

A tool is a promise. It says "I can do this one thing, and here is what I need to do it." Each tool has a name, a short description, and a list of inputs. The agent reads the descriptions and decides which tool fits the job.

Write tool descriptions as if you were explaining them to a clever new colleague. Say what the tool does, when to use it, and what it needs. "Check the calendar for tomorrow" is better than "calendar". "Send an email to the address given, with the subject and body given" is better than "email".

Good starter tools for a personal assistant are: check the calendar, add a calendar event, search your notes, send an email, and search the web. Five tools. Each one does one clear job. That is enough to build something genuinely useful.

You can also give the agent **MCP tools**. MCP is a standard plug that lets AI use other apps, which you met in Chapter 2.20. In n8n, you can connect an MCP server and offer its tools to the agent. That is how one agent can reach dozens of apps through a single connection.

> TRY IT: Write down five tools your ideal assistant would have. For each one, write one sentence that says what it does and when to use it. If you cannot explain a tool in one sentence, the agent will not understand it either.

## Writing the system message

The system message is the agent's job description. Write it in plain words, in four parts.

First, say who the agent is. "You are a friendly personal assistant for Dylan. You help with calendar, email, and notes."

Second, list the tools and when to use each one. "Use the calendar tool to check or add events. Use the email tool only when the user asks you to send something."

Third, set the rules. "Never send an email without showing a draft first. Never delete anything. If you are unsure, ask."

Fourth, say how to answer. "Keep answers short. Use plain words. If you used a tool, say what you found in one sentence."

Keep it short. A system message of ten to twenty lines beats a wall of text. The agent reads it every time it thinks, so every extra line costs money and attention.

## Structured output and helper nodes

Sometimes you do not want a chatty answer. You want clean data, in JSON, that the next box can use. That is **structured output**. You tell the agent the exact shape you want, using a schema. The agent then answers in that shape, every time.

n8n has helper nodes for this. The Structured Output Parser takes the agent's answer and forces it into your shape. There are also small AI nodes that do one job well: summarise this text, pull out the names, sort this list. Use a helper node when the job is fixed. Use a full agent when the job needs decisions.

## RAG inside n8n

**RAG** means letting the AI read your own documents before it answers. You met it in Chapter 3.3. In n8n, it works like this: your documents are split into small chunks, each chunk is turned into a searchable form, and those chunks are stored in a database. When you ask a question, n8n finds the chunks that match, and gives them to the agent. The agent then answers using your documents, not just its general knowledge.

You do not need to build this on day one. But know that it exists. It is how an agent answers "what did we agree in last week's meeting?" instead of guessing.

## Humans in the loop

Some jobs should never run without a human check. Sending money. Deleting files. Replying to an angry customer. For those jobs, add a **human in the loop** step.

In n8n, that means the workflow pauses and waits for you. It might send you a message on Telegram with the draft and two buttons: approve or reject. The workflow only continues when you press approve. This is the single best safety habit in automation. The agent does the work. You keep the final say.

Set this up for any tool that changes something outside n8n. Reading is safe to automate. Writing, sending, and deleting should pause for a human, at least until you trust the agent.

> NOTE: An agent that can send email without asking is a loaded tool. Add an approval step before any action that reaches another person. It takes a minute to set up, and it prevents the kind of mistake you only make once.

## Build: a personal assistant on Telegram

Here is the build that pulls this chapter together. It takes about 30 minutes. You will text a bot on Telegram, and it will answer using your calendar and notes.

First, make a Telegram bot. Open Telegram, find the user called BotFather, and send it the message `/newbot`. Follow its questions. It will give you a token, which is a secret password for your bot. Keep it safe.

Next, in n8n, make a new workflow. Add a Telegram Trigger node. Paste your bot token into it. This box fires every time someone messages your bot.

Then add an AI Agent node. Connect a chat model, such as Claude. Add Window Buffer Memory, so the agent remembers the conversation. Add two tools to start: a calendar tool and a web search tool. You can add more later.

Write the system message. Keep it short. Say the agent is a personal assistant. Say it can check the calendar and search the web. Say it must never send email or delete anything. Say it should keep answers short.

Then add a Telegram node after the agent, to send the answer back to the person who asked. Connect the agent's answer to the message field.

Test it. Send your bot a message: "What is on my calendar tomorrow?" Watch the agent check the calendar, then answer. Try a follow-up: "And what about the day after?" The memory should let it follow the conversation.

When it works, activate the workflow. Your assistant now lives in your pocket. You can add tools one at a time, and approve each one before it goes live.

## Guardrails and cost tips

Guardrails are rules that keep an agent safe. Set a step limit, so a confused agent stops instead of looping forever. Set an approval step before any action that reaches the outside world. Write the system message so it says what the agent must never do.

Keep costs down with three habits. Use a cheaper model for simple agents. Keep memory short, so the agent does not re-read a long chat every time. And cache answers to repeated questions, so the agent does not think twice about the same thing.

Test your agent the way a critic would. Ask it strange questions. Ask it to do something it should refuse. Ask it the same question three times and see if the answers agree. Agents that pass those tests are ready for real work.

## Check yourself

1. What are the four inputs of the AI Agent node?
**Answer:** The chat model, the memory, the tools, and the system message.

2. Why should you give an agent only the tools it needs?
**Answer:** Because the agent chooses from the list you give it, and a long confusing list leads to wrong choices.

3. What is the difference between short-term and long-term memory?
**Answer:** Short-term memory is the current chat. Long-term memory is facts that last between chats, such as your time zone.

4. What is a human-in-the-loop step?
**Answer:** A pause where the workflow waits for a person to approve or reject an action before it continues.

5. Why set a step limit on an agent?
**Answer:** So a confused agent stops after a few steps instead of looping forever and running up a bill.

## In short

- An AI Agent node lets a model choose its own tools and order, instead of following fixed steps.
- The four inputs are the model, the memory, the tools, and the system message.
- Write tool descriptions in plain words, and keep the tool list short.
- The system message is the agent's job description: who it is, what it can do, and what it must never do.
- Add a human approval step before any action that reaches another person.
- Build the Telegram assistant one tool at a time, and test it like a critic before you trust it.
