# 6.9 Build-along: the automated newsletter
<!-- original: ch. 118 -->

By the end of this build, a lovely newsletter will write itself every week. It reads your favourite feeds. Claude picks the best items and explains why each matters. A nice email lands in your inbox, or in your subscribers' inboxes.

You will run the newsletter pipeline kit, make it yours, put it on autopilot, and optionally rebuild it with no code in n8n.

Time: about two hours. Level: beginner to intermediate.

## What you will build

A pipeline with four stages.

- **Read.** It fetches your favourite feeds and sites.
- **Pick.** Claude reads the items and picks the best ones.
- **Write.** Claude writes a short note on why each item matters.
- **Send.** It sends a well-designed email, every week, on time.

Your own personal editor-in-chief, working while you sleep.

## Before you start

You need four things.

- **Python 3.10 or newer**, or n8n if you prefer the no-code path.
- **An Anthropic API key**, with a spending cap set.
- **An email account or a newsletter platform**, such as Buttondown, Substack, or plain Gmail.
- **The newsletter-pipeline kit**, downloaded from the book's kit page. No account is needed.

Pick your audience first. A newsletter for yourself is a personal digest. A newsletter for subscribers is a publication. The build is the same. The voice and the care are different.

## Step 1: test and dry run, 10 minutes

A **dry run** is a test that does everything except send. It is the safest way to start.

Run the kit with its sample data.

```
python3 newsletter.py --dry-run
```

Line by line: `python3 newsletter.py` runs the pipeline. `--dry-run` tells it to build the email but not send it. Read the output. You should see a finished email in your terminal or in a file. If it fails, read the error. It usually names a missing key or a missing feed.

A dry run costs almost nothing. Run it after every change you make.

## Step 2: choose your feeds, 20 minutes

Feeds are the raw material. Good feeds make a good newsletter. Bad feeds make noise.

Pick five to ten feeds you actually read. Blogs, news sites, and journals. Mix big sources with small ones. Small blogs often have the freshest ideas.

Add them to the kit's feeds file. Each feed needs a name and a URL. Remove any feed you have not read in a month. A feed you ignore is a feed that wastes your reader's time.

Test the feeds. Run the pipeline in dry-run mode. Check that each feed returns items. A dead feed returns nothing. Remove it or fix its URL. A feed that only posts once a month is fine too, as long as it posts something worth reading when it does.

## Step 3: your first AI-curated issue, 15 minutes

Run the pipeline for real, but send it only to yourself.

The kit uses Claude's structured output to get a clean newsletter object. **Structured output** means the AI returns data in a set format, with named fields, instead of free text. The kit asks for a list of items, each with a title, a link, and a short note. That clean shape makes the email easy to build.

Read the issue like a reader. Is the pick good? Is the note useful? Does it sound like you? If the picks are weak, your feeds are weak. If the notes are bland, your prompt is bland. Fix the input, not the output.

## Step 4: make it yours, 30 minutes

A newsletter with no voice is a list of links. Give it a voice.

**Voice.** Tell Claude how to write. "Warm, curious, and plain. Short sentences. One idea per note. No hype." Add an example of a note you like. Examples teach faster than rules.

**Sections.** Add sections that fit your topic. "One big idea, three links, one question for readers." Or "What I read, what I tried, what I am watching." Sections give the reader a map.

**Design.** Keep the email simple. A clear title. A short intro. One item at a time, with a title, a link, and a note. A footer with an unsubscribe link. Simple emails get read. Fancy emails get skimmed.

**Name.** Give the newsletter a name that says what it is. "The Sunday Field Notes." "What I Learned This Week." A good name is a promise. Keep it.

## Step 5: send it, 20 minutes

Send the first real issue to yourself. Then to three friends. Ask them what they thought. Did they read it? Did they click anything? What would they change?

Fix the top complaint. Then send to your full list. Your friends' honest feedback is the cheapest editor you will ever hire, and it makes the second issue far better than the first. If you use a newsletter platform, it handles subscribes and unsubscribes for you. If you use plain email, keep a simple list and honour every unsubscribe at once.

Always send a test to yourself first. A typo in a test is a laugh. A typo in a send to a thousand people is a lesson.

## Step 6: put it on autopilot, 15 minutes

Schedule the pipeline to run every week. A cron job or a scheduled task runs it at the same time each week. A **cron job** is a scheduled job on your computer that runs a command at a set time.

Pick a time that gives you room to review. Run it on Sunday evening. Review the draft on Monday morning. Send it on Monday at 9am. A human review between the draft and the send catches bad picks and typos.

Set a spending cap. A weekly pipeline that calls Claude every week costs money every week. Check the cost of one issue. Multiply by four. Set the cap above that.

## Level-ups

- **No-code rebuild.** Rebuild the pipeline in n8n: RSS nodes fetch the feeds, an AI node picks and writes, and an email node sends. Same result, no Python.
- **Reader replies.** Ask a question at the end of each issue. Reply to every answer. A newsletter with replies is a conversation.
- **Archive.** Publish each issue to a simple web page. New readers can browse the back catalogue.
- **Topics.** Let readers pick topics. Send each reader only the sections they chose.
- **Guest picks.** Once a month, ask a friend to pick their favourite link of the week. It brings a fresh voice and new ideas to your readers.

> NOTE: A newsletter is a promise to show up every week. Pick a schedule you can keep for a year. Weekly is ambitious. Fortnightly is fine. Monthly is fine too. A newsletter that arrives on time, every time, beats a newsletter that arrives in bursts and then vanishes.

## Troubleshooting

- **The dry run fails.** Check your API key and your feeds file. One bad feed URL can break the whole run.
- **The picks are weak.** Your feeds are weak, or your prompt is vague. Add better feeds. Tell Claude exactly what "interesting" means to you.
- **The email looks broken.** Check the email template. Test it in two email apps. Simple HTML works everywhere. Fancy HTML breaks somewhere.
- **Nobody opens it.** Your subject line is weak, or your schedule is wrong. Test a plain subject that says what is inside. Send at a time your readers are awake.
- **Costs spike.** A feed with a thousand items is feeding Claude too much. Limit each feed to its ten newest items.

> TRY IT: Pick five feeds you love and run a dry run today. Read the draft issue. If you would enjoy receiving it, your newsletter is ready to send to three friends. Ask them what they think. Their answers are your next edits.

## Check yourself

1. What is a dry run, and why should you run one first?
**Answer:** A test that builds the email without sending it, so you can check it safely and cheaply.

2. Why does the kit use structured output from Claude?
**Answer:** So the newsletter comes back as clean data with named fields, which is easy to turn into an email.

3. Why should a human review the draft before it is sent?
**Answer:** To catch bad picks, typos, and tone problems before readers see them.

4. What schedule should you pick for a newsletter?
**Answer:** One you can keep for a year, even if that means fortnightly or monthly instead of weekly.

## In short

- A newsletter pipeline reads feeds, picks the best items, writes notes, and sends an email.
- Test with a dry run first, then choose five to ten feeds you actually read.
- Give the newsletter a voice, sections, and a simple design.
- Send a test to yourself, then to three friends, then to your full list.
- Put it on autopilot with a human review between draft and send.
- Pick a schedule you can keep for a year.
