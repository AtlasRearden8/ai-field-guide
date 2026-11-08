# 1.18 A short, fun history of AI
<!-- original: ch. 34 -->

AI did not appear out of nowhere in 2022. It is a 75-year story. Big dreams. Long winters. Surprise breakthroughs. One very important research paper. Knowing the story makes today's tools less magical and more understandable. It also helps you spot hype versus real progress.

## The dreamers: 1950s to 1960s

In 1950, a British mathematician named Alan Turing asked a famous question. If you cannot tell a machine from a human in conversation, does it matter whether the machine "thinks"? He called it the imitation game. We now call it the Turing test.

In 1956, a small workshop at Dartmouth College in America gave the field its name: **artificial intelligence**. The organisers were optimistic. They thought big progress might come in a single summer. It did not.

In 1958, Frank Rosenblatt built the **Perceptron**, a tiny network inspired by brain cells. It could learn to recognise simple patterns. Newspapers got very excited. They predicted machines that would soon walk, talk, and be conscious.

In 1966, Joseph Weizenbaum built **ELIZA**, a program that imitated a therapist. It worked by simple pattern-matching. You typed "I am sad about my mother." It replied "Tell me more about your mother." People got emotionally attached to it anyway.

> NOTE: Weizenbaum was startled by this. He knew ELIZA was just shuffling words. People confided in it anyway. This is called the ELIZA effect: our tendency to see understanding where there is only pattern-matching. It is still worth remembering today.

## Winters and expert systems: 1970s to 1990s

The big promises did not come true. Funding dried up. Twice. These cold periods are called **AI winters**. The first came in the 1970s. The second came in the late 1980s.

In between, a new idea took hold: **expert systems**. These tried to capture human expertise as thousands of hand-written rules. "If the patient has a fever and a rash, then consider..." They worked in narrow areas, like configuring computers or diagnosing infections. But they were brittle. Every new case needed a new rule. They were expensive to maintain.

Quietly, the ideas that would win later kept developing. In 1986, researchers popularised **backpropagation**, a way for networks to learn from their mistakes. In 1997, a system called **LSTM** helped networks handle sequences, like sentences.

And in 1997, IBM's **Deep Blue** beat world chess champion Garry Kasparov. It won mostly through brute-force search, not learning. But it showed the world that machines could beat humans at a game of deep thought.

## The deep learning boom: 2010s

Three things came together in the 2010s: huge amounts of data from the internet, fast computer chips called **GPUs**, and better ways to train networks. The result was **deep learning**: networks with many layers, learning patterns from data at a scale never seen before.

In 2012, a system called **AlexNet** crushed an image-recognition competition, using deep networks on GPUs. The deep learning era had begun.

In 2013 and 2014, new tools arrived: **word2vec**, which turned words into meaningful numbers, and **GANs**, networks that could generate images. Speech recognition, translation, and photo search in everyday apps quietly got dramatically better.

In 2016, DeepMind's **AlphaGo** beat Go champion Lee Sedol. Go is far harder than chess. AlphaGo's famous "move 37" looked like a mistake to experts. It turned out to be brilliant. A machine had shown something like creativity.

## The Transformer changes everything: 2017

In June 2017, a Google research paper arrived with a confident title: "Attention Is All You Need". It introduced the **Transformer**.

The Transformer had three gifts.

- **Attention.** Every word can "look at" every other word to understand context. "Bank" near "river" means something different from "bank" near "money". Attention catches that.
- **Parallelism.** Unlike older models, Transformers train efficiently on GPUs at enormous scale. They can read huge piles of text fast.
- **Generality.** The same design turned out to work for text, code, images, audio, video, even protein structures.

Nearly every model in this book, including GPT, Gemini, Claude, Llama, and Qwen, is a descendant of that paper. One paper, in 2017, shaped the next decade.

> TRY IT: Ask your assistant: "Explain the Transformer to me like I am ten years old, using a cooking example." Then ask: "Now explain it using a music example." Two metaphors, same idea. That is how you test whether you really understand something.

## Scale is almost all you need: 2018 to 2022

Once the Transformer existed, labs made it bigger. More data. More computing power. More parameters. And performance kept improving, in a predictable way. This became known as **scaling laws**.

