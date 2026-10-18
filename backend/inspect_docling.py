from pathlib import Path

from app.ingestion.docling_parser import DoclingParser


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = PROJECT_ROOT / "sample_docs" / "test.pdf"


def main():
    parser = DoclingParser()

    result = parser.converter.convert(str(PDF_PATH))
    document = result.document

    print("=== DOCUMENT STRUCTURE ===")
    print("Document type:", type(document))
    print("Document name:", PDF_PATH.name)

    print("\n=== FIRST 10 TEXT ITEMS ===")

    for index, item in enumerate(document.texts[:10]):
        print(f"\nItem {index}")
        print("Type:", type(item).__name__)
        print("Text:", item.text[:300])
        print("Provenance:", getattr(item, "prov", None))


if __name__ == "__main__":
    main()