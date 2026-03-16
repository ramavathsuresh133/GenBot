"""
logger.py - Centralized logging for GENBOT
"""

import logging
import sys

def setup_logger(name="genbot"):
    """Configure and return a standard logger."""
    logger = logging.getLogger(name)
    
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
    return logger

# Alias — allows both get_logger() and setup_logger() to work
get_logger = setup_logger

# Singleton instance
logger = setup_logger()