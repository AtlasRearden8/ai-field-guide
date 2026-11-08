# 2.31 Hardware for local AI
<!-- original: ch. 79 -->

The single most important number for local AI is not your processor speed. It is memory. How much memory decides which models fit. How fast that memory is decides how quickly they talk. Once you understand those two ideas, the whole hardware world snaps into focus. Why Macs are surprisingly good. Why gamers' graphics cards are so wanted. Why a used GPU can beat a brand-new laptop.

This chapter explains it all. Then it gives you budget tiers, a buying checklist, and upgrade paths. The honest headline: start with what you own. Buy new hardware only for a specific, proven need.

## The two numbers that matter

| Number | Decides | Rule of thumb |
|---|---|---|
| Memory capacity (VRAM on a GPU, unified memory on a Mac) | Which models fit | About 0.6 GB per billion parameters at 4-bit, plus a few GB for context |
| Memory bandwidth (GB/s) | How fast it generates | Tokens per second is roughly bandwidth divided by model size in GB |

Worked example: a 14B model at 4-bit is about 9 GB. On memory with about 400 GB/s bandwidth, that is roughly 400 divided by 9, or about 40 tokens a second at best. Comfortably faster than you read. On a laptop with about 100 GB/s, it is closer to 10 tokens a second. Usable, but you will wait.

**Mixture-of-experts** models are a hardware hack. They only use a few billion parameters per token. So a "35B-A3B" model needs memory for 35B, but runs about as fast as a 3B model. If you have lots of memory but modest bandwidth, these models are your best friend.

> NOTE: Memory first, bandwidth second. A machine with more memory fits bigger models. A machine with faster memory answers quicker. Both matter, in that order.

## The hardware landscape

| Kind | Examples | Strengths | Trade-offs |
|---|---|---|---|
| Apple Silicon Macs | MacBook Pro, Mac mini, Mac Studio | Unified memory the GPU can use, quiet, efficient, huge memory options | Slower than top GPUs per GB, memory cannot be upgraded later |
| PCs with NVIDIA GPUs | GeForce RTX cards, workstation cards | Fastest tokens per second, best software support, great for image and video models too | VRAM is limited and expensive, power and noise |
| Unified-memory mini PCs | AMD Ryzen AI Max boxes, NVIDIA DGX Spark | Up to about 128 GB shared memory in a small box | Middling bandwidth, newer software support |
| Tiny boards | Raspberry Pi 5, NVIDIA Jetson | Low power, always on, cheap | Tiny models only |
| Copilot+ and NPU laptops | Laptops with neural processing units | Great battery life for built-in AI features | NPUs are rarely used by local AI tools yet |

A **GPU** is a graphics card. It is also the fastest chip for running AI. **VRAM** is the GPU's own memory. An **NPU** is a neural processing unit, a small AI chip inside some laptops. It is great for built-in features. It is rarely used by local model tools yet.

## Macs: the surprise champions

Apple Silicon Macs use **unified memory**. The CPU and GPU share one big, fast pool. That means a Mac with 64 GB can load models that would need a very expensive GPU on a PC.

| Mac memory | What fits well |
|---|---|
| 16 GB | 7 to 12B models, plus your other apps |
| 24 to 36 GB | 14 to 27B models |
| 48 to 64 GB | 30 to 35B models, including big mixture-of-experts models, with room for long context |
| 96 to 128 GB | 70B-class and about 100B or more mixture-of-experts models |
| 192 to 512 GB (Mac Studio) | The largest open models, heavily quantised |

Mac tips: Pro, Max, and Ultra chips have much higher bandwidth than base chips, so they generate faster. Use MLX builds of models for extra speed. Buy more memory than you think you need, because you cannot add it later. Apple refreshed the Mac line in late 2026, but the memory ceilings are the same, so this advice still holds.

## NVIDIA GPUs: the speed kings

| VRAM | Typical cards | What fits |
|---|---|---|
| 8 GB | Entry gaming cards | 3 to 8B models, image generation |
| 12 to 16 GB | Mid-range RTX cards | 12 to 14B models fast, most image models |
| 24 GB | High-end cards, including popular used RTX 3090s | About 30B models, big image and video models |
| 32 GB | Flagship consumer cards | 30B or more comfortably, long context |
| 48 GB or more | Two cards, or workstation cards | 70B-class models |

GPU tips: VRAM beats speed. A card with more VRAM that is a bit slower usually wins for language models. Used 24 GB cards are a classic value pick for local AI. Two GPUs can split a model, but it is more complex. Image and video generation are much happier on NVIDIA than elsewhere. Check your power supply and case size before buying a big card.

