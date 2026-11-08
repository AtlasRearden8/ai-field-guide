# 2.18 Context: prompting's big sibling
<!-- original: ch. 36 -->

You already know the basics of good prompts. This chapter goes one level up. **Context engineering** means designing everything the model sees. Not just your message. Everything. Standing instructions. Examples. Documents. Tool descriptions. Memory. Conversation history. It is the single biggest skill gap between casual users and people who get jaw-dropping results.

A prompt is the message you type. Context is the entire package the model receives. In modern setups, your typed message is often the smallest part. The app adds its own system prompt. You add standing instructions. Tools add descriptions. Documents get attached. History piles up. Context engineering means shaping each layer on purpose.

## Standing instructions that actually work

Standing instructions live in Projects, Gems, custom instructions, or files like CLAUDE.md. They are written once and applied every time. A great set covers six things.

- **Goal and audience.** "You help me write a weekly newsletter for beginner gardeners."
- **Context about me.** "I am a nurse, not a gardener by trade. Readers are busy parents in cool climates."
- **Constraints.** "Max 600 words. No Latin plant names without a plain name."
- **Output format.** "Sections: Hook, This Week's Task, Plant Spotlight, Quick Wins."
- **Reference material.** "Use the attached past issues for tone. Never repeat a spotlight plant."
- **Judgment calls.** "If a claim is uncertain, say so. Ask me before recommending pesticides."

Explain why, not just what. "Keep it short because readers skim on phones" works better than "keep it short." The reason helps the model apply the rule in new cases. Positive instructions beat negative ones. "Write in plain, warm language" works better than a long list of banned words. Do not over-prescribe. Modern models are smart. A wall of ALL-CAPS rules makes them rigid and anxious. State priorities calmly.

Keep your instructions alive. When the AI makes the same mistake twice, add one line. When a line stops mattering, delete it. A short, living set beats a long, stale one.

> NOTE: Standing instructions are the highest-leverage writing you will ever do with AI. Fifteen minutes once can improve every answer for months.

## Examples beat adjectives

"Make it punchy" means different things to different people. One good example says more than ten adjectives. Show the model what great looks like.

For example, to teach a product-description style, give one finished example wrapped in tags, like this: a bamboo cutting board described as tough on knives' enemies, gentle on the knives, and pretty enough to serve cheese on. Then ask for a new one in the same style, for a cast-iron skillet. The model will copy the rhythm, the warmth, and the length.

Use two or three varied examples if you want range. One example can make outputs too similar. Wrap examples in tags so the model knows they are examples, not instructions. For automations, show the exact output format. Consistency jumps immediately.

> TRY IT: Pick something you write often, like an email or a post. Find your best example. Paste it and say, "Write like this." Compare the result with what you got from adjectives alone.

## Feeding documents the right way

Documents are powerful context. They are also easy to waste. Follow these habits.

- **Documents first, question last.** Models answer best when the question comes after the material.
- **Label each document.** Give each one a clear title, so the model keeps sources straight and can cite them.
- **Quote first, then answer.** Ask it to pull relevant quotes, then reason from them. This cuts made-up facts sharply.
- **Only what is relevant.** Twenty focused pages beat 500 loosely related ones.
- **Add metadata.** Dates, authors, and versions help it judge what is current.
- **Say what to do when it is missing.** "If the documents do not say, reply 'not in the sources'."

For big, changing collections, you will want **RAG**. That means the system fetches only the relevant chunks automatically. It is covered in Section 3. For now, remember the rule: relevance beats volume.

Tool descriptions are context too. For agents, tool names and descriptions are some of the most important context there is. Compare "search(q): searches" with a clear one: "Find a customer's orders by email. Use when the user asks about order status or refunds. Returns up to 20 orders, newest first." Good descriptions say what the tool does, when to use it, what it returns, and any cautions. Also, fewer tools mean better context. Every enabled tool takes up space and adds a choice. Turn off what the task does not need.

## Structured outputs and long sessions

