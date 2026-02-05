"""Command-line interface for my app."""

from loguru import logger


def main() -> None:
    """Main entry point."""
    logger.info("Hello from my-app!")


if __name__ == "__main__":
    main()