Price warning: in late 2026 a memory shortage pushed street prices far above launch prices. Treat any price in this chapter as a launch price, and check today's street price before you buy.

## Unified-memory mini PCs and budget tiers

Mini PCs built on chips like AMD's Ryzen AI Max and NVIDIA's DGX Spark offer up to about 128 GB of memory the GPU can use, in a compact box. Great for big mixture-of-experts models, always-on home AI servers, and experimenting with 70B-class models. Less great for raw speed on dense models, because bandwidth is lower than top GPUs. Check software support for your favourite tools. It is improving quickly. Prices moved a lot in 2026, so check the current price before you buy.

| Tier | Setup | You get |
|---|---|---|
| $0 | Whatever you own, plus small models, or free cloud tiers | Learning, summaries, simple automations |
| Budget | A used office mini PC or Raspberry Pi 5 as an always-on box | n8n, databases, tiny models, cloud AI for the hard stuff |
| Mid | A 16 to 24 GB GPU in an existing PC, or a Mac with 32 to 48 GB | 14 to 30B models, image generation, private coding help |
| Enthusiast | A Mac with 64 to 128 GB, a 32 GB GPU, or a 128 GB mini PC | 30 to 120B models, long contexts, a serious home lab |
| Wild | Multi-GPU rigs or a maxed-out Mac Studio | The biggest open models at home |

Cloud might be cheaper. For occasional big-model use, renting a cloud GPU by the hour or using hosted open models can cost far less than buying hardware. Buy when you will use it every day, or when privacy truly requires it.

> TRY IT: Find your computer's memory, and your GPU's VRAM if you have one. Use the 0.6 GB rule to work out the biggest model you can run. Then pull one just under that size in Ollama or LM Studio and time how many tokens per second you get. Now you know your machine's AI power level.

## The buying checklist

- **What will you run?** Chat, coding, images, video, or an always-on server?
- **Which model size do you want?** Use the 0.6 GB rule, then add 20 to 30 percent headroom.
- **Memory first.** The most VRAM or unified memory you can afford.
- **Bandwidth second.** Pro, Max, and Ultra Macs and higher-end GPUs are much faster.
- **Software support.** NVIDIA is the safest bet. Apple is excellent for language models.
- **Noise, heat, and power.** Is it going in your bedroom? Is it always on? Low idle power matters for a 24/7 home server.
- **Upgrade path.** Can you add a GPU or more storage later?
- **Try before you buy.** Test the model size you want on a cloud GPU or hosted service first.

Storage, power, and cooling matter too. Models are 2 to 80 or more GB each. A fast 1 to 2 TB SSD fills up faster than you would think. A PC wants 32 GB or more of system RAM so the rest of your computer stays happy. Big GPUs draw lots of power under load. Macs and mini PCs sip it. Sustained AI work runs hot, so good airflow means stable speeds. Use wired Ethernet for a home server, and a private network tool for remote access.

Where is hardware heading? Smarter small models: each generation packs more skill into fewer parameters, so your existing machine gets "upgraded" for free every few months. More unified memory everywhere: big shared-memory designs are spreading beyond Apple. Laptop neural processors are slowly gaining support in local AI tools. New quantisation formats keep squeezing models smaller with less quality loss.

> NOTE: Your current computer is probably enough to start. A small model on the machine you own beats a big model on a machine you have not bought yet.

## Check yourself

1. What are the two numbers that matter most for local AI hardware?
**Answer:** Memory capacity, which decides which models fit, and memory bandwidth, which decides how fast they run.

2. Roughly how much memory does a 30B model need at 4-bit quantisation?
**Answer:** About 18 GB, plus a few GB for context, so a 24 GB GPU or a 32 GB or larger Mac.

3. Why are Macs surprisingly good for local AI?
**Answer:** Unified memory lets the GPU use most of the RAM, so a Mac with lots of memory can load very large models.

4. Why is VRAM more important than raw GPU speed for language models?
**Answer:** VRAM decides which models fit at all. A slower card with more VRAM usually wins.

5. When is the cloud cheaper than buying hardware?
**Answer:** For occasional big-model use. Buy hardware when you will use it every day, or when privacy requires it.

## In short

- Memory capacity decides which models fit. Memory bandwidth decides how fast they run.
- About 0.6 GB per billion parameters at 4-bit, plus headroom for context.
- Macs shine for big models thanks to unified memory. NVIDIA GPUs shine for speed and image and video.
- Mixture-of-experts models give big-model smarts at small-model speed if you have the memory.
- Start with what you own, try big models in the cloud, and buy for daily use.
- Check today's street price before you buy. Prices moved a lot in late 2026.
