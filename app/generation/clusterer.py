from __future__ import annotations
import numpy as np
from dataclasses import dataclass
from app.utils.logger import get_logger


@dataclass
class ClusterResult:
    labels: list[int]          # -1 = noise point
    n_clusters: int
    noise_count: int
    cluster_sizes: dict[int, int]  # cluster_id -> size


class HDBSCANClusterer:
    def __init__(self, min_cluster_size: int = 2, min_samples: int = 1):
        self.min_cluster_size = min_cluster_size
        self.min_samples = min_samples
        self.logger = get_logger(step="cluster")

    def cluster(self, embeddings: list[list[float]]) -> ClusterResult:
        """
        Cluster embeddings using HDBSCAN with cosine distance.
        Returns ClusterResult with labels (-1 for noise).
        """
        if len(embeddings) < 2:
            labels = [0] * len(embeddings) if embeddings else []
            return ClusterResult(
                labels=labels,
                n_clusters=len(embeddings),
                noise_count=0,
                cluster_sizes={i: 1 for i in range(len(embeddings))},
            )

        try:
            import hdbscan
            X = np.array(embeddings, dtype=np.float32)
            # Normalize for cosine similarity
            norms = np.linalg.norm(X, axis=1, keepdims=True)
            norms = np.where(norms == 0, 1, norms)
            X_normalized = X / norms

            clusterer = hdbscan.HDBSCAN(
                min_cluster_size=self.min_cluster_size,
                min_samples=self.min_samples,
                metric="euclidean",  # euclidean on normalized = cosine similarity
            )
            labels = clusterer.fit_predict(X_normalized).tolist()
        except ImportError:
            message = (
                "HDBSCAN clustering requires the hdbscan package. Install hdbscan "
                "or run the pipeline with requirements.txt so the report is not "
                "silently collapsed into one cluster."
            )
            self.logger.error("hdbscan_unavailable", error=message)
            raise RuntimeError(message)

        label_array = labels
        n_clusters = len(set(label for label in label_array if label >= 0))
        noise_count = sum(1 for label in label_array if label == -1)
        cluster_sizes = {}
        for label in label_array:
            if label >= 0:
                cluster_sizes[label] = cluster_sizes.get(label, 0) + 1

        self.logger.info("clustering_done", n_clusters=n_clusters, noise_count=noise_count, total=len(embeddings))
        return ClusterResult(
            labels=label_array,
            n_clusters=n_clusters,
            noise_count=noise_count,
            cluster_sizes=cluster_sizes,
        )
