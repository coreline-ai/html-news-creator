#!/usr/bin/env python3
"""Daily AI trend report pipeline entrypoint."""
from __future__ import annotations
import asyncio
from datetime import date, datetime, timezone
import click
from app.utils.logger import get_logger

STEPS = [
    "collect",
    "extract",
    "classify",
    "cluster",
    "verify",
    "image_analyze",
    "generate",
    "render",
    "publish",
    "notify",
]


async def run_collect(run_date: date, dry_run: bool, logger, source_types=None) -> dict:
    from app.collectors.orchestrator import CollectorOrchestrator
    from app.db import AsyncSessionLocal
    from app.models.db_models import RawItem
    from sqlalchemy import select

    orchestrator = CollectorOrchestrator()
    items = await orchestrator.collect_items(run_date, source_types=source_types)

    total = len(items)
    inserted = 0
    skipped = 0

    if dry_run:
        logger.info("dry_run_collect", total=total)
    else:
        async with AsyncSessionLocal() as session:
            for item in items:
                existing = await session.scalar(
                    select(RawItem).where(RawItem.canonical_url_hash == item.canonical_url_hash)
                )
                if existing:
                    skipped += 1
                    continue
                db_item = RawItem(
                    source_type=item.source_type,
                    title=item.title,
                    url=item.url,
                    canonical_url=item.canonical_url,
                    canonical_url_hash=item.canonical_url_hash,
                    raw_text=item.raw_text,
                    author=item.author,
                    published_at=item.published_at,
                    metrics_json=item.metrics_json or {},
                    raw_json=item.raw_json or {},
                )
                session.add(db_item)
                inserted += 1
            await session.commit()

    logger.info("collect_done", total=total, inserted=inserted, skipped=skipped)
    return {"total": total, "inserted": inserted, "skipped": skipped}


async def run_extract(run_date: date, dry_run: bool, logger) -> dict:
    from app.db import AsyncSessionLocal
    from app.models.db_models import RawItem, ExtractedContent
    from app.extractors.trafilatura import TrafilaturaExtractor
    from app.extractors.base import ExtractorUnavailableError, ExtractorError
    from sqlalchemy import select, not_, exists

    extractor = TrafilaturaExtractor()

    async with AsyncSessionLocal() as session:
        stmt = select(RawItem).where(
            not_(exists().where(ExtractedContent.raw_item_id == RawItem.id))
        )
        raw_items = list(await session.scalars(stmt))

    extracted = 0
    failed = 0

    for raw_item in raw_items:
        try:
            result = await extractor.extract(raw_item.url, str(raw_item.id))
            if not dry_run:
                async with AsyncSessionLocal() as session:
                    ec = ExtractedContent(
                        raw_item_id=raw_item.id,
                        extractor=result.extractor,
                        extraction_status=result.status,
                        content_text=result.content_text,
                        content_markdown=result.content_markdown,
                        quality_score=result.quality_score,
                        metadata_json={},
                    )
                    session.add(ec)
                    await session.commit()
            extracted += 1
        except (ExtractorUnavailableError, ExtractorError) as e:
            logger.error("extract_failed", url=raw_item.url, error=str(e))
            failed += 1
        except Exception as e:
            logger.error("extract_error", url=raw_item.url, error=str(e))
            failed += 1

    logger.info("extract_done", extracted=extracted, failed=failed)
    return {"extracted": extracted, "failed": failed}


