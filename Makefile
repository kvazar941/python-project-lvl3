install:
	poetry install

run:
	poetry run page-loader

build:
	poetry build

package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 loader
	poetry run flake8 tests

tests:
	poetry run pytest

by:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl
	poetry run pytest
	poetry run flake8 loader
	poetry run flake8 tests
