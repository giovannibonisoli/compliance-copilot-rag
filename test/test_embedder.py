from chunker import chunk_text
from embedder import Embedder


def main():

    text = """
    Artificial Intelligence systems can be classified
    according to different levels of risk.
    """ * 100

    chunks = chunk_text(text)

    embedder = Embedder()

    embeddings = embedder.embed_chunks(
        chunks
    )

    print(
        f"Embeddings shape: "
        f"{embeddings.shape}"
    )

    query_embedding = embedder.embed_query(
        "What are high-risk AI systems?"
    )

    print(
        f"Query shape: "
        f"{query_embedding.shape}"
    )


if __name__ == "__main__":
    main()