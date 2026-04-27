from __future__ import annotations
import asyncio
from openai import AsyncOpenAI
from app.config import settings
from app.utils.logger import get_logger


class EmbeddingClient:
    BATCH_SIZE = 100  # OpenAI allows up to 2048, keep conservative

    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_embedding_model  # text-embedding-3-small
        self.logger = get_logger(step="cluster")

    async def embed(self, text: str) -> list[float]:
        """Embed a single text string. Returns 1536-dim vector."""
        result = await self.embed_batch([text])
        return result[0]

    async def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """Embed a batch of texts. Splits into batches of BATCH_SIZE."""
        if not texts:
            return []

        all_embeddings = []
        for i in range(0, len(texts), self.BATCH_SIZE):
            batch = texts[i:i + self.BATCH_SIZE]
            try:
                response = await self.client.embeddings.create(
                    model=self.model,
                    input=batch,
                )
                batch_embeddings = [item.embedding for item in response.data]
                all_embeddings.extend(batch_embeddings)
                self.logger.info("embeddings_batch_done", batch_size=len(batch), offset=i)
            except Exception as e:
                self.logger.error("embeddings_failed", batch_offset=i, error=str(e))
                # Return zero vectors for failed batch
                all_embeddings.extend([[0.0] * 1536] * len(batch))

        return all_embeddings
