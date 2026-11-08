# 4.6 Phone and desktop automation
<!-- original: ch. 50 -->

The most personal automations do not live in the cloud. They live in your pocket and on your desk. One tap, one voice command, or one keyboard shortcut can send AI your thoughts, your photos, or your clipboard, and get something useful back in seconds.

This chapter covers the tools that already live on your devices. Apple Shortcuts on iPhone and Mac. Tasker and Gemini on Android. Raycast and Power Automate on desktop. A few terminal tricks for people who like the command line. And text expanders, the quiet superpower nobody talks about.

## Why device automation is a superpower

Cloud tools are strong, but they have a weakness. They run far away, on someone else's computer. Your phone is always with you. It has your camera, your microphone, your location, and your clipboard. An automation that lives on your phone can use all of that, at once, with one tap.

Device automations are also fast. There is no website to open. There is no form to fill in. You press a button on your home screen, you speak, and the job is done.

The best device automations share three traits. They start with one tap or one voice command. They do one small job well. And they give you the answer where you already are, on your phone or your computer.

## Apple Shortcuts and AI

**Shortcuts** is Apple's automation app. It comes free on every iPhone, iPad, and Mac. A shortcut is a small list of actions, joined in order. You can run one from your home screen, from a widget, from Siri, or on its own when something happens.

Recent versions of iOS add AI to Shortcuts. There is an action called **Use Model**, which sends text to an on-device AI model, or to a larger model when you allow it. That means a shortcut can read, summarise, rewrite, or answer, without leaving your phone.

Here is a simple example. Make a shortcut called "Tidy my thought". It has three actions. First, **Dictate Text**, which records what you say. Second, **Use Model**, with a prompt like "Turn this ramble into three tidy bullet points." Third, **Show Result**, which displays the bullets on screen. Now you can speak a messy idea while walking, and get tidy notes back in seconds.

Shortcuts can also talk to the wider world. The **Get Contents of URL** action can send a web request to any address, including a webhook. That is how one tap on your phone can start an automation in n8n or Zapier. Chapter 4.2 explained webhooks. This is where they shine.

> NOTE: On-device AI keeps your words on your phone. That is the private choice. If a shortcut sends your text to a larger cloud model, that text leaves your phone. Check the setting, and choose on-device when the text is private.

## Five Shortcuts recipes to build today

1. **Voice note to tidy list.** Dictate, send to the model, show the result. Use it for ideas on the move.
2. **Receipt to log.** Take a photo of a receipt. Send the photo to the AI. Ask it to pull out the shop, the date, and the total. Save the answer to a note.
3. **Clipboard summariser.** Take whatever is on your clipboard. Ask the AI for a three-line summary. Show it on screen. Perfect for long articles you copied.
4. **Meeting prep.** Ask for the name of a meeting. Let the shortcut search your notes for that name, and show what it finds. Walk in prepared.
5. **Photo to alt text.** Take a photo. Ask the AI to describe it in one sentence. Save the description with the photo. Helpful, and a kind habit for sharing.

Build one of these today. Each takes about ten minutes. Each one teaches you a new action. After five of them, Shortcuts will feel like a second language.

## Personal automations: triggers that fire on their own

Shortcuts can also run by themselves. These are called **personal automations**. They fire when something happens on your phone: you arrive home, you connect to your car, the battery drops below 20 percent, or it is 8 in the morning.

A few useful ones: when you arrive at work, show today's calendar. When you connect to your car's Bluetooth, start your driving playlist and read out your first meeting. When the battery drops low, switch on low power mode and send yourself a note to charge.

Be careful with personal automations that send messages or share your location. A trigger that fires on its own can surprise you. Test each one for a week before you trust it.

## Mac: Shortcuts, Raycast, and more

Your Mac runs Shortcuts too, and the same shortcuts often work on both devices. But the Mac has extra tools worth knowing.

**Raycast** is a launcher. You press a keys, type a few letters, and run anything: open an app, search your files, run a shortcut, or ask AI a question. It replaces the slow hunt through menus with a fast keyboard flow. Its AI features can summarise text, draft replies, and search your apps. It is free to start, with a paid plan for the deeper AI features, so check the current price.

