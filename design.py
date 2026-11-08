"""Design system for "The AI Field Guide" — a field-notebook look.

Deliberately NOT the v2 design (see ~/workspace/manual-v2/DESIGN.md):
no purple, no gradients, no pill chips, no coloured callout boxes, no
cards. One paper colour, one ink, one accent (vermilion).

Palette
    paper    #F7F3EA  warm cream, drawn as a full-page rect on every page
    ink      #1A1714  near-black text and hairlines
    vermilion #C2410F the only accent: rules, numerals, small labels
    faint    #C9C2B2  the quiet vertical rule between body and margin notes

Type
    Liberation Serif throughout (regular / bold / italic / bold-italic).
    DejaVu Sans only for the ballot-box glyph (U+2610), which Liberation
    lacks. Body 11.5pt / 17pt leading, generous margins.

Layout (US Letter, 612 x 792)
    Body frame:   x=60, width 356  (leaves the right side clear)
    Margin notes: x=434, width 96, separated by a faint vertical rule
    Footer: hairline + "The AI Field Guide" left, page number right.
"""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Flowable,
    Table, TableStyle, NextPageTemplate, PageBreak, Spacer,
)
from reportlab.lib.units import inch  # noqa: F401  (kept for builders)

# ---------------------------------------------------------------- palette
PAPER = HexColor("#F7F3EA")
INK = HexColor("#1A1714")
VERMILION = HexColor("#C2410F")
FAINT = HexColor("#C9C2B2")
SOFT_INK = HexColor("#4A443C")   # secondary text (captions, footer)

PAGE_W, PAGE_H = LETTER

# ---------------------------------------------------------------- geometry
LEFT = 60            # body left edge
BODY_W = 356         # body column width
GAP = 18             # gap between body and margin column
MARGIN_X = LEFT + BODY_W + GAP   # 434
MARGIN_W = 96        # margin-note column width
FRAME_TOP = 728      # top of text frames (main template)
FRAME_BOT = 48       # bottom of text frames
FRAME_H = FRAME_TOP - FRAME_BOT

# ---------------------------------------------------------------- fonts
SERIF_DIR = "/usr/share/fonts/truetype/liberation/"
DEJAVU_DIR = "/usr/share/fonts/truetype/dejavu/"

