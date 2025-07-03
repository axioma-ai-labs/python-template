import logfire
from loguru import logger

from src.core.config import settings


# configure logfire
logfire.configure(
    send_to_logfire="if-token-present",
    token=settings.LOGFIRE_TOKEN,
    service_name=settings.PROJECT_NAME,
    environment=settings.ENVIRONMENT.value,
)

# configure loguru to send logs to logfire
logger.configure(handlers=[logfire.loguru_handler()])


def main() -> None:
    """
    Main entry point for the application. This is example docstring following Google style.

    Returns:
        None
    """
    logger.info("Hello, world!")


if __name__ == "__main__":
    main()
