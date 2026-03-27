"""Logging configuration for OpenClaw Telegram Bot."""

import logging
import logging.handlers
import os
from pathlib import Path
from datetime import datetime


class LogConfig:
    """Centralized logging configuration."""

    LOG_DIR = Path("logs")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s"
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    
    # Log file names
    MAIN_LOG = "bot.log"
    ERROR_LOG = "errors.log"
    DEBUG_LOG = "debug.log"
    
    # Default levels
    FILE_LEVEL = logging.INFO
    CONSOLE_LEVEL = logging.INFO

    @classmethod
    def setup_logging(cls, level=logging.INFO):
        """Configure logging for the application.
        
        Args:
            level: Logging level (default: INFO)
        """
        # Create logs directory if it doesn't exist
        cls.LOG_DIR.mkdir(exist_ok=True)
        
        # Get root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        
        # Remove existing handlers
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(cls.CONSOLE_LEVEL)
        console_formatter = logging.Formatter(cls.LOG_FORMAT, cls.DATE_FORMAT)
        console_handler.setFormatter(console_formatter)
        root_logger.addHandler(console_handler)
        
        # File handler for all logs
        main_file_path = cls.LOG_DIR / cls.MAIN_LOG
        file_handler = logging.handlers.RotatingFileHandler(
            main_file_path,
            maxBytes=10485760,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(cls.FILE_LEVEL)
        file_formatter = logging.Formatter(cls.LOG_FORMAT, cls.DATE_FORMAT)
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)
        
        # Error file handler
        error_file_path = cls.LOG_DIR / cls.ERROR_LOG
        error_handler = logging.handlers.RotatingFileHandler(
            error_file_path,
            maxBytes=10485760,  # 10MB
            backupCount=3
        )
        error_handler.setLevel(logging.ERROR)
        error_formatter = logging.Formatter(cls.LOG_FORMAT, cls.DATE_FORMAT)
        error_handler.setFormatter(error_formatter)
        root_logger.addHandler(error_handler)
        
        return root_logger


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance.
    
    Args:
        name: Module name for the logger
        
    Returns:
        logging.Logger: Configured logger instance
    """
    return logging.getLogger(name)


# Setup logging when module is imported
LogConfig.setup_logging()
