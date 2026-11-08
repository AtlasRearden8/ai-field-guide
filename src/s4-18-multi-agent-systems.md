# 4.18 Multi-agent systems: teams of AIs
<!-- original: ch. 70 -->

One agent is useful. Several agents that divide the work can take on much bigger jobs: deep research across dozens of sources, big codebases, content pipelines, and "build it and then check it" loops. This chapter explains when multi-agent setups are worth it, the six core patterns, and how to try them today without drowning in complexity.

## Why multiple agents?

A single agent has limits. Its working memory is limited. It can only focus on so much at once. When a task is large, a single agent starts to forget details, mix up steps, or make confident mistakes.

Splitting the work helps in three ways. First, **focus**: each agent has one role, and a short, clear job. It does not need to hold the whole task in mind. Second, **parallel work**: several agents can work at the same time, on different parts, so a big job finishes faster. Third, **checking**: one agent can check another's work, and catch mistakes the first one missed.

But teams cost more. Each agent uses the model. Each agent needs instructions. And teams can go wrong in ways a single agent cannot: they can misunderstand each other, repeat each other's work, or argue in circles. Use a team only when one agent genuinely falls short.

The honest rule: start with one agent. Split only when you see a specific failure. "The agent forgets the plan when the research gets long" is a reason to split. "Teams sound cool" is not.

> NOTE: A team of agents is like a team of people. It needs clear roles, clear handoffs, and one person, or one agent, in charge. A team with no leader drifts.

## Pattern 1: Orchestrator and workers

The **orchestrator** is the lead agent. It does not do the work itself. It plans the job, splits it into pieces, gives each piece to a worker agent, and joins the results together.

This is the most common pattern, and the best one to learn first. Example: you ask for a report on a topic. The orchestrator splits the topic into five questions. It gives one question to each of five worker agents. Each worker researches its question. The orchestrator reads all five answers, and writes the final report.

Use this pattern when a job splits neatly into independent pieces. Do not use it when the pieces depend on each other, because the workers will wait, or guess, instead of working together.

## Pattern 2: Pipeline, the assembly line

A **pipeline** is a line of agents, each doing one step, in order. The first agent's output is the second agent's input, and so on, like an assembly line.

Example: a content pipeline. Agent one researches a topic. Agent two writes a draft from the research. Agent three edits the draft for clarity. Agent four checks the facts. Each agent does one job well, and the work flows down the line.

Pipelines are simple to understand and easy to test, because you can check each step's output before it goes to the next step. Their weakness is that an early mistake flows down the whole line. So check the early steps most carefully.

## Pattern 3: Builder and critic loop

In this pattern, two agents work against each other, in a loop. The **builder** makes something. The **critic** reads it and finds problems. The builder fixes the problems. The critic checks again. The loop repeats until the critic is happy, or until a set number of rounds is reached.

Example: the builder writes a piece of code. The critic reviews it for bugs and for clarity. The builder fixes what the critic found. After two or three rounds, the code is better than either agent could have made alone.

This pattern is powerful for work where quality matters and where mistakes are easy to spot. Set a limit on the rounds, such as three. Without a limit, the builder and the critic can argue forever, each finding new nits to pick.

## Pattern 4: Debate and ensemble

In a **debate**, several agents argue different sides of a question, and a judge agent picks the best answer. In an **ensemble**, several agents answer the same question independently, and you take the answer most of them agree on.

Use these patterns when you need a careful answer to a hard question, and when you can afford the cost of asking several times. They are good for research, for planning, and for decisions where being wrong is costly.

Do not use them for simple questions. Asking five agents what time it is wastes money and time. Save debate for questions that deserve it.

## Pattern 5: Handoffs, or routing

A **handoff** is a pass. One agent starts with a request, works out what kind of request it is, and hands it to the agent best suited to handle it.

Example: a support system. A triage agent reads each incoming message. If it is about billing, it hands it to the billing agent. If it is about a technical fault, it hands it to the technical agent. If it is angry, it hands it to a human.

Handoffs are the pattern behind most real customer-facing systems. They are simple, they scale well, and they keep each agent's job small and clear.

