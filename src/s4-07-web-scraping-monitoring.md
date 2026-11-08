# 4.7 Web scraping and monitoring with AI
<!-- original: ch. 51 -->

A huge amount of useful information lives on web pages with no easy way out. Prices. Job posts. Event listings. Government notices. Product restocks. Your competitor's new prices. None of it arrives in your inbox. You have to go and look.

**Web scraping** means collecting information from web pages automatically. **Monitoring** means checking those pages on a schedule and telling you when something changes. AI makes both much easier, because it can read a messy page the way a person does, and pull out exactly what you asked for.

This chapter shows you how to do it politely, legally, and reliably. You will build a price-drop watcher and a news monitor, and you will learn the small Python version too.

## First: is there an API?

Before you scrape anything, ask one question. Does this site offer a proper way to get the data?

Many sites offer an **API**, which is a front door for programs, as you learned in Chapter 4.2. Some offer an **RSS feed**, which is a simple list of new posts that updates itself. Some let you download the data as a spreadsheet. Any of these is better than scraping.

An API is faster, cleaner, and allowed. A feed is simple and stable. Scraping is the fallback, for when the site offers nothing else. Always check the site's help pages, its developer pages, and its footer links first. The words to look for are API, developers, data, export, and feed.

> NOTE: If a site offers an API, use it. Scraping a site that offers an API is like climbing through a window when the front door is open.

## The polite and legal scraping rules

Scraping is powerful, and it has rules. Follow them, and you stay safe and welcome. Break them, and you can get blocked, or worse.

First, read the site's **terms of service**. That is the page of rules you agree to by using the site. Some sites say clearly that automated access is not allowed. If they say that, do not scrape them. Find another source.

Second, respect **robots.txt**. That is a small file on every well-run site, at an address like `example.com/robots.txt`. It says which pages automated visitors should avoid. It is not a law, but it is a clear request. Honour it.

Third, be gentle. Check a page once an hour, not once a second. A human reads one page at a time. Your scraper should act like a polite human, not a flood. If the site slows down or blocks you, stop and wait. That block is the site telling you to slow down.

Fourth, take only what you need. If you need a price, take the price. Do not copy whole articles, whole photo libraries, or other people's work. And never scrape personal data about other people, such as names, emails, or phone numbers, without a clear and lawful reason.

Fifth, check the law where you live. Rules differ by country. Public facts, like a listed price, are usually fine to read. Private data, copyrighted text, and anything behind a login are not. When in doubt, ask a human, or do not scrape it.

## The toolbox

You do not need to write a scraper from scratch. These tools cover almost every job.

**n8n and Make** both have web nodes. The HTTP Request node fetches a page. The HTML Extract node pulls out pieces of it. The AI nodes read the messy result and return clean facts. For most monitoring jobs, this is all you need, and you already know how to use it.

**Browser tools** handle pages that load with JavaScript, where the content appears only after the page runs code. Tools like Playwright and Puppeteer drive a real browser, wait for the page to load, and then read it. They are slower, but they work on pages that simple fetching cannot read.

**Scraping services** do the hard parts for you. Tools like Firecrawl, Apify, and Bright Data fetch pages, handle blocks, and return clean text or structured data. They cost money, so check the current price, but they save hours on stubborn sites.

**AI extraction** is the new star. Instead of writing rules that say "take the third heading on the page", you ask the AI: "Find the price, the product name, and whether it is in stock." The AI reads the page like a person and answers. When the site changes its layout, the AI usually still finds the facts. The old rule-based way breaks every time the site changes.

## AI extraction: from messy page to clean JSON

Here is the core trick. Fetch the page. Send its text to the AI. Ask for JSON back, with the exact labels you want.

A good prompt looks like this: "Read the page text below. Pull out the product name, the price as a number, and whether it is in stock. Answer with JSON only, using the labels name, price, and in_stock. If a fact is missing, write null for that label."

The word **null** means "no value here". Telling the AI to use null stops it from inventing a price when the page does not show one. That is important. An AI that guesses a price is worse than an AI that says it does not know.

Keep the page text short. A whole web page can be very long, and long pages cost more to send to the AI. Strip out the navigation, the adverts, and the footer before you send it. In n8n, the HTML Extract node can pull out just the main content. In Python, a small library can do the same.

> TRY IT: Open any product page in your browser. Copy the main text of the page. Paste it into your favourite chatbot with this prompt: "Pull out the product name and price. Answer with JSON only, using the labels name and price." See how clean the answer is. That is AI extraction, with no tools at all.

## Monitoring and alerts

Scraping once is useful. Scraping on a schedule is a superpower. That is monitoring.

