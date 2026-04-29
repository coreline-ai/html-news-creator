from __future__ import annotations
import asyncio
from openai import AsyncOpenAI
from app.config import settings
from app.utils.logger import get_logger


def _local_embed_batch(texts: list[str]) -> list[list[float]]:
    """Fallback: local sentence-transformers embeddings."""
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    vecs = model.encode(texts, normalize_embeddings=True)
    # Pad/trim to 1536 dims to keep interface consistent
    result = []
    for v in vecs:
        v_list = v.tolist()
        if len(v_list) < 1536:
            v_list = v_list + [0.0] * (1536 - len(v_list))
        else:
            v_list = v_list[:1536]
        result.append(v_list)
    return result


class EmbeddingClient:
    BATCH_SIZE = 100

    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key, base_url=settings.openai_base_url)
        self.model = settings.openai_embedding_model
        self.logger = get_logger(step="cluster")

    async def embed(self, text: str) -> list[float]:
        result = await self.embed_batch([text])
        return result[0]

    async def embed_batch(self, texts: list[str]) -> list[list[float]]:
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
                self.logger.warning(
                    "embeddings_api_failed_using_local",
                    batch_offset=i,
                    error=str(e),
                )
                try:
                    local_embeddings = await asyncio.to_thread(_local_embed_batch, batch)
                    all_embeddings.extend(local_embeddings)
                    self.logger.info("embeddings_local_done", batch_size=len(batch), offset=i)
                except Exception as e2:
                    self.logger.error("embeddings_local_failed", error=str(e2))
                    all_embeddings.extend([[0.0] * 1536] * len(batch))

        return all_embeddings
