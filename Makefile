locally: manifest
	clear
	dagster dev

ruff:
	-ruff check --fix .
	ruff format .