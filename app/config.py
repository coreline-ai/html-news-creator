from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "local"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/ai_trend"
    redis_url: str = "redis://localhost:6379"
    report_public_base_url: str = "http://localhost:3000"

    # OpenAI-compatible proxy (multi_model_tui local proxy: http://127.0.0.1:4317)
    openai_api_key: str = "local-proxy"
    openai_base_url: str = "http://127.0.0.1:4317/openai/v1"
    openai_model: str = "gpt-5.5"
    openai_embedding_model: str = "text-embedding-3-small"
    news_studio_llm_proxy_start_command: str = "make proxy"

    firecrawl_api_key: str = ""
    crawl4ai_enabled: bool = True
    trafilatura_enabled: bool = True

    supabase_url: str = ""
    supabase_anon_key: str = ""
    supabase_service_role_key: str = ""

    github_token: str = ""
    github_allow_unauthenticated: bool = True

    x_bearer_token: str = ""
    x_enabled: bool = False

    naver_client_id: str = ""
    naver_client_secret: str = ""

    s3_endpoint: str = "http://localhost:9000"
    s3_access_key: str = "minioadmin"
    s3_secret_key: str = "minioadmin"
    s3_bucket: str = "ai-trend-assets"
    s3_region: str = "us-east-1"

    netlify_auth_token: str = ""
    netlify_site_id: str = ""

    slack_webhook_url: str = ""

    timezone: str = "Asia/Seoul"
    log_level: str = "info"
    max_sources_per_run: int = 500
    max_images_per_run: int = 50
    generated_image_fallback_enabled: bool = True
    # Full runs can spend several minutes in classify/verify/generate when the
    # local GPT proxy is used. Keep this configurable, but default high enough
    # that normal 10-section runs reach generate/render instead of leaving the
    # previous report visible.
    admin_run_default_max_runtime_sec: int = 900

    # News Studio web UI (Phase 1)
    ui_dist_path: str = "ui/dist"
    ui_dev_origin: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
