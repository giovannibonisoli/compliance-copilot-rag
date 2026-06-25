from pathlib import Path
from typing import TypedDict

from pypdf import PdfReader


class Page(TypedDict):
    page_number: int
    source: str
    text: str


def load_pdf(pdf_path: str) -> list[Page]:
    """
    Load a PDF and extract text page by page.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of pages with metadata.
    """

    path = Path(pdf_path)

    reader = PdfReader(path)

    pages: list[Page] = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if not text:
            continue

        pages.append(
            {
                "page_number": page_number,
                "source": path.stem,
                "text": text.strip()
            }
        )

    return pages