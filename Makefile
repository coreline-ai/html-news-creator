.PHONY: dev migrate run run-dry test test-all lint lint-design build-tokens check-tokens ui-dev ui-build ui-test serve e2e

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

# Scan ui/src/ (excluding shadcn primitives) for raw colors, radius, and
# shadows that bypass docs/design/tokens.css. Spec: docs/design/06-automation-spec.md §4.
lint-design:
	python3 scripts/lint_design_tokens.py

# Regenerate docs/design/tokens.css from docs/design/tokens.json.
build-tokens:
	python3 scripts/build_tokens.py

# CI gate: fail if tokens.css would change after rebuild from tokens.json.
check-tokens:
	python3 scripts/build_tokens.py --check

ui-dev:
	cd ui && npm run dev

ui-build:
	cd ui && npm run build

ui-test:
	cd ui && npm run test

# Build the SPA bundle, then serve it (and the API) from FastAPI on :8000.
serve: ui-build
	uvicorn app.admin.api:app --port 8000

# Run Playwright E2E tests against a freshly built SPA + the API. Tests
# mock all `/api/*` calls, so the DB state doesn't matter — but a server
# must be reachable on :8000 (Playwright's webServer config will boot one
# automatically if not).
e2e: ui-build
	cd ui && npx playwright test
