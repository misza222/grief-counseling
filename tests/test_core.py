"""Tests for core module."""

from grief_counseling.core import Config, process_config


def test_process_config() -> None:
    """Test configuration processing."""
    config = Config(name="test-app")
    result = process_config(config)
    print(result)
    assert "test-app" in result
    assert "debug=False" in result
