# 2.11 Qwen, Kimi, and other global assistants
<!-- original: ch. 27 -->

The AI world is not just Silicon Valley. Some of the most impressive, and most openly shared, AI models now come from China. There are also excellent assistants built for Europe, India, Korea, the Middle East, and beyond.

This chapter is your passport. It covers Qwen, Kimi, Z.ai, MiniMax, and friends. It says what they are great at, how to try them, and the privacy rules of the road.

## Why look beyond the big names?

There are four good reasons.

**Generous free tiers.** Several global assistants offer powerful features at no cost. Long documents, image generation, and research tools that cost money elsewhere are often free here.

**Open weights.** Many Chinese labs publish their models openly. **Open weights** means the model's inner workings are free for anyone to download and run. You can run them on your own computer, or through providers you trust. Your data never goes to the original company.

**Languages and culture.** Regional assistants often understand local languages, idioms, and contexts better than the big Western assistants. If you speak a language the big assistants handle awkwardly, a local option may surprise you.

**Innovation.** Long-document handling, agent modes, and slide and website builders often appear here first. An **agent mode** is a setting where the AI does multi-step jobs for you, instead of just answering one question.

**Travel.** In mainland China, most Western assistants are not available. Locals use Doubao, Qwen, DeepSeek, Kimi, and others. If you travel there, you will need a local assistant.

> NOTE: "Free" does not mean "no cost to you." Your chats are the product in a different way: they are stored under the laws of the country where the company keeps them. Read the privacy section before you share anything personal.

## Qwen (Alibaba)

Qwen is the assistant from Alibaba, one of China's biggest tech companies. You can find it at **chat.qwen.ai**, also called Qwen Chat, and in the Qwen app.

Qwen's standouts:

- **119 languages.** Few assistants match that range. It is strong at translation and multilingual tasks.
- **Image and video understanding.** Upload a picture or a clip and ask about it.
- **Image generation.** Make pictures from a description.
- **Document processing.** Upload files and ask questions about them.
- **Voice chat.** Talk instead of typing.
- **Deep research.** Long, sourced reports on big questions.
- **A web-building mode.** Describe a website and watch Qwen build a simple version.

The Qwen family is among the world's most-downloaded open models. The Qwen3.8 series runs locally with Ollama, a free tool for running models on your own computer. Qwen3.8-Max became the flagship model on August 3, 2026.

Try this: "Translate this paragraph into Portuguese, Swahili, and Vietnamese, and flag any phrases that do not translate well culturally."

Qwen is great for multilingual tasks, translation, trying many model sizes, and running AI locally.

## Kimi (Moonshot AI)

Kimi is the assistant from Moonshot AI, a Chinese lab. You can find it at **kimi.com**, which has an English interface, and in the Kimi app, now on the US App Store.

Kimi's standouts:

- **Very long documents.** Kimi was built for huge inputs. Upload a long report, a book, or a bundle of files and ask questions.
- **Polished file uploads.** It handles PDFs and research bundles well.
- **Agent tasks.** Give Kimi a job with many tool steps and let it work through them.
- **Research reports and slide decks.** Turn research into a presentation. Try: upload a long report and ask, "Turn this into a 10-slide deck for a non-expert audience, with one key chart idea per slide."

The **Kimi K2** family is open-weight and popular with developers. Perplexity offers Kimi models to Pro users.

One warning: Moonshot is retiring K2. There are no new sign-ups from October 31, 2026. K2 models go offline by the end of December 2026. Moonshot is moving to **K3.1 Pro**, released on October 23, 2026. Check kimi.com before building anything on K2.

Kimi is great for big PDFs, research bundles, turning research into slides, and agent experiments.

> TRY IT: Pick a phrase from your family's heritage language, or one you are learning. Ask three assistants from three different countries to explain its meaning, its origin, and how to use it. Who understood the culture best?

## Z.ai, MiniMax, Doubao, and more from China

China has several other major assistants. Each has its own flavor.

