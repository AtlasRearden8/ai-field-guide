# 5.12 Data analysis for everyone
<!-- original: ch. 102 -->

Data analysis sounds scary. It sounds like maths, code, and charts. It is really just asking questions of information. How much did we spend? What sells best? When do people visit? AI lets anyone ask those questions in plain words. You do not need to be a data expert. You need a clear question and a tidy table.

A CSV is a simple file that holds a table. CSV stands for Comma-Separated Values. Each line is a row. Commas separate the columns. Spreadsheets can open CSV files. So can AI tools. Most data you meet will be a CSV or a spreadsheet. That is your starting point.

## The five levels

Data analysis has five levels. You can stop at any level. Each one answers harder questions.

Level one is chat with a spreadsheet. Upload a file to a chatbot. Ask questions in plain words. "What was our best month?" "Which product sells most?" The AI reads the file and answers. This is the fastest way to start. It works for files with a few thousand rows.

Level two is AI inside your spreadsheet. Tools like Excel and Google Sheets now have AI built in. You can ask for a formula in plain words. "Add up sales by month." The AI writes the formula. You check it. You can also ask it to explain a formula someone else wrote. This level keeps you in a tool you already know.

Level three is analysis notebooks with AI. A notebook is a document that mixes text, code, and charts. AI helps you write the code. You ask for a chart. It writes the steps. You run them. This level suits bigger files and repeat work. It needs a little learning. It pays off fast if you analyse data every week.

Level four is talking to databases with MCP. A database is a big store of tables. MCP is a standard plug that lets AI use your tools. With the right setup, you can ask an AI assistant a question and it queries the database for you. It writes the query. It runs it. It shows the answer. This level is for work teams with real databases. It needs care with permissions. Only let the AI read what it should read.

Level five is dashboards and data apps. A dashboard is a page of live charts that update themselves. AI can help you build one. You describe what you want to see. It builds the charts. You share the page with your team. This level turns a one-off answer into a tool everyone uses.

> NOTE: Never upload private data to a random AI tool. Customer lists, salaries, and health records are sensitive. Read the privacy terms. Use tools your work approves. Delete uploads you no longer need.

## Thinking clearly about data

Tools are the easy half. Thinking is the hard half. Here are the habits that keep you honest.

Start with the question. "What do I want to decide?" is the question behind every analysis. A clear decision makes a clear analysis. "Should we open on Sundays?" is a decision. "Tell me about sales" is not.

Check the data before you trust it. Are there missing rows? Are dates in the right format? Are there duplicates? Messy data gives wrong answers. Ask AI to clean it. Ask it to list problems it found. Fix the problems at the source if you can.

Watch for small numbers. Ten customers is not a trend. A hundred is a hint. A thousand is a pattern. AI will happily draw a chart from tiny data. You must ask whether the data is enough.

Beware of averages. An average can hide the truth. Average sales might look fine while half your products lose money. Ask for the spread. What is the best? What is the worst? What is the middle? Averages lie by hiding.

Correlation is not causation. Correlation means two things move together. Causation means one causes the other. Ice cream sales and sunburns rise together. Ice cream does not cause sunburns. Summer causes both. AI can spot correlations. Only you can judge causes.

> TRY IT: Find a small dataset to practise with. Public data works well: weather, sports results, or film ratings. Upload it to a chatbot. Ask five questions. Then check one answer by hand in the spreadsheet. That check teaches you how much to trust the tool.

## Fun datasets to practise with

Practice makes this stick. Here are safe datasets to try. Weather records for your city. How does rain change by month? Sports results for your team. Who scores most at home? Film ratings. Which genre scores highest? Your own spending, with names removed. Where does the money go? Your step count from your phone. Do you walk more on weekends?

Each one teaches the same loop. Ask a question. Get an answer. Check it. Ask a better question. After five datasets, the loop feels natural. After ten, you will use it at work without thinking.

Level three is analysis notebooks with AI. A notebook is a document that mixes text, code, and charts. AI helps you write the code. You ask for a chart. It writes the steps. You run them. This level suits bigger files and repeat work. It needs a little learning. It pays off fast if you analyse data every week.

Level four is talking to databases with MCP. A database is a big store of tables. MCP is a standard plug that lets AI use your tools. With the right setup, you can ask an AI assistant a question and it queries the database for you. It writes the query. It runs it. It shows the answer. This level is for work teams with real databases. It needs care with permissions. Only let the AI read what it should read. Never let it change data without a human check.

Level five is dashboards and data apps. A dashboard is a page of live charts that update themselves. AI can help you build one. You describe what you want to see. It builds the charts. You share the page with your team. This level turns a one-off answer into a tool everyone uses. Start at level one. Move up only when the lower level feels too small.

Thinking clearly matters more than tools. Start with the question. "What do I want to decide?" A clear decision makes a clear analysis. Check the data before you trust it. Are there missing rows? Duplicates? Wrong dates? Messy data gives wrong answers. Ask AI to list the problems it found. Fix them at the source if you can. Watch for small numbers. Ten customers is not a trend. A hundred is a hint. A thousand is a pattern. AI will happily draw a chart from tiny data. You must ask whether the data is enough.

Dashboards are the fifth level. A dashboard is a page of live charts that update themselves. AI can help you build one. You describe what you want to see. It builds the charts. You share the page with your team. This turns a one-off answer into a tool everyone uses. Start at level one. Move up only when the lower level feels too small.

## Try this week

- [ ] Upload a small spreadsheet or CSV and ask it five plain-words questions.
- [ ] Ask AI inside your spreadsheet to write one formula for you, and check it.
- [ ] Find one messy column in your data and ask AI to help clean it.
- [ ] Practise on one public dataset, and check one answer by hand.

## Check yourself

1. What is a CSV, in plain words?
**Answer:** A simple file that holds a table, where each line is a row and commas separate the columns.

2. What is level one of data analysis?
**Answer:** Chatting with a spreadsheet: uploading a file to a chatbot and asking questions in plain words.

3. Why start with the decision, not the data?
**Answer:** Because a clear decision makes a clear analysis, while a vague request gives vague answers.

4. Why beware of averages?
**Answer:** Because an average can hide the truth, like fine average sales while half the products lose money.

5. What does correlation is not causation mean?
**Answer:** That two things moving together does not prove one causes the other, as with ice cream sales and sunburns both rising in summer.

## In short

- Data analysis is asking questions of information in plain words.
- Five levels run from chatting with a spreadsheet to live dashboards.
- Start with the decision you need to make, then find the data for it.
- Clean messy data first, and beware of small numbers and averages.
- Correlation is not causation, so judge causes yourself.
- Try this week: five questions of a real file, one AI formula, one clean-up, and one practice dataset.
