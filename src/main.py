from loguru import logger

from src.core.exceptions.base import AppError
from src.core.logging import setup_logging
from src.core.sentry import init_sentry


setup_logging()
init_sentry()


def main() -> None:
    """
    Main entry point for the application. This is example docstring following Google style.

    Returns:
        None
    """
    logger.info("Hello, world!")


def run() -> None:
    """Run the application with top-level app error handling."""
    try:
        main()
    except AppError as exc:
        logger.exception(
            "Application error [%s]: %s | details=%s",
            exc.code,
            exc.message,
            exc.details,
        )
        raise SystemExit(1) from exc


if __name__ == "__main__":
    run()
