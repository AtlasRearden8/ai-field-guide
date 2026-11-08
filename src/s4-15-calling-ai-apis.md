# 4.15 Calling AI APIs directly
<!-- original: ch. 67 -->

Chat apps are wonderful, but the **API** is where AI becomes a programmable ingredient. An API is a front door that lets your own programs send requests to a model, and get answers back as data, without a chat window. It is how apps, automations, and agents use AI behind the scenes.

This chapter gets you making real API calls in minutes. Then it covers the patterns that matter: conversations, streaming, structured output, tool use, vision, and keeping costs down. The examples use Python and the Claude API, with notes on other providers. The same ideas work everywhere.

## Setup in five minutes

You need three things: an account with an AI provider, an API key, and Python on your computer.

First, pick a provider. Anthropic makes Claude. OpenAI makes ChatGPT. Google makes Gemini. All three offer API access. Pick the one you already use, or the one whose model you like best.

Next, get an API key. Go to the provider's website, open your account, and find the API section. Create a key. It is a long secret string. Treat it like a password. Never paste it into a chat, a screenshot, or a shared document.

Then set a spending limit. Every provider lets you set a cap, so you cannot spend more than you mean to. Set a low limit to start, like a few dollars a month. You can raise it later.

Last, install Python if you do not have it. Python 3.10 or newer works. Then install the provider's library. For Claude, that library is called `anthropic`. You install it with one command in the terminal. The provider's docs will show you the exact command.

Store your key in a `.env` file, as Chapter 4.14 explained. Your code reads it from there. Never write the key in the code itself.

> NOTE: Set a spending limit before you make your first call. An API charges for what you use. A limit turns a surprise into a small, safe lesson.

## Your first call

Here is the smallest real API call, in Python, using Claude. Read each line. The comments explain what it does.

```
import anthropic

  # Connect to Claude, using the key from your .env file.
client = anthropic.Anthropic()

  # Send one message, and get one answer back.
answer = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ],
)

  # Print the text of the answer.
print(answer.content[0].text)
```

Line one loads the library. Line four connects to Claude. Line seven sends the message. The `model` says which Claude to use. The `max_tokens` says how long the answer may be. A **token** is a small chunk of text, roughly three quarters of a word. The `messages` list holds your message, marked as from the user. The last line prints the answer.

Run it. If it prints a hello, you have just called an AI API. That is the whole trick. Everything else in this chapter is a fancier version of this call.

## The same first call with other providers

The shape is the same everywhere. You connect, you send a message, you get an answer. Only the names change.

With OpenAI, the library is called `openai`, the call is to the chat endpoint, and the model name is something like `gpt-5`. With Google Gemini, the library is Google's AI library, and the model name is something like `gemini-2.5-flash`. With xAI, DeepSeek, or a local model, the shape is the same again: a client, a model name, and a list of messages.

If you learn one provider well, you can learn another in an afternoon. The ideas transfer. The names do not.

> TRY IT: Run the first call above, then change the message to a question you actually care about. Then change `max_tokens` to 50, and run it again. Watch how the answer gets shorter. You are now tuning an API call.

## Conversations and system prompts

A single message is useful. A conversation is more useful. To have a conversation, you send the whole history each time. Each message has a **role**: user for your words, assistant for the AI's words. You keep a list, and you add each new message to it.

A **system prompt** is a special instruction that sets the AI's behaviour for the whole conversation. It is not part of the chat. It sits above it. For example: "You are a friendly cooking helper. Keep answers short. Use plain words." That prompt shapes every answer that follows. You pass it as a separate field in the call, next to the model and the messages.

System prompts are where you put the rules. The user's messages are where you put the question. Keep them apart, and your app will behave more reliably.

## Streaming

Normally, you wait for the whole answer, then you get it at once. **Streaming** is the alternative: the answer arrives word by word, as the model writes it. That is how chat apps show text appearing live.

Streaming matters when an answer is long, because the user sees something at once, instead of staring at a blank screen. Most provider libraries have a streaming mode. You turn it on, and you print each chunk as it arrives. The total answer is the same. The experience is better.

Use streaming in anything a person watches. Skip it in scripts that run in the background, where nobody is waiting.

## Structured output: data instead of prose

Sometimes you do not want a chatty answer. You want clean data. That is **structured output**. You tell the model the exact shape you want, using a schema, which is a formal description of the shape. The model then answers in that shape, every time.

For example, you might ask for JSON with the labels `name`, `price`, and `in_stock`. The model returns exactly that, with no extra words. Your code can then read the price directly, without parsing a sentence.

