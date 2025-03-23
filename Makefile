locally: 
	dagster dev

dependencies:
	uv venv
	uv pip install -e ".[dev]"

update_packages:
	uv lock --upgrade;

ruff:
	-ruff check --fix .
	ruff format .