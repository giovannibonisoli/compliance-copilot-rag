from typing import TypedDict


class Chunk(TypedDict):
    chunk_id: int
    source: str
    page_number: int
    text: str


def chunk_text(
    text: str,
    source: str,
    page_number: int,
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[Chunk]:

    if chunk_size <= 0:
        raise ValueError(
            "chunk_size must be greater than 0"
        )

    if overlap < 0:
        raise ValueError(
            "overlap must be >= 0"
        )

    if overlap >= chunk_size:
        raise ValueError(
            "overlap must be smaller than chunk_size"
        )

    chunks: list[Chunk] = []

    start = 0
    local_chunk_id = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            {
                "chunk_id": local_chunk_id,
                "source": source,
                "page_number": page_number,
                "text": text[start:end]
            }
        )

        local_chunk_id += 1
        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    with open("test.txt", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)

    print(f"Numero chunk: {len(chunks)}")
    print(chunks[0])