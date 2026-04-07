"""
model_loader.py - Singleton model loader for GENBOT
Supports: summarization, bias analysis, and translation models.
"""

from transformers import BartForConditionalGeneration, BartTokenizer
from core.config import SUMM_MODEL_NAME, DEVICE
from core.logger import logger

class ModelLoader:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelLoader, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Prevent initialization if it's already set up
        if not hasattr(self, '_initialized'):
            self._summ_model = None
            self._summ_tokenizer = None
            self._bias_classifier = None
            self._initialized = True

    def get_summarization_model(self):
        """Lazy load the summarization model and tokenizer."""
        if self._summ_model is None:
            logger.info(f"Loading summarization model: {SUMM_MODEL_NAME} on {DEVICE}...")
            self._summ_tokenizer = BartTokenizer.from_pretrained(SUMM_MODEL_NAME)
            self._summ_model = BartForConditionalGeneration.from_pretrained(SUMM_MODEL_NAME).to(DEVICE)
            logger.info("Summarization model loaded successfully.")
        return self._summ_model, self._summ_tokenizer

    def get_bias_classifier(self):
        """Lazy load the zero-shot classification pipeline."""
        if self._bias_classifier is None:
            from transformers import pipeline
            from core.config import BIAS_MODEL_NAME
            logger.info(f"Loading bias classifier: {BIAS_MODEL_NAME} on {DEVICE}...")
            self._bias_classifier = pipeline(
                "zero-shot-classification",
                model=BIAS_MODEL_NAME,
                device=0 if DEVICE == "cuda" else -1
            )
            logger.info("Bias classifier loaded successfully.")
        return self._bias_classifier

# Global instance
model_loader = ModelLoader()


