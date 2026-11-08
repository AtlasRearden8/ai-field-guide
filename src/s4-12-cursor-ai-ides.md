# 4.12 Cursor and AI IDEs
<!-- original: ch. 64 -->

An AI IDE is a code editor with an AI co-pilot built in. You see every file, every change, and every suggestion as it happens. That makes AI IDEs wonderful for learning, and for precise work where you want to see what the AI is doing.

This chapter tours the big editors, teaches the four ways to work with AI inside them, and explains when to reach for an IDE instead of a terminal agent like Claude Code.

## What an IDE is

An **IDE** is the application where code is written. It stands for Integrated Development Environment. You can think of it as a smart text editor for code. It shows your files in a list on the left. It shows the file you are editing in the middle. It can run your code, show errors, and help you find things.

An **AI IDE** adds an assistant to that editor. The assistant can finish your sentences, rewrite a section, answer questions about your project, and make changes across many files. The key difference from a chat-to-app builder is visibility. You see the code. You see each change. You can open any file and read it.

If Claude Code is a colleague who works in the next room and reports back, an AI IDE is a colleague who sits beside you, and you watch every keystroke.

## The four ways to work with AI in an editor

There are four ways to use AI inside an editor. Learn them, and you can use any AI IDE.

First, **autocomplete**. As you type, the AI suggests the rest of the line, or the next few lines. You press Tab to accept, or keep typing to ignore it. It is fast, quiet, and surprisingly helpful. It is best for routine code you have written a hundred times.

Second, **inline edits**. You highlight a piece of code, and ask the AI to change it. "Make this faster." "Fix the bug." "Add a check for empty input." The AI rewrites just that piece, and shows you the change before you accept it.

Third, **chat**. You open a chat panel beside your code, and ask questions. "What does this file do?" "Where is the login handled?" "How do I add a new page?" The AI answers in plain words, and it can point to the exact lines it means.

Fourth, **agent mode**. You give the agent a whole task, like "Add a search box to the home page." It plans the work, edits several files, runs the code, and fixes its own errors. This is the same idea as Claude Code, but inside the editor, where you can watch every step.

Start with autocomplete and chat. Add inline edits next. Try agent mode when you have a task that touches more than one file.

> NOTE: In agent mode, watch the list of changed files. If the agent touches a file you did not expect, stop it and ask why. A good agent can explain every change it makes.

## Cursor tour

**Cursor** is the best-known AI IDE. It looks like a normal editor, because it is built on the same base as VS Code. That means it feels familiar to millions of people, and it works with the same extensions.

Here is a quick tour. On the left, you see your files. In the middle, you see the file you are editing. On the right, or in a panel, you see the AI chat. At the bottom, you see errors and messages from running your code.

To use Cursor, open a project folder. Click on a file. Start typing, and watch the suggestions appear. Press Tab to accept one. To chat, press the keys for the AI panel, and type a question. To use agent mode, type your task, and watch it work through the files.

Cursor has a feature called **rules**. Rules are short instructions that Cursor reads every time it works in your project, like "Use plain words in the interface" or "Always write tests for new features." They are the same idea as the CLAUDE.md file from Chapter 4.10. Write a few rules, and Cursor's work will match your taste.

Cursor is a paid tool, with a free tier to try. Check the current price before you commit.

## VS Code and Copilot tour

**VS Code** is a free editor from Microsoft. It is the most widely used editor in the world. **Copilot** is its AI helper. Together, they are a strong, low-cost way into AI editors.

Copilot does autocomplete very well. As you type, it suggests code. It also has a chat panel, where you can ask questions and give tasks. In agent mode, it can edit several files at once, much like Cursor.

If you already use Microsoft tools, or if you want the biggest community to learn from, VS Code with Copilot is a solid choice. It is also the easiest editor to get help with, because so many people use it.

To start, install VS Code, then add the Copilot extension from the extensions panel. Sign in, open a project, and try the chat. Ask it to explain a file. That first answer will tell you how well it understands your project.

## Zed, JetBrains, Devin Desktop, and friends

Cursor and VS Code are the big two, but they are not the only choices.

**Zed** is a fast, light editor with AI built in. It starts quickly, it feels snappy, and it works well on older computers. If other editors feel slow, try Zed.

**JetBrains** makes editors for professional developers, such as IntelliJ and PyCharm. Their AI helper is built in, and it is very good at large projects with many files. If you work on a big project, JetBrains is worth a look.

