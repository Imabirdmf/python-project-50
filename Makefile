install:
	uv sync

lint:
	uv run flake8 .
	uv run black --check .
	uv run isort --check-only .
	uv run mypy .

format:
	uv run black .
	uv run isort .

check:
	uv run pytest .

test-coverage:
	 uv run pytest --cov --cov-report=xml:coverage.xml --cov-config=.coveragerc --cov-branch