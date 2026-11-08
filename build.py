"""Build The AI Field Guide (full book) from Markdown sources in src/.

Usage:  ~/workspace/.venv-manual/bin/python build.py
Output: The-AI-Field-Guide.pdf  (Letter, design A — colorful field guide)
        build-report.json       (chapter/word/page counts)

Markdown subset parsed (see writer briefs):
  # Title            chapter / front-matter / appendix heading
  ## Section          section heading (+ hairline)
  paragraphs         body text (**bold**, *italic*, `code`)
  - bullet           bullet list
  1. numbered        numbered list (quiz questions)
  - [ ] item         green checklist
  | a | b |          teal-headed table
  > NOTE: ...        teal margin note
  > TRY IT: ...      amber "Try it" box
  ``` code ```       code block
  **Answer:** ...    quiz answer (italic, indented)
  ## In short        following bullets become a green recap box
  <!-- ... -->       skipped
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    Paragraph, Spacer, PageBreak, NextPageTemplate, Table, TableStyle,
    HRFlowable,
)
from reportlab.platypus.tableofcontents import TableOfContents

import design as D
from design import S
import design_a as A

OUT = os.path.join(HERE, "The-AI-Field-Guide.pdf")
REPORT = os.path.join(HERE, "build-report.json")
SRC = os.path.join(HERE, "src")

SECTIONS = [
    (1, "First Conversations",
     "Meet AI. Talk to it. Learn what it can and cannot do."),
    (2, "The Workshop",
     "The assistants, how AI works, and the tools around it."),
    (3, "A Second Brain",
     "Notes, memory, and AI that knows your stuff."),
    (4, "Building Things",
     "Automation, coding, agents, and making things."),
    (5, "Working With Others",
     "AI for life, work, family, and other people."),
    (6, "Field Exercises",
     "Build-alongs, recipe books, and project ideas."),
]
SECTION_MAP = {n: (t, tag) for n, t, tag in SECTIONS}

# h1 look, top-level outline entry: front matter, glossary, appendices.
H1_TOP = ParagraphStyle("h1_top", parent=S["h1"])

# ---------------------------------------------------------------- ordering
FRONT_RE = re.compile(r"^front-(\d+)-")
CHAP_RE = re.compile(r"^s(\d)-(\d+)-")
APP_RE = re.compile(r"^app-([a-z])-")


def order_key(name):
    m = FRONT_RE.match(name)
    if m:
        return (0, int(m.group(1)), name)
    m = CHAP_RE.match(name)
    if m:
        return (int(m.group(1)), int(m.group(2)), name)
    if name == "glossary.md":
        return (7, 0, name)
    m = APP_RE.match(name)
    if m:
        return (8, ord(m.group(1)), name)
    return (9, 0, name)


# ---------------------------------------------------------------- flowable to set the edge tab
class SetTab(A.Flowable):
    """Zero-height flowable: sets doc.tab (edge-tab colour/label) when
    the page is drawn, so tabs follow the story order on every pass."""
    def __init__(self, doc, tab):
        A.Flowable.__init__(self)
        self.doc = doc
        self.tab = tab
        self.width = 0
        self.height = 0

    def wrap(self, aW, aH):
        return (0, 0)

    def draw(self):
        self.doc.tab = self.tab


def tab_for_section(n):
    colour = A.SECTION_COLOURS[(n - 1) % len(A.SECTION_COLOURS)]
    return (colour, "SECTION %d" % n)


# ---------------------------------------------------------------- markdown parsing
class Chapter:
    def __init__(self, path, kind):
        self.path = path
        self.kind = kind          # front | chapter | glossary | appendix
        self.num = None           # "1.1" / "B" / None
        self.section = None       # int for chapters
        self.title = ""
        self.original = ""
        self.flowables = []
        self.recap = []           # "In short" bullets
        self.words = 0


def _lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()


def _table_widths(header, rows):
    """Column widths proportional to longest cell, with a floor so
    short columns (e.g. a one-word header) never wrap mid-word, and
    a fallback to equal widths when everything is narrow."""
    n = len(header)
    lens = [len(h) for h in header]
    for row in rows:
        for i, cell in enumerate(row):
            lens[i] = max(lens[i], len(cell))
    total = float(sum(lens)) or 1.0
    widths = [A.BODY_W * (ln / total) for ln in lens]
    min_w = 76.0
    for _ in range(5):
        narrow = [i for i, w in enumerate(widths) if w < min_w]
        if not narrow:
            break
        deficit = sum(min_w - widths[i] for i in narrow)
        wide = [i for i, w in enumerate(widths) if w > min_w]
        if not wide:
            break
        take = deficit / len(wide)
        for i in narrow:
            widths[i] = min_w
        for i in wide:
            widths[i] -= take
    if sum(widths) > A.BODY_W + 0.5:
        widths = [A.BODY_W / n] * n
    return widths


def parse_markdown(path, kind, section_num=None):
    """Parse one .md file into flowables. Returns a Chapter."""
    ch = Chapter(path, kind)
    lines = _lines(path)
    i = 0
    n = len(lines)
    in_code = False
    code_lines = []
    in_recap = False
    table_buf = []

    def flush_table():
        nonlocal table_buf
        if not table_buf:
            return
        header = table_buf[0]
        rows = table_buf[1:]
        ch.flowables.append(
            A.colour_table(header, rows, _table_widths(header, rows)))
        ch.flowables.append(Spacer(1, 10))
        table_buf = []

    def flush_code():
        nonlocal code_lines
        if code_lines:
            ch.flowables.append(A.code_block(code_lines))
            ch.flowables.append(Spacer(1, 10))
            code_lines = []

    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        i += 1

        if in_code:
            if line.strip().startswith("```"):
                in_code = False
                flush_code()
            else:
                code_lines.append(line)
            continue
        if line.strip().startswith("```"):
            in_code = True
            code_lines = []
            continue
        if not line.strip():
            flush_table()
            continue
        if line.strip().startswith("<!--"):
            m = re.search(r"original:\s*(.+?)\s*-->", line)
            if m:
                ch.original = m.group(1).strip()
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue  # separator row
            table_buf.append([A.md_inline(c) for c in cells])
            continue
        flush_table()

        # "In short": gather ALL consecutive list items (bullets and
        # checklists) into ONE recap box. `line` holds the current
        # line; `i` is the index of the next unread line. After the
        # group, fall through so the first non-list line is processed
        # by the normal branches below.
        if in_recap and (line.startswith("- ") or
                         line.startswith("- [ ] ") or
                         line.startswith("- [x] ")):
            items = []
            while True:
                if line.startswith("- [ ] ") or line.startswith("- [x] "):
                    items.append(A.md_inline(line[5:].strip()))
                elif line.startswith("- "):
                    items.append(A.md_inline(line[2:].strip()))
                else:
                    break
                if i >= n:
                    line = None
                    break
                line = lines[i].rstrip()
                i += 1
            ch.recap.extend(items)
            ch.flowables.append(A.green_recap_box(items))
            ch.flowables.append(Spacer(1, 10))
            if line is None or not line.strip():
                if line is None:
                    break
                continue
        if line.startswith("# "):
            title = line[2:].strip()
            m = re.match(r"^(\d+\.\d+)\s+(.*)$", title)
            if m:
                ch.num = m.group(1)
                ch.title = m.group(2)
                ch.section = int(ch.num.split(".")[0])
            elif title.lower().startswith("appendix"):
                m2 = re.match(r"^Appendix\s+([A-J])\s+[—–-]\s+(.*)$",
                              title, re.I)
                if m2:
                    ch.num = m2.group(1).upper()
                    ch.title = m2.group(2)
                else:
                    ch.title = title
            elif title.lower() == "glossary":
                ch.num = "A"
                ch.title = "Glossary"
            else:
                ch.title = title
            continue
        if line.startswith("## "):
            head = line[3:].strip()
            if head.lower() == "in short":
                in_recap = True
                continue
            in_recap = False
            colour = A.GREEN if head.lower() == "check yourself" \
                else A.VERMILION
            ch.flowables.append(Paragraph(A.md_inline(head), S["h2"]))
            ch.flowables.append(D.hairline(space_after=10, color=colour,
                                           thickness=1.2))
            continue
        if line.startswith("> "):
            # Gather the whole blockquote.
            parts = [line[2:].strip()]
            while i < n and lines[i].startswith("> "):
                parts.append(lines[i][2:].strip())
                i += 1
            text = " ".join(parts)
            if text.startswith("NOTE:"):
                ch.flowables.append(
                    A.MarginNoteTeal(A.md_inline(text[5:].strip())))
            elif text.startswith("TRY IT:"):
                ch.flowables.append(
                    A.amber_try_it_box("Try it",
                                       A.md_inline(text[7:].strip())))
                ch.flowables.append(Spacer(1, 10))
            else:
                ch.flowables.append(
                    Paragraph(A.md_inline(text), S["body"]))
            continue
        if line.startswith("- [ ] ") or line.startswith("- [x] "):
            items = [A.md_inline(line[5:].strip())]
            while i < n and (lines[i].startswith("- [ ] ") or
                             lines[i].startswith("- [x] ")):
                items.append(A.md_inline(lines[i][5:].strip()))
                i += 1
            if in_recap:
                ch.recap.extend(items)
                ch.flowables.append(A.green_recap_box(items))
                ch.flowables.append(Spacer(1, 10))
            else:
                ch.flowables.extend(A.green_checklist(items))
            continue
        if line.startswith("- "):
            items = [line[2:].strip()]
            while i < n and lines[i].startswith("- ") and not (
                    lines[i].startswith("- [ ] ") or
                    lines[i].startswith("- [x] ")):
                items.append(lines[i][2:].strip())
                i += 1
            if in_recap:
                ch.recap.extend([A.md_inline(t) for t in items])
                ch.flowables.append(
                    A.green_recap_box([A.md_inline(t) for t in items]))
                ch.flowables.append(Spacer(1, 10))
            else:
                for t in items:
                    ch.flowables.append(Paragraph(
                        "\u2022&nbsp;&nbsp;" + A.md_inline(t), S["bullet"]))
            continue
        m = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m:
            ch.flowables.append(Paragraph(
                "<b>%s.</b>&nbsp;&nbsp;%s" % (m.group(1),
                                              A.md_inline(m.group(2))),
                S["numbered"]))
            continue
        # Plain paragraph.
        in_recap = False
        if line.startswith("**Answer:**"):
            ch.flowables.append(Paragraph(A.md_inline(line), S["answer"]))
        else:
            ch.flowables.append(Paragraph(A.md_inline(line), S["body"]))
        ch.words += len(line.split())

    flush_table()
    flush_code()
    return ch


# ---------------------------------------------------------------- glossary rendering
def glossary_flowables(ch):
    """Render glossary.md entries grouped by letter."""
    out = []
    entries = []
    for fl in ch.flowables:
        if isinstance(fl, Paragraph):
            entries.append(fl.text)
    # Re-parse the raw file: entries are "**Term** — def. *First seen ...*"
    entries = []
    for line in _lines(ch.path):
        line = line.strip()
        if line.startswith("**") and "—" in line:
            entries.append(line)
    entries.sort(key=lambda e: re.sub(r"\*\*", "", e).lower())
    letter = None
    for e in entries:
        first = re.sub(r"^\*\*", "", e).strip()[0].upper()
        if first != letter:
            letter = first
            out.append(Paragraph(letter, S["gloss_letter"]))
        out.append(Paragraph(A.md_inline(e), S["gloss_entry_a"]))
    return out, len(entries)


# ---------------------------------------------------------------- cover
def cover_story():
    st = []
    st.append(Spacer(1, 10))
    st.append(A.p("A FIELD NOTEBOOK FOR EVERYDAY PEOPLE", "cover_eyebrow"))
    st.append(A.p("The AI<br/>Field Guide", "cover_title"))
    st.append(D.hairline(width=120, color=A.VERMILION, thickness=1.2,
                         space_before=4, space_after=12))
    st[-1].hAlign = "CENTER"
    st.append(A.p("A friendly handbook for using AI, even if you have "
                  "never tried it before.", "cover_sub"))
    st.append(Spacer(1, 10))
    sketch = A.ColourSketch(width=220, height=150)
    t = Table([[sketch]], colWidths=[468])
    t.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    st.append(t)
    st.append(Spacer(1, 10))
    st.append(A.p("<b>What this book is.</b> &nbsp;This is a notebook, not a "
                  "textbook. It walks you through AI one small step at a "
                  "time, in plain words. You will try things as you read, "
                  "and by the end you will know what AI can do for you "
                  "and where it still needs a human eye.", "cover_what"))
    st.append(Spacer(1, 12))
    st.append(A.whats_inside_strip(
        [("One", "First Conversations", "meet AI, have your first chats"),
         ("Two", "The Workshop", "assistants, how AI works, tools"),
         ("Three", "A Second Brain", "notes, memory, your own files"),
         ("Four", "Building Things", "automation, coding, agents"),
         ("Five", "Working With Others", "AI for life, work, family"),
         ("Six", "Field Exercises", "build-alongs and projects")]))
    st.append(Spacer(1, 12))
    st.append(A.colour_key_strip())
    st.append(Spacer(1, 14))
    st.append(A.p("Written by Muse", "cover_author"))
    st.append(A.p("November 2026", "cover_date"))
    return st


# ---------------------------------------------------------------- chapter heading
def chapter_heading(ch):
    out = []
    if ch.kind == "chapter":
        eyebrow = ("CHAPTER %s &middot; SECTION %d &mdash; %s" % (
            ch.num, ch.section,
            SECTION_MAP[ch.section][0].upper()))
        out.append(Paragraph(eyebrow, S["eyebrow"]))
    elif ch.kind == "appendix":
        out.append(Paragraph("APPENDIX %s" % ch.num, S["eyebrow"]))
    elif ch.kind == "glossary":
        out.append(Paragraph("APPENDIX A &middot; GLOSSARY", S["eyebrow"]))
    else:
        out.append(Paragraph("BEFORE WE BEGIN", S["eyebrow"]))
    h1_style = S["h1"] if ch.kind == "chapter" else H1_TOP
    out.append(Paragraph(A.md_inline(ch.title), h1_style))
    out.append(D.hairline(space_after=12, color=A.VERMILION, thickness=1.2))
    return out


def section_opener(num, chapters):
    title, tagline = SECTION_MAP[num]
    colour = A.SECTION_COLOURS[(num - 1) % len(A.SECTION_COLOURS)]
    out = []
    out.append(Spacer(1, 30))
    num_style = ParagraphStyle("section_num_c", parent=S["section_num"],
                               textColor=colour)
    out.append(Paragraph("Section %d" % num, S["eyebrow"]))
    out.append(Paragraph(str(num), num_style))
    out.append(Paragraph(title, S["section_title"]))
    out.append(D.hairline(width=A.SECTION_W, color=colour, thickness=1.2,
                          space_after=14))
    out.append(Paragraph(tagline, S["section_intro"]))
    rows = []
    for c in chapters:
        rows.append([Paragraph(c.num, S["map_num"]),
                     Paragraph(A.md_inline(c.title), S["map_title"])])
    t = Table(rows, colWidths=[52, A.SECTION_W - 52])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -2), 0.4, A.FAINT),
    ]))
    out.append(t)
    return out


# ---------------------------------------------------------------- main build
def main():
    names = sorted((f for f in os.listdir(SRC) if f.endswith(".md")),
                   key=order_key)
    chapters = []
    for name in names:
        path = os.path.join(SRC, name)
        if name.startswith("front-"):
            kind = "front"
        elif name.startswith("s"):
            kind = "chapter"
        elif name == "glossary.md":
            kind = "glossary"
        else:
            kind = "appendix"
        ch = parse_markdown(path, kind)
        chapters.append(ch)
        print("parsed %-42s %-9s %6d words  recap=%d" % (
            name, kind, ch.words, len(ch.recap)))

    front = [c for c in chapters if c.kind == "front"]
    sections = {}
    for c in chapters:
        if c.kind == "chapter":
            sections.setdefault(c.section, []).append(c)
    glossary = next((c for c in chapters if c.kind == "glossary"), None)
    appendices = [c for c in chapters if c.kind == "appendix"]

    doc = A.FieldDocA(OUT)
    story = []

    # Cover.
    story.extend(cover_story())

    # Contents (section template, full width).
    story.append(SetTab(doc, None))
    story.append(NextPageTemplate("section"))
    story.append(PageBreak())
    story.append(Paragraph("Contents", S["contents_title"]))
    story.append(D.hairline(width=A.SECTION_W, color=A.VERMILION,
                            thickness=1.2, space_after=12))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("toc0", fontName="Serif-Bold", fontSize=13,
                       leading=18, textColor=A.VERMILION, leftIndent=0,
                       firstLineIndent=0, spaceBefore=10),
        ParagraphStyle("toc1", fontName="Serif", fontSize=11,
                       leading=15, textColor=A.INK, leftIndent=12,
                       firstLineIndent=0, spaceBefore=1),
    ]
    story.append(toc)

    # Front matter.
    story.append(SetTab(doc, None))
    story.append(NextPageTemplate("main"))
    for idx, ch in enumerate(front):
        if idx:
            story.append(PageBreak())
        else:
            story.append(PageBreak())
        story.extend(chapter_heading(ch))
        story.extend(ch.flowables)

    # Sections + chapters.
    for num in sorted(sections):
        story.append(SetTab(doc, tab_for_section(num)))
        story.append(NextPageTemplate("section"))
        story.append(PageBreak())
        story.extend(section_opener(num, sections[num]))
        story.append(NextPageTemplate("main"))
        for ch in sections[num]:
            story.append(PageBreak())
            story.extend(chapter_heading(ch))
            story.extend(ch.flowables)
            story.append(Spacer(1, 6))

    # Glossary.
    if glossary:
        story.append(SetTab(doc, (A.GREEN, "GLOSSARY")))
        story.append(NextPageTemplate("main"))
        story.append(PageBreak())
        story.extend(chapter_heading(glossary))
        gloss_flows, gloss_count = glossary_flowables(glossary)
        story.extend(gloss_flows)
    else:
        gloss_count = 0

    # Appendices B, C, D, E, then G (generated), then H, I, J.
    app_order = ["B", "C", "D", "E", "H", "I", "J"]
    app_by_letter = {c.num: c for c in appendices}
    recaps = [(c.num, c.title, c.recap) for c in chapters
              if c.kind == "chapter" and c.recap]
    for letter in app_order:
        ch = app_by_letter.get(letter)
        if not ch:
            print("WARNING: appendix %s missing" % letter)
            continue
        story.append(SetTab(doc, (A.AMBER, "APPENDIX %s" % letter)))
        story.append(NextPageTemplate("main"))
        story.append(PageBreak())
        story.extend(chapter_heading(ch))
        story.extend(ch.flowables)
        if letter == "E":
            # Appendix G — the key points edition, generated from recaps.
            story.append(SetTab(doc, (A.AMBER, "APPENDIX G")))
            story.append(PageBreak())
            story.append(Paragraph("APPENDIX G", S["eyebrow"]))
            story.append(Paragraph("The key points edition",
                                   H1_TOP))
            story.append(D.hairline(space_after=12, color=A.VERMILION,
                                    thickness=1.2))
            story.append(Paragraph(
                "Every chapter's main points, on as few pages as possible.",
                S["body"]))
            for num, title, items in recaps:
                story.append(Paragraph(
                    "<b>%s &mdash; %s</b>" % (num, A.md_inline(title)),
                    S["h2"]))
                story.append(D.hairline(space_after=8, color=A.GREEN,
                                        thickness=1.2))
                for it in items:
                    story.append(Paragraph("\u2022&nbsp;&nbsp;" + it,
                                           S["bullet"]))

    doc.multiBuild(story)
    total_words = sum(c.words for c in chapters)
    n_chapters = len([c for c in chapters if c.kind == "chapter"])
    report = {
        "pdf": OUT,
        "files": names,
        "chapters": n_chapters,
        "front_matter": len(front),
        "appendices": sorted(app_by_letter.keys()),
        "glossary_entries": gloss_count,
        "total_words": total_words,
        "recap_chapters": len(recaps),
    }
    with open(REPORT, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print("Wrote", OUT)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
