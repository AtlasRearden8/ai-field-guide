# 6.1 The MCP recipe book: 44 multi-tool combos
<!-- original: ch. 44 -->

One MCP server is useful. Two or three together are magic. **MCP** is a standard plug that lets AI use your tools. A combo joins several tools into one job, so the AI can read from one place, think, and act in another.

Each recipe below lists what it does, what you need, and how to set it up. Pick one that matches a job you do every week. Connect the ingredients. Paste the prompt. Review the result before anything is sent.

## For builders

1. **The Bug Detective.** It finds your most frequent error, traces it to the code, and drafts a fix. You need Sentry, your code host, and a coding agent. Connect all three, then ask for the most frequent unresolved error this week, the code responsible, the root cause, a fix with a test, and a draft pull request that links the error.
2. **The Visual QA Robot.** It clicks through your app and lists what is broken. You need Playwright or Chrome DevTools and a coding agent. Ask it to open your local app, click through signup, dashboard, and settings, screenshot each page at mobile and desktop sizes, and list anything broken, misaligned, or slow.
3. **Docs-Accurate Coding.** It stops the AI from using outdated APIs. You need Context7 and a coding agent. Ask it to pull the latest docs for your library, then refactor your code to the current recommended API, citing which doc sections it used.
4. **Design-to-Code.** It turns a Figma frame into real code. You need the Figma MCP server and a coding agent. Select a frame and ask for a React component that uses your existing design tokens and components, matches spacing exactly, and flags anything missing from your component library.
5. **The Database Whisperer.** It answers questions about your data in plain words. You need a read-only database connection, such as Supabase or Postgres, and a chart-capable client. Ask which signup source produced users with the highest 30-day retention, and ask it to show the SQL and make a chart.
6. **The Incident Commander.** It summarises what changed before an outage. You need Datadog or Grafana, your code host, and Slack. Ask for deploys, config changes, and error trends from the hour before the latency spike, plus a draft incident summary for your channel that you approve before posting.
7. **The Onboarding Guide.** It writes a guide for a new teammate. You need DeepWiki or your repo, and Notion. Ask it to explain the codebase architecture, the main modules, the data flow, and how to run tests, then save it as a Notion onboarding page with a diagram.
8. **The Dependency Gardener.** It keeps your libraries up to date safely. You need your code host, Context7, and a coding agent. Ask it to list outdated dependencies, check each changelog for breaking changes, upgrade the safe ones on a branch with tests passing, and summarise the risky ones for you.

## For productivity

9. **Monday Morning Briefing.** It prepares your whole week in one message. You need Gmail, Google Calendar, Slack, and Linear or Asana. Ask for this week's meetings with prep notes, unanswered emails older than two days, Slack threads where you are mentioned, and your top tasks.
10. **The Inbox Triage.** It sorts your email into actions. You need Gmail and your task tool. Ask it to read today's inbox, sort messages into reply, task, read later, and archive, draft replies for the first group, and create tasks for the second.
11. **Meeting Notes to Tasks.** It turns a meeting into owned work. You need your calendar, a transcript or notes file, and Notion or Linear. Ask it to read the notes, list decisions, create one task per action with an owner and a due date, and post the summary to your team channel.
12. **The Calendar Guard.** It finds clashes and fixes your day. You need Google Calendar and Gmail. Ask it to find double bookings, back-to-back meetings with no break, and meetings with no agenda, then propose fixes and draft the reschedule emails for your approval.
13. **The Travel Pack.** It builds a trip file from your bookings. You need Gmail, Google Calendar, and Notion. Ask it to find all bookings for your trip, build a Notion page with flights, hotels, and times, and add a packing checklist based on the weather.
14. **The Expense Catcher.** It turns receipts into a clean list. You need Gmail or Drive, and a spreadsheet. Ask it to find receipts from the last month, pull out the vendor, date, and amount, and add them to a spreadsheet with a monthly total.
15. **The Focus Planner.** It plans your day around your energy. You need your calendar and your task list. Ask it to look at today's tasks and meetings, block deep work in your free morning hours, and move low-priority tasks to tomorrow.
16. **The Follow-Up Machine.** It finds people you owe a reply to. You need Gmail and Slack. Ask it to list everyone who wrote to you more than three days ago without a reply, draft a short follow-up for each, and let you approve them one by one.

