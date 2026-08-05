from unittest.mock import patch

import pytest

from src.core.exceptions.base import AppError
from src.main import main, run


def test_main_logs_hello_world():
    """Test the main function logs the expected message."""
    with patch("src.main.logger.info") as mock_info:
        main()
        mock_info.assert_called_once_with("Hello, world!")


def test_main_is_callable():
    """Test that main function exists and is callable."""
    assert callable(main)


def test_run_exits_on_app_error():
    """Test that top-level app errors are logged and exit cleanly."""
    app_error = AppError("Boom", code="boom", details={"key": "value"})

    with (
        patch("src.main.main", side_effect=app_error),
        patch("src.main.logger.exception") as mock_exception,
        pytest.raises(SystemExit) as exc_info,
    ):
        run()

    assert exc_info.value.code == 1
    mock_exception.assert_called_once_with(
        "Application error [%s]: %s | details=%s",
        "boom",
        "Boom",
        {"key": "value"},
    )
