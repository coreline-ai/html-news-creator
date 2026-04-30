from __future__ import annotations
import hashlib
import httpx
from app.config import settings
from app.utils.url_utils import is_ssrf_blocked
from app.utils.logger import get_logger


class MediaDownloader:
    MAX_IMAGE_BYTES = 10 * 1024 * 1024  # 10MB limit
    ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}

    def __init__(self):
        self.logger = get_logger(step="image_analyze")
        self._download_count = 0

    async def download(self, url: str, raw_item_id: str = "") -> dict | None:
        """
        Downloads an image, computes SHA256, uploads to MinIO if configured.
        Returns: dict with {url, sha256, mime_type, size_bytes, storage_path} or None on failure.
        """
        # SSRF protection
        if is_ssrf_blocked(url):
            self.logger.warning("ssrf_blocked_image", url=url)
            return None

        # Rate limit check
        if self._download_count >= settings.max_images_per_run:
            self.logger.warning("max_images_reached", limit=settings.max_images_per_run)
            return None

        try:
            async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
                resp = await client.get(url, headers={"User-Agent": "ai-trend-bot/0.1"})
                resp.raise_for_status()

                content_type = resp.headers.get("content-type", "").split(";")[0].strip()
                if content_type not in self.ALLOWED_MIME_TYPES:
                    self.logger.debug("skip_non_image", url=url, content_type=content_type)
                    return None

                data = resp.content
                if len(data) > self.MAX_IMAGE_BYTES:
                    self.logger.warning("image_too_large", url=url, size=len(data))
                    return None

                sha256 = hashlib.sha256(data).hexdigest()
                ext = {"image/jpeg": "jpg", "image/png": "png", "image/gif": "gif", "image/webp": "webp"}.get(content_type, "bin")
                storage_path = f"images/{sha256[:2]}/{sha256}.{ext}"

                self._download_count += 1
                self.logger.info("image_downloaded", url=url, sha256=sha256[:8], size=len(data))

                return {
                    "url": url,
                    "sha256": sha256,
                    "mime_type": content_type,
                    "size_bytes": len(data),
                    "storage_path": storage_path,
                    "data": data,
                }
        except Exception as e:
            self.logger.error("image_download_failed", url=url, error=str(e))
            return None

    def reset_count(self):
        self._download_count = 0