async def run_classify(run_date: date, dry_run: bool, logger) -> dict:
    from app.db import AsyncSessionLocal
    from app.models.db_models import RawItem, ExtractedContent, AnalysisResult
    from app.processors.classifier import RelevanceClassifier
    from sqlalchemy import select, not_, exists

    classifier = RelevanceClassifier()

    async with AsyncSessionLocal() as session:
        # Items with extracted content
        stmt = (
            select(RawItem, ExtractedContent)
            .join(ExtractedContent, ExtractedContent.raw_item_id == RawItem.id)
            .where(not_(exists().where(AnalysisResult.raw_item_id == RawItem.id)))
        )
        rows = list(await session.execute(stmt))
        # Items without extracted content — fall back to raw_text
        stmt2 = (
            select(RawItem)
            .where(not_(exists().where(ExtractedContent.raw_item_id == RawItem.id)))
            .where(not_(exists().where(AnalysisResult.raw_item_id == RawItem.id)))
        )
        raw_only = list(await session.scalars(stmt2))

    # Combine: extracted items + raw-only items (ec=None)
    combined = [(ri, ec) for ri, ec in rows] + [(ri, None) for ri in raw_only]

    classified = 0
    ai_related = 0

    for raw_item, ec in combined:
        content = (ec.content_text if ec else None) or raw_item.raw_text or ""
        result = await classifier.classify(
            title=raw_item.title or "",
            content=content,
            item_id=str(raw_item.id),
        )
        if not dry_run:
            async with AsyncSessionLocal() as session:
                ar = AnalysisResult(
                    raw_item_id=raw_item.id,
                    extracted_content_id=ec.id if ec else None,
                    is_ai_related=result.get("is_ai_related", False),
                    ai_relevance_score=result.get("score", 0.0),
                    confidence=result.get("score", 0.0),
                    summary_ko=result.get("reason_ko", ""),
                )
                session.add(ar)
                await session.commit()
        if result.get("is_ai_related"):
            ai_related += 1
        classified += 1

    logger.info("classify_done", classified=classified, ai_related=ai_related)
    return {"classified": classified, "ai_related": ai_related}


async def run_cluster(run_date: date, dry_run: bool, logger) -> dict:
    from app.db import AsyncSessionLocal
    from app.models.db_models import RawItem, ExtractedContent, AnalysisResult, Cluster, ClusterItem
    from app.generation.embeddings import EmbeddingClient
    from app.generation.clusterer import HDBSCANClusterer
    from sqlalchemy import select, not_, exists

    async with AsyncSessionLocal() as session:
        # AI-relevant items with extracted content
        stmt = (
            select(RawItem, ExtractedContent)
            .join(AnalysisResult, AnalysisResult.raw_item_id == RawItem.id)
            .join(ExtractedContent, ExtractedContent.raw_item_id == RawItem.id)
            .where(AnalysisResult.is_ai_related == True)  # noqa: E712
        )
        rows = list(await session.execute(stmt))
        # AI-relevant items without extracted content — use raw_text fallback
        stmt2 = (
            select(RawItem)
            .join(AnalysisResult, AnalysisResult.raw_item_id == RawItem.id)
            .where(AnalysisResult.is_ai_related == True)  # noqa: E712
            .where(not_(exists().where(ExtractedContent.raw_item_id == RawItem.id)))
        )
        raw_only = list(await session.scalars(stmt2))

    combined = [(ri, ec) for ri, ec in rows] + [(ri, None) for ri in raw_only]

    if not combined:
        logger.info("cluster_done", clusters=0, items=0, note="no AI-relevant items")
        return {"clusters": 0, "items": 0}

    texts = [
        f"{ri.title or ''}\n{((ec.content_text if ec else None) or ri.raw_text or '')[:500]}"
        for ri, ec in combined
    ]

    embedder = EmbeddingClient()
    vectors = await embedder.embed_batch(texts)

    clusterer = HDBSCANClusterer(min_cluster_size=2)
    cluster_result = clusterer.cluster(vectors)

    if not dry_run:
        async with AsyncSessionLocal() as session:
            cluster_db_ids: dict = {}
            for label in sorted(set(l for l in cluster_result.labels if l >= 0)):
                c = Cluster(
                    report_date=run_date,
                    title=f"Cluster {label}",
                    importance_score=0.0,
                    keywords_json=[],
                )
                session.add(c)
                await session.flush()
                cluster_db_ids[label] = c.id

            for idx, (label, (raw_item, _)) in enumerate(zip(cluster_result.labels, combined)):
                if label < 0:
                    continue
                ci = ClusterItem(
                    cluster_id=cluster_db_ids[label],
                    raw_item_id=raw_item.id,
                    similarity_score=0.5,
                )
                session.add(ci)

            await session.commit()

    logger.info("cluster_done", clusters=cluster_result.n_clusters, items=len(combined),
                noise=cluster_result.noise_count)
    return {"clusters": cluster_result.n_clusters, "items": len(combined), "noise": cluster_result.noise_count}


