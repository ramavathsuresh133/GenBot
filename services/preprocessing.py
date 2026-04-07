"""
preprocessing.py — Fixed
Purpose: Clean and safely prepare text before passing to any LLM.
This is the CENTRAL fix for 'large input' errors — all text should
pass through preprocess() before going to any model.
"""

import re
import unicodedata


# ── Config ────────────────────────────────────────────────────────────────────
MAX_CHARS_DEFAULT = 50_000   # reasonable upper limit for any document


# ── Cleaning ──────────────────────────────────────────────────────────────────

def clean_text(text: str) -> str:
    """Remove noise from extracted PDF/URL text."""
    # Normalize unicode (handles special chars from PDFs)
    text = unicodedata.normalize("NFKD", text)
    # Remove non-printable/control characters but PRESERVE Unicode scripts
    # (Devanagari, Telugu, Tamil, Kannada, Malayalam, etc.)
    text = re.sub(r'[^\w\s.,;:!?\'\"()\-–—/\n]', ' ', text, flags=re.UNICODE)
    # Remove excessive whitespace
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove page numbers like "- 12 -" or "Page 12"
    text = re.sub(r'-\s*\d+\s*-', '', text)
    text = re.sub(r'Page\s+\d+', '', text, flags=re.IGNORECASE)
    # Remove URLs
    text = re.sub(r'https?://\S+', '', text)
    return text.strip()


def remove_headers_footers(text: str) -> str:
    """Try to remove repeating header/footer lines."""
    lines = text.split('\n')
    # Find lines that repeat (likely headers/footers)
    from collections import Counter
    line_counts = Counter(line.strip() for line in lines if line.strip())
    repeated = {line for line, count in line_counts.items() if count > 3 and len(line) < 100}
    cleaned = [line for line in lines if line.strip() not in repeated]
    return '\n'.join(cleaned)


# ── Safe Truncation ───────────────────────────────────────────────────────────

def safe_truncate(text: str, max_chars: int = MAX_CHARS_DEFAULT) -> str:
    """
    Truncate text to max_chars at a sentence boundary.
    This prevents 'large input' errors in all downstream models.
    """
    if len(text) <= max_chars:
        return text
    truncated = text[:max_chars]
    # Try to end at last sentence boundary
    last_period = max(
        truncated.rfind('. '),
        truncated.rfind('.\n'),
    )
    if last_period > max_chars * 0.8:  # only truncate at period if near the end
        truncated = truncated[:last_period + 1]
    return truncated.strip()


# ── Main API ──────────────────────────────────────────────────────────────────

def preprocess(text: str, max_chars: int = MAX_CHARS_DEFAULT) -> str:
    """
    Full preprocessing pipeline. Call this on ALL text before
    passing to summarization, comparison, or analysis modules.

    Args:
        text:      Raw text from PDF extraction or web scraping.
        max_chars: Maximum characters to keep (default 50,000).

    Returns:
        Cleaned, truncated text ready for model input.
    """
    text = clean_text(text)
    text = remove_headers_footers(text)
    text = safe_truncate(text, max_chars)
    return text


def get_stats(text: str) -> dict:
    """Return basic stats about the text."""
    words = len(text.split())
    chars = len(text)
    sentences = len(re.findall(r'[.!?]+', text))
    return {
        "characters": chars,
        "words": words,
        "sentences": sentences,
        "estimated_tokens": chars // 4,  # rough token estimate
    }