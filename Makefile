install:
	uv sync
gendiff:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json
gendiff-help:
	uv run gendiff -h
lint:
	uv run ruff check gendiff
build:
	uv build
package-install:
	uv tool install dist/*.whl
package-force-install:
	uv tool install --force dist/*.whl

.PHONY: install gendiff lint build package-install package-force-install