| Assistant | Maker | Known for |
|---|---|---|
| DeepSeek | DeepSeek | Free reasoning you can watch. See chapter 2.9 for the full guide. |
| Qwen | Alibaba | 119 languages, open models, web building |
| Kimi | Moonshot AI | Very long documents, agents, slides |
| Z.ai | Zhipu AI | Chat, image and video creation, and agents for everyday tasks |
| MiniMax | MiniMax | Creative tools, including video and voice, and lively chat |
| Doubao | ByteDance | One of China's most-used assistants, built for everyday life |

Z.ai and MiniMax are worth a try if you want creative tools or a different style of chat. Doubao is the assistant most people in China reach for first. It comes from ByteDance, the company behind TikTok.

All of these change fast. Features, names, and availability shift every few months. Check the assistant's own site before you rely on it.

## Around the world

Beyond the US and China, a growing number of assistants focus on regional languages and needs.

- **Europe.** Mistral's Vibe, covered in chapter 2.10, is the leading European assistant. Other European projects focus on local languages and strict privacy rules.
- **India.** Assistants and models built for India's many languages are growing. They handle Hindi and regional languages better than global models sometimes do.
- **Korea.** Korean assistants understand Korean language and culture deeply. They are useful if you live, work, or travel there.
- **The Middle East.** Arabic-first assistants serve a region the big models have underserved. They handle dialects and local context better.
- **Africa.** Research groups are building models for African languages. These are languages the big models often underserve.

Quality varies. These tools change fast. If you speak a language that the big assistants handle awkwardly, a local option may surprise you.

## Privacy: know where your words go

The same rule applies to every assistant. Your chats are subject to the laws where the company stores them.

**Chinese services** like Qwen, Kimi, Z.ai, Doubao, and DeepSeek generally store data in China. Chinese law can require companies to share data with the authorities. These services are great for general knowledge, coding practice, and creative play. They are **not** for personal, financial, health, or work-confidential information.

**The open-weight loophole.** Run these models **locally**, or through a provider in your own country, and your data never goes to the original company. That is the private way to use a global model. Install Ollama, then run a small model. For example: `ollama run qwen3.6:27b`. Or pick a smaller size for a modest computer. Ask it something offline. Your data never leaves your computer.

**Content rules.** Assistants follow local laws. Chinese assistants avoid politically sensitive topics. Other countries have their own rules. For history, politics, or current affairs involving China, use another assistant and multiple sources.

**Work and school.** Check your organization's policy first. Many restrict foreign AI services. Do not use them for work until you know the rules.

> NOTE: Running a model locally sounds technical. It is simpler than it sounds, and there is a full guide later in this book, in the local AI chapters. You do not need to do it today. Just know the option exists.

## Check yourself

1. What is the private way to use a Chinese open-weight model like Qwen?

**Answer:** Run it locally, for example with Ollama, or through a trusted provider in your country, so your data never goes to the original company.

2. You are traveling in mainland China and your usual assistant does not work. Why, and what do locals use?

**Answer:** Most Western assistants are not available there. Locals use Doubao, Qwen, DeepSeek, Kimi, and others.

3. Which global assistant is best known for handling very long documents?

**Answer:** Kimi. It was built for huge inputs, and it turns research into slide decks.

4. How many languages does Qwen support?

**Answer:** 119 languages, which makes it strong for translation and multilingual tasks.

5. Why should you keep work secrets out of a Chinese assistant's app?

**Answer:** The data is generally stored in China, where companies can be required to share data with the authorities. Check your employer's policy first.

## In short

- Qwen is multilingual and open. Kimi is built for long documents, agents, and slides.
- Z.ai, MiniMax, Doubao, and ERNIE are other major Chinese assistants. DeepSeek has its own chapter, 2.9.
- Regional assistants in Europe, India, Korea, the Middle East, and Africa serve local languages and needs.
- Mind jurisdiction: keep sensitive information out of foreign services, or run open models locally.
- Chinese assistants avoid politically sensitive topics. Use other sources for those.
- Check the current features on each assistant's own site. They change fast.
