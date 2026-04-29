from datetime import date, datetime, timezone

from app.pipeline.date_window import (
    _SLACK_HOURS_AFTER,
    _SLACK_HOURS_BEFORE,
    contains_datetime,
    local_day_window_utc,
)


def test_local_day_window_utc_for_asia_seoul():
    # KST midnight = 15:00 UTC previous day; window starts 1h before = 14:00 UTC
    # KST end-of-day = 14:59:59 UTC; window ends 9h after = 23:59:59 UTC
    date_from, date_to = local_day_window_utc(date(2026, 4, 28), "Asia/Seoul")

    assert date_from == datetime(2026, 4, 27, 15 - _SLACK_HOURS_BEFORE, 0, 0, tzinfo=timezone.utc)
    assert date_to == datetime(2026, 4, 28, 14 + _SLACK_HOURS_AFTER, 59, 59, 999999, tzinfo=timezone.utc)


def test_local_day_window_utc_for_utc_timezone():
    # UTC midnight = 00:00 UTC; window starts 1h before = 23:00 UTC previous day
    # UTC end-of-day = 23:59:59 UTC; window ends 9h after = 08:59:59 UTC next day
    date_from, date_to = local_day_window_utc(date(2026, 4, 28), "UTC")

    assert date_from == datetime(2026, 4, 27, 24 - _SLACK_HOURS_BEFORE, 0, 0, tzinfo=timezone.utc)
    assert date_to == datetime(2026, 4, 29, _SLACK_HOURS_AFTER - 1, 59, 59, 999999, tzinfo=timezone.utc)


def test_invalid_timezone_falls_back_to_asia_seoul():
    date_from, date_to = local_day_window_utc(date(2026, 4, 28), "Invalid/Timezone")

    assert date_from == datetime(2026, 4, 27, 15 - _SLACK_HOURS_BEFORE, 0, 0, tzinfo=timezone.utc)
    assert date_to == datetime(2026, 4, 28, 14 + _SLACK_HOURS_AFTER, 59, 59, 999999, tzinfo=timezone.utc)


def test_contains_datetime_uses_local_day_window():
    run_date = date(2026, 4, 28)

    # Start of window (14:00 UTC) should be included
    assert contains_datetime(
        datetime(2026, 4, 27, 15 - _SLACK_HOURS_BEFORE, 0, 0, tzinfo=timezone.utc),
        run_date,
        "Asia/Seoul",
    )
    # End of window (23:59:59 UTC) should be included
    assert contains_datetime(
        datetime(2026, 4, 28, 14 + _SLACK_HOURS_AFTER, 59, 59, 999999, tzinfo=timezone.utc),
        run_date,
        "Asia/Seoul",
    )
    # Just after window end should be excluded
    assert not contains_datetime(
        datetime(2026, 4, 29, _SLACK_HOURS_AFTER, 0, 0, tzinfo=timezone.utc),
        run_date,
        "Asia/Seoul",
    )


def test_none_timezone_uses_configured_settings(monkeypatch):
    from app.config import settings

    monkeypatch.setattr(settings, "timezone", "UTC")

    date_from, date_to = local_day_window_utc(date(2026, 4, 28))

    assert date_from == datetime(2026, 4, 27, 24 - _SLACK_HOURS_BEFORE, 0, 0, tzinfo=timezone.utc)
    assert date_to == datetime(2026, 4, 29, _SLACK_HOURS_AFTER - 1, 59, 59, 999999, tzinfo=timezone.utc)
