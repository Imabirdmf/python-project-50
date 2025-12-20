install:
	pip install flake8 black isort mypy

lint:
	flake8 .
	black --check .
	isort --check-only .
	mypy .

format:
	black .
	isort .