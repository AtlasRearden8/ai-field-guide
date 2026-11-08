# 4.34 Running n8n and Notion in production
<!-- original: ch. 128 -->

Building a workflow is the fun part. Keeping dozens of them running reliably for months is the real skill.

Once your business, your team, or your daily life depends on n8n and Notion, you need the habits professionals use. Workflows that can safely run twice. Monitoring that catches silent failures. Backups. Security. Documentation. Cost control. A plan for API changes.

This chapter brings them together, with a checklist you can work through in an afternoon.

## Reliability: workflows that can run twice safely

**Idempotent** means safe to run twice. The second run changes nothing. Idempotent workflows survive duplicate webhooks, retries, and crashes. Build for it from the start.

Use these techniques.

**Idempotent writes.** Use upserts by External ID. An **upsert** updates a row if it exists and creates it if it does not. A webhook delivered twice does not create two rows.

**Processing flags.** Add flags such as "AI processed" or "Synced." A batch job picks up only rows without the flag. A failed run is picked up next time without redoing finished work.

**Sub-workflows.** Put shared logic in a sub-workflow. A **sub-workflow** is a small workflow that other workflows call. Triage, logging, and notifications live in one place. Fix a bug once, and it is fixed everywhere.

**Retries and timeouts.** Set a retry on steps that call outside services. A service that fails once often works on the second try. Set a timeout so a stuck step does not hang forever. A **timeout** is a maximum wait time.

**Queues for heavy work.** When many jobs arrive at once, put them in a queue. A **queue** is a waiting line. Workers take jobs one at a time. The system stays calm under load.

## Scaling n8n

Most workflows are light. A few are heavy. Heavy ones need care.

**Notion is the bottleneck.** Notion's rate limit is about three requests per second, shared across all workflows using the same integration. A **rate limit** is a cap on how many requests you can make. Batch your writes. Add waits between batches. Filter in Notion so you read fewer rows. Give heavy workflows separate integrations so they do not share one limit.

**Split big jobs.** A workflow that processes a thousand rows should split the work into batches of fifty. Each batch is a separate run. If one batch fails, the rest still finish.

**Stagger schedules.** Do not run five heavy workflows at the same minute. Spread them across the hour. They stop fighting over the same rate limit.

**Self-hosting.** If n8n Cloud limits bother you, self-host. **Self-hosting** means running n8n on your own server. It costs time to maintain, but it removes cloud limits. Keep it updated. Keep it backed up.

## Monitoring and visibility

The worst failure is the silent one. A workflow stops triggering. No error appears. Nobody notices for weeks.

**Error logging.** Every workflow writes failures to an Automation Log database in Notion. Workflow name, time, error message, and a link to the execution. Check it every morning.

**Heartbeat rows.** Critical workflows update a "Last success" date each time they run. A daily check flags any workflow whose last success is too old. A **heartbeat** is a regular signal that says "I am still alive."

**Execution history.** n8n keeps a history of every run. Check it when something looks wrong. Look for runs that failed, runs that took too long, and runs that never started.

**Usage and costs.** Watch AI provider dashboards and spend alerts. Watch n8n execution counts. A runaway loop shows up as a spike. Set alerts so you hear about it in minutes, not at the end of the month.

**A weekly review.** Once a week, read the Automation Log. Fix the top failure. Delete workflows nobody uses. A system that shrinks a little each week stays healthy.

## Backups and version control

Backups save you when things break. They are not optional in production.

**Export n8n workflows.** Export every workflow as JSON on a regular schedule. **JSON** is a simple data format. Store the exports in version control, such as Git. **Version control** is a system that tracks every change to your files, so you can go back to any earlier version.

**Export Notion data.** A weekly workflow exports key databases to CSV in cloud storage. **CSV** is a simple spreadsheet format. If Notion ever fails, your data survives.

**Credentials list.** Keep a private note of which credentials exist and where they come from. Never write the secrets themselves in the note. When a key expires, you know which one to replace.

**On change.** Back up before every big change. A backup made after the change is too late. Make the backup, make the change, test it, then move on.

## Security

Security is a habit, not a product.

**Least privilege.** Give each integration only the databases it needs. Give each credential only the access it needs. A read-only integration cannot break anything.

**Secrets.** Secrets live in n8n credentials, never in Notion pages, never in code, never in screenshots. Rotate them when someone leaves the team. **Rotate** means replace an old secret with a new one.

**Webhook secrets.** Every webhook checks a long random secret before it acts. A webhook without a secret is an open door.

**Access control.** Limit who can edit the pages that trigger real actions. A button that sends email to clients should not sit on a page everyone can edit.

**Updates.** Keep n8n updated. Updates fix security holes. Test updates in a copy first, then roll them out.

## Working as a team

A production system is a team system, even if the team is two people.

