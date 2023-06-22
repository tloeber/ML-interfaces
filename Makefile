setup:
	# Install Poetry into base environment, if not already present
	python3 -m poetry --version | pip3 install poetry

	# Note that Poetry creates *editable* install for root project by default
	python3 -m poetry install

	# Activate virtual environment for current shell
	# Note: You need to manually set it as default in IDE for this project!
	python3 -m poetry shell

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish
