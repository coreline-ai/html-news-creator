.PHONY: dev migrate run run-dry test test-all lint ui-dev ui-build ui-test serve

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

ui-dev:
	cd ui && npm run dev

ui-build:
	cd ui && npm run build

ui-test:
	cd ui && npm run test

# Build the SPA bundle, then serve it (and the API) from FastAPI on :8000.
serve: ui-build
	uvicorn app.admin.api:app --port 8000
