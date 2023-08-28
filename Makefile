setup:
	@# Install Poetry into base environment, if not already present
	python3 -m poetry --version | pip3 install poetry

	@# Note that Poetry creates *editable* install for root project by default
	python3 -m poetry install

	@echo "\nPlease manually set this environment as default in IDE for this project (so you "\
		"don't have to manually activate it for each shell using 'python3 -m poetry shell')."
	@echo `python3 -m poetry env info | grep Path:`

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish
