from src.retriever import Retriever


def main():

    retriever = Retriever()

    results = retriever.search("What are high-risk AI systems?")

    print()

    for i, result in enumerate(
        results,
        start=1
    ):

        payload = result.payload

        print("=" * 80)

        print(f"Result #{i}")

        print(f"Source: {payload['source']}")

        print(f"Page: {payload['page_number']}")

        print()

        print(payload["text"][:500])

        print()

    print("=" * 80)


if __name__ == "__main__":
    main()