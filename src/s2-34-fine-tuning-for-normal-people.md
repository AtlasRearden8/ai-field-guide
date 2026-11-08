# 2.34 Fine-tuning for normal people
<!-- original: ch. 82 -->

**Fine-tuning** means taking an existing model and training it a little more on your own examples. It picks up your style, format, or specialty. It sounds like a PhD-only activity. But tools like Unsloth, MLX, and LoRA have made it a weekend project on free or cheap hardware. This chapter explains when fine-tuning is worth it, and when it is not. How LoRA works, in plain English. How to prepare data. A step-by-step walkthrough. And how to run your custom model in Ollama.

Fine-tuning does not teach the model everything from scratch. It adjusts how it responds, based on hundreds of examples of what you want. It is for behaviour, not knowledge. That distinction decides everything in this chapter.

## Do you actually need fine-tuning?

| You want the model to… | Best tool | Why |
|---|---|---|
| Follow instructions or a format | Prompting plus examples | Instant, free, easy to change |
| Know facts from your documents | Document search or long context | Facts change; fine-tuning is bad at memorising facts |
| Remember you | Memory | Built for exactly this |
| Nail a consistent style, tone, or format every time | Fine-tuning | Learned behaviour, no long prompt needed |
| Make a small model do one job as well as a big one | Fine-tuning | Cheaper, faster, runs locally |
| Handle a niche task with your labels and jargon | Fine-tuning | Learns patterns from many examples |
| Speak in a character's voice for a game | Fine-tuning, or prompting | Consistent personality |

The golden rule: try prompting first. Then document search. Fine-tune last. If a great prompt with examples gets you 90 percent there, you probably do not need it. Fine-tuning is for behaviour: style, format, skill. Not knowledge.

> NOTE: Fine-tuning will not teach a model your price list. Prices change. Facts belong in documents, not in weights.

## How fine-tuning works: LoRA in plain English

| Method | What changes | Needs |
|---|---|---|
| Full fine-tuning | Every parameter in the model | Lots of GPU memory and expertise |
| LoRA (Low-Rank Adaptation) | Small "adapter" matrices added alongside the model; the original stays frozen | A fraction of the memory |
| QLoRA | LoRA on a quantised, compressed model | Fits bigger models on consumer GPUs |

Picture it like this. The base model is frozen, like a printed book. The LoRA adapter is a thin overlay, like sticky notes on the pages. The overlay is often only tens of megabytes. You can keep one base model and swap adapters: "email voice," "support tone," "pirate mode." Each adapter is small, cheap, and easy to share.

## Step one: prepare your data

Data is the part that matters most. Fine-tuning data is usually example conversations in **JSONL**. That is one JSON object per line. Each example has a system message, a user message, and an assistant reply. For example, a product-description task: the system says "You write product descriptions for Cozy Candles." The user gives the product facts. The assistant gives the finished description in the house style.

| Guideline | Why |
|---|---|
| Quality over quantity | 200 excellent examples beat 5,000 sloppy ones |
| Start with 100 to 1,000 examples | Enough to learn a style or format |
| Cover the variety you expect | Short and long, easy and weird inputs |
| Consistent format | The model copies whatever patterns you show it, including mistakes |
| Hold out 10 to 20 percent for testing | Check it on examples it did not train on |
| Remove private info | Models can memorise and repeat training data |

Let a big model help build the dataset. Write 20 perfect examples yourself. Then ask Claude to generate 300 more in exactly this style, varied in length and topic. Review a sample carefully. Using a big model to teach a small one is called **distillation**. Check the big model's terms of use first. Some providers restrict using outputs to train other models.

> TRY IT: Write 20 examples of a fun style: your texting voice, a pirate, a haiku bot. Ask Claude to expand them to 200. You have just built a training dataset.

## Step two: pick your tool

| Tool | Where | Why pick it |
|---|---|---|
| Unsloth | Free Google Colab or Kaggle notebooks, or your NVIDIA GPU | Fast, memory-efficient, beginner-friendly notebooks |
| MLX-LM | Apple Silicon Macs | LoRA fine-tuning on your Mac with one command |
| Axolotl, LLaMA-Factory | Your GPU or a rented one | Config-driven, powerful, lots of options |
| Hugging Face tools | Anywhere | The ecosystem everything builds on |
| Hosted fine-tuning | Providers like OpenAI, Google Vertex AI, Together, Fireworks | Upload your file, click train, get an API model |
| Rented GPUs | RunPod, Lambda, Modal, Vast.ai, and others | Bigger models for a few dollars an hour |

