# 6.8 Build-along: the private home assistant
<!-- original: ch. 117 -->

In this build you will create an AI assistant for your whole household that never sends a word to the cloud. Family members get their own accounts. It answers questions about your household documents: manuals, recipes, school info. It can listen and talk. It is reachable from everyone's phone. It can optionally control your smart home.

It is the Home Lab, turned into something the whole family truly uses.

Time: about three hours. Level: intermediate, copy-paste friendly.

## What you will build

A home assistant that runs on a computer in your house. It has a chat page the family opens in a browser. It knows your household documents. It speaks and listens. Each family member has an account, so it can keep things separate.

Nothing leaves your house. Your family's data stays at home.

## Before you start

You need four things.

- **A computer that can stay on.** 16 GB of memory or more is ideal. A small home server or a spare desktop works well.
- **Docker.** **Docker** is a tool that runs programs in neat, sealed boxes called containers. It makes setup repeatable.
- **The homelab starter kit**, downloaded from the book's kit page. No account is needed.
- Optionally, **Home Assistant**, if you want smart home control.

Pick a spot for the computer. It needs power, internet, and airflow. A cupboard with no air is a bad home. A shelf near your router is a good one.

## Step 1: start the lab, 20 minutes

Open a terminal on the home computer. Go to the starter kit folder. Start the lab with Docker.

```
docker compose up -d
```

Line by line: `docker compose` runs a set of programs defined in the kit. `up` starts them. `-d` means run in the background, so you can close the terminal. The first start downloads the programs. It takes a few minutes.

Check that the lab is running. Open the chat page in your browser. You should see a welcome screen. If it fails, read the Docker logs. The error usually names the missing piece.

Download a model. Pick a small one first, such as a 7 or 8 billion parameter model. A **parameter** is a number the model learned during training. More parameters usually means a smarter model, and a slower one. A small model runs well on a home computer. A big model may be too slow. You can upgrade later.

## Step 2: family accounts and a house personality, 20 minutes

Create an account for each family member. Give each person a name and a password. Test each login. A child who cannot log in will not use the assistant.

Give the assistant a house personality. Write a short system prompt. A **system prompt** is the hidden instruction that tells the assistant how to behave. Try this:

> You are the house assistant for the Harper family. You are warm, patient, and clear. You help with homework, recipes, manuals, and schedules. You explain things simply. You never share one family member's private notes with another. If you do not know something, say so.

Keep the personality short. A short prompt is a prompt the model follows. A long prompt is a prompt it forgets.

## Step 3: the household knowledge base, 30 minutes

A **knowledge base** is a set of documents the assistant can read before it answers. This is what makes it a home assistant, not just a chatbot.

Gather your household documents. Manuals for appliances. School term dates. Recipes. The Wi-Fi password note. The bin collection schedule. The plumber's number. Scan paper documents with your phone if you need to.

Put them in the kit's documents folder. The lab reads them, splits them into chunks, and indexes them. When someone asks a question, the assistant finds the relevant chunks and answers from them, with a link to the source.

Test it with real questions. "How do I descale the coffee machine?" "When does the school term end?" "What is the Wi-Fi password?" If an answer is wrong, check the source document. The assistant can only be as good as the documents you feed it.

Keep private notes separate. A diary or a health note should not go in the shared knowledge base. Give each person a private folder the assistant only reads for them.

## Step 4: voice, 20 minutes

Turn on voice chat. The lab includes speech-to-text and text-to-speech. **Speech-to-text** turns spoken words into text. **Text-to-speech** turns text back into spoken words.

Test it on your phone. Ask a question out loud. Listen to the answer. Voice is how kids and grandparents will use the assistant most. If voice is hard to use, they will not use it at all.

Pick a calm, clear voice. A fast voice is hard to follow in a kitchen. A slow voice is boring. Test two voices and let the family vote.

## Step 5: reach it from every phone, privately, 20 minutes

Your family needs to reach the assistant from their phones, even away from home. Do it privately with Tailscale. **Tailscale** is a tool that connects your devices in a private network, as if they were all at home.

Install Tailscale on the home computer and on each phone. Log in with the same account. Now each phone can open the assistant's page through the private network. No ports are open to the public internet. No one outside your family can reach it.

Test it. Turn off your phone's Wi-Fi. Open the assistant over mobile data through Tailscale. If it loads, your private network works.

## Step 6, optional: smart home with Home Assistant

If you have Home Assistant, connect it. **Home Assistant** is a free program that controls smart home devices: lights, plugs, thermostats, and sensors.

Connect it to the lab. Give the assistant a few safe tools: turn lights on and off, check the temperature, and lock the door. Do not give it tools that can cause harm, such as opening the garage or turning off the heating in winter.

Test each tool with a family member watching. "Turn the kitchen lights on." Watch the lights. If it works, add one more tool. If it fails, check the Home Assistant logs.

Keep safety jobs local and simple. A light switch can be smart. A smoke alarm should stay dumb and reliable.

## Keeping it healthy

A home assistant needs a little care each month.

- **Update the model.** Try a new model every few months. Keep the old one until the new one proves itself.
- **Update the documents.** Add new manuals. Remove old ones. A knowledge base with stale documents gives stale answers.
- **Check the disk.** Models and documents take space. Delete models you no longer use.
- **Check the backups.** Back up the documents folder and the settings every month. A backup means a dead hard drive is an annoyance, not a disaster.
- **Ask the family.** What do they use it for? What do they wish it could do? Build the top request next.

> NOTE: Private does not mean unguarded. Family accounts still need real passwords. The computer still needs updates. Tailscale still needs care. A private system that no one maintains becomes a fragile system.

## Troubleshooting

- **The lab does not start.** Read the Docker logs. The error usually names the missing piece: a port in use, a missing folder, or too little memory.
- **The model is too slow.** Use a smaller model. Close other programs. Add more memory if you can.
- **Answers are wrong.** Check the source documents. Add the missing document. Remove a document that contradicts the right one.
- **A phone cannot connect.** Check Tailscale is running on both the phone and the home computer. Check they are on the same Tailscale account.
- **Voice does not work.** Check the microphone permission in the browser. Test with a wired headset first.

> TRY IT: Gather five household documents today and add them to the knowledge base. Ask the assistant three questions about them. If it answers two well, your home assistant is already useful. Add five more documents tomorrow.

## Check yourself

1. Why should the assistant run on a computer in your home?
**Answer:** So your family's data never leaves your house, and the assistant works even if a cloud service fails.

2. What is a knowledge base?
**Answer:** A set of your own documents the assistant reads before it answers, so it answers from your household's facts.

3. Why use Tailscale to reach the assistant from phones?
**Answer:** Because it connects your devices in a private network, with no ports open to the public internet.

4. What should you never give a home assistant control over?
**Answer:** Tools that can cause harm, such as opening the garage or turning off heating in winter.

## In short

- Start the lab with Docker and download a small model first.
- Create a family account for each person and a short house personality.
- Build a knowledge base from real household documents.
- Turn on voice, and reach the assistant privately with Tailscale.
- Add Home Assistant carefully, with safe tools only.
- Keep it healthy: update models, refresh documents, and back up monthly.
