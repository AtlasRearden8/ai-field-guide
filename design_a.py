"""Design A — "colorful field guide" for The AI Field Guide (full book).

Adapted from variants/a/build_a.py (the approved 3-page sample) and
extended for the full book: section template + section opener, cover
that fills the page ("What's inside" strip), code blocks, recap boxes,
and PDF outline (TOC) notifications.

Palette (flat colours only — no purple, no gradients):
    paper     #F7F3EA  warm cream
    ink       #1A1714  near-black text
    vermilion #C2410F  chapters / rules / chapter tab
    teal      #0F766E  margin notes / table header
    amber     #B45309  "Try it" box
    green     #166534  checklists / recap / diagrams
Light tints (flat fills) for diagram boxes, Try-it box, table header.

Run:  ~/workspace/.venv-manual/bin/python build.py
Output: The-AI-Field-Guide.pdf
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Flowable,
    Table, TableStyle, NextPageTemplate, PageBreak, Spacer,
    HRFlowable,
)

import design as D
from design import S

# ---------------------------------------------------------------- palette
PAPER = D.PAPER
INK = D.INK
VERMILION = HexColor("#C2410F")
TEAL = HexColor("#0F766E")
AMBER = HexColor("#B45309")
GREEN = HexColor("#166534")
SOFT_INK = D.SOFT_INK
FAINT = D.FAINT

TINT_VERMILION = HexColor("#FFEDD5")
TINT_TEAL = HexColor("#CCFBF1")
TINT_AMBER = HexColor("#FEF3C7")
TINT_GREEN = HexColor("#DCFCE7")
TINT_CODE = HexColor("#EFE9DB")
WHITE = HexColor("#FFFFFF")

PAGE_W, PAGE_H = LETTER
LEFT, BODY_W = D.LEFT, D.BODY_W
GAP, MARGIN_X, MARGIN_W = D.GAP, D.MARGIN_X, D.MARGIN_W
FRAME_TOP, FRAME_BOT, FRAME_H = D.FRAME_TOP, D.FRAME_BOT, D.FRAME_H
SECTION_LEFT = LEFT
SECTION_W = PAGE_W - 2 * LEFT

# Section colours, cycled for edge tabs and section openers.
SECTION_COLOURS = [VERMILION, TEAL, AMBER, GREEN, VERMILION, TEAL]

# ---------------------------------------------------------------- extra styles
S["margin_note_teal"] = ParagraphStyle(
    "margin_note_teal", fontName="Serif-Italic", fontSize=9, leading=12.5,
    textColor=TEAL)
S["tryit_head_amber"] = ParagraphStyle(
    "tryit_head_amber", fontName="Serif-Bold", fontSize=10.5, leading=13,
    textColor=AMBER, spaceAfter=5)
S["check_item_green"] = ParagraphStyle(
    "check_item_green", fontName="Serif", fontSize=11.5, leading=17,
    textColor=INK, spaceAfter=9)
S["table_head_teal"] = ParagraphStyle(
    "table_head_teal", fontName="Serif-Bold", fontSize=11, leading=14,
    textColor=TEAL)
S["legend"] = ParagraphStyle(
    "legend", fontName="Serif-Bold", fontSize=8, leading=11,
    textColor=SOFT_INK, alignment=TA_CENTER)
S["gloss_entry_a"] = ParagraphStyle(
    "gloss_entry_a", fontName="Serif", fontSize=11.5, leading=16.5,
    textColor=INK, leftIndent=14, spaceAfter=7)
S["cover_tab_label"] = ParagraphStyle(
    "cover_tab_label", fontName="Serif-Bold", fontSize=8, leading=10,
    textColor=SOFT_INK, alignment=TA_CENTER)
S["answer"] = ParagraphStyle(
    "answer", fontName="Serif-Italic", fontSize=11, leading=16,
    textColor=INK, leftIndent=18, spaceAfter=8)
S["bullet"] = ParagraphStyle(
    "bullet", parent=S["body"], leftIndent=16, firstLineIndent=0,
    bulletIndent=6, spaceAfter=6)
S["numbered"] = ParagraphStyle(
    "numbered", parent=S["body"], leftIndent=22, firstLineIndent=0,
    spaceAfter=6)
S["code_line"] = ParagraphStyle(
    "code_line", fontName="Courier", fontSize=9.5, leading=13,
    textColor=INK, leftIndent=0, spaceAfter=0)
S["recap_head"] = ParagraphStyle(
    "recap_head", fontName="Serif-Bold", fontSize=10.5, leading=13,
    textColor=GREEN, spaceAfter=5)
S["recap_item"] = ParagraphStyle(
    "recap_item", fontName="Serif", fontSize=11, leading=16,
    textColor=INK, leftIndent=16, spaceAfter=4)
S["section_num"] = ParagraphStyle(
    "section_num", fontName="Serif-Bold", fontSize=84, leading=84,
    textColor=VERMILION, spaceAfter=2)
S["section_title"] = ParagraphStyle(
    "section_title", fontName="Serif-Bold", fontSize=34, leading=38,
    textColor=INK, spaceAfter=12)
S["section_intro"] = ParagraphStyle(
    "section_intro", fontName="Serif", fontSize=12.5, leading=19,
    textColor=INK, spaceAfter=18)
S["map_num"] = ParagraphStyle(
    "map_num", fontName="Serif-Bold", fontSize=13, leading=16,
    textColor=VERMILION, alignment=TA_LEFT)
S["map_title"] = ParagraphStyle(
    "map_title", fontName="Serif", fontSize=11.5, leading=16,
    textColor=INK, spaceAfter=0)
S["contents_title"] = ParagraphStyle(
    "contents_title", fontName="Serif-Bold", fontSize=28, leading=33,
    textColor=INK, spaceAfter=6)
S["toc_section"] = ParagraphStyle(
    "toc_section", fontName="Serif-Bold", fontSize=13, leading=17,
    textColor=VERMILION, spaceBefore=10, spaceAfter=2)
S["whats_inside"] = ParagraphStyle(
    "whats_inside", fontName="Serif", fontSize=10.5, leading=15,
    textColor=INK, alignment=TA_LEFT, spaceAfter=4)
S["cover_section_head"] = ParagraphStyle(
    "cover_section_head", fontName="Serif-Bold", fontSize=10,
    leading=13, textColor=VERMILION, alignment=TA_CENTER, spaceAfter=8)


def p(text, style="body"):
    return Paragraph(text, S[style])


# ---------------------------------------------------------------- teal margin notes
_margin_last_bottom = {}


def reset_margin_state(page):
    _margin_last_bottom[page] = FRAME_TOP + 8


class MarginNoteTeal(Flowable):
    """Teal margin note: teal tick + teal italic text in the margin column."""
    def __init__(self, text):
        Flowable.__init__(self)
        self.text = text
        self.width = 0
        self.height = 0

    def wrap(self, aW, aH):
        return (0, 0)

    def draw(self):
        c = self.canv
        page = c.getPageNumber()
        par = Paragraph(self.text, S["margin_note_teal"])
        w, h = par.wrap(MARGIN_W, FRAME_H)
        x_abs, y_abs = c.absolutePosition(0, 0)
        top = y_abs + 2
        last_bottom = _margin_last_bottom.get(page, FRAME_BOT)
        if top > last_bottom - 8:
            top = last_bottom - 8
        bottom = top - h
        x_rel = MARGIN_X - x_abs
        y_rel = bottom - y_abs
        c.saveState()
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.4)
        c.line(x_rel, y_rel + h + 5, x_rel + 14, y_rel + h + 5)
        c.restoreState()
        par.drawOn(c, x_rel, y_rel)
        _margin_last_bottom[page] = bottom


# ---------------------------------------------------------------- coloured step diagram
class ColourStepDiagram(Flowable):
    """Ask -> Answer -> Check. Ask = vermilion tint, Answer = teal tint,
    Check = green tint."""
    def __init__(self, labels=("Ask", "Answer", "Check"), width=BODY_W,
                 height=64):
        Flowable.__init__(self)
        self.labels = labels
        self.width = width
        self.height = height

    def wrap(self, aW, aH):
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        colours = [(VERMILION, TINT_VERMILION), (TEAL, TINT_TEAL),
                   (GREEN, TINT_GREEN)]
        box_w, box_h = 92, 34
        gap = (self.width - 3 * box_w) / 2
        y0 = (self.height - box_h) / 2
        c.saveState()
        for i, label in enumerate(self.labels):
            colour, tint = colours[i % 3]
            x0 = i * (box_w + gap)
            c.setFillColor(tint)
            c.setStrokeColor(colour)
            c.setLineWidth(1.2)
            c.rect(x0, y0, box_w, box_h, stroke=1, fill=1)
            c.setFillColor(colour)
            c.setFont("Serif-Bold", 10.5)
            c.drawCentredString(x0 + box_w / 2, y0 + 13, label)
            if i < 2:
                ax0 = x0 + box_w + 3
                ax1 = x0 + box_w + gap - 3
                ay = y0 + box_h / 2
                c.setStrokeColor(INK)
                c.setLineWidth(0.9)
                c.line(ax0, ay, ax1, ay)
                c.line(ax1, ay, ax1 - 6, ay + 3.5)
                c.line(ax1, ay, ax1 - 6, ay - 3.5)
        c.restoreState()


# ---------------------------------------------------------------- boxes
def amber_try_it_box(heading, body_text):
    inner = [
        Paragraph(heading.upper(), S["tryit_head_amber"]),
        Paragraph(body_text, S["tryit_body"]),
    ]
    t = Table([[inner]], colWidths=[BODY_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TINT_AMBER),
        ("BOX", (0, 0), (-1, -1), 0.75, AMBER),
        ("LINEBEFORE", (0, 0), (0, 0), 4, AMBER),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def green_recap_box(items):
    """'In short' recap: green-tinted box, green left rule."""
    inner = [Paragraph("IN SHORT", S["recap_head"])]
    for it in items:
        inner.append(Paragraph("\u2022&nbsp;&nbsp;" + it, S["recap_item"]))
    t = Table([[inner]], colWidths=[BODY_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TINT_GREEN),
        ("BOX", (0, 0), (-1, -1), 0.75, GREEN),
        ("LINEBEFORE", (0, 0), (0, 0), 4, GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def code_block(lines):
    """Short code block: warm tint, thin ink border, Courier lines."""
    inner = [Paragraph(_esc(line) if line.strip() else "&nbsp;",
                       S["code_line"]) for line in lines]
    t = Table([[inner]], colWidths=[BODY_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TINT_CODE),
        ("BOX", (0, 0), (-1, -1), 0.5, INK),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


# ---------------------------------------------------------------- teal-headed table
def colour_table(header, rows, col_widths=None):
    data = [[Paragraph(h, S["table_head_teal"]) for h in header]]
    for row in rows:
        data.append([Paragraph(cell, S["table_cell"]) for cell in row])
    if col_widths is None:
        n = len(header)
        w = BODY_W / n
        col_widths = [w] * n
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TINT_TEAL),
        ("LINEABOVE", (0, 0), (-1, 0), 1.2, TEAL),
        ("LINEBELOW", (0, 0), (-1, 0), 1.2, TEAL),
        ("LINEBELOW", (0, -1), (-1, -1), 1.2, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
    for i in range(1, len(data) - 1):
        style.append(("LINEBELOW", (0, i), (-1, i), 0.5, FAINT))
    t.setStyle(TableStyle(style))
    return t


# ---------------------------------------------------------------- green checklist
def green_checklist(items):
    out = []
    for it in items:
        out.append(Paragraph(
            '<font name="Sym" color="#166534">\u2610</font>&nbsp;&nbsp;' + it,
            S["check_item_green"]))
    return out


# ---------------------------------------------------------------- coloured cover sketch
class ColourSketch(Flowable):
    """Notebook sketch in colour: forest-green notebook, teal spiral,
    amber ruled highlight, vermilion compass needle."""
    def __init__(self, width=220, height=150):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def wrap(self, aW, aH):
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        c.saveState()
        c.setStrokeColor(GREEN)
        c.setFillColor(INK)
        c.setLineWidth(1.4)
        c.rect(30, 10, 160, 130, stroke=1, fill=0)
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.2)
        for y in (28, 52, 76, 100, 124):
            c.circle(30, y, 5, stroke=1, fill=0)
        c.setStrokeColor(SOFT_INK)
        c.setLineWidth(0.5)
        for y in (112, 92, 72, 52, 32):
            c.line(46, y, 178, y)
        c.setStrokeColor(AMBER)
        c.setLineWidth(1.4)
        c.line(46, 112, 120, 112)
        c.setStrokeColor(INK)
        c.setLineWidth(1.1)
        c.line(46, 92, 150, 92)
        cx, cy, r = 168, 30, 16
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.1)
        c.circle(cx, cy, r, stroke=1, fill=0)
        c.setStrokeColor(VERMILION)
        c.setLineWidth(1.4)
        c.line(cx, cy, cx + 9, cy + 9)
        c.setStrokeColor(INK)
        c.setLineWidth(0.9)
        c.line(cx, cy, cx - 7, cy - 7)
        c.circle(cx, cy, 1.6, stroke=0, fill=1)
        c.restoreState()


def colour_key_strip():
    """Four flat colour swatches with a one-word label each."""
    cells = []
    for colour, label in ((VERMILION, "CHAPTERS"), (TEAL, "NOTES"),
                          (AMBER, "TRY IT"), (GREEN, "CHECKLISTS")):
        cells.append([Paragraph(
            '<font color="#%s">\u25a0</font>&nbsp; %s' % (
                colour.hexval()[2:], label), S["legend"])])
    t = Table([cells], colWidths=[117, 117, 117, 117])
    t.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def whats_inside_strip(sections):
    """Cover filler: 'WHAT'S INSIDE' + six section rows with colour dots.
    Fixes the variant's empty bottom half."""
    rows = [[Paragraph("WHAT'S INSIDE", S["cover_section_head"])]]
    for i, (num, title, tagline) in enumerate(sections):
        colour = SECTION_COLOURS[i % len(SECTION_COLOURS)]
        rows.append([Paragraph(
            '<font color="#%s">\u25cf</font>&nbsp;&nbsp;<b>%s &mdash; %s</b>'
            '&nbsp;&nbsp;%s' % (colour.hexval()[2:], num, title, tagline),
            S["whats_inside"])])
    t = Table(rows, colWidths=[468])
    t.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ("LINEABOVE", (0, 0), (-1, 0), 0.75, VERMILION),
        ("LINEBELOW", (0, -1), (-1, -1), 0.75, VERMILION),
    ]))
    return t


