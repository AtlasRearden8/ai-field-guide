# The AI Field Guide

A field notebook for people who have never used AI before.

Short sentences. Everyday words. One idea at a time.

## What this book is

A full-length guide to AI, written from scratch in plain language.
It covers the same ground as *The Massive AI Manual*, but in a
completely different design: a colorful field notebook, not a textbook.
Warm cream paper. Ink black. Four flat accents, each with one job:
vermilion for chapters and rules, teal for margin notes, amber for
"Try it" boxes, forest green for checklists and recaps. Coloured
edge tabs down the side. No gradients. No purple.

## Who it is for

Complete beginners. No assumed knowledge.
If you have never talked to an AI before, start on page one.
If you already use one, skip to the section that fits your day.

## What's inside

Six field sections, 129 chapters, plus a glossary and reference appendices:

1. **First Conversations** — meet AI, have your first chats, stay safe.
2. **The Workshop** — the assistants, how AI works, and the tools around it.
3. **A Second Brain** — notes, memory, and AI that knows your stuff.
4. **Building Things** — automation, coding, agents, and making things.
5. **Working With Others** — AI for life, work, family, and other people.
6. **Field Exercises** — build-alongs, recipe books, and project ideas.

Then a **Glossary** at the end: every jargon term, defined in plain words.

The full chapter plan lives in [OUTLINE.md](OUTLINE.md).
Every chapter of the original manual is mapped to its new home there.

## How the book is built

The book is written in Markdown, one file per chapter, under `src/`.
A Python build script (`build.py`) turns those files into the PDF.
It sets the field-notebook design: cream pages, ink text, four
colour accents, margin notes, and roomy type. The design lives in
`design.py` (shared styles) and `design_a.py` (design A: the
colourful field guide). Early design samples live under `variants/`.

To build the PDF (needs reportlab and PyMuPDF installed):

```sh
python3 build.py
```

The finished PDF lands next to the script as
`The-AI-Field-Guide.pdf`, and a `build-report.json` records the
chapter, glossary, and word counts.

## How to read it

Read it front to back, or jump in anywhere.
Each chapter stands on its own and ends with something to try.
The front matter has a "Pick your path" page and a 60-minute
first session if you want a guided start.

## Current as of

**November 2026.**

AI tools change fast. Prices, features, and names in this book were
checked in November 2026. If something looks different on your screen,
the idea still holds — only the buttons moved.

## License

To be decided.