pdfmetrics.registerFont(TTFont("Serif", SERIF_DIR + "LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Bold", SERIF_DIR + "LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif-Italic", SERIF_DIR + "LiberationSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Serif-BoldItalic", SERIF_DIR + "LiberationSerif-BoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("Sym", DEJAVU_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold",
                              italic="Serif-Italic", boldItalic="Serif-BoldItalic")

# ---------------------------------------------------------------- styles
S = {}

S["body"] = ParagraphStyle("body", fontName="Serif", fontSize=11.5,
                           leading=17, textColor=INK, alignment=TA_LEFT,
                           spaceAfter=10)
S["body_last"] = ParagraphStyle("body_last", parent=S["body"], spaceAfter=0)

S["h1"] = ParagraphStyle("h1", fontName="Serif-Bold", fontSize=28,
                         leading=33, textColor=INK, spaceAfter=6)
S["h2"] = ParagraphStyle("h2", fontName="Serif-Bold", fontSize=15,
                         leading=19, textColor=INK, spaceBefore=14,
                         spaceAfter=6)
S["eyebrow"] = ParagraphStyle("eyebrow", fontName="Serif-Bold", fontSize=10,
                              leading=13, textColor=VERMILION, spaceAfter=10)
S["eyebrow_ink"] = ParagraphStyle("eyebrow_ink", parent=S["eyebrow"],
                                  textColor=INK)

S["margin_note"] = ParagraphStyle("margin_note", fontName="Serif-Italic",
                                  fontSize=9, leading=12.5, textColor=INK,
                                  alignment=TA_LEFT, spaceAfter=0)

S["cover_eyebrow"] = ParagraphStyle("cover_eyebrow", fontName="Serif-Bold",
                                    fontSize=11, leading=14,
                                    textColor=VERMILION, alignment=TA_CENTER,
                                    spaceAfter=18)
S["cover_title"] = ParagraphStyle("cover_title", fontName="Serif-Bold",
                                  fontSize=46, leading=50, textColor=INK,
                                  alignment=TA_CENTER, spaceAfter=14)
S["cover_sub"] = ParagraphStyle("cover_sub", fontName="Serif-Italic",
                                fontSize=14.5, leading=20, textColor=INK,
                                alignment=TA_CENTER, spaceAfter=0)
S["cover_what"] = ParagraphStyle("cover_what", fontName="Serif",
                                 fontSize=11.5, leading=17, textColor=INK,
                                 alignment=TA_CENTER, spaceAfter=0)
S["cover_author"] = ParagraphStyle("cover_author", fontName="Serif",
                                   fontSize=12, leading=16, textColor=INK,
                                   alignment=TA_CENTER, spaceAfter=2)
S["cover_date"] = ParagraphStyle("cover_date", fontName="Serif-Italic",
                                 fontSize=11, leading=15, textColor=SOFT_INK,
                                 alignment=TA_CENTER, spaceAfter=0)

S["part_num"] = ParagraphStyle("part_num", fontName="Serif-Bold",
                               fontSize=84, leading=84, textColor=VERMILION,
                               spaceAfter=2)
S["part_title"] = ParagraphStyle("part_title", fontName="Serif-Bold",
                                 fontSize=34, leading=38, textColor=INK,
                                 spaceAfter=12)
S["part_intro"] = ParagraphStyle("part_intro", fontName="Serif",
                                 fontSize=12.5, leading=19, textColor=INK,
                                 spaceAfter=18)
S["map_num"] = ParagraphStyle("map_num", fontName="Serif-Bold", fontSize=20,
                              leading=24, textColor=VERMILION,
                              alignment=TA_CENTER)
S["map_title"] = ParagraphStyle("map_title", fontName="Serif-Bold",
                                fontSize=12.5, leading=16, textColor=INK,
                                spaceAfter=2)
S["map_desc"] = ParagraphStyle("map_desc", fontName="Serif",
                               fontSize=11, leading=15, textColor=SOFT_INK,
                               spaceAfter=0)
S["section_label"] = ParagraphStyle("section_label", fontName="Serif-Bold",
                                    fontSize=10, leading=13,
                                    textColor=VERMILION, spaceAfter=14)

S["tryit_head"] = ParagraphStyle("tryit_head", fontName="Serif-Bold",
                                 fontSize=10.5, leading=13,
                                 textColor=VERMILION, spaceAfter=5)
S["tryit_body"] = ParagraphStyle("tryit_body", fontName="Serif",
                                 fontSize=11, leading=16, textColor=INK,
                                 spaceAfter=0)

S["table_head"] = ParagraphStyle("table_head", fontName="Serif-Bold",
                                 fontSize=11, leading=14, textColor=INK)
S["table_cell"] = ParagraphStyle("table_cell", fontName="Serif",
                                 fontSize=10.5, leading=14.5, textColor=INK)
S["check_item"] = ParagraphStyle("check_item", fontName="Serif",
                                 fontSize=11.5, leading=17, textColor=INK,
                                 leftIndent=0, spaceAfter=9)

S["gloss_letter"] = ParagraphStyle("gloss_letter", fontName="Serif-Bold",
                                   fontSize=14, leading=18,
                                   textColor=VERMILION, spaceBefore=12,
                                   spaceAfter=4)
S["gloss_entry"] = ParagraphStyle("gloss_entry", fontName="Serif",
                                  fontSize=11.5, leading=16.5, textColor=INK,
                                  leftIndent=14, firstLineIndent=0,
                                  spaceAfter=7)

# ---------------------------------------------------------------- rules
def hairline(width=BODY_W, color=INK, thickness=0.5, space_before=0,
             space_after=10):
    """A plain ink hairline (HRFlowable)."""
    from reportlab.platypus import HRFlowable
    return HRFlowable(width=width, thickness=thickness, color=color,
                      spaceBefore=space_before, spaceAfter=space_after,
                      hAlign="LEFT", vAlign="BOTTOM", dash=None)


# ---------------------------------------------------------------- margin notes
# Per-page record of the bottom y of the last margin note drawn, so a
# second note on the same page never overlaps the first. Reset in
# on_page_main() before any flowable on that page is drawn.
_margin_last_bottom = {}


def reset_margin_state(page):
    # Before any note on the page, the "previous note's bottom" is
    # above the frame top, so the first note is never pushed down.
    _margin_last_bottom[page] = FRAME_TOP + 8


class MarginNote(Flowable):
    """Zero-height flowable: draws a short italic note in the outer
    margin column, top-aligned with the body text that follows it.
    Insert it in the story immediately BEFORE the paragraph it annotates.
    Never collides with body text (body frame is 356pt wide; notes live
    at x=434) and never overlaps a previous note on the same page.
    """
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
        p = Paragraph(self.text, S["margin_note"])
        w, h = p.wrap(MARGIN_W, FRAME_H)
        x_abs, y_abs = c.absolutePosition(0, 0)
        # Top of the note sits just above the flowable's y (the top of
        # the paragraph that follows). Small vermilion tick above it.
        # NOTE: drawOn/line use the CURRENT (translated) user space, so
        # the absolute page coordinates must be converted back to
        # coordinates relative to this flowable's origin. Drawing the
        # absolute values directly puts the note off the page.
        top = y_abs + 2
        last_bottom = _margin_last_bottom.get(page, FRAME_BOT)
        # Notes are laid out top-down: in PDF coords y decreases down
        # the page, so a later note must sit BELOW the previous note's
        # bottom (with an 8pt gap). If its top would reach above that,
        # push it down instead of up.
        if top > last_bottom - 8:
            top = last_bottom - 8
        bottom = top - h
        x_rel = MARGIN_X - x_abs
        y_rel = bottom - y_abs
        c.saveState()
        c.setStrokeColor(VERMILION)
        c.setLineWidth(1.2)
        c.line(x_rel, y_rel + h + 5, x_rel + 14, y_rel + h + 5)
        c.restoreState()
        p.drawOn(c, x_rel, y_rel)
        _margin_last_bottom[page] = bottom


# ---------------------------------------------------------------- try-it box
def try_it_box(heading, body_text):
    """Simple box: thin ink border, 3pt vermilion left rule, no fill."""
    inner = [
        Paragraph(heading.upper(), S["tryit_head"]),
        Paragraph(body_text, S["tryit_body"]),
    ]
    t = Table([[inner]], colWidths=[BODY_W])
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 0.5, INK),
        ("LINEBEFORE", (0, 0), (0, 0), 3, VERMILION),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


