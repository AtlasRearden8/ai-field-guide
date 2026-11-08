# 6.10 Build-along: an AI voice receptionist
<!-- original: ch. 119 -->

This is the grand finale. A friendly AI receptionist answers a real phone number, answers questions, checks your calendar, books appointments, and sends you a summary of every call.

You will write a system prompt for the ear, connect two tested tools, test it with tricky calls, add a human handoff and post-call summaries, and launch it with care.

Perfect for a small business, a side hustle, or just the coolest party trick you will ever show your friends.

Time: a weekend. Level: intermediate to advanced.

## What you will build

A phone number people can call. An AI answers. It says who it is. It answers common questions from your FAQ. It checks your calendar. It books appointments. It takes messages. After each call, it sends you a summary.

It can also hand the caller to a real person when needed. A **handoff** is passing the call to a human. The AI says "Let me connect you," and the call moves to your phone.

## Before you start

You need five things.

- **A voice-agent platform account.** Vapi, Retell, or ElevenLabs Agents. All charge by the minute, roughly $0.05 to $0.08 a minute plus call costs, and each offers free trial credit. Check the current price on the platform's own site.
- **n8n with a public web address.** Your calendar tools live in n8n. The platform calls them by webhook.
- **Google Calendar.** For checking and booking appointments.
- **An LLM key.** For the language model behind the agent.
- **A phone number.** You can buy one from the platform, or attach one you already own.

Set a spending cap on the platform and on your LLM account before you start. A phone agent that runs all day can spend money all day.

## Step 1: import and test the tools, 30 minutes

Your agent needs two tools. Both live in n8n as webhooks. A **webhook** is a message one app sends another when something happens.

- **check_availability.** Takes a day and returns free slots. It reads Google Calendar and returns the open times.
- **book_appointment.** Takes a name, a phone number, a day, and a time. It creates the calendar event and returns a confirmation.

Import the voice-receptionist workflow from the book's kit. Test each tool by hand in n8n. Send a test webhook for Thursday. Check that the free slots come back right. Send a test booking. Check that the event appears in Google Calendar. Delete the test event.

Do not connect the tools to the agent until they work by hand. A tool that fails by hand will fail on a live call, in front of a real customer.

## Step 2: create the voice agent, 30 minutes

Create an agent in your platform. Pick a fast speech-to-text model, your language model, and a warm voice. Pick a voice that sounds like your business: friendly for a café, calm for a clinic, bright for a studio.

Write the system prompt. A **system prompt** is the hidden instruction that tells the agent how to behave. Write it for the ear, not the eye. Short sentences. One question at a time. No lists. No bullet points. No links.

Try this one:

> You are Riley, the friendly AI receptionist for Pixel's Plant Studio. Start every call with: "Hi, this is Riley, the AI assistant at Pixel's Plant Studio. How can I help?"
> Keep replies to one or two short sentences. Your goal is to answer questions and book 30-minute plant consultations. Collect the caller's name, phone number, and preferred day and time. Use check_availability before offering times. Use book_appointment after the caller confirms. Confirm the details back before you book. If asked something you do not know, offer to take a message. Never make up prices, hours, or availability. If the caller asks for a person, say "Of course, let me connect you" and hand the call over.

Upload your FAQ as knowledge: hours, location, services, and prices. The agent answers common questions from this file instead of guessing.

## Step 3: connect the tools, 30 minutes

Point the agent's tools at your n8n webhook URLs. Test the connection from the platform. Call the tool once from the platform's test panel. Check that n8n receives it and returns the right answer.

Buy or attach a phone number. Point it at your agent. Call the number yourself. Book an appointment. Check that the event appears in your calendar. Cancel it. Call again and ask a question from the FAQ. Check the answer is right.

If the agent talks too long, shorten the prompt. If it offers times that are taken, check the calendar tool. If it cannot hear names, ask it to spell them back. "Could you spell your name for me, please?"

## Step 4: test with tricky calls, 30 minutes

Real callers are not polite test scripts. Test with the hard ones.

- **The changer.** A caller who picks a time, then changes their mind twice.
- **The rambler.** A caller who tells a long story before asking a question.
- **The interrupter.** A caller who talks over the agent mid-sentence.
- **The odd question.** "Do you sell cacti that glow in the dark?"
- **The angry caller.** "I have been waiting three weeks for my order!"
- **The mumbler.** A caller with a strong accent or a bad connection.

