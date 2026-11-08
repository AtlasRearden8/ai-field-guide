# 4.25 Voice agents
<!-- original: ch. 87 -->

Voice is the most natural way to talk. You do not type. You do not click. You just speak.

Today you can build an AI that answers your phone, books appointments, runs a language lesson, or quizzes you while you drive. It sounds natural. It replies in under a second. It never gets tired.

This chapter shows you how to use voice AI today. It explains how voice agents work. It covers the platforms. It walks you through a full phone-agent build. It shows you how to write prompts for the ear. And it covers the rules for doing it responsibly.

## Use voice AI today, no building required

You do not need to build anything to start. Voice mode is already in the assistants you know.

Open ChatGPT, Gemini, or Claude on your phone. Tap the voice button. Talk. The assistant talks back. It is that simple.

Here are ten great things to do with voice mode.

1. "Be my Spanish conversation partner. I am a beginner. Speak slowly and correct me gently."
2. "Mock-interview me for this job. Be tough but kind. Give feedback after each answer."
3. Brainstorm a project on a walk, then say "summarise what we decided as a to-do list."
4. Get hands-free recipe help while you cook.
5. "Quiz me on my biology flashcards" on the commute.
6. Rehearse a hard conversation, like asking for a raise.
7. Practise a presentation and get feedback on pacing and filler words.
8. Make up a bedtime story together with your kids.
9. Get real-time help translating a conversation while travelling.
10. Ask for a guided breathing or wind-down session.

Phone assistants help too. Siri, Google Assistant, and Alexa now use newer AI models. They handle everyday requests and smart home controls. For deep conversations, a full chatbot voice mode is better.

## How voice agents work

A **voice agent** is an AI you talk to out loud, often over the phone. It has three parts: ears, a brain, and a mouth.

**Ears: speech-to-text.** This turns your spoken words into text. **STT** is short for speech-to-text. It listens and writes down what you said.

**Brain: the language model plus tools.** The model reads the text. It decides what to say. It can also use tools, such as checking a calendar or looking up an order.

**Mouth: text-to-speech.** This turns the reply back into spoken words. **TTS** is short for text-to-speech. It speaks in a natural voice.

There are two ways to build this.

**The pipeline.** Three separate models chained together: STT, then the language model, then TTS. The advantage is choice. You can pick the best model for each step. You can use any language model, such as Claude. You also get transcripts for free. The disadvantage is delay. Each step adds a little time.

**Speech-to-speech.** One model hears and speaks directly. There is no text in the middle. The advantage is speed. Replies come faster. The model also hears tone and emotion. The disadvantage is fewer choices and less control.

Latency is everything in voice. **Latency** is the delay between you speaking and the AI replying. People expect a reply in well under a second. Long pauses feel broken. Platforms handle streaming, interruptions, and turn-taking, which is why most people build on a platform instead of from scratch.

**Barge-in** means the caller can interrupt the AI mid-sentence, just like a real conversation. Good platforms handle this well. Bad ones talk over you.

## Voice agent platforms

A platform gives you the phone number, the voices, and the tool connections. You bring the instructions.

- **Vapi, Retell, and ElevenLabs Agents.** These are the no-code choices. They give you a phone number and a simple setup. Pick one of these for your first build.
- **LiveKit and Pipecat.** These are open-source choices. They give you full control. Pick one if you like to code and want to own every part.
- **ElevenLabs** is known for the most natural voices. If voice quality matters most, start there.

All of these charge by the minute for calls, plus call costs. Check the current price on each platform's own site. Each one offers free trial credit to start.

## Build: an appointment-booking phone agent

This build takes one to two hours. The goal is a phone number people can call to book a slot on your calendar.

Here is how a call flows. A caller says "Can I book a consultation Thursday?" The agent checks the calendar through a tool called `check_availability`. It finds free slots at 10:00 and 14:30. It says "I have 10 or 2:30. Which works?" The caller says "2:30, please." The agent calls `book_appointment`. The event is created. The agent says "You are booked for Thursday at 2:30. See you then!"

Follow these steps.

1. **Pick a platform.** Choose Vapi, Retell, or ElevenLabs Agents. Create an agent.
2. **Choose your models.** Pick a fast STT model, your language model such as Claude, and a warm voice.
3. **Write the system prompt.** A **system prompt** is the hidden instruction that tells the agent how to behave. Try this one:

