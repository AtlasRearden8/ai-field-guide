# 4.26 3D, games, and interactive worlds
<!-- original: ch. 88 -->

Making a game used to take a team and a year. Now you can build a playable browser game in one evening.

AI can write the game code. It can make 3D models from a sentence or a photo. It can drive Blender through MCP. It can make sprites, music, and sound effects. It can give game characters living dialogue. It can even generate whole worlds you can walk through.

This chapter is your game studio tour. You will build your first game tonight. You will learn the loop that makes games better. You will meet 3D tools, AI characters, and world models. Press start.

## The game-making map

A game has many parts. AI can help with each one.

**Code.** The rules and the logic. AI writes it from your description.

**Art.** Sprites, backgrounds, and characters. AI makes them from prompts.

**3D models.** Objects and scenes with depth. AI makes them from text or pictures.

**Music and sound.** Tunes and effects. AI makes them from prompts.

**Dialogue.** What characters say. AI writes it and can speak it too.

**Worlds.** Whole explorable scenes. New **world models** generate them as you move through them.

You do not need all of these at once. Start with code and one kind of art. Add the rest as you grow.

## Vibe-code your first game tonight

Start tiny. A great first game has one mechanic. One mechanic means one thing the player does: jump, dodge, match, or shoot. It fits on a single web page.

Ask any assistant for a game. Claude Artifacts, ChatGPT Canvas, Gemini Canvas, and Grok can all make a small browser game in minutes. For bigger projects, use a coding agent such as Claude Code, Codex, Gemini CLI, or Cursor.

Here is a prompt to try:

> Build a browser game in a single HTML file. A cat jumps between floating clouds. Space or tap to jump. Collect fish for points. Avoid storm clouds. Speed increases slowly. Show the score and the high score, saved in localStorage. Cute pastel style, drawn with canvas shapes, no image files. Works on phone and desktop. Add a start screen and a game-over screen. Then open it in my browser.

**localStorage** is a small store in your browser. It remembers the high score between visits.

Tools that build and host apps, such as Lovable, Bolt, and Replit, can also build games. They put the game on the internet for you in one click.

Game-friendly frameworks your AI knows well include plain HTML canvas, Phaser for 2D games, Three.js and Babylon.js for 3D in the browser, Pygame for Python, and Godot, a free full game engine with its own scripting language.

> NOTE: Start with one mechanic and one page. A tiny game you finish beats a huge game you abandon. You can always add more later.

## The game-dev loop

A first version is never the final version. Games get better through a loop: play it, find one problem, fix one thing, play again.

Play your game. Notice one thing that feels wrong. Ask the AI for one change. Repeat.

Here are common fixes, in plain words you can paste to your AI.

- "It is too hard. Make the first thirty seconds much easier, then ramp up difficulty gradually."
- "It feels floaty. Make the jump snappier: faster rise, faster fall, a tiny squash on landing."
- "It is boring. Add a power-up every twenty seconds and a combo multiplier."
- "It has no juice. Add screen shake on hits, particles on pickups, and a satisfying sound."
- "It does not work on phones. Add touch controls and make the canvas scale to any screen."

**Juice** is the secret sauce. It means tiny effects: particles, screen shake, bouncy animations, and sounds. Juice makes simple games feel amazing. Ask your AI to "add juice" and watch your game come alive.

Save your work after each good change. Git is your save button for code. Commit often. Then you can always go back to a version that worked.

## Text-to-3D and image-to-3D

AI can turn words into 3D objects. It can also turn a picture into a 3D object.

The best workflow is: make a concept picture first, then turn it into 3D, then clean it up, then use it.

1. **Concept image.** Generate a picture of the object. You control the look here.
2. **Image-to-3D.** Turn the picture into a 3D model. Tools for this include the text-to-3D and image-to-3D features in major creative apps and open tools.
3. **Clean up.** Open the model in Blender. Fix rough edges. Check the size.
4. **Export.** Save as `.glb` for the web, `.fbx` for game engines, or `.stl` for 3D printing.

Text-to-3D is getting better fast. Image-to-3D is usually more reliable, because the picture locks the look in place. Either way, expect to clean up the result. AI models are a starting point, not a finished asset.

## Blender, Godot, and Unity through MCP

Community MCP servers connect Claude to creative apps. **MCP** is a standard plug that lets AI use your tools.

With a Blender MCP server, you can say: "Create a low-poly tree and place five copies on the hill." Claude runs the commands in Blender. It can look at a screenshot and fix what looks wrong.

