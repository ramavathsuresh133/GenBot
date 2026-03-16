"""
pdf_service.py - PDF extraction service
"""

from core.logger import logger

def extract_text(file):
    """Extract text from an uploaded PDF file using PyMuPDF."""
    try:
        import fitz  # PyMuPDF
        pdf_bytes = file.read()
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        text_parts = []
        for page in doc:
            text_parts.append(page.get_text())
        doc.close()
        
        extracted_text = "\n".join(text_parts).strip()
        logger.info(f"Successfully extracted {len(extracted_text)} characters from PDF")
        return extracted_text
    except Exception as e:
        logger.error(f"PDF extraction failed: {e}")
        raise RuntimeError(f"Failed to extract text from PDF: {e}")
