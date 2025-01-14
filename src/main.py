from src.core.config import settings
from loguru import logger


# Configure loguru logger
logger.add("logs/debug.log", rotation="1 MB", retention="10 days", level="DEBUG")


def main() -> None:
    """
    Main entry point for the application. This is example docstring following Google style.

    Returns:
        None
    """
    print(settings.PROJECT_NAME)


if __name__ == "__main__":
    main()
