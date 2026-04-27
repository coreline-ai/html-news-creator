import hashlib
import ipaddress
import re
from urllib.parse import urlparse, urlencode, parse_qsl, urlunparse

_SSRF_BLOCKED_NETWORKS = [
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
]

_UTM_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term",
    "utm_content", "fbclid", "gclid", "ref", "source",
}


def canonicalize_url(url: str) -> str:
    parsed = urlparse(url.strip())
    clean_params = [
        (k, v) for k, v in parse_qsl(parsed.query)
        if k.lower() not in _UTM_PARAMS
    ]
    clean = parsed._replace(
        query=urlencode(clean_params),
        fragment="",
        path=parsed.path.rstrip("/") or "/",
    )
    return urlunparse(clean)


def url_hash(url: str) -> str:
    return hashlib.sha256(canonicalize_url(url).encode()).hexdigest()


def is_ssrf_blocked(url: str) -> bool:
    try:
        host = urlparse(url).hostname or ""
        if host.lower() in ("localhost", "metadata.google.internal"):
            return True
        addr = ipaddress.ip_address(host)
        return any(addr in net for net in _SSRF_BLOCKED_NETWORKS)
    except ValueError:
        return False