**Alfred** is an older launcher with the same spirit, and a loyal following. **Keyboard Maestro** is a deeper automation tool for people who want to automate almost anything on a Mac, from moving windows to filling in forms. **Hazel** watches folders and acts on files: it can rename photos, file receipts, and clean up your downloads by itself.

Pick one launcher. Learn its ten most useful commands. That is enough. The rest is decoration.

## Windows: Power Automate, AutoHotkey, and Copilot

Windows has its own set of tools. **Power Automate** is Microsoft's automation tool. It comes with many Windows computers, and it connects to Microsoft apps like Outlook, Excel, and Teams. If your work lives in Microsoft tools, Power Automate is the natural first choice. It has AI features that can read documents, draft replies, and sort email.

**AutoHotkey** is a free tool for keyboard lovers. It lets you turn any keys into a shortcut. Press one combination, and it types a whole paragraph, opens a program, or runs a small script. It takes a little learning, but it is very powerful. People who use it often say it saves them an hour a day.

**Copilot** is built into Windows and Microsoft apps. You can ask it to summarise a document, draft an email, or explain a spreadsheet. It is not a full automation tool, but it is a fast helper that is always one click away.

## Terminal lovers

A **terminal** is a window where you type commands to your computer, instead of clicking. It sounds old-fashioned. It is also one of the fastest ways to automate small jobs, on Mac, Windows, or Linux.

You do not need to learn the terminal to use this book. But if you are curious, here is the smallest useful trick. Most AI coding tools, like Claude Code, live in the terminal. They can write small scripts for you. Ask one to write a script that renames all the photos in a folder by date. It will write it, explain it, and run it. You just learned the terminal, by asking.

> TRY IT: Open the terminal on your computer. Type `echo hello` and press Enter. You should see the word hello printed back. That is your first command. Now ask your favourite AI assistant: "Write me a tiny terminal command that lists the files on my Desktop, and explain each part." Run what it gives you. You are now a terminal user.

## Text expanders and AI

A **text expander** is a tool that turns a short code into a longer piece of text. You type `;sig`, and it types your full email signature. You type `;addr`, and it types your address. That alone saves minutes every day.

Add AI, and it gets better. Some expanders can now rewrite what you typed as you type it. Type a rough email, press a keys, and the expander rewrites it in a friendlier tone. Type a meeting note, and it tidies the grammar. It is like a proofreader who lives in your keyboard.

Popular expanders include TextExpander, Espanso, and Raycast's built-in snippets. Pick one. Add five snippets you use every week. Your future self will thank you.

> NOTE: Never put passwords in a text expander. Snippets are stored as plain text, and anyone who can see your snippets can see your passwords. Passwords belong in a password manager, not in a shortcut.

## Privacy notes

Device automations touch private things: your photos, your location, your clipboard, your messages. Keep three rules.

First, prefer on-device AI for private data. It never leaves your phone. Second, check what each automation can see. A shortcut that reads your photos does not need your location too. Third, turn off anything that sends data somewhere you do not recognise. If an app asks for a permission you do not understand, say no, and look it up later.

## Check yourself

1. What is Apple Shortcuts?
**Answer:** Apple's free automation app on iPhone, iPad, and Mac, where a shortcut is a small list of actions that runs in order.

2. What does the Use Model action do?
**Answer:** It sends text to an AI model on your device, or in the cloud, and returns the model's answer inside a shortcut.

3. What is a personal automation?
**Answer:** A shortcut that runs by itself when something happens, such as arriving home or the battery running low.

4. What is Raycast?
**Answer:** A launcher for Mac that lets you run apps, search files, and ask AI questions from your keyboard.

5. Why should you never put a password in a text expander?
**Answer:** Because snippets are stored as plain text, so anyone who can see your snippets can see the password.

## In short

- The best automations live on the devices you already carry.
- Apple Shortcuts plus the Use Model action turns spoken thoughts into tidy notes.
- Personal automations fire on their own, from arrival to low battery.
- Raycast on Mac and Power Automate on Windows bring the same speed to your desktop.
- Text expanders turn short codes into full text, and AI can polish it as you type.
- Prefer on-device AI for private data, and keep passwords in a password manager.
