"""
Configuration settings for the application.

Loads environment variables and provides application settings.
"""

from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"
    )

    # Database
    DATABASE_URL: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_DAYS: int = 7

    # App
    APP_NAME: str = "Salesforce Admin Learning Platform"
    VERSION: str = "0.30.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # CORS - can be comma-separated string or will use defaults
    ALLOWED_ORIGINS: Optional[str] = None

    # Content
    CONTENT_PATH: str = "./content"

    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100

    def get_allowed_origins(self) -> List[str]:
        """Get ALLOWED_ORIGINS as a list."""
        if self.ALLOWED_ORIGINS:
            return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]
        return [
            "http://localhost:3000",
            "http://localhost:8000",
            "http://127.0.0.1:8000",
        ]


settings = Settings()
