from unittest.mock import patch

import pytest

from src.core.defs import Environment
from src.core.sentry import _traces_sample_rate, init_sentry


@pytest.fixture(autouse=True)
def reset_sentry_state():
    """Reset module-level init flag between tests."""
    import src.core.sentry as sentry_module

    sentry_module._sentry_initialized = False
    yield
    sentry_module._sentry_initialized = False


def test_init_sentry_without_dsn_is_noop():
    with patch("src.core.sentry.settings.SENTRY_DSN", ""):
        assert init_sentry() is False


def test_init_sentry_with_dsn():
    with (
        patch("src.core.sentry.settings.SENTRY_DSN", "https://example@sentry.io/1"),
        patch("src.core.sentry.settings.ENVIRONMENT", Environment.DEVELOPMENT),
        patch("src.core.sentry.settings.PROJECT_VERSION", "1.2.3"),
        patch("src.core.sentry.sentry_sdk.init") as mock_init,
        patch("src.core.sentry._add_loguru_sentry_sink") as mock_sink,
    ):
        assert init_sentry() is True
        mock_init.assert_called_once()
        mock_sink.assert_called_once()


def test_init_sentry_is_idempotent():
    with (
        patch("src.core.sentry.settings.SENTRY_DSN", "https://example@sentry.io/1"),
        patch("src.core.sentry.sentry_sdk.init") as mock_init,
        patch("src.core.sentry._add_loguru_sentry_sink"),
    ):
        assert init_sentry() is True
        assert init_sentry() is False
        mock_init.assert_called_once()


@pytest.mark.parametrize(
    ("environment", "expected"),
    [
        (Environment.DEVELOPMENT, 1.0),
        (Environment.TEST, 0.0),
        (Environment.CI, 0.0),
        (Environment.PRODUCTION, 0.1),
    ],
)
def test_traces_sample_rate_by_environment(environment, expected):
    with (
        patch("src.core.sentry.settings.ENVIRONMENT", environment),
        patch("src.core.sentry.settings.SENTRY_TRACES_SAMPLE_RATE", 0.1),
    ):
        assert _traces_sample_rate() == expected
