# 4.17 Agent frameworks tour
<!-- original: ch. 69 -->

Once you have written an agent loop by hand, as you did in Chapter 4.16, frameworks stop being magic. They start being time-savers. A framework is a starter kit for building agents. It gives you memory, multi-agent handoffs, guardrails, tracing, retries, and deployment patterns, ready made, instead of you building each one from scratch.

This chapter tours the major frameworks, shows you the same tiny agent in several of them, and helps you pick one without getting stuck choosing.

## Do you even need a framework?

Often, the answer is no. That is the first thing to say, and the most useful.

You do not need a framework when your agent has one goal, a few tools, and a short loop. The hand-written loop from Chapter 4.16 is enough. You do not need one when a fixed workflow will do the job. And you do not need one when an existing agent, like Claude Code or an n8n AI Agent, already does what you want.

You do need a framework when your agent has many tools, when it needs memory that lasts, when several agents must work together, when you need to see what happened step by step, or when you are building something for other people to use. A framework gives you those parts, tested and ready, instead of you inventing them.

The rule is simple. Build the loop by hand first. When you feel the pain of a missing part, that is the moment to pick a framework that provides it.

> NOTE: A framework does not make a bad agent good. It makes a good agent easier to grow. If your agent is confused, fix the goal, the tools, and the system prompt first. Then reach for a framework.

## The framework landscape

Here are the main frameworks, in plain words. You do not need to learn them all. Read the list, and notice which one fits the way you think.

The **Claude Agent SDK** is Anthropic's toolkit for building agents with Claude. It gives you the same loop Claude Code uses, with tools, memory, and permissions, in a form you can put inside your own app. If you like Claude Code, this is the natural next step.

The **OpenAI Agents SDK** is OpenAI's toolkit. It is built around handoffs, where one agent passes a job to another agent that is better suited to it. If you use OpenAI models, start here.

**Google ADK**, the Agent Development Kit, is Google's toolkit. It works well with Gemini models and Google's cloud tools. If your work lives in Google's world, it is a natural fit.

**LangGraph** is a popular framework built on LangChain. It treats an agent as a graph, which is a map of steps joined by lines. Each step is a node, and the agent moves between them based on conditions. It is powerful, and it is the most flexible of the big frameworks. It is also the one with the most to learn.

**CrewAI** treats agents as a crew. Each agent has a role, like researcher, writer, or editor. They work together on a task, passing work between them. It is a friendly way to think about multi-agent work, and Chapter 4.18 covers the team patterns in depth.

The **Vercel AI SDK** is a toolkit for building AI features into web apps, in TypeScript. It is less about agents, and more about putting AI into a website: chat, streaming, tool use, and structured output, with little fuss. If you are building a web app, it is worth knowing.

There are also TypeScript options for agents, such as the Vercel AI SDK and the OpenAI Agents SDK for JavaScript. If you work in TypeScript rather than Python, those are your starting points. The ideas are the same. Only the language changes.

## The same agent in four frameworks

Imagine a tiny agent with one job: "Check the weather in a city, and say if I need a coat." It has one tool: get the weather. Here is how that agent looks in each framework, in plain words, not code.

In the Claude Agent SDK, you define the tool, write a short system prompt, and start the loop. The SDK handles the back-and-forth with the model, the tool calls, and the permissions.

In the OpenAI Agents SDK, you define an agent with a name, instructions, and tools. You run it with a message. The SDK handles the loop, and it can hand the job to another agent if the first one decides it should.

In LangGraph, you draw the steps as a graph. One node calls the model. One node runs the tool. Lines join them, with a condition that says "if the model asked for a tool, go to the tool node, else finish." It is more work to set up, but you can see the whole flow as a picture.

In CrewAI, you define two agents: a researcher that checks the weather, and a writer that turns the result into a friendly message. You give them a task, and the crew runs it in order. It is the most human way to describe the work.

Same agent. Four shapes. The shape that matches how you think is the right one to try first.

## Graphs, crews, and handoffs: three mental models

Frameworks organise agents in three main ways. Learn the three models, and you can read any framework's docs.

A **graph** is a map of steps. The agent moves from step to step, following lines, until it reaches the end. LangGraph is the clearest example. Graphs are good when the flow has branches, loops, and conditions, and you want to see it all as a picture.

A **crew** is a team with roles. Each agent has a job, and they pass work to each other. CrewAI is the clearest example. Crews are good when a task naturally splits into roles, like research, writing, and editing.

