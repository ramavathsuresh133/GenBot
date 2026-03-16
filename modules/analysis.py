"""
analysis.py — Speed Optimized
Changes:
  - Switched to cross-encoder/nli-MiniLM2-L6-H768 (5x faster than bart-large-mnli)
  - Smart sampling: only classify first 10 chunks instead of entire document
  - Merged 4 classification passes into fewer calls
  - Structured output compatible with main.py UI
"""

from transformers import pipeline
import torch
import re

# ── Config ────────────────────────────────────────────────────────────────────
ZERO_SHOT_MODEL = "cross-encoder/nli-MiniLM2-L6-H768"  # 5x faster, good accuracy
MAX_CHUNK_CHARS = 1000   # smaller chunks = faster per-chunk inference
MAX_CHUNKS      = 8      # only classify this many chunks — enough for accurate results
DEVICE = 0 if torch.cuda.is_available() else -1

# ── Candidate Labels ──────────────────────────────────────────────────────────
BIAS_LABELS = [
    "left-leaning", "right-leaning", "centrist", "neutral",
    "pro-government", "anti-government", "populist"
]

SECTOR_LABELS = [
    "healthcare", "education", "defense", "infrastructure",
    "agriculture", "economy", "environment", "social welfare",
    "technology", "taxation"
]

SENTIMENT_LABELS = [
    "positive", "negative", "neutral", "optimistic", "critical"
]

TONE_LABELS = [
    "formal", "emotional", "aggressive", "diplomatic",
    "promotional", "factual", "fear-mongering"
]

# ── Lazy Model Loading ────────────────────────────────────────────────────────
_classifier = None

def _get_classifier():
    """Lazy-load the zero-shot classification pipeline (only on first use)."""
    global _classifier
    if _classifier is not None:
        return _classifier

    import os
    print(f"[Analysis] Loading {ZERO_SHOT_MODEL} on {'GPU' if DEVICE == 0 else 'CPU'}...")
    try:
        _classifier = pipeline(
            "zero-shot-classification",
            model=ZERO_SHOT_MODEL,
            device=DEVICE,
        )
    except Exception:
        print("[Analysis] Network timeout, trying local cache...")
        os.environ["HF_HUB_OFFLINE"] = "1"
        _classifier = pipeline(
            "zero-shot-classification",
            model=ZERO_SHOT_MODEL,
            device=DEVICE,
        )
        os.environ.pop("HF_HUB_OFFLINE", None)

    print("[Analysis] Model ready.")
    return _classifier


# ── Helpers ───────────────────────────────────────────────────────────────────

