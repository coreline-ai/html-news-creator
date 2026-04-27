from app.utils.url_utils import canonicalize_url, url_hash, is_ssrf_blocked


def test_canonicalize_removes_utm():
    url = "https://example.com/a?utm_source=twitter&id=1"
    assert canonicalize_url(url) == "https://example.com/a?id=1"


def test_canonicalize_removes_fragment():
    url = "https://example.com/page#section"
    assert "#" not in canonicalize_url(url)


def test_url_hash_deterministic():
    url = "https://openai.com/blog"
    assert url_hash(url) == url_hash(url)


def test_ssrf_blocked_localhost():
    assert is_ssrf_blocked("http://localhost/admin") is True


def test_ssrf_blocked_metadata():
    assert is_ssrf_blocked("http://169.254.169.254/latest") is True


def test_ssrf_allowed_public():
    assert is_ssrf_blocked("https://openai.com") is False
