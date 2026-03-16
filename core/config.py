"""
config.py - Centralized configuration for GENBOT
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

# ── UI Config ────────────────────────────────────────────────────────────────
THEME_GRADIENT = "linear-gradient(135deg, #0f0c29, #302b63, #24243e)"
ACCENT_COLOR = "#a78bfa"
