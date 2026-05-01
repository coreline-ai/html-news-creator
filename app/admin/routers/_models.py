"""Pydantic request/response models shared across the admin routers.

Extracted verbatim from the previous ``app/admin/api.py`` so import paths
inside the routers stay self-contained — no behavioural change.
"""

from __future__ import annotations
from typing import Any, Optional

from pydantic import BaseModel, Field

from app.admin.sources_admin import ALLOWED_UPDATE_FIELDS


class PreviewRequest(BaseModel):
    target_sections: Optional[int] = Field(default=None, ge=1, le=30)
    date_kst: Optional[str] = None
    # Free-form policy overrides — accepted as a nested dict.
    policy_override: Optional[dict] = None

    model_config = {"extra": "allow"}


class RunRequest(BaseModel):
    date: Optional[str] = None
    mode: Optional[str] = None
    from_step: Optional[str] = None
    to_step: Optional[str] = None
    dry_run: bool = False

    model_config = {"extra": "allow"}


class PolicyPatchRequest(BaseModel):
    patch: Optional[dict] = None


class SourcePatchRequest(BaseModel):
    enabled: Optional[bool] = None
    priority: Optional[int] = None
    max_items: Optional[int] = None
    trust_level: Optional[str] = None
    source_tier: Optional[str] = None
    category: Optional[str] = None

    def to_fields(self) -> dict[str, Any]:
        return {
            key: getattr(self, key)
            for key in ALLOWED_UPDATE_FIELDS
            if getattr(self, key, None) is not None
        }


class AddSourceRequest(BaseModel):
    """Body for ``POST /api/sources`` — append a new yaml registry entry.

    ``name`` and ``source_type`` are required; everything else is optional and
    validated/whitelisted by :func:`app.admin.sources_admin.add_source`. The
    pydantic layer is intentionally permissive (no ``Literal`` enums) so
    domain-level errors come through as HTTP 400 with a readable message.
    """

    name: str
    source_type: str
    url: Optional[str] = None
    homepage_url: Optional[str] = None
    trust_level: Optional[str] = None
    source_tier: Optional[str] = None
    category: Optional[str] = None
    priority: Optional[int] = None
    max_items: Optional[int] = None
    enabled: Optional[bool] = None
    org: Optional[str] = None
    query: Optional[str] = None
    listing_url: Optional[str] = None
    sitemap_url: Optional[str] = None
    include_url_patterns: Optional[list[str]] = None
    max_candidates: Optional[int] = None
    collector_type: Optional[str] = None
    content_category: Optional[str] = None

    model_config = {"extra": "ignore"}

    def to_fields(self) -> dict[str, Any]:
        return {k: v for k, v in self.model_dump().items() if v is not None}


class SectionPatchRequest(BaseModel):
    """Allowed editable fields on a single ReportSection.

    Maps to the existing DB columns:
      - title          → ReportSection.title
      - summary_ko     → ReportSection.fact_summary
      - implication_ko → ReportSection.inference_summary
      - image_url      → injected into image_evidence_json (first entry)
    """

    title: Optional[str] = None
    summary_ko: Optional[str] = None
    implication_ko: Optional[str] = None
    image_url: Optional[str] = None

    model_config = {"extra": "ignore"}

    def has_any(self) -> bool:
        return any(
            getattr(self, k) is not None
            for k in ("title", "summary_ko", "implication_ko", "image_url")
        )


class ReorderRequest(BaseModel):
    section_ids: list[str] = Field(default_factory=list)


class PublishRequest(BaseModel):
    publish_dir: Optional[str] = None
    dry_run: bool = False
    # Section UUIDs the operator toggled OFF in Review. The DB row has no
    # `enabled` column — re-render time is the only place we apply this.
    disabled_section_ids: Optional[list[str]] = None

    model_config = {"extra": "allow"}


class RenderRequest(BaseModel):
    """Body for ``POST /api/reports/{date}/render`` — render-only debug hook."""

    disabled_section_ids: Optional[list[str]] = None

    model_config = {"extra": "allow"}
