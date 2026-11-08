# 4.30 Connecting n8n to Notion
<!-- original: ch. 122 -->

This is the reference chapter you will keep open while building. It covers connecting n8n to Notion securely. It tours every operation the Notion node offers. It shows four ways to start a workflow from Notion. It covers mapping properties, filtering, and the raw API fallback. It ends with the patterns that separate fragile workflows from dependable ones.

Work through it once. Then use it as a handbook whenever you build.

## Step 1: set up the credential

A **credential** is a saved login that lets one tool talk to another. n8n connects to Notion through a credential that holds your integration secret. An **integration** is a small app identity inside Notion that you create for n8n.

Follow these steps.

1. **Create the integration.** Go to notion.so/profile/integrations. Click New integration. Give it a clear name, such as "n8n automations." Select your workspace and save it.
2. **Set the capabilities.** Keep read, update, and insert content turned on. Add comment capabilities only if you need them. Less access is safer.
3. **Copy the secret.** On the integration's page, reveal and copy the Internal integration secret. Treat it like a password. Never share it in a chat or a screenshot.
4. **Add it to n8n.** In n8n, go to Credentials, then Add credential. Search for Notion API. Paste the secret. n8n tests the connection when you save. If the secret is wrong, n8n tells you straight away.
5. **Share your databases.** In Notion, open each database the workflow needs. Click the three dots, then Connections, then add your integration. A database that is not shared stays invisible to n8n.
6. **Confirm it works.** Add a Notion node to a workflow. Choose Database Page, then Get Many. Open the database dropdown. If your database appears, everything is connected.

> NOTE: Make one integration per purpose. Create separate integrations for personal work, for team CRM, and for read-only reports. Each one gets only the access it needs. You can revoke one without breaking the others. Revoke means to cancel its access.

## A tour of the Notion node

The Notion node in n8n does many jobs. Here are the main ones.

**Database Page: Get Many.** Read many rows from a database. Use it to list tasks, find overdue items, or feed a report.

**Database Page: Get.** Read one row by its ID. Use it when a webhook gives you a page ID and you need the full row.

**Database Page: Create.** Add a new row to a database. Use it for capture workflows: emails, forms, and voice notes become rows.

**Database Page: Update.** Change a row. Update its Status, its Owner, or its Due Date. Use it to write results back after AI processing.

**Page: Get.** Read a page and its blocks. Use it to fetch the text of a page.

**Page: Get as Markdown.** Read a page as Markdown text. **Markdown** is a plain-text format with simple marks for headings and lists. This is the best way to send a page to AI.

**Block operations.** Read and write the blocks inside a page. Blocks are the pieces of a page: paragraphs, headings, lists, and images.

**User: Get and Get Many.** Look up workspace members. Use this to fill Person properties with the right person.

**Search.** Find pages and databases by title. Use it when the AI needs to find something by name.

The Notion node is also an AI tool. Attach it to an AI Agent node's tool slot. The agent can then search, create, and update pages itself. You fix the parts that should never change, such as which database to use. You let the agent fill in the rest, such as the filter or the title.

Operation names evolve. n8n adds Notion operations as Notion's API grows. An **API** is a way for apps to talk to each other. If your version shows slightly different names, update n8n, or use the HTTP Request approach later in this chapter.

## Four ways to start a workflow from Notion

A workflow needs a start. Here are four ways to start one from Notion.

**Option A: the Notion Trigger.** Add a Notion Trigger node. Pick your credential. Choose the event: Page Added to Database or Page Updated in Database. Pick the database. Set the polling interval. **Polling** means checking for changes every so often, such as every minute. Publish the workflow. n8n remembers what it has already seen, so each page fires once per change.

**Option B: a webhook from a Notion button or automation.** Add a Webhook node in n8n. Use POST and a path such as `notion-process`. Add Header Auth with a long random secret. Copy the Production URL. In Notion, add a button or a database automation, choose Send webhook, paste the URL, and add a custom header with the same name and secret. Choose the properties to include. Click the button once. Inspect the payload in n8n's execution view. The page ID arrives in the payload, so the next node can fetch or update that exact page.

**Option C: Notion integration webhooks.** Notion itself can send a webhook when something changes. This is faster than polling. Set it up in the integration settings where available. Point it at your n8n webhook URL with the same secret header.

**Option D: a schedule.** Add a Schedule Trigger node. Run every hour, or every morning at 7am. Use a Notion node to find rows that need work, such as rows with Status "Ready" that have not been processed. This is the simplest option, and it works on every plan.

Pick by your needs. Polling is easy. Buttons are instant and visible. Integration webhooks are fast. Schedules are simple and reliable.

## Mapping properties correctly

A Notion database has **properties**. Each property has a type. Mapping means matching your data to the right type. Get this wrong and the workflow fails.

Here are the common types.