# ---------------------------------------------------------------- inline markup helpers
def _esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def md_inline(text):
    """Convert a small Markdown inline subset to ReportLab markup:
    **bold**, *italic*, `code`. Escapes everything else."""
    import re
    # Protect code spans first.
    codes = []

    def _code(m):
        codes.append(m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)

    text = re.sub(r"`([^`]+)`", _code, text)
    text = _esc(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", text)
    for i, code in enumerate(codes):
        text = text.replace("\x00%d\x00" % i,
                            '<font face="Courier" size="10">%s</font>'
                            % _esc(code))
    return text


# ---------------------------------------------------------------- page drawing
def _cream(c):
    c.saveState()
    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.restoreState()


def _edge_tab(c, colour, label):
    """Coloured tab on the right page edge with a vertical white label."""
    c.saveState()
    c.setFillColor(colour)
    c.rect(PAGE_W - 16, 600, 16, 84, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Serif-Bold", 8.5)
    c.saveState()
    c.translate(PAGE_W - 8, 642)
    c.rotate(90)
    c.drawCentredString(0, 0, label)
    c.restoreState()
    c.restoreState()


def _footer(c, page_num):
    c.saveState()
    c.setStrokeColor(INK)
    c.setLineWidth(0.5)
    c.line(LEFT, 40, LEFT + BODY_W + GAP + MARGIN_W, 40)
    c.setFont("Serif", 8.5)
    c.setFillColor(SOFT_INK)
    c.drawString(LEFT, 28, "The AI Field Guide")
    c.setFillColor(VERMILION)
    c.setFont("Serif-Bold", 9)
    c.drawRightString(LEFT + BODY_W + GAP + MARGIN_W, 28, str(page_num))
    c.restoreState()


def _top_label(c):
    c.saveState()
    c.setFillColor(TEAL)
    c.rect(LEFT, 754, 9, 9, stroke=0, fill=1)
    c.setFont("Serif-Bold", 8.5)
    c.setFillColor(SOFT_INK)
    c.drawString(LEFT + 14, 754, "THE AI FIELD GUIDE")
    c.setStrokeColor(FAINT)
    c.setLineWidth(0.5)
    c.line(LEFT, 748, LEFT + BODY_W + GAP + MARGIN_W, 748)
    c.restoreState()


def on_page_cover(c, doc):
    _cream(c)
    c.saveState()
    c.setStrokeColor(INK)
    c.setLineWidth(0.75)
    c.rect(36, 36, PAGE_W - 72, PAGE_H - 72, stroke=1, fill=0)
    c.restoreState()
    _edge_tab(c, VERMILION, "FIELD GUIDE")


def on_page_section(c, doc):
    _cream(c)
    _footer(c, c.getPageNumber())
    tab = getattr(doc, "tab", None)
    if tab:
        _edge_tab(c, tab[0], tab[1])


def on_page_main(c, doc):
    _cream(c)
    reset_margin_state(c.getPageNumber())
    c.saveState()
    c.setStrokeColor(FAINT)
    c.setLineWidth(0.5)
    c.line(MARGIN_X - GAP / 2, FRAME_BOT, MARGIN_X - GAP / 2, FRAME_TOP)
    c.restoreState()
    _top_label(c)
    _footer(c, c.getPageNumber())
    tab = getattr(doc, "tab", None)
    if tab:
        _edge_tab(c, tab[0], tab[1])


class FieldDocA(BaseDocTemplate):
    """Full-book document: cover / section / main templates, with
    afterFlowable notifications so build.py can drive a TOC via
    multiBuild. `doc.tab` is a (colour, label) tuple set by build.py
    before each section's pages."""

    def __init__(self, filename):
        super().__init__(filename, pagesize=LETTER,
                         leftMargin=LEFT, rightMargin=LEFT,
                         topMargin=PAGE_H - FRAME_TOP,
                         bottomMargin=FRAME_BOT,
                         title="The AI Field Guide",
                         author="Muse")
        self.tab = None
        frame_cover = Frame(72, 72, PAGE_W - 144, PAGE_H - 144, id="cover")
        frame_section = Frame(SECTION_LEFT, 60, SECTION_W, PAGE_H - 120,
                              id="section")
        frame_main = Frame(LEFT, FRAME_BOT, BODY_W, FRAME_H, id="main")
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[frame_cover],
                         onPage=on_page_cover),
            PageTemplate(id="section", frames=[frame_section],
                         onPage=on_page_section),
            PageTemplate(id="main", frames=[frame_main],
                         onPage=on_page_main),
        ])

    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            style = flowable.style.name
            text = flowable.getPlainText()
            if style == "h1":
                self.notify("TOCEntry", (1, text, self.page))
                self._bookmark(text, 1)
            elif style == "h1_top":
                # Front matter, glossary, appendices: top-level in the
                # PDF outline (level 0), indented entry in the visible
                # Contents list (level 1) like a chapter.
                self.notify("TOCEntry", (1, text, self.page))
                self._bookmark(text, 0)
            elif style == "section_title":
                self.notify("TOCEntry", (0, text, self.page))
                self._bookmark(text, 0)
            elif style == "contents_title":
                pass

    def _bookmark(self, text, level):
        """Add a real PDF outline (bookmark) entry. Every h1 /
        section_title is the first flowable on a fresh page, so the
        page number is a unique key. Called on every multiBuild
        pass; each pass rebuilds the canvas, so no duplicates land
        in the final file."""
        key = "bm-%d" % self.page
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=0)