## For research and learning

17. **The Literature Review.** It reads papers and summarises the field. You need a web search tool, a file reader, and a notes app. Ask it to find the five most cited papers on your topic, read them, and write a two-page summary with the key findings and open questions.
18. **The Fact Checker.** It checks claims against sources. You need web search and a document reader. Paste a draft and ask it to check each factual claim against live sources, flag anything it cannot verify, and suggest a fix for each one.
19. **The Study Podcast.** It turns your notes into audio. You need your notes files and Gemini Notebook or a voice tool. Ask it to turn your notes into a two-host audio overview, then listen to it on your walk.
20. **The Concept Explainer.** It teaches you anything in plain words. You need web search and your notes. Ask it to explain a hard concept with three examples, then quiz you with five questions and explain any answer you get wrong.
21. **The Source Collector.** It builds a reading list with summaries. You need web search, a bookmark tool, and Notion. Ask it to find the ten best articles on your topic, write a one-paragraph summary of each, and save them to a Notion reading list.
22. **The Comparison Table.** It compares options side by side. You need web search and a spreadsheet. Ask it to compare three tools by price, features, and limits, and put the result in a table with a recommendation and the reasons.
23. **The Interview Prep.** It prepares you for a job interview. You need the job description, your CV, and web search. Ask it to find likely questions, draft answers from your experience, and run a mock interview with feedback after each answer.

## For life

24. **The Meal Planner.** It plans a week of meals from your fridge. You need a photo of your fridge and a notes app. Ask it to list what you have, plan five dinners that use it up, write a shopping list for the missing items, and save the plan to Notion.
25. **The Budget Watcher.** It shows where your money went. You need your bank export or a finance tool, and a spreadsheet. Ask it to categorise last month's spending, show the top five categories, and flag any subscriptions you have not used in three months.
26. **The Health Log.** It turns scattered notes into a health summary. You need your health app and a notes file. Ask it to summarise your sleep, steps, and workouts for the last four weeks, note any patterns, and suggest one small change to try.
27. **The Gift Finder.** It finds a gift for someone you love. You need your notes about them and web search. Describe the person, their interests, and your budget, and ask for five gift ideas with links, prices, and why each one fits.
28. **The Home Fixer.** It turns a problem into a plan. You need a photo of the problem and web search. Show the photo, ask what is likely wrong, what tools you need, and the steps to fix it, with a warning if it is a job for a professional.
29. **The Event Planner.** It plans a party from start to finish. You need your calendar, your contacts, and a notes app. Give it the date, the guest count, and the budget, and ask for a plan with a timeline, a shopping list, and invitations to send.
30. **The Memory Keeper.** It turns photos into a family story. You need your photos and a notes app. Pick ten photos, ask it to order them into a story, write a caption for each, and save the result as a page you can print.

## For creators

31. **The Content Repurposer.** It turns one idea into five formats. You need your notes and a publishing tool. Give it a blog draft and ask for a social post, a short video script, a newsletter section, and five headlines, all in the same voice.
32. **The Thumbnail Tester.** It makes and ranks thumbnails. You need an image tool and a video platform. Ask it to generate three thumbnail options for your video, rank them by clarity and curiosity, and explain the ranking.
33. **The Podcast Producer.** It turns a recording into a finished episode. You need your audio file, a transcript tool, and a publishing tool. Ask it to transcribe the episode, write show notes with timestamps, pull five quotable moments, and draft the episode description.
34. **The Brand Voice Checker.** It checks your writing against your brand. You need your brand guide and your draft. Ask it to read the draft, flag any sentence that breaks the brand voice, and rewrite those sentences to match.
35. **The Newsletter Curator.** It picks the best links of the week. You need your feeds and an email tool. Ask it to read your saved links, pick the five most interesting ones, write a short note on why each matters, and draft the newsletter for your approval.

