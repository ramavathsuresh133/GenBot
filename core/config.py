"""
config.py - Centralized configuration for GENBOT
Includes multilingual support settings.
"""

import torch

# ── Project Info ─────────────────────────────────────────────────────────────
APP_NAME = "GENBOT"
VERSION = "1.0.0"
ENV = "Prototype"

# ── Model Config ─────────────────────────────────────────────────────────────
# Summarization model
SUMM_MODEL_NAME = "facebook/bart-large-cnn"

# Bias analysis model
BIAS_MODEL_NAME = "facebook/bart-large-mnli"

# Bias category labels
BIAS_LABELS = [
    "Economic Focus",
    "Social Welfare",
    "Defense",
    "Development",
    "Neutral"
]

# Device configuration
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ── Processing Config ────────────────────────────────────────────────────────
MAX_CHUNK_SIZE = 3000
SUMM_MAX_LENGTH = 130
SUMM_MIN_LENGTH = 30
MAX_SUMMARY_CHUNKS = 3

# ── UI Config (Strategic Portal Styling) ──────────────────────────────────────
# Official Government Navy Blue and Professional Accents
PRIMARY_COLOR = "#1E3A8A"
SECONDARY_COLOR = "#FFFFFF"
ACCENT_COLOR = "#FF9933"  # Saffron
SUCCESS_COLOR = "#138808" # Green
TEXT_COLOR = "#1F2937"    # Dark Grey
BACKGROUND_COLOR = "#F3F4F6" # Light Grey

# ── Language Config ──────────────────────────────────────────────────────────
SUPPORTED_LANGUAGES = ["English", "Hindi", "Telugu", "Tamil", "Kannada", "Malayalam"]
DEFAULT_LANGUAGE = "English"
NLLB_MODEL_NAME = "facebook/nllb-200-distilled-600M"