## Pattern 6: Parallel variants, best of N

In this pattern, several agents do the same job, each in a slightly different way, and you pick the best result. The name "best of N" means "best of N tries."

Example: you ask three agents to write a headline for an article. Each one writes a different headline. You read all three, and pick the best. Or a judge agent picks the best, using rules you wrote.

This pattern is cheap to understand and easy to try. Its weakness is cost: you pay for N agents instead of one. Use it when quality matters more than cost, and when the job is short enough that trying it three times is affordable.

> TRY IT: Pick one short job, like writing a headline or a one-line summary. Ask a single agent to do it three times, with a fresh conversation each time. Read the three answers. Pick the best. You have just run a best-of-three ensemble, with no framework at all.

## Try it today, easiest to hardest

You do not need a framework to try multi-agent work. Here is the ladder, from easiest to hardest.

Easiest: use subagents in Claude Code. Ask the main agent to send research to a subagent, while it keeps working. You already met subagents in Chapter 4.11.

Next: use the AI Agent node in n8n, with a clear system message that says "you are the orchestrator, split this job into three parts." Chapter 4.4 showed you that node.

Next: build a pipeline with a framework, such as CrewAI or LangGraph, where each agent has a role and the work flows in order.

Hardest: build a full orchestrator-workers system with tracing, guardrails, and evaluations. That is a real project, not an afternoon experiment. Save it for when you have a job that truly needs it.

## Design tips

Give each agent one role, in one sentence. Write down how agents hand work to each other, and what the handoff looks like. Keep the messages between agents short and structured, so nothing gets lost. Give the team a leader, even if the leader only plans and joins results. And set limits everywhere: a limit on rounds, a limit on steps, and a limit on cost.

## Failure modes and fixes

Teams fail in predictable ways. Here are the four most common, and their fixes.

Agents repeat each other's work. Fix it by giving each agent a clear, non-overlapping job, and by telling the orchestrator to check what is already done before it assigns work.

Agents misunderstand each other. Fix it by making handoffs structured. Instead of free text, pass a short list of facts, with labels, so the next agent knows exactly what it received.

Agents argue in circles. Fix it with a round limit. Three rounds, then stop, and let a human decide.

Costs balloon. Fix it by tracing the team, counting the steps, and asking whether each agent earns its place. A team of three that works is better than a team of eight that wanders.

## Two examples

A **content studio crew** has four agents. A researcher gathers facts. A writer turns the facts into a draft. An editor tightens the draft. A fact-checker checks the claims. The work flows in a pipeline, and a human reads the final draft before it is published.

A **coding team in Claude Code** has a main agent and two subagents. The main agent plans a feature. One subagent searches the codebase for related code. Another subagent writes the tests. The main agent writes the feature, runs the tests, and reports back. Each agent has one job, and the main agent stays in charge.

## Check yourself

1. What are the three benefits of splitting work across agents?
**Answer:** Focus, because each agent has one clear role; parallel work, because several agents can work at once; and checking, because one agent can catch another's mistakes.

2. What is the orchestrator-workers pattern?
**Answer:** A lead agent plans the job, splits it into pieces, gives each piece to a worker agent, and joins the results together.

3. What is a builder-critic loop?
**Answer:** One agent makes something, another agent finds problems in it, the first fixes them, and the loop repeats until the work is good or the round limit is reached.

4. What is a handoff?
**Answer:** One agent passing a job to the agent best suited to handle it, such as a triage agent routing a billing question to a billing agent.

5. Why should you start with one agent before building a team?
**Answer:** Because a team costs more and can go wrong in new ways, so you should split only when you see a specific failure in the single agent.

## In short

- Use a team only when one agent genuinely falls short, and start with one agent first.
- The six patterns are orchestrator-workers, pipeline, builder-critic, debate and ensemble, handoffs, and best of N.
- Give each agent one role, keep handoffs structured, and give the team a leader.
- Set limits on rounds, steps, and cost, so a team cannot argue or spend forever.
- Try subagents in Claude Code first, then n8n, then a framework when the job truly needs it.
- A small team that works beats a large team that wanders.
