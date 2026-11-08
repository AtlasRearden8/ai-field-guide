# 2.32 The AI home lab
<!-- original: ch. 80 -->

A home lab is your personal AI playground. Models, chat interfaces, automations, and databases running on hardware you control. It is private. It is free to run all day. It is one of the best ways to understand how all the pieces in this book fit together. This chapter gets you from zero to a working lab in about 15 minutes. Then it shows you how to grow it into a 24/7 private assistant with voice, search, document chat, and remote access from your phone.

A home lab runs a complete private AI setup on your own computer. Ollama runs models. Open WebUI provides a ChatGPT-style interface. n8n runs automations. One command starts all three. Nothing leaves your network.

## What's in the lab

| Service | Job | Like… |
|---|---|---|
| Ollama | Runs open models and serves an API | The engine |
| Open WebUI | ChatGPT-style interface with document chat, tools, multiple users | The dashboard |
| n8n | Automations and AI agents | The robot arms |

**Docker** is the tool that makes this easy. It runs each service in a sealed container, so they do not fight each other. You write one small file, called a compose file, that lists the services. One command starts them all. First run downloads a few gigabytes. Then you pull a model and chat.

On a Mac, run Ollama natively instead of in Docker. Docker cannot use the Mac GPU. For much faster models, install Ollama from its website, remove the Ollama service from the compose file, and point the other services at your Mac's Ollama address. Stuck? Open a coding agent in the lab folder and say, "Get this running on my machine and fix whatever is wrong." It will read the error messages for you.

> NOTE: A home lab is a playground, not a production system. Keep it simple at first. Add one service at a time.

## Wire everything together

| Connection | How |
|---|---|
| n8n to Ollama | Add an Ollama credential with the local address. Containers reach each other by service name. |
| Open WebUI to Claude | In settings, add an Anthropic API key for the hard jobs |
| Open WebUI to documents | Upload files to its Knowledge area, then chat with them. Built-in document search. |
| n8n to Claude | Use an Anthropic credential for hard jobs, Ollama for private and bulk ones |
| Claude Code to lab | Point MCP servers or scripts at your local services |

The pattern is hybrid. Local models for private and bulk work. Cloud models for the hardest thinking. All in one interface. Once the wiring works, the lab feels like a private cloud that belongs to you.

## Level-ups for your lab

| Add | Why | How |
|---|---|---|
| Tailscale | Reach your lab securely from your phone, anywhere | Install on the host and phone. No port-forwarding. |
| Postgres with pgvector | A real database and vector store for document search | Add a database service |
| Qdrant | A dedicated vector database | Add a service |
| Whisper speech-to-text | Transcribe voice memos locally | A transcription server container |
| Local text-to-speech | Give your assistant a voice | A voice container, then enable it in Open WebUI |
| SearXNG | Private web search for Open WebUI and agents | Add a container, enable web search |
| ComfyUI | Local image generation, NVIDIA recommended | A container |
| Home Assistant | Smart home plus AI, with its own MCP server | Separate install, then connect |
| Uptime Kuma | Watches that everything is running | One container, alerts to your phone |
| Cloudflare Tunnel | Expose specific webhooks publicly, safely | For webhooks from outside services |

Let AI do the plumbing. Ask a coding agent to add a database, a vector store, and a transcription server to your compose file, wire n8n to the database, and update the readme. That is a real task, and it works.

> TRY IT: Get the base lab running. Then do project one below with a document you would never upload to a cloud service. Feeling the privacy of local AI firsthand is a great "aha" moment.

## Eight home lab projects

1. **Private document chat.** Upload manuals, notes, or tax docs to Open WebUI's Knowledge area. Chat with them. Nothing leaves your machine.
2. **Local voice journal.** A phone shortcut sends a voice memo to n8n. Local transcription turns it into text. A local model summarises and tags it. The result lands in your notes vault. Your diary never touches the cloud.
3. **The hybrid assistant.** In Open WebUI, add local models and a cloud API key. Use local for private or quick stuff. Use cloud for hard thinking. All in one interface.
4. **The 24/7 automation box.** Move n8n to an always-on mini PC or Raspberry Pi. Run morning digests, idea inboxes, and price trackers without leaving your laptop on.
5. **Model tasting night.** Pull three or four models. Use Open WebUI's side-by-side mode to run the same ten prompts. Score them blind. You will develop real intuition for model differences.
6. **Family AI, safely.** Create Open WebUI accounts for family members with a friendly, age-appropriate system prompt and a small model. Homework help that you control.
7. **Photo library tagger.** A local vision model plus a batch job captions and tags thousands of photos. Search "birthday cake 2024" later.
8. **Private search engine.** SearXNG plus Open WebUI web search gives you a research assistant that does not log your queries.

## Security basics

| Rule | Why |
|---|---|
| Keep services on localhost or a private network | Never expose them raw to the internet |
| Strong passwords for Open WebUI admin and the n8n owner | These control your data and credentials |
| Keep images updated | Security fixes arrive often |
| Expose only specific webhooks, with HTTPS, login, and a tunnel | Minimal attack surface |
| Separate accounts for family members | Everyone gets their own chats and permissions |
| Do not store API keys in compose files you share | Use a settings file that stays out of version control |

Open ports get found fast. Bots scan the internet constantly. An exposed n8n or Ollama without a login can be found and abused within hours. A private network tool is the easy, safe way to reach your lab remotely. Do not use port-forwarding. Port-forwarding opens a door from the internet straight to your service. A private network opens a door only to your devices.

> NOTE: Your lab holds your workflows and credentials. Back it up like it matters, because it does.

## Maintenance cheat sheet

Check what is running. Watch the logs. Update all services. List installed models. Remove models to free disk space. Check what is using disk. Back up the Docker volumes, or use folders you already back up. The n8n data volume matters most, because it holds your workflows and credentials. Ask your agent: "Write a nightly backup script for these Docker volumes to my external drive."

## A lab growth plan

| Week | Add | You can now… |
|---|---|---|
| 1 | The base lab plus one model | Chat privately, chat with documents |
| 2 | Private remote access | Use your lab from your phone anywhere |
| 3 | Voice transcription plus a voice-journal workflow | Talk to your notes |
| 4 | A vector database plus a document-search bot | Ask questions of your whole document archive |

One week at a time. One addition at a time. A lab that grows slowly stays working. A lab built all at once breaks in ways that are hard to untangle.

## Check yourself

1. What are the three core services in the home lab?
**Answer:** Ollama runs models, Open WebUI provides the chat interface, and n8n runs automations.

2. Why should Ollama run natively on a Mac instead of in Docker?
**Answer:** Docker cannot use the Mac GPU, so native Ollama is much faster for models.

3. How do containers reach each other in the lab?
**Answer:** By service name, such as the local address for Ollama.

4. What is the safe way to reach your lab from your phone?
**Answer:** A private network tool, not port-forwarding.

5. What should you back up first in your lab?
**Answer:** The n8n data volume, because it holds your workflows and credentials.

## In short

- One command gives you Ollama, Open WebUI, and n8n.
- On a Mac, run Ollama natively for GPU speed.
- A private network gives safe remote access. Never expose services raw.
- Level up with vector databases, transcription, private search, and image generation.
- Go hybrid: local for private and bulk, cloud models for the hardest thinking.
- Back up your lab, especially the n8n data.