This is the same idea as Chapter 4.2's advice on getting JSON out of AI. The difference is that structured output enforces the shape, instead of just asking for it. Use it whenever another program will read the answer.

## Tool use: letting the model call your functions

**Tool use** is how a model does things, not just says things. You give the model a list of tools, each with a name, a description, and the inputs it needs. The model reads the list, and when it needs a tool, it asks to use it. Your code runs the tool, sends the result back, and the model continues.

For example, you might give the model a tool called `get_weather`, which needs a city name. When you ask "What is the weather in Paris?", the model asks to call `get_weather` with Paris. Your code looks up the weather, sends it back, and the model writes the answer.

This is the same loop as the agent in Chapter 4.16, but inside a single API call. It is how chatbots check calendars, search databases, and take actions. Start with one tool. Add more only when you need them.

## Vision and documents

Modern models can see. You can send them an image, or a document, along with your message. The model reads it and answers questions about it.

To send an image, you pass the image data in the message, along with your words. To send a document, you pass the file, or its text. The model can then describe the image, read the text in it, or answer questions about the document.

Useful jobs: read a photo of a receipt and pull out the total. Read a page of handwriting and type it out. Look at a screenshot and explain the error. All of these are one API call, with an image attached.

## Server-side tools: search, fetch, and code

Some providers offer tools that run on their side, not yours. The model can search the web, fetch a page, or run code, without you building those tools yourself. You just switch them on in the call.

These are handy, but they cost more, and they send your question to the provider's tools. Use them when they save you real work. Build your own tool when you need control, or when the job is simple enough to do yourself.

## Make it cheap and fast

API calls cost money, and they take time. Four habits keep both down.

First, use the smallest model that does the job. A small model is cheaper and faster. Save the big model for hard jobs.

Second, keep your prompts short. Every word you send costs a little. Every word the model writes costs a little more. Cut the fluff.

Third, **cache** repeated work. Caching means saving an answer and reusing it, instead of asking again. If you ask the same question twice, save the first answer. Some providers also cache long system prompts for you, so you pay less for them on later calls.

Fourth, use **batching** for jobs that can wait. Batching means sending many requests together, at a lower price, for work that does not need an instant answer. If you need to summarise a hundred documents overnight, batch them. If you need one answer now, do not.

## Handling errors gracefully

APIs fail sometimes. Your code should handle that calmly. The three most common errors are easy to recognise.

A **rate limit** error means you sent too many requests too fast. Wait a few seconds, and try again. A good program waits a little longer each time it retries.

An **authentication** error means your key is wrong or missing. Check the key, and check that your code is reading it from the right place.

A **server** error means something broke on the provider's side. Wait, and try again. If it keeps failing, check the provider's status page.

Write your code so that one failed call does not crash the whole program. Catch the error, wait, retry once or twice, and if it still fails, save the job to try later, and tell the user in plain words.

## Ten weekend API projects

1. A script that summarises your inbox each morning.
2. A tool that turns a photo of a receipt into a spreadsheet row.
3. A chatbot that answers questions about your notes.
4. A script that rewrites rough notes into tidy bullets.
5. A tool that checks a web page and tells you what changed.
6. A quiz maker that turns a chapter into five questions.
7. A translator for a language you are learning.
8. A script that sorts files into folders by what they contain.
9. A small web app that answers questions with AI, using one API call.
10. A daily digest that reads three news sites and writes a three-line summary.

## Check yourself

1. What is an AI API, in plain words?
**Answer:** A front door that lets your own programs send requests to a model and get answers back as data, without a chat window.

2. What is a token?
**Answer:** A small chunk of text, roughly three quarters of a word, which is how API use is measured and charged.

3. What is a system prompt?
**Answer:** A special instruction that sets the AI's behaviour for the whole conversation, kept apart from the user's messages.

4. What is structured output?
**Answer:** An answer forced into an exact shape you specify, such as JSON with fixed labels, so another program can read it directly.

5. What should you do before your first API call?
**Answer:** Set a spending limit on your account, and store your key in a .env file, never in the code.

## In short

- An API lets your programs use AI directly, with a client, a model name, and a list of messages.
- Send the whole conversation history to continue a chat, and use a system prompt for the rules.
- Streaming shows answers word by word; structured output returns clean data; tool use lets the model call your functions.
- Models can read images and documents too.
- Keep costs down with small models, short prompts, caching, and batching.
- Handle errors calmly: wait, retry, and tell the user in plain words if it still fails.
