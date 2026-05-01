#!/usr/bin/env python3
"""Daily AI trend report pipeline entrypoint."""
from __future__ import annotations
import asyncio
import os
from datetime import date, datetime, timezone
import click
from app.editorial.policy import POLICY_PATH_ENV
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


def _json_dict(value) -> dict:
    return value if isinstance(value, dict) else {}


def _fallback_extract_result_from_raw_item(raw_item, error: str | None = None):
    """Build a low-quality extraction result from already collected text.

    Some official sites (notably OpenAI) can return Cloudflare challenge pages to
    non-browser HTTP extractors. When the collector already captured an official
    RSS summary/raw text, storing that text prevents repeated failed extraction
    attempts and keeps downstream steps on the ExtractedContent path.
    """
    from app.extractors.base import ExtractResult

    content = (getattr(raw_item, "raw_text", None) or "").strip()
    if not content:
        return None

    source_type = str(getattr(raw_item, "source_type", "") or "")
    extractor = "rss_summary_fallback" if source_type == "rss" else "raw_text_fallback"
    quality = min(0.35, len(content) / 2000)

    return ExtractResult(
        raw_item_id=str(getattr(raw_item, "id", "") or ""),
        extractor=extractor,
        status="low_quality",
        title=getattr(raw_item, "title", None),
        description=content,
        content_markdown=content,
        content_text=content,
        quality_score=quality,
        error=error,
    )


def _extract_result_metadata(result) -> dict:
    metadata = {}
    if result.og_image_url:
        metadata["og_image_url"] = result.og_image_url
    if result.content_image_urls:
        metadata["content_image_urls"] = result.content_image_urls
    if result.error:
        metadata["extract_error"] = result.error
    if str(result.extractor).endswith("_fallback"):
        metadata["fallback"] = True
        metadata["fallback_source"] = "raw_item.raw_text"
    return metadata


def _is_access_blocked_error(error: str | None) -> bool:
    lower = str(error or "").lower()
    return any(
        token in lower
        for token in (
            "403",
            "forbidden",
            "cloudflare",
            "challenge",
            "enable javascript and cookies",
        )
    )


def _registry_source_url(source: dict) -> str:
    source_type = source.get("source_type", "")
    if source_type == "rss" and source.get("url"):
        return source["url"]
    if source_type == "github" and source.get("org"):
        return f"https://github.com/{source['org']}"
    if source_type == "arxiv" and source.get("category"):
        return f"https://arxiv.org/list/{source['category']}/recent"
    if source.get("url"):
        return source["url"]
    return f"registry://{source.get('name', 'unknown-source').replace(' ', '-')}"


def _registry_homepage_url(source: dict) -> str:
    from urllib.parse import urlparse

    if source.get("homepage_url"):
        return source["homepage_url"]
    if source.get("source_type") == "github" and source.get("org"):
        return f"https://github.com/{source['org']}"
    if source.get("source_type") == "arxiv":
        return "https://arxiv.org"
    if source.get("url"):
        parsed = urlparse(source["url"])
        if parsed.scheme and parsed.netloc:
            return f"{parsed.scheme}://{parsed.netloc}"
    return ""


def _source_raw_json(item_raw_json: dict, source_db) -> dict:
    raw_json = dict(item_raw_json or {})
    if source_db:
        metadata = _json_dict(source_db.metadata_json)
        raw_json.setdefault("source_name", source_db.name)
        raw_json.setdefault("source_trust_level", source_db.trust_level)
        raw_json.setdefault("source_tier", metadata.get("source_tier", ""))
        raw_json.setdefault("source_priority", metadata.get("priority", 0))
        raw_json.setdefault("source_category", metadata.get("source_category", ""))
    return raw_json


def _source_dict_for_editorial(source_db, raw_item=None) -> dict:
    raw_json = _json_dict(getattr(raw_item, "raw_json", None))
    metadata = _json_dict(getattr(source_db, "metadata_json", None))
    if not source_db:
        return {
            "name": raw_json.get("source_name", ""),
            "source_type": getattr(raw_item, "source_type", ""),
            "trust_level": raw_json.get("source_trust_level", ""),
            "source_tier": raw_json.get("source_tier", ""),
            "priority": raw_json.get("source_priority", 0),
        }
    return {
        "name": source_db.name,
        "source_type": source_db.source_type,
        "trust_level": source_db.trust_level,
        "source_tier": metadata.get("source_tier") or raw_json.get("source_tier", ""),
        "priority": metadata.get("priority") or raw_json.get("source_priority", 0),
        "category": metadata.get("source_category") or metadata.get("category", ""),
    }


def _youtube_video_id_from_url(url: str) -> str:
    from urllib.parse import parse_qs, urlparse

    parsed = urlparse(url or "")
    host = parsed.netloc.lower()
    if "youtube.com" in host:
        return parse_qs(parsed.query).get("v", [""])[0]
    if "youtu.be" in host:
        return parsed.path.strip("/").split("/", 1)[0]
    return ""


