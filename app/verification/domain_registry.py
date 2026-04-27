from __future__ import annotations
import yaml
from pathlib import Path
from urllib.parse import urlparse


YAML_PATH = Path("data/official_domains.yaml")


class DomainRegistry:
    def __init__(self, yaml_path: Path = YAML_PATH):
        with open(yaml_path) as f:
            self._data = yaml.safe_load(f)
        # Build lookup sets
        self._official = set(self._data.get("official", []))
        self._trusted_media = set(self._data.get("trusted_media", []))
        self._community = set(self._data.get("community", []))

    def _extract_domain(self, url: str) -> str:
        parsed = urlparse(url)
        return parsed.netloc.lower().lstrip("www.")

    def classify(self, url: str) -> str:
        """Returns: 'official' | 'trusted_media' | 'community' | 'unknown'"""
        domain = self._extract_domain(url)
        full_url_lower = url.lower()

        # Check official (including path-based matches like github.com/openai)
        for entry in self._official:
            if domain == entry or domain.endswith("." + entry) or full_url_lower.startswith("https://" + entry) or full_url_lower.startswith("http://" + entry):
                return "official"

        for entry in self._trusted_media:
            if domain == entry or domain.endswith("." + entry):
                return "trusted_media"

        for entry in self._community:
            if domain == entry or domain.endswith("." + entry) or full_url_lower.startswith("https://" + entry):
                return "community"

        return "unknown"

    def trust_base_score(self, url: str) -> int:
        """Returns base trust score: official=90, trusted_media=70, community=40, unknown=20"""
        category = self.classify(url)
        return {"official": 90, "trusted_media": 70, "community": 40, "unknown": 20}[category]
