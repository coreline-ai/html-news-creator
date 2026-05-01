"""In-memory preview rendering for News Studio.

The preview path renders the daily report HTML using the existing
``app.rendering.jinja_renderer`` but with a per-request options patch that
overrides the editorial policy. **It performs zero DB writes**.

If a real DB report exists for ``date_kst`` we hydrate from it (read-only).
Otherwise we synthesize a mock report so the operator can still see how the
template responds to editorial knobs before any pipeline run.
"""
from __future__ import annotations

import asyncio
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from app.admin.policy_admin import merge_with_options
from app.rendering.jinja_renderer import JinjaRenderer

TEMPLATES_DIR = str(Path(__file__).resolve().parents[2] / "templates")

# Mock fixtures used when no DB report exists / DB unreachable
_MOCK_TITLES = [
    "OpenAI, 차세대 모델 공개 — 공식 발표",
    "Anthropic Claude 업데이트 요약",
    "Google DeepMind 연구 노트",
    "Hugging Face 신규 모델 트렌드",
    "Microsoft Copilot 통합 확장",
    "Meta AI 오픈소스 릴리스",
    "Mistral 신규 가중치 공개",
    "AI 정책 동향 — 산업 영향",
    "AI 도구 생태계 — 개발자 신호",
    "AI 인프라 시장 변화",
]


def _coerce_target_sections(options: dict[str, Any]) -> int:
    """Resolve ``target_sections`` from the merged options, with bounds."""
    selection = options.get("report_selection") or {}
    target = options.get("target_sections")
    if target is None:
        target = selection.get("target_sections")
    if target is None:
        target = 10
    try:
        target = int(target)
    except (TypeError, ValueError):
        raise ValueError(f"target_sections must be int-coercible: {target!r}")
    if target < 1 or target > 30:
        raise ValueError(f"target_sections out of range [1, 30]: {target}")
    return target


def _mock_section(idx: int) -> dict[str, Any]:
    title = _MOCK_TITLES[idx % len(_MOCK_TITLES)]
    return {
        "title": title,
        "summary_ko": f"미리보기용 섹션 {idx + 1}: 옵션 변경의 효과를 확인하세요.",
        "fact_summary": "이 섹션은 미리보기 모드에서 합성된 데이터입니다.",
        "social_signal_summary": "",
        "inference_summary": "",
        "importance_score": 80.0 - idx * 2,
        "verification_status": "official_confirmed" if idx == 0 else "trusted_media_only",
        "sources_json": [
            {"name": "Preview", "url": "https://example.com/preview"}
        ],
        "content_image_urls": [],
        "og_image_url": "",
        "category": "other",
    }


def _mock_report(date_kst: str | None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    today = date_kst or date.today().isoformat()
    report = {
        "title": f"AI 트렌드 리포트 {today} (미리보기)",
        "report_date": today,
        "summary_ko": "미리보기 모드 — 옵션 오버라이드를 적용한 합성 데이터입니다.",
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "stats": {
            "total_sources": 0,
            "ai_relevant": 0,
            "clusters": 0,
            "verified": 0,
        },
    }
    return report, []


async def _hydrate_from_db(
    date_kst: str,
) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    """Read the persisted report + sections (read-only).

    Returns ``(None, [])`` when DB is unreachable or the date has no report —
    the caller falls back to mocks.
    """
    try:
        from sqlalchemy import select

        from app.db import AsyncSessionLocal
        from app.models.db_models import Report, ReportSection
    except Exception:
        return None, []

    try:
        run_date = date.fromisoformat(date_kst)
    except ValueError:
        return None, []

    try:
        async with AsyncSessionLocal() as session:
            db_report = await session.scalar(
                select(Report).where(Report.report_date == run_date)
            )
            if not db_report:
                return None, []
            sections_rows = list(
                await session.scalars(
                    select(ReportSection)
                    .where(ReportSection.report_id == db_report.id)
                    .order_by(ReportSection.section_order)
                )
            )
    except Exception:
        return None, []

    report_data = {
        "title": db_report.title,
        "report_date": str(db_report.report_date),
        "summary_ko": db_report.summary_ko or "",
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "stats": dict(db_report.stats_json or {}),
    }
    sections_data: list[dict[str, Any]] = []
    for rs in sections_rows:
        sections_data.append(
            {
                "title": rs.title or "",
                "summary_ko": rs.fact_summary or "",
                "fact_summary": rs.fact_summary,
                "social_signal_summary": rs.social_signal_summary,
                "inference_summary": rs.inference_summary,
                "importance_score": rs.importance_score or 0.0,
                "verification_status": "unverified",
                "sources_json": rs.sources_json or [],
                "content_image_urls": [],
                "og_image_url": "",
                "category": "other",
            }
        )
    return report_data, sections_data


def render_preview(
    options: dict[str, Any] | None = None,
    date_kst: str | None = None,
) -> str:
    """Render an HTML preview with ``options`` applied as a policy override.

    No database writes ever happen on this path (`AGENTS.md` rule). When a DB
    report for ``date_kst`` is available it is fetched read-only; otherwise the
    template is rendered against synthesized mock data so operators can still
    iterate on options before producing a real run.
    """
    opts = options or {}
    if not isinstance(opts, dict):
        raise ValueError("options must be a mapping")

    merged = merge_with_options(opts)
    target_sections = _coerce_target_sections(opts if "target_sections" in opts else merged)

    report_data: dict[str, Any] | None = None
    sections_data: list[dict[str, Any]] = []
    if date_kst:
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Caller is already in an async context; this sync wrapper
                # only runs in tests / dev tooling that don't supply a running
                # loop. Fall through to mock data to stay non-blocking.
                report_data, sections_data = None, []
            else:
                report_data, sections_data = loop.run_until_complete(
                    _hydrate_from_db(date_kst)
                )
        except RuntimeError:
            report_data, sections_data = asyncio.run(_hydrate_from_db(date_kst))

    if report_data is None:
        report_data, sections_data = _mock_report(date_kst)

    # Slice / pad sections to the requested target, mocking extras when needed.
    if len(sections_data) > target_sections:
        sections_data = sections_data[:target_sections]
    elif len(sections_data) < target_sections:
        for idx in range(len(sections_data), target_sections):
            sections_data.append(_mock_section(idx))

    report_data.setdefault("stats", {})
    report_data["stats"] = dict(report_data["stats"])
    report_data["stats"]["clusters"] = len(sections_data)

    output_theme = (opts.get("output_theme") if isinstance(opts, dict) else None) or "dark"

    renderer = JinjaRenderer(templates_dir=TEMPLATES_DIR)
    return renderer.render_report(
        report_data, sections_data, output_theme=output_theme
    )


__all__ = ["render_preview"]
