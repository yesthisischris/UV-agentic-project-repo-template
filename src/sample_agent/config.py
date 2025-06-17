"""Configuration for sample-agent package."""
from dataclasses import dataclass
import os

@dataclass
class Settings:
    """Application settings loaded from environment variables."""

    langsmith_api_key: str = os.getenv("LANGSMITH_API_KEY", "")

settings = Settings()