Unsloth on a free Colab notebook is the easiest start. MLX on a Mac is the easiest start if you own a Mac. Hosted fine-tuning is the easiest start if you never want to touch a GPU. Pick one path. Do not compare all of them for a week.

## Step three: train

The walkthrough is short. Prepare your data as two files: one for training, one for testing. Pick a small model. Run the training command. On a Mac with MLX, it is one command with the model name, the data folder, and the number of training rounds. On Colab with Unsloth, you open a notebook, fill in your data, and run the cells. Ask a coding agent to walk you through fusing the adapter and exporting it. "Fusing" means merging the adapter into the model file.

Key settings, with the defaults usually fine:

| Setting | Meaning | Starting point |
|---|---|---|
| Epochs | How many times it sees your data | 1 to 3; too many means overfitting |
| Learning rate | How big each adjustment is | The tool's default |
| LoRA rank | Size of the adapter | 8 to 32 |
| Max length | Longest example it handles | Fit your longest example |

**Overfitting** means the model memorised your examples instead of learning the pattern. It repeats training data instead of generalising. Too many epochs or too little variety causes it. Use fewer epochs, more varied examples, and a held-out test set.

## Step four: evaluate honestly

Compare your fine-tuned model against the base model with a good prompt. Same test set. Same scoring. If the base model with a good prompt is just as good, keep the prompt. It is cheaper, simpler, and easier to change. Fine-tuning earns its keep only when it clearly wins. Measure accuracy, style consistency, and cost per task. Do not trust a feeling. Trust a scorecard.

## Step five: run it in Ollama

Export your model to GGUF format. Write a short Modelfile: the model file, a system prompt describing the style, and a temperature setting. **Temperature** controls creativity. Low means focused. High means varied. Then create the model in Ollama and run it. Now n8n, Open WebUI, and your scripts can all use your custom model like any other model. That is the payoff: your style, on your machine, in every tool.

## Fine-tuning beyond text

| Kind | What you train | Example |
|---|---|---|
| Image LoRAs | A style, character, product, or pet | 20 photos of your dog, then "my dog as an astronaut" |
| Voice models | A voice, with consent | Your own voice for narrating your videos |
| Classifiers and embedders | Labels or similarity for your domain | Tag support tickets your way |

Consent and rights matter. Only train on data you have the right to use. Never train on someone's face, voice, or art without their permission. Respect artists' and authors' wishes.

## Fun fine-tuning projects

| Project | Examples needed |
|---|---|
| Your email voice in a small local model | 200 of your sent emails, cleaned of private info |
| Product-description writer for a small shop | 150 great descriptions |
| Support-ticket tagger with your categories | 500 labelled tickets |
| A game character with a consistent personality | 300 in-character dialogues |
| Receipt-to-JSON extractor that always nails your format | 200 receipts plus target JSON |
| Pet image LoRA | 15 to 30 good photos |
| Plain-language explainer that always avoids jargon | 300 question-to-answer pairs |
| Family recipe rewriter in grandma's voice | 100 recipes in her style |

> NOTE: Start with the smallest project on the list. A pet image LoRA or a haiku bot teaches you the whole loop in an afternoon.

## Check yourself

1. When should you fine-tune, and when should you use document search instead?
**Answer:** Fine-tune for behaviour like style and format. Use document search for facts, because facts change and fine-tuning is bad at memorising them.

2. What is LoRA, in plain words?
**Answer:** It trains only a small adapter while the base model stays frozen, so it needs far less memory and the result is small and swappable.

3. How many examples do you need to start?
**Answer:** 100 to 1,000 excellent, varied examples, with 10 to 20 percent held out for testing.

4. What is overfitting?
**Answer:** The model memorised your examples instead of learning the pattern, usually from too many epochs or too little variety.

5. How do you know if fine-tuning was worth it?
**Answer:** Compare the fine-tuned model against the base model with a good prompt on the same test set. Keep the prompt if it is just as good.

## In short

- Fine-tune for behaviour, like style, format, and niche skills, not knowledge.
- Try prompting first, then document search, then fine-tuning.
- LoRA and QLoRA make it cheap: a tiny adapter on a frozen base model.
- Data quality is everything: 100 to 1,000 excellent, varied examples, with a held-out test set.
- Evaluate against a well-prompted base model, then export and run it in Ollama.
- Only train on data you have the right to use, and always get consent for faces and voices.
