from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from app.admin.api import app
from app.db import get_db


def _empty_db_override():
    async def _gen():
        mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all.return_value = []
        scalars_mock.first.return_value = None
        execute_result = MagicMock()
        execute_result.scalars.return_value = scalars_mock
        execute_result.scalar.return_value = 0
        mock.execute.return_value = execute_result
        yield mock

    return _gen


@pytest.fixture(autouse=True)
def _reset_admin_db_override():
    """Keep admin API unit tests isolated from real Postgres and each other."""
    previous = app.dependency_overrides.get(get_db)
    app.dependency_overrides[get_db] = _empty_db_override()
    try:
        yield
    finally:
        if previous is None:
            app.dependency_overrides.pop(get_db, None)
        else:
            app.dependency_overrides[get_db] = previous
