from src.chunker import chunk_text


def main():

    text = "A" * 5000

    chunks = chunk_text(
        text=text,
        chunk_size=1000,
        overlap=200
    )

    print(f"Chunks generated: {len(chunks)}")

    for chunk in chunks[:3]:
        print(
            f"ID: {chunk['chunk_id']} "
            f"Length: {len(chunk['text'])}"
        )


if __name__ == "__main__":
    main()