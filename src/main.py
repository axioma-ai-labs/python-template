from loguru import logger

from src.core.logging import setup_logging


setup_logging(httpx=True, system_metrics=True)


def main() -> None:
    """
    Main entry point for the application. This is example docstring following Google style.

    Returns:
        None
    """
    logger.info("Hello, world!")


if __name__ == "__main__":
    main()
