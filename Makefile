install:
	uv sync

update:
	uv lock --upgrade
	uv sync

gendiff-json:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json

gendiff-yml:
	uv run gendiff tests/test_data/file1.yml tests/test_data/file2.yml

gendiff-help:
	uv run gendiff -h

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check
	
check: test lint

build:
	uv build

package-install:
	uv tool install dist/*.whl
	
package-force-install:
	uv tool install --force dist/*.whl

.PHONY: install gendiff gendiff-help test test-coverage lint check build package-install package-force-install