# 3.5 Build a RAG system, step by step
<!-- original: ch. 74 -->

This is the chapter where you build the thing. By the end, you will have a working question-answering system over your own files. It will read your documents, find the best pages, and answer with sources. You will build it in four stages. Each stage works on its own. You can stop after any stage and still have something useful.

You need a computer, a text editor, and a little patience. You do not need to be a programmer. You will copy short pieces of code and run them. Each piece is explained in plain words first.

A quick note on tools. This chapter uses Python. Python is a popular programming language. It is free. It is the language most AI examples use. If you have never installed it, search for "install Python" for your computer and follow the official guide. You need version 3.10 or newer.

## Stage 0: gather your documents

Before any code, pick your documents. This matters more than any tool choice. A RAG system is only as good as its library.

Choose ten to twenty files on one topic. Course notes. A club handbook. Your own writing. Recipes. Any topic works. Keep them as plain text or Markdown files if you can. PDFs work too, but plain text is simpler for a first build.

Put them in a folder called "docs". Give each file a clear name. "gardening-notes.md" is good. "file1.txt" is not. The name becomes part of the source label later. Good names make good answers.

Now write down ten test questions. These are questions you already know the answer to. They must be answerable from your files. Write the expected answer next to each one. This list is your test set. You will use it to judge every stage. A system you cannot test is a system you cannot trust.

> NOTE: Use your own files or files you have the right to use. Do not upload someone else's private documents, work files, or copyrighted books into a cloud AI service.

## Stage 1: RAG from scratch

Stage 1 uses no fancy tools. You will write the four moves yourself. Chunk, embed, retrieve, generate. Doing it by hand once teaches you what the tools hide later.

The four moves are simple. First, cut each document into chunks. Second, turn each chunk into numbers. Third, find the chunks closest to the question. Fourth, send the question and the chunks to an AI and get an answer.

Start with chunking. Write a short script that reads each file in your "docs" folder. Split the text into pieces of about 500 characters. Let each piece overlap the next by 100 characters. Overlap stops ideas from being cut in half. Save each chunk with its file name.

Next, embeddings. For this stage, use a small free local model. Install the Sentence Transformers library. It is a free tool that turns text into vectors on your own machine. Load a small model. Send each chunk through it. Save the vectors in a file next to the chunks.

Then retrieval. Turn the question into a vector the same way. Compare it with every chunk vector. Keep the five closest. This is a simple loop. It is slow for huge libraries. It is fine for twenty files.

Finally, generation. Take the five best chunks. Paste them under the question. Send the whole thing to a chatbot or an AI service. Ask it to answer using only the pasted text. Read the answer. Check it against your test set.

> TRY IT: Before you write any code, do Stage 1 by hand. Pick one question. Open your files. Find the three best paragraphs yourself. Paste them into a chatbot with your question. That is RAG, done by a human. The code just automates what you did.

## Stage 2: real embeddings with Chroma

Stage 1 works. Stage 2 makes it last. You will replace your hand-rolled storage with Chroma. Chroma is a small vector database. It runs on your laptop. It stores your chunks and vectors. It finds the nearest chunks for you.

Install Chroma. Then write a script that does three things. It reads your chunks. It sends them to Chroma. It saves the source file name with each one as metadata. Run the script once to load your library. Run it again only when your files change.

Now write a second script for asking questions. It takes your question. It asks Chroma for the five nearest chunks. It prints them with their source names. Read them. Do they answer the question? If yes, your retrieval works. If no, your chunks may be too long, too short, or off-topic.

Next, connect the answer step. Take the five chunks. Send them with the question to an AI chat service. You can use any assistant that accepts text, or an API call. An API is a way for programs to talk to an AI service. You will need a key for that. A key is like a password for programs. Keep it secret. Never paste it into a shared file.

Ask the AI to answer only from the chunks. Ask it to name its sources. Check the answer against your test set. How many of your ten questions now pass? Write the score down. This is your baseline.

## Stage 3: pro retrieval

Stage 3 makes the answers better. You will add three upgrades. Each one is small. Together they make a big difference.

Upgrade one is hybrid search. Meaning search misses exact names. Keyword search misses ideas. Hybrid search uses both. Add a keyword search over your chunks. Combine its results with the vector search results. A chunk that scores well on either list gets a boost. Most vector databases support this. In Chroma, you can run a simple keyword pass yourself and merge the lists.

