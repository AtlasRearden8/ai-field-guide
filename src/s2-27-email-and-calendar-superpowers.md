# 2.27 Email and calendar superpowers
<!-- original: ch. 57 -->

Email and meetings quietly eat a huge share of most people's working week. AI can sort your inbox, draft replies in your voice, turn newsletters into one digest, schedule meetings without the back-and-forth, prep you for every call, and write the follow-ups. This chapter builds you a calm, AI-assisted inbox and calendar, step by step.

Most inbox time is not reading. It is deciding: is this important, and what do I do? Then it is drafting. That is exactly what AI is good at. The goal is not "AI answers my email." The goal is AI sorts, AI drafts, and you decide.

## Your email AI options

| Option | Examples | Best for |
|---|---|---|
| Built-in AI | Gmail with Gemini, Outlook with Copilot | Summaries and drafts without switching apps |
| AI-first email clients | Superhuman, Shortwave, Spark | Auto-triage, AI search, "write like me," speed |
| Your assistant plus connector | Claude or ChatGPT with Gmail or Outlook connected | Cross-app tasks, like replying using your calendar |
| Automations | n8n, Zapier, Make, Power Automate | Always-on sorting, labelling, and drafting |

You can mix them. Many people use built-in AI for quick drafts and an automation for 24/7 sorting. Start with built-in AI. Add automation only when the manual habit works.

> NOTE: Drafts, not auto-send. Keep AI at draft level for email. A human glance catches wrong names, wrong dates, and wrong tone. Those are the three classic AI email mistakes.

## Build an AI triage system

**Step one: choose five to seven piles.** Labels are the piles. Here is a set that works for most people.

- **Needs me.** Real decisions or replies only you can give.
- **Quick reply.** AI can draft, and you just approve.
- **FYI.** Read when you have time. No action needed.
- **Newsletters.** Batched into one daily digest.
- **Receipts and bills.** Auto-filed, with reminders for due dates.
- **Scheduling.** Meeting requests that flow to your calendar.
- **Noise.** Promotions you never read. Then unsubscribe.

**Step two: automate it.** New email goes to an AI classifier. The classifier applies a label. Include examples of each label in the prompt for accuracy. You can build this in n8n, Zapier, or Make.

**Step three: check a sample daily for a week.** Correct mistakes. Add those corrections as examples. Accuracy climbs fast. After a week, you will trust it. After a month, you will wonder how you lived without it.

## Drafting replies in your voice

A style guide makes drafts sound like you. Build one from five of your real sent emails. Ask your AI: "Read these five emails. Write a style guide: my tone, my sentence length, my greetings, my sign-offs, words I use, words I never use." Save the result. Paste it into your assistant's instructions or a project. Every draft from then on will sound more like you.

Then use the three-option trick. Ask for three reply options: short, warm, and firm. Pick one. Edit one line. Send. Replying takes a minute instead of ten.

For finding things, use natural-language search. "Find the email where Sam sent the venue options in March." For long threads, ask for a summary: "Sum up this 40-message thread: decisions, open questions, who owes what." After time off, ask: "I was away for a week. What needs my attention, grouped by urgency?" For attachments, ask: "Find the latest version of the contract PDF and list the payment terms."

> TRY IT: Build your email style guide today from five sent emails. Then ask for three reply options to one real email in your inbox. Pick, edit, send.

## Taming newsletters

Newsletters are useful and overwhelming at the same time. The fix is batching. Route all newsletters to one label. Once a day, ask AI to digest them: "Summarise today's newsletters in ten bullets. Flag anything with a date or a deadline." Read the digest. Delete the rest. Once a month, unsubscribe from anything you skipped three times in a row. Your inbox will shrink. Your attention will grow.

## Calendar superpowers

| Superpower | How |
|---|---|
| Find a time | "Find three 45-minute slots next week that fit Tokyo business hours and avoid my focus blocks." |
| Protect focus | AI calendars auto-schedule focus blocks, habits, and tasks around meetings |
| Weekly sanity check | "Look at next week: am I overbooked? Which meetings could be async or declined?" |
| Travel buffers | "Add 20-minute travel buffers before in-person meetings." |
| Time zones | The Time MCP server or built-in tools handle conversions without mistakes |