When AI output feeds another step, like an automation or a spreadsheet, ask for **structured output**. That means a fixed format a machine can read. For example: "Classify this support email. Reply with only this JSON: category, urgency from 1 to 5, and a one-sentence summary." Many tools can enforce a format so the output is always valid. This turns fuzzy text into reliable data.

Long sessions have their own problem: **context rot**. As a conversation grows, stale ideas, abandoned attempts, and contradictions pile up. Quality slowly drops, even when there is room left in the window. Fight it with simple hygiene. One task per session. Start fresh for fresh work. When a session gets long, ask for a handoff summary, then paste it into a new chat. Summarise early decisions before they get buried.

Where should each kind of information live? Stable facts about you belong in custom instructions or memory. Project knowledge belongs in project files. Big or changing reference material belongs in RAG, connectors, or MCP. Today's specifics belong in your message. Secrets belong nowhere in prompts. API keys and passwords go in environment variables and secure connectors, never in chats.

## Build a reusable context kit

Make a folder with five files. Then attach or reference them whenever you start important work.

- **about-me.md.** Your role, goals, preferences, and what "good" looks like to you.
- **style-guide.md.** Your voice, formatting, words you love and hate, plus two or three examples.
- **glossary.md.** Terms, acronyms, and project names the AI would otherwise guess.
- **project-brief.md.** The goal, audience, constraints, and decisions made so far.
- **examples.** Gold-standard outputs to imitate.

Many people turn their kit into Projects, Gems, or a CLAUDE.md file in their project. The format matters less than the habit. Build it once. Reuse it everywhere.

> NOTE: Never paste secrets into your context kit. If a file holds a key or password, it does not belong in any AI chat or shared folder.

## Context for teams, not just for you

Context engineering scales to teams. A shared project brief means every teammate's AI gives consistent answers. A shared style guide means every draft sounds like the same company. A shared glossary means the AI stops guessing what your acronyms mean. Keep these files where the team can find them, in a shared drive or a project folder. Review them when the project changes. One person should own each file, or nobody updates it. Team context is a living document, just like personal context, only more people depend on it.

> NOTE: Shared context files are worth a short team meeting. Ten minutes of agreement saves ten hours of inconsistent drafts.

## Common context mistakes

Even good prompters make these mistakes. The first is dumping everything. A 500-page dump feels thorough. It is mostly noise. The model spends attention on pages that do not matter. Pick the 20 pages that matter. The second is burying the key fact. If the deadline is the most important thing, say it first. Do not hide it in paragraph nine. The third is contradicting yourself. Old instructions say "be brief." New instructions say "give full detail." The model must guess which one wins. Delete the old line. The fourth is never updating. A context kit from six months ago describes a job you no longer have. Review it monthly. The fifth is trusting memory too much. Memory features save facts, but they can save wrong facts too. Check what is saved every few months and delete what is stale.

> NOTE: Context is a garden, not a filing cabinet. Weed it often, or it fills with things you no longer want.

## Check yourself

1. What is the difference between a prompt and context?
**Answer:** A prompt is the message you type. Context is the entire package the model receives, including instructions, examples, documents, tools, and history.

2. Why do examples beat adjectives?
**Answer:** Adjectives like "punchy" mean different things to different people. One good example shows the exact tone, length, and style.

3. Where should the question go when you attach a document?
**Answer:** After the document, at the end of the message.

4. What is context rot?
**Answer:** Quality slowly drops in a long session as stale ideas, abandoned attempts, and contradictions pile up.

5. What belongs in a context kit?
**Answer:** An about-me file, a style guide, a glossary, a project brief, and gold-standard examples.

## In short

- Your typed message is a small part of the context. The rest matters more.
- Explain why, prefer examples to adjectives, and do not over-prescribe.
- Documents first, question last, labelled, with "quote first, then answer."
- Tool descriptions are prompts. Be specific, and enable only what you need.
- Fight context rot with one task per session and handoff summaries.
- Build a reusable context kit and use it everywhere.
