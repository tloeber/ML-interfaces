setup:
	@# Install Poetry into base environment, if not already present
	python3 -m poetry --version | pip3 install poetry

	@# Note that Poetry creates *editable* install for root project by default
	python3 -m poetry install

	@echo "Please manually set environment as default in IDE for this project, so you "
	@echo "don't have to manually activate it for each shell using 'python3 -m poetry shell'"
	@echo "Location: `python3 -m poetry env info`"

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish
