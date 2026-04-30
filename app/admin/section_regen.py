"""Single-section regeneration helper.

Bridges the FastAPI admin route to the existing LLM-backed
`SectionGenerator` from `app.generation.section_generator`.

Design notes:
- Touches a single `ReportSection` row by id; never mutates other sections.
- Uses the section's `cluster_id` to load the same RawItem/ExtractedContent
  shape that the daily pipeline feeds to `SectionGenerator.generate()`.
- Maps the LLM result back onto the editable columns:
    title          ← title_ko
    fact_summary   ← fact_summary  (legacy: summary_ko)
    inference_summary ← inference_summary
- Raises ValueError on bad input so the route can surface a 4xx; lets other
  exceptions bubble for a generic 500.
"""
from __future__ import annotations

from typing import Any

from sqlalchemy import select

from app.db import AsyncSessionLocal
from app.generation.section_generator import SectionGenerator
from app.models.db_models import (
    ClusterItem,
    ExtractedContent,
    RawItem,
    ReportSection,
)
from app.utils.logger import get_logger

logger = get_logger(step="admin")


async def _load_cluster_items(session, cluster_id: Any) -> list[dict]:
    """Build the SectionGenerator-compatible item dicts for a cluster."""
    stmt = (
        select(RawItem, ExtractedContent)
        .join(ClusterItem, ClusterItem.raw_item_id == RawItem.id)
        .outerjoin(
            ExtractedContent, ExtractedContent.raw_item_id == RawItem.id
        )
        .where(ClusterItem.cluster_id == cluster_id)
    )
    rows = list(await session.execute(stmt))
    items: list[dict] = []
    for ri, ec in rows:
        items.append(
            {
                "title": ri.title or "",
                "url": ri.url or "",
                "content_text": (ec.content_text if ec else ri.raw_text) or "",
            }
        )
    return items


async def regenerate_section(section_id: str) -> dict:
    """Regenerate a single ReportSection's editorial fields via the LLM.

    Returns a dict with the updated section fields. Raises:
      - LookupError if section is missing
      - ValueError if the section has no cluster_id (can't regen)
    """
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(ReportSection).where(ReportSection.id == section_id)
        )
        section = result.scalars().first()
        if section is None:
            raise LookupError(f"section not found: {section_id}")

        if section.cluster_id is None:
            raise ValueError(
                f"section {section_id} has no cluster_id; cannot regenerate"
            )

        items = await _load_cluster_items(session, section.cluster_id)

        generator = SectionGenerator()
        generated = await generator.generate(str(section.cluster_id), items)

        # Map LLM output → editable columns (single-row update only).
        new_title = generated.get("title_ko") or section.title
        new_fact = generated.get("fact_summary")
        new_inference = generated.get("inference_summary")

        section.title = new_title
        if new_fact is not None:
            section.fact_summary = new_fact
        if new_inference is not None:
            section.inference_summary = new_inference

        await session.commit()
        await session.refresh(section)

        logger.info(
            "regenerate_section_done",
            section_id=section_id,
            cluster_id=str(section.cluster_id),
        )
        return {
            "id": str(section.id),
            "title": section.title,
            "fact_summary": section.fact_summary,
            "inference_summary": section.inference_summary,
            "cluster_id": str(section.cluster_id),
        }
