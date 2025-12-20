install:
	pip install flake8 black isort mypy

lint:
	@echo "--- Запуск Flake8 (поиск ошибок) ---"
	flake8 .
	@echo "--- Запуск Black (проверка форматирования) ---"
	black --check .
	@echo "--- Запуск isort (проверка импортов) ---"
	isort --check-only .
	@echo "--- Запуск Mypy (проверка типов) ---"
	mypy .

format:
	black .
	isort .