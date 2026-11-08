# 3.4 Embeddings and vector databases: search by meaning
<!-- original: ch. 73 -->

Keyword search is dumb. It only finds exact words. Search for "dog" and you miss every page that says "puppy". Search for "car" and you miss "automobile". You know what you mean. The search box does not. Embeddings fix that. They let a computer search by meaning.

An embedding is a list of numbers that captures what a piece of text means. The list is long, often hundreds of numbers. You never need to look at the numbers. What matters is the idea behind them. Texts with similar meanings get similar numbers. Texts with different meanings get different numbers.

A vector is just that list of numbers. People use the words "embedding" and "vector" to mean almost the same thing. An embedding is a vector made from text. A vector database is a store built to search vectors fast.

## The map of meaning

Picture a map. On this map, every word and sentence has a spot. Words with similar meanings sit close together. Words with different meanings sit far apart.

"Dog" sits near "puppy" and "pet". It sits far from "airplane". "Happy" sits near "joyful". It sits far from "miserable". That is the whole idea. Meaning becomes distance. Close means similar. Far means different.

Imagine the map has only two directions. Up and down means calm versus energetic. Left and right means food versus animals. "Sleepy cat" would sit in the calm, animal corner. "Spicy taco" would sit in the energetic, food corner. "Warm soup" would sit in the calm, food corner. Real embeddings use hundreds of directions, not two. But the idea is the same. Each direction captures some shade of meaning.

How close are two things? The system measures the distance between their spots. A common measure is called cosine similarity. You do not need the maths. Just know that it gives a score. A high score means close in meaning. A low score means far apart.

This is why embeddings beat keywords. A keyword search for "dog" finds only the letters d-o-g. A meaning search for "dog" finds "puppy", "hound", and "man's best friend". It finds ideas, not letters.

> NOTE: Embeddings capture meaning, but they are not perfect. They can miss jokes, sarcasm, and rare words. They work best on clear, plain text. Keep your chunks short and clear, and they will work better.

## How to make embeddings

You do not compute embeddings by hand. A model does it for you. An embedding model is an AI model trained to turn text into vectors. You send it text. It sends back numbers.

You have two choices. Use a cloud service, or run a model on your own computer. Cloud services are easy. You send text to a provider's service, and it returns the vectors. You pay a small fee per piece of text. Check the current price before you build anything big.

Local models are free to run once you have the model file. They run on your laptop. No text leaves your machine. They are a little less accurate than the best cloud models. For most personal projects, they are plenty good. A well-known free option is a small model you can run with a tool called Sentence Transformers. You do not need to know how it works inside. You just install it and call it.

Picking a model is simpler than it sounds. Check three things. How many numbers does each vector have? More numbers can mean finer meaning, but also more storage. What languages does it handle? Make sure it covers yours. How fast is it? Small models are fast and cheap. Big models are slower and sharper.

Here is a practical rule. For a personal project, start with a small free local model. If the search feels wrong, then try a bigger cloud model. Most people never need to switch.

> TRY IT: Take two sentences that mean the same thing in different words, like "The cat slept all afternoon" and "The kitten napped for hours". Then take a third sentence about something else, like "The stock market rose today". Ask a chatbot which two are closest in meaning and why. That judgement is what embeddings do with numbers.

## Vector databases: a store built for meaning

A normal database is great at exact matches. Find the row where the name equals "Dylan". A vector database is great at near matches. Find the ten chunks closest in meaning to this question.

You could store vectors in a normal database. It would work for a few hundred chunks. It would crawl for a hundred thousand. Vector databases use clever tricks to stay fast. They group similar vectors together. They skip whole groups that cannot match. They trade a tiny bit of accuracy for a lot of speed. That trade is called approximate search. In practice, you will not notice the missing accuracy.

Here are the names you will meet. Chroma is small, simple, and runs on your laptop. It is the best first choice for learning. Pinecone is a cloud service. It handles big collections and stays fast. Weaviate and Qdrant are also popular. They offer more controls for bigger projects. pgvector adds vector search to the Postgres database. It is a good pick if you already use Postgres.

Choosing is easy at first. Use Chroma for learning and small projects. Move to a cloud service only when your collection grows past tens of thousands of chunks, or when several people need to share it.

The database stores more than numbers. Each vector sits next to its chunk of text and some labels. Labels are called metadata. Metadata might hold the source file, the page number, and the date. When the system finds a good chunk, it hands back the text and the metadata together. That is how RAG can show you sources.

## Beyond RAG: ten things embeddings can do

Embeddings are not only for search. Once your text is numbers, you can do clever things with it.

You can find duplicates. Two chunks with nearly identical vectors are probably the same idea twice. You can group topics. Chunks that cluster together form a theme. You can build recommendations. "People who read this note also liked that one." You can spot outliers. A chunk far from all the others may be miscategorised or just odd. You can sort by meaning. You can classify text into groups. You can find similar images, if the images have embeddings too. You can compare documents. You can track how a topic shifts over time. And you can build the search box your notes deserve.

One warning applies to all of these. The quality of your chunks decides the quality of everything. Long, messy chunks give muddy vectors. Short, clear chunks give sharp vectors. Keep each chunk to one idea. That one habit improves every use on this list.

## Pitfalls and best practices

The biggest pitfall is chunking badly. A chunk that mixes three topics matches nothing well. A chunk cut in the middle of a sentence loses meaning. Aim for one idea per chunk. Overlap chunks slightly so no idea gets cut in half.

The second pitfall is stale data. Your notes change. Your vectors do not update themselves. Rebuild your embeddings when you add or change files. A weekly rebuild is enough for most people.

The third pitfall is picking the wrong model for your language. Some models are strong in English and weak elsewhere. Test with your own text before you commit.

A short checklist will keep you safe. Keep chunks short and focused. Store the source with every vector. Test search with ten questions you already know the answer to. Measure how often the right chunk lands in the top five. And keep a copy of your original files. Vectors are a search aid, not a replacement for the real text.

## Check yourself

1. What is an embedding, in plain words?
**Answer:** A list of numbers that captures what a piece of text means, so texts with similar meanings get similar numbers.

2. Why does meaning search beat keyword search?
**Answer:** Because it finds ideas expressed in different words, like finding "puppy" when you search for "dog".

3. What does a vector database do that a normal database does not?
**Answer:** It finds the nearest matches in meaning, fast, even across very large collections of vectors.

4. What is metadata, and why store it with a vector?
**Answer:** Labels like the source file, page, and date stored beside each vector, so the system can show you where a result came from.

5. What is the single best habit for good embeddings?
**Answer:** Keep each chunk short and focused on one idea.

## In short

- An embedding turns meaning into numbers, so similar ideas sit close together.
- Meaning search finds ideas, not just exact letters, which is why it beats keywords.
- You can make embeddings with a cloud service or a free local model.
- A vector database stores vectors and finds the nearest ones fast.
- Chroma is the best first choice for learning; cloud services suit big shared collections.
- Short, clear chunks and fresh rebuilds are what make the whole thing work.
