# 4.13 Vibe coding your first real app
<!-- original: ch. 65 -->

**Vibe coding** means building software by describing what you want, and refining it through conversation with an AI, rather than writing code yourself. It is real. It works. And people with no programming background ship useful apps with it every day.

This chapter takes you from an idea to a working, deployed app. You will pick a small, real idea. You will write a short spec. You will build version one. You will fix what is wrong. And you will ship it, so real people can use it.

## The vibe coding stack

You need three things. A builder, a place to store data, and a place to put the app on the internet.

The **builder** is the AI tool that writes the app. Pick one from Chapter 4.8: Lovable, Bolt, v0, or Replit in the browser, or Claude Code or Cursor on your computer. Browser builders are the easiest start. They need no install, and they show you the app as it grows.

The **database** is where your app keeps its facts. For a small app, a hosted database service is easiest. **Supabase** is a popular free choice. It gives you tables to store data, and a way to sign users in, without you running a server. Make a free account, and keep it for this chapter.

The **host** is where the app lives on the internet. Many builders deploy for you with one click. If yours does not, Chapter 4.14 shows you how to deploy with Vercel, Netlify, or Cloudflare. For now, know that the host is a separate step, and it is usually the easiest step.

As of November 5, 2026, the paid plans for the main browser builders were Lovable Pro at $25 a month, Bolt Pro at $25 a month, v0 Plus at $30 a month, and Replit Core at $20 a month. All of them have free tiers to start. Check the current price before you pay for any of them.

## Step 1: Pick a small, real idea

A good first app is small, real, and useful to at least one person. Small means one main job, not ten. Real means it solves a problem you actually have. Useful means someone will open it more than once.

Good first ideas: a shopping list that two people can share. A habit tracker with one habit and a tick box. A recipe box that saves your favourite meals. A simple booking form for a small club. A tip calculator that splits a bill.

Bad first ideas: a social network. A marketplace. An app with payments, logins, and chat, all at once. Those are real projects, but they are not first projects. They have too many moving parts, and you will get stuck on the fifth part before the first one works.

Pick one idea. Write it down in one sentence. "A shared shopping list for me and my partner." That sentence is your compass. Every time you are tempted to add a feature, ask if it serves that sentence. If it does not, save it for version two.

> NOTE: The best first app is a little bit boring. Boring means it has one clear job, and you can tell when it works. Exciting ideas with ten features are how first apps die unfinished.

## Step 2: Write a mini spec, in five minutes

A **spec** is a short description of what to build. It is the message you give the builder. Write it before you open the tool, in plain words. Five minutes is enough.

Your spec needs five parts. What the app is, in one sentence. Who it is for. What the user can do, as a short list. What the app looks like, in a few words. And what it must not do.

Here is an example, for the shared shopping list:

"We are building a shared shopping list for two people at home. The user can add an item, tick an item off, delete an item, and see the list on their phone. The design is clean and simple, with big buttons that are easy to tap. It must not need an account to try it. It must save the list, so it is still there tomorrow."

That is a spec. It is short. It is clear. It says what success looks like. Give that to your builder, and it will build something close to what you meant. Give it a vague sentence, and it will guess, and the guess will be wrong.

> TRY IT: Write a mini spec for your own idea right now, using the five parts above. Keep it under 150 words. If it is longer, cut it. A short spec is a clear spec.

## Step 3: Build version one

Now open your builder. Paste in your spec. Press send. Wait. In a minute or two, you will see a first version of your app.

Do not judge it yet. Click around. Add an item. Tick it off. Delete it. Does the main job work? If yes, you have a version one. If no, read the next section before you change anything.

If you are using Claude Code or Cursor instead of a browser builder, the steps are the same, but the conversation is longer. Paste the spec. Ask for a plan first. Then say go. Then test it. The five-step workflow from Chapter 4.10 applies here too: explore, plan, code, check, commit.

One warning: do not ask for five new features at once. Ask for one. Check it. Then ask for the next. Small steps are how version one becomes version two without breaking.

## Step 4: The iteration loop

**Iteration** means improving something a little at a time, in rounds. Each round has four steps: try it, notice what is wrong, describe the fix in plain words, and check the fix.

Try it like a real user, not like a builder. Use your phone, not just your computer. Add a strange item. Leave a field empty. Press the button twice. Real users do all of these things, and your app should handle them gracefully.

When you find a problem, describe it precisely. "When I add an item with no name, the app shows a blank row. It should show a message that says 'Please type an item first.'" That is a good bug report. "The list is broken" is not. The better your description, the better the fix.

Then check the fix. Add an empty item again. Does the message appear now? If yes, move on. If no, describe what you see, and ask again. Two or three rounds of this loop will fix most problems.

