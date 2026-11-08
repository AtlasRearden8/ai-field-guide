# 2.36 Privacy and your data
<!-- original: ch. 104 -->

AI gets more helpful the more it knows about you. That is exactly why privacy matters. The good news: you do not need to be fearful, just careful on purpose. This chapter explains what happens to what you type, the settings worth checking in every AI app, a simple traffic-light system for choosing what to share, how to handle work data, connectors, and children's data, when to go fully local, and how to build AI tools that respect privacy.

Anything you type into a cloud AI service is sent to the provider's servers. A cloud service runs on the provider's computers, not yours. It may be stored there. Based on your settings, it may be used to train future models. Most everyday use is fine. Some details should never be shared. Some belong only with local models that run on your own device.

## What happens to what you type?

| Question | The general picture; check each product's current policy |
|---|---|
| Where does it go? | To the provider's servers, unless you run a local model |
| Is it stored? | Usually yes, as chat history, for a period that varies by product and setting |
| Is it used for training? | Consumer apps often let you choose. Business, team, and API plans usually do not train on your data by default |
| Can humans see it? | Some providers may review flagged content for safety. Policies explain when |
| What about connectors? | The AI reads connected data, like email and Drive, to answer you, within the permissions you grant |
| Memory? | Some facts may be saved across chats. You can view and delete them |

Privacy rules change. Terms and default settings shift over time. Check your settings again every few months, and whenever a product adds new features.

> NOTE: "Free" does not mean "private." Read the training setting in every free app you use. It is the one switch that matters most.

## Settings to check in every AI app

- **Model training, or "help improve" switch.** Choose whether your chats can train models.
- **Chat history and storage.** How long chats are kept, and how to delete them.
- **Memory.** What the app remembers about you. Look through it. Delete anything you do not want kept.
- **Temporary or private chats.** Know how to start one for sensitive topics.
- **Connectors and add-ons.** Which apps are linked, and what they can reach.
- **Shared links.** Any chats you shared in public? Cancel old ones.
- **Data export and deletion.** How to download or erase everything.
- **Account safety.** A strong password plus two-factor login.

Ask your assistant: "Walk me through every privacy setting in this app, one at a time." Then open settings and do it together. Twenty minutes, and you will know exactly where your data goes.

> TRY IT: Ask your assistant, "What do you remember about me?" Read the answer. Delete anything you do not want kept. Then start a temporary chat and ask something personal there instead.

## The traffic-light system: what to share

| Green: share freely | Yellow: share with care | Red: do not share, or go local |
|---|---|---|
| General questions and learning | Your own work documents, following company policy | Passwords, PINs, two-factor codes |
| Public information | Health questions without identifying details | Full card, bank, or ID numbers |
| Your own creative writing | Finances with account numbers hidden | Other people's private information without consent |
| Anonymous or made-up examples | Family details, first names, general situations | Confidential client or employer data on unapproved tools |
| Code without secrets | Personal journals; consider local models | Detailed medical records with identifiers |

Hiding details is a skill. Swap names for roles: "my manager," "Client A." Mask numbers. Crop screenshots. Strip location data from photos before you share them. Ask AI to help: "Here is a document. List everything I should hide before sharing it with an AI tool." Do this on a local model if the document is sensitive.

## Work data and company policies

| Do | Don't |
|---|---|
| Use your company's approved AI tools and plans | Paste confidential data into personal accounts |
| Read your organisation's AI policy | Upload customer data without permission |
| Ask IT or legal when unsure | Connect work email to unapproved AI apps |
| Use business plans with admin controls | Assume "it is just a quick question" is harmless |

Business and enterprise plans usually promise no training on your data, plus admin controls, audit logs, data-storage settings, and safety certificates. If your company has no approved tool, say so. People use AI anyway, and safe choices beat secret ones.

## Connectors, MCP, and permissions

Least access: connect only the folders, calendars, or repos needed. Read-only first, especially for email and databases. Review often. Remove connectors you do not use. Know who sees it: team connectors may expose data to colleagues' AI chats, following existing permissions. Beware prompt injection. Connected data can contain hostile instructions, as covered in chapter 2.35.

## Going local for maximum privacy

Local models run entirely on your device. Nothing leaves your machine.

| Great for local | Setup |
|---|---|
| Journals and diaries | Ollama plus Obsidian plugins |
| Health records and symptom logs | LM Studio or Open WebUI |
| Detailed financial documents | Local model plus local spreadsheet analysis |
| Redacting documents before cloud use | A small local model that finds names and numbers |
| Private voice memos | Local transcription |

The hybrid pattern: a local model redacts or summarises sensitive data, then a cloud model does the hard reasoning on the cleaned version. You get the smarts and keep the secrets.

## Kids, family, and other people's data

Children's photos: avoid uploading photos that identify children to tools you are unsure about. Other people's messages: get permission before feeding a friend's private messages or voice into AI. Family group chats: tell people if an AI bot is in the chat. Age rules: many AI apps have minimum ages. Check before setting children up. Voice and face clones: only with clear permission.

## Your rights

Based on where you live, privacy laws may give you the right to see, fix, delete, and export your data, and to object to some uses. In Europe, the GDPR covers this. In California, the CCPA covers this. Most AI providers offer data export and deletion in settings or through a privacy request form. "Help me write a data access request to this company" is a great AI task.

## Privacy for builders

If you build AI tools for other people, collect less. Only the data you need, for as short a time as possible. Tell people, in plain language, what is sent to AI providers and why. Choose providers carefully: API and business terms that do not train on your users' data. Protect secrets and data with encryption, access controls, and settings files. Scope per user: memory and document search results must never leak between users. Let users delete: a clear "delete my data" path. Redact logs: do not log full prompts with personal data forever.

> NOTE: Privacy is a design choice, not a settings page. The best time to think about it is before you collect the data, not after.

## Check yourself

1. Where does what you type into a cloud AI service go?
**Answer:** To the provider's servers, where it is usually stored as chat history, and may be used for training depending on your settings.

2. What are three things that belong in the red category?
**Answer:** Any three of: passwords, PINs, or two-factor codes; full card, bank, or ID numbers; other people's private details without permission; secret employer or client data on unapproved tools; medical records that identify someone.

3. How do you share a sensitive document with a cloud model safely?
**Answer:** Hide names and numbers first, or summarise it locally with a local model, then send the cleaned version to the cloud model.

4. Why should you check the training setting in a free app?
**Answer:** Because consumer apps often let you choose whether your chats train models, and the default may not be what you want.

5. What should builders do about user data?
**Answer:** Collect less, explain plainly what is sent and why, scope data per user, and offer a clear way to delete it.

## In short

- What you type usually goes to the provider's servers. Know your settings: training, history, memory, connectors.
- Use the traffic-light system: green means share freely, yellow means share with care, red means never share, or use a local model.
- Work data belongs in approved tools only.
- Give connectors the least access they need, and check them often.
- Local models keep the most private data at home.
- Builders should collect less and explain more.
