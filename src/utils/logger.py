import logging
import sys
from pathlib import Path

def setup_logger(name: str) -> logging.Logger:
    """
    Configures and returns a production-grade logger.
    Logs to both console (stdout) and a persistent 'execution.log' file.
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate logs if instantiated multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Define formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File Handler
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    file_handler = logging.FileHandler(log_dir / "execution.log", mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
