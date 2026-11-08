# 4.23 Video and audio production with AI
<!-- original: ch. 85 -->

You can now make a short film, a podcast, or a music video from your laptop in one afternoon. No studio. No crew. Just you, a few tools, and a clear plan.

This chapter covers the toolbox. It shows you how to prompt video models like a film director. Then it gives you four complete pipelines you can follow step by step: a short film, a podcast, a faceless explainer video, and a family memory video.

## The toolbox

**Video makers.** These turn words or pictures into moving clips. Current leaders include Veo in Gemini, Kling, Seedance, and Runway. Open models such as Wan, HunyuanVideo, and LTX also exist for people who like to tinker. Check the current price before you commit to one.

**Editors.** CapCut and Descript are the two to know. CapCut is a friendly video editor with captions and effects. Descript lets you edit video by editing the written transcript. Delete a word in the text, and the video cuts that word out.

**Voice tools.** ElevenLabs is the best-known voice tool. It turns text into natural speech. It can also clone a voice, but only with clear permission. It can dub a video into another language with lip-sync.

**Music tools.** Suno makes full songs from a prompt. You will learn more in the next chapter. For background music, simple instrumentals work best.

**Talking heads.** HeyGen and Synthesia make videos of a person speaking. You type the script. An avatar speaks it. They are useful for training videos and translations.

> NOTE: Sora is shut down. OpenAI shut down its Sora video app in April 2026, and its Sora video API in September 2026. Do not build a project that depends on Sora. Use Veo, Kling, Seedance, or Runway instead. And keep your own copies of everything you make. Tools come and go. Your files should not vanish with them.

## Prompt video like a film director

A video prompt needs more than a subject. It needs a shot. Think like a director. Cover these parts.

**Subject and action.** Who is in the shot, and what are they doing?

**Setting.** Where does it happen?

**Camera.** How does the camera move? A static shot feels calm. A slow push-in feels intimate. A drone shot feels epic. A handheld shot feels urgent and real.

**Lighting.** What light falls on the scene? Warm lamp light feels cosy. Cold blue light feels tense.

**Style.** What does it look like? Film-like, animated, documentary, or dreamy?

**Sound.** What do we hear? Rain on glass. Distant thunder. A soft piano.

**Duration.** How long is the clip? Short clips of three to six seconds hide most AI weirdness.

Here is a full example:

> Close-up of an old lighthouse keeper's weathered hands lighting an oil lamp, warm flicker on his face, storm raging through the window behind. Slow push-in. Film-like, 35mm grain, moody blue and amber palette. Sound: rain on glass, distant thunder. Six seconds.

**Image-to-video beats text-to-video.** Make a perfect still picture first. Then ask the video tool to animate it. You control the look. The video model only has to add motion. This one trick fixes most consistency problems.

Generate three or four versions of each shot. Pick the best. Short shots hide glitches in hands, text, and faces.

## Pipeline 1: the 60-second short film

This pipeline makes a tiny film in about two hours.

1. **Script with Claude.** Ask for a 60-second film about a lighthouse keeper who befriends a whale. Ask for six shots. For each shot, ask for a visual description, a camera move, a narration line, and a mood.
2. **Storyboard frames.** Make one picture per shot. Use the same style and the same character reference each time.
3. **Animate.** Turn each frame into a short clip with image-to-video. Add the camera move in the prompt.
4. **Voiceover.** Paste the narration into ElevenLabs. Pick a warm storyteller voice.
5. **Music.** Ask Suno for gentle orchestral piano, hopeful, oceanic, sixty seconds, instrumental.
6. **Edit.** Assemble everything in CapCut or Descript. Time the cuts to the narration. Add captions and a title card.

Keep each shot short. Reuse your reference images. Generate extra versions and pick the best ones.

## Pipeline 2: the effortless podcast

Podcasts are easier than films. Sound forgives more than pictures do.

1. **Record on anything.** Your phone is fine. A quiet room matters more than a fancy microphone.
2. **Clean the sound.** Run the recording through Adobe Podcast Enhance. It removes background noise and makes it sound like a studio.
3. **Edit in Descript.** Delete words in the transcript to cut the audio. Remove "ums" in one click.
4. **Show notes.** Ask Claude to turn the transcript into a summary, timestamps, key quotes, and links.
5. **Clips.** Find the five best thirty-second moments. Turn them into vertical clips with captions for social media.
6. **Bonus.** Translate and dub the episode with ElevenLabs to reach a new audience.

