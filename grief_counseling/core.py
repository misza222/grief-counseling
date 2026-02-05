"""Core module with example functionality."""

from pydantic import BaseModel


class Config(BaseModel):
    """Application configuration."""

    name: str
    debug: bool = False


def process_config(config: Config) -> str:
    """Process configuration and return result."""
    return f"Configured app: {config.name} (debug={config.debug})"
