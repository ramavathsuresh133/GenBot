"""
pdf_export_service.py - PDF Report Generator for GENBOT Summarization
Generates a styled PDF report from bullet points and table data using PyMuPDF (fitz).
PyMuPDF is already installed (requirement: PyMuPDF>=1.23.0).
"""

import io
from datetime import datetime
import fitz  # PyMuPDF


class SummaryPDFExporter:
    """
    Builds a styled A4 PDF report for a GENBOT summarization result.
    Uses PyMuPDF (fitz) which supports full Unicode rendering via embedded fonts.
    """

    # Colours as 0-1 floats for fitz (r, g, b)
    PRIMARY  = (0.10, 0.23, 0.42)   # Dark navy
    ACCENT   = (1.00, 0.60, 0.00)   # Saffron
    WHITE    = (1.00, 1.00, 1.00)
    DARK     = (0.12, 0.12, 0.12)
    ROW_ALT  = (0.95, 0.96, 0.98)   # light grey

    PAGE_W   = 595   # A4 points
    PAGE_H   = 842
    MARGIN   = 40

    def _draw_rect(self, page, x0, y0, x1, y1, fill, stroke=None):
        rect = fitz.Rect(x0, y0, x1, y1)
        page.draw_rect(rect, color=stroke, fill=fill)

    def _text(self, page, x, y, text, fontsize=10, color=None, bold=False):
        if color is None:
            color = self.DARK
        fontname = "hebo" if bold else "helv"
        page.insert_text(
            fitz.Point(x, y), text,
            fontsize=fontsize, color=color, fontname=fontname
        )

    def _text_width(self, text, fontsize=10):
        """Estimate text width in points (approx 0.6 * fontsize per char)."""
        return len(text) * fontsize * 0.52

    def _wrap_text(self, text, max_width, fontsize=10):
        """Simple word-wrap returning list of lines."""
        words = text.split()
        lines, cur = [], ""
        for w in words:
            trial = (cur + " " + w).strip()
            if self._text_width(trial, fontsize) <= max_width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines or [""]

    def _header(self, page, source_name: str, language: str) -> float:
        """Draw govt-style header, return y position after header."""
        W = self.PAGE_W

        # Top navy bar
        self._draw_rect(page, 0, 0, W, 50, fill=self.PRIMARY)

        # Title text
        self._text(page, self.MARGIN, 22, "GENBOT - Strategic Intelligence Division",
                   fontsize=14, color=self.WHITE, bold=True)
        self._text(page, self.MARGIN, 38, "National Strategic Document Analysis Portal",
                   fontsize=9, color=self.WHITE)

        # Accent stripe
        self._draw_rect(page, 0, 50, W, 53, fill=self.ACCENT)

        y = 70
        self._text(page, self.MARGIN, y, "DOCUMENT SUMMARY REPORT",
                   fontsize=13, bold=True)
        y += 20

        # Meta info box
        self._draw_rect(page, self.MARGIN, y, W - self.MARGIN, y + 38,
                        fill=self.ROW_ALT, stroke=self.PRIMARY)
        self._text(page, self.MARGIN + 8, y + 14,
                   f"Source: {source_name[:70]}", fontsize=9)
        self._text(page, self.MARGIN + 8, y + 28,
                   f"Language: {language}     |     Generated: {datetime.now().strftime('%d %b %Y  %H:%M')}",
                   fontsize=9)

        return y + 50

    def _section_title(self, page, y: float, title: str) -> float:
        """Draw a navy section heading, return y after it."""
        self._draw_rect(page, self.MARGIN, y, self.PAGE_W - self.MARGIN, y + 18,
                        fill=self.PRIMARY)
        self._text(page, self.MARGIN + 6, y + 13, title,
                   fontsize=10, color=self.WHITE, bold=True)
        return y + 22

    def _footer(self, page):
        """Draw footer strip at bottom of page."""
        W, H = self.PAGE_W, self.PAGE_H
        self._draw_rect(page, 0, H - 24, W, H, fill=self.PRIMARY)
        self._text(page, self.MARGIN, H - 8,
                   "GENBOT Strategic Intelligence Division  |  Confidential  |  Auto-generated Report",
                   fontsize=7, color=self.WHITE)

    def build(self, bullets: list, table_data: list, source_name: str, language: str) -> bytes:
        """
        Build and return the PDF as bytes.

        Args:
            bullets    : List of summary bullet strings.
            table_data : List of dicts for the structured table.
            source_name: Document name / URL used as source.
            language   : User-selected language label.

        Returns:
            PDF file content as bytes.
        """
        doc = fitz.open()
        page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)

        content_w = self.PAGE_W - 2 * self.MARGIN
        bottom_limit = self.PAGE_H - 40   # leave room for footer

        y = self._header(page, source_name, language)
        y += 10

        # ── Bullets Section ───────────────────────────────────────────────────
        y = self._section_title(page, y, "KEY SUMMARY POINTS")
        y += 4

        line_h = 16
        for i, bullet in enumerate(bullets):
            # Wrap long bullets
            wrapped = self._wrap_text(f"  -  {bullet}", content_w - 10, fontsize=10)
            block_h = len(wrapped) * line_h + 4

            # New page if needed
            if y + block_h > bottom_limit:
                self._footer(page)
                page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
                self._draw_rect(page, 0, 0, self.PAGE_W, 14, fill=self.PRIMARY)
                y = 24

            fill = self.ROW_ALT if i % 2 == 0 else self.WHITE
            self._draw_rect(page, self.MARGIN, y, self.PAGE_W - self.MARGIN,
                            y + block_h, fill=fill)

            for j, line in enumerate(wrapped):
                self._text(page, self.MARGIN + 6, y + 12 + j * line_h, line, fontsize=10)

            y += block_h + 2

        y += 8

        # ── Table Section ─────────────────────────────────────────────────────
        if table_data:
            cols = list(table_data[0].keys())
            col_w = content_w / len(cols)
            row_h = 16

            if y + 30 > bottom_limit:
                self._footer(page)
                page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
                self._draw_rect(page, 0, 0, self.PAGE_W, 14, fill=self.PRIMARY)
                y = 24

            y = self._section_title(page, y, "STRUCTURED ANALYSIS TABLE")
            y += 4

            # Table header row
            self._draw_rect(page, self.MARGIN, y,
                            self.PAGE_W - self.MARGIN, y + row_h, fill=self.PRIMARY)
            for ci, col in enumerate(cols):
                self._text(page, self.MARGIN + ci * col_w + 4, y + 11,
                           str(col)[:25], fontsize=9, color=self.WHITE, bold=True)
            y += row_h

            # Data rows
            for ri, row in enumerate(table_data):
                if y + row_h > bottom_limit:
                    self._footer(page)
                    page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
                    self._draw_rect(page, 0, 0, self.PAGE_W, 14, fill=self.PRIMARY)
                    y = 24
                    # Re-draw header
                    self._draw_rect(page, self.MARGIN, y,
                                    self.PAGE_W - self.MARGIN, y + row_h, fill=self.PRIMARY)
                    for ci, col in enumerate(cols):
                        self._text(page, self.MARGIN + ci * col_w + 4, y + 11,
                                   str(col)[:25], fontsize=9, color=self.WHITE, bold=True)
                    y += row_h

                fill = self.ROW_ALT if ri % 2 == 0 else self.WHITE
                self._draw_rect(page, self.MARGIN, y,
                                self.PAGE_W - self.MARGIN, y + row_h, fill=fill)
                for ci, col in enumerate(cols):
                    val = str(row.get(col, ""))[:30]
                    self._text(page, self.MARGIN + ci * col_w + 4, y + 11,
                               val, fontsize=9)
                y += row_h

        self._footer(page)

        buf = io.BytesIO()
        doc.save(buf)
        doc.close()
        return buf.getvalue()

    # ── Compare Report ────────────────────────────────────────────────────────

    def _similarity_gauge(self, page, y: float, score: float) -> float:
        """Draw a horizontal similarity score bar, return y after it."""
        label_a = self.MARGIN
        bar_x   = self.MARGIN
        bar_w   = self.PAGE_W - 2 * self.MARGIN
        bar_h   = 14

        # Background track
        self._draw_rect(page, bar_x, y, bar_x + bar_w, y + bar_h,
                        fill=(0.88, 0.88, 0.88))

        # Filled portion
        filled_w = bar_w * min(score / 100.0, 1.0)
        # Colour: green → amber → red based on score
        if score >= 60:
            bar_color = (0.13, 0.55, 0.13)
        elif score >= 30:
            bar_color = (1.00, 0.60, 0.00)
        else:
            bar_color = (0.80, 0.10, 0.10)

        if filled_w > 0:
            self._draw_rect(page, bar_x, y, bar_x + filled_w, y + bar_h,
                            fill=bar_color)

        # Score label centred on bar
        score_txt = f"{score}%"
        self._text(page, bar_x + bar_w / 2 - 10, y + 10,
                   score_txt, fontsize=9, color=self.WHITE, bold=True)

        return y + bar_h + 4

    def _unique_points_section(self, page, doc, y: float,
                               label: str, points: list) -> tuple:
        """
        Render a unique-points block for one document.
        Returns (page, y) after drawing — may create new pages.
        """
        bottom_limit = self.PAGE_H - 40
        line_h = 15

        if y + 30 > bottom_limit:
            self._footer(page)
            page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
            self._draw_rect(page, 0, 0, self.PAGE_W, 14, fill=self.PRIMARY)
            y = 24

        # Sub-heading with accent colour
        self._draw_rect(page, self.MARGIN, y,
                        self.PAGE_W - self.MARGIN, y + 16, fill=self.ACCENT)
        self._text(page, self.MARGIN + 6, y + 11,
                   f"Unique Points — {label[:60]}", fontsize=9,
                   color=self.DARK, bold=True)
        y += 20

        if not points:
            self._text(page, self.MARGIN + 6, y + 10,
                       "No unique points identified.", fontsize=9)
            return page, y + 20

        content_w = self.PAGE_W - 2 * self.MARGIN - 10

        for i, point in enumerate(points):
            wrapped = self._wrap_text(f"  -  {point}", content_w, fontsize=9)
            block_h = len(wrapped) * line_h + 4

            if y + block_h > bottom_limit:
                self._footer(page)
                page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
                self._draw_rect(page, 0, 0, self.PAGE_W, 14, fill=self.PRIMARY)
                y = 24

            fill = self.ROW_ALT if i % 2 == 0 else self.WHITE
            self._draw_rect(page, self.MARGIN, y,
                            self.PAGE_W - self.MARGIN, y + block_h, fill=fill)
            for j, line in enumerate(wrapped):
                self._text(page, self.MARGIN + 6, y + 11 + j * line_h,
                           line, fontsize=9)
            y += block_h + 2

        return page, y + 8

    def build_compare_pdf(self, similarity_score: float, interpretation: str,
                          unique_points: dict, source_labels: list,
                          language: str) -> bytes:
        """
        Build a comparison report PDF.

        Args:
            similarity_score : Float 0-100.
            interpretation   : Human-readable similarity verdict string.
            unique_points    : Dict mapping sanitised label keys to lists of strings.
                               e.g. {"unique_to_doc_a.pdf": [...], "unique_to_doc_b.pdf": [...]}
            source_labels    : Original document label list (for display names).
            language         : User-selected language.

        Returns:
            PDF bytes.
        """
        doc = fitz.open()
        page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
        bottom_limit = self.PAGE_H - 40

        # Header
        y = self._header(page,
                         " vs ".join(source_labels[:2]),
                         language)
        y += 10

        # ── Similarity Score ──────────────────────────────────────────────────
        y = self._section_title(page, y, "SIMILARITY SCORE")
        y += 8

        y = self._similarity_gauge(page, y, similarity_score)
        y += 4

        # Interpretation text (wrapped)
        wrapped_interp = self._wrap_text(interpretation,
                                         self.PAGE_W - 2 * self.MARGIN - 10,
                                         fontsize=10)
        self._draw_rect(page, self.MARGIN, y,
                        self.PAGE_W - self.MARGIN,
                        y + len(wrapped_interp) * 14 + 8,
                        fill=self.ROW_ALT)
        for j, line in enumerate(wrapped_interp):
            self._text(page, self.MARGIN + 6, y + 12 + j * 14, line, fontsize=10)
        y += len(wrapped_interp) * 14 + 16

        # ── Unique Points ─────────────────────────────────────────────────────
        if y + 30 > bottom_limit:
            self._footer(page)
            page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
            self._draw_rect(page, 0, 0, self.PAGE_W, 14, fill=self.PRIMARY)
            y = 24

        y = self._section_title(page, y, "UNIQUE POINTS PER DOCUMENT")
        y += 6

        for display_label in source_labels[:2]:
            safe_key = "unique_to_" + display_label.replace(" ", "_").replace("/", "_")
            points = unique_points.get(safe_key, [])
            page, y = self._unique_points_section(page, doc, y, display_label, points)

        self._footer(page)

        buf = io.BytesIO()
        doc.save(buf)
        doc.close()
        return buf.getvalue()

    # ── Analyze / Bias Report ─────────────────────────────────────────────────

    def build_analyze_pdf(self, pred_cat: str, pred_score: float, scores_dict: dict,
                          source_name: str, language: str) -> bytes:
        """
        Build a Bias Analysis report PDF.

        Args:
            pred_cat     : The predicted dominant category.
            pred_score   : The confidence score for the predicted category.
            scores_dict  : Dictionary of all category scores.
            source_name  : Document name.
            language     : User-selected language.

        Returns:
            PDF bytes.
        """
        doc = fitz.open()
        page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
        bottom_limit = self.PAGE_H - 40

        # Header
        y = self._header(page, source_name, language)
        y += 10

        # ── Primary Focus ─────────────────────────────────────────────────────
        y = self._section_title(page, y, "PRIMARY FOCUS / DOMINANT THEME")
        y += 8

        # Large text for category
        self._text(page, self.MARGIN, y + 14, f"Predicted Category: {pred_cat}",
                   fontsize=12, color=self.DARK, bold=True)
        y += 24

        # Gauge bar for the predicted score
        y = self._similarity_gauge(page, y, pred_score)
        y += 14

        # ── Detailed Scores Table ─────────────────────────────────────────────
        y = self._section_title(page, y, "DETAILED BUREAU ANALYSIS")
        y += 6

        if scores_dict:
            # Sort scores descending
            sorted_scores = sorted(scores_dict.items(), key=lambda item: item[1], reverse=True)
            
            row_h = 16
            content_w = self.PAGE_W - 2 * self.MARGIN
            col_w_cat = content_w * 0.7
            col_w_score = content_w * 0.3

            # Table Header
            self._draw_rect(page, self.MARGIN, y,
                            self.PAGE_W - self.MARGIN, y + row_h, fill=self.PRIMARY)
            self._text(page, self.MARGIN + 6, y + 11, "Category", fontsize=9, color=self.WHITE, bold=True)
            self._text(page, self.MARGIN + col_w_cat + 6, y + 11, "Confidence (%)", fontsize=9, color=self.WHITE, bold=True)
            y += row_h

            # Rows
            for i, (cat, score) in enumerate(sorted_scores):
                if y + row_h > bottom_limit:
                    self._footer(page)
                    page = doc.new_page(width=self.PAGE_W, height=self.PAGE_H)
                    self._draw_rect(page, 0, 0, self.PAGE_W, 14, fill=self.PRIMARY)
                    y = 24
                    # Re-draw header
                    self._draw_rect(page, self.MARGIN, y,
                                    self.PAGE_W - self.MARGIN, y + row_h, fill=self.PRIMARY)
                    self._text(page, self.MARGIN + 6, y + 11, "Category", fontsize=9, color=self.WHITE, bold=True)
                    self._text(page, self.MARGIN + col_w_cat + 6, y + 11, "Confidence (%)", fontsize=9, color=self.WHITE, bold=True)
                    y += row_h

                fill = self.ROW_ALT if i % 2 == 0 else self.WHITE
                self._draw_rect(page, self.MARGIN, y,
                                self.PAGE_W - self.MARGIN, y + row_h, fill=fill)
                self._text(page, self.MARGIN + 6, y + 11, str(cat)[:60], fontsize=9)
                self._text(page, self.MARGIN + col_w_cat + 6, y + 11, f"{score:.1f}%", fontsize=9)
                y += row_h

        self._footer(page)

        buf = io.BytesIO()
        doc.save(buf)
        doc.close()
        return buf.getvalue()


# Singleton
pdf_export_service = SummaryPDFExporter()