> You are Riley, the friendly receptionist for Pixel's Plant Studio. Keep replies to one or two short sentences. Your goal is to book 30-minute plant consultations. Collect the caller's name, phone number, and preferred day and time. Use check_availability before offering times, then use book_appointment. Confirm the details back. If asked something you do not know, offer to take a message. Never make up prices. Start every call with: "Hi, this is Riley, the AI assistant at Pixel's Plant Studio."

4. **Connect the tools.** The agent needs `check_availability` and `book_appointment`. Most platforms call a webhook to reach them. A **webhook** is a message one app sends another when something happens. Point the platform at an n8n or Make workflow that talks to Google Calendar.
5. **Add knowledge.** Upload your FAQ: hours, location, and services. The agent answers common questions from this file.
6. **Buy or attach a phone number.** Call it yourself. Improve the prompt based on real calls.

The full polished version of this build is in chapter 6.10. It adds handoff to a human, post-call summaries, and a careful launch.

## Write prompts for the ear

Writing for voice is different from writing for a screen. A listener cannot re-read a sentence. They cannot see a list. They cannot click a link.

Keep replies to one or two short sentences. Ask one question at a time. Confirm details back. Say "So that is Thursday at 2:30, is that right?" before you book anything.

Never use bullet points in a voice reply. Lists do not exist in speech. Say the options as a short sentence. "I have ten o'clock or half past two. Which suits you?"

Use spoken numbers. Say "half past two," not "14:30." Use names, not codes. Say "the plant consultation," not "SKU-4421."

Give the agent a clear job. One job per agent works best. An agent that books appointments should book appointments. It should not also try to sell products and answer tax questions.

Tell the agent what to do when it does not know. "Offer to take a message" is a good default. "Say you will check and call back" is another. Never let it invent an answer.

## Test and improve

Most platforms record calls and save transcripts. A **transcript** is the written text of a call. Review ten calls a week. Note what went wrong. Update the prompt or the tools.

Test with tricky callers. Try a caller who changes their mind. Try a caller who asks an odd question. Try a caller with a strong accent. Try a caller who talks fast and interrupts.

Some platforms run simulated test calls automatically. Use them. They catch problems before real callers do.

Watch for these common failures. The agent offers a time that is already taken. The agent forgets to confirm the details. The agent talks for too long. The agent cannot hear a name correctly. Each one has a fix in the prompt or the tools.

> NOTE: Tell every caller they are talking to AI. Say it at the start of the call. "Hi, this is Riley, the AI assistant." That one sentence is honest, and in many places it is also the law. Get consent before recording a call. Follow the calling rules where you live. Never let a voice agent pretend to be a real person.

## More voice projects

Once you have built one voice agent, try these.

- A language tutor that chats with you every evening.
- A quiz master for exam revision on the drive to school.
- A check-in caller for an elderly relative, with a summary sent to you.
- A bedtime story narrator with different voices for each character.
- A meeting assistant that joins a call, takes notes, and sends a summary.

> TRY IT: Open voice mode in your favourite assistant. Say: "Be my Spanish conversation partner. I am a beginner. Speak slowly and correct me gently." Talk for five minutes. Then say: "Summarise what I did well and what I should practise." You have just used a voice agent, no building required.

## Check yourself

1. What is the main advantage of a speech-to-speech model over a pipeline?
**Answer:** Lower delay and better capture of tone and emotion, because one model hears and speaks directly.

2. Why should a voice agent not reply with bullet-point lists?
**Answer:** Lists and formatting do not exist in speech. Voice replies should be short, natural sentences.

3. What should every phone agent say at the start of a call?
**Answer:** That the caller is speaking to an AI assistant, and its name.

4. What are the three parts of a voice agent?
**Answer:** Ears (speech-to-text), brain (language model plus tools), and mouth (text-to-speech).

5. Why is latency so important in voice?
**Answer:** People expect a reply in well under a second, and long pauses feel broken.

## In short

- A voice agent has ears, a brain, and a mouth: speech-to-text, a language model, and text-to-speech.
- Pipelines offer choice; speech-to-speech models offer speed and tone.
- Build on a platform such as Vapi, Retell, or ElevenLabs Agents for your first agent.
- Write for the ear: short sentences, one question at a time, confirm details.
- Test with tricky callers and review transcripts every week.
- Always say it is AI at the start of the call, and get consent to record.
