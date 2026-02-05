.PHONY: help install lint format type test clean run

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make lint       - Run linting"
	@echo "  make format     - Format code"
	@echo "  make type       - Run type checking"
	@echo "  make test       - Run tests"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make run        - Run the application"

install:
	uv sync

lint:
	uv run ruff check .

format:
	uv run ruff format .
	uv run ruff check . --fix

type:
	uv run mypy grief_counseling

test:
	uv run pytest --cov=grief_counseling

clean:
	rm -rf build dist *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov

run:
	uv run main
