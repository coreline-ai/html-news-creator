from app.utils.url_utils import canonicalize_url, url_hash


def canonicalize(url: str) -> tuple[str, str]:
    """Returns (canonical_url, url_hash)"""
    canon = canonicalize_url(url)
    return canon, url_hash(canon)