A **handoff** is a pass. One agent starts a job, and when it meets a part it is not suited to, it hands the job to another agent. The OpenAI Agents SDK is built around this idea. Handoffs are good when different agents are experts in different things, like a triage agent that routes questions to a billing agent or a support agent.

You do not need to pick one model forever. You need to recognise which model a framework uses, so you can think in its terms while you use it.

## Tracing and observability

**Tracing** means recording what an agent did, step by step, so you can look at it later. **Observability** is the wider idea: being able to see inside a running system, to understand why it did what it did.

When an agent works, it makes many calls. It thinks, it calls a tool, it reads the result, it thinks again. Without tracing, you only see the final answer. With tracing, you see every step, how long each step took, and what it cost.

Most frameworks have tracing built in, or they connect to a tracing tool. Turn it on early. When your agent makes a mistake, the trace shows you where it went wrong. Was the tool description unclear? Did the model pick the wrong tool? Did the tool return a confusing result? The trace answers those questions.

> TRY IT: Pick one framework from this chapter. Read its tracing docs for ten minutes. Find out what it records, and where you look at the trace. You do not need to build anything yet. Just know where the record lives.

## Protocols: MCP, A2A, and friends

Frameworks do not live alone. They speak shared languages, called **protocols**, so tools and agents from different makers can work together.

**MCP** is the plug that lets AI use tools, which you met in Chapter 2.20. Many frameworks can use MCP servers as tools, and some can act as MCP servers themselves. That means an agent built in one framework can use tools built for another.

**A2A** is a protocol for agents talking to agents. It lets one agent ask another agent for help, even if they were built with different tools. It is newer than MCP, and it is still growing, but it points to a future where agents from different makers can work as a team.

You do not need to use these protocols on day one. Know that they exist. When you pick a framework, check that it speaks MCP. That one check keeps your options open.

## How to choose: a decision flow

Here is a short flow. Answer each question in order.

Do you already use Claude Code, and want the same power inside your own app? Pick the Claude Agent SDK.

Do you use OpenAI models, and like the idea of agents handing jobs to each other? Pick the OpenAI Agents SDK.

Do you work in Google's world, with Gemini and Google Cloud? Pick Google ADK.

Do you want the most flexible flow, drawn as a map, and you are happy to learn more? Pick LangGraph.

Do you think in teams and roles, and want the friendliest start? Pick CrewAI.

Are you building a web app in TypeScript, and you want AI features with little fuss? Pick the Vercel AI SDK.

If you are still unsure, pick the one that matches the model you already use. The model matters more than the framework. You can change frameworks later. Changing models is harder.

## Framework pitfalls

Three traps catch beginners. First, picking a framework before building the loop by hand. You will not understand what the framework does for you, and you will fight it instead of using it. Build the loop first, as Chapter 4.16 showed you.

Second, adding too many agents too soon. One agent that works beats five agents that confuse each other. Add a second agent only when the first one has a clear job it cannot do.

Third, ignoring cost. Frameworks make it easy to add steps, tools, and agents. Each one costs money and time. Trace your agent, count the steps, and cut the ones that do not earn their place.

## Check yourself

1. What is an agent framework, in plain words?
**Answer:** A starter kit for building agents, with ready-made parts for memory, multi-agent work, guardrails, tracing, and deployment.

2. When do you not need a framework?
**Answer:** When your agent has one goal, a few tools, and a short loop, or when a fixed workflow or an existing agent already does the job.

3. What is the difference between a graph, a crew, and a handoff?
**Answer:** A graph is a map of steps, a crew is a team with roles, and a handoff is one agent passing a job to another agent.

4. What is tracing?
**Answer:** Recording what an agent did step by step, so you can look back and see where it went wrong.

5. What is MCP, and why does it matter when picking a framework?
**Answer:** MCP is the standard plug that lets AI use tools, and a framework that speaks MCP can use tools built for other systems.

## In short

- Build the agent loop by hand first; pick a framework when you feel a missing part.
- The main frameworks are the Claude Agent SDK, OpenAI Agents SDK, Google ADK, LangGraph, CrewAI, and the Vercel AI SDK.
- Frameworks organise agents as graphs, crews, or handoffs.
- Turn on tracing early, so you can see what your agent did and why.
- Check that a framework speaks MCP, to keep your options open.
- Start with one agent, and add a second only when the first has a job it cannot do.
