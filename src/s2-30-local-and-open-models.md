# 2.30 Local and open models: AI on your own machine
<!-- original: ch. 78 -->

Yes, you can run surprisingly capable AI entirely on your laptop. Offline. Private. Free per use. Open-weight models have improved at a startling pace. A mid-range computer now runs assistants that would have seemed like frontier magic a couple of years ago. This chapter explains why you would go local, the tools, the model families, what your computer can handle, the jargon, and a pile of fun projects.

Most AI runs on remote servers. But smaller open models can now run directly on your computer. Local AI keeps your data private, works offline, and costs nothing per use. It is less capable than the largest cloud models. It is more than enough for many everyday tasks.

## Why go local?

| Great for | Not great for |
|---|---|
| Privacy: journals, medical notes, client data | The hardest reasoning and big coding tasks |
| Offline use: flights, cabins, bad Wi-Fi | Very long documents on small machines |
| Unlimited experimentation at no per-use cost | Speed on older hardware |
| Batch jobs, like tagging 10,000 photos | "It just works" convenience |
| Learning how AI actually works | Web search and tools out of the box, which need setup |
| Control: pick the model, no surprise changes | |

The sweet spot is hybrid. Use frontier models for hard thinking. Use local models for private, repetitive, or high-volume grunt work. Many tools let you mix both in one place.

> NOTE: Local does not mean worse. It means different. A small local model can beat a giant cloud model at a narrow, private, high-volume job.

## Your first local model in five minutes

**Ollama** is the standard starting point. It is a command-line model runner. Install it from ollama.com for Mac, Windows, or Linux. Then run one command to download a model and chat with it in your terminal. Useful commands list your installed models, download another, show what is loaded, and free up disk space.

**LM Studio** is the friendly alternative. It is a desktop app. Browse models, download one, chat in a window, and run a local server. No terminal needed. Ask it something, then turn off your Wi-Fi and ask again. It still works. That moment is the whole point of local AI.

Other tools fill other niches. **Jan** is an open-source, ChatGPT-style desktop app, local-first. **Open WebUI** is a self-hosted, ChatGPT-like web interface with document chat and multiple users. That is your own private ChatGPT. **llama.cpp** is the engine under much of this, for tinkerers who want maximum control. **MLX** is Apple's framework, very fast on Apple Silicon. **vLLM** and **SGLang** serve models to a team on GPUs. **AnythingLLM**, **Msty**, and **GPT4All** are friendly desktop apps. Try a few and keep the one you like.

## Open model families to know

| Family | From | Known for |
|---|---|---|
| Gemma | Google | Excellent small and mid-size models, vision, many languages |
| Qwen | Alibaba | Strong all-rounders and coding models, many sizes |
| DeepSeek | DeepSeek | Strong reasoning and big mixture-of-experts models |
| Llama | Meta | The family that kicked off the open-model boom |
| gpt-oss | OpenAI | Open-weight reasoning models under a permissive licence |
| Mistral | Mistral AI | Efficient European models, strong small ones |
| Phi | Microsoft | Tiny models that punch above their weight |
| Nemotron | NVIDIA | Models tuned for reasoning and agents |
| Kimi, GLM, MiniMax | Moonshot, Zhipu, MiniMax | Big, capable models popular for agent coding |

Names move fast. Popular local picks change every few months. By the time you read this, there may be newer ones. Check the Ollama library, LM Studio's Discover tab, and Hugging Face trending pages. Do not memorise model names. Learn the families and the sizes.

## What can my computer run?

The rule of thumb: a model needs roughly its size in gigabytes of memory, plus a bit extra for the conversation. Squeezed to 4 bits, that is about 0.6 GB per billion parameters. A **parameter** is one of the model's internal knobs. Billions of them, written as B, measure rough size.

| Your machine | Comfortable models | Feels like |
|---|---|---|
| 8 GB RAM laptop | 1 to 4B, like small Gemma, Phi, or Qwen | Quick helper: summaries, rewriting, classification |
| 16 GB RAM, or Apple M-series | 7 to 14B | Solid chat, decent coding help |
| 32 to 64 GB Mac, or 24 GB GPU | 20 to 35B, including mixture-of-experts models | Genuinely impressive |
| 128 GB or more Mac, or multi-GPU | 70 to 120B or more | Near-frontier on many tasks |