In 2018, OpenAI's **GPT-1** and Google's **BERT** showed that pre-training on lots of text, then adapting, works wonders. In 2019, **GPT-2** wrote surprisingly coherent paragraphs. Its full release was staged over misuse concerns.

In 2020, **GPT-3** arrived with 175 billion parameters. It could do new tasks from just a few examples in the prompt. In 2021, **GitHub Copilot** brought AI pair programming to millions of developers, and **DALL-E** generated images from text.

In 2022, image generation exploded: DALL-E 2, Midjourney, and the open-source Stable Diffusion. Then, on November 30, 2022, **ChatGPT** launched. It became one of the fastest-growing consumer apps in history.

The model behind the first ChatGPT was not dramatically different from what researchers already had. What changed everything was instruction tuning, human feedback, and a friendly chat box. Sometimes the interface is the innovation.

## The Cambrian explosion: 2023 to 2024

In 2023, **GPT-4** raised the bar in March. Anthropic launched **Claude**. Meta's **Llama** models kicked off an open-weight boom, so soon anyone could run capable models locally. Tool use appeared. Context windows grew from a few thousand tokens to hundreds of thousands.

In 2024, multimodal became normal: models that see, hear, and speak in real time. Claude got Artifacts for building interactive things in chat. Reasoning models that "think before answering" arrived. And in November 2024, Anthropic open-sourced the **Model Context Protocol**, the USB-C port for AI.

## The age of agents: 2025 to 2026

In January 2025, DeepSeek-R1 showed that frontier-level reasoning could be open-weight and efficient. Coding agents went mainstream: Claude Code, then agents in Cursor, VS Code, Codex, and more. Developers delegated whole features. Non-developers started vibe coding their own apps.

New frontier generations arrived from every major lab. By early November 2026, the newest were Claude Sonnet 5.5 and Opus 5.5, GPT-5.6, Gemini 3.5 Flash, and Grok 4.7, with rapid-fire updates after. Creative AI levelled up: video models generated sound and dialogue together, image models got great at editing and text, and AI music became genuinely catchy.

Agents learned to browse and click. AI browsers and computer-use agents operated websites for you. MCP became the universal standard, adopted across ChatGPT, Gemini, Copilot, IDEs, and automation tools, with an official registry and, in July 2026, a new stateless spec built for web scale.

> NOTE: Dates after November 2026 will have moved on by the time you read this. New models arrive every few months. The story stays the same, even as the names change. Check the current news if a model name matters to you.

## What history teaches you

Five lessons, from 75 years of AI.

1. **The long run is bigger than we expect.** The 1956 dream took about 70 years. It arrived faster at the end than anyone predicted.
2. **Winters follow hype.** When promises outrun results, funding and faith collapse. Be wary of anyone who promises everything.
3. **One good idea can change everything.** The Transformer was one paper. It reshaped a decade.
4. **The interface matters as much as the model.** ChatGPT won not with a new brain, but with a chat box anyone could use.
5. **You are living in the payoff era.** The tools in this book exist because of 75 years of work. You get to use them on day one.

## Check yourself

1. What did Alan Turing propose in 1950?
**Answer:** The imitation game, later called the Turing test: if you cannot tell a machine from a human in conversation, does it matter whether it "thinks"?

2. What is an AI winter?
**Answer:** A cold period when overpromising led to funding cuts, in the 1970s and again in the late 1980s.

3. What is the ELIZA effect?
**Answer:** Our tendency to see understanding where there is only pattern-matching, named after the 1966 ELIZA program.

4. What did the Transformer paper introduce in 2017?
**Answer:** A design based on attention, which lets every word look at every other word for context, and trains efficiently at huge scale.

5. Why did ChatGPT take off in 2022, if its model was not dramatically new?
**Answer:** Because of instruction tuning, human feedback, and a friendly chat box. Sometimes the interface is the innovation.

## In short

- AI is a 75-year story: early dreams, winters, a deep learning boom, the Transformer, scale, and now agents.
- The 1950s dreamers, ELIZA, Deep Blue, AlexNet, and AlphaGo are the milestones to remember.
- The Transformer paper of 2017 shaped nearly every model you will use.
- ChatGPT in 2022 made AI mainstream through a better interface, not just a better model.
- 2024 to 2026 brought multimodal models, reasoning models, open-weight models, coding agents, and MCP.
- History says: discount short-term hype, and bet on long-term change.
