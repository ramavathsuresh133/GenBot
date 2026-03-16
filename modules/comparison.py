"""
comparison.py — Fixed & Optimized
Fixes:
  - AttributeError / import errors with sentence-transformers
  - Large input error → chunked mean pooling
  - Structured diff output
  - Lazy model loading to avoid startup crashes on network timeout
"""

from sentence_transformers import SentenceTransformer, util
import torch
import re
import os

# ── Config ────────────────────────────────────────────────────────────────────
MODEL_NAME     = "all-MiniLM-L6-v2"   # fast, accurate, 384-dim embeddings
MAX_CHUNK_CHARS = 500                  # chars per sentence chunk for embedding
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ── Lazy Model Loading ───────────────────────────────────────────────────────
_model = None

def _get_model() -> SentenceTransformer:
    """Lazy-load the SentenceTransformer model (only on first use)."""
    global _model
    if _model is not None:
        return _model

    print(f"[Comparison] Loading {MODEL_NAME} on {DEVICE}...")
    try:
        _model = SentenceTransformer(MODEL_NAME, device=DEVICE)
    except Exception:
        # Network failed — try loading from local cache only
        print("[Comparison] Network timeout, trying local cache...")
        os.environ["HF_HUB_OFFLINE"] = "1"
        _model = SentenceTransformer(MODEL_NAME, device=DEVICE)
        os.environ.pop("HF_HUB_OFFLINE", None)

    print("[Comparison] Model ready.")
    return _model


# ── Helpers ───────────────────────────────────────────────────────────────────

def _split_sentences(text: str) -> list[str]:
    """Split text into sentences for granular comparison."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if len(s.strip()) > 20]


def _get_document_embedding(text: str) -> torch.Tensor:
    """
    Safely embed a full document by chunking and mean-pooling.
    Fixes 'large input' errors by never passing the full text at once.
    """
    sentences = _split_sentences(text)
    if not sentences:
        sentences = [text[:MAX_CHUNK_CHARS]]  # fallback

    # Batch encode all sentences
    model = _get_model()
    embeddings = model.encode(sentences, convert_to_tensor=True, show_progress_bar=False)
    # Mean pool → single document vector
    doc_embedding = embeddings.mean(dim=0)
    return doc_embedding


def _find_unique_points(text_a: str, text_b: str, threshold: float = 0.75) -> dict:
    """Find sentences unique to each document (low similarity to the other)."""
    sents_a = _split_sentences(text_a)
    sents_b = _split_sentences(text_b)

    if not sents_a or not sents_b:
        return {"unique_to_a": [], "unique_to_b": []}

    model = _get_model()
    emb_a = model.encode(sents_a, convert_to_tensor=True)
    emb_b = model.encode(sents_b, convert_to_tensor=True)

    # For each sentence in A, find max similarity to any sentence in B
    sim_a_to_b = util.cos_sim(emb_a, emb_b).max(dim=1).values
    sim_b_to_a = util.cos_sim(emb_b, emb_a).max(dim=1).values

    unique_a = [sents_a[i] for i, s in enumerate(sim_a_to_b) if s.item() < threshold]
    unique_b = [sents_b[i] for i, s in enumerate(sim_b_to_a) if s.item() < threshold]

    return {
        "unique_to_doc1": unique_a[:10],   # top 10 to avoid overload
        "unique_to_doc2": unique_b[:10],
    }


# ── Main API ──────────────────────────────────────────────────────────────────

def compare(text_a: str, text_b: str, label_a: str = "Document 1", label_b: str = "Document 2") -> dict:
    """
    Compare two documents semantically.

    Args:
        text_a:   First document text.
        text_b:   Second document text.
        label_a:  Label for first document (e.g. "Budget 2023").
        label_b:  Label for second document (e.g. "Budget 2024").

    Returns:
        dict with similarity score, interpretation, and unique points.
    """
    if not text_a.strip() or not text_b.strip():
        return {"error": "One or both documents are empty."}

    # Get safe document-level embeddings
    emb_a = _get_document_embedding(text_a)
    emb_b = _get_document_embedding(text_b)

    # Overall similarity score
    similarity = util.cos_sim(emb_a.unsqueeze(0), emb_b.unsqueeze(0)).item()
    similarity_pct = round(similarity * 100, 2)

    # Interpret score
    if similarity_pct >= 80:
        interpretation = "Very High Similarity — documents are nearly identical in focus."
    elif similarity_pct >= 60:
        interpretation = "High Similarity — significant overlap in topics and intent."
    elif similarity_pct >= 40:
        interpretation = "Moderate Similarity — some shared themes, notable differences."
    elif similarity_pct >= 20:
        interpretation = "Low Similarity — documents differ substantially."
    else:
        interpretation = "Very Low Similarity — documents cover entirely different content."

    # Unique points per document
    unique = _find_unique_points(text_a, text_b)

    return {
        "similarity_score": similarity_pct,
        "interpretation": interpretation,
        f"unique_to_{label_a.replace(' ', '_')}": unique["unique_to_doc1"],
        f"unique_to_{label_b.replace(' ', '_')}": unique["unique_to_doc2"],
        "labels": {
            "doc1": label_a,
            "doc2": label_b,
        }
    }