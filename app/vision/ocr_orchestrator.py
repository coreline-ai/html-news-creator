from __future__ import annotations
from app.vision.ocr_paddle import PaddleOCRClient, PaddleOCRUnavailableError
from app.vision.ocr_surya import SuryaOCRClient, SuryaOCRUnavailableError
from app.utils.logger import get_logger


class OCROrchestrator:
    """Fallback chain: PaddleOCR -> Surya -> skip."""

    def __init__(self):
        self.paddle = PaddleOCRClient()
        self.surya = SuryaOCRClient()
        self.logger = get_logger(step="image_analyze")

    async def extract_text(self, image_data: bytes) -> str | None:
        """Extract text, trying PaddleOCR first, then Surya. Returns None if both unavailable."""
        for ocr, unavailable_err in [
            (self.paddle, PaddleOCRUnavailableError),
            (self.surya, SuryaOCRUnavailableError),
        ]:
            try:
                text = await ocr.extract_text(image_data)
                return text
            except unavailable_err:
                continue
            except Exception as e:
                self.logger.warning("ocr_failed", extractor=type(ocr).__name__, error=str(e))
                continue

        self.logger.info("no_ocr_available", note="Skipping OCR extraction")
        return None