With a Unity MCP server, you can say: "Create a spinning coin prefab and a score counter UI." A **prefab** is a reusable object in Unity. Claude builds it and places it in your scene.

With a Godot MCP server, you can say similar things in the free Godot engine.

This is like having a technical artist on call. Start with backups. Review scripts before you run them. AI can change a scene fast, and a backup lets you undo anything.

## AI characters that talk back

Game characters used to say the same lines every time. Now they can talk freely.

Give each character a personality, secrets, and goals in a **system prompt**. A system prompt is the hidden instruction that tells the AI how to behave. Then let players chat with the character.

Here is an example:

> You are Marta, the village baker in Brightwater. Warm, gossipy, secretly afraid of the forest. You know: the mill closed last spring, the blacksmith's son vanished near the old oak. Never mention anything outside this world. Keep replies under forty words. If the player is kind, hint that the old oak hides a door.

Add guardrails. Keep characters in their world. "You only know things a medieval baker would know." Set content limits. Give them memory, so they remember what the player did last time.

Give each character a distinct voice with text-to-speech. Platforms built for game characters, such as Inworld and Convai, handle voices, memory, and engine plugins for you.

## World models: generated, explorable worlds

**World models** generate interactive worlds frame by frame as you move through them. Google DeepMind's Genie research is the best-known example. Other tools turn pictures or text into explorable 3D scenes.

It is early. The worlds are often short-lived and low resolution. But they point to a future where games and simulations are generated rather than built by hand. Try them when you get access. Do not build a business on them yet.

## From AI to real objects: 3D printing

AI models can become real objects on your desk.

1. **Generate a model.** Use text-to-3D or image-to-3D. Or ask Claude to write OpenSCAD code for precise parts, such as "a hook for my bike helmet, five centimetres deep, with two screw holes." OpenSCAD is a program that builds 3D shapes from code.
2. **Check it is printable.** It needs a closed, watertight shape with a flat base. Fix it in Blender or your slicer.
3. **Slice it.** A **slicer** is a program that turns a 3D model into layers your printer can print. Bambu Studio, PrusaSlicer, and Cura are popular slicers.
4. **Print it.** Start small. Measure the result. Tweak and print again.

## Twenty game and 3D projects

Try one of these when you want practice.

1. A jumping game with your pet as the hero.
2. A memory match game with pictures you generated.
3. A maze game with three levels.
4. A space shooter with power-ups.
5. A word game that uses your own vocabulary list.
6. A 3D model of your house, from a photo.
7. A chess set, printed in 3D.
8. A game character with a personality and a voice.
9. A racing game with a track you designed.
10. A tower defence game with five enemy types.
11. A virtual tour of an imaginary museum.
12. A 3D-printed phone stand in your style.
13. A quiz game about your favourite show.
14. A fishing game with a day and night cycle.
15. A board game, built as a web app.
16. A 3D model of a gift for a friend.
17. A platform game with a double jump.
18. A game where an AI character gives you quests.
19. A 3D-printed cookie cutter in a fun shape.
20. A tiny world you can walk through in your browser.

> TRY IT: Ask your favourite assistant to build the cloud-jumping cat game from this chapter. Play it. Then ask for one change: "Add juice: particles on pickups and screen shake on hits." Play it again. Feel the difference one sentence makes.

## Check yourself

1. What should your first game have, and why?
**Answer:** One mechanic and one page, because a tiny game you finish beats a huge game you abandon.

2. What is "juice" in a game?
**Answer:** Tiny effects such as particles, screen shake, bouncy animations, and sounds that make a simple game feel amazing.

3. What is the best workflow for making a 3D model?
**Answer:** Make a concept image first, turn it into 3D, clean it up in Blender, then export it in the right format.

4. How do you keep an AI game character in its world?
**Answer:** Give it a system prompt with its personality and knowledge, and tell it never to mention anything outside that world.

5. What is a world model?
**Answer:** A model that generates an interactive world frame by frame as you move through it.

## In short

- Start tiny: one mechanic, one page, one finished game.
- The game-dev loop is play, find one problem, fix one thing, repeat.
- Juice is the secret sauce: particles, shake, bounce, and sound.
- Make a concept image first, then turn it into 3D, then clean it up.
- MCP lets Claude drive Blender, Godot, and Unity.
- AI characters need a personality, secrets, goals, and guardrails.
- World models are early but exciting; 3D printing turns AI models into real objects.
