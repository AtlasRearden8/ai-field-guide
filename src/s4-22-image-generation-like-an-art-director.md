# 4.22 Image generation, like an art director
<!-- original: ch. 84 -->

An art director does not just say "make a picture." She says what the picture is about. She says how it should feel. She says what light to use, what colours to pick, and where the eye should go first.

You can do the same with AI. The trick is to describe your picture in layers. Each layer adds control. Together, they turn a vague idea into a picture you are proud of.

This chapter shows you how. You will pick the right tool for each job. You will write prompts in layers. You will edit by chatting. You will keep one character looking the same across many pictures.

## Pick the right tool for the job

Different tools are good at different jobs. Pick by the job, not by the brand name.

- **ChatGPT and Gemini** are best when you want to edit by chatting. Describe a change in plain words. The picture updates. They also follow complex instructions well.
- **Midjourney** is best for beautiful, artistic pictures. It has a strong sense of style. It is a good pick for posters, book covers, and fantasy art.
- **Ideogram** is best when the picture needs words in it. Posters, signs, and logos need text that is spelled right. Ideogram handles that well.
- **FLUX and other open models** are best for photo-real pictures. They are also good when you want to run the model on your own computer.
- **Recraft** is best for clean vector-style graphics. Think icons, simple illustrations, and flat design.

> NOTE: Rankings change every few months. New models arrive. Old leaders fall behind. Check a public leaderboard when you need the current best. A leaderboard is a site where people vote blind between pictures from different models. The winner is the one people pick most.

Start with one tool. Learn it well. Add a second tool only when you hit a limit. Two tools you know well beat five tools you barely know.

## The anatomy of a great prompt

A great prompt has layers. Cover the layers you care about. Skip the rest.

**Subject.** What is in the picture? Be specific. Say "a red fox wearing a tiny knitted scarf." Do not just say "a fox."

**Action or pose.** What is the subject doing? Say "curled up asleep on a stack of old books."

**Setting.** Where is it? Say "in a cosy attic library, rain on the skylight."

**Style or medium.** What does it look like? Say "watercolour illustration." Or "35mm film photo." Or "3D animated-film render."

**Lighting.** What light falls on the scene? Say "warm lamp light, soft shadows." Or "golden hour sun."

**Camera and composition.** How is the shot framed? Say "close-up, shallow depth of field, eye level." Shallow depth of field means the subject is sharp and the background is soft.

**Colour palette.** What colours dominate? Say "muted autumn tones, with pops of teal."

**Mood.** How should it feel? Say "peaceful, nostalgic."

**Text.** What words appear in the picture? Put them in quotes. Say 'the words "Reading Nook" in hand-lettered serif at the top.'

**Format.** What shape is the picture? Say "square." Or "16:9 wide." Or "vertical 9:16 phone wallpaper."

Here is all of it together:

> A red fox wearing a tiny knitted scarf, curled up asleep on a stack of old books in a cosy attic library, rain on the skylight. Watercolour illustration, warm lamp light, muted autumn palette with teal accents. Peaceful, nostalgic. Square.

That one paragraph gives the model everything it needs. Compare it with "a fox." The difference is the difference between a lucky guess and a picture you meant to make.

Let AI write your prompts too. Ask Claude: "Turn my idea into three detailed image prompts in different styles." Then pick the best one. Claude is a good prompt writer. It is especially good at keeping a series of pictures consistent.

## Editing: the real superpower

Making a first picture is easy. Fixing it is the real skill. Modern tools let you edit by chatting.

Try these edits. Each one is a plain sentence.

- "Make the sky sunset orange instead of blue."
- "Remove the person on the left."
- "Zoom out so we see the whole house."
- "Make the fox look at the camera."
- "Change the style to a pencil sketch."

Edit one thing at a time. If you change five things at once, you will not know which change caused a problem. Small steps give you control.

You can also edit part of a picture. Some tools let you paint over an area. Tell the tool what should be in that area. The rest of the picture stays the same.

If an edit goes wrong, do not start over. Ask for the change again, in different words. Or go back one step. Most tools keep a history of your edits.

## Keep one character looking the same

A single picture is easy. Twelve pictures of the same character are hard. The character's face drifts. Her hair changes. Her coat changes colour. Here is how to stop that.

First, make a **reference sheet**. Ask for "a character sheet: front, side, and back views of Maya, plain background." This gives you one picture that defines the character.

