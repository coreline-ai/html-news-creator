"""News Studio API routers.

Split from the original monolithic ``app/admin/api.py`` for readability.
Each module exposes a ``router = APIRouter()`` that ``api.py`` includes.
"""

from app.admin.routers.legacy import router as legacy_router
from app.admin.routers.policy import router as policy_router
from app.admin.routers.reports import router as reports_router
from app.admin.routers.runs import router as runs_router

__all__ = [
    "legacy_router",
    "policy_router",
    "reports_router",
    "runs_router",
]
