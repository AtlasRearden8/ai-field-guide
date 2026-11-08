# 6.7 Build-along: a research agent that writes reports
<!-- original: ch. 116 -->

In this build you will run, learn, and change your own research agent. Give it a question. It plans, searches the live web, reads original sources, cross-checks claims, and saves a report with sources.

You will see exactly how the agent loop works. You will tune the research process. You will add a feature. You will test it offline. You will schedule weekly reports.

Time: about three hours. Level: intermediate, copy-paste friendly Python.

## What you will build

A Python agent that takes a question and returns a report.

- **Plan.** It breaks the question into smaller searches.
- **Search.** It searches the live web and reads the best sources.
- **Cross-check.** It compares what sources say and flags disagreements.
- **Write.** It saves a clear report with sources for every claim.

## Before you start

You need three things.

- **Python 3.10 or newer.** Check yours with `python3 --version` in a terminal.
- **An Anthropic API key** with a spending cap set.
- **The research-agent starter kit**, downloaded from the book's kit page. No account is needed.

The kit includes the agent code, an offline test mode, and a sample question. Keep a terminal open in the kit folder.

## Step 1: run the offline tests, 5 minutes

Offline tests check the agent without calling any AI or the web. They are fast and free. Run them first.

```
python3 -m pytest tests/
```

Line by line: `python3` runs Python. `-m pytest` runs the test tool. `tests/` is the folder of tests. If all tests pass, the kit works on your machine. If a test fails, read its message. It usually points at a missing piece. Install it and run the tests again.

Offline tests are your safety net. Run them after every change you make.

## Step 2: your first real report, 15 minutes

Run the agent with a real question. Pick something you care about. "What are the best ways to store solar power at home in 2026?"

```
python3 agent.py "What are the best ways to store solar power at home in 2026?"
```

Line by line: `python3 agent.py` runs the agent. The text in quotes is your question. The agent plans, searches, reads, and writes a report. It takes a few minutes. Watch the output. You will see each search and each source it reads.

Open the saved report. Read it. Check the sources. Are the claims backed by the links? Is anything missing? A good first report is rarely perfect. That is fine. You will tune it next.

## Step 3: understand the loop, 20 minutes

Open the agent code. Find the loop. It has four parts.

1. **Think.** The model reads the question and the results so far, then decides what to do next.
2. **Act.** It calls a tool: web search, fetch a page, or save the report.
3. **Observe.** It reads the tool's result.
4. **Repeat.** It thinks again, with the new information, until the report is done.

Two tools run on the server side: web search and fetch. **Server-side** means Anthropic runs them for you. Your own tool is `save_report`. It saves the finished report to a file.

Long research runs can pause. The agent may stop mid-task and wait. This is normal. The kit handles paused turns by saving its state and resuming. Do not kill a paused run. Let it finish.

## Step 4: tune the research process, 30 minutes

The system prompt controls how the agent researches. A **system prompt** is the hidden instruction that tells the agent how to behave. Change it to change the research.

Try these tunings, one at a time.

- **More sources.** "Use at least five independent sources for any factual claim."
- **Sceptical tone.** "Flag any claim where sources disagree. Say what each side claims."
- **Shorter reports.** "Keep the report under 800 words. Lead with the answer, then the evidence."
- **Freshness.** "Prefer sources from the last twelve months. Say the date of each source."

After each change, run the same question again. Compare the two reports. Keep the change if the report gets better. Undo it if it gets worse. Tuning is an experiment, not a guess.

## Step 5: add a feature, 45 minutes

Add one feature of your own. Here are three good ones.

- **A summary box.** After the report is written, ask the model for a three-bullet summary and put it at the top.
- **A confidence score.** Ask the model to rate its confidence in each claim as high, medium, or low, and show it next to the claim.
- **A comparison table.** For questions with options, add a table that compares them by price, pros, and cons.

Pick one. Write the code with Claude's help. Run the offline tests. Run a real question. Check the output. A feature that survives a real question is a feature that works.

## Step 6: schedule a weekly report, 20 minutes

A weekly report is the payoff. Pick a question that changes each week. "What happened in AI this week?" Or "What are the best new restaurants in my city?"

Schedule the agent with a cron job or a scheduled task. A **cron job** is a scheduled job on your computer that runs a command at a set time. It runs the agent every Monday at 7am and saves the report to a folder. You read it with your coffee.

Set a spending cap first. A scheduled agent that runs every week can spend money every week. Check the cost of one report. Multiply by four. Set the cap above that, but not far above it.

## Costs and responsibility

Research agents cost money. Each report uses many AI calls. Check the cost of one report before you schedule it. If a report costs a lot, shorten it, use fewer sources, or use a cheaper model for the search steps.

Check the sources. An agent can still get things wrong. It can cite a weak source. It can miss a disagreement. Read the report before you share it. You are the editor. The agent is the researcher.

Cite honestly. If the agent could not verify a claim, say so in the report. A report that admits what it does not know is more useful than one that pretends to know everything.

Keep a folder of your best reports. Over time it becomes a library of things you have learned properly, with sources. When a friend asks about a topic you researched, send them the report. Good research keeps paying off long after the day you wrote it.

> NOTE: Never let a research agent publish directly to the public. Always review the report first. A wrong claim with your name on it is your wrong claim, even if an agent wrote it.

## Troubleshooting

- **Tests fail.** Read the failure message. It usually names the missing piece. Install it and run the tests again.
- **The agent loops.** It searches the same thing again and again. Tighten the system prompt: "Stop searching when you have three good sources. Do not repeat a search you already ran."
- **The report has no sources.** The save step is broken, or the model skipped citations. Add to the prompt: "Every factual claim must cite a source with a link."
- **Costs spike.** A runaway loop is calling the model too often. Add a maximum step limit, such as twenty steps per report. The agent stops when it hits the limit.
- **Stale answers.** The agent used old sources. Add a freshness rule to the prompt and prefer recent sources.

> TRY IT: Run your first real report today on a question you genuinely care about. Read it with a sceptical eye. Check two sources by hand. Then tune one thing in the system prompt and run the same question again. Compare the two reports. You are now tuning an agent, not just using one.

## Check yourself

1. What are the four parts of the agent loop?
**Answer:** Think, act, observe, and repeat until the report is done.

2. Why should you run the offline tests first?
**Answer:** Because they check the kit works on your machine without calling AI or the web, so they are fast and free.

3. How do you tune the research process?
**Answer:** By changing the system prompt, one change at a time, and comparing the reports before and after.

4. Why should a research agent never publish directly?
**Answer:** Because it can get things wrong, and a wrong claim with your name on it is your wrong claim.

## In short

- A research agent plans, searches, reads, cross-checks, and writes a report with sources.
- Run offline tests first, then a real report on a question you care about.
- The loop is think, act, observe, repeat, with server-side search and your own save tool.
- Tune through the system prompt, one change at a time.
- Add one feature, test it offline and live, then schedule weekly reports.
- Set a spending cap, check the sources, and always review before sharing.