## Debugging without panic

**Debugging** means finding out why something does not work. It feels scary. It is mostly calm detective work.

When something breaks, do three things. First, read the error out loud. Errors sound scary, but they usually say what went wrong, in plain words hidden under jargon. Second, ask the AI to explain the error in plain words. "This error appeared when I pressed the button. Explain what it means, and what you think caused it." Third, fix one thing at a time. Change one thing, test it, and see if the error changes. If you change five things at once, you will never know which one fixed it.

Common beginner bugs: a button that does nothing, because it is not connected to the action. A list that shows nothing, because the data is saved in one place and read from another. A page that looks wrong on a phone, because it was only tested on a computer. All of these are normal. All of them are fixable. None of them mean you have failed.

If you are truly stuck, make the app smaller. Remove a feature. Get the main job working. Add the feature back later. A small app that works beats a big app that does not.

## Making it beautiful

A beautiful app is not about fancy effects. It is about three things: clear text, enough space, and one consistent style.

Use big, readable text. Leave space between things, so fingers can tap the right button. Pick one colour for your main buttons, and use it everywhere. Pick one font, and use it everywhere. That is most of good design.

Ask your builder for help. "Make this look clean and friendly, with big buttons, lots of space, and one accent colour." Then look at the result on your phone. If it feels calm and easy, it is good. If it feels crowded, ask for more space and fewer things on each screen.

## Step 5: Ship it

**Shipping** means putting your app on the internet, so other people can use it. This is the step most beginners skip. Do not skip it. An app nobody can open is a draft. An app with a link is real.

If you used a browser builder, look for a Deploy or Publish button. Press it. You will get a link. Open that link on your phone. Does it work? If yes, share it with one person. Ask them to try it, and to tell you what confused them.

If you used Claude Code or Cursor, Chapter 4.14 shows you how to deploy with a host like Vercel or Netlify. It is usually a matter of connecting your project folder and pressing deploy.

After you ship, watch for two things. First, does the link work for someone who is not you? Second, does the app still work tomorrow? If yes to both, you have shipped a real app. That is a genuine achievement. Tell someone.

## Step 6: Do not skip the safety basics

Before you share your app widely, do three safety checks.

First, check your secrets. An **API key** is a secret password that lets your app talk to a service. If your app uses one, make sure the key is stored in a safe place, not written in the code where anyone can read it. Chapter 4.14 explains how to store secrets properly.

Second, check what data your app collects. If it asks for names, emails, or anything personal, say clearly what you do with that data, and do not collect more than you need.

Third, check who can see what. If your shopping list is shared, make sure only the people you invite can see it. Test this by opening the link in a browser where you are not signed in. If you can see things you should not, fix the permissions before you share the link widely.

## Adding AI features to your app

Once the main job works, you can add AI to it. Good first AI features: a button that summarises a long list. A search box that understands plain words, like "show me the vegetarian recipes." A helper that suggests what to add, based on what is already there.

To add one, describe it the same way you described the app: one sentence, what it does, and what success looks like. "Add a button that turns the shopping list into a tidy summary, grouped by shop aisle." The builder will add the AI call for you, or you can ask Claude Code to wire it up, as Chapter 4.15 shows.

## Common beginner traps, and the fix

Trying to build everything at once. Fix it by picking one main job, and saving the rest for later.

Adding features before the main job works. Fix it by testing the main job first, every time.

Trusting the app without testing it on your phone. Fix it by opening the link on your phone, today.

Skipping Git. Fix it by saving a snapshot before each new feature, as Chapter 4.9 taught you.

Giving up at the first error. Fix it by reading the error out loud, asking the AI to explain it, and fixing one thing at a time.

## Check yourself

1. What is vibe coding?
**Answer:** Building software by describing what you want in plain words, and refining it through conversation with an AI, rather than writing code yourself.

2. What are the five parts of a mini spec?
**Answer:** What the app is, who it is for, what the user can do, what it looks like, and what it must not do.

3. What are the four steps of the iteration loop?
**Answer:** Try it, notice what is wrong, describe the fix in plain words, and check the fix.

4. What does shipping an app mean?
**Answer:** Putting it on the internet so other people can open it with a link.

5. What should you check before sharing your app widely?
**Answer:** That secrets are stored safely, that you collect only the data you need, and that only the right people can see it.

## In short

- Pick a small, real idea with one main job.
- Write a short spec before you open the builder.
- Build version one, then improve it in small rounds.
- Describe bugs precisely, fix one thing at a time, and test on your phone.
- Ship it with a link, and share it with one real person.
- Do the safety basics: protect secrets, collect little data, and check who can see what.