**Devin Desktop**, formerly called Windsurf, is an AI-first editor from the team behind the Devin agent. It leans hard into agent mode, where the AI takes on whole tasks. If you like the agent style of working, try it.

You do not need to try them all. Pick one editor. Learn it well. The skills transfer. An editor is a home, not a test to pass.

## Rules and memory files everywhere

Every AI editor has a way to remember your rules. In Cursor, they are called rules. In VS Code, you can add a file called `.github/copilot-instructions.md` that Copilot reads. In Claude Code, it is CLAUDE.md. The names differ. The idea is the same.

Write your rules in plain words. Say what the project is. Say how to run it. Say what you care about. Say what to avoid. Keep it short. Update it when you learn something.

A good rules file does two things. It makes the AI's work match your taste, and it stops the AI from making the same mistake twice. When the AI does something you do not like, do not just fix it. Add a rule that says not to do it again.

> TRY IT: Open your editor's rules file, or make one. Write five lines: what the project is, how to run it, one rule about style, one rule about safety, and one thing that is easy to get wrong. Save it. Then ask the AI to do a small task, and see if its work follows your rules.

## MCP inside your editor

**MCP** is a standard plug that lets AI use your tools, which you met in Chapter 2.20. Most AI editors can connect to MCP servers. That means the editor's AI can reach your notes, your database, or your web browser, not just your code.

To add one, find the MCP settings in your editor. Add the server's name and how to start it. Once it is connected, its tools appear in the chat, and the AI can use them.

Only connect servers you trust. An MCP server can act in the app it connects to. Chapter 2.24 covers MCP safety, and it is worth reading before you connect a powerful server.

## Background and cloud agents

Some editors can run agents in the background, while you do other work. You give the agent a task, it works away, and it tells you when it is done. Some can run agents in the cloud, on a remote computer, so the work continues even when your laptop is closed.

These are useful for long jobs, like tidying a large project or checking many files. They are also easy to forget about. Always check what a background agent changed before you merge its work. A quiet agent that changed twenty files is still an agent that changed twenty files.

## IDE or terminal agent: which when?

Here is the guide. Reach for an IDE when you want to see the code, learn how it works, or make precise changes to one or two files. The editor shows you everything, and that visibility helps you learn.

Reach for a terminal agent like Claude Code when you want a whole task done, across many files, without watching each step. The terminal agent is better at long, multi-file work. It is also better at jobs that are not about code at all, like organising files or studying data.

Many people use both. They plan and build in Claude Code, then open the result in Cursor to read it, tidy it, and learn from it. That is a good habit. The agent builds. The editor teaches.

| Situation | Reach for |
| --- | --- |
| You want to learn how the code works | An AI IDE |
| You want to change one file precisely | An AI IDE |
| You want a whole feature built across many files | A terminal agent |
| You want to organise files or study data | A terminal agent |
| You want to watch every change as it happens | An AI IDE |

## Pro tips for AI IDEs

Keep your project folder tidy, so the AI can find things. Name files clearly. Write short rules, and update them when the AI makes a mistake. Review the list of changed files before you accept agent mode work. Use chat to ask "what does this do?" before you change code you do not understand. And commit with Git before you let an agent loose on a project, as Chapter 4.9 taught you.

## Check yourself

1. What is an IDE?
**Answer:** An IDE is the application where code is written, showing your files, the file you are editing, and tools to run your code.

2. What are the four ways to use AI in an editor?
**Answer:** Autocomplete, inline edits, chat, and agent mode.

3. What are rules in an AI editor?
**Answer:** Short instructions the editor reads every time it works in your project, so its work matches your taste and avoids past mistakes.

4. When is an IDE a better choice than a terminal agent?
**Answer:** When you want to see the code, learn how it works, or make precise changes to one or two files.

5. What should you check before accepting agent mode work?
**Answer:** The list of changed files, to see if the agent touched anything you did not expect.

## In short

- An AI IDE is a code editor with an assistant built in, where you see every change.
- The four ways to work are autocomplete, inline edits, chat, and agent mode.
- Cursor and VS Code with Copilot are the main choices; Zed, JetBrains, and Devin Desktop are worth a look.
- Rules files teach the editor your taste, in plain words.
- MCP servers let the editor's AI reach your other apps.
- Use an IDE to learn and to change things precisely; use a terminal agent for whole multi-file tasks.
