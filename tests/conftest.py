import pytest
from loguru import logger


@pytest.fixture(autouse=True)
def setup_test_logger():
    """Configure logger for testing to prevent writing to files during tests."""
    logger.remove()  # Remove default handlers
    logger.add(lambda msg: None, level="DEBUG")  # Add null handler for testing
    yield
    logger.remove()  # Cleanup after tests
