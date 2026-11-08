# 2.17 Who's who in AI
<!-- original: ch. 35 -->

Claude, GPT, Gemini, Llama, Qwen, Mistral, DeepSeek. Cursor, Perplexity, Midjourney, ElevenLabs. The AI world has a lot of names. This chapter is your field guide to them. Who makes what? How do the pieces fit together? What does "open-weight" mean? How do you read a model name? By the end, AI news will feel much less confusing.

Think of AI as a stack of layers. At the bottom are chips. Above them are clouds that run models. Above those are the labs that build models. Then come assistants and apps. You sit at the top. Most of what you use lives in the top two layers. But the lower layers explain prices, speed, and why the same model shows up in many apps.

## The frontier labs

A handful of labs build the most capable models. These are the names to know.

- **Anthropic** makes Claude. It is known for writing, coding, and agent work. It also created MCP, the plug standard covered later in this section.
- **OpenAI** makes the GPT series and ChatGPT. It kicked off the chat era. It also released open-weight models called gpt-oss.
- **Google DeepMind** makes Gemini, plus Gemma (open), Veo for video, and Imagen for images. It is strong on long context and deep Google integration.
- **Meta** makes Llama, the open-weight family that popularised open models. Meta AI lives inside WhatsApp, Instagram, and Facebook.
- **xAI** makes Grok. It is built into X and Tesla cars, and it makes images and video too.
- **Mistral AI**, from France, makes efficient open models and a chat app called Vibe.
- **DeepSeek**, from China, makes very efficient open-weight reasoning models.
- **Alibaba** makes the Qwen family. Qwen is huge, open, and strong at coding and many languages.
- **Moonshot, Zhipu, and MiniMax**, also from China, make Kimi, GLM, and MiniMax. They are strong at long context and agent work.
- **Microsoft, Amazon, and Apple** build their own models too. They also partner with other labs and bake AI into products billions of people use.

Names and rankings change fast. New flagship versions ship every few months. "Who is best" rotates. Do not memorise rankings. Learn the families and test models on your own tasks.

> NOTE: A lab is not the same as an app. OpenAI is a lab. ChatGPT is its app. Many apps are built on models from labs you have never heard of.

## Thinking Machines Lab and the Inkling models

One newer lab deserves its own spotlight. **Thinking Machines Lab** was founded in 2025 by **Mira Murati**. She was OpenAI's chief technology officer. On May 13, 2024, she introduced GPT-4o to the world on stage for OpenAI. After leaving OpenAI, she started her own lab.

The lab's models are called **Inkling**. The first Inkling arrived in July 2026. Then, on November 5, 2026, the lab released **Inkling 2 Small**. It is the first model of the lab's second generation. Here is what matters about it.

- It is a **mixture-of-experts** model. That means it has 594 billion parameters in total, but only about 17 billion are active for each token. Think of it as a huge team where only a few experts work on each word.
- It takes text and images as input. It answers in text.
- It can handle up to a 1 million-token context window. That is an enormous amount of text at once.
- It is built for long, self-directed work: coding, using tools, and carrying out tasks without supervision.
- At launch, you could only use it through the lab's platform, called **Tinker**. The full weights were not yet downloadable. The lab said it plans to release them under the Apache 2.0 licence after outside safety testing and red-teaming finish.

Why does this matter to you? Inkling 2 Small shows where open models are heading. A model this capable may soon be free to download and run. That is a big deal for privacy, cost, and choice. But note the caution too. The weights were promised, not yet released. Check the current price and availability before you build on it.

> TRY IT: Pick one task you do often, like summarising a long email thread. Try it in two different assistants this week. Note which you preferred and why. You have just started your own personal leaderboard.

## Open versus closed models

Models come in two broad kinds. **Closed** models are used through the company's app or service. Claude, flagship GPT models, and Gemini Pro are closed. They are usually the most capable. They need zero setup. They keep improving. But your data goes to the provider, and you follow their pricing and rules.

**Open-weight** models can be downloaded and run anywhere. Llama, Qwen, DeepSeek, Gemma, Mistral, and gpt-oss are open-weight. Their strengths are privacy, offline use, customisation, and no per-token fees at home. The trade-offs are clear too. You provide the hardware. Top open models can lag the frontier a little.

