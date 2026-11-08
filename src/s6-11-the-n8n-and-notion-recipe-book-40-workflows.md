# 6.11 The n8n and Notion recipe book: 40 workflows
<!-- original: ch. 126 -->

Forty proven workflows that combine n8n and Notion. Each one lists the trigger, the steps, and what you end up with in Notion, plus a difficulty rating.

Difficulty is Easy (under 30 minutes), Medium (about an hour), or Advanced (an afternoon). "AI" means any model node: Claude, GPT, Gemini, or a local model through Ollama.

**How to read a recipe.** Trigger is what starts it. Steps are what happens. Notion result is what you see when it finishes. Recipes marked with a star need a paid Notion plan for button or automation webhooks. Each one can also use a checkbox plus the Notion Trigger instead.

## Capture

1. **Voice capture. Easy.** Trigger: a phone shortcut sends a voice note to a webhook. Steps: transcribe it, ask AI for a title, type, and priority, then create a row. Notion result: an Inbox row with the note, title, and priority.
2. **Email to Inbox. Easy.** Trigger: you label an email "To Notion." Steps: read the email, ask AI for a summary and a due date, then create a row. Notion result: an Inbox row with the summary and a link to the email.
3. **Chat capture. Easy.** Trigger: you send a message to your Telegram bot. Steps: read the message, ask AI for a title and type, then create a row. Notion result: an Inbox row, ready to triage.
4. **Form intake. Medium.** Trigger: a form is submitted. Steps: read the answers, look up the company, ask AI to score the lead, then create a row and notify Slack. Notion result: a Leads row with a score, a summary, and an owner.
5. **Web clipper. Easy.** Trigger: you save a link. Steps: fetch the page, ask AI for a summary and tags, then create a page. Notion result: a Reading page with a summary, tags, and the original link.
6. **Meeting notes. Medium.** Trigger: a meeting ends. Steps: read the transcript, list decisions and actions, then create one task per action. Notion result: Tasks rows with owners and due dates, plus a meeting summary page.
7. **Book highlights. Easy.** Trigger: highlights sync from Readwise or a Kindle file. Steps: group highlights by book, ask AI for key ideas, then create one page per book. Notion result: a Books page per book with highlights and ideas.

## Organise and enrich

8. **AI triage. Medium.** Trigger: a new row appears in Inbox. Steps: ask AI to pick the right project, add tags, and set a priority, then update the row. Notion result: the Inbox row sorted, tagged, and prioritised.
9. **Summarise this page. Easy, star.** Trigger: you click a "Summarise" button on a page. Steps: read the page as Markdown, ask AI for a summary, then write it to the page. Notion result: a summary section at the top of the page.
10. **Make subtasks. Easy, star.** Trigger: you click a "Make subtasks" button on a task. Steps: ask AI to break the task into steps, then create one row per step. Notion result: subtask rows linked to the parent task.
11. **Research this company. Medium, star.** Trigger: you click a "Research" button on a lead. Steps: search the web, ask AI for a company profile, then write it to the page. Notion result: a profile with size, products, and recent news.
12. **Translate page. Medium, star.** Trigger: you click a "Translate" button. Steps: read the page as Markdown, ask AI to translate it, then append the translation or create a linked page. Notion result: a translated section or a linked translated page.
13. **Tag cleanup. Easy.** Trigger: every Sunday. Steps: find rows with missing or odd tags, ask AI to suggest fixes, then update the rows. Notion result: a tidy database with consistent tags.
14. **Duplicate finder. Medium.** Trigger: every week. Steps: find rows with the same title or the same External ID, ask AI if they are true duplicates, then flag them for review. Notion result: duplicate rows flagged, never auto-deleted.

## Plan and review

15. **Daily briefing. Medium.** Trigger: every weekday at 7am. Steps: read today's tasks and calendar, ask AI to write a briefing, then create a page. Notion result: a Daily Briefing page with today's plan.
16. **Weekly review. Medium.** Trigger: every Friday at 4pm. Steps: read completed tasks, journal entries, and metrics, ask AI to write a review, then create a page. Notion result: a Weekly Review page with wins, lessons, and next week's focus.
17. **Monthly report. Medium.** Trigger: the first of the month. Steps: read the month's tasks, sales, and notes, ask AI for a report, then create a page. Notion result: a Monthly Report page with numbers and observations.
18. **Goal tracker. Easy.** Trigger: every Sunday. Steps: read progress on each goal, calculate the percentage done, then update the goal rows. Notion result: goal rows with fresh progress and a status.
19. **Habit summary. Easy.** Trigger: every Sunday. Steps: read the week's habit checks, count streaks, then write a summary. Notion result: a habit summary page with streaks and one suggestion.
20. **Time blocking. Medium.** Trigger: every evening at 6pm. Steps: read tomorrow's tasks, ask AI to propose time blocks, create calendar events, then save the event IDs. Notion result: tasks with Scheduled times and External IDs.

## Work and business

21. **New customer onboarding. Advanced.** Trigger: a payment arrives in Stripe. Steps: create a customer row, create onboarding tasks, send a welcome message, then notify the team. Notion result: a customer row and a set of onboarding tasks.
22. **Deal won. Medium.** Trigger: a deal is marked Won in your CRM. Steps: create the project, assign the owner, create starter tasks, then notify Slack. Notion result: a project row with tasks and an owner.
23. **Invoice reminder. Medium.** Trigger: an invoice is seven days overdue. Steps: find the invoice, draft a polite reminder, wait for your approval, then send it. Notion result: the invoice row marked as reminded, with the sent date.
24. **Support triage. Advanced.** Trigger: a support message arrives. Steps: classify it by urgency and topic, draft a reply from your help docs, then create a ticket row. Notion result: a ticket row with a draft reply, awaiting your approval.
25. **Job application tracker. Easy.** Trigger: you apply for a job. Steps: save the role, company, and date, then set a follow-up reminder for seven days. Notion result: an Applications row with a follow-up date.
26. **Timesheet draft. Medium.** Trigger: every Friday at 5pm. Steps: read your calendar events, group them by project, then draft a timesheet page. Notion result: a timesheet page ready for your review.
27. **Expense log. Easy.** Trigger: a receipt photo arrives. Steps: read the photo, pull out the vendor, date, and amount, then create a row. Notion result: an Expenses row with the amount and a link to the receipt.

## Content and learning

28. **Content pipeline. Medium.** Trigger: a post's Status changes to Drafting. Steps: ask AI to write a first draft, save it to the page, then move Status to Review. Notion result: a draft on the page, ready for review.
29. **Publish to blog. Medium, star.** Trigger: a post's Status changes to Ready. Steps: read the page as Markdown, publish it through your blog platform's API, then save the live URL. Notion result: the page with its live URL and Published status.
30. **Newsletter draft. Medium.** Trigger: every Sunday at 6pm. Steps: read the week's notes and saved links, ask AI to pick the best five and write notes, then draft the issue. Notion result: a newsletter draft page, ready for your review.
31. **Social scheduler. Medium.** Trigger: a post is marked Ready. Steps: format it for each platform, schedule it, then log the link when it goes live. Notion result: a post row with scheduled times and live links.
32. **Flashcards from notes. Easy, star.** Trigger: you click a button on a study page. Steps: ask AI to write question-and-answer pairs, then create rows. Notion result: Flashcards rows linked to the study page.
33. **Reading summary. Easy.** Trigger: you finish a book. Steps: read your highlights, ask AI for a summary and three takeaways, then update the book page. Notion result: a book page with a summary and takeaways.
34. **Idea to outline. Easy, star.** Trigger: you click a button on an idea. Steps: ask AI for an outline with three angles, then save it to the page. Notion result: an outline on the idea page.

## Builders and system maintenance

35. **Issue-tracker sync. Medium.** Trigger: an issue changes on your code host. Steps: upsert the issue by its number into your Roadmap, then update its status. Notion result: Roadmap rows that match your code host.
36. **Release notes. Medium.** Trigger: a new release is published. Steps: ask AI to summarise the merged changes, then create a Changelog page. Notion result: a Changelog page with the release summary.
37. **Error logger. Easy.** Trigger: the Error Trigger fires on any workflow. Steps: write a row with the workflow name, time, and error message, then alert you. Notion result: an Automation Log row for every failure.
38. **Workflow inventory. Medium.** Trigger: every week. Steps: list all workflows from the n8n API, update your Automations database with status and last run, then flag any that have not run. Notion result: an Automations database that shows the health of your system.
39. **Notion backup. Easy.** Trigger: every week. Steps: export key databases to CSV and Markdown, copy them to cloud storage, then log the backup. Notion result: a Backups log row with the date and the file links.
40. **RAG sync. Advanced.** Trigger: a page is updated in Notion. Steps: read the page as Markdown, split it into chunks, create embeddings, then store them in your vector store. Notion result: a search index that stays fresh as you write.

## How to build any recipe

Build one recipe at a time with this six-step method.

- **Step 1: Prepare the database.** Create the Notion database with the properties the recipe needs. Share it with your integration.
- **Step 2: Build the trigger.** Start with the event that starts the workflow. Test it with a real sample.
- **Step 3: Add the reads.** Add the Notion and app nodes that fetch the data. Test each one.
- **Step 4: Add the AI step.** Tell the model exactly which fields to return, as JSON. Test it on five real examples.
- **Step 5: Add the writes.** Write results back to Notion with a Status flow, such as Ready, Processing, Done or Error.
- **Step 6: Add the error path.** On failure, write to the Automation Log. Publish, and watch it for a week.

Use this recipe card for each build.

- Name: ____
- Trigger: ____
- Reads: ____
- AI step: ____
- Writes: ____
- Status flow: ____
- Approval? ____
- Error path: Automation Log

> NOTE: Build the error logger, recipe 37, first. It takes under 30 minutes. Every failure in every other workflow then becomes visible in Notion instead of going unnoticed. A system you cannot see is a system you cannot trust.

> TRY IT: Build recipe 37, the error logger, and recipe 1, voice capture, today. Together they take under an hour. You will have a capture system you can trust, and a log that catches every failure.

## Check yourself

- **Q1:** Which recipe should every n8n and Notion setup include first, and why?
**Answer:** The error logger, recipe 37, so every failure in every other workflow becomes visible in Notion instead of going unnoticed.

- **Q2:** A recipe needs a paid Notion plan for its status webhook. How could you build it on the free plan?
**Answer:** Use a Notion Trigger on Page Updated, or a scheduled Get Many that finds rows with the right Status that have not been processed yet, and mark them processed afterward.

- **Q3:** What is the first step in building any recipe?
**Answer:** Prepare the Notion database, with the right properties, and share it with your integration.

## In short

- Forty recipes cover capture, organising, planning, business, content, and maintenance.
- Every recipe follows trigger, steps, Notion result, with status and errors written back.
- Recipes marked with a star can also run with a checkbox and the Notion Trigger.
- Build the error logger first, then the recipe that saves you the most time.
- Build one recipe at a time with the six-step method, testing on real data.