async def run_verify(run_date: date, dry_run: bool, logger) -> dict:
    from app.db import AsyncSessionLocal
    from app.models.db_models import Cluster, ClusterItem, RawItem, Verification
    from app.verification.verifier import SourceVerifier
    from sqlalchemy import select, not_, exists

    verifier = SourceVerifier()

    async with AsyncSessionLocal() as session:
        unverified_clusters = list(await session.scalars(
            select(Cluster)
            .where(Cluster.report_date == run_date)
            .where(not_(exists().where(Verification.cluster_id == Cluster.id)))
        ))

    verified = 0
    for cluster in unverified_clusters:
        async with AsyncSessionLocal() as session:
            source_urls = list(await session.scalars(
                select(RawItem.url)
                .join(ClusterItem, ClusterItem.raw_item_id == RawItem.id)
                .where(ClusterItem.cluster_id == cluster.id)
            ))

        result = await verifier.verify(
            cluster_id=str(cluster.id),
            title=cluster.title or "",
            summary="",
            source_urls=source_urls,
        )
        if not dry_run:
            async with AsyncSessionLocal() as session:
                v = Verification(
                    cluster_id=cluster.id,
                    verification_status=result.get("verification_status", "unverified"),
                    trust_score=result.get("trust_score", 0),
                    evidence_summary=result.get("evidence_summary", ""),
                    evidence_json=result.get("confirmed_facts", []),
                )
                session.add(v)
                await session.commit()
        verified += 1

    logger.info("verify_done", verified=verified)
    return {"verified": verified}


async def run_image_analyze(run_date: date, dry_run: bool, logger) -> dict:
    logger.info("image_analyze_step", status="skipped", note="optional step")
    return {}


async def run_generate(run_date: date, dry_run: bool, logger) -> dict:
    from app.db import AsyncSessionLocal
    from app.models.db_models import Cluster, ClusterItem, RawItem, ExtractedContent, Report, ReportSection
    from app.generation.section_generator import SectionGenerator
    from app.generation.title_generator import TitleGenerator
    from app.generation.report_assembler import ReportAssembler
    from sqlalchemy import select

    async with AsyncSessionLocal() as session:
        clusters = list(await session.scalars(
            select(Cluster).where(Cluster.report_date == run_date)
        ))

    if not clusters:
        logger.info("generate_done", sections=0, note="no clusters for today")
        return {"sections": 0}

    section_gen = SectionGenerator()
    sections = []

    for cluster in clusters:
        async with AsyncSessionLocal() as session:
            stmt = (
                select(RawItem, ExtractedContent)
                .join(ClusterItem, ClusterItem.raw_item_id == RawItem.id)
                .outerjoin(ExtractedContent, ExtractedContent.raw_item_id == RawItem.id)
                .where(ClusterItem.cluster_id == cluster.id)
            )
            rows = list(await session.execute(stmt))

        items = [
            {
                "title": ri.title or "",
                "url": ri.url or "",
                "content_text": (ec.content_text if ec else ri.raw_text) or "",
            }
            for ri, ec in rows
        ]

        section = await section_gen.generate(str(cluster.id), items)
        sections.append(section)

    assembler = ReportAssembler()
    title_gen = TitleGenerator()
    sections_summary = " ".join(s.get("summary_ko", "") for s in sections[:5])
    titles = await title_gen.generate_titles(sections_summary)
    title = titles[0] if titles else f"AI 트렌드 리포트 {run_date}"

    report = assembler.assemble(run_date=run_date, title=title, sections=sections)

    if not dry_run:
        async with AsyncSessionLocal() as session:
            db_report = Report(
                report_date=run_date,
                title=title,
                status="draft",
                summary_ko=report.summary_ko,
                stats_json=report.stats,
                method_json={},
            )
            session.add(db_report)
            await session.flush()

            for i, section in enumerate(report.sections):
                rs = ReportSection(
                    report_id=db_report.id,
                    section_order=i,
                    title=section.get("title_ko", ""),
                    fact_summary=section.get("fact_summary"),
                    social_signal_summary=section.get("social_signal_summary"),
                    inference_summary=section.get("inference_summary"),
                    importance_score=section.get("importance_score", 0.0),
                    sources_json=[],
                    image_evidence_json=[],
                    tags_json=[],
                )
                session.add(rs)

            await session.commit()

    logger.info("generate_done", sections=len(sections), title=title)
    return {"sections": len(sections), "title": title}