## For business

36. **The Lead Scorer.** It scores new leads automatically. You need your form tool, web search, and your CRM. Ask it to look up each new lead's company, score it from one to ten, write a one-line reason, and save the score to your CRM.
37. **The Customer Reply Draft.** It drafts replies to support messages. You need your inbox, your help docs, and your CRM. Ask it to read a support message, find the answer in your docs, draft a friendly reply, and save it for your approval before sending.
38. **The Invoice Chaser.** It finds unpaid invoices politely. You need your accounting tool and email. Ask it to list invoices overdue by more than seven days, draft a polite reminder for each, and let you approve them before sending.
39. **The Competitor Watcher.** It tracks what rivals are doing. You need web search and a notes app. Ask it to check three competitor sites each week, note any price or feature changes, and write a short summary to your notes.
40. **The Sales Brief.** It prepares you for a sales call. You need your CRM, web search, and your calendar. Ask it to research the prospect, list their likely needs, suggest three questions to ask, and write a one-page brief before the call.

## Meta-recipes

41. **The Automation Maker.** It builds an automation from a complaint. You need your chat assistant and n8n or Make. Describe a repetitive job in plain words, and ask it to design the workflow, list the nodes, and write the setup steps for you to follow.
42. **The Agent Team.** It splits a big job across agents. You need your coding agent and a task tool. Describe a big project, ask it to split the work into roles, assign each role to a subagent, and track the results in a shared task list.
43. **The Daily Digest.** It combines many recipes into one morning message. You need your calendar, inbox, tasks, and chat tools. Ask it to combine the Monday briefing, the inbox triage, and the calendar guard into one short digest, sent to you each morning at 7am.
44. **The Self-Improving System.** It reviews your automations and improves them. You need your automation logs and your notes. Ask it to read last week's automation logs, find the most common failure, suggest a fix, and draft the change for your approval.

## Seasoning tips

A recipe is a starting point, not a rule. These tips make any recipe better.

- **Review before anything is sent.** No recipe should send email, post a message, or move money without your approval, at least for the first month.
- **Test on real samples.** A recipe that works on a test email may fail on a real one. Test with five real examples before you trust it.
- **Ask for JSON.** When a recipe returns data, ask for JSON with named fields. **JSON** is a simple data format with named fields. It is easier to check and store than free text.
- **Log every run.** Write each run to a log for the first week. When something breaks, the log tells you what happened.
- **Start with one recipe.** Pick the one that fixes your biggest weekly annoyance. Build it. Live with it. Then add the next.

> NOTE: A combo is only as safe as its most powerful tool. Before you connect a tool that can send, delete, or pay, check what it can do. Give it the least access it needs. Add an approval step before anything leaves your system.

> TRY IT: Pick recipe 9, the Monday Morning Briefing. Connect Gmail, your calendar, and your task tool. Run it once on a Monday. Read the briefing. Keep the parts you like. Drop the rest. You have just run your first multi-tool combo.

## Check yourself

- **Q1:** What is the first step in using any recipe in this chapter?
**Answer:** Find the recipe that matches your goal, connect the listed servers, then paste the prompt and review the result before anything is sent.

- **Q2:** Why should a recipe never send email without your approval at first?
**Answer:** Because a mistake in a connected tool can send the wrong message to the wrong person, and approval catches it first.

- **Q3:** What does it mean to ask for JSON output?
**Answer:** It means asking for a simple data format with named fields, which is easier to check and store than free text.

## In short

- One MCP server is useful; two or three together do a whole job.
- Every recipe lists what it does, what you need, and how to set it up.
- Start with one recipe that fixes a real weekly annoyance.
- Test on real samples, ask for JSON, and add approvals before anything is sent.
- Log every run for the first week, then relax and enjoy the time you got back.
