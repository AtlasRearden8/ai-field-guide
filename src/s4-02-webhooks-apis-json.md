# 4.2 Webhooks, APIs, and JSON for non-programmers
<!-- original: ch. 46 -->

Three scary words unlock almost everything in this book. They are JSON, API, and webhook. They sound technical. They are not hard. Learn them once, and every tool from n8n to MCP gets easier.

Think of it this way. JSON is how data looks when apps pass it around. An API is how one app asks another app for something. A webhook is how one app taps another on the shoulder and says, "Hey, this just happened."

You do not need to write code to use any of them. You just need to recognise them, read them, and copy the right bits into the right boxes.

## JSON: the universal data format

**JSON** is a way of writing facts so that both people and computers can read them. It stands for JavaScript Object Notation, but you can forget the full name. Just remember the shape.

JSON is made of pairs. Each pair has a label and a value. The label sits in quotes. Then comes a colon. Then comes the value. Pairs sit inside curly brackets, separated by commas.

```
{
  "name": "Pixel",
  "age": 3,
  "hungry": true
}
```

Read it line by line. The first line says the name is Pixel. The second says the age is 3. The third says hungry is true. That is all JSON is: labelled facts, written neatly.

Values can be words in quotes, numbers, true or false, or lists. A list sits in square brackets. Here is a list of toys:

```
{
  "name": "Pixel",
  "toys": ["ball", "rope", "sock"]
}
```

Lists can also hold whole groups of facts. A list of two friends looks like this:

```
{
  "friends": [
    { "name": "Milo", "age": 4 },
    { "name": "Bella", "age": 2 }
  ]
}
```

Each friend is a group inside curly brackets. The groups sit inside one list. This nesting is the only tricky part, and you will get used to it fast.

> NOTE: When something goes wrong with JSON, the error is almost always one of four things: a missing comma, an extra comma at the end of a list, a missing quote mark, or a curly bracket that never closes. Check those four first.

## Getting JSON out of AI reliably

AI loves to write chatty answers. That is a problem when you need clean JSON. The fix is simple: tell the AI exactly what shape you want, and tell it to output only JSON, with no extra words.

Try a prompt like this: "Read the email below. Answer with JSON only, no other text. Use these exact labels: sender, amount, what_for." Then paste the email. Most of the time, the AI will obey.

If it still adds chatty words, use a **structured output** feature if your tool has one. That is a setting that forces the AI to answer in a fixed shape. In n8n, the Structured Output Parser node does this. In code, many AI tools let you pass a **schema**, which is just a formal description of the shape you want. You do not need to write the schema by hand. Ask the AI to write it for you.

> TRY IT: Ask your favourite chatbot to turn this sentence into JSON: "Mara ordered two books for $24 on Tuesday." Tell it to use the labels customer, items, total, and day, and to output JSON only. Then change one word in the sentence and ask again. Watch how the values change but the labels stay the same.

## APIs: apps' front doors

An **API** is a front door that an app leaves open for other programs. It stands for Application Programming Interface. Forget the full name. Think of it as a menu in a restaurant. The menu lists what you can order. You order by sending a request. The kitchen sends back what you asked for.

A request has four parts. The **address** is a web link, called a URL, that points to the thing you want. The **method** is the verb: GET means "give me this," POST means "make this," PUT means "update this," and DELETE means "remove this." The **headers** are extra notes, like your ID badge. The **body** is the data you send along, usually in JSON.

The answer comes back with a **status code**. That is a three-digit number that says what happened. The most useful ones are easy to remember.

| Code | What it means |
| --- | --- |
| 200 | It worked. Here is what you asked for. |
| 201 | It worked, and something new was created. |
| 400 | Your request was wrong. Check what you sent. |
| 401 | You are not signed in, or your key is wrong. |
| 403 | You are signed in, but you are not allowed to do this. |
| 404 | That thing does not exist at this address. |
| 429 | Too many requests. Slow down and try again later. |
| 500 | Something broke on their side. Try again later. |

You can try a real API right now, with no key and no account. Open your browser and visit a public test API, such as the JSONPlaceholder test service. Ask for a sample post, and your browser will show you JSON. You just made an API call with your browser. It really is that simple.