**Naming.** Name workflows clearly: `[Area] Verb object`. Examples: `[Sales] Score new leads`. `[Ops] Log errors to Notion`. Anyone can tell what a workflow does from its name.

**Ownership.** Every workflow has an owner listed in the Automations database. When it breaks, someone owns the fix.

**Environments.** Build and test in a copy before changing anything live. Use a test workflow and a test Notion database. n8n's projects and environments features help on team plans.

**Change requests.** Keep a Notion Automation Requests database. Teammates describe what they need. You triage it like any other backlog. **Triage** means sorting by urgency and deciding what to do next.

**Documentation.** Write a short note on each workflow using n8n sticky notes. Add a Notion inventory entry. Anyone should be able to understand a workflow from its name, its notes, and its inventory entry.

**Handover.** If you were away for a month, could someone else keep the system running? If not, write the missing docs now.

## Controlling costs

Costs creep up quietly. Control them with caps and habits.

**Spend caps.** Set a monthly spending cap on every AI account. A cap stops a runaway workflow from emptying your wallet.

**Cheaper models.** Use a small, cheap model for simple jobs such as classifying or summarising. Save the big model for hard jobs such as writing and reasoning.

**Batching.** Process many rows in one AI call where you can. One call with fifty short items costs less than fifty calls.

**Caching.** If the same question is asked twice, reuse the first answer. A **cache** is a store of recent answers. It saves money and time.

**Review monthly.** Once a month, read the bills. Find the most expensive workflow. Ask if it is worth it. Often a small change, such as a cheaper model or a filter, halves the cost.

## Handling API and version changes

Tools change their APIs. An **API** is a way for apps to talk to each other. When an API changes, workflows built on the old version can break.

**Watch the changelogs.** Notion and n8n both publish changelogs. A **changelog** is a list of what changed in each version. Read them when you update.

**Notion's data-source model.** Workflows built before the 2025-09-03 API version may assume one table per database. After updating n8n, note that a newer API version, 2026-03-11, exists. Check Notion's changelog for the latest steps. In general, open each Notion node and reselect the database, so n8n resolves the data source. In HTTP Request nodes, change the query path to use the data source ID, and update the `Notion-Version` header.

**Test after updates.** Update one thing at a time. Test the workflows that touch it. Roll back if something breaks. A backup made before the update makes rollback easy.

**Pin versions.** Where you can, pin the versions you depend on. **Pinning** means fixing a version number so it does not change without your say-so. Update on your schedule, not by surprise.

> NOTE: Production is a mindset, not a size. Even a household system with five workflows deserves backups, error logs, and spend caps. The habits are the same. Only the scale changes.

## The production checklist

Work through this list in one afternoon. Tick each item off.

- [ ] Every workflow uses upserts or processing flags, so it is safe to run twice.
- [ ] Every workflow writes failures to the Automation Log in Notion.
- [ ] A heartbeat check flags any critical workflow that has not run on time.
- [ ] All workflows are exported and stored in version control.
- [ ] Key Notion databases are backed up weekly to cloud storage.
- [ ] A private note lists every credential and where it came from, without secrets.
- [ ] Every webhook checks a long random secret.
- [ ] Each integration has only the databases it needs.
- [ ] Every workflow has a name, an owner, and a short note.
- [ ] Spend caps are set on every AI account.
- [ ] A test copy exists for changes before they go live.
- [ ] Someone else could keep the system running from the docs alone.

> TRY IT: Run the checklist on your own system today. Pick the three items you cannot tick. Fix the easiest one this week. A production system is built one tick at a time.

## Check yourself

1. What does idempotent mean, and why does it matter?
**Answer:** Safe to run twice, so a duplicate webhook or a retry does not create duplicate rows or actions.

2. What is a heartbeat, and what problem does it catch?
**Answer:** A regular "last success" update from a workflow, which catches workflows that stopped triggering without any error.

3. Why should you back up before a change, not after?
**Answer:** Because a backup made after the change cannot undo it if the change breaks something.

4. What is least privilege?
**Answer:** Giving each integration and credential only the access it needs, and nothing more.

5. How do you control AI costs in production?
**Answer:** With spend caps, cheaper models for simple jobs, batching, caching, and a monthly bill review.

## In short

- Make workflows idempotent: upserts, processing flags, and sub-workflows.
- Notion's rate limit is about three requests per second per integration; batch and stagger.
- Monitor with error logs, heartbeat rows, and usage alerts.
- Back up workflows and Notion data, and keep a credentials list without secrets.
- Secure webhooks with secrets, and give each integration least privilege.
- Document, name, and assign owners so a team can run the system.
- Control costs with caps, cheap models, batching, and monthly reviews.
- Plan for API changes: read changelogs, test updates, and pin versions.