def _raw_item_run_date_filter(RawItem, run_date: date):
    """Filter raw items to the configured local report date.

    Prefer published_at. For sources without a parsable publication date, use
    collected_at so newly discovered mainstream/news items still enter the run.
    """
    from app.pipeline.date_window import local_day_window_utc
    from sqlalchemy import and_, or_

    date_from, date_to = local_day_window_utc(run_date)
    return or_(
        RawItem.published_at.between(date_from, date_to),
        and_(
            RawItem.published_at.is_(None),
            RawItem.collected_at.between(date_from, date_to),
        ),
    )


def _cluster_editorial_summary(items: list[dict]) -> dict:
    ranks = [item.get("editorial", {}) for item in items if item.get("editorial")]
    if not ranks:
        return {
            "editorial_score": 0.0,
            "topic_type": "industry",
            "eligible_for_main": False,
            "rejected": True,
            "rejection_reason": "no_ranked_items",
            "source_tiers": [],
            "arxiv_only": False,
        }

    usable = [rank for rank in ranks if not rank.get("rejected")]
    best = max(ranks, key=lambda rank: rank.get("editorial_score", 0.0))
    source_tiers = sorted({rank.get("source_tier", "unknown") for rank in ranks})
    arxiv_only = bool(source_tiers) and set(source_tiers) <= {"research"}

    return {
        "editorial_score": best.get("editorial_score", 0.0),
        "topic_type": best.get("topic_type", "industry"),
        "eligible_for_main": any(rank.get("eligible_for_main") for rank in ranks),
        "rejected": not usable,
        "rejection_reason": "all_items_rejected" if not usable else None,
        "source_tiers": source_tiers,
        "arxiv_only": arxiv_only,
        "best_item": best,
    }


def _select_editorial_clusters(candidates: list[dict], policy: dict) -> list[dict]:
    selection_cfg = policy.get("report_selection", {})
    quotas = policy.get("section_quotas", {})
    max_sections = int(selection_cfg.get("max_sections", 6))
    min_score = float(selection_cfg.get("min_section_score", 35))
    max_arxiv_only = int(selection_cfg.get("max_arxiv_only_sections", 1))

    selected: list[dict] = []
    topic_counts: dict[str, int] = {}
    arxiv_only_count = 0

    def _sort_key(candidate: dict) -> tuple[int, float]:
        editorial = candidate["editorial"]
        return (
            1 if editorial.get("eligible_for_main") else 0,
            float(editorial.get("editorial_score", 0.0)),
        )

    for candidate in sorted(candidates, key=_sort_key, reverse=True):
        editorial = candidate["editorial"]
        topic = editorial.get("topic_type", "industry")
        score = float(editorial.get("editorial_score", 0.0))

        if editorial.get("rejected") or score < min_score:
            continue
        if topic_counts.get(topic, 0) >= int(quotas.get(topic, max_sections)):
            continue
        if editorial.get("arxiv_only"):
            if arxiv_only_count >= max_arxiv_only:
                continue
            arxiv_only_count += 1

        selected.append(candidate)
        topic_counts[topic] = topic_counts.get(topic, 0) + 1
        if len(selected) >= max_sections:
            break

    return selected


