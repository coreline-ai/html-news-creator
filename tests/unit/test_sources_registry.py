from pathlib import Path

import yaml


REGISTRY_PATH = Path(__file__).resolve().parents[2] / "data" / "sources_registry.yaml"
ALLOWED_SOURCE_TYPES = {"rss", "website", "github", "arxiv", "x", "manual"}
ALLOWED_SOURCE_TIERS = {
    "official",
    "mainstream",
    "research",
    "developer_signal",
    "community",
    "unknown",
}
REQUIRED_FIELDS = {"name", "source_type", "trust_level", "source_tier", "priority"}
EXPANDED_SOURCE_NAMES = {
    "Google AI Blog",
    "NVIDIA AI Blog",
    "AWS Machine Learning Blog",
    "Google Cloud Tech YouTube",
    "OpenAI YouTube",
    "VentureBeat AI",
    "Yahoo Finance AI",
    "AI타임스",
    "Hacker News AI",
    "Reddit MachineLearning",
    "Reddit LocalLLaMA",
}
EXCLUDED_DEFAULT_SOURCE_NAMES = {
    "NAVER News AI",
    "NAVER 뉴스 AI",
    "YouTube AI Search",
    "X @AnthropicAI",
    "X @OpenAI",
}
EXCLUDED_DEFAULT_SOURCE_TYPES = {
    "naver_news",
    "youtube_search",
    "x",
}
EXCLUDED_URL_FRAGMENTS = {
    "openapi.naver.com",
    "googleapis.com/youtube",
    "api.twitter.com",
    "nitter.net",
    "nitter.privacyredirect.com",
}


def load_sources() -> list[dict]:
    with REGISTRY_PATH.open() as f:
        data = yaml.safe_load(f)
    assert isinstance(data, dict)
    assert isinstance(data.get("sources"), list)
    return data["sources"]


def test_sources_registry_loads_yaml():
    sources = load_sources()
    assert sources


def test_sources_have_required_fields():
    for source in load_sources():
        missing = REQUIRED_FIELDS - set(source)
        assert not missing, f"{source.get('name', '<unnamed>')} missing {missing}"
        assert source["source_type"] in ALLOWED_SOURCE_TYPES
        if source["source_type"] in {"rss", "website"}:
            assert source.get("url")
        if source["source_type"] == "github":
            assert source.get("org")
        if source["source_type"] == "arxiv":
            assert source.get("category")


def test_source_tier_values_are_known():
    tiers = {source["source_tier"] for source in load_sources()}
    assert tiers <= ALLOWED_SOURCE_TIERS
    assert {"official", "mainstream", "research", "developer_signal"} <= tiers


def test_mainstream_sources_include_at_least_three_priority_outlets():
    sources = load_sources()
    mainstream_names = {
        source["name"]
        for source in sources
        if source.get("source_tier") == "mainstream"
    }
    expected = {"TechCrunch AI", "MIT News AI", "The Verge AI"}
    assert expected <= mainstream_names
    assert len(mainstream_names) >= 3


def test_arxiv_sources_are_low_priority_research():
    arxiv_sources = [source for source in load_sources() if source["source_type"] == "arxiv"]
    assert arxiv_sources
    for source in arxiv_sources:
        assert source["source_tier"] == "research"
        assert source.get("content_category") == "research"
        assert source["priority"] <= 30
        assert source["max_items"] <= 5


def test_github_sources_are_developer_signal():
    github_sources = [source for source in load_sources() if source["source_type"] == "github"]
    assert github_sources
    for source in github_sources:
        assert source["source_tier"] == "developer_signal"
        assert source["priority"] <= 55


def test_expanded_ai_trend_sources_are_registered_with_quality_metadata():
    sources = {source["name"]: source for source in load_sources()}
    assert EXPANDED_SOURCE_NAMES <= set(sources)

    for name in EXPANDED_SOURCE_NAMES:
        source = sources[name]
        assert source["max_items"] > 0
        assert isinstance(source.get("required"), bool)
        assert source.get("purpose")
        assert source.get("content_category")
        assert isinstance(source.get("keywords"), list)
        assert source["keywords"], f"{name} should define trend keywords"


def test_special_collectors_use_website_source_type():
    sources = {source["name"]: source for source in load_sources()}

    hacker_news = sources["Hacker News AI"]
    assert hacker_news["source_type"] == "website"
    assert hacker_news["collector_type"] == "hackernews"
    assert hacker_news["source_tier"] == "community"


def test_api_key_required_sources_are_excluded_from_default_registry():
    sources = load_sources()
    source_names = {source["name"] for source in sources}
    source_types = {source["source_type"] for source in sources}
    urls = {
        str(source.get(url_field, ""))
        for source in sources
        for url_field in ("url", "fallback_url")
    }

    assert source_names.isdisjoint(EXCLUDED_DEFAULT_SOURCE_NAMES)
    assert source_types.isdisjoint(EXCLUDED_DEFAULT_SOURCE_TYPES)
    for url in urls:
        assert not any(fragment in url for fragment in EXCLUDED_URL_FRAGMENTS)


def test_yahoo_finance_ai_uses_ai_filter():
    sources = {source["name"]: source for source in load_sources()}

    assert sources["Yahoo Finance AI"].get("ai_filter") is True
