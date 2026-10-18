from pathlib import Path

from app.ingestion.docling_parser import DoclingParser

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = PROJECT_ROOT / "sample_docs" / "test.pdf"


def main():
    print(f"PDF path: {PDF_PATH}")
    print(f"File exists: {PDF_PATH.exists()}")

    parser = DoclingParser()
    result = parser.parse(str(PDF_PATH))

    print(f"\nDocument: {result['document_name']}")
    print("\n=== EXTRACTED CONTENT ===\n")
    print(result["text"][:5000])


if __name__ == "__main__":
    main()