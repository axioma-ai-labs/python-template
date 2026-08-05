import sys

from loguru import logger

from src.core.config import settings
from src.core.defs import Environment


def setup_logging() -> None:
    """Configure Loguru with environment-appropriate log level."""
    log_level = "DEBUG" if settings.ENVIRONMENT == Environment.DEVELOPMENT else "INFO"

    logger.remove()
    logger.add(sys.stderr, level=log_level)

    logger.info(f"Logging configured for {settings.ENVIRONMENT.value} environment")
