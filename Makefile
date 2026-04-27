.PHONY: dev migrate run run-dry test test-all lint

dev:
	docker compose up -d

migrate:
	psql "$(DATABASE_URL)" -f migrations/001_initial.sql

run:
	python scripts/run_daily.py --mode full

run-dry:
	python scripts/run_daily.py --mode full --dry-run

test:
	pytest tests/unit/ -v --tb=short

test-all:
	pytest tests/ -v --tb=short

lint:
	ruff check app/ scripts/ tests/
