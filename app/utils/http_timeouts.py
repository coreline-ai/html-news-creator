"""Standard ``httpx.Timeout`` constants for outbound HTTP calls.

Centralised here so collectors / extractors share consistent connect/read
budgets and so an operator can tune them via environment variables without
touching code. Created in response to the 5/1 hang sample where a collector
``httpx.get`` issued a request without an explicit timeout and waited
indefinitely on read.

Defaults (seconds):
    - total / overall : ``COLLECTOR_TOTAL_TIMEOUT`` (default ``30``)
    - connect         : ``COLLECTOR_CONNECT_TIMEOUT`` (default ``5``)
    - read / write    : ``COLLECTOR_READ_TIMEOUT`` (default ``20``)

The ``EXTRACTOR_*`` variants exist for future use by ``app/extractors``;
they are intentionally not consumed yet.
"""
from __future__ import annotations

import os

import httpx


def _float_env(name: str, default: str) -> float:
    raw = os.getenv(name, default)
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return float(default)
    return value if value > 0 else float(default)


COLLECTOR_TIMEOUT = httpx.Timeout(
    timeout=_float_env("COLLECTOR_TOTAL_TIMEOUT", "30"),
    connect=_float_env("COLLECTOR_CONNECT_TIMEOUT", "5"),
    read=_float_env("COLLECTOR_READ_TIMEOUT", "20"),
    write=_float_env("COLLECTOR_READ_TIMEOUT", "20"),
)

EXTRACTOR_TIMEOUT = httpx.Timeout(
    timeout=_float_env("EXTRACTOR_TOTAL_TIMEOUT", "30"),
    connect=_float_env("EXTRACTOR_CONNECT_TIMEOUT", "5"),
    read=_float_env("EXTRACTOR_READ_TIMEOUT", "20"),
    write=_float_env("EXTRACTOR_READ_TIMEOUT", "20"),
)


__all__ = ["COLLECTOR_TIMEOUT", "EXTRACTOR_TIMEOUT"]
