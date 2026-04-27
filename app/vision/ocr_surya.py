from __future__ import annotations
import asyncio
from app.utils.logger import get_logger


class SuryaOCRUnavailableError(Exception):
    pass


class SuryaOCRClient:
    def __init__(self):
        self.logger = get_logger(step="image_analyze")
        try:
            import surya
            self._available = True
        except ImportError:
            self._available = False

    async def extract_text(self, image_data: bytes) -> str:
        """Extract text from image bytes using Surya OCR."""
        if not self._available:
            raise SuryaOCRUnavailableError("surya-ocr not installed")

        try:
            from PIL import Image
            import io

            image = Image.open(io.BytesIO(image_data))

            from surya.ocr import run_ocr
            from surya.model.detection.segformer import load_model as load_det_model, load_processor as load_det_processor
            from surya.model.recognition.model import load_model as load_rec_model
            from surya.model.recognition.processor import load_processor as load_rec_processor

            langs = ["ko", "en"]
            det_model, det_processor = load_det_model(), load_det_processor()
            rec_model, rec_processor = load_rec_model(), load_rec_processor()

            predictions = await asyncio.to_thread(
                run_ocr, [image], [langs], det_model, det_processor, rec_model, rec_processor
            )

            texts = []
            if predictions:
                for pred in predictions[0].text_lines:
                    texts.append(pred.text)
            return "\n".join(texts)
        except Exception as e:
            self.logger.error("surya_ocr_failed", error=str(e))
            raise