# ---------------------------------------------------------------- plain table
def plain_table(header, rows, col_widths):
    """Thin ink rules only, no fills, no colour. Header row in bold."""
    data = [[Paragraph(h, S["table_head"]) for h in header]]
    for row in rows:
        data.append([Paragraph(cell, S["table_cell"]) for cell in row])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("LINEABOVE", (0, 0), (-1, 0), 1, INK),
        ("LINEBELOW", (0, 0), (-1, 0), 1, INK),
        ("LINEBELOW", (0, -1), (-1, -1), 1, INK),
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


# ---------------------------------------------------------------- checklist
def checklist(items):
    """Plain lines with empty square boxes (DejaVu Sans glyph)."""
    out = []
    for it in items:
        out.append(Paragraph(
            '<font name="Sym">\u2610</font>&nbsp;&nbsp;' + it,
            S["check_item"]))
    return out


# ---------------------------------------------------------------- sketch drawing
class NotebookSketch(Flowable):
    """A thin-ink notebook sketch for the cover: ruled notebook with a
    spiral binding, a few ruled lines, and a small compass circle.
    Ink lines only, no fill, no colour except the vermilion needle.
    """
    def __init__(self, width=220, height=150):
        Flowable.__init__(self)
        self.width = width
        self.height = height

    def wrap(self, aW, aH):
        return (self.width, self.height)

    def draw(self):
        c = self.canv
        c.saveState()
        c.setStrokeColor(INK)
        c.setFillColor(INK)
        c.setLineWidth(0.9)
        # Notebook body: x 30..190, y 10..140
        c.rect(30, 10, 160, 130, stroke=1, fill=0)
        # Spiral binding: small loops along the left edge
        for y in (28, 52, 76, 100, 124):
            c.circle(30, y, 5, stroke=1, fill=0)
        # Ruled lines inside
        c.setLineWidth(0.5)
        for y in (112, 92, 72, 52, 32):
            c.line(46, y, 178, y)
        # A short "written" line, slightly darker/heavier
        c.setLineWidth(1.1)
        c.line(46, 112, 120, 112)
        c.line(46, 92, 150, 92)
        # Small compass circle, bottom-right, overlapping the notebook edge
        cx, cy, r = 168, 30, 16
        c.setLineWidth(0.9)
        c.circle(cx, cy, r, stroke=1, fill=0)
        c.setStrokeColor(VERMILION)
        c.setLineWidth(1.2)
        c.line(cx, cy, cx + 9, cy + 9)   # needle
        c.setStrokeColor(INK)
        c.setLineWidth(0.9)
        c.line(cx, cy, cx - 7, cy - 7)
        c.circle(cx, cy, 1.6, stroke=0, fill=1)
        c.restoreState()