async def run_render(run_date: date, dry_run: bool, logger) -> dict:
    from app.db import AsyncSessionLocal
    from app.models.db_models import Report, ReportSection
    from app.rendering.jinja_renderer import JinjaRenderer
    from sqlalchemy import select

    renderer = JinjaRenderer()
    report_data = None
    sections_data = []

    async with AsyncSessionLocal() as session:
        db_report = await session.scalar(
            select(Report).where(Report.report_date == run_date)
        )
        if db_report:
            sections_rows = list(await session.scalars(
                select(ReportSection)
                .where(ReportSection.report_id == db_report.id)
                .order_by(ReportSection.section_order)
            ))
            report_data = {
                "title": db_report.title,
                "report_date": str(db_report.report_date),
                "summary_ko": db_report.summary_ko or "",
                "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
                "stats": db_report.stats_json or {},
            }
            sections_data = [
                {
                    "title_ko": rs.title,
                    "summary_ko": rs.fact_summary or "",
                    "fact_summary": rs.fact_summary,
                    "social_signal_summary": rs.social_signal_summary,
                    "inference_summary": rs.inference_summary,
                    "importance_score": rs.importance_score or 0.0,
                    "verification_status": "unverified",
                    "category": "other",
                }
                for rs in sections_rows
            ]

    if not report_data:
        report_data = {
            "title": f"AI 트렌드 리포트 {run_date}",
            "report_date": str(run_date),
            "summary_ko": "오늘의 AI 트렌드 리포트입니다.",
            "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
            "stats": {"total_sources": 0, "ai_relevant": 0, "clusters": 0, "verified": 0},
        }

    output_path = f"public/news/{run_date}-trend.html"
    if not dry_run:
        renderer.render_to_file(report_data, sections_data, output_path)
    else:
        html = renderer.render_report(report_data, sections_data)
        logger.info("render_dry_run", html_length=len(html))

    return {"output_path": output_path}


async def run_publish(run_date: date, dry_run: bool, logger) -> dict:
    logger.info("publish_step", status="not_implemented_yet")
    return {}


async def run_notify(run_date: date, dry_run: bool, logger) -> dict:
    logger.info("notify_step", status="not_implemented_yet")
    return {}


STEP_FUNCTIONS = {
    "collect": run_collect,
    "extract": run_extract,
    "classify": run_classify,
    "cluster": run_cluster,
    "verify": run_verify,
    "image_analyze": run_image_analyze,
    "generate": run_generate,
    "render": run_render,
    "publish": run_publish,
    "notify": run_notify,
}


async def run_pipeline(
    run_date: date,
    mode: str,
    from_step: str,
    to_step: str,
    dry_run: bool,
) -> None:
    logger = get_logger(step="pipeline")
    logger.info("pipeline_start", date=str(run_date), mode=mode, from_step=from_step,
                to_step=to_step, dry_run=dry_run)

    from_idx = STEPS.index(from_step)
    to_idx = STEPS.index(to_step)
    steps_to_run = STEPS[from_idx:to_idx + 1]

    if mode == "rss-only":
        steps_to_run = [s for s in steps_to_run if s in ("collect", "render")]

    results = {}
    for step in steps_to_run:
        logger.info("step_start", step=step)
        try:
            fn = STEP_FUNCTIONS[step]
            kwargs: dict = {}
            if step == "collect" and mode == "rss-only":
                kwargs["source_types"] = ["rss", "arxiv"]
            result = await fn(run_date, dry_run, logger, **kwargs)
            results[step] = result
            logger.info("step_done", step=step, **{k: v for k, v in result.items()
                                                    if isinstance(v, (int, float, str))})
        except Exception as e:
            logger.error("step_failed", step=step, error=str(e))
            if step == "collect":
                raise
            # other steps: log and continue

    logger.info("pipeline_done", steps_run=len(steps_to_run))


@click.command()
@click.option("--date", "run_date_str", default=None, help="YYYY-MM-DD, default=today")
@click.option(
    "--mode",
    default="full",
    type=click.Choice(["full", "rss-only", "dry-run"]),
    help="Pipeline mode",
)
@click.option("--from-step", default="collect", type=click.Choice(STEPS))
@click.option("--to-step", default="notify", type=click.Choice(STEPS))
@click.option("--dry-run", is_flag=True, default=False, help="Skip DB writes, log only")
def main(run_date_str, mode, from_step, to_step, dry_run):
    """Run the daily AI trend report pipeline."""
    if run_date_str:
        run_date = date.fromisoformat(run_date_str)
    else:
        run_date = date.today()

    if mode == "dry-run":
        dry_run = True

    asyncio.run(run_pipeline(run_date, mode, from_step, to_step, dry_run))


if __name__ == "__main__":
    main()
