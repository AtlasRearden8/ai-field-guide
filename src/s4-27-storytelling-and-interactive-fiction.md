# 4.27 Storytelling and interactive fiction
<!-- original: ch. 89 -->

AI is a wonderful creative partner. It is a brainstorming buddy at 2am. It is a tireless game master. It is a character you can interview. It is a kind editor. It is a bedtime-story machine.

This chapter shows you how to co-write with AI while keeping your own voice. You will build a story bible. You will learn writing workflows for each stage. You will run tabletop adventures. You will build choose-your-own-adventure stories. You will make bedtime stories with kids. And you will publish responsibly.

## Co-writer, not ghostwriter

A **ghostwriter** writes the whole thing for you. A co-writer works with you. AI should be the second one. You stay the author.

AI is brilliant at some jobs. It can brainstorm fifty "what ifs" in a minute. It can ask questions about your world. It can play your characters so you can interview them. It can spot plot holes. It can suggest titles.

You bring the rest. You bring the idea that makes you excited. You bring answers rooted in your life and taste. You bring the emotional truth of who your characters are. You make the final choices.

Ask for options, not answers. Say "Give me ten possible reasons the lighthouse keeper refuses to leave. Make three of them surprising." Choosing from options keeps you the author. The best idea is often a mix of two options.

If AI writes a paragraph you love, keep it. If it writes a paragraph that sounds wrong, change it. Your taste is the editor. AI is the first draft machine.

## Build a story bible

A **story bible** keeps a long project consistent. It is one document with everything that must stay true: the premise, the tone, the characters, the world rules, and the plot so far.

Put it in a Claude Project, or in a file called `STORY.md` for Claude Code. Then every conversation knows your world.

Here is a small example:

> Story bible: The Lighthouse at Gull's End
> Premise: A retired lighthouse keeper befriends a whale who can speak only during storms.
> Tone and style: cosy, bittersweet, quiet humour. Present tense. Short chapters. For ages ten and up.
> Characters: Edda Marsh, 71, stubborn, kind, hums sea shanties off-key. She lost her husband at sea. Old Grey, an ancient whale who speaks in riddles and fears the new shipping lanes.
> World rules: The whale speaks only when lightning strikes. The lighthouse is being automated next spring.
> Plot so far: Chapters one to three: Edda hears the whale for the first time.

Use the bible in your prompts. "Check chapter four against the story bible. List any contradictions." Or "Suggest three ways Old Grey's fear could raise the stakes in act two."

Update the bible as you write. A bible that is out of date is worse than no bible. It teaches the AI the wrong facts.

## Writing workflows

Different stages need different help. Use a targeted prompt for each stage.

**Ideas.** "Give me twenty story ideas about a lighthouse keeper and a whale. Make five of them funny, five sad, five strange, and five hopeful." Pick one. Mix two if you like.

**Outlining.** "Outline this as a three-act story with a midpoint twist. Keep my beats, suggest missing ones." A **beat** is one key moment in the story.

**Drafting.** "Write chapter one, about 500 words, in the voice of the story bible. End on a small mystery." Then edit it yourself. AI drafts are a starting point.

**Revision.** "Read this chapter and list the three weakest sentences. Suggest a fix for each." Or "Where does the pacing drag? What could I cut?"

**Dialogue.** "Write this scene as dialogue only. Edda is hiding something. Old Grey knows it." Read it aloud. If it sounds stiff, ask for a simpler version.

**Titles.** "Give me ten titles for this story. Make three poetic, three plain, and four funny."

Keep your drafts in one place. A folder per story works well. Name files by chapter and date, so you can always go back.

## AI as game master

Chat adventures are one of the most fun things you can do with AI. The secret is a great setup prompt.

Try this one:

> You are the game master for a cosy fantasy adventure. I play Pip, a halfling baker with a magic rolling pin.
> Describe scenes vividly in three to five sentences, then ask "What do you do?" Never decide my actions or feelings for me.
> When an action is risky, roll a d20 and show the roll. One to seven fails, eight to fourteen is mixed, fifteen to twenty succeeds.
> Track my inventory, health (ten hearts), and gold in a short status line after each turn.
> Keep a mystery running in the background, with clues I can discover. Keep it PG, funny, and warm.
> Begin in the village square on market day.

A **d20** is a twenty-sided die, the classic die of tabletop games. A **game master** is the person, or AI, who runs the adventure and describes the world.

Level up your adventures with these tricks.

- **Group play.** Run the adventure in a Discord bot for your friends.
- **Real dice.** Give an agent a dice tool so rolls are truly random.
- **Campaign memory.** Keep a notes file the AI updates after each session.
- **Maps and portraits.** Generate character art and maps with an image tool.
- **Voice narration.** Use a voice agent as the narrator for an audio adventure.

For human game masters, AI is an amazing prep partner. "Generate a tavern with five NPCs, each with a secret and a rumour." An **NPC** is a non-player character, a person in the game world who is not played by a human. Or: "My players went off-script into the sewers. Give me a twenty-minute sewer encounter, fast!"

## Build a choose-your-own-adventure

A choose-your-own-adventure story gives the reader choices. Each choice leads to a different scene. The reader picks the path.

You have three good tools for this.

**Twine.** A free, visual editor for branching stories. It exports a web page. You drag boxes and connect them with arrows. It is the easiest way to start.

**Ink.** A scripting language for branching narrative, used in real games. It is more powerful than Twine. It takes longer to learn.

**A custom web app.** Vibe-code it with Claude Code. Story nodes in a simple data file, plus a pretty reader with page-turn animations and a map of choices made.

The hybrid that works best is simple. You design the skeleton. The AI writes the prose.

Design the key choices and the endings first. That way the story always makes sense. Then let AI write each scene. Add personal flavour, such as the reader's name or their pet's name.

Here is a tiny skeleton:

> Start: the storm. Open the door, or hide?
> Open: meet the whale. Hide: find the old logbook.
> Meet the whale: help the ships, or warn them?
> Help: happy ending. Warn: bittersweet ending.

Four endings are enough for a first story. You can add more later.

> NOTE: Design the skeleton yourself. If AI designs the whole branching story, the branches tangle and the endings stop making sense. Your job is the map. AI's job is the words on each page.

## Bedtime stories and kids' books

Co-create with your child. They choose the hero, the setting, and the problem. "A story about Maya and her dog Biscuit who find a door in the moon."

Keep kids in the driver's seat. Stop at a cliffhanger and ask them what happens next. A **cliffhanger** is a moment of suspense at the end of a scene. It makes the reader want to know more.

Add gentle values. "The story should show that it is okay to be scared and ask for help." Values land better inside a story than inside a lecture.

Make it a book. Generate consistent illustrations with an image tool. Use a reference sheet for the hero. Then print a photo book or make a PDF.

Read it aloud in your own voice. AI voices are fine, but your voice is the magic. A story read by a parent is a memory, not just a story.

## Worldbuilding superpowers

**Worldbuilding** means inventing the world your story lives in: its places, its history, its rules, and its people.

AI is good at worldbuilding. Ask it to invent a town. Ask it to write the history of a war that ended fifty years ago. Ask it to design a magic system with three rules and one cost. Ask it to invent ten street names, ten shop names, and ten local sayings.

Keep a world file next to your story bible. Every new fact goes in the file. When you invent a rule, write it down. When you break a rule, the reader notices.

Ask AI to check your world for contradictions. "Here is my world file. List any places where the rules contradict each other." Fix the list before you publish.

## Publishing and ethics

When you publish a story made with AI, be honest about it. Say how AI helped. "Written with AI assistance" is enough for most cases. Some publishers and platforms have their own rules. Read them first.

Do not publish a story that copies a living author's style or characters. Do not sell a story that is mostly AI text and call it fully your own work. Your voice and your choices are what make it yours.

Check the terms of the tools you used. Some free plans allow personal use only. If you plan to sell a book, check the commercial terms first.

> TRY IT: Write a story bible for a story you have always wanted to tell. One page is enough. Premise, tone, three characters, three world rules, and the plot so far. Then ask Claude: "Suggest three ways to raise the stakes in act two." Pick one. Write the next scene.

## Check yourself

1. What is a story bible, and why does it matter?
**Answer:** It is one document with the premise, tone, characters, world rules, and plot so far, and it keeps a long story consistent.

2. Why should you ask AI for options instead of answers?
**Answer:** Choosing from options keeps you the author, and the best idea is often a mix of two options.

3. What is the game master's job in a chat adventure?
**Answer:** To describe the world, run the rules, and ask "What do you do?" without deciding the player's actions.

4. In a choose-your-own-adventure, what should you design yourself?
**Answer:** The skeleton: the key choices and endings, so the story always makes sense.

5. Why should you read a bedtime story in your own voice?
**Answer:** Because your voice is the magic, and the story becomes a memory, not just a story.

## In short

- AI is a co-writer, not a ghostwriter; you stay the author.
- A story bible keeps long projects consistent.
- Use a targeted prompt for each stage: ideas, outline, draft, revision.
- A great game master prompt sets rules, tracks status, and keeps a mystery running.
- Design the branching skeleton yourself; let AI write the prose.
- Co-create bedtime stories with kids, and read them in your own voice.
- Be honest about AI help when you publish.