Or skip recording entirely. Gemini Notebook can turn your documents into a two-host podcast automatically. It is a fast way to learn from your own notes.

## Pipeline 3: the faceless explainer video

You do not need to appear on camera to make a good video. Many popular channels never show a face.

1. **Research and script with Claude.** Ask for a hook, three key points, examples, and a call to action. Use web search to check the facts.
2. **Voiceover.** Use ElevenLabs, or record your own voice. Your real voice builds more trust.
3. **Visuals.** Mix AI pictures, short clips, screen recordings, and stock footage. Descript or CapCut can match footage to your script automatically.
4. **Captions and thumbnail.** Add captions and proofread them. Make a bold thumbnail with an image tool. Big text and one clear face or object work best.
5. **Publish.** Post the video. Then ask AI to write the description, the tags, and three social posts about it.

Keep the video tight. Read the script aloud. Cut a fifth of the words. Short videos keep viewers watching.

## Pipeline 4: the family memory video

This one is personal. It turns old photos into a short film your family will treasure.

1. **Scan old photos.** A phone scanning app works well. Scan at the best quality you can.
2. **Restore gently.** Ask an image tool to repair scratches and colourise naturally. Say "keep faces exactly as they are."
3. **Animate subtly.** Use image-to-video with a gentle prompt. "Gentle breeze in the trees, very slow push-in, keep faces still."
4. **Narrate.** Interview a relative. Or write the story with Claude from family notes.
5. **Music.** Pick soft, era-appropriate instrumental music.
6. **Edit.** Cut it into a two to three minute film. Share it with family first.

Be gentle with real people's faces. Keep animation subtle. Share only with family members' blessing. Do not put words in real people's mouths.

## Dubbing, translation, and access

AI can translate a video into another language. It can match the new voice to the speaker's lips. It can add captions in many languages. It can make a transcript for people who prefer to read.

This matters for access. Captions help deaf viewers. Translations help viewers in other countries. Clear audio helps everyone.

Add captions to every video you publish. Proofread them. Bad captions are worse than none. Check the sound on a phone speaker too. Many people watch without headphones.

## The production checklist

Run through this list before you publish anything.

- Is the script tight? Read it aloud and cut a fifth.
- Are the characters and style consistent across shots?
- Is the audio clean? Is the music drowning the voice?
- Are captions added and proofread?
- Did you check for AI weirdness in hands, text, faces, and physics?
- Did you check the rights? Music licence, commercial terms, and consent for any real voice or face?
- Did you label AI use where viewers could be misled?
- Did you save your own backup copies?

## Ethics and consent

Only clone a voice with explicit permission. Your own voice is fine. Anyone else's voice needs their clear, written yes.

Never make deceptive deepfakes of real people. A **deepfake** is a fake video or voice that looks or sounds like a real person. Do not make one to trick anyone.

Label AI-made media where people could be misled. Many platforms now require AI labels for realistic synthetic media. Follow their rules.

Check music and commercial terms before you earn money from a video. A song that is fine for a family video may not be fine for an advert.

> TRY IT: Make a thirty-second film about your pet, your hometown, or a childhood memory. Use four shots. Keep each shot under six seconds. Write the script with Claude, animate still pictures, add a voiceover, and finish it in CapCut. Your first AI film will be imperfect and completely magical.

## Check yourself

1. Why should you make a still picture first and then animate it?
**Answer:** It gives you control over the look and consistency, and the video model only has to add motion.

2. Your AI clips have weird glitches in long shots. What is a simple fix?
**Answer:** Use shorter shots of three to six seconds, generate several versions, and pick the best.

3. When is it okay to clone someone's voice?
**Answer:** Only with their explicit consent, or if it is your own voice, and never to deceive anyone.

4. What happened to Sora?
**Answer:** OpenAI shut down the Sora video app in April 2026 and the Sora video API in September 2026.

5. Why should you keep your own copies of everything you make?
**Answer:** Because tools can shut down, and your work should not vanish with them.

## In short

- Sora is shut down; use Veo, Kling, Seedance, or Runway for video now.
- Prompt video like a director: subject, action, setting, camera, light, style, sound, duration.
- Image-to-video with a still frame first is the secret to consistency.
- Four pipelines cover most jobs: short film, podcast, explainer, and memory video.
- Short shots and extra versions hide most AI glitches.
- Clone voices only with permission, label AI media, and save your own backups.
