"""News Studio FastAPI app — composition root.

Route handlers live in :mod:`app.admin.routers`; this module wires the
FastAPI instance, CORS, the four routers, and the SPA static mount in the
correct order (SPA fallback MUST be last so it does not shadow ``/api/*``).
"""

from __future__ import annotations
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.admin.routers import (
    legacy_router,
    policy_router,
    reports_router,
    runs_router,
)
from app.config import settings
from app.utils.logger import get_logger

app = FastAPI(
    title="News Studio API",
    description="Admin + News Studio web UI for the AI Trend Report engine",
    version="0.2.0",
)

# CORS — Vite dev server lives at localhost:5173 by default; honor the
# configured origin for non-default deploys.
_allowed_origins = list({"http://localhost:5173", settings.ui_dev_origin})
app.add_middleware(
    CORSMiddleware,
    allow_origins=_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = get_logger(step="admin")

# Order matters only between the SPA fallback and the routers; among the
# routers themselves FastAPI's matcher prefers more specific paths so the
# include order is purely cosmetic.
app.include_router(legacy_router)
app.include_router(reports_router)
app.include_router(runs_router)
app.include_router(policy_router)


# ---------------------------------------------------------------------------
# Phase 6 — Static SPA mount (MUST be last so it does not shadow /api routes)
# ---------------------------------------------------------------------------

_ui_dist = Path(settings.ui_dist_path)
if _ui_dist.is_dir():
    # Serve hashed assets out of /assets/* with proper caching headers via
    # StaticFiles. The SPA fallback below handles every other path so that
    # client-side routes (e.g. /sources, /reports/2026-04-30) survive a hard
    # refresh by rendering index.html.
    _assets_dir = _ui_dist / "assets"
    if _assets_dir.is_dir():
        app.mount(
            "/assets",
            StaticFiles(directory=str(_assets_dir)),
            name="ui-assets",
        )

    _index_html = _ui_dist / "index.html"

    @app.get("/{full_path:path}", include_in_schema=False)
    async def spa_fallback(full_path: str) -> Any:
        # Never shadow API routes — they are registered above and FastAPI's
        # router resolution would already have matched them. Defensive guard
        # in case of unknown /api/* requests so the user gets JSON 404 rather
        # than HTML.
        if full_path.startswith("api/") or full_path == "api":
            raise HTTPException(status_code=404, detail="Not Found")

        # index.html and SPA fallback responses must NEVER be cached, otherwise
        # users keep loading old chunk hashes after a fresh build (the symptom
        # was 404 on Sources-XXXX.js after rebuilding tokens.css). /assets/* is
        # already content-hashed by Vite so the StaticFiles mount above can
        # cache long-term — this only applies to the shell.
        no_store = {"Cache-Control": "no-store, must-revalidate"}

        # Top-level static files (favicon.ico, robots.txt, etc.) ship straight
        # from disk when they exist.
        candidate = (_ui_dist / full_path).resolve()
        try:
            candidate.relative_to(_ui_dist.resolve())
        except ValueError:
            # Path traversal — fall through to index.html.
            candidate = None  # type: ignore[assignment]
        if candidate and candidate.is_file():
            # Top-level non-hashed files (favicon, robots) get default caching
            # via FileResponse, but if the request is for an unhashed JS/CSS
            # at the root we still want freshness. Apply no-store only to the
            # shell entry.
            return FileResponse(str(candidate))

        # All other paths render the SPA shell — must always be fresh.
        return FileResponse(str(_index_html), headers=no_store)

else:
    logger.info(
        "ui_dist_not_found",
        path=str(_ui_dist),
        note="run `make ui-build` to populate ui/dist before serving the SPA",
    )
