"""Optional Sentry initialization for error and performance monitoring.

Sentry is disabled when ``SENTRY_DSN`` is empty. Call ``init_sentry()`` once at
application startup (after ``setup_logging()``) to enable it.

For FastAPI or other framework-specific apps, add the relevant integrations here
or in a project-specific module — see Sentry docs for
``FastApiIntegration``, ``SqlalchemyIntegration``, etc.
"""

from __future__ import annotations

from typing import Any

import sentry_sdk
from loguru import logger
from sentry_sdk.integrations.logging import LoggingIntegration

from src.core.config import settings
from src.core.defs import Environment


_sentry_initialized = False


def _traces_sample_rate() -> float:
    """Return the trace sample rate for the current environment."""
    if settings.ENVIRONMENT == Environment.DEVELOPMENT:
        return 1.0
    if settings.ENVIRONMENT in (Environment.TEST, Environment.CI):
        return 0.0
    return settings.SENTRY_TRACES_SAMPLE_RATE


def _add_loguru_sentry_sink() -> None:
    """Forward Loguru ERROR records to Sentry."""

    def _sink(message: Any) -> None:
        record = message.record
        if record["level"].no < 40:
            return
        if record["exception"] is not None:
            sentry_sdk.capture_exception(record["exception"])
            return
        sentry_sdk.capture_message(record["message"], level="error")

    logger.add(_sink, level="ERROR")


def init_sentry() -> bool:
    """Initialize Sentry when ``SENTRY_DSN`` is configured.

    Idempotent: returns ``False`` and does nothing when no DSN is set or Sentry
    was already initialized.

    Returns:
        ``True`` when Sentry was initialized, ``False`` otherwise.
    """
    global _sentry_initialized

    if _sentry_initialized or not settings.SENTRY_DSN:
        return False

    is_dev = settings.ENVIRONMENT == Environment.DEVELOPMENT

    sentry_sdk.init(  # pragma: no cover
        dsn=settings.SENTRY_DSN,
        environment=settings.ENVIRONMENT.value,
        release=settings.PROJECT_VERSION,
        traces_sample_rate=_traces_sample_rate(),
        profiles_sample_rate=1.0 if is_dev else 0.0,
        integrations=[
            LoggingIntegration(level=None, event_level=40),
        ],
        send_default_pii=False,
        include_source_context=False,
    )
    _add_loguru_sentry_sink()
    _sentry_initialized = True
    return True
