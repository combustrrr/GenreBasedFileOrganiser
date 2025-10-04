"""
Logging module for the Genre-Based File Organizer.
"""

import logging
import os
from datetime import datetime


def setup_logging(log_dir="logs"):
    """Sets up the logging configuration for the application.
    
    Args:
        log_dir: Directory to store log files
    """
    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)
    
    # Create log file with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"file_organizer_{timestamp}.log")
    
    # Set up logging configuration
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    # Also log to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    )
    logging.getLogger().addHandler(console_handler)
    
    logging.info(f"Logger setup complete. Log file: {log_file}")
    return log_file


def log_info(message):
    """Logs informational messages."""
    logging.info(message)


def log_error(message):
    """Logs error messages."""
    logging.error(message)


def log_warning(message):
    """Logs warning messages."""
    logging.warning(message)


def log_debug(message):
    """Logs debug messages."""
    logging.debug(message)
