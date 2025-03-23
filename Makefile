locally: manifest
	clear
	dagster dev

dependencies
	uv pip install -e ".[dev]"

update_packages:
	uv lock --upgrade;

ruff:
	-ruff check --fix .
	ruff format .