from __future__ import annotations

from typing import Any


class AppError(Exception):
    """Base application exception with optional machine-readable context."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "application_error",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}

    def __str__(self) -> str:
        return self.message
