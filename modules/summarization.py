"""
summarization.py — Speed Optimized
Changes:
  - Switched to sshleifer/distilbart-cnn-12-6 (3x faster than bart-large-cnn)
  - Increased chunk size to reduce total number of chunks
  - num_beams reduced to 2 (faster inference, still good quality)
  - Smart sampling: for very large docs, takes key sections instead of all chunks
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# ── Config ────────────────────────────────────────────────────────────────────
MODEL_NAME        = "sshleifer/distilbart-cnn-12-6"  # 3x faster than bart-large-cnn
MAX_INPUT_TOKENS  = 1024
MAX_CHUNK_CHARS   = 4000   # larger chunks = fewer chunks = faster
MAX_OUTPUT_TOKENS = 250
MAX_CHUNKS        = 20     # cap total chunks — beyond this, smart sampling kicks in
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ── Load once at module level ─────────────────────────────────────────────────
print(f"[Summarization] Loading {MODEL_NAME} on {DEVICE}...")
_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
_model     = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME, low_cpu_mem_usage=False).to(DEVICE)
_model.eval()
print("[Summarization] Model ready.")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _chunk_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list:
    """Split text into paragraph-aware chunks under max_chars."""
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) + 1 <= max_chars:
            current += para + " "
        else:
            if current:
                chunks.append(current.strip())
            while len(para) > max_chars:
                chunks.append(para[:max_chars])
                para = para[max_chars:]
            current = para + " "
    if current.strip():
        chunks.append(current.strip())
    return chunks or [text[:max_chars]]


def _smart_sample(chunks: list, max_chunks: int = MAX_CHUNKS) -> list:
    """
    For very large documents, sample key chunks instead of processing all.
    Takes: first 40% (intro/context) + last 30% (conclusions) + middle sample.
    This captures most meaning in policy/budget/manifesto documents.
    """
    if len(chunks) <= max_chunks:
        return chunks

    n = len(chunks)
    front  = chunks[:int(n * 0.4)]                          # first 40%
    back   = chunks[int(n * 0.75):]                         # last 25%
    middle = chunks[int(n * 0.4):int(n * 0.75)]
    # Sample every Nth chunk from middle
    step = max(1, len(middle) // (max_chunks - len(front) - len(back)))
    mid_sample = middle[::step]

    sampled = front + mid_sample + back
    print(f"[Summarization] Large doc: sampled {len(sampled)}/{n} chunks for speed.")
    return sampled[:max_chunks]


def _summarize_chunk(text: str) -> str:
    """Summarize a single safe-length chunk using the model directly."""
    inputs = _tokenizer(
        text,
        return_tensors="pt",
        max_length=MAX_INPUT_TOKENS,
        truncation=True,
    ).to(DEVICE)

    with torch.no_grad():
        output_ids = _model.generate(
            inputs["input_ids"],
            max_length=MAX_OUTPUT_TOKENS,
            min_length=30,
            num_beams=2,        # reduced from 4 → 2x faster inference
            early_stopping=True,
        )

    return _tokenizer.decode(output_ids[0], skip_special_tokens=True).strip()


# ── Main API ──────────────────────────────────────────────────────────────────

def summarize(text: str, bullet_points: bool = True) -> dict:
    """
    Summarize a (potentially long) document.

    Args:
        text:          Raw extracted document text.
        bullet_points: If True, format output as bullet points.

    Returns:
        dict with keys: 'summary', 'chunks_processed', 'bullets', 'table_data'
    """
    text = text.strip()
    if not text:
        return {
            "summary": "No content to summarize.",
            "chunks_processed": 0,
            "bullets": [],
            "table_data": [],
        }

    all_chunks = _chunk_text(text)
    chunks     = _smart_sample(all_chunks)
    chunk_summaries = []

    for i, chunk in enumerate(chunks):
        try:
            summary = _summarize_chunk(chunk)
            chunk_summaries.append(summary)
            print(f"[Summarization] Chunk {i+1}/{len(chunks)} done.")
        except Exception as e:
            print(f"[Summarization] Chunk {i+1} failed: {e}")

    if not chunk_summaries:
        final_summary = "Summary unavailable."
        bullets = []
    else:
        # Each chunk summary becomes its own bullet — no re-collapsing
        raw_bullets = []
        for s in chunk_summaries:
            # Split on ". " in case a chunk summary has multiple sentences
            parts = [p.strip() for p in s.split(". ") if len(p.strip()) > 10]
            raw_bullets.extend(parts)

        # Deduplicate near-identical bullets
        seen, bullets = set(), []
        for b in raw_bullets:
            key = b[:60].lower()
            if key not in seen:
                seen.add(key)
                bullets.append(b if b.endswith(".") else b + ".")

        final_summary = "\n".join(f"• {b}" for b in bullets)

    # Table data for the structured tab in UI
    table_data = [{"#": i+1, "Key Point": b} for i, b in enumerate(bullets)]

    if bullet_points:
        final_summary = "\n".join(f"• {b}" for b in bullets)

    return {
        "summary": final_summary,
        "bullets": bullets,
        "table_data": table_data,
        "chunks_processed": len(chunks),
        "total_chunks": len(all_chunks),
    }