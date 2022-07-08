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
	poetry run pytest --cov=page_loader --cov-report xml tests/

by:
	poetry build
	python3 -m pip install --force-reinstall dist/*.whl
	poetry run pytest --cov=page_loader --cov-report xml tests/
	poetry run coverage xml --data-file=./coverage.xml
	#poetry run flake8 page_loader
	#poetry run flake8 tests

test-coverage:
	poetry run coverage xml --data-file=coverage.xml
