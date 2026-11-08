# 1.2 How a chatbot works, without the math
<!-- original: ch. 02 -->

A chatbot feels like talking to a person. It answers in full sentences. It remembers what you said. It even has a tone. So it is natural to wonder: is there a little person in there?

No. There is a very clever guessing machine. This chapter shows you how it works, with no equations and no jargon walls. Just a clear picture.

## The one big idea: guess the next word

Everything a chatbot does comes from one job: guess the next word.

Give it the words "The cat sat on the". What comes next? Probably "mat". Maybe "floor" or "sofa". Almost never "potato". The chatbot has seen billions of sentences. It knows which words usually follow which words.

Now imagine it does that again, and again, and again. It picks a word. Then it looks at all the words so far and picks the next one. Then the next. A sentence appears. Then a paragraph. Then a full answer.

That is all it is doing. One word at a time, hundreds of times a second. The magic is in how good the guesses have become.

> NOTE: A chatbot does not plan its answer, then write it. It writes as it guesses. That is why it can wander off, repeat itself, or end a sentence in a strange place.

## How it learned: reading the internet

Before a chatbot can guess well, it has to learn. Learning means reading. A lot of reading.

Builders feed the model huge piles of text: books, websites, articles, code, conversations. The model reads them all and adjusts itself, little by little, so its guesses get better. This is called **training**. Training is the long, expensive part. It takes months and enormous computers.

Then comes a second stage. People show the model examples of good answers and bad answers. They reward the helpful, honest, clear ones. This is called **fine-tuning**, which means small adjustments after the big training. It is how a raw guessing machine becomes a polite assistant that follows instructions.

Finally, the model is put inside an app, like ChatGPT or Claude. The app adds memory for your chat, tools like web search, and safety rules. The model is the brain. The app is the body.

| Stage | What happens | Plain words |
|---|---|---|
| Training | Reads huge piles of text | Learns patterns |
| Fine-tuning | Shown good and bad answers | Learns to be helpful |
| The app | Wrapped in buttons, memory, tools | Becomes your assistant |

## Tokens: the chatbot's building blocks

Chatbots do not really work in words. They work in **tokens**. A token is a small chunk of text. It can be a whole short word, like "cat", or part of a long word, like "un" in "unhappy". On average, one token is about three-quarters of a word in English.

Why does this matter to you? Because chatbots have a **context window**. That is the amount of text they can hold in mind at once, measured in tokens. Think of it as the size of the chatbot's desk. A small desk holds a short chat. A big desk holds a whole book.

When a chat gets longer than the desk, the oldest words fall off. That is why a very long chat can start forgetting what you said at the beginning. Starting a fresh chat gives it a clean desk.

> TRY IT: Ask your assistant: "How many tokens are in the sentence 'The quick brown fox jumps over the lazy dog'?" Then ask it to explain what a token is in its own words. Compare its answer with this chapter. You are learning to check AI, and to learn from it, at the same time.

## Why two assistants can disagree

Ask the same question to two assistants. You will often get two different answers. Both can sound right. One may be wrong. Why?

Because each model was trained on different text, tuned by different people, and given different rules. Each one guesses from its own patterns. They are like two well-read people who read different books. They agree on the basics. They differ on the details.

This is useful, not confusing. Disagreement is a signal. It tells you the answer is uncertain, or that the question has more than one good answer. When two assistants disagree, check a third source. When they agree, you can relax a little.

It is also a reason to keep a favourite assistant for everyday jobs, and a second one for checking. One for writing. One for facts. The pair is stronger than either alone.

> NOTE: If two assistants disagree about a fact, do not pick the answer you like best. Pick the answer with the best source. A link to an official page beats a confident paragraph every time.

## Why it remembers your chat (and what it forgets)

Inside one chat, the chatbot sees everything you have both said. That is how it can answer follow-ups like "make it shorter" or "now do it in French". It is not remembering like you remember. It is re-reading the whole conversation each time, from the top.

That has two consequences worth knowing.

First, a chat is a fresh start. A new chat knows nothing about your old chats, unless the assistant has a memory feature turned on. Each chat is a clean room.

Second, long chats get muddled. As the conversation grows, the chatbot has more to juggle. Old details blur. New instructions can clash with old ones. When a chat starts going wrong, the fastest fix is often to start a new chat and paste in a short summary of what matters.

## Why it sometimes goes wrong

Now you can see why chatbots make the mistakes they do.

- **It guesses.** A guess can be wrong, especially about rare facts or numbers.
- **It has no source to check.** Unless it searches the web, it is working from memory of patterns, not from a book of facts.
- **It wants to please.** Fine-tuning rewards helpful, confident answers. So it would rather give you a smooth answer than say "I do not know."
- **It copies patterns.** If your question contains a wrong idea, it may repeat that idea back to you.

None of this is a reason to stop using chatbots. It is a reason to use them the way you would use a keen junior helper: give clear instructions, check the important bits, and stay in charge.

## What about "thinking" models?

Some newer assistants can "think before they answer". That means they spend extra time working through a problem step by step, in private, before they reply. They are better at hard maths, tricky logic, and long plans.

For everyday chats, you do not need to worry about this. Your assistant picks the right mode itself, or offers a button for harder tasks. The key idea stays the same: it is still guessing, one token at a time. It is just guessing more carefully.

> NOTE: You do not need to understand tokens, training, or context windows to use a chatbot well. But knowing the picture helps you forgive its mistakes, and fix them faster.

## Check yourself

1. What is the one job a chatbot does, over and over?
**Answer:** It guesses the next word, or token, one at a time, until an answer appears.

2. What is training, in plain words?
**Answer:** The model reads huge piles of text and adjusts itself so its guesses get better.

3. What is a token?
**Answer:** A small chunk of text, roughly three-quarters of a word, that the chatbot uses as its building block.

4. What is a context window?
**Answer:** The amount of text the chatbot can hold in mind at once. When a chat gets longer than that, the oldest words fall off.

5. Why does starting a new chat sometimes fix a muddled conversation?
**Answer:** A new chat gives the chatbot a clean desk, with no old instructions or details to clash with the new ones.

## In short

- A chatbot guesses the next word, one word at a time.
- It learned by reading huge piles of text, then by being shown good answers.
- It works in tokens, not words, and it has a limited context window.
- Inside one chat it re-reads everything. A new chat starts fresh.
- It goes wrong because it guesses, has no facts to check, and wants to please.
- Knowing this picture helps you use it well and forgive its slips.
