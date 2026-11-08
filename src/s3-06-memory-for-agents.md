# 3.6 Memory for agents
<!-- original: ch. 75 -->

An agent is AI with a job, tools, and a loop. It can plan steps and use tools on its own. But an agent with no memory starts every day as a stranger. It forgets what you told it last week. It asks the same questions again. Memory fixes that. Memory is how an agent remembers.

Memory is not one thing. It comes in four kinds. Each kind lives in a different place. Each kind suits different facts. Getting the kinds right is the whole skill.

Think of a human assistant. They remember the task you gave them five minutes ago. They remember your name and your project from last month. They remember how your team likes reports written. They also know where the files live. An AI agent needs all four kinds of memory too.

## The four kinds of memory

Short-term memory is the current chat. It holds what you just said. It lives in the context window. It is fast and fresh. It vanishes when the chat ends. Use it for the task at hand. Do not trust it to remember anything tomorrow.

Long-term memory is facts about you that last. Your name. Your goals. Your preferences. It lives in a store the agent can read each time. Use it for stable facts. A fact that changes often does not belong here.

Procedural memory is how things are done. Your team writes reports in a certain style. Your code goes through a certain checklist. This memory holds habits and rules. Use it for repeatable ways of working. Write rules as short, plain sentences. Long rules get ignored.

Episodic memory is a record of past events. What happened on Tuesday. What the agent did last time. What went wrong. Use it for history you may need to check. An agent that can look back can avoid repeating mistakes.

A good agent uses all four. A bad agent stores everything in one pile. Then it cannot find anything, and old facts pollute new answers.

> NOTE: Memory is not free. Every fact the agent reads costs space in its context window. Store less, not more. Ten true facts beat a hundred stale ones.

## Where memory lives today

Different tools store memory in different places. Know where yours lives, or you cannot manage it.

Built-in memory lives inside the assistant. Many chat assistants now remember facts across chats. You can often see a memory page in settings. Read it once a month. Delete what is wrong. Turn it off if you do not want it. Built-in memory is easy. It is also the hardest to control, because the rules are the company's, not yours.

File-based memory lives in plain files. You write facts into a file. The agent reads the file at the start of each task. This is simple and powerful. It works with almost any agent. A file called "about-me.md" might hold your name, your project, and your preferences. A file called "project-rules.md" might hold how you like things done. Files are easy to edit, back up, and delete. For most people, this is the best place to start.

Memory servers use MCP. MCP is a standard plug that lets AI use your tools. A memory server is a small program that stores and fetches memories for the agent. The agent asks it to save a fact. Later it asks it to recall facts about a topic. This is fancier than files. It suits people building agents for a team. It also adds moving parts. Start with files. Move to a server only when files feel too small.

## Build: remember and recall tools

An agent needs two tools to use memory well. One tool saves a memory. One tool finds a memory. That is enough to start.

The save tool takes a fact and a topic. It writes the fact into a file, under the right heading. The recall tool takes a topic and returns the matching facts. The agent calls the save tool when you tell it something lasting. It calls the recall tool before it starts a task.

Here is a small design you can copy. Keep one folder called "memory". Inside it, keep three files. "facts.md" holds stable facts about you. "rules.md" holds how you like things done. "log.md" holds a dated list of past events. At the start of each task, the agent reads "facts.md" and "rules.md". When it needs history, it searches "log.md". At the end of a task, it adds one line to "log.md" about what happened.

That design is about forty lines of code in Python, if you build it as tools. If you do not code, you can do the same thing by hand. Write the three files. Paste them into the chat at the start of a task. The agent reads them. The habit matters more than the code.

> TRY IT: Write a "facts.md" file about yourself right now. Five lines only. Your name. Your main project. How you like answers written. One thing you dislike. One goal for this month. Now ask an assistant a question with those five lines pasted in. Notice how much better the answer fits you.

## Design patterns that work

A few patterns keep memory healthy. Use them from the start.

Write memories as facts, not essays. "Dylan prefers short emails" is a memory. A paragraph about email philosophy is not. Short facts are easy to find and easy to delete.

Date your memories. Add a date to each fact. "Prefers short emails (added March)". Old facts with dates are easy to review. Old facts without dates rot quietly.

Separate facts from rules. Facts describe you. Rules describe how work should be done. Mixing them confuses the agent. Keep them in different files.

Summarise, do not hoard. A log with a thousand lines is useless. Once a month, ask the agent to summarise the log into ten key events. Save the summary. Archive the rest.

Let the user correct memory. When the agent says something wrong about you, correct it once, in plain words. Then check that the stored fact changed. A memory you cannot correct is a liability.

## Memory gone wrong, and fixes

Memory fails in familiar ways. Each failure has a fix.

Stale facts are the most common failure. You changed jobs. The agent still thinks you work at the old one. Fix it by reviewing your memory files monthly. Delete or update anything old.

Contradictions come next. Two stored facts disagree. "Prefers morning meetings" and "never book before ten" might both be true, or one might be old. Fix it by dating facts and deleting the loser.

Over-sharing is a quiet risk. The agent remembers something private and repeats it to someone else. Fix it by keeping private facts out of shared memory. Use separate memory files for shared agents.

Hallucinated memory is the sneakiest failure. The agent claims you told it something you never said. Fix it by checking the log. If the fact is not in your files, it is not real. Delete it and tell the agent it was wrong.

Memory servers deserve a closer look. A memory MCP server is a small program that stores facts for the agent. The agent saves a fact through the server. Later it asks the server for facts about a topic. The server can search, rank, and return the best matches. This beats plain files when many facts pile up. It also adds a moving part that can break. Start with files. Move to a server when your facts file grows past a few hundred lines and searching it by hand feels slow.

Another pattern is to let the agent propose memories, not save them silently. When the agent thinks something is worth remembering, it should ask you first. "Should I remember that you prefer short emails?" You say yes or no. That one check stops most bad memories before they are stored. It also keeps you in charge of what the agent knows about you.

## Check yourself

1. What are the four kinds of agent memory?
**Answer:** Short-term memory in the current chat, long-term memory of stable facts, procedural memory of how things are done, and episodic memory of past events.

2. What is file-based memory, and why start there?
**Answer:** Facts stored in plain files the agent reads each time, which are simple to edit, back up, and delete, and work with almost any agent.

3. What two tools does an agent need for memory?
**Answer:** One tool to save a fact, and one tool to find facts about a topic.

4. Why should you date your memories?
**Answer:** So you can spot old facts during a monthly review and update or delete them before they go stale.

5. What is hallucinated memory?
**Answer:** When the agent claims you told it something you never said, which you fix by checking your files and deleting the false fact.

## In short

- An agent without memory starts every day as a stranger.
- Four kinds exist: short-term, long-term, procedural, and episodic.
- Built-in memory is easy but hard to control, so read its settings page.
- File-based memory in three files is the best start for most people.
- Write memories as short dated facts, and summarise logs monthly.
- Review memory every month, and keep private facts out of shared agents.
