from __future__ import annotations

import uuid
from datetime import date, datetime, timezone
from types import SimpleNamespace

from app.admin.job_runs import (
    build_job_metadata,
    coerce_run_uuid,
    job_run_to_summary,
    parse_report_date,
)
from app.models.db_models import JobRun


def test_coerce_run_uuid_accepts_hex_and_hyphenated():
    value = uuid.uuid4()
    assert coerce_run_uuid(value.hex) == value
    assert coerce_run_uuid(str(value)) == value
    assert coerce_run_uuid("not-a-uuid") is None


def test_parse_report_date_accepts_date_and_run_date():
    assert parse_report_date({"date": "2026-05-01"}) == date(2026, 5, 1)
    assert parse_report_date({"run_date": "2026-05-02"}) == date(2026, 5, 2)
    assert parse_report_date({"date": "bad"}) is None


def test_job_run_to_summary_uses_metadata_run_id_and_options():
    job_id = uuid.uuid4()
    run_id = job_id.hex
    job = JobRun(
        id=job_id,
        job_name="daily_report",
        report_date=date(2026, 5, 1),
        status="completed",
        started_at=datetime(2026, 5, 1, 0, 0, tzinfo=timezone.utc),
        completed_at=datetime(2026, 5, 1, 0, 1, tzinfo=timezone.utc),
        metadata_json={
            "run_id": run_id,
            "options": {"date": "2026-05-01", "mode": "full"},
            "return_code": 0,
        },
    )

    summary = job_run_to_summary(job, trackable=False)

    assert summary["id"] == str(job_id)
    assert summary["run_id"] == run_id
    assert summary["status"] == "completed"
    assert summary["report_date"] == "2026-05-01"
    assert summary["return_code"] == 0
    assert summary["options"]["mode"] == "full"
    assert summary["trackable"] is False
    assert summary["source"] == "db"


def test_job_run_to_summary_marks_db_only_running_as_untrackable_error():
    job = JobRun(
        id=uuid.uuid4(),
        job_name="daily_report",
        status="running",
        metadata_json={},
    )

    summary = job_run_to_summary(job, trackable=False)

    assert summary["trackable"] is False
    assert summary["status"] == "running"
    assert "server_restart_or_memory_state_lost" in summary["error"]


def test_build_job_metadata_copies_state_options():
    state = SimpleNamespace(
        run_id="abc",
        options={"date": "2026-05-01", "dry_run": True},
        return_code=2,
        error="max_runtime_exceeded: 300s",
    )

    metadata = build_job_metadata(state)

    assert metadata["run_id"] == "abc"
    assert metadata["options"] == {"date": "2026-05-01", "dry_run": True}
    assert metadata["return_code"] == 2
    assert metadata["error"] == "max_runtime_exceeded: 300s"