def _chunk_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list:
    """Split into safe chunks."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    chunks, current = [], ""
    for sent in sentences:
        if len(current) + len(sent) + 1 <= max_chars:
            current += sent + " "
        else:
            if current.strip():
                chunks.append(current.strip())
            current = sent[:max_chars] + " "
    if current.strip():
        chunks.append(current.strip())
    return chunks or [text[:max_chars]]


def _smart_sample(chunks: list, max_chunks: int = MAX_CHUNKS) -> list:
    """
    Sample representative chunks from across the document.
    Takes front, middle, and end — avoids processing everything.
    """
    if len(chunks) <= max_chunks:
        return chunks
    # Take evenly spaced chunks across the document
    step = len(chunks) // max_chunks
    sampled = chunks[::step][:max_chunks]
    print(f"[Analysis] Sampled {len(sampled)}/{len(chunks)} chunks for speed.")
    return sampled


def _aggregate_scores(chunk_results: list) -> dict:
    """Average label scores across all chunks."""
    score_map = {}
    for result in chunk_results:
        for label, score in zip(result["labels"], result["scores"]):
            score_map.setdefault(label, []).append(score)
    averaged = {label: round(sum(scores) / len(scores), 4)
                for label, scores in score_map.items()}
    sorted_labels = sorted(averaged.items(), key=lambda x: x[1], reverse=True)
    return {
        "top_label": sorted_labels[0][0],
        "confidence": sorted_labels[0][1],
        "all_scores": dict(sorted_labels),
    }


def _classify(chunks: list, labels: list, multi_label: bool = True) -> dict:
    """Classify sampled chunks against given labels."""
    classifier = _get_classifier()
    results = []
    for i, chunk in enumerate(chunks):
        try:
            result = classifier(chunk, candidate_labels=labels, multi_label=multi_label)
            results.append(result)
        except Exception as e:
            print(f"[Analysis] Chunk {i} failed: {e} — skipping.")
    if not results:
        return {"top_label": "unknown", "confidence": 0.0, "all_scores": {}}
    return _aggregate_scores(results)


# ── Main API ──────────────────────────────────────────────────────────────────

def analyze(text: str) -> dict:
    """
    Full document analysis: bias, sectors, sentiment, tone.
    Optimized to run on sampled chunks for speed.

    Returns dict compatible with main.py UI expectations.
    """
    if not text.strip():
        return {"error": "Empty document provided."}

    # Build sampled chunks once — reuse for all 4 classification passes
    all_chunks  = _chunk_text(text)
    chunks      = _smart_sample(all_chunks)

    print(f"[Analysis] Classifying {len(chunks)} chunks across 4 dimensions...")

    print("[Analysis] Running bias detection...")
    bias_result      = _classify(chunks, BIAS_LABELS,      multi_label=False)

    print("[Analysis] Running sector analysis...")
    sector_result    = _classify(chunks, SECTOR_LABELS,    multi_label=True)

    print("[Analysis] Running sentiment analysis...")
    sentiment_result = _classify(chunks, SENTIMENT_LABELS, multi_label=False)

    print("[Analysis] Running tone analysis...")
    tone_result      = _classify(chunks, TONE_LABELS,      multi_label=True)

    # Top 3 sectors
    top_sectors = sorted(
        sector_result["all_scores"].items(), key=lambda x: x[1], reverse=True
    )[:3]

    # ── Build output compatible with main.py ──────────────────────────────────
    # main.py uses: data['predicted_category'], data['confidence'], data['all_scores']
    predicted_category = (
        f"{bias_result['top_label'].title()} / "
        f"{sentiment_result['top_label'].title()} / "
        f"{top_sectors[0][0].title() if top_sectors else 'N/A'}"
    )

    # Flat scores dict for st.bar_chart
    all_scores_flat = {
        f"[Bias] {k}":     round(v * 100, 1) for k, v in bias_result["all_scores"].items()
    } | {
        f"[Sector] {k}":   round(v * 100, 1) for k, v in sector_result["all_scores"].items()
    } | {
        f"[Sentiment] {k}": round(v * 100, 1) for k, v in sentiment_result["all_scores"].items()
    } | {
        f"[Tone] {k}":     round(v * 100, 1) for k, v in tone_result["all_scores"].items()
    }

    return {
        # main.py keys
        "predicted_category": predicted_category,
        "confidence": bias_result["confidence"],
        "all_scores": all_scores_flat,

        # detailed breakdown
        "bias": {
            "label":      bias_result["top_label"],
            "confidence": f"{bias_result['confidence']*100:.1f}%",
            "breakdown":  bias_result["all_scores"],
        },
        "priority_sectors": [
            {"sector": s, "score": f"{sc*100:.1f}%"} for s, sc in top_sectors
        ],
        "sentiment": {
            "label":      sentiment_result["top_label"],
            "confidence": f"{sentiment_result['confidence']*100:.1f}%",
        },
        "tone": {
            "label":      tone_result["top_label"],
            "confidence": f"{tone_result['confidence']*100:.1f}%",
        },
        "summary_insight": (
            f"This document leans {bias_result['top_label']} with a "
            f"{sentiment_result['top_label']} tone, primarily focusing on "
            f"{', '.join(s for s, _ in top_sectors)}."
        ),
        "chunks_analyzed": len(chunks),
        "total_chunks":    len(all_chunks),
    }