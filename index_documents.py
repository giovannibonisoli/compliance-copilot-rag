from parser import load_pdf
from chunker import chunk_text, Chunk
from embedder import Embedder
from qdrant_manager import QdrantManager


COLLECTION_NAME = "compliance_docs"


def main():

    pdf_path = "data/raw/GDPR.pdf"

    pages = load_pdf(pdf_path)

    all_chunks: list[Chunk] = []

    global_chunk_id = 0

    for page in pages:

        page_chunks = chunk_text(
            text=page["text"],
            source=page["source"],
            page_number=page["page_number"]
        )

        for chunk in page_chunks:

            chunk["chunk_id"] = global_chunk_id

            all_chunks.append(chunk)

            global_chunk_id += 1

    print(f"Generated {len(all_chunks)} chunks")

    embedder = Embedder()

    embeddings = embedder.embed_chunks(all_chunks)

    print(f"Embeddings shape: {embeddings.shape}")

    qdrant = QdrantManager()

    qdrant.create_collection(collection_name=COLLECTION_NAME, vector_size=embeddings.shape[1])

    qdrant.upload_chunks(
        collection_name=COLLECTION_NAME,
        chunks=all_chunks,
        embeddings=embeddings
    )

    print(
        f"Indexed {len(all_chunks)} chunks "
        f"into '{COLLECTION_NAME}'"
    )


if __name__ == "__main__":
    main()