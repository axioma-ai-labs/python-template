import logfire
from loguru import logger

from src.core.config import settings
from src.core.defs import Environment


def setup_logging(
    httpx: bool = False,
    pydantic: bool = False,
    pydantic_ai: bool = False,
    system_metrics: bool = False,
) -> None:
    """
    Configure minimal logging with Logfire and Loguru.

    This setup:
    - Uses Logfire as the main observability platform
    - Configures Loguru to send logs to Logfire with environment-based filtering
    - Sets environment-appropriate log levels
    - Prevents debug logs from reaching Logfire in production
    """
    logfire.configure(
        send_to_logfire="if-token-present",
        token=settings.LOGFIRE_TOKEN,
        service_name=settings.PROJECT_NAME,
        environment=settings.ENVIRONMENT.value,
    )

    log_level = "DEBUG" if settings.ENVIRONMENT == Environment.DEVELOPMENT else "INFO"

    logger.configure(handlers=[{**logfire.loguru_handler(), "level": log_level}])

    if httpx:
        logfire.instrument_httpx()
    if pydantic:
        logfire.instrument_pydantic()
    if pydantic_ai:
        logfire.instrument_pydantic_ai()
    if system_metrics:
        logfire.instrument_system_metrics()

    logger.info(f"Logging configured for {settings.ENVIRONMENT.value} environment")