A monitor has four parts. A schedule, such as every morning at 8. A fetch step, which reads the page. A compare step, which checks if anything changed since last time. And an alert, which tells you when it did.

The compare step is where beginners go wrong. Web pages change all the time for boring reasons: adverts rotate, dates update, a banner appears. If you compare the whole page, you will get an alert every day about nothing. Compare only the facts you care about. Store the last price you saw. Compare the new price with the old one. Alert only when the price changes.

Store the last value somewhere simple. A spreadsheet row works. A small file works. A database works. The tool does not matter. What matters is that you compare the new fact with the old fact, not the whole page with the whole page.

## Build: a price-drop watcher in n8n

This build takes about 30 minutes. It watches one product page, and messages you when the price drops below a target you set.

First, add a Schedule Trigger. Set it to run once a day, at a time you will notice, like 8 in the morning.

Next, add an HTTP Request node. Put in the product page address. This fetches the page.

Then add an AI step. Use the prompt from the extraction section above. Ask for the product name and price, in JSON. Set a target price in your head, such as $50. Write it down in the workflow, so the next step can use it.

Then add an IF node. That is a box that sends data down one path or another, based on a condition. The condition is: price is less than your target. If yes, go down the "tell me" path. If no, stop.

On the "tell me" path, add a message node. Send yourself an email, or a Telegram message, with the product name, the new price, and the link. That is the alert.

Test it with a product that is already below your target, so the alert fires at once. Then set the target to a real number, and let it watch. You will get a message only when the price actually drops.

## Build: a news and mentions monitor

This build takes about 20 minutes. It watches for news about a topic you care about, such as your company, your town, or a subject you study.

The trigger is a schedule, once or twice a day. The fetch step reads a news search page, or an RSS feed, for your topic. The AI step reads the results and pulls out the headline, the source, and one sentence that says why it matters. It also drops duplicates and adverts.

Then add a filter. Only items the AI scored as relevant get through. The rest are quietly dropped. The survivors go to a daily digest: one email, with the best three to five items, each with a link.

The trick is the same as before. Compare, filter, and summarise. A monitor that sends you everything is noise. A monitor that sends you the best three items is a gift.

## A tiny Python version

If you like a little code, here is the smallest honest scraper. It uses Python, and two popular libraries. Read each line. The comments explain what it does.

```
import requests
from bs4 import BeautifulSoup

  # Fetch the page, like a browser would.
page = requests.get("https://example.com/product", timeout=10)

  # Turn the page into a shape we can search.
soup = BeautifulSoup(page.text, "html.parser")

  # Find the first heading, and print its text.
print(soup.find("h1").get_text(strip=True))
```

Line one and two load the tools. Line five fetches the page. Line eight turns the page into a searchable shape. Line eleven finds the first big heading and prints it. That is a scraper. Everything else is a fancier version of these five ideas.

> NOTE: Some sites block simple requests like this one. If you get an error, or an empty page, the site may need a real browser. Use a browser tool, or a scraping service, instead of fighting the block.

## Common problems and fixes

The page comes back empty. The site loads its content with JavaScript, after the first fetch. Use a browser tool, or a scraping service that runs JavaScript.

The scraper worked yesterday and broke today. The site changed its layout. If you used AI extraction, it probably still works. If you used fixed rules, update them, or switch to AI extraction.

You get blocked after a few runs. You are checking too often. Slow down to once an hour, or once a day. Add a pause between requests. And check the site's robots.txt again.

The AI invents a price. You did not tell it to use null for missing facts. Add that instruction to your prompt, and test it on a page with no price.

## Check yourself

1. What should you check before you scrape a site?
**Answer:** Whether the site offers an API, an RSS feed, or a download, because those are better than scraping.

2. What is robots.txt?
**Answer:** A small file on a site that says which pages automated visitors should avoid.

3. Why is AI extraction better than fixed rules?
**Answer:** Because the AI reads the page like a person, so it still finds the facts when the site changes its layout.

4. Why should a monitor compare only the facts you care about?
**Answer:** Because whole pages change for boring reasons, and comparing everything would send you false alerts every day.

5. What should the AI write when a fact is missing?
**Answer:** Null, which means no value here, so it does not invent a price.

## In short

- Check for an API, a feed, or a download before you scrape anything.
- Follow the rules: read the terms, respect robots.txt, go slowly, and take only what you need.
- AI extraction turns a messy page into clean JSON, and survives layout changes.
- A good monitor compares one fact, not the whole page, and alerts only on real change.
- Build the price watcher and the news monitor one step at a time, and test each step.
- When a page loads with JavaScript, use a browser tool or a scraping service.
