from typing import Sequence

import numpy as np
from sentence_transformers import SentenceTransformer

from src.chunker import Chunk


class Embedder:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> None:
        self.model = SentenceTransformer(model_name)

    def embed_chunks(self, chunks: Sequence[Chunk]) -> np.ndarray:

        if not chunks:
            raise ValueError("chunks cannot be empty")

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(texts, show_progress_bar=True, convert_to_numpy=True)

        return embeddings

    def embed_query(self, query: str) -> np.ndarray:

        if not query.strip():
            raise ValueError("query cannot be empty")

        embedding = self.model.encode(query, convert_to_numpy=True)

        return embedding