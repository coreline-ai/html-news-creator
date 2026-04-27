from __future__ import annotations
import asyncio
from app.utils.logger import get_logger


class PaddleOCRUnavailableError(Exception):
    pass


class PaddleOCRClient:
    def __init__(self):
        self.logger = get_logger(step="image_analyze")
        try:
            from paddleocr import PaddleOCR
            self._ocr = PaddleOCR(use_angle_cls=True, lang="korean", show_log=False)
        except ImportError:
            self._ocr = None

    async def extract_text(self, image_data: bytes) -> str:
        """Extract text from image bytes using PaddleOCR."""
        if self._ocr is None:
            raise PaddleOCRUnavailableError("paddleocr not installed")

        try:
            import tempfile
            import os

            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
                f.write(image_data)
                tmp_path = f.name

            try:
                result = await asyncio.to_thread(self._ocr.ocr, tmp_path, cls=True)
                texts = []
                if result and result[0]:
                    for line in result[0]:
                        if line and len(line) >= 2:
                            texts.append(line[1][0])
                return "\n".join(texts)
            finally:
                os.unlink(tmp_path)
        except Exception as e:
            self.logger.error("paddle_ocr_failed", error=str(e))
            raise
