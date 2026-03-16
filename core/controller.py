"""
controller.py — Fixed Central Controller
Orchestrates all three LLMs with proper preprocessing to prevent errors.
"""

from core.logger import get_logger
from services.preprocessing import preprocess, get_stats
from modules.summarization import summarize
from modules.comparison import compare
from modules.analysis import analyze
import time

logger = get_logger(__name__)

# ── Convenience function expected by main.py ──────────────────────────────────

_TASK_MAP = {
    "Summarize Document": "summarize",
    "Compare Documents":  "compare",
    "Analyze Bias":       "analyze",
}

_controller = None


def route_task(task_label: str, text, **kwargs) -> dict:
    """
    Convenience wrapper used by the Streamlit frontend.

    Args:
        task_label: UI label e.g. "Summarize Document"
        text:       str for summarize/analyze
                    list[str] for compare (2 or 3 documents)
        kwargs:     doc_labels (list[str]) — optional labels for compare docs
    """
    global _controller
    if _controller is None:
        _controller = Controller()

    task_key = _TASK_MAP.get(task_label, task_label)

    start = time.time()
    try:
        # ── Compare: receives a list of texts ────────────────────────────────
        if task_key == "compare":
            docs = text if isinstance(text, list) else [text]
            doc_labels = kwargs.get("doc_labels", [f"Document {i+1}" for i in range(len(docs))])

            if len(docs) < 2:
                return {"status": "error", "message": "At least 2 documents are required for comparison."}

            result = _controller.handle(
                task_key,
                docs=docs,
                doc_labels=doc_labels,
            )
            elapsed = round(time.time() - start, 2)
            total_tokens = sum(len(d.split()) for d in docs)

        # ── Summarize / Analyze: receives a single string ────────────────────
        else:
            result = _controller.handle(task_key, text=text, **kwargs)
            elapsed = round(time.time() - start, 2)
            total_tokens = len(text.split()) if isinstance(text, str) else 0

        if "error" in result:
            return {"status": "error", "message": result["error"]}

        # Pick model name based on task
        model_names = {
            "summarize": "facebook/bart-large-cnn",
            "compare":   "all-MiniLM-L6-v2",
            "analyze":   "facebook/bart-large-mnli",
        }

        return {
            "status": "success",
            "task": task_key,
            "data": result,
            "metadata": {
                "model_name": model_names.get(task_key, "unknown"),
                "execution_time": elapsed,
                "input_token_length": total_tokens,
            },
        }

    except Exception as e:
        logger.error(f"route_task error: {e}")
        return {"status": "error", "message": str(e)}


# ── Controller Class ──────────────────────────────────────────────────────────

class Controller:
    """
    Central controller that routes tasks to the correct LLM module.
    All text passes through preprocessing to prevent large-input errors.
    """

    def handle(self, task: str, **kwargs) -> dict:
        try:
            if task == "summarize":
                return self._run_summarize(**kwargs)
            elif task == "compare":
                return self._run_compare(**kwargs)
            elif task == "analyze":
                return self._run_analyze(**kwargs)
            else:
                return {"error": f"Unknown task: '{task}'. Use 'summarize', 'compare', or 'analyze'."}
        except Exception as e:
            logger.error(f"Controller error on task '{task}': {e}")
            return {"error": str(e)}

    # ── Summarize ─────────────────────────────────────────────────────────────

    def _run_summarize(self, text: str, **kwargs) -> dict:
        logger.info("Starting summarization...")
        stats = get_stats(text)
        logger.info(f"Input stats: {stats}")
        clean = preprocess(text)
        kwargs.pop("doc_labels", None)
        result = summarize(clean, **kwargs)
        result["input_stats"] = stats
        logger.info("Summarization complete.")
        return result

    # ── Compare: supports 2 or 3 documents ───────────────────────────────────

    def _run_compare(self, docs: list, doc_labels: list = None, **kwargs) -> dict:
        logger.info(f"Starting comparison of {len(docs)} documents...")

        if doc_labels is None:
            doc_labels = [f"Document {i+1}" for i in range(len(docs))]

        # Preprocess all docs
        cleaned = [preprocess(d) for d in docs]

        # Validate none are empty
        for i, c in enumerate(cleaned):
            if not c.strip():
                return {"error": f"{doc_labels[i]} is empty after preprocessing."}

        # ── 2-document comparison ─────────────────────────────────────────────
        if len(cleaned) == 2:
            result = compare(
                cleaned[0], cleaned[1],
                label_a=doc_labels[0],
                label_b=doc_labels[1],
            )
            logger.info(f"Comparison complete. Similarity: {result.get('similarity_score')}%")
            return result

        # ── 3-document comparison: all pairs ──────────────────────────────────
        elif len(cleaned) >= 3:
            # Run pairwise comparisons for all 3 pairs
            pairs = [
                (0, 1), (0, 2), (1, 2)
            ]
            pairwise_rows = []
            all_unique = {}

            for i, j in pairs:
                pair_result = compare(
                    cleaned[i], cleaned[j],
                    label_a=doc_labels[i],
                    label_b=doc_labels[j],
                )
                pairwise_rows.append({
                    "Document A": doc_labels[i],
                    "Document B": doc_labels[j],
                    "Similarity (%)": pair_result.get("similarity_score", "N/A"),
                    "Interpretation": pair_result.get("interpretation", ""),
                })
                # Collect unique points per doc
                key_a = f"unique_to_{doc_labels[i].replace(' ', '_').replace('/', '_')}"
                key_b = f"unique_to_{doc_labels[j].replace(' ', '_').replace('/', '_')}"
                if key_a in pair_result:
                    all_unique.setdefault(key_a, []).extend(pair_result[key_a])
                if key_b in pair_result:
                    all_unique.setdefault(key_b, []).extend(pair_result[key_b])

            # Deduplicate unique points
            all_unique = {k: list(dict.fromkeys(v)) for k, v in all_unique.items()}

            # Overall similarity = average of all pairs
            scores = [r["Similarity (%)"] for r in pairwise_rows if isinstance(r["Similarity (%)"], (int, float))]
            avg_score = round(sum(scores) / len(scores), 2) if scores else "N/A"

            logger.info(f"3-doc comparison complete. Avg similarity: {avg_score}%")

            return {
                "similarity_score": avg_score,
                "interpretation": f"Average similarity across all 3 document pairs: {avg_score}%",
                "pairwise": pairwise_rows,
                **all_unique,
            }

    # ── Analyze ───────────────────────────────────────────────────────────────

    def _run_analyze(self, text: str, **kwargs) -> dict:
        logger.info("Starting bias/analysis...")
        clean = preprocess(text)
        kwargs.pop("doc_labels", None)
        result = analyze(clean, **kwargs)
        logger.info("Analysis complete.")
        return result