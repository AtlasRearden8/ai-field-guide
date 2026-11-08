# 2.26 Google Workspace and Microsoft 365 AI
<!-- original: ch. 55 -->

Most of the world's work lives in Google Workspace or Microsoft 365. Both now have AI woven through every app. This chapter is your practical tour. The best feature in each app. Power workflows that save real hours. How to automate with Apps Script and Power Automate. And how to bring outside AI, like Claude or ChatGPT, into the mix.

Features depend on your plan. Look for the Gemini or Copilot icons in your apps. Business, education, and personal plans include different features. Admins can turn things on or off. Prices change often, so check the current price before you buy. As of November 2026, Gemini was included in Google Workspace Business plans with no separate AI fee. Microsoft 365 Copilot was a paid add-on on top of a Microsoft 365 plan.

## Google Workspace and Gemini, app by app

| App | What Gemini does | Try |
|---|---|---|
| Gmail | Summarise threads, draft and refine replies, smart search | "Summarise this thread and draft a reply that politely declines." |
| Docs | Draft, rewrite, summarise, generate from your files | "Draft a project brief using my Q3 notes and budget sheet." |
| Sheets | Build formulas and tables, analyse, per-cell AI prompts | Classify a column of feedback with one AI function |
| Slides | Generate slides and images from prompts or docs | "Make a six-slide deck from this doc." |
| Meet | Take notes, recaps, action items, translated captions | Turn on auto notes for recurring meetings |
| Drive | Summarise folders and files, answer questions across docs | "What is the status of the Aurora project across these files?" |
| Calendar | Scheduling help, Gemini in the side panel | "Find time with Priya next week for 30 minutes." |
| Vids | AI-assisted video creation from docs and prompts | "Turn this onboarding doc into a two-minute training video." |

The Gemini app itself adds more. **Gems** are custom assistants with standing instructions. A "Meeting prep Gem." An "Email tone checker Gem." A "Recipe scaler Gem." **Deep Research** runs multi-step research across the web and your files, and produces a long, cited report you can export to Docs. **Canvas** is a live document or code editor beside the chat. Connected apps let Gemini pull from Gmail, Drive, Calendar, Maps, and YouTube inside the chat. **Gemini Notebook** is grounded research on your chosen sources, with audio overviews. **Google AI Studio** is a free playground with API keys for building with Gemini models.

> NOTE: Ground the AI in specific files for much better answers. In Gemini, point at the file. In Copilot, use the slash to reference it. Vague questions get vague answers.

## Microsoft 365 and Copilot, app by app

| App | What Copilot does | Try |
|---|---|---|
| Outlook | Summaries, drafting, tone coaching, scheduling | "Summarise my unread emails from leadership." |
| Word | Drafting from files, rewriting, summarising, Q and A on long docs | "Draft a proposal based on this document and this email." |
| Excel | Formulas, analysis, charts, Python in Excel, insights | "Which region's sales dropped most? Chart it." |
| PowerPoint | Decks from prompts or Word docs, redesign, speaker notes | "Turn this Word report into a ten-slide deck." |
| Teams | Meeting recaps, "what did I miss," action items, chat summaries | Ask during a meeting: "What decisions have we made so far?" |
| Copilot Chat | Work-grounded chat across emails, files, and meetings | "Prep me for my 2 p.m. meeting." |

Beyond single apps, Microsoft offers agents. Microsoft 365 Copilot includes specialist agents for deep research and data analysis. **Copilot Studio** lets you build custom agents with your knowledge sources, connectors, actions, and MCP tools. A classic first agent is an HR policy Q and A bot grounded in SharePoint, Microsoft's shared document system. **SharePoint agents** are grounded in a specific site or document library. **Power Automate** builds cloud and desktop flows with over a thousand connectors, AI Builder, and Copilot-assisted flow building. For example: "When a file lands in this SharePoint folder, sum it up and post to Teams."

## Power workflows

The real wins come from combining apps. Here are workflows that save hours every week.

**Google workflow one: the morning brief.** Gemini in Gmail summarises overnight threads. Gemini in Calendar finds your gaps. Drive answers "what changed on the project?" One prompt in the Gemini app can pull all three together into a five-bullet morning brief.

**Google workflow two: the form digest.** New form responses land in a Sheet. A small Apps Script robot summarises the latest responses every morning and emails you the digest. Apps Script is free JavaScript that runs inside Google Workspace. You can ask Claude or Gemini to write the script for you. Store your API key in Script properties, never in the code. Add a time-driven trigger so it runs daily.

**Microsoft workflow one: the meeting machine.** Teams records and recaps the meeting. Copilot writes the action items. Power Automate posts them to the project channel and creates tasks. You review, not retype.

**Microsoft workflow two: the report pipeline.** Word drafts from your source files. Excel analyses the numbers. PowerPoint turns the report into a deck. Each step is one prompt. The human checks each step before the next begins.

> TRY IT: Pick one recurring task you do in Gmail or Outlook, or Docs or Word, every week. A status email. Meeting notes. A report. Do it with the built-in AI this week. If it saves ten minutes, automate it next week.

## Bringing outside AI in

Nothing stops you from mixing ecosystems. Claude has Google Drive, Gmail, and Calendar connectors, plus Microsoft 365 options. ChatGPT has Drive, Gmail, Calendar, and SharePoint connectors. Every Workspace and 365 app has rich nodes in n8n, Zapier, Make, and Power Automate. Mix and match. Use Claude to write while Gemini handles your Google-native tasks. Use ChatGPT for research while Copilot handles your Teams recaps.

Cross-platform tips: ground the AI in specific files for much better answers. Permissions equal visibility. AI only sees what you, or the agent, can access. Tidy sharing settings help. Name files clearly. "2026-Q3 Budget (FINAL)" beats "budget v7 new new." Check before sending. AI-drafted emails and slides deserve a human read, especially for outside audiences. Follow your organisation's rules on which AI tools may see which data.

> NOTE: Work data policies matter. If your company has an approved AI tool, use it. If it has no approved tool, say so. People use AI anyway, and safe choices beat secret ones.

## What to do when the AI is missing or wrong

Sometimes the Gemini or Copilot icon is missing. First, check your plan. Features vary by plan, and admins can turn things off. Ask your admin or check your account page. Sometimes the AI is present but wrong. It may draft from the wrong file. Ground it again: point at the exact file by name. It may invent a meeting that never happened. Ask it to quote its source. It may write in the wrong tone. Add one line to your instructions: "Write like this example." And sometimes the AI is simply the wrong tool for the job. A two-minute task does not need a ten-minute AI setup. Do it by hand. AI is a power tool. You do not use a power drill to hang a picture hook. Well, you could. But a hammer is faster.

> NOTE: When AI gets a fact wrong, check the source it used, not the answer it gave. The source is where the error lives.

## Check yourself

1. What is a Gem in Gemini?
**Answer:** A custom assistant with standing instructions, like a "Meeting prep Gem" or an "Email tone checker Gem."

2. What does Copilot Studio let you build?
**Answer:** Custom agents with your knowledge sources, connectors, actions, and MCP tools, such as an HR policy Q and A bot.

3. How do you get much better answers from Gemini or Copilot?
**Answer:** Ground the AI in specific files, instead of asking vague questions.

4. What is Apps Script?
**Answer:** Free JavaScript that runs inside Google Workspace, which you can use to build small robots like a daily form summary.

5. Why should you check an AI-drafted email before sending it?
**Answer:** AI can get names, dates, tone, and facts wrong, and an email to an outside audience is hard to undo.

## In short

- Gemini and Copilot are built into mail, docs, sheets, slides, and meetings.
- Gems, Deep Research, and Gemini Notebook go beyond quick chat on Google's side.
- Copilot agents, Copilot Studio, and Power Automate go beyond quick chat on Microsoft's side.
- Apps Script and Power Automate let you build low-cost robots inside each ecosystem.
- Ground AI in specific files, keep sharing tidy, and mix in outside AI where it is stronger.
