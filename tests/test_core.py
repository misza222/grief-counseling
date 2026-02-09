"""Tests for core module."""

from grief_counseling.core import Entity, process_config


def test_process_config() -> None:
    """Test configuration processing."""
    entity = Entity(name="test-app")
    result = process_config(entity)
    print(result)
    assert "test-app" in result
    assert "debug=False" in result
