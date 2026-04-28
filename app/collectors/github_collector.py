from __future__ import annotations

from datetime import datetime, timezone

from github import Github, GithubException, RateLimitExceededException
from github import GithubRetry

from app.collectors.base import BaseCollector, CollectedItem
from app.config import settings
from app.utils.logger import get_logger
from app.utils.url_utils import canonicalize_url, url_hash

logger = get_logger(step="collect")

# Maximum number of repos to inspect per org to avoid exhausting rate limit.
_MAX_REPOS = 30
# Maximum releases to fetch per repo.
_MAX_RELEASES_PER_REPO = 10


class GitHubCollector(BaseCollector):
    """Collects recent releases from a GitHub organisation."""

    def __init__(self, source: dict) -> None:
        self.source = source
        self.org: str = source["org"]
        self.source_id: str = source.get("name", self.org)

    async def collect(self, date_from: datetime, date_to: datetime) -> list[CollectedItem]:
        token = settings.github_token or None
        # total=0 disables PyGitHub's exponential-backoff on rate-limit — fail fast instead
        retry = GithubRetry(total=0)
        gh = Github(login_or_token=token, retry=retry) if token else Github(retry=retry)

        items: list[CollectedItem] = []

        try:
            org = gh.get_organization(self.org)
            repos = org.get_repos(sort="updated", direction="desc")

            repo_count = 0
            for repo in repos:
                if repo_count >= _MAX_REPOS:
                    break
                repo_count += 1

                try:
                    releases = repo.get_releases()
                    release_count = 0
                    for release in releases:
                        if release_count >= _MAX_RELEASES_PER_REPO:
                            break
                        release_count += 1

                        published_at: datetime | None = None
                        if release.published_at:
                            published_at = release.published_at.replace(tzinfo=timezone.utc)

                        # Only keep releases within the requested window.
                        if published_at is not None:
                            if published_at < date_from or published_at > date_to:
                                # Releases are sorted newest-first; stop early if we
                                # have gone past the window.
                                if published_at < date_from:
                                    break
                                continue

                        raw_url = release.html_url
                        canonical = canonicalize_url(raw_url)
                        canon_hash = url_hash(raw_url)

                        body_text: str | None = release.body or None

                        item = CollectedItem(
                            source_id=self.source_id,
                            source_type="github",
                            title=f"{repo.full_name} {release.tag_name}",
                            url=raw_url,
                            canonical_url=canonical,
                            canonical_url_hash=canon_hash,
                            raw_text=body_text,
                            author=release.author.login if release.author else None,
                            published_at=published_at,
                            metrics_json={
                                "stars": repo.stargazers_count,
                                "forks": repo.forks_count,
                            },
                            raw_json={
                                "repo": repo.full_name,
                                "tag": release.tag_name,
                                "prerelease": release.prerelease,
                                "draft": release.draft,
                            },
                        )
                        items.append(item)

                except RateLimitExceededException:
                    logger.warning(
                        "github_rate_limit_hit",
                        source=self.source_id,
                        repo=repo.full_name,
                        collected_so_far=len(items),
                    )
                    return items

                except GithubException as exc:
                    logger.warning(
                        "github_repo_error",
                        source=self.source_id,
                        repo=repo.full_name,
                        error=str(exc),
                    )

        except RateLimitExceededException:
            logger.warning(
                "github_rate_limit_hit",
                source=self.source_id,
                collected_so_far=len(items),
            )
            return items

        except Exception as exc:
            logger.error("github_collect_failed", source=self.source_id, error=str(exc))
            return []

        finally:
            gh.close()

        logger.info("github_collected", source=self.source_id, count=len(items))
        return items
