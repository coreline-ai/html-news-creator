#!/usr/bin/env python3
"""Daily AI trend report pipeline entrypoint."""
from __future__ import annotations
import asyncio
import sys
from datetime import date, datetime, timezone
from pathlib import Path
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


async def run_collect(run_date: date, dry_run: bool, logger) -> dict:
    from app.collectors.orchestrator import CollectorOrchestrator
    orchestrator = CollectorOrchestrator()
    result = await orchestrator.run(run_date, dry_run=dry_run)
    logger.info("collect_done", total=result.total, inserted=result.inserted, skipped=result.skipped)
    return {"total": result.total, "inserted": result.inserted}


async def run_extract(run_date: date, dry_run: bool, logger) -> dict:
    logger.info("extract_step", status="not_implemented_yet")
    return {}


async def run_classify(run_date: date, dry_run: bool, logger) -> dict:
    logger.info("classify_step", status="not_implemented_yet")
    return {}


async def run_cluster(run_date: date, dry_run: bool, logger) -> dict:
    from app.generation.embeddings import EmbeddingClient
    from app.generation.clusterer import HDBSCANClusterer
    logger.info("cluster_step", status="stub_ready")
    return {}


async def run_verify(run_date: date, dry_run: bool, logger) -> dict:
    from app.verification.verifier import SourceVerifier
    logger.info("verify_step", status="stub_ready", note="Full implementation requires Phase 4 clusters")
    return {"status": "skipped_no_clusters"}


async def run_image_analyze(run_date: date, dry_run: bool, logger) -> dict:
    logger.info("image_analyze_step", status="not_implemented_yet")
    return {}


async def run_generate(run_date: date, dry_run: bool, logger) -> dict:
    from app.generation.section_generator import SectionGenerator
    from app.generation.report_assembler import ReportAssembler
    logger.info("generate_step", status="stub_ready")
    return {}


async def run_render(run_date: date, dry_run: bool, logger) -> dict:
    from app.rendering.jinja_renderer import JinjaRenderer
    renderer = JinjaRenderer()

    # Build minimal report object for dry-run/stub
    report = {
        "title": f"AI 트렌드 리포트 {run_date}",
        "report_date": str(run_date),
        "summary_ko": "오늘의 AI 트렌드 리포트입니다.",
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "stats": {
            "total_sources": 0,
            "ai_relevant": 0,
            "clusters": 0,
            "verified": 0,
        },
    }
    sections = []

    output_path = f"public/news/{run_date}-trend.html"
    if not dry_run:
        renderer.render_to_file(report, sections, output_path)
        logger.info("render_done", output_path=output_path)
    else:
        html = renderer.render_report(report, sections)
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
    logger.info("pipeline_start", date=str(run_date), mode=mode, from_step=from_step, to_step=to_step, dry_run=dry_run)

    # Determine which steps to run
    from_idx = STEPS.index(from_step)
    to_idx = STEPS.index(to_step)
    steps_to_run = STEPS[from_idx:to_idx + 1]

    # In rss-only mode, only run collect and render
    if mode == "rss-only":
        steps_to_run = [s for s in steps_to_run if s in ("collect", "render")]

    results = {}
    for step in steps_to_run:
        logger.info("step_start", step=step)
        try:
            fn = STEP_FUNCTIONS[step]
            result = await fn(run_date, dry_run, logger)
            results[step] = result
            logger.info("step_done", step=step)
        except Exception as e:
            logger.error("step_failed", step=step, error=str(e))
            if step == "collect":
                raise  # fatal
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
