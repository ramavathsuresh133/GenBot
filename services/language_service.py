"""
language_service.py — Fast Multilingual Translation for GENBOT
Uses deep-translator (Google Translate API) instead of local NLLB model.

Speed comparison:
  - NLLB-200 on CPU: ~30 sec/chunk × 29 chunks = ~14 minutes
  - Google Translate:  ~0.2 sec/chunk × 29 chunks = ~6 seconds

No model download needed. No GPU needed. Just internet access.
"""

from deep_translator import GoogleTranslator
import re

from core.logger import get_logger

logger = get_logger(__name__)

# ── Google Translate Language Codes ───────────────────────────────────────────
LANGUAGE_MAP = {
    "English":    "en",
    "Hindi":      "hi",
    "Telugu":     "te",
    "Tamil":      "ta",
    "Kannada":    "kn",
    "Malayalam":  "ml",
}

SUPPORTED_LANGUAGES = list(LANGUAGE_MAP.keys())

# Google Translate has a ~5000 char limit per request
MAX_CHUNK_CHARS = 4500


# ── Singleton Service ─────────────────────────────────────────────────────────

class LanguageService:
    """
    Fast translation service using Google Translate via deep-translator.
    No model loading, no GPU, near-instant translations.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # ── Chunking ──────────────────────────────────────────────────────────────

    def _chunk_for_translation(self, text: str, max_length: int = MAX_CHUNK_CHARS) -> list:
        """
        Split text into chunks that fit Google Translate's character limit.
        Splits at sentence boundaries for better translation quality.
        """
        if len(text) <= max_length:
            return [text]

        # Split on sentence boundaries (including Hindi purna viram ।)
        sentences = re.split(r'(?<=[.!?।])\s+', text.strip())
        chunks, current = [], ""

        for sent in sentences:
            if len(current) + len(sent) + 1 <= max_length:
                current += sent + " "
            else:
                if current.strip():
                    chunks.append(current.strip())
                # Handle very long sentences
                while len(sent) > max_length:
                    split_pos = sent[:max_length].rfind(' ')
                    if split_pos < max_length * 0.3:
                        split_pos = max_length
                    chunks.append(sent[:split_pos].strip())
                    sent = sent[split_pos:].strip()
                current = sent + " "

        if current.strip():
            chunks.append(current.strip())

        return chunks if chunks else [text[:max_length]]

    # ── Core Translation ──────────────────────────────────────────────────────

    def _translate_chunk(self, text: str, src_code: str, tgt_code: str) -> str:
        """Translate a single chunk using Google Translate."""
        if not text.strip():
            return text
        try:
            translated = GoogleTranslator(source=src_code, target=tgt_code).translate(text)
            return translated if translated else text
        except Exception as e:
            logger.error(f"Translation chunk failed: {e}")
            return text  # return original on failure

    # ── Public API ────────────────────────────────────────────────────────────

    def translate_to_english(self, text: str, source_language: str) -> str:
        """
        Translate text from any supported Indian language to English.

        Args:
            text:            Input text in the source language.
            source_language: Display name (e.g. "Hindi", "Telugu").

        Returns:
            English translation of the input text.
        """
        if source_language == "English" or source_language not in LANGUAGE_MAP:
            return text

        if not text.strip():
            return text

        src_code = LANGUAGE_MAP[source_language]

        logger.info(f"Translating input from {source_language} to English...")
        print(f"[Translation] Translating from {source_language} → English...")

        chunks = self._chunk_for_translation(text)
        translated_chunks = []

        for i, chunk in enumerate(chunks):
            translated = self._translate_chunk(chunk, src_code, "en")
            translated_chunks.append(translated)
            if len(chunks) > 5 and (i + 1) % 5 == 0:
                print(f"[Translation] {i+1}/{len(chunks)} chunks translated...")

        result = " ".join(translated_chunks)
        logger.info(f"Translation to English complete ({len(chunks)} chunks).")
        print(f"[Translation] Done — {len(chunks)} chunks translated.")
        return result

    def translate_from_english(self, text: str, target_language: str) -> str:
        """
        Translate English text to a target Indian language.

        Args:
            text:            English text to translate.
            target_language: Display name (e.g. "Tamil", "Kannada").

        Returns:
            Translated text in the target language.
        """
        if target_language == "English" or target_language not in LANGUAGE_MAP:
            return text

        if not text.strip():
            return text

        tgt_code = LANGUAGE_MAP[target_language]

        logger.info(f"Translating output English → {target_language}...")

        chunks = self._chunk_for_translation(text)
        translated_chunks = []

        for chunk in chunks:
            translated = self._translate_chunk(chunk, "en", tgt_code)
            translated_chunks.append(translated)

        result = " ".join(translated_chunks)
        logger.info(f"Translation to {target_language} complete.")
        return result

    def translate_list(self, items: list, target_language: str) -> list:
        """
        Translate a list of strings from English to the target language.
        Useful for bullet points, unique points, etc.
        """
        if target_language == "English":
            return items
        return [self.translate_from_english(item, target_language) for item in items]

    def is_translation_needed(self, language: str) -> bool:
        """Check if translation is needed for the selected language."""
        return language != "English" and language in LANGUAGE_MAP


# ── Global singleton ──────────────────────────────────────────────────────────
language_service = LanguageService()