Second, reuse that picture every time. Say "Using this character, show her at the beach." The model copies the look from your reference.

Third, write a **character bible**. This is a short paragraph that never changes. It lists the character's hair, eyes, clothes, and style. Paste it into every prompt. For example: "Maya is eight, with curly black hair in two braids, brown eyes, a red coat, and yellow boots."

Fourth, keep a style reference too. One picture that defines the look of the whole series. Reuse it the same way.

Fifth, for advanced work, train a small **LoRA**. A LoRA is a tiny add-on trained on ten to twenty pictures of a character, a product, or your style. It locks the look in place. You need a local model or a service that supports it. It is worth the effort for a long series.

## Run image models on your own computer

You can also run image models at home. The benefits are real. You get unlimited pictures. Your pictures stay private. You can use custom add-ons like LoRAs. You can run big batches, such as fifty product shots in the same style.

You need a good graphics card. A card with 8 GB of memory runs many models. A card with 16 to 24 GB runs the big ones with ease. Macs work too, but they are slower for this job.

The most popular home tool is **ComfyUI**. It is a free program that builds pictures from a chain of small blocks. Each block does one job. It looks complex at first. Start with a ready-made workflow from the community. Change one block at a time.

Local models are a hobby in themselves. Start with a cloud tool. Move local only when you want privacy, volume, or control that the cloud cannot give you.

## Automate your image work

Once you can make one good picture, you can make a hundred. **Automation** means a workflow makes pictures for you, without you clicking each time.

Here is a common pattern. A blog post is published. Claude writes an image prompt for it. An image service makes the picture. The picture is uploaded to your site. Nobody touches it by hand.

You can build this with n8n, Make, or Zapier. You can also use an image service directly through its **API**. An API is a way for programs to talk to each other. You send a prompt. You get a picture back.

MCP servers can do this too. An image-making MCP server lets Claude make pictures in the middle of a chat. You ask for a picture. Claude calls the server. The picture appears in your chat.

## Practical uses that pay off

Image AI is not just for fun. It pays off in real work.

- **Personal:** pet portraits in old painting styles, custom phone wallpapers, birthday cards.
- **Stories:** character art for a game, illustrations for a children's book, a comic strip.
- **Business:** product shots in a consistent style, social media graphics, a logo draft.
- **Learning:** diagrams of how things work, maps of imaginary places, flashcards with pictures.

Start with a job that repeats. A weekly social post. A monthly report cover. A set of product shots. One good workflow saves hours every month.

## Ethics and rights, the practical version

A few rules keep you safe and fair.

Name an era or a medium instead of a living artist. Say "1970s science fiction paperback cover." You get the vibe. You do not copy a real person's work.

Do not use a real person's face without permission. Do not make fake photos of real people. Do not pass AI pictures off as real photos.

Check the commercial terms before you sell anything. Some plans allow sales. Some do not. Check the current price and terms on the tool's own site. Terms change often.

Label AI-made work where it matters. A small note is enough. "Made with AI" is honest and simple.

> TRY IT: Pick a character you love. It could be your pet, your child, or an invented hero. Write a character bible in three sentences. Make a reference sheet. Then make three pictures of the character in three different places, reusing the reference each time. Compare them. Does the character look the same? Fix the bible until she does.

## Check yourself

1. You need a poster with the exact words "Summer Fete 2026" spelled correctly. Which tools are strongest for that job?
**Answer:** Tools known for good text in pictures, such as Ideogram, ChatGPT, or Gemini.

2. How do you keep the same character looking the same across twelve pictures?
**Answer:** Make a reference sheet, reuse it each time, keep a fixed character bible, and optionally train a LoRA.

3. Why is it better to name an era or medium instead of a living artist?
**Answer:** You get the style you want without copying a real person's signature work, which is kinder to artists and safer for commercial use.

4. Why should you edit one thing at a time?
**Answer:** So you can see which change caused a problem, and keep control of the result.

5. What is the main benefit of running image models on your own computer?
**Answer:** Unlimited pictures, full privacy, custom add-ons, and big batches in one style.

## In short

- Pick the tool by the job: chat editing, art, text, photo-realism, or clean graphics.
- Write prompts in layers: subject, action, setting, style, light, camera, colours, mood, text, format.
- Editing by chatting is the real superpower; change one thing at a time.
- Reference sheets and a character bible keep a character consistent.
- Local models give privacy and volume, but need a good graphics card.
- Name an era or medium, not a living artist, and check commercial terms first.