After each test, read the transcript. A **transcript** is the written text of a call. Note what went wrong. Fix the prompt or the tools. Test again. Five tricky calls teach you more than fifty easy ones.

## Step 5: human handoff and messages, 30 minutes

Add a handoff. When a caller asks for a person, or when the agent cannot help, the call moves to your phone. Test it. Call the agent, ask for a person, and check that your phone rings.

Add message-taking. When the agent cannot answer, it takes a message: name, number, and reason. It sends the message to you by email or chat. Test it. Leave a message. Check that it arrives with the right details.

Add a rule: the agent never argues, never guesses, and never keeps a caller on the line when a human is needed. A fast handoff is a good handoff.

## Step 6: post-call summaries, 30 minutes

After each call, the agent should send you a summary. Add a workflow in n8n that runs when a call ends. It reads the transcript, asks AI for a short summary, and sends it to you.

A good summary has five lines: caller name and number, reason for the call, what was booked or decided, any message left, and anything that needs a follow-up. You read it in ten seconds and know what happened.

Store the summaries in Notion if you use it. A Calls database with the date, the caller, and the outcome becomes a record of your business. You can search it later. "Who called about the big plant last month?"

## Step 7: go live responsibly, 30 minutes

Launch with care. Do this checklist before you share the number.

- [ ] The agent says it is AI at the start of every call.
- [ ] You have consent to record calls, and you follow the calling rules where you live.
- [ ] The agent never makes up prices, hours, or availability.
- [ ] Handoff to a human works, and you tested it.
- [ ] Post-call summaries arrive and are correct.
- [ ] Spending caps are set on the platform and the LLM account.
- [ ] You tested with at least five tricky callers.
- [ ] The FAQ is up to date and the agent uses it.

Start with a soft launch. Give the number to three friends. Let them call it. Fix what breaks. Then put the number on your website and your business cards.

Tell your team the number exists. Tell them what it can do. Tell them how to take over a call. A receptionist no one knows about is a receptionist no one uses.

> NOTE: Say it is AI on every call. "Hi, this is Riley, the AI assistant." That one sentence is honest, and in many places it is also the law. Never let a voice agent pretend to be a real person. Get consent before recording a call. Follow the calling rules where you live.

## Level-ups

- **Reminders.** After booking, send the caller a text reminder the day before.
- **After-hours mode.** Outside business hours, the agent takes messages only and does not book.
- **Languages.** Add a second language. The agent asks which language the caller prefers, then switches.
- **Reviews.** After a visit, the agent calls the customer and asks for a short review.

## Troubleshooting

- **Callers cannot hear the agent.** Check the voice settings and the call quality. Try a different voice.
- **The agent books the wrong time.** Check the calendar tool and the time zone. Time zones cause more booking errors than any other bug.
- **The agent talks over callers.** Turn on barge-in handling in the platform. **Barge-in** means the caller can interrupt the AI mid-sentence.
- **Costs spike.** Check the call logs. Long calls cost more. Add a polite time limit for calls that go nowhere.
- **Transcripts are wrong.** Names and numbers are the hardest part of speech recognition. Ask the agent to spell back names and repeat numbers.

> TRY IT: Call your agent right now and play the tricky caller. Change your mind twice. Ask an odd question. Interrupt it mid-sentence. Then read the transcript. Every failure you find in a test is a failure a real customer never sees.

## Check yourself

1. What should the agent say at the start of every call?
**Answer:** That it is an AI assistant, and its name.

2. Why should you test the calendar tools by hand before connecting them?
**Answer:** Because a tool that fails by hand will fail on a live call, in front of a real customer.

3. What is a handoff?
**Answer:** Passing the call to a real person when the caller asks for one or the agent cannot help.

4. What should a post-call summary include?
**Answer:** Caller name and number, reason for the call, what was booked or decided, any message left, and follow-ups needed.

## In short

- Import and test the calendar tools by hand before you connect them.
- Write a system prompt for the ear: short sentences, one question at a time.
- Connect the tools, buy a number, and call it yourself.
- Test with tricky callers and fix what the transcripts show.
- Add handoff, message-taking, and post-call summaries.
- Launch responsibly: disclose the AI, get consent, cap spending, and soft-launch first.
