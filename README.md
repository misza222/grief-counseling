# Grief Counseling App

The idea is that it helps people who have lost someone close to them, to process that effectively.



### TODO:
1. ~~Generate conversations to discover the domain better~~
1. What do I need to make it happen:
 - memory (multiple levels)
 - tools?
 - UI
 - evals
1. Steps:
 - [ ] Project scaffold with `uv`
 - [ ] Gradio developer UI with chat interface
 - [ ] templating for prompts (choose engine)
 - [ ] visualize app state in UI (mem, recent prompts)
 - [ ] core and session memory
 - [ ] build evals framework/use one and add checks to UI
 - [ ] introduce persistent user memory (choose simple sql/document backend)


### Prerequisites

- Python 3.11+
- `uv` (install from https://github.com/astral-sh/uv)

### Installation

```bash
# Install with uv
uv sync

# Or with pip
pip install -e ".[dev]"

### Format code
uv run ruff format .

### Lint code
uv run ruff check . --fix

### Type check
uv run mypy my_app

### Run tests
uv run pytest

### Run the app
uv run my-app

### Install pre-commit hooks
uv run pre-commit install

### Run hooks manually
uv run pre-commit run --all-files