## Authentication: proving who you are

Most APIs ask you to prove who you are before they help you. This is called **authentication**. There are a few common ways it works.

An **API key** is a long secret password for programs. You get one from the app's settings page. You send it with every request. Treat it like a house key. Never paste it into a chat, a screenshot, or a shared document.

**OAuth** is the "Sign in with Google" flow you already know. You click a button, you sign in, and you approve what the app may do. The tool then gets a token, which is a temporary pass that proves your approval. This is safer than a key, because you can take the approval back any time.

**Bearer tokens** are the most common way keys travel. The request carries a header that says "Bearer" followed by the secret. You rarely type this by hand. Your tool fills it in for you.

> NOTE: If an API says 401, your key is wrong, missing, or expired. If it says 403, your key works, but it does not have permission for that action. That difference saves you a lot of guessing.

## Webhooks: call me when something happens

An API is you asking. A **webhook** is the other way round. It is the app calling you.

Here is how it works. Your automation tool gives you a special web address. You paste that address into another app's settings, in the webhooks section. From then on, whenever something happens in that app, it sends a message to your address at once. A new order, a new form answer, a new comment: each one arrives as a JSON message, seconds after it happens.

That is why webhooks are fast. A schedule checks every hour. A webhook tells you at once. If you want instant reactions, use a webhook. If the app does not offer webhooks, fall back to a schedule.

Webhooks have one weakness. Anyone who knows the address can send fake messages to it. So treat a webhook address like a secret. Some tools let you add a secret word that the sender must include. Turn that on when it is offered. And never put a webhook address in a public place.

Your phone can send webhooks too. On an iPhone, the Shortcuts app can send a web request to a webhook address. That means one tap on your phone can start any automation you own. Android users can do the same with Tasker or a similar app. Chapter 4.6 shows you how.

## Reading API docs without fear

API docs look scary. They are mostly the same page, repeated. Look for four things and skip the rest.

First, find the **base URL**. That is the start of every address. It looks like `https://api.example.com/v1`. Every request starts with it.

Second, find the **endpoints**. An endpoint is one address on the menu, plus its method. It might say `GET /users` to list users, or `POST /orders` to make an order. Copy the address exactly.

Third, find the **authentication** section. It tells you where your key goes. Usually it goes in a header. Sometimes it goes in the address itself.

Fourth, find one **example**. Good docs show a sample request and a sample answer. Copy the sample. Change one small thing. Run it. That is how everyone learns an API, including professionals.

Two more ideas will save you trouble. A **rate limit** is how many requests you may send in a minute or a day. If you hit it, you get a 429 code. Slow down, and try again later. **Pagination** is how big lists are split into pages. If an API says there are 500 items but sends you 50, ask for page two, then page three, until you have them all.

> TRY IT: Pick an app you use every day. Search the web for its name plus the word "API". Open the docs page. Find the base URL, one endpoint, and the authentication section. Do not send anything yet. Just find those three things. You have now read real API docs.

## Check yourself

1. What is JSON, in one sentence?
**Answer:** JSON is a way of writing labelled facts, in pairs of a label and a value, so that people and computers can both read them.

2. What is the difference between an API and a webhook?
**Answer:** With an API, you ask another app for something. With a webhook, the other app tells you the moment something happens.

3. What does a 404 status code mean?
**Answer:** The thing you asked for does not exist at that address.

4. What should you check first when JSON fails?
**Answer:** A missing comma, an extra comma at the end, a missing quote mark, or a bracket that never closes.

5. Why should you keep an API key secret?
**Answer:** Anyone with the key can act as you in that app, so it works like a password and must never be shared.

## In short

- JSON is labelled facts in pairs, written so both people and computers can read them.
- An API is a front door that lets one program ask another for data or actions.
- A webhook is the reverse: an app sends you a message the moment something happens.
- Status codes tell you what happened: 200 means it worked, 401 means your key is wrong, 404 means it does not exist, and 429 means slow down.
- Keep keys and webhook addresses secret, and use a secret word on webhooks when you can.
- Read API docs by finding the base URL, one endpoint, the authentication section, and one example.