class StepDiagram(Flowable):
    """Minimal 3-step arrow diagram: three small ink boxes joined by
    arrows. Used on the chapter page to show ask -> answer -> check.
    """
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
        c.saveState()
        c.setStrokeColor(INK)
        c.setFillColor(INK)
        c.setLineWidth(0.8)
        box_w, box_h = 92, 34
        gap = (self.width - 3 * box_w) / 2
        y0 = (self.height - box_h) / 2
        for i, label in enumerate(self.labels):
            x0 = i * (box_w + gap)
            c.rect(x0, y0, box_w, box_h, stroke=1, fill=0)
            c.setFont("Serif-Bold", 10.5)
            c.drawCentredString(x0 + box_w / 2, y0 + 13, label)
            if i < 2:
                ax0 = x0 + box_w + 3
                ax1 = x0 + box_w + gap - 3
                ay = y0 + box_h / 2
                c.setLineWidth(0.8)
                c.line(ax0, ay, ax1, ay)
                c.line(ax1, ay, ax1 - 6, ay + 3.5)
                c.line(ax1, ay, ax1 - 6, ay - 3.5)
        c.restoreState()


# ---------------------------------------------------------------- page drawing
def _cream(c):
    c.saveState()
    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.restoreState()


def _footer(c, page_num):
    c.saveState()
    c.setStrokeColor(INK)
    c.setLineWidth(0.5)
    c.line(LEFT, 40, LEFT + BODY_W + GAP + MARGIN_W, 40)
    c.setFont("Serif", 8.5)
    c.setFillColor(SOFT_INK)
    c.drawString(LEFT, 28, "The AI Field Guide")
    c.drawRightString(LEFT + BODY_W + GAP + MARGIN_W, 28, str(page_num))
    c.restoreState()


def _top_label(c, label="THE AI FIELD GUIDE"):
    c.saveState()
    c.setFont("Serif-Bold", 8.5)
    c.setFillColor(SOFT_INK)
    c.drawString(LEFT, 754, label)
    c.setStrokeColor(FAINT)
    c.setLineWidth(0.5)
    c.line(LEFT, 748, LEFT + BODY_W + GAP + MARGIN_W, 748)
    c.restoreState()


def on_page_cover(c, doc):
    _cream(c)
    # thin ink frame, notebook style
    c.saveState()
    c.setStrokeColor(INK)
    c.setLineWidth(0.75)
    c.rect(36, 36, PAGE_W - 72, PAGE_H - 72, stroke=1, fill=0)
    c.restoreState()


def on_page_section(c, doc):
    _cream(c)
    _footer(c, c.getPageNumber())


def on_page_main(c, doc):
    _cream(c)
    reset_margin_state(c.getPageNumber())
    # faint vertical rule between body and margin column
    c.saveState()
    c.setStrokeColor(FAINT)
    c.setLineWidth(0.5)
    c.line(MARGIN_X - GAP / 2, FRAME_BOT, MARGIN_X - GAP / 2, FRAME_TOP)
    c.restoreState()
    _top_label(c)
    _footer(c, c.getPageNumber())


# ---------------------------------------------------------------- document
class FieldDoc(BaseDocTemplate):
    def __init__(self, filename):
        super().__init__(filename, pagesize=LETTER,
                         leftMargin=LEFT, rightMargin=LEFT,
                         topMargin=PAGE_H - FRAME_TOP,
                         bottomMargin=FRAME_BOT,
                         title="The AI Field Guide",
                         author="Muse")
        frame_cover = Frame(72, 72, PAGE_W - 144, PAGE_H - 144, id="cover")
        frame_section = Frame(LEFT, 60, PAGE_W - 2 * LEFT, PAGE_H - 120,
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
        pass
