# 2.37 How to judge and compare AI tools
<!-- original: ch. 105 -->

"Which model is best?" The honest answer is "best at what, for you?" Leaderboards are a starting point. The only test that truly matters is your own tasks. This chapter teaches the skill that sets strong AI users apart: testing things properly. It is easier than it sounds. It is fun. It saves money, time, and embarrassment.

An **evaluation**, or eval, is a planned test. Give several AI models or tools the same real tasks. Score the results fairly. See which works best for your needs. Evals also show whether a change made your system better or worse.

## Why evaluate?

| Reason | Example |
|---|---|
| Pick the right model or tool | A small, cheap model might do your job just as well |
| Know if a change helped | Did the new prompt actually improve answers, or just feel better? |
| Catch regressions | A model update quietly broke your invoice extraction |
| Build trust | Before automating something important |
| Save money | Stop over-buying capability you do not need |

A **regression** is when something that worked stops working. Models update silently. A prompt that worked last month can fail this month. Evals catch that before your customers do.

## The 15-minute personal eval

Pick ten real tasks you care about. Write them in a spreadsheet. Add the criteria for each one. Run each task through two or three models. Score them.

| Task | Criteria | Model A | Model B | Model C |
|---|---|---|---|---|
| Reply to an angry customer email | Empathetic, concise, offers a fix, no over-promising | 4/5 | 5/5 | 3/5 |
| Extract invoice fields | All six fields correct | 5/5 | 4/5 | 5/5 |
| Summarise a meeting | Captures all decisions and owners | 3/4 | 4/4 | 4/4 |
| Explain a concept to a 12-year-old | Accurate, simple, one good analogy | 5/5 | 4/5 | 4/5 |

Put it in a spreadsheet. Well done: you have built an eval set. Keep it. Re-run it when something new ships. It becomes more valuable every time you reuse it.

> TRY IT: Write ten prompts that matter to you. Run them through three assistants. Free tiers are fine. Score them blind, without knowing which answer came from which model. Share your results with a friend.

## Scoring methods

| Method | Use for | Notes |
|---|---|---|
| Exact match or checks | Extraction, classification, maths, code tests | Objective and automatable: the gold standard |
| Rubric scoring by you | Writing, advice, creativity | Three to five specific criteria, not vibes |
| Pairwise comparison | "Which is better, A or B?" | Humans are better at comparing than rating |
| AI as judge | Scaling rubric scoring | A strong model grades outputs against your rubric |
| Real-world signals | Deployed bots and tools | Thumbs up or down, edits users make, escalation rates |

A good **rubric** is a scoring guide. It must be specific. "Good tone" is vague. "Acknowledges the problem in the first sentence" is specific. "Accurate" is vague. "All prices match the price list" is specific. "Helpful" is vague. "Ends with one clear next step" is specific. "Concise" is vague. "Under 120 words" is specific. Write rubrics before you look at the answers. That keeps you honest.

## AI as judge, and how not to fool yourself

A strong model can grade outputs against your rubric. That scales your testing. But judges have biases. Watch for them.

| Pitfall | Fix |
|---|---|
| Position bias: prefers the first answer | Randomise order, or judge each answer alone |
| Length bias: prefers longer answers | Put length limits in the rubric |
| Self-preference: likes its own model's style | Use a different model as judge, and spot-check |
| Vague rubrics | Binary, specific criteria |
| Blind trust | Compare the judge's scores with yours on ten to twenty examples |

Score blind whenever you can. Hide which model wrote which answer. Your hopes about which model is better will bend your scores otherwise. That is human, not a flaw. Blind scoring removes it.

> NOTE: One amazing or awful answer is not a trend. Test ten or more. Variance is real. Run important tests two or three times.

## Arenas and leaderboards

| Resource | What it measures |
|---|---|
| LMArena | Human preference votes in blind head-to-heads: text, vision, coding, images, and more |
| Artificial Analysis | Quality indices, speed, and price comparisons |
| SWE-bench and coding leaderboards | Real-world coding tasks |
| Specialised leaderboards | Embeddings, agents, long context, reasoning |
| Vendor model cards | Benchmarks the labs report; read the fine print |

Leaderboards show you who is in the top group. Your own eval shows you who is best for you. Test scores can also be "maxed out," where everyone scores near 100 percent, or leaked into training data. Treat them as hints, not proof. Boards move weekly as new models ship. Check the live board on the day you choose.

## Evaluating your own AI systems

Building chatbots that look up your own documents, agents, or automations? Treat quality like code. Keep a test set, inputs plus the answers you expect, in a file. Re-run it after every change: prompt, model, chunk size, tool description. Track results over time: accuracy, correct "I don't know" answers, cost per task, and speed.

Include tricky cases: empty input, trick questions, hidden-instruction attacks, and questions with no answer in the docs. Judge agents by what they achieve and how they get there: did it finish, and did it take a sensible path? Helpful tools include promptfoo, Braintrust, LangSmith, Langfuse, and the providers' own eval tools.

## Comparing tools, not just models

When choosing between three meeting-note apps or two automation platforms, score more than quality.

| Criterion | Tool A | Tool B | Tool C |
|---|---|---|---|
| Quality (1 to 5) | | | |
| Setup time | | | |
| Integrations I need | | | |
| Privacy fit | | | |
| Monthly cost | | | |
| Joy factor | | | |

Joy factor is real. A tool you enjoy using gets used. A tool you dread gets abandoned. Score it honestly.

## Mindset tips

Beware the first impression. One amazing or awful answer is not a trend. Test ten or more. Variance is real. Run important tests two or three times. Cheaper often wins. A smaller model often scores the same on simple tasks at a fraction of the cost. Re-test when models update. The landscape shifts every few months. Write it down. Your eval spreadsheet becomes more valuable every time you reuse it.

> NOTE: The best model is the best for your tasks, not the best on a leaderboard. Your tasks are the test. Everything else is advertising.

## A worked example: picking a meeting notetaker

Three apps promise the same thing. You test all three on the same four meetings. You score accuracy of action items, speaker names, summary quality, and privacy fit. App A gets the names right but misses half the actions. App B gets the actions right but stores audio on its servers, which your company forbids. App C is slightly worse on summaries but keeps everything in your cloud and costs half as much. The leaderboard would pick App A. Your eval picks App C. That is the point. The test that matters is yours, on your meetings, with your rules. A tool that fails your privacy rule fails the test, however good its summary is.

> NOTE: A deal-breaker is a deal-breaker. One failed must-have beats ten passed nice-to-haves.

## Check yourself

1. What is an eval, in plain words?
**Answer:** A planned test: give several AI models or tools the same real tasks, score the results fairly, and see which works best for you.

2. Why should you score answers blind?
**Answer:** So your hopes about which model is better do not bend your scores.

3. What are three biases of an AI judge?
**Answer:** Position bias (prefers the first answer), length bias (prefers longer answers), and self-preference (likes its own model's style).

4. Why are leaderboards only hints, not proof?
**Answer:** Test scores can be maxed out or leaked into training data, and boards move weekly as new models ship.

5. What should you track when you change your own AI system?
**Answer:** Re-run your eval set and compare accuracy, "I don't know" handling, cost, and speed before and after.

## In short

- The best model is the best for your tasks. Build a test set of ten to twenty tasks.
- Score with checks, clear rubrics, side-by-side comparisons, or a checked AI judge.
- Leaderboards show the top group. Your eval picks your winner.
- For your own systems, re-run evals after every change and include edge cases.
- Test enough times, and do not forget cost and speed.
