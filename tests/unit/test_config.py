from app.config import Settings


def test_settings_defaults():
    s = Settings(_env_file=None)
    assert s.app_env == "local"
    assert s.openai_api_key == "local-proxy"
    assert s.openai_base_url == "http://127.0.0.1:4317/openai/v1"
    assert s.openai_model == "gpt-5.5"
    assert s.openai_embedding_model == "text-embedding-3-small"


def test_settings_database_url_has_value():
    s = Settings(_env_file=None)
    assert "postgresql" in s.database_url
