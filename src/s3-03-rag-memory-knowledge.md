# 3.3 RAG, memory, and knowledge: make AI know your stuff
<!-- original: ch. 72 -->

A chatbot knows a lot about the world. It knows nothing about you. It has not read your notes. It has not seen your files. It does not know your project. RAG fixes that. RAG lets AI read your documents before it answers.

RAG stands for Retrieval-Augmented Generation. That is a mouthful. Here is what it means in plain words. Retrieval means finding the right pages. Augmented means added to. Generation means writing the answer. So RAG means: find the right pages, add them to the question, then write the answer.

Think of it like an open-book exam. Without RAG, the AI answers from memory alone. With RAG, it can open your book first. Open-book answers are better. They use your facts. They quote your words. They make fewer things up.

## The knowledge ladder: four ways AI can know things

There are four rungs on the ladder. Each one is stronger than the last. Most beginners only need the first two.

Rung one is a long chat. You paste text into the chat. The AI reads it and answers. This works for a page or two. It is the simplest move in the whole book. The limit is the context window. A context window is how much text the AI can hold in mind at once. Paste too much, and the oldest text falls out.

Rung two is RAG. You give the AI a library of documents. It finds the best pages for each question. Then it answers from those pages. This works for hundreds or thousands of pages. You do not paste anything by hand.

Rung three is fine-tuning. Fine-tuning means training a model further on your material. It learns your style and your facts. It is costly and slow. Most people should try RAG first. Fine-tuning is covered in Section 2.

Rung four is memory. Memory means the AI remembers things about you across chats. It stores facts like your name, your project, and your preferences. Memory is the subject of Chapter 3.6. It is powerful. It also needs care, because stored facts can go stale.

> NOTE: RAG does not make the AI smarter about the world. It makes the AI better informed about your stuff. If your documents are wrong, the answers will be wrong too. Fix the source, not the answer.

## How RAG really works, in 60 seconds

RAG has four steps. They run every time you ask a question.

Step one is chunking. Your documents are cut into small pieces called chunks. A chunk is usually a paragraph or two. Small pieces are easier to search than whole books.

Step two is embedding. Each chunk is turned into numbers that capture its meaning. This is covered in depth in Chapter 3.4. For now, just know that similar meanings get similar numbers.

Step three is retrieval. Your question is turned into numbers the same way. The system finds the chunks whose numbers are closest to your question. Those chunks are the most relevant ones.

Step four is generation. The question plus the best chunks go to the AI. The AI writes an answer based on those chunks. A good RAG system shows its sources. You can click through and check.

That is the whole trick. Four steps. Find the right pieces. Add them to the question. Write the answer.

## RAG flavors: from simple to clever

Simple RAG is the basic version. One question. A few chunks. One answer. It handles most jobs well. Start here.

Then there are cleverer flavors. Hybrid search mixes meaning search with keyword search. Keyword search finds exact words. Meaning search finds ideas. Together they catch more. Reranking means scoring the found chunks a second time. The best chunks rise to the top. The weak ones drop out.

Agentic RAG is the fanciest flavor. An agent is AI that can plan and use tools. An agentic RAG system can decide to search again. It can ask a follow-up question. It can check its own answer. This is powerful for hard research. It is also slower and more costly. Do not start here.

There is also a simple upgrade called query rewriting. The system rewrites your question before it searches. "That report from last month" becomes "Q3 sales report, October". A clearer question finds better chunks.

> TRY IT: Pick a long document you own, like a report or a set of notes. Open a chatbot that accepts files. Upload it. Ask a question whose answer is on page two. Then ask a question the document does not answer at all. Notice how the AI handles each one. A good answer says "not in the document" when the fact is missing.

## Memory: making AI remember you

Memory is different from RAG. RAG reads documents at answer time. Memory stores facts about you between chats.

There are two kinds of memory. Short memory lives inside one chat. The AI remembers what you said five minutes ago. That is the context window at work. Long memory lives across chats. The AI remembers your name, your goals, and your preferences next week.

Long memory is handy. It saves you from repeating yourself. It also has risks. A stored fact can be wrong. It can be old. You might have changed your mind. Check what your assistant remembers about you. Most assistants have a memory settings page. Read it. Delete anything wrong or stale.

Which approach should you use? Use a long chat for a one-off question about one file. Use RAG when you have many files and many questions. Use memory for stable facts about you. Use fine-tuning almost never, unless RAG has failed you twice.

## Privacy, and fun projects

Privacy matters here. RAG sends your documents to an AI system. Read the privacy settings first. Some tools keep your files private. Some use them to train models. If your documents hold secrets, use a local RAG system. Local means it runs on your own computer. Chapter 3.5 shows you how to build one.

Fun projects make this real. Build a "talk to my notes" system for your journal. Build a handbook helper for your club or small team. Build a recipe finder over your saved recipes. Build a study helper over your course notes. Each one teaches the same four steps. Chunk, embed, retrieve, generate.

Privacy deserves a pause. RAG sends your documents to an AI system. Before you upload anything, read the privacy settings. Some tools keep your files private. Some use them to train future models. Some keep them for a set time and then delete them. If you do not like the answer, do not upload. Use a local system instead. Local means it runs on your own computer. Nothing leaves the machine. Chapter 3.5 shows you how to build one.

Which approach should you use? The answer depends on the job. One file, one question? Paste it into the chat. Many files, many questions? Build or buy a RAG system. Stable facts about you? Use memory. A new style you want the AI to learn? Try fine-tuning, but only after RAG has failed you twice. Most people never need the last rung. The first two cover almost everything.

Fun projects make the ideas stick. Build a helper that answers questions about your club's handbook. Build a study buddy over your course notes. Build a recipe finder over your saved recipes. Build a "what did we decide" helper over meeting notes. Each project uses the same four steps. Chunk, embed, retrieve, generate. After two projects, the steps will feel natural.

## Check yourself

1. What does RAG stand for, in plain words?
**Answer:** Find the right pages in your documents, add them to the question, then write the answer from those pages.

2. What is a chunk?
**Answer:** A small piece of a document, usually a paragraph or two, that the system can search and retrieve on its own.

3. What is a context window?
**Answer:** How much text an AI can hold in mind at once in a single chat; paste too much and the oldest text falls out.

4. How is RAG different from memory?
**Answer:** RAG reads your documents fresh each time you ask, while memory stores facts about you between chats.

5. When should you use a long chat instead of RAG?
**Answer:** For a one-off question about a single file, where pasting the text is quick and simple.

## In short

- A chatbot knows the world but nothing about you, until you give it your documents.
- RAG means find the right pages, add them to the question, then answer.
- The knowledge ladder runs from pasting text, to RAG, to fine-tuning, to memory.
- RAG works in four steps: chunk, embed, retrieve, generate.
- Cleverer flavors add hybrid search, reranking, and agents that search again.
- Check privacy settings before uploading sensitive files, and use local RAG for secrets.
