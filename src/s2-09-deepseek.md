# 2.9 DeepSeek, start to finish
<!-- original: ch. 25 -->

DeepSeek shook the AI world in January 2025. A small Chinese lab released a free reasoning mode that rivaled the best in the West. Then it published the model openly, for anyone to download.

Today DeepSeek offers a capable, completely free chat app with a **DeepThink** reasoning mode. It also offers open models you can run yourself.

It is also the assistant where you most need to think about privacy. Here is how to use it wisely.

## Getting started

You need a free DeepSeek account. Or a local AI setup, which we cover later in this chapter.

1. Go to **chat.deepseek.com** or install the DeepSeek app. Check the developer is DeepSeek. There are copycat apps.
2. Sign up with email, or a supported sign-in option.
3. Use the toggles under the message box. **DeepThink** turns on reasoning mode for harder problems. You will see its thinking. **Search** lets it search the web for current information.
4. Upload files with the attach button. PDFs, documents, and images with text all work.

A **reasoning mode** means the model thinks step by step before it answers. It is slower. It is also better at maths, logic, and tricky problems.

> NOTE: DeepSeek is free in the app. There is no paid plan to buy. If an app or a website asks you to pay for DeepSeek, stop. It is not the real one.

**Plans in plain English**

| Plan | Price | What you get |
|---|---|---|
| Free app | $0 | Chat, DeepThink reasoning, web search, file uploads |
| Paid plan | None | There is no paid plan in the app |

For developers, DeepSeek's own API is very cheap. The Flash model costs about $0.15 per million input tokens off-peak. A **token** is a small chunk of text, roughly part of a word. API prices matter only if you build apps. Everyday users can ignore them. But the low price is part of why DeepSeek's models appear in so many other apps and hubs, and why developers reach for them first when cost matters.

## What it is best at

**DeepThink: watch it reason.** DeepSeek's reasoning mode shows its **chain of thought**. That is the step-by-step path it took to reach an answer. You can expand the "thinking" section and read how it approached the problem. That is genuinely educational.

Try: "A train leaves at 3:40 and arrives at 7:15 with a 25-minute stop. How long is it actually moving?" Or: "Help me plan a seating chart for 24 wedding guests with these constraints." Or: "Why does this spreadsheet formula return an error? Walk through it."

Reading the reasoning helps you spot where it went wrong, if the answer seems off.

**Maths and coding practice.** DeepThink is strong at logic, maths, and code. Try: "I am learning Python. Explain what this code does line by line and suggest one improvement." Paste the code after the question.

**Long documents.** The newest models handle very long inputs well. Upload a long report and ask for the key points.

**Open weights: DeepSeek beyond the app.** DeepSeek publishes its models openly, under the MIT license. **Open weights** means the model's inner workings are free for anyone to download and run. That has big benefits.

- **Other providers host them.** You can use DeepSeek models through services in your own country, and through hub apps like Poe or HuggingChat. Your data is not sent to DeepSeek's servers.
- **Run it yourself.** Smaller distilled versions run on a good laptop or home PC with tools like **Ollama** or **LM Studio**. Fully private. Nothing leaves your computer.
- **Developers** use the cheap API to build apps and agents.

The current model family is **DeepSeek-V4**, with V4 and V4-Pro. It was previewed in April 2026 and fully released in August 2026.

> TRY IT: Give DeepSeek, with DeepThink on, and one other assistant the same logic puzzle: "Three friends split a $96 bill. One paid $40, one paid $36, and one paid $20. Who owes whom, and how much?" Read DeepSeek's thinking. Did both get it right?

**A worked example.** Ask DeepSeek, with DeepThink on: "Explain how compound interest works, then calculate what $5,000 becomes after 10 years at 4 percent, compounded monthly." Expand the thinking. Follow each step. You will see it work out the monthly rate, the number of months, and the final figure. If a step looks wrong, you can see exactly where it went off track. That is the point of visible reasoning: you can audit it.

**Recipes to try.** First, learn maths the transparent way: turn DeepThink on, ask a maths question, and read the thinking. Second, get coding help: paste a small piece of code and ask DeepSeek to explain it line by line and suggest one improvement. Third, compare it privately: install Ollama, run a small DeepSeek-based model offline, and ask it the same reasoning question. Compare the two answers. The local one never sends your words anywhere.

**When DeepSeek is the right tool.** DeepSeek is at its best when you want to learn, not just to get an answer. Because it shows its thinking, it teaches as it answers. Use it to learn maths, to understand code, or to work through a logic puzzle. For those jobs, it is as good as any assistant, and it costs nothing. For image creation, voice chat, or deep memory of your life, use another assistant instead. Pick the tool for the job, and DeepSeek earns its place for thinking out loud.

## Privacy: the important bit

Read this part carefully. It is the most important thing in this chapter.

DeepSeek's app and website store data on servers in the **People's Republic of China**. Chinese law can require companies to share data with the authorities. Several governments have restricted DeepSeek on official devices. Some regulators have investigated its data practices.

Sensible rules:

- **Fine for:** general knowledge, maths, coding practice, learning, brainstorming.
- **Avoid:** personal documents, health or financial details, work secrets, anything about other people.

Want DeepSeek's brains with privacy? Use the open model locally, or through a trusted provider in your country. Check your employer's or school's policy before using it for work or study.

## Content limits to know about

DeepSeek's app operates under Chinese regulations. It avoids or deflects questions on topics sensitive to the Chinese government. Certain historical events, political figures, and territorial questions are among them.

For history, politics, or current affairs involving China, use another assistant and multiple sources. Open models run elsewhere can behave somewhat differently, but they still reflect their training.

This is not a reason to avoid DeepSeek. It is a reason to know its blind spots, the same way you know every assistant's blind spots.

## Traps to avoid

**Fewer features than the big Western assistants.** DeepSeek has limited voice, no image generation, no memory, and fewer integrations. If you need those, pair it with another assistant.

**Busy periods bring "server busy" errors.** DeepSeek is free and popular. At peak times it may refuse a request. Wait a few minutes and try again, or ask another assistant.

**DeepThink is slower.** Reasoning mode takes longer. You do not need it for simple questions. Turn it on for logic and hard problems. Turn it off for chat.

**Turn on Search for anything recent.** Without search, DeepSeek's knowledge stops at its training date. It will not know today's news.

**Check your work.** DeepThink shows its working, which helps you catch errors. Use that. Read the thinking when the answer matters.

## Check yourself

1. What is the most private way to use DeepSeek's models?

**Answer:** Run an open DeepSeek model locally, for example with Ollama, or through a trusted provider in your own country.

2. Is DeepSeek's app a good place to paste your medical test results?

**Answer:** No. Its data is stored in China. Use it for general questions and keep sensitive information out.

3. What does DeepThink do?

**Answer:** It turns on reasoning mode. DeepSeek works through the problem step by step and shows its thinking before answering.

4. Why might DeepSeek refuse to answer a question about a historical event?

**Answer:** Its app operates under Chinese regulations and avoids topics sensitive to the Chinese government. Use another assistant for those topics.

5. DeepSeek says "server busy." What should you do?

**Answer:** Wait a few minutes and try again, or ask another assistant. It happens at busy times because the app is free and popular.

## In short

- DeepSeek offers a free, capable assistant with a transparent DeepThink reasoning mode.
- Its open-weight models can run locally or via other providers. That is the private way to use them.
- The app stores data in China. Keep personal and work information out.
- It avoids topics sensitive to the Chinese government. Use other sources for those.
- It has fewer features than the big Western assistants: limited voice, no image generation, no memory.
- DeepThink is for logic and hard problems. Turn it off for simple chat.
