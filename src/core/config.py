from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the autopvs1 CLI."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

    # === General settings ===

    #: Whether to enable debug mode
    DEBUG: bool = False

    #: Project name
    PROJECT_NAME: str = ""


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")  # type: ignore[call-arg]
