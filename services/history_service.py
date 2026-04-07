"""
history_service.py - Persistent CSV Logging for GENBOT
Handles logging of tasks (Summarize, Compare, Analyze) to data/history.csv.
"""

import os
import pandas as pd
from datetime import datetime
from core.logger import get_logger

logger = get_logger(__name__)

HISTORY_PATH = os.path.join("data", "history.csv")

class HistoryService:
    """
    Service to log and retrieve task execution history using a CSV file.
    Ensures that users can revisit past summaries and comparisons.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def _ensure_history_exists(self):
        """Create directory and headers if the file does not exist."""
        # Ensure 'data' directory exists
        os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)
        
        if not os.path.exists(HISTORY_PATH):
            df = pd.DataFrame(columns=[
                "Timestamp", "Task", "Source", "Language", 
                "Token Count", "Metrix", "Result Summary"
            ])
            df.to_csv(HISTORY_PATH, index=False)
            logger.info("Initialized new history.csv file.")

    def log_task(self, task: str, source: str, language: str, tokens: int, metrix: str, result: str):
        """
        Log a completed task metadata to the CSV.
        
        Args:
            task: Type of task (Summarize/Compare/Analyze)
            source: Document name or URL
            language: User's selected language
            tokens: Input token count
            metrix: Task-specific metric (Confidence/Similarity/Time)
            result: Truncated or full result snippet
        """
        self._ensure_history_exists()
        
        # Clean result text for CSV (remove newlines)
        clean_result = str(result).replace("\n", " ")[:200] + "..." if len(str(result)) > 200 else str(result)
        
        new_row = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Task": task,
            "Source": source,
            "Language": language,
            "Token Count": tokens,
            "Metrix": metrix,
            "Result Summary": clean_result
        }
        
        try:
            df = pd.read_csv(HISTORY_PATH)
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            # Keep only the last 100 entries to prevent file bloating
            df = df.tail(100)
            df.to_csv(HISTORY_PATH, index=False)
            logger.info(f"Task '{task}' logged to history.")
        except Exception as e:
            logger.error(f"Failed to log task to history: {e}")

    def get_history(self) -> pd.DataFrame:
        """Retrieve the last 100 tasks from the CSV."""
        self._ensure_history_exists()
        try:
            return pd.read_csv(HISTORY_PATH).sort_values(by="Timestamp", ascending=False)
        except Exception as e:
            logger.error(f"Failed to read history: {e}")
            return pd.DataFrame()

    def clear_history(self):
        """Remove the history file."""
        if os.path.exists(HISTORY_PATH):
            os.remove(HISTORY_PATH)
            logger.info("History cleared.")

# Singleton instance
history_service = HistoryService()
