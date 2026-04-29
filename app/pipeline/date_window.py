from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

_FALLBACK_TIMEZONE = "Asia/Seoul"

# US tech outlets publish during US business hours (roughly 13:00–23:00 UTC).
# The KST day window closes at 14:59 UTC (= 23:59 KST), so US afternoon/evening
# articles published after 15:00 UTC would be missed. We extend the window end
# by this many hours to capture US Pacific evening content (e.g. 22:00 UTC =
# 15:00 PDT).  The start is also relaxed slightly so KST-morning items pushed
# to UTC the previous evening are not lost.
_SLACK_HOURS_BEFORE = 1   # extra hours before local midnight
_SLACK_HOURS_AFTER = 9    # extra hours after local end-of-day (covers US PT evening)


def _configured_timezone_name() -> str:
    from app.config import settings

    return settings.timezone or _FALLBACK_TIMEZONE


def _zoneinfo(timezone_name: str | None = None) -> ZoneInfo:
    name = timezone_name or _configured_timezone_name()
    try:
        return ZoneInfo(name)
    except (ZoneInfoNotFoundError, ValueError):
        return ZoneInfo(_FALLBACK_TIMEZONE)


def local_day_window_utc(
    run_date: date,
    timezone_name: str | None = None,
) -> tuple[datetime, datetime]:
    """Return the UTC datetime window covering one local calendar day plus slack.

    The window starts ``_SLACK_HOURS_BEFORE`` hours before local midnight and
    ends ``_SLACK_HOURS_AFTER`` hours after local end-of-day.  This captures US
    business-hour articles that are published after the KST calendar day closes
    in UTC terms.

    When ``timezone_name`` is omitted, the configured application timezone is
    used. Invalid timezone names fall back to Asia/Seoul.
    """
    local_tz = _zoneinfo(timezone_name)
    date_from_local = datetime.combine(run_date, time.min, tzinfo=local_tz)
    date_to_local = datetime.combine(run_date, time.max, tzinfo=local_tz)
    date_from_utc = date_from_local.astimezone(timezone.utc) - timedelta(hours=_SLACK_HOURS_BEFORE)
    date_to_utc = date_to_local.astimezone(timezone.utc) + timedelta(hours=_SLACK_HOURS_AFTER)
    return date_from_utc, date_to_utc


def contains_datetime(
    dt: datetime,
    run_date: date,
    timezone_name: str | None = None,
) -> bool:
    """Return whether ``dt`` falls inside the local-day UTC window."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    dt_utc = dt.astimezone(timezone.utc)
    date_from_utc, date_to_utc = local_day_window_utc(run_date, timezone_name)
    return date_from_utc <= dt_utc <= date_to_utc
