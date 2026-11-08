# 3.9 Notion for builders: databases, data sources, and the API
<!-- original: ch. 121 -->

Notion is more than notes. Under the surface, it is a database you can build on. A database is a table where each row is a page and each column is a property. Once you see Notion that way, you can build real tools with it. This chapter is for builders. It explains the data model, the property types, and the API. The API is the door that lets other tools talk to Notion.

You do not need to be a programmer to read this chapter. You need curiosity and one Notion workspace to try things in. Everything here is explained in plain words first. The technical terms come second.

## The Notion data model

Notion has three building blocks. Pages, blocks, and databases. A page is a document. It can hold text, images, and other pages. A block is one piece of a page. A paragraph is a block. A heading is a block. A checklist item is a block. A database is a collection of pages shown as a table, a board, or a calendar.

Each database has properties. A property is a column with a type. The type decides what the column holds and what automations can do with it. Here are the types you will meet most.

A title is the name of the row. Every database has one. Text holds short words. Number holds figures you can add up. Select holds one label from a list. Multi-select holds several labels. Date holds a day, with an optional time. Checkbox is a simple yes or no. Person links to a member of your workspace. Relation links one database to another. Rollup pulls a value from a linked database. Formula computes a value from other properties. Files hold attachments. Status tracks stages like "to do" and "done".

Relations are the most powerful idea here. A relation links a task to a project. Or an order to a customer. Once two databases are linked, you can see the connection from both sides. A project page shows all its tasks. A task page shows its project. Rollups then add up numbers across the link. How many tasks are done? What is the total cost? The database answers for you.

> NOTE: Notion's features change often. Property types, limits, and plan details move. Check the current Notion help pages before you build something that depends on a specific feature.

## Property types, and how automations see them

Automations see your database differently than you do. You see a nice table. An automation sees field names and values. A few habits make automations reliable.

Name properties clearly. "Due date" is good. "Date 1" is not. An automation that reads "Date 1" will break the day someone renames it. Use short names with no special characters.

Use select and status instead of free text where you can. Free text is flexible. It is also messy. One person writes "done". Another writes "Done!". An automation sees two different values. A select list forces one spelling.

Use dates properly. A date property holds a real date. A text property that says "next Friday" does not. Automations can compare real dates. They cannot parse your handwriting.

Keep a unique ID for important rows. Notion gives every page an ID. An ID is a long string of letters and numbers that names one thing and nothing else. You will need IDs when you use the API. You can find a page ID in its link. The long string after the title in the web address is the ID. Copy it carefully.

## API essentials

The API is the way programs talk to Notion. API stands for Application Programming Interface. Think of it as a menu. A program orders from the menu. Notion serves the dish. The program can read pages, create pages, update properties, and search the workspace.

To use the API, you need an integration. An integration is a small app you create in Notion's settings. It gets a secret token. A token is a long password for programs. Keep it secret. Never paste it into a shared page or a public file.

Give the integration access to only the pages it needs. Share a database with the integration the same way you share it with a person. If the integration cannot see a page, it cannot read it. That is a feature. It limits damage if the token leaks.

The API has limits. It allows only so many requests per second. A request is one question to the API. If you send too many too fast, Notion will slow you down. This is called rate limiting. Design your tools to wait and retry. Never hammer the API in a tight loop.

Common API moves are simple. Search for a page by title. Read a database's rows. Create a new page in a database. Update a property on a row. Add a block to a page. Each move is one call. A workflow chains several calls together.

> TRY IT: Create a test integration in Notion's settings. Share one small test database with it. Use a free API testing tool or a short script to list the rows. Then change one property through the API and watch it change in Notion. That round trip proves the door works.

## Designing databases for automation

A database built for humans and a database built for automations look different. Build for both from the start.

Add a status property to every workflow database. Statuses like "new", "processing", and "done" tell automations what to do next. An automation picks up rows marked "new". It works on them. It marks them "done". The status is the conveyor belt.

Add a "last processed" date property. It records when an automation last touched the row. If the date is old, something broke. If it is missing, the row was never processed. This one property saves hours of debugging.

Add an error log. A simple text property called "error" holds the last problem. When an automation fails, it writes the reason there. You can see failures in the table without opening any logs.

Keep formulas simple. A formula that calls five other formulas is hard to debug. Break it into steps. Use one formula per step. Name each step clearly.

Design for the API's limits. Reading a whole database with thousands of rows is slow. Filter first. Ask the API for only the rows you need. Ask for rows where the status is "new", not every row ever made.

## Notion's own automation tools

You do not always need outside tools. Notion has its own automations. They are simple. They are built in. They cover many jobs.

Notion automations run on triggers. A trigger is an event that starts the automation. Common triggers are "a page is added", "a property changes", or "a date arrives". When the trigger fires, the automation does its actions. Actions include editing a property, adding a page, or sending a message to Slack.

Buttons are another built-in tool. A button is a clickable control on a page. Click it, and it runs a set of actions. A button can add a task, update a status, or open a form. Buttons are perfect for repeated jobs. "Add weekly review" is a button. "Mark all as done" is a button.

Notion also has integration webhooks. A webhook is a message one app sends to another when something happens. Notion can send a webhook when a page changes. An outside tool listens for it and acts. This is how Notion tells n8n that something happened, without n8n asking every minute.

## Check yourself

1. What are Notion's three building blocks?
**Answer:** Pages, blocks, and databases, where a page holds blocks and a database is a collection of pages shown as a table or board.

2. What is a relation, and why is it powerful?
**Answer:** A link between two databases, so a project page can show all its tasks and rollups can add up values across the link.

3. What is an API token, and how should you treat it?
**Answer:** A long secret password that lets a program talk to Notion, which you must keep private and never paste into a shared page.

4. Why add a status property to a workflow database?
**Answer:** Because statuses like "new", "processing", and "done" tell automations which rows to pick up and what to do next.

5. What is a trigger in Notion automations?
**Answer:** An event that starts an automation, such as a page being added, a property changing, or a date arriving.

## In short

- Notion is a database: pages as rows, properties as columns, relations as links.
- Relations and rollups turn separate tables into one connected system.
- The API lets programs read and write Notion through an integration with a secret token.
- Name properties clearly, use select lists, and use real dates for automations.
- Status, last-processed, and error properties make automations reliable.
- Built-in automations, buttons, and webhooks cover many jobs without outside tools.