async def run_collect(run_date: date, dry_run: bool, logger, source_types=None) -> dict:
    from collections import Counter
    from app.collectors.orchestrator import CollectorOrchestrator
    from app.db import AsyncSessionLocal
    from app.models.db_models import RawItem, Source
    from sqlalchemy import select

    orchestrator = CollectorOrchestrator()
    items = await orchestrator.collect_items(run_date, source_types=source_types)
    registry_sources = orchestrator._load_registry()
    if source_types:
        registry_sources = [
            source for source in registry_sources
            if source.get("source_type") in source_types
        ]

    total = len(items)
    inserted = 0
    skipped = 0
    source_counts = Counter(item.source_id for item in items)
    registry_by_name = {source.get("name", ""): source for source in registry_sources}
    source_tier_counts = Counter(
        registry_by_name.get(source_name, {}).get("source_tier", "unknown")
        for source_name in source_counts
    )
    image_items = sum(
        1
        for item in items
        if _json_dict(item.raw_json).get("image_url")
    )
    community_items = sum(
        count
        for source_name, count in source_counts.items()
        if registry_by_name.get(source_name, {}).get("source_tier") == "community"
    )
    logger.info(
        "collect_source_summary",
        sources_seen=len(source_counts),
        image_items=image_items,
        community_items=community_items,
        top_sources=[
            {"source": source_name, "count": count}
            for source_name, count in source_counts.most_common(10)
        ],
        source_tiers=dict(source_tier_counts),
    )

    if dry_run:
        logger.info("dry_run_collect", total=total)
    else:
        async with AsyncSessionLocal() as session:
            source_by_name = {}
            for source in registry_sources:
                source_url = _registry_source_url(source)
                source_db = await session.scalar(
                    select(Source).where(Source.url == source_url)
                )
                metadata_json = {
                    "registry_name": source.get("name", ""),
                    "source_type": source.get("source_type", ""),
                    "collector_type": source.get("collector_type", source.get("source_type", "")),
                    "org": source.get("org", ""),
                    "query": source.get("query", ""),
                    "category": source.get("category", ""),
                    "source_category": source.get("content_category") or source.get("category", ""),
                    "source_tier": source.get("source_tier", ""),
                    "priority": source.get("priority", 0),
                    "max_items": source.get("max_items", 0),
                }
                if source_db:
                    source_db.name = source.get("name", source_url)
                    source_db.source_type = source.get("source_type", "website")
                    source_db.homepage_url = _registry_homepage_url(source)
                    source_db.trust_level = source.get("trust_level", "unknown")
                    source_db.enabled = True
                    source_db.metadata_json = metadata_json
                    source_db.updated_at = datetime.now(timezone.utc)
                else:
                    source_db = Source(
                        name=source.get("name", source_url),
                        source_type=source.get("source_type", "website"),
                        url=source_url,
                        homepage_url=_registry_homepage_url(source),
                        trust_level=source.get("trust_level", "unknown"),
                        enabled=True,
                        metadata_json=metadata_json,
                    )
                    session.add(source_db)
                    await session.flush()
                source_by_name[source_db.name] = source_db

            for item in items:
                source_db = source_by_name.get(item.source_id)
                raw_json = _source_raw_json(item.raw_json or {}, source_db)
                existing = await session.scalar(
                    select(RawItem).where(RawItem.canonical_url_hash == item.canonical_url_hash)
                )
                if existing:
                    existing_raw_json = _json_dict(existing.raw_json).copy()
                    for key, value in raw_json.items():
                        if value and not existing_raw_json.get(key):
                            existing_raw_json[key] = value
                    existing.raw_json = existing_raw_json
                    if source_db and not existing.source_id:
                        existing.source_id = source_db.id
                    skipped += 1
                    continue
                db_item = RawItem(
                    source_id=source_db.id if source_db else None,
                    source_type=item.source_type,
                    title=item.title,
                    url=item.url,
                    canonical_url=item.canonical_url,
                    canonical_url_hash=item.canonical_url_hash,
                    raw_text=item.raw_text,
                    author=item.author,
                    published_at=item.published_at,
                    metrics_json=item.metrics_json or {},
                    raw_json=raw_json,
                )
                session.add(db_item)
                inserted += 1
            await session.commit()

    logger.info(
        "collect_done",
        total=total,
        inserted=inserted,
        skipped=skipped,
        sources_seen=len(source_counts),
        image_items=image_items,
        community_items=community_items,
    )
    return {
        "total": total,
        "inserted": inserted,
        "skipped": skipped,
        "sources_seen": len(source_counts),
        "image_items": image_items,
        "community_items": community_items,
    }


