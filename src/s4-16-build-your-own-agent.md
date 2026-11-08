# 4.16 Build your own agent
<!-- original: ch. 68 -->

You have used agents. Now you will build one, and understand exactly what happens inside. Once you have written an agent loop yourself, every "AI agent" product stops being mysterious. You can build custom agents for anything: research, files, inboxes, games, your home.

The secret is surprisingly small. An agent is a loop. Give it a goal and some tools. It picks a tool, looks at the result, and repeats until the job is done. That loop is the whole idea. This chapter builds it, step by step, in about 100 lines of Python.

## The whole secret, in one diagram

Here is the loop, in plain words.

You give the agent a goal. The agent thinks: what should I do next? It picks a tool, and calls it. The tool runs, and sends back a result. The agent reads the result, and thinks again. Has the goal been reached? If yes, it stops and gives you the answer. If no, it picks another tool, and the loop goes round again.

Goal, think, act, look, repeat. That is an agent. The model does the thinking. The tools do the acting. The loop holds them together.

Two details make the difference between a toy and a useful agent. First, a **step limit**. The agent may only loop a set number of times, say ten. If it has not finished by then, it stops and says so. That prevents an agent from looping forever and running up a bill. Second, a way to finish. The agent needs a clear way to say "I am done, here is the answer." Without that, it will keep working long after the job is finished.

## When do you need an agent?

Not every job needs an agent. Use an agent when the job has more than one step, when the steps depend on what the last step found, or when you cannot list the steps in advance.

Good agent jobs: research a topic across several sources, then write a summary. Tidy a folder, by looking at each file and deciding where it goes. Answer a question that needs checking a calendar, then an inbox, then a document.

Bad agent jobs: a job with one fixed step. A job where every step is known in advance. A job where a mistake is costly and no human is watching. For those, a simple script or a fixed workflow is better, cheaper, and safer.

Ask yourself one question. Can I write the steps down in advance? If yes, you do not need an agent. If no, because the steps depend on what you find, you do need one.

> NOTE: Start with one agent, one goal, and two or three tools. Agents grow by adding tools, not by adding cleverness. A small agent that works beats a big agent that wanders.

## Hands-on: run the agent

You need Python 3.10 or newer, and an Anthropic API key, as in Chapter 4.15. You also need the starter code. The starter is a single Python file, about 100 lines long, called `agent.py`. It holds the loop, the tools, and the code that talks to Claude.

Get the starter file from the book's starter-kit list, and save it in a folder on your computer. Open the folder in your terminal. Install the library it needs, which is the `anthropic` package. Then run it with a simple goal, like "Find the largest file in this folder and tell me its name and size."

Watch what happens. The agent will think, call a tool to list the files, read the result, and answer. It will print each step as it goes, so you can see the loop working. That printed trace is the best teacher in this chapter. Read it slowly.

If it fails, check two things. First, is your API key set? Second, is Python new enough? Fix those, and run it again.

## Walkthrough of agent.py

Here is what the starter file does, in order. You do not need to memorise the code. You need to understand the shape.

First, it sets up the connection to Claude, using your API key. Second, it defines the tools. Each tool is a small Python function, with a name, a description, and a list of inputs. Third, it defines the loop. Fourth, it runs the loop with your goal.

The loop itself is short. Here it is, in plain Python, with comments. Read it line by line.

```
  # Keep going, but never more than 10 steps.
for step in range(10):
    # Ask Claude what to do next.
    reply = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=500,
        tools=tools,
        messages=history,
    )

    # If Claude gives a final answer, print it and stop.
    if reply.stop_reason == "end_turn":
        print(reply.content[0].text)
        break

    # Otherwise, run the tool Claude asked for.
    tool_call = find_tool_call(reply)
    result = run_tool(tool_call)

    # Add the tool result to the history, and loop again.
    history.append(tool_call)
    history.append(result)
```

