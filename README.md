# GENBOT - Modular Document Intelligence

GENBOT is a production-style modular Streamlit application for document summarization, comparison, and analysis.

## 🏗 Architecture

- **`app/`**: Streamlit frontend components.
- **`core/`**: Configuration, logging, and the task controller.
- **`models/`**: AI model loading (Singleton pattern).
- **`modules/`**: Specific AI task modules (Summarization, etc.).
- **`services/`**: Generic services (PDF extraction, URL scraping, Preprocessing).
- **`utils/`**: Helper functions.

## 🚀 Getting Started

1. **Install Dependencies**:
   ```bash
   python -m pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python run.py
   ```

## 🛠 Features (v1.0)
- **Summarization**: High-quality BART-based document summarization.
- **Comparison**: Semantic comparison between two documents (Coming Soon).
- **Bias Analysis**: Zero-shot stance detection (Coming Soon).