async def run_extract(run_date: date, dry_run: bool, logger) -> dict:
    from app.db import AsyncSessionLocal
    from app.models.db_models import RawItem, ExtractedContent
    from app.extractors.orchestrator import ExtractorOrchestrator
    from app.extractors.base import (
        ExtractorUnavailableError,
        ExtractorError,
        SSRFBlockedError,
    )
    from sqlalchemy import select, not_, exists

    extractor = ExtractorOrchestrator()

    async with AsyncSessionLocal() as session:
        stmt = select(RawItem).where(
            _raw_item_run_date_filter(RawItem, run_date),
            not_(exists().where(ExtractedContent.raw_item_id == RawItem.id))
        )
        raw_items = list(await session.scalars(stmt))

    extracted = 0
    failed = 0
    fallback = 0

    for raw_item in raw_items:
        result = None
        try:
            result = await extractor.extract(raw_item.url, str(raw_item.id))
            if result.status == "failed":
                result = _fallback_extract_result_from_raw_item(
                    raw_item,
                    error=result.error,
                )
                if result:
                    fallback += 1
                    logger.warning(
                        "extract_fallback_used",
                        url=raw_item.url,
                        extractor=result.extractor,
                        reason=result.error,
                    )
        except SSRFBlockedError as e:
            logger.error("extract_failed", url=raw_item.url, error=str(e))
            failed += 1
            continue
        except (ExtractorUnavailableError, ExtractorError) as e:
            result = _fallback_extract_result_from_raw_item(raw_item, error=str(e))
            if result:
                fallback += 1
                logger.warning(
                    "extract_fallback_used",
                    url=raw_item.url,
                    extractor=result.extractor,
                    reason=str(e),
                )
            else:
                logger.error("extract_failed", url=raw_item.url, error=str(e))
                failed += 1
                continue
        except Exception as e:
            result = _fallback_extract_result_from_raw_item(raw_item, error=str(e))
            if result:
                fallback += 1
                logger.warning(
                    "extract_fallback_used",
                    url=raw_item.url,
                    extractor=result.extractor,
                    reason=str(e),
                )
            else:
                logger.error("extract_error", url=raw_item.url, error=str(e))
                failed += 1
                continue

        if not result:
            logger.error(
                "extract_failed",
                url=raw_item.url,
                error="all extractors failed and no raw_text fallback is available",
            )
            failed += 1
            continue

        if not dry_run:
            async with AsyncSessionLocal() as session:
                ec = ExtractedContent(
                    raw_item_id=raw_item.id,
                    extractor=result.extractor,
                    extraction_status=result.status,
                    title=result.title,
                    description=result.description,
                    content_text=result.content_text,
                    content_markdown=result.content_markdown,
                    quality_score=result.quality_score,
                    metadata_json=_extract_result_metadata(result),
                )
                session.add(ec)
                await session.commit()
        extracted += 1

    logger.info("extract_done", extracted=extracted, failed=failed, fallback=fallback)
    return {"extracted": extracted, "failed": failed, "fallback": fallback}


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
            .where(_raw_item_run_date_filter(RawItem, run_date))
            .where(not_(exists().where(AnalysisResult.raw_item_id == RawItem.id)))
        )
        rows = list(await session.execute(stmt))
        # Items without extracted content — fall back to raw_text
        stmt2 = (
            select(RawItem)
            .where(_raw_item_run_date_filter(RawItem, run_date))
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
    from sqlalchemy import delete, select, not_, exists

    async with AsyncSessionLocal() as session:
        # AI-relevant items with extracted content
        stmt = (
            select(RawItem, ExtractedContent)
            .join(AnalysisResult, AnalysisResult.raw_item_id == RawItem.id)
            .join(ExtractedContent, ExtractedContent.raw_item_id == RawItem.id)
            .where(_raw_item_run_date_filter(RawItem, run_date))
            .where(AnalysisResult.is_ai_related == True)  # noqa: E712
        )
        rows = list(await session.execute(stmt))
        # AI-relevant items without extracted content — use raw_text fallback
        stmt2 = (
            select(RawItem)
            .join(AnalysisResult, AnalysisResult.raw_item_id == RawItem.id)
            .where(_raw_item_run_date_filter(RawItem, run_date))
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
            await session.execute(delete(Cluster).where(Cluster.report_date == run_date))
            await session.flush()

            cluster_db_ids: dict = {}
            for label in sorted(set(cluster_label for cluster_label in cluster_result.labels if cluster_label >= 0)):
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
    from app.models.db_models import (
        Cluster,
        ClusterItem,
        ExtractedContent,
        RawItem,
        Report,
        ReportSection,
        Source,
    )
    from app.config import settings
    from app.editorial.policy import load_policy
    from app.editorial.ranker import EditorialRanker
    from app.editorial.selection import (
        select_editorial_clusters,
        summarize_cluster_editorial,
    )
    from app.generation.section_generator import SectionGenerator
    from app.generation.title_generator import TitleGenerator
    from app.generation.report_assembler import ReportAssembler
    from app.utils.generated_images import create_section_fallback_svg
    from app.utils.source_images import (
        fetch_representative_image_url,
        is_usable_representative_image_url,
    )
    from sqlalchemy import delete, select, update

    async with AsyncSessionLocal() as session:
        clusters = list(await session.scalars(
            select(Cluster).where(Cluster.report_date == run_date)
        ))

    if not clusters:
        logger.info("generate_done", sections=0, note="no clusters for today")
        return {"sections": 0}

    editorial_policy = load_policy()
    editorial_ranker = EditorialRanker(editorial_policy)
    section_gen = SectionGenerator()
    cluster_candidates = []
    sections_with_cluster = []

    for cluster in clusters:
        async with AsyncSessionLocal() as session:
            stmt = (
                select(RawItem, ExtractedContent, Source)
                .join(ClusterItem, ClusterItem.raw_item_id == RawItem.id)
                .outerjoin(ExtractedContent, ExtractedContent.raw_item_id == RawItem.id)
                .outerjoin(Source, Source.id == RawItem.source_id)
                .where(ClusterItem.cluster_id == cluster.id)
            )
            rows = list(await session.execute(stmt))

        items = []
        for ri, ec, source_db in rows:
            ec_metadata = _json_dict(ec.metadata_json if ec else {})
            raw_json = _json_dict(ri.raw_json)
            content_image_candidates = ec_metadata.get("content_image_urls", [])
            if not isinstance(content_image_candidates, list):
                content_image_candidates = []
            image_candidates = (
                ec_metadata.get("og_image_url"),
                *content_image_candidates,
                raw_json.get("image_url"),  # RSS/YouTube/Reddit thumbnail fallback
            )
            image_url = next(
                (
                    url for url in image_candidates
                    if is_usable_representative_image_url(url)
                    and "youtube.com/v/" not in url  # skip YouTube embed URLs
                ),
                "",
            )
            image_fetch_blocked = _is_access_blocked_error(
                ec_metadata.get("extract_error")
            )
            if not image_url and ri.url and not image_fetch_blocked:
                try:
                    image_url = await asyncio.to_thread(
                        fetch_representative_image_url,
                        ri.url,
                    )
                except Exception as exc:
                    logger.warning(
                        "representative_image_fetch_failed",
                        url=ri.url,
                        error=str(exc),
                    )

            source_name = (
                source_db.name
                if source_db
                else raw_json.get("source_name", "")
            )
            source_trust_level = (
                source_db.trust_level
                if source_db
                else raw_json.get("source_trust_level", "")
            )
            source_for_editorial = _source_dict_for_editorial(source_db, ri)
            editorial_item = {
                "source_id": source_name or raw_json.get("source_name", ""),
                "source_type": ri.source_type,
                "title": ri.title or "",
                "url": ri.url or "",
                "canonical_url": ri.canonical_url or "",
                "raw_text": ri.raw_text or "",
                "metrics_json": ri.metrics_json or {},
                "raw_json": raw_json,
                "image_url": image_url,
            }
            editorial = editorial_ranker.rank(editorial_item, source=source_for_editorial)

            items.append(
                {
                    "title": ri.title or "",
                    "url": ri.url or "",
                    "content_text": (ec.content_text if ec else ri.raw_text) or "",
                    "og_image_url": image_url,
                    "content_image_urls": content_image_candidates,
                    "source_name": source_name,
                    "source_trust_level": source_trust_level,
                    "video_id": raw_json.get("video_id") or _youtube_video_id_from_url(ri.url or ""),
                    "editorial": editorial,
                }
            )

        editorial_summary = summarize_cluster_editorial(items, policy=editorial_policy)
        cluster_candidates.append(
            {
                "cluster": cluster,
                "items": items,
                "editorial": editorial_summary,
            }
        )

    selected_candidates = select_editorial_clusters(cluster_candidates, editorial_policy)

    for candidate in selected_candidates:
        cluster = candidate["cluster"]
        items = candidate["items"]
        editorial_summary = candidate["editorial"]
        section = await section_gen.generate(str(cluster.id), items)

        # 출처 목록
        sources = [
            {
                "url": it["url"],
                "name": (
                    f"{it['source_name']}: {it['title']}"
                    if it.get("source_name") and it.get("title")
                    else it.get("title") or it.get("source_name") or it["url"]
                ),
                "source_name": it.get("source_name", ""),
                "trust_level": it.get("source_trust_level", ""),
                "video_id": it.get("video_id", ""),
            }
            for it in items if it["url"]
        ]

        # 본문 콘텐츠 이미지 수집 — UI 요소·로고·기자 초상 제외
        _CONTENT_IMG_SKIP = (
            "arxiv.org/html/",     # arXiv 논문 내부 figure: 섹션 주제와 맥락 없이 배치됨
            "redditstatic.com",    # Reddit UI 자산
            "styles.redditmedia.com",
        )
        content_image_urls: list[str] = []
        seen_imgs: set[str] = set()
        for it in items:
            for img_url in it.get("content_image_urls", []):
                if any(skip in img_url for skip in _CONTENT_IMG_SKIP):
                    continue
                if not is_usable_representative_image_url(img_url):
                    continue  # 기자 초상·로고 등 is_usable 필터 통과 못한 이미지 제외
                if img_url not in seen_imgs:
                    seen_imgs.add(img_url)
                    content_image_urls.append(img_url)
                if len(content_image_urls) >= 5:
                    break

        # OG/썸네일 이미지 폴백 — arXiv 로고·YouTube embed URL 제외
        _OG_IMG_SKIP = (
            "arxiv.org/static",
            "youtube.com/v/",         # YouTube embed (not a real image)
            "redditstatic.com",
        )
        og_image_url = next(
            (it["og_image_url"] for it in items
             if it.get("og_image_url")
             and is_usable_representative_image_url(it["og_image_url"])
             and not any(s in it["og_image_url"] for s in _OG_IMG_SKIP)),
            "",
        )
        image_source = "content" if content_image_urls else ("source" if og_image_url else "")

        if not content_image_urls and not og_image_url and settings.generated_image_fallback_enabled:
            og_image_url = create_section_fallback_svg(
                run_date=run_date,
                cluster_id=str(cluster.id),
                title=section.get("title_ko") or cluster.title or "AI Trend",
                summary=section.get("fact_summary") or section.get("summary_ko", ""),
            )
            image_source = "generated_svg"

        section["sources_json"] = sources
        section["content_image_urls"] = content_image_urls
        section["og_image_url"] = og_image_url if not content_image_urls else ""
        section["image_source"] = image_source
        section["editorial_json"] = editorial_summary
        section["importance_score"] = max(
            float(section.get("importance_score") or 0.0),
            float(editorial_summary.get("editorial_score", 0.0)) / 100.0,
        )
        sections_with_cluster.append((section, cluster))

    sections = [s for s, _ in sections_with_cluster]

    assembler = ReportAssembler()
    title_gen = TitleGenerator()
    sections_summary = " ".join(s.get("summary_ko", "") for s in sections[:5])
    if sections_summary:
        titles = await title_gen.generate_titles(sections_summary)
        title = titles[0] if titles else f"AI 트렌드 리포트 {run_date}"
    else:
        title = f"AI 트렌드 리포트 {run_date}: 주요 대형 뉴스 없음"

    report = assembler.assemble(
        run_date=run_date,
        title=title,
        sections=sections,
        stats={
            "candidate_clusters": len(cluster_candidates),
            "selected_clusters": len(selected_candidates),
            "editorial_filtered": max(0, len(cluster_candidates) - len(selected_candidates)),
        },
    )

    method_json = {
        "editorial_policy": "data/editorial_policy.yaml",
        "report_selection": editorial_policy.get("report_selection", {}),
        "section_quotas": editorial_policy.get("section_quotas", {}),
    }

    if not dry_run:
        async with AsyncSessionLocal() as session:
            db_report = await session.scalar(
                select(Report).where(Report.report_date == run_date)
            )
            if db_report:
                db_report.title = title
                db_report.status = "draft"
                db_report.summary_ko = report.summary_ko
                db_report.stats_json = report.stats
                db_report.method_json = method_json
                db_report.updated_at = datetime.now(timezone.utc)
                await session.execute(
                    delete(ReportSection).where(ReportSection.report_id == db_report.id)
                )
            else:
                db_report = Report(
                    report_date=run_date,
                    title=title,
                    status="draft",
                    summary_ko=report.summary_ko,
                    stats_json=report.stats,
                    method_json=method_json,
                )
                session.add(db_report)
            await session.flush()

            for i, (section, cluster) in enumerate(sections_with_cluster):
                section_title = section.get("title_ko", "")
                image_evidence = [
                    {"url": u, "source": "content"}
                    for u in section.get("content_image_urls", [])
                ]
                if not image_evidence and section.get("og_image_url"):
                    image_evidence = [
                        {
                            "url": section["og_image_url"],
                            "source": section.get("image_source") or "source",
                        }
                    ]
                rs = ReportSection(
                    report_id=db_report.id,
                    cluster_id=cluster.id,           # ← 클러스터 연결 기록
                    section_order=i,
                    title=section_title,
                    fact_summary=section.get("fact_summary"),
                    social_signal_summary=section.get("social_signal_summary"),
                    inference_summary=section.get("inference_summary"),
                    importance_score=section.get("importance_score", 0.0),
                    sources_json=section.get("sources_json", []),
                    image_evidence_json=image_evidence,
                    tags_json=[{"editorial": section.get("editorial_json", {})}],
                )
                session.add(rs)
                # 클러스터 제목도 LLM이 생성한 제목으로 갱신
                await session.execute(
                    update(Cluster)
                    .where(Cluster.id == cluster.id)
                    .values(title=section_title)
                )

            await session.commit()

    logger.info("generate_done", sections=len(sections), title=title)
    return {"sections": len(sections), "title": title}


async def run_render(
    run_date: date,
    dry_run: bool,
    logger,
    output_theme: str | None = None,
) -> dict:
    from app.db import AsyncSessionLocal
    from app.models.db_models import Report, ReportSection, Verification, RawItem, AnalysisResult
    from app.rendering.jinja_renderer import JinjaRenderer
    from app.utils.source_images import is_usable_representative_image_url
    from sqlalchemy import select, func

    renderer = JinjaRenderer()
    report_data = None
    sections_data = []
    theme_value = output_theme or "dark"

    def _is_allowed_render_image(evidence: dict) -> bool:
        image_url = evidence.get("url", "")
        if not image_url:
            return False
        if evidence.get("source") == "generated_svg":
            return image_url.startswith("../assets/generated/") and image_url.endswith(".svg")
        return is_usable_representative_image_url(image_url)

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

            # 클러스터별 검증 상태를 한 번에 조회
            cluster_ids = [rs.cluster_id for rs in sections_rows if rs.cluster_id]
            verif_map: dict = {}
            if cluster_ids:
                verif_rows = list(await session.scalars(
                    select(Verification).where(Verification.cluster_id.in_(cluster_ids))
                ))
                verif_map = {str(v.cluster_id): v.verification_status for v in verif_rows}

            # 실제 수집·분류 통계를 DB에서 조회
            total_sources = await session.scalar(select(func.count(RawItem.id))) or 0
            ai_relevant = await session.scalar(
                select(func.count(AnalysisResult.id))
                .where(AnalysisResult.is_ai_related == True)  # noqa: E712
            ) or 0
            verified_count = len(verif_map)

            report_data = {
                "title": db_report.title,
                "report_date": str(db_report.report_date),
                "summary_ko": db_report.summary_ko or "",
                "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
                "stats": {
                    "total_sources": total_sources,
                    "ai_relevant": ai_relevant,
                    "clusters": len(sections_rows),
                    "verified": verified_count,
                },
            }
            sections_data = []
            for rs in sections_rows:
                image_evidence = rs.image_evidence_json or []
                content_images = [
                    e["url"]
                    for e in image_evidence
                    if e.get("url") and e.get("source") == "content"
                    and _is_allowed_render_image(e)
                ]
                fallback_image = next(
                    (
                        e["url"]
                        for e in image_evidence
                        if e.get("url") and e.get("source") != "content"
                        and _is_allowed_render_image(e)
                    ),
                    "",
                )
                sections_data.append(
                    {
                        "title": rs.title or "",
                        "summary_ko": rs.fact_summary or "",
                        "fact_summary": rs.fact_summary,
                        "social_signal_summary": rs.social_signal_summary,
                        "inference_summary": rs.inference_summary,
                        "importance_score": rs.importance_score or 0.0,
                        "verification_status": verif_map.get(str(rs.cluster_id), "unverified"),
                        "sources_json": rs.sources_json or [],
                        "content_image_urls": content_images,
                        "og_image_url": fallback_image,
                        "category": "other",
                    }
                )

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
        renderer.render_to_file(
            report_data, sections_data, output_path, output_theme=theme_value
        )
    else:
        html = renderer.render_report(
            report_data, sections_data, output_theme=theme_value
        )
        logger.info("render_dry_run", html_length=len(html))

    return {"output_path": output_path, "output_theme": theme_value}


async def run_publish(run_date: date, dry_run: bool, logger) -> dict:
    from pathlib import Path
    import hashlib
    from app.config import settings
    from app.deployment.static_publisher import StaticPublisher
    from app.deployment.netlify import NetlifyPublisher
    from app.db import AsyncSessionLocal
    from app.models.db_models import Report, ReportArtifact
    from sqlalchemy import select

    html_path = Path(f"public/news/{run_date}-trend.html")
    if not html_path.exists():
        logger.warning("publish_skipped", reason="html_not_found", path=str(html_path))
        return {"status": "skipped"}

    html_content = html_path.read_text(encoding="utf-8")
    public_url = f"{settings.report_public_base_url}/news/{run_date}-trend.html"

    if not dry_run:
        # index.html 리다이렉트 업데이트
        publisher = StaticPublisher()
        publisher._update_index(str(run_date))

        # DB에 아티팩트 기록 + 리포트 상태 published로 변경
        async with AsyncSessionLocal() as session:
            db_report = await session.scalar(select(Report).where(Report.report_date == run_date))
            if db_report:
                artifact = ReportArtifact(
                    report_id=db_report.id,
                    artifact_type="html",
                    storage_path=str(html_path),
                    public_url=public_url,
                    sha256=hashlib.sha256(html_content.encode()).hexdigest(),
                )
                session.add(artifact)
                db_report.status = "published"
                db_report.published_at = datetime.now(timezone.utc)
                db_report.updated_at = datetime.now(timezone.utc)
                await session.commit()

        # Netlify 자격증명이 있으면 배포
        if settings.netlify_auth_token and settings.netlify_site_id:
            netlify = NetlifyPublisher(
                site_id=settings.netlify_site_id,
                auth_token=settings.netlify_auth_token,
            )
            deploy_result = await netlify.deploy("public")
            logger.info("netlify_deploy", **{k: str(v)[:100] for k, v in deploy_result.items()})
            return {"status": "published", "netlify": deploy_result.get("status"), "public_url": public_url}

    logger.info("publish_done", path=str(html_path), url=public_url)
    return {"status": "published", "public_url": public_url}


async def run_notify(run_date: date, dry_run: bool, logger) -> dict:
    from app.utils.notifier import Notifier
    from app.config import settings
    from app.db import AsyncSessionLocal
    from app.models.db_models import Report
    from sqlalchemy import select

    if dry_run:
        logger.info("notify_dry_run")
        return {}

    async with AsyncSessionLocal() as session:
        db_report = await session.scalar(select(Report).where(Report.report_date == run_date))
        stats = db_report.stats_json if db_report else {}

    public_url = f"{settings.report_public_base_url}/news/{run_date}-trend.html"
    notifier = Notifier()
    sent = await notifier.notify_report_ready(
        run_date=str(run_date),
        report_url=public_url,
        stats=stats,
    )
    logger.info("notify_done", sent=sent, url=public_url)
    return {"sent": sent, "url": public_url}


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

LLM_REQUIRED_STEPS = {"classify", "verify", "generate"}


def _local_proxy_health_url(openai_base_url: str) -> str | None:
    from urllib.parse import urlparse

    parsed = urlparse(openai_base_url)
    if parsed.hostname not in {"127.0.0.1", "localhost"}:
        return None
    if parsed.port != 4317:
        return None
    return f"{parsed.scheme}://{parsed.netloc}/api/v1/health"


async def run_llm_preflight(steps_to_run: list[str], logger) -> None:
    """Fail fast when the automatic pipeline is configured for the local GPT-5.5 proxy."""
    if not any(step in LLM_REQUIRED_STEPS for step in steps_to_run):
        return

    from app.config import settings
    import httpx

    health_url = _local_proxy_health_url(settings.openai_base_url)
    logger.info(
        "llm_runtime_config",
        openai_base_url=settings.openai_base_url,
        openai_model=settings.openai_model,
        openai_embedding_model=settings.openai_embedding_model,
        proxy_health_url=health_url or "",
    )

    if not health_url:
        return

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(health_url)
            response.raise_for_status()
            payload = response.json()
        if payload.get("ok") is not True:
            raise RuntimeError(f"unexpected health payload: {payload}")
    except Exception as e:
        raise RuntimeError(
            "GPT-5.5 local proxy is configured but unavailable. "
            "Start the proxy at http://127.0.0.1:4317 or override OPENAI_BASE_URL."
        ) from e

    logger.info("llm_proxy_ready", health_url=health_url)


async def run_pipeline(
    run_date: date,
    mode: str,
    from_step: str,
    to_step: str,
    dry_run: bool,
    output_theme: str | None = None,
) -> None:
    logger = get_logger(step="pipeline")
    logger.info("pipeline_start", date=str(run_date), mode=mode, from_step=from_step,
                to_step=to_step, dry_run=dry_run, output_theme=output_theme or "dark")

    from_idx = STEPS.index(from_step)
    to_idx = STEPS.index(to_step)
    steps_to_run = STEPS[from_idx:to_idx + 1]

    if mode == "rss-only":
        steps_to_run = [s for s in steps_to_run if s in ("collect", "render")]

    await run_llm_preflight(steps_to_run, logger)

    results = {}
    for step in steps_to_run:
        logger.info("step_start", step=step)
        try:
            fn = STEP_FUNCTIONS[step]
            kwargs: dict = {}
            if step == "collect" and mode == "rss-only":
                kwargs["source_types"] = ["rss", "website", "arxiv"]
            if step == "render":
                kwargs["output_theme"] = output_theme
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
@click.option(
    "--policy-path",
    default=None,
    help=(
        "Path to a yaml editorial policy. Equivalent to setting "
        "$EDITORIAL_POLICY_PATH — handy when launching ad-hoc runs with a "
        "tuned policy without touching data/editorial_policy.yaml."
    ),
)
@click.option(
    "--policy-override-json",
    default=None,
    help=(
        "JSON string with deep-merge policy overrides. Exported as "
        "$EDITORIAL_POLICY_OVERRIDE_JSON so ``app.editorial.policy.load_policy`` "
        "deep-merges it on top of the resolved YAML policy. Used by the API "
        "subprocess flow to forward per-run editorial knobs without writing "
        "a tempfile when the override is purely additive."
    ),
)
@click.option(
    "--output-theme",
    type=click.Choice(["light", "dark", "newsroom-white"]),
    default=None,
    help=(
        "Override the rendered HTML theme for this run only. Forwarded to "
        "``JinjaRenderer.render_to_file`` so the published bundle reflects "
        "the operator's per-run choice instead of the dark default."
    ),
)
def main(
    run_date_str,
    mode,
    from_step,
    to_step,
    dry_run,
    policy_path,
    policy_override_json,
    output_theme,
):
    """Run the daily AI trend report pipeline."""
    if run_date_str:
        run_date = date.fromisoformat(run_date_str)
    else:
        run_date = date.today()

    if mode == "dry-run":
        dry_run = True

    # ``--policy-path`` is the explicit operator-facing knob; the env var is
    # how the API subprocess flow injects the runtime override. Both end up at
    # the same dispatch point in ``app.editorial.policy.load_policy``.
    if policy_path:
        os.environ[POLICY_PATH_ENV] = policy_path

    # Per-run policy override from the API → child process. Stored in env so
    # downstream callers of ``load_policy()`` (in any subprocess of this run)
    # can pick it up without threading the dict through every call site.
    if policy_override_json:
        os.environ["EDITORIAL_POLICY_OVERRIDE_JSON"] = policy_override_json

    asyncio.run(
        run_pipeline(
            run_date,
            mode,
            from_step,
            to_step,
            dry_run,
            output_theme=output_theme,
        )
    )


if __name__ == "__main__":
    main()