Line two sets the step limit to ten. Line four asks Claude what to do next, and passes the list of tools. Line eleven checks if Claude has finished. If it has, the loop prints the answer and stops. Line sixteen finds the tool Claude asked for. Line seventeen runs it. Lines twenty and twenty-one add the tool call and its result to the history, so Claude can see what happened when it thinks again.

That is the whole agent. A loop, a model, some tools, and a history that grows. Everything else in this chapter is a better version of one of those parts.

## Designing great tools

Tools are where an agent's power lives. A good tool does one job, does it well, and says clearly what it needs.

Write each tool's description as if you were explaining it to a clever colleague. Say what it does, when to use it, and what it returns. "List the files in a folder, and return their names and sizes" is good. "Files" is not.

Give tools safe inputs. If a tool deletes files, make it ask for a clear yes, or do not give the agent that tool at all. If a tool sends email, make it show a draft first. The safest tool is one that only reads. Reading cannot break anything. Writing, sending, and deleting can.

Start with three tools. A tool to list files. A tool to read a file. A tool to search the web. With those three, your agent can already do research, answer questions, and explore a project.

> TRY IT: Add one new tool to the starter agent. Make a tool that returns today's date. Give it a clear name and description. Then ask the agent: "What day is it today, and what files did I change this week?" Watch it use your new tool.

## Details that separate toy agents from good ones

Five details make an agent reliable. Add them one at a time.

First, a step limit, as you saw above. Ten steps is a good start. Second, a clear system prompt. Tell the agent its job, its tools, and its rules, in plain words. Third, good error messages. When a tool fails, it should say why, in words the agent can act on, like "No file with that name exists" instead of "Error 404."

Fourth, a way to stop early. If the agent finds the answer in step two, it should stop, not use all ten steps. The "I am done" signal in the loop above does that. Fifth, a log. Print each step, so you can see what the agent did, and why. When an agent makes a mistake, the log shows you where it went wrong.

## Levelling up your agent

Once your small agent works, you can grow it in four directions.

Add **memory**, so it remembers facts between chats. Chapter 3.6 covers memory for agents. Add more tools, one at a time, as real jobs need them. Add **guardrails**, such as asking a human before any action that changes something outside the agent's folder. And add **evaluations**: a small set of test goals, which you run after each change, to check the agent still works.

When the agent outgrows a single file, move to an SDK or a framework. The Claude Agent SDK gives you the same loop, with more power, in a form you can build into a real app. Agent frameworks, which Chapter 4.17 tours, give you ready-made parts for memory, multi-agent work, and tracing. You do not need them yet. Build the loop by hand first. Then you will understand what the frameworks are doing for you.

## Agent design principles

Keep these five principles on a card by your desk.

One goal, one agent. An agent with a clear job works better than an agent with ten jobs.

Few tools, well described. Three clear tools beat twenty vague ones.

Short system prompt, clear rules. Say what to do, and what never to do.

Human check before outside actions. Reading is safe. Sending, deleting, and spending need a human.

Log everything. If you cannot see what the agent did, you cannot fix it when it goes wrong.

## Check yourself

1. What is an agent, in one sentence?
**Answer:** An agent is an AI that takes actions to reach a goal, by picking tools, looking at the results, and repeating until the job is done.

2. What are the parts of the agent loop?
**Answer:** A goal, a model that thinks, tools that act, a history of what happened, and a step limit.

3. Why does an agent need a step limit?
**Answer:** So it stops after a set number of steps instead of looping forever and running up a bill.

4. When should you use an agent instead of a fixed workflow?
**Answer:** When the steps depend on what the last step found, and you cannot list them all in advance.

5. What makes a good tool description?
**Answer:** One that says what the tool does, when to use it, and what it returns, in plain words.

## In short

- An agent is a loop: think, act, look, repeat, until the goal is reached or the step limit runs out.
- The loop needs a model, tools, a history, and a clear way to finish.
- Start with one goal and two or three well-described tools.
- Add a step limit, a clear system prompt, good error messages, and a log.
- Use an agent when the steps depend on what you find; use a fixed workflow when you know the steps in advance.
- Grow by adding memory, tools, guardrails, and tests, one at a time.