Meetings have three phases, and AI helps in each. Before: a prep brief with attendees, past emails, company news, and three talking points. During: AI notes in Meet, Teams, Zoom, or Notion, plus live questions like "what have we decided so far?" After: action items with owners, a follow-up email draft, and a decision log. Tell people when AI is taking notes. It builds trust and saves everyone time.

## Automations to build

| Automation | Trigger leads to result |
|---|---|
| VIP alert | Email from key people leads to a two-line summary on your phone |
| Follow-up reminder | Sent question, no reply in three days, leads to a draft nudge and a task |
| Bill reminder | Bill email leads to amount and due date on your calendar |
| Meeting prep | 30 minutes before external meetings leads to a brief in Slack or email |
| Weekly schedule preview | Sunday evening leads to "your week at a glance" with prep suggestions |
| School email decoder | School newsletter leads to dates and forms on the family calendar |

## Safety and privacy

Prompt injection is real in email. A harmful email can contain hidden instructions for your AI. **Prompt injection** means sneaking instructions into text the AI reads, so it follows the attacker's orders instead of yours. Do not combine "reads all incoming email" with "can send email or share files" without approvals. That completes the lethal trifecta from chapter 2.24.

Phishing is the other risk. AI writes flawless scam emails now. Ask AI for a second opinion: "Is this email suspicious? Check the sender, links, and urgency tricks." Grant read-only access when you only need summaries. Follow your organisation's AI policies for work email.

> NOTE: Never let inbound email trigger outbound actions without human approval. That one rule stops the most dangerous email attack.

## Your seven-day inbox makeover

- **Day 1.** Connect email and calendar to your assistant. Try three thread summaries.
- **Day 2.** Write your email style guide from five sent emails.
- **Day 3.** Set up five to seven triage labels and an AI classifier.
- **Day 4.** Newsletter digest plus an unsubscribe audit.
- **Day 5.** Meeting prep automation for tomorrow's calls.
- **Day 6.** Focus-time blocks for next week.
- **Day 7.** Review: what saved the most time? Keep it, tweak it, celebrate.

## When AI should not touch your email

Some emails are too sensitive for AI. A redundancy notice. A medical result. A legal dispute. A message about a colleague's private life. For these, read them yourself. Draft the reply yourself. AI is a helper, not a shield. Also, never let AI send email while you sleep. An auto-sent reply at 3 a.m. with the wrong name is worse than a late reply at 9 a.m. Keep a human in the loop for anything that affects a person's job, health, or money. And if an email makes you angry, do not let AI reply at once. Write your angry draft. Sleep on it. Ask AI to make it kinder in the morning. Your future self will thank you.

> NOTE: The fastest reply is not always the best reply. A pause costs nothing. A sent email costs a lot to undo.

## Check yourself

1. What is the goal of an AI-assisted inbox?
**Answer:** AI sorts, AI drafts, and you decide. Not auto-pilot email.

2. Why should AI stay at draft level for email?
**Answer:** A quick human check catches wrong names, dates, and tone, and email is hard to un-send.

3. How do you make AI drafts sound like you?
**Answer:** Build a style guide from five of your real sent emails.

4. What is prompt injection in email?
**Answer:** A harmful email hides instructions for your AI, so it follows the attacker's orders instead of yours.

5. What are the three phases of meeting help?
**Answer:** Before (prep brief), during (notes and live questions), and after (action items and follow-up draft).

## In short

- AI sorts and drafts. You decide. That is the whole system.
- A style guide makes drafts sound like you. Three options make replying fast.
- Triage labels plus an AI classifier tame any inbox in a week.
- Digest newsletters, protect focus time, and let AI prep and follow up on meetings.
- Watch for prompt injection and phishing. Keep sending behind approval.
