# 2.16 How models really work, for power users
<!-- original: ch. 33 -->

You do not need a degree to use AI well. But a few ideas under the hood explain almost every odd thing AI does. Why does it forget? Why is it so sure when it is wrong? Why does one model cost far more than another? Why are some answers slow? Learn these ideas and you can fix AI problems like a pro.

A **model** is the brain inside an assistant. It is software trained on huge amounts of text. It guesses the next word, again and again. That one trick explains both its skill and its mistakes. This chapter goes deeper than the basics, still without maths.

## How a model is made

A model is built in three stages. Each stage adds something different.

First comes **pre-training**. The model reads a vast pile of text, code, and images. It learns to predict what comes next. This gives it language, facts, and ways of thinking. It also gives it a **knowledge cutoff**. That is the date its training data stops. After that date, it knows nothing on its own.

Second comes **instruction tuning**. The model is shown thousands of examples of good assistant behaviour. A question goes in. A helpful answer comes out. This teaches it to follow instructions and chat well.

Third comes **reinforcement learning**. This is practice with feedback. The model tries tasks with checkable answers. Does the code pass its tests? Is the maths right? Good results earn a reward. Bad ones do not. Much of the progress in recent years came from this stage. Models learned to think step by step and use tools well.

> NOTE: A model does not "know" things the way you do. It stores patterns from text. That is why it can be fluent and wrong at the same time.

## Tokens and the context window

Models do not read words. They read **tokens**. A token is a chunk of text. On average, one token is about three quarters of an English word. "Hello world" is about two or three tokens. A one-page email is about 400 tokens. A long novel is about 120,000 tokens.

Tokens matter for two reasons. First, price. Most services charge per token. Output tokens often cost several times more than input tokens. Second, limits. Every model has a **context window**. That is everything it can see at once. It includes your message, the chat history, attached files, tool results, and its own reply. Top models today can hold hundreds of thousands of tokens. That is several novels at once.

But the model has no memory outside that window. When you start a new chat, it starts blank. Memory features work by putting saved notes back into the window. A bigger window is not free. More context costs more, runs slower, and can spread the model's attention thin. A focused 20-page excerpt often beats 500 dumped pages. Put key instructions first and your question last.

> TRY IT: Ask your assistant, "How many tokens is this message, roughly? And what is your knowledge cutoff date?" Then paste a long document and ask about a detail in the middle. You will learn its limits firsthand.

## Why AI makes things up, and what to do

At its core, a model predicts the most plausible next token. Training makes "plausible" line up with "correct" most of the time. But not always. A **hallucination** is a confident-sounding guess where no real knowledge exists. It is most likely when the fact is obscure, very recent, or very exact. Exact quotes, web addresses, and numbers are danger zones. Leading questions make it worse. "What did Einstein say about TikTok?" invites an invented answer.

The fix is not cleverer wording. The fix is ground truth. Give the model something real to look at. Web search, attached documents, and connectors let it check instead of guess. Ask for sources, then open them. Newer models are trained to say "I do not know" when unsure. You can help by adding that line to your request. It really does change behaviour.

**Thinking models** are a related idea. Many top models can think before they answer. They work through steps in private, check their work, and then reply. Thinking mode is slower and costs more, because thinking tokens are billed. Use it for maths, code, planning, and tricky analysis. Use quick mode for chat, rewriting, and simple lookups. Many apps pick the depth for you now.

## The harness, tools, and model tiers

What you type is not the whole input. Apps wrap your message in extra layers. There is a **system prompt**, which is the app's standing instructions. There are tool descriptions. There is memory and project context. There are retrieved documents. This wrapper is called the **harness**. It is why the same model feels different in ChatGPT, Claude, Cursor, and other apps. When you write project instructions, you are adding to the harness.

**Tool calling** is how AI "does" things. The model is shown a list of tools, each with a name and a description. When it wants to act, it outputs a structured request, like "create a calendar event at 9 a.m." Your app runs that request and sends back the result. The model never touches your calendar directly. That is why good apps ask before running risky tools.

Models also come in **tiers**. Every big lab ships a family. The top tier is the smartest and priciest. Use it for hard reasoning and high-stakes work. The middle tier is the everyday workhorse. It is fast, smart, and affordable. The small tier is quick and cheap. Use it for sorting, extraction, and high-volume jobs. **Open-weight** models are ones you can download and run yourself. They suit local and private use.

> NOTE: If a model ignores part of your instructions, the cause is often too many competing rules. Put priorities first. Split big jobs into steps. Short and clear beats long and loud.

## Debugging AI with these ideas

| Symptom | Likely cause | Fix |
|---|---|---|
| It forgot what you said earlier | Context got long, or it is a new chat | Restate key facts, or start fresh with a summary |
| Confident but wrong facts | Hallucination, or past its cutoff | Give it search, documents, or connectors, and ask for sources |
| A different answer each time | Randomness in how it picks tokens | Ask for a self-check, or compare two runs |
| Slow and expensive | Thinking depth too high, or huge context | Lower the effort, trim the context, use a smaller model |
| It mangles counting or spelling | Tokens are chunks, not letters | Ask it to use a code tool for exact counting |
| A tool agent flails | Vague tool descriptions, or too many tools | Enable fewer tools and describe them clearly |

Randomness deserves one more word. Models sample from likely next tokens, so outputs vary. Some tools let you set **temperature**. Low means focused and repeatable. High means creative and varied. For anything important, run it twice. If the two runs disagree, you have found the uncertain part.

> TRY IT: Ask the same tricky question twice in two fresh chats. Compare the answers word by word. Where they agree, trust more. Where they differ, check the facts yourself.

## What the model cannot do

Knowing the limits matters as much as knowing the tricks. A model cannot know what happened after its cutoff unless you give it search or documents. It cannot run code unless the app gives it a code tool. It cannot remember your last chat unless the app puts those notes back in. It cannot feel, want, or care. It predicts words. It cannot verify a fact by itself. It needs a source, a tool, or a test. And it cannot take responsibility. When an answer matters, the responsibility stays with you. Check it. Own it. That is not a flaw in the tool. It is the deal.

> NOTE: "The AI said so" is never a source. It is a starting point. The source is the document, the test, or the person you checked with.

## Check yourself

1. What is a token, in plain words?
**Answer:** A chunk of text the model reads and writes. On average, one token is about three quarters of an English word.

2. What is the context window?
**Answer:** Everything the model can see at once: your message, chat history, files, tool results, and its own reply.

3. Why does a model hallucinate?
**Answer:** It predicts the most plausible next word. When it has no real knowledge, a plausible guess can still sound confident.

4. What is the harness?
**Answer:** The wrapper around your message: the system prompt, tool descriptions, memory, and retrieved documents. It is why the same model feels different in different apps.

5. When should you use a thinking model instead of a quick one?
**Answer:** For hard, high-stakes work like maths, code, planning, and tricky analysis. Quick mode is fine for chat and simple lookups.

## In short

- Models are trained in three stages: reading, manners, then coached practice.
- Tokens drive cost and limits. The context window is the model's whole working memory.
- Hallucinations are confident guesses. Fix them with ground truth and sources.
- Thinking trades speed for accuracy. Use it where it matters.
- The harness explains why the same model feels different in different apps.
- Pick a model tier by task: workhorse by default, bigger for hard jobs, smaller for volume.