Note the wording. "Open-weight" is not quite the same as "open-source." Usually you get the trained weights and a licence. You do not get the training data or the full recipe. Licences vary. Some are very permissive. Others restrict certain uses. Check before building a business on one.

## The platforms, the app layer, and where models run

The big platforms put AI into products you already use. Microsoft puts Copilot in Windows, Edge, and Microsoft 365. Google puts Gemini in Android, Search, Gmail, Docs, and Chrome. Apple puts Apple Intelligence on iPhone and Mac, with ChatGPT built in. Amazon puts Alexa+ in homes and hosts models on AWS Bedrock. NVIDIA powers most AI training with its chips, and also releases open models.

Above the labs sits the app and tool layer. Coding tools like Claude Code, Cursor, and GitHub Copilot build on lab models. Search tools like Perplexity do the same. So do Notion AI, Zapier, n8n, Midjourney, Suno, and ElevenLabs. When you judge an app, ask which model powers it. The app is the experience. The model is the engine.

Models actually run in a few places. Big clouds like AWS, Google Cloud, and Microsoft Azure host many labs' models. Specialist hosts like Together, Fireworks, Groq, and Cerebras run open models fast and cheap. **OpenRouter** gives you one key for hundreds of models, which is great for comparing. **Hugging Face** is a popular home for open models, datasets, and demos. And your own machine can run models with Ollama or LM Studio, as covered later in this section.

## How to decode model names

Model names look like code. They follow patterns. Learn the patterns and the names start to make sense.

| What you see | What it usually means |
|---|---|
| Version numbers like 4, 4.5, 5 | A newer generation, usually better |
| Opus, Pro, Ultra | Biggest, smartest, priciest tier |
| Sonnet, Flash, "mini" | Balanced workhorse tier |
| Haiku, Flash-Lite, "nano" | Small, fast, cheap |
| "Instruct" or "chat" | Tuned to follow instructions |
| "Coder" | Specialised for programming |
| "VL" or "vision" | Understands images |
| 7B, 70B, 405B | Billions of parameters: rough size and hardware needs |
| "A3B" or "MoE" | Mixture of experts: only a slice activates per token, so it is fast for its size |
| Q4, Q8, GGUF, MLX | Squeezed or packaged for local use |
| A date suffix | A pinned snapshot, so behaviour will not change under you |

To keep track without drowning, use leaderboards as hints, not gospel. **LMArena** collects human preference votes. **Artificial Analysis** compares quality, speed, and price. **SWE-bench** tests coding. Read the release notes of tools you already pay for. And keep your own test: ten real tasks you care about, re-run when something new ships.

> NOTE: Rankings change monthly. A model that wins today may lose next month. Your own tasks are the only test that truly matters.

## Check yourself

1. What is the difference between a lab and an app?
**Answer:** A lab builds the model. An app is the product you use, which may run on a lab's model.

2. Who founded Thinking Machines Lab, and what did she do before?
**Answer:** Mira Murati founded it in 2025. She was OpenAI's chief technology officer and introduced GPT-4o on May 13, 2024.

3. What is Inkling 2 Small, in one sentence?
**Answer:** A large mixture-of-experts model released November 5, 2026, with 594 billion total parameters and about 17 billion active per token, built for long, self-directed work.

4. What does "open-weight" mean?
**Answer:** You can download the trained model and run it yourself, though you usually do not get the training data or full recipe.

5. How do you decode a name like "Qwen 30B-A3B"?
**Answer:** It is a Qwen model with 30 billion total parameters, of which about 3 billion are active per token, because it is a mixture of experts.

## In short

- The stack runs from chips to clouds to labs to assistants to apps to you.
- A handful of frontier labs make the top models. Many apps build on them.
- Thinking Machines Lab, founded by Mira Murati, released Inkling 2 Small on November 5, 2026.
- Closed models run through a company's service. Open-weight models can run anywhere.
- Model names follow patterns: tier words, sizes, specialisations, and packaging.
- Rankings change monthly, so trust your own tests over any leaderboard.
