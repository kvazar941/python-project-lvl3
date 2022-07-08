install:
	poetry install

run:
	poetry run page-loader

build:
	poetry build

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 page_loader
	poetry run flake8 tests

tests:
	poetry run pytest

by:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl
	poetry run pytest
	poetry run flake8 page_loader
	poetry run flake8 tests

coverage:
	poetry run pytest -v --cov=page_loader tests/ --cov-report xml
