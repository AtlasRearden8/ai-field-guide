# 2.28 Spreadsheet superpowers
<!-- original: ch. 58 -->

Spreadsheets are where AI quietly delivers some of its biggest everyday wins. It writes and explains formulas. It cleans messy data. It classifies hundreds of rows with a single function. It builds charts. It finds the story in your numbers. This chapter turns you into the spreadsheet wizard of your group, with no formula memorisation needed.

Spreadsheets are structured, repetitive, and full of fuzzy text. Rows and columns. The same job for every row. Messy comments, descriptions, and addresses. That is the exact shape of work AI excels at. And the grid shows every result, so it is easy to spot-check.

## Formula help: write, explain, fix

Describe what you need in plain language. Get a working formula with an explanation. Ask where? Gemini in Sheets, Copilot in Excel, or any assistant with a few sample rows pasted in.

| You say… | AI gives you… |
|---|---|
| "Sum column C where column A is 'Paid' and the date is this month." | A SUMIFS formula with the right date logic |
| "Look up each email in Sheet2 and return the plan name." | An XLOOKUP with error handling |
| "Explain this formula step by step in plain English." | A step-by-step breakdown of a scary nested formula |
| "Why does this return an error?" | The likely cause, like extra spaces or text versus number, plus a fix |
| "Extract the domain from these emails." | A text-extraction formula |

**XLOOKUP** is Excel's modern lookup function: give it a value, tell it where to look, and it returns the match. **SUMIFS** adds up numbers that meet several conditions at once. You do not need to memorise them. You need to know they exist, and that AI can write them for you.

> TRY IT: Open a sheet you use. Ask your assistant: "Explain this formula in plain English." Then ask: "Write a formula that sums sales where the region is North and the month is June." Paste it in and test it.

## AI functions in cells

The magic trick is AI functions. These run one AI prompt per cell, across hundreds of rows.

| Tool | Function | Example |
|---|---|---|
| Google Sheets | =AI(prompt, range) | Classify a review as positive, neutral, or negative |
| Excel (Microsoft 365 Copilot) | COPILOT(prompt, range) | Summarise feedback in five words |
| Airtable | AI fields | An AI field that auto-tags each new record |

Take 500 survey responses. Add AI columns for sentiment, theme, and a one-line summary. Then build a pivot table by theme. A **pivot table** is a summary that groups and totals your data. Qualitative mush becomes a clear chart in ten minutes.

But AI cells are not ordinary formulas. They can give slightly different answers on recalculation. They have usage limits. They send cell contents to the AI service. Freeze results once you are happy: copy, then paste values. Do not feed them sensitive data unless your plan allows it.

> NOTE: Always write AI output to a new column. Keep the original. Undo is your friend, and originals are your safety net.

## Cleaning messy data

Messy data is the most common spreadsheet pain. AI is superb at cleaning it. The trick is to ask for proposed changes before applying them.

| Mess | Prompt |
|---|---|
| Inconsistent names: "Acme Inc", "ACME", "acme corp." | "Standardise company names in column A, and show me a mapping table first." |
| Mixed date formats | "Convert column C to standard dates. Flag anything ambiguous." |
| Full names in one cell | "Split into first and last name. Handle middle names and tricky surnames." |
| Duplicates with small differences | "Find likely duplicate contacts and propose merges." |
| Free-text categories | "Map these 300 free-text job titles into eight standard categories." |

A **mapping table** shows old value next to new value, so you can review every change before it happens. Ask for one every time. Keep the original column. Check a sample by hand.

## Analysis and charts

In-app AI can answer questions, build pivot tables, and suggest charts. Or upload the sheet to an assistant with code execution, like Claude, ChatGPT, or Gemini. Say: "Clean this, find the top three insights, and make a chart for each." Behind the scenes, it writes and runs Python code. That is the same skill as chapter 5.12's data analysis, in miniature.

Always ask two questions: "Show me the calculation" and "What assumptions did you make?" That is how you catch mistakes. AI is great at arithmetic when it runs code. It is less reliable when it does maths in its head. Verify one number by hand or with a pivot table. Prefer real formulas for arithmetic.

