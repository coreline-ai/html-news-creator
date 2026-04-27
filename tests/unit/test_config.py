import pytest
from app.config import Settings


def test_settings_defaults():
    s = Settings()
    assert s.app_env == "local"
    assert s.openai_model == "gpt-5.5"


def test_settings_database_url_has_value():
    s = Settings()
    assert "postgresql" in s.database_url
