from src.embedder import Embedder
from src.qdrant_manager import QdrantManager


COLLECTION_NAME = "compliance_docs"


class Retriever:

    def __init__(self):

        self.embedder = Embedder()

        self.qdrant = QdrantManager()

    def search(
        self,
        query: str,
        limit: int = 5
    ):

        query_embedding = (
            self.embedder.embed_query(query)
        )

        results = self.qdrant.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=limit
        )

        return results