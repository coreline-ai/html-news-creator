"""Editorial policy + source-registry endpoints.

Routes:
  - GET  /api/policy
  - PUT  /api/policy
  - POST /api/policy/persist
  - GET  /api/sources
  - POST /api/sources
  - PUT  /api/sources/{name}
"""

from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse

from fastapi import APIRouter, Body, HTTPException

from app.admin.policy_admin import (
    get_policy,
    persist_runtime_override_to_yaml,
    set_policy_override,
)
from app.admin.routers._models import (
    AddSourceRequest,
    PolicyPatchRequest,
    SourcePatchRequest,
)
from app.admin.sources_admin import (
    add_source as registry_add_source,
    list_sources as registry_list_sources,
    update_source as registry_update_source,
)
from app.utils.logger import get_logger

logger = get_logger(step="admin")

router = APIRouter()


@router.get("/api/policy")
async def api_get_policy():
    return {"policy": get_policy()}


@router.put("/api/policy")
async def api_put_policy(payload: PolicyPatchRequest = Body(default_factory=PolicyPatchRequest)):
    try:
        merged = set_policy_override(payload.patch or {})
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"policy": merged}


# POST /api/policy/persist — flush the volatile override into yaml.
# Errors:
#   400 — runtime override is empty (nothing to persist).
#   500 — atomic write failed (disk full, permissions, etc.).
@router.post("/api/policy/persist")
async def api_persist_policy():
    """Atomically write the in-memory runtime override into ``editorial_policy.yaml``.

    Creates a ``*.yaml.bak`` next to the target on success so the operator can
    recover the previous policy. Body is intentionally empty — the helper uses
    the project-default yaml path.
    """
    try:
        result = persist_runtime_override_to_yaml()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:  # pragma: no cover — defensive
        logger.error("policy_persist_failed", error=str(exc))
        raise HTTPException(status_code=500, detail=f"policy persist failed: {exc}")

    project_root = Path(__file__).resolve().parents[3]
    persisted = result["persisted_to"]
    backup = result["backup"]

    def _to_rel(path: Path | None) -> str | None:
        if path is None:
            return None
        try:
            return str(Path(path).resolve().relative_to(project_root))
        except ValueError:
            return str(path)

    return {
        "persisted_to": _to_rel(persisted),
        "backup": _to_rel(backup),
    }


@router.get("/api/sources")
async def api_list_sources():
    return {"sources": registry_list_sources()}


# POST /api/sources — append a new entry to the registry yaml.
# Errors:
#   400 — missing/invalid required field, duplicate name, unknown key,
#         malformed url (when supplied).
@router.post("/api/sources", status_code=201)
async def api_add_source(
    payload: AddSourceRequest = Body(...),
):
    fields = payload.to_fields()

    # Validate URL eagerly when supplied — the registry layer accepts
    # arbitrary strings, but the FE always sends a value so we want a clear
    # error here rather than at collect-time.
    url = fields.get("url")
    if url is not None:
        parsed = urlparse(str(url))
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise HTTPException(
                status_code=400,
                detail="'url' must be an http(s) URL with a host",
            )

    try:
        created = registry_add_source(fields)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"source": created}


@router.put("/api/sources/{name}")
async def api_update_source(
    name: str,
    payload: SourcePatchRequest = Body(default_factory=SourcePatchRequest),
):
    fields = payload.to_fields()
    if not fields:
        raise HTTPException(status_code=400, detail="no updatable fields supplied")
    try:
        updated = registry_update_source(name, fields)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"source": updated}
