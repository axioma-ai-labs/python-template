from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.defs import Environment


class Settings(BaseSettings):
    """Settings for the autopvs1 CLI."""

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

    #: Logging
    LOGFIRE_TOKEN: str = ""


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")  # type: ignore[call-arg]
