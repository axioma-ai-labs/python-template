from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.defs import Environment


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

    # === General settings ===

    #: Environment
    ENVIRONMENT: Environment = Environment.PRODUCTION

    #: Project name
    PROJECT_NAME: str = "your_project_name"

    #: Project version
    PROJECT_VERSION: str = "0.1.0"

    # === Observability (optional) ===

    #: Sentry DSN; leave empty to disable Sentry
    SENTRY_DSN: str = ""

    #: Trace sample rate for non-development environments (0.0–1.0)
    SENTRY_TRACES_SAMPLE_RATE: float = 0.1


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")  # type: ignore[call-arg]
