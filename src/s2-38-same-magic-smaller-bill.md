# 2.38 Same magic, smaller bill
<!-- original: ch. 106 -->

AI can cost almost nothing or a surprising amount, based on how you use it. The good news: a few simple habits usually cut costs a lot with no loss in quality. This chapter is your money-saving playbook for subscriptions, API bills, and automation platforms. How the bill works. The steps to take, in order. Model routing. Guards against surprise bills. And worked examples.

AI costs build up through subscriptions and per-token API use. This chapter shows how to cut your bill while keeping quality where it matters.

## Subscriptions: stop overpaying

One main paid assistant. Free tiers for the rest. Most people do not need three paid plans. Audit every three months. Cancel tools you have not opened in 30 days. Annual billing is usually cheaper for tools you are sure about. Team or business plans only make sense when you need admin or privacy features. They cost more per seat.

Check what is bundled. Paid Claude plans include Claude Code. Google and Microsoft bundles include Gemini and Copilot features. Hitting limits often? Compare the higher tier's cost to your API usage. Sometimes upgrading is cheaper than pay-per-token. Sometimes it is the other way round. Do the maths before you upgrade.

> NOTE: A subscription you forgot is the most expensive kind. Audit every three months. Set a calendar reminder now.

## API costs: understanding the bill

The bill follows a simple formula. Cost is roughly input tokens times input price, plus output tokens times output price, minus discounts for cached input and batch jobs. A **token** is a small chunk of text, about three quarters of an English word.

| Fact | What it means |
|---|---|
| Output costs several times more than input | Long answers are the expensive part |
| Thinking tokens are billed as output | Deep thinking on easy tasks wastes money |
| Agents multiply calls | A ten-step agent resends the growing conversation about ten times |
| Tool results count as input | Big web pages or file dumps add up fast |
| Images and PDFs use tokens too | Resize images, send only needed pages |

Always record usage from API replies: input, output, and cached tokens. You cannot improve what you cannot see.

## The levers, in order

Start with free wins. These cost no quality at all.

| Lever | Savings | How |
|---|---|---|
| Prompt caching | Big on repeated prefixes | Keep stable content, like system prompts and docs, at the start. Put changeable content at the end. |
| Trim the input | Proportional | Send the relevant excerpt, not the whole file. Summarise old conversation turns. |
| Filter before AI | Up to 100 percent per item | Plain workflow logic skips items that do not need AI. |
| Batch API | Around half off | For non-urgent bulk jobs, like overnight classification. |
| Deduplicate | Varies | Do not reprocess the same email, doc, or row. Store what is done. |
| Cache results | Up to 100 percent on repeats | Same question twice? Return the saved answer. |

Then the trade-offs. Test these with your eval set from chapter 2.37.

| Lever | How |
|---|---|
| Lower effort or thinking | Simple tasks do not need deep reasoning. Tune per task. |
| Smaller model for simple steps | Classify, extract, and route with small, fast models. |
| Cap output length | Concise formats, like JSON or bullets, and a sensible max length. |
| Fewer agent turns | Better tool descriptions mean fewer wasted calls, plus turn limits. |
| Local models for grunt work | High-volume, low-stakes tasks for the cost of electricity. |

Measure before you switch to a cheaper model. Run your eval set on the cheaper option. Judge cost per finished task, not per request. A cheap model that needs retries is not cheap.

> TRY IT: Pick one automation or script you run. Record its token use for a day. Then use just two tricks, trimming plus caching, or a smaller model for one step, and compare. Watching the number drop is deeply satisfying.

## Model routing: the biggest structural win

**Model routing** means sending easy jobs to cheap models and hard jobs to top models. Most tasks are easy. About 80 to 90 percent of incoming work can go to a small, fast model. Only the hard 10 to 20 percent needs the frontier model.

Three patterns work well. A cheap sorter sends jobs by difficulty. A small model answers first and hands over when unsure. Or a big model plans while small models run the steps. The pattern matters less than the principle: save costly smarts for where they earn their keep.

## Automation-platform costs

| Platform | Billing unit | Optimisation |
|---|---|---|
| Zapier | Tasks, each action step | Filters early, use a formatter instead of AI for simple text, fewer steps |
| Make | Operations, each module run | Aggregate before processing, avoid unnecessary iterations |
| n8n Cloud | Executions, whole runs | One run costs the same however many steps it has. Check the current price for plan limits. Self-hosting removes limits |
| All | Plus AI API costs | Cache, batch, and right-size models inside workflows |

Prices change often. Check the current price before you commit to a platform. The optimisation habits do not change: filter early, batch often, and right-size the model inside each step.

## Guardrails against surprise bills

Spend limits in every API console, with hard caps and alerts at 50 and 80 percent. Separate API keys per project, so you can see what is spending. Turn limits on agents and max items on loops. Rate limits on any public-facing app that calls AI. Bots can drain your budget. Test on five items before running on 5,000. A monthly review of usage dashboards.

## Worked example: the email summariser

The job: summarise about 100 emails a day for a morning digest.

- **Naive version.** Frontier model, max thinking, full threads with quoted history, one call per email. The most expensive way to do it.
- **Trimmed version.** Only the latest message in each thread. Concise output format. Much cheaper, same useful digest.
- **Cached and routed version.** Shared instructions cached. A small model triages. Only the 10 percent of important emails get the frontier model. Far cheaper again.
- **Batched version.** The same, via the Batch API overnight. Even less.

Same useful digest, a fraction of the cost. The pattern is always the same. Route easy work to cheap paths. Save costly smarts for where they earn their keep. Real prices change by model and over time, so always measure your own.

> NOTE: Cost per finished task is the only number that matters. A cheap model that needs three retries costs more than a good model that gets it right first time.

## A monthly money routine

Once a month, spend fifteen minutes on your AI money. Open every usage dashboard. Write down the total. Compare it with last month. If it jumped, find why. One automation looping? One agent running wild? One team member on a pricey model? Then check your subscriptions. Anything unused for 30 days gets cancelled. Then check your eval set. Is the cheap model still good enough for the easy jobs? If yes, keep it. If quality slipped, route a little more work to the bigger model. Small monthly checks beat one big yearly panic. Money leaks are quiet. A routine makes them loud.

> NOTE: Put the routine on your calendar, same day each month. A habit you schedule is a habit you keep.

## Check yourself

1. Where should stable content go in a prompt for caching to work?
**Answer:** At the start: system prompt, documents, tool descriptions. Changeable content goes at the end.

2. Why is output more expensive than input?
**Answer:** Output tokens usually cost several times more than input tokens, and thinking tokens are billed as output.

3. What is model routing?
**Answer:** Sending easy tasks to small, cheap models and only hard tasks to top models, often with a cheap sorter or a hand-over step.

4. What are the three guardrails every API account needs?
**Answer:** Spend limits with alerts, separate keys per project, and turn limits on agents.

5. Why test on five items before running on 5,000?
**Answer:** To catch loops and bugs, and to measure the real cost, before a small mistake becomes a big bill.

## In short

- One main subscription, a check every three months, and look at what is bundled.
- On APIs, output and thinking tokens are the costly part, and agents multiply calls.
- Use free wins first: caching, trimming, filtering, batching, and removing repeats.
- Model routing is the biggest structural win: small models for most work, big models where it matters.
- Spending caps, one key per project, turn limits, and small test runs stop surprise bills.
- Judge cost per finished task, not per request.