Upgrade two is reranking. The first search is fast and rough. Reranking scores the top results a second time, more carefully. Take the top ten chunks from the first search. Send them to a reranking model. Keep the best five. The answers get sharper because weak chunks drop out. A small free reranking model is enough for a personal project.

Upgrade three is contextual chunks. A chunk on its own can be confusing. "He agreed to the plan" means nothing without knowing who "he" is. Fix this by adding context to each chunk before you embed it. Add the file name and the section heading at the top. Or ask an AI to write one line of context for each chunk. "This chunk is from the gardening notes, in the section about watering." That one line helps retrieval a lot.

After each upgrade, rerun your ten test questions. Write the score down. If the score goes up, keep the upgrade. If it goes down, undo it. Let the test set decide, not your gut.

> NOTE: Do not chase a perfect score. A personal RAG system that answers eight out of ten questions well is a great tool. The last two questions usually need better source files, not better code.

## Stage 4: no-code RAG in n8n

Not everyone wants to write code. Stage 4 builds the same system with clicks. You will use n8n. n8n is an automation tool that connects apps with visual workflows. A workflow is a chain of steps shown as boxes on a screen.

Make a workflow with four boxes. The first box reads your files. The second box cuts them into chunks. The third box makes embeddings and stores them in a vector database. The fourth box takes a question, finds the best chunks, and asks an AI to answer.

n8n has ready-made boxes for each step. There is a document loader, a text splitter, an embeddings node, and a vector store node. There is also a retrieval chain that ties them together. You connect the boxes with lines. You fill in each box's settings. No code needed.

This version is easier to share. You can put a chat box on the front of it. Friends or colleagues can ask questions without seeing the workflow. You can also schedule it. Every night, it can reload any files that changed. Your library stays fresh on its own.

The code version is better for learning. The no-code version is better for sharing. Build the code version first, even if you plan to use n8n later. You will understand what the boxes do, and you will fix them faster when they break.

## Evaluate it, then run it for real

Evaluation means testing honestly. Your ten test questions are the start. Now add ten harder ones. Add five questions the files cannot answer. A good system says "I cannot find that in your documents" for those five. A bad system invents an answer. The honest "I don't know" is a feature, not a bug.

Score each answer on three points. Is it correct? Does it name its sources? Is it clear? Give one point for each. A perfect answer scores three. Track the total out of ninety for thirty questions. That number tells you if your system is getting better or worse as you change it.

Keep a tuning checklist by your desk. Are chunks one idea each? Are they about 500 characters? Do they overlap? Are sources attached? Is the AI told to use only the chunks? Is the test set fresh? Run through it whenever answers get worse.

Going to production means using it every day. Production is a fancy word for "real use". A few habits help. Back up your "docs" folder. Rebuild embeddings weekly. Keep a log of bad answers. Fix the source file when an answer is wrong. If the same question fails twice, your documents need a better paragraph, not a better model.

Project ideas to try next. A handbook helper for your sports club. A study buddy over your course notes. A recipe finder over your saved recipes. A "what did we decide?" helper over meeting notes. Each one is the same four stages, with different files.

## Check yourself

1. What are the four stages of this build?
**Answer:** Stage 1 builds RAG from scratch by hand, Stage 2 uses Chroma, Stage 3 adds pro retrieval upgrades, and Stage 4 rebuilds it with no code in n8n.

2. What is a test set, and why write it before you build?
**Answer:** A list of questions with known answers from your files, written first so you can judge honestly whether each stage actually works.

3. What does hybrid search add over plain vector search?
**Answer:** It also matches exact words, so it catches names and terms that meaning search alone can miss.

4. What is reranking?
**Answer:** Scoring the first search results a second time, more carefully, and keeping only the best few.

5. What should a good RAG system say when the answer is not in your files?
**Answer:** That it cannot find the answer in your documents, instead of inventing one.

## In short

- Pick ten to twenty files on one topic, and write ten test questions first.
- Stage 1 does the four moves by hand: chunk, embed, retrieve, generate.
- Stage 2 stores chunks and vectors in Chroma, a small local database.
- Stage 3 adds hybrid search, reranking, and context lines on each chunk.
- Stage 4 rebuilds the same system with clicks in n8n, so others can use it.
- Test honestly, keep the "I don't know" answers, and fix bad source files first.
