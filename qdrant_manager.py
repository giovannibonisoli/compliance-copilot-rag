from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class QdrantManager:

    def __init__(self, path: str = "./qdrant_data"):
        self.client = QdrantClient(path=path)

    def create_collection(self, collection_name: str,  vector_size: int = 384):

        collections = self.client.get_collections()

        existing = [c.name for c in collections.collections]

        if collection_name in existing:
            return

        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

    def upload_chunks(self, collection_name: str, chunks, embeddings):

        points = []

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):

            points.append(
                PointStruct(
                    id=chunk["chunk_id"],
                    vector=embedding.tolist(),
                    payload={
                        "source": chunk["source"],
                        "page_number": chunk["page_number"],
                        "text": chunk["text"]
                    }
                )
            )

        self.client.upsert(
            collection_name=collection_name,
            points=points
        )