**Python in Excel** lets you run Python code inside cells, and Copilot can write the Python for you. **Google Apps Script** automates Sheets and can call AI services on schedules. **Office Scripts** and VBA are small programs that automate tasks. AI is excellent at writing and explaining them: "Write a script that formats this table and highlights overdue rows."

## Spreadsheets as AI databases

Spreadsheets double as simple infrastructure for your automations.

- **Logs.** Every automation run appends a row. Fixing problems and tracking stats gets easy.
- **Config.** A "settings" sheet with keywords, targets, and recipients that non-technical teammates can edit.
- **Memory.** A simple table of facts or preferences that an agent reads and updates.
- **Mini CRM.** Contacts plus AI columns for "next best action." A **CRM** is a customer-relationship tracker.

Google Sheets, Excel Online, and Airtable all have great connections in n8n, Zapier, and Make. A sheet is often the simplest database you will ever need.

## Ten spreadsheet projects to try

| # | Project | AI does |
|---|---|---|
| 1 | Survey analyser | Sentiment, themes, and summaries per response |
| 2 | Expense categoriser | Categories from bank descriptions |
| 3 | Receipt log | Extracts vendor, amount, and date from photos |
| 4 | Lead scorer | Fit score and reason from company info |
| 5 | Translation table | Product descriptions in five languages |
| 6 | Reading list | Summary and "worth reading?" score from links |
| 7 | Inventory tagger | Categories and attributes from product names |
| 8 | Content calendar | Post ideas and captions per row |
| 9 | Gradebook helper | Draft comments from scores and notes; teacher reviews each one |
| 10 | Home maintenance tracker | Due dates and plain-English instructions per task |

## Pitfalls to avoid

| Pitfall | Fix |
|---|---|
| Trusting AI maths blindly | Verify one number by hand, and prefer real formulas for arithmetic |
| Results change on recalculation | Copy and paste values once final |
| Hitting usage limits on AI functions | Process in batches, and only rows that need it |
| Sensitive data in AI cells | Check your plan's data policy, and anonymise first |
| Overwriting originals | Always write AI output to a new column |

> TRY IT: Export any list you have: reviews, expenses, contacts, even a playlist. Add one AI column with a fun question, like "what mood is this song?" Then make a chart of the results. Spreadsheets have never been this fun.

## Asking for charts that tell the truth

A chart can lie without meaning to. A bar chart that starts at 90 instead of zero makes a small gap look huge. A pie chart with twelve slices is unreadable. A line chart with no labels is decoration. When you ask AI for a chart, say what story you want told. "Show monthly sales as bars, starting at zero, with values labelled." Then look at the chart like a sceptic. Does the scale start at zero? Are the labels clear? Does the title say what the chart shows? A good chart answers one question at a glance. If you need a paragraph to explain it, the chart has failed. Ask for a simpler one.

> NOTE: The best chart is the simplest one that answers your question. If a table would do, use a table.

## Check yourself

1. Why should you freeze AI cell results with copy and paste values?
**Answer:** AI functions can recalculate with slightly different results, so freezing locks in the version you checked.

2. What is a mapping table, and why ask for one?
**Answer:** A table showing old values next to new values, so you can review every change before it is applied.

3. What two questions should you always ask about AI analysis?
**Answer:** "Show me the calculation" and "What assumptions did you make?"

4. What is a pivot table?
**Answer:** A summary that groups and totals your data, such as survey responses grouped by theme.

5. Why write AI output to a new column instead of overwriting?
**Answer:** So you keep the original data as a safety net, and you can compare before and after.

## In short

- AI writes, explains, and fixes formulas from plain English.
- AI functions classify and summarise across hundreds of rows at once.
- AI is a superb data cleaner. Ask for proposed changes first and keep originals.
- For analysis, ask for the calculation and assumptions, and check a number yourself.
- Spreadsheets double as logs, config, and memory for automations.
- Freeze final results, and never feed sensitive data to AI cells without checking your plan.
