from __future__ import annotations

from scripts.run_daily import (
    _noise_singleton_backfill_count,
    _selection_target_sections,
)


def _policy(**selection_overrides):
    selection = {
        "max_sections": 10,
        "target_sections": 10,
        "noise_singleton_backfill_enabled": True,
        "max_noise_singleton_backfill_clusters": 10,
    }
    selection.update(selection_overrides)
    return {"report_selection": selection}


def test_selection_target_sections_is_capped_by_max_sections():
    assert _selection_target_sections(_policy(max_sections=8, target_sections=10)) == 8


def test_noise_singleton_backfill_adds_candidate_pool_for_section_target():
    count = _noise_singleton_backfill_count(
        hdbscan_clusters=6,
        noise_count=14,
        policy=_policy(),
    )

    assert count == 10


def test_noise_singleton_backfill_disabled_by_policy():
    count = _noise_singleton_backfill_count(
        hdbscan_clusters=1,
        noise_count=20,
        policy=_policy(noise_singleton_backfill_enabled=False),
    )

    assert count == 0


def test_noise_singleton_backfill_skips_when_cluster_pool_already_reaches_target():
    count = _noise_singleton_backfill_count(
        hdbscan_clusters=10,
        noise_count=20,
        policy=_policy(),
    )

    assert count == 0
