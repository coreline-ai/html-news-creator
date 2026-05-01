.PHONY: dev migrate backup run run-dry test test-all test-integration lint lint-design build-tokens check-tokens ui-dev ui-build ui-test serve e2e

dev:
	docker compose up -d

migrate:
	psql "$(DATABASE_URL)" -f migrations/001_initial.sql

# Personal-use database backup. Dumps the live ai-trend-postgres container to
# a gzip'd timestamped file under $(BACKUP_DIR) (default: ~/Backups/html-news-creator).
# Drops backups older than 30 days. Install via crontab for daily automation:
#   0 23 * * * cd /Users/hwanchoi/projects/html-news-creator && make backup >> $$HOME/Backups/html-news-creator/cron.log 2>&1
BACKUP_DIR ?= $(HOME)/Backups/html-news-creator
backup:
	@mkdir -p "$(BACKUP_DIR)"
	@docker exec ai-trend-postgres pg_dump -U postgres ai_trend | gzip > "$(BACKUP_DIR)/$$(date +%Y%m%d_%H%M%S).sql.gz"
	@find "$(BACKUP_DIR)" -name "*.sql.gz" -mtime +30 -delete
	@echo "Backup written to $(BACKUP_DIR) (retention: 30 days)"

run:
	python scripts/run_daily.py --mode full

run-dry:
	python scripts/run_daily.py --mode full --dry-run

test:
	pytest tests/unit/ -v --tb=short

test-all:
	pytest tests/ -v --tb=short

# Integration smoke tests — drive the FastAPI app through an in-memory ASGI
# transport (no uvicorn, no Postgres, no LLM proxy). The pipeline subprocess
# and Netlify deploy are mocked at the module boundary. CI's default unit
# job uses `pytest -m "not integration"` so these are opt-in only.
test-integration:
	pytest tests/integration/ -v --tb=short -m integration

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
