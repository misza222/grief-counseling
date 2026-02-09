"""Core module with example functionality."""

from pydantic import BaseModel


class Entity(BaseModel):
    """Application configuration."""

    name: str
    debug: bool = False


def process_config(entity: Entity) -> str:
    """Process configuration and return result."""
    return f"Configured app: {entity.name} (debug={entity.debug})"