This is honest, not hype. An 8 GB laptop will not run a 70B model. It will run a small model well. A small model is enough for summaries, rewriting, tagging, and extraction. Match the model to the machine you have, not the machine you wish you had.

## Local AI jargon, decoded

| Term | Plain English |
|---|---|
| Parameters (7B, 70B) | The number of knobs in the model. Bigger is usually smarter and hungrier. |
| Open-weight | You can download and run the model. Fully "open source" also shares training data and code, which is rarer. |
| Quantisation (Q4, Q5, Q8) | Storing the knobs with fewer bits to shrink the model. Q4 is the usual sweet spot. |
| GGUF | The file format used by llama.cpp, Ollama, and LM Studio. |
| MLX | Apple's format and framework for fast Mac inference. |
| MoE, mixture of experts | A big model where only a few experts work per token. Big-model smarts, small-model speed. |
| Context length | How much text the model can consider at once. Longer context uses more memory. |
| Tokens per second | Speed. About 10 or more feels comfortable for reading along. |
| Licence | What you are allowed to do. Apache 2.0 and MIT are permissive. Others have conditions. Check before commercial use. |

**Quantisation** deserves one more line. It squeezes a model smaller with little quality loss. A 4-bit version of a 7B model fits in about 4 to 5 GB. That is why your laptop can run it at all.

## Using local models from other apps

Ollama and LM Studio expose an **OpenAI-compatible API** on your machine. That is a standard way for programs to talk to AI. Most tools that speak "OpenAI" can use your local models instead. Point n8n's Ollama node at it for free, unlimited automations. Point Obsidian plugins at it for private note chat. Point code editors at it for local coding help. Point Open WebUI at it for a private ChatGPT. Point your own scripts at it with the OpenAI SDK and a local address. Pull an embeddings model for local document search.

Open models also live in the cloud. **OpenRouter** gives one key for hundreds of models, open and closed. **Groq**, **Cerebras**, **Together**, and **Fireworks** host open models very fast. **Hugging Face** runs models from its hub without you managing servers. Handy for trying a big model before buying hardware for it. Remember: cloud means your data leaves your machine. Check the current price before you use a cloud host heavily.

> TRY IT: Install Ollama. Run a small model. Ask it to write a haiku about your Wi-Fi being off. Then turn your Wi-Fi off and ask again. Next, try a model battle: the same three questions to the local model and to Claude. Where is the gap? Where is there not one? That is your local-AI intuition forming.

## Fun local projects

| # | Project | Why local shines |
|---|---|---|
| 1 | Private journal analyst: find mood patterns in your journal | Nothing leaves your machine |
| 2 | Photo tagger: a vision model captions and tags your photo library | Thousands of images, zero cost |
| 3 | Local agent in n8n for free, unlimited automations | No per-call bills |
| 4 | Offline coding buddy | Works on a plane |
| 5 | Model battle: the same ten prompts through three local models and a frontier model, scored blind | Builds real intuition |
| 6 | Voice notes to summaries with local transcription | Private meetings and memos |
| 7 | Receipt extractor from scanned PDFs | Sensitive finances stay home |
| 8 | File renamer: "rename these 500 PDFs by their content" | Bulk work for free |
| 9 | Offline translator for travel | No roaming data needed |
| 10 | Kid-safe story generator on a family computer | You control the model and settings |

## Check yourself

1. What are the three big advantages of local AI?
**Answer:** Privacy, offline use, and no per-use cost.

2. What is the easiest way to start with local AI?
**Answer:** Install Ollama and run a small model, or install LM Studio for a friendly desktop app.

3. Roughly how much memory does a 7B model need at 4-bit quantisation?
**Answer:** About 4 to 5 GB, using the rule of about 0.6 GB per billion parameters.

4. What is a mixture-of-experts model?
**Answer:** A big model where only a few experts work on each token, so it has big-model smarts at small-model speed.

5. How do other apps use your local models?
**Answer:** Through Ollama's or LM Studio's OpenAI-compatible API on your machine, or through n8n's Ollama nodes.

## In short

- Local AI is private, offline, and free per use, and good enough for loads of everyday jobs.
- Ollama and LM Studio get you running in minutes.
- Pick models by memory first, task second. Quantisation and mixture-of-experts stretch your hardware.
- Local models speak the OpenAI-compatible API, so other apps can use them.
- Go hybrid: local for private and bulk work, frontier models for the hardest thinking.
