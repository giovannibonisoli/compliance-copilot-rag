from parser import load_pdf


def main():

    pages = load_pdf(
        "data/raw/GDPR.pdf"
    )

    print(
        f"Pages extracted: {len(pages)}"
    )

    print()

    print(
        f"Source: {pages[0]['source']}"
    )

    print(
        f"Page: {pages[0]['page_number']}"
    )

    print()

    print(
        pages[0]["text"][:1000]
    )


if __name__ == "__main__":
    main()