- **Title.** The name of the row. Every database has one. Send plain text.
- **Text.** A short piece of text. Send plain text.
- **Number.** A number. Send a number, not text that looks like a number.
- **Select.** One choice from a list. Send the exact option name, spelled the same way. "High" is not the same as "high."
- **Multi-select.** Several choices. Send a list of exact option names.
- **Date.** A date, with an optional time. Send it in a standard format such as `2026-11-07` or `2026-11-07T14:30:00`.
- **Checkbox.** True or false. Send a real true or false value.
- **Person.** A workspace member. Send the member's user ID, not their name.
- **Relation.** A link to a row in another database. Send the linked page ID.
- **URL and Email.** Send the full address. n8n checks the format.
- **Status.** Like Select, but tied to a workflow state. Send the exact status name.

Test with one real row before you run a batch. One row shows you every mapping error at once. A hundred rows hide them in a mess.

## Filtering and querying

Reading a whole database is slow. Filtering reads only the rows you need. A **filter** is a rule that picks rows, such as "Status is To do and Due is before today."

Use filters in the Notion node where you can. Filter by Status. Filter by date. Filter by Owner. The fewer rows n8n reads, the faster the workflow runs.

Sort results too. Sort by Due Date to process the most urgent first. Sort by Created time to handle the oldest first.

Limit the number of rows. Ask for ten rows, not ten thousand. Add paging if you need more. **Paging** means reading results in small batches, one page at a time.

## The HTTP Request fallback

Sometimes the Notion node cannot do what you need. Then use the HTTP Request node. It calls Notion's API directly. This is the fallback for everything else.

You need three things. The URL of the API call, such as `https://api.notion.com/v1/pages`. The header `Authorization: Bearer YOUR_SECRET`. And the header `Notion-Version` with the current version date.

Here is a small example. This call searches your workspace for pages with "plan" in the title.

```
POST https://api.notion.com/v1/search
Header: Authorization: Bearer ntn_xxx
Header: Notion-Version: 2022-06-28
Body: { "query": "plan" }
```

Line by line: the first line is the address and the method. The second and third lines are headers that prove who you are and which API version you want. The last line is the body, the data you send. Replace `ntn_xxx` with your real secret. Replace the version date with the current one from Notion's docs.

Use the HTTP Request node for new API features that n8n has not added yet. It is also the way to fix a workflow after Notion changes its API.

## Patterns for dependable workflows

Fragile workflows break quietly. Dependable workflows survive. Use these patterns.

**Upserts.** An **upsert** updates a row if it exists, and creates it if it does not. Match rows by an External ID, such as an order number or an email address. An upsert means a webhook delivered twice does not create two rows.

**Deduplication.** **Deduplication** means removing duplicates. Keep a record of what you already processed. Check it before you act. A simple way is to store the source ID in a property and search for it first.

**Batching.** Process rows in small batches. Notion's rate limit is about three requests per second, shared across all workflows using the same integration. A **rate limit** is a cap on how many requests you can make. Add a Wait node between batches. Give heavy workflows separate integrations so they do not share one limit.

**Error paths.** Add an error branch to every workflow. On error, write a row to an Automation Log database in Notion. Include the workflow name, the time, and the error message. You will learn this in the recipe book.

**Idempotency.** Make workflows safe to run twice. **Idempotent** means the second run changes nothing. Use upserts, processing flags, and status checks. A workflow that runs twice and creates two orders is not safe.

## Troubleshooting

Here are the common errors and their fixes.

- **"Database not found."** The database is not shared with your integration. Share it in Notion under Connections.
- **"Invalid secret."** The credential is wrong or was revoked. Copy the secret again from the integration page.
- **"Property type mismatch."** You sent text where a number was expected, or a wrong Select option. Check the exact type and spelling.
- **"Rate limited."** You are sending too many requests too fast. Add waits. Split the work across integrations.
- **"Workflow fires twice."** The trigger and a button both start the same job. Use one trigger per job, or add a processing flag.
- **"Page ID is missing."** The webhook payload did not include the properties you expected. Click the button once and inspect the payload in n8n.

> TRY IT: Build the connection now. Create an integration, add the credential to n8n, share one database, and read five rows with Get Many. That test takes ten minutes. It proves the whole link works before you build anything on top of it.

## Check yourself

1. What is the first step in connecting n8n to Notion?
**Answer:** Create a Notion integration, copy its secret, add it as a credential in n8n, and share your databases with it.

2. Why should you share only the databases a workflow needs?
**Answer:** Less access is safer, and you can revoke one integration without breaking the others.

3. Which trigger should you use when a person clicks a button in Notion?
**Answer:** A webhook from the button, with a secret header for safety.

4. What is an upsert, and why does it matter?
**Answer:** It updates a row if it exists and creates it if it does not, so a webhook delivered twice does not create duplicates.

5. What is Notion's rate limit, and how do you handle it?
**Answer:** About three requests per second per integration, so batch your writes, add waits, and use separate integrations for heavy workflows.

## In short

- Create one integration per purpose, and share only the databases it needs.
- The Notion node reads and writes pages, databases, blocks, and users.
- Four triggers start workflows: Notion Trigger, button webhook, integration webhook, and schedule.
- Map each property to its exact type and spelling.
- Filter and limit reads so workflows stay fast.
- Use upserts, deduplication, batching, and error logging for dependable workflows.
