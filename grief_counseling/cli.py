"""Command-line interface for my app."""

import sys

from loguru import logger


def main() -> None:
    """Main entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "ui":
        # Launch Gradio UI
        from grief_counseling.ui import launch

        launch()
    else:
        # Default CLI behavior
        logger.info("Hello from grief-counseling!")
        logger.info("Use 'grief-counseling ui' to launch the Gradio interface")


if __name__ == "__main__":
    main()
