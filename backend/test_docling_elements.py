from pathlib import Path

from app.ingestion.docling_parser import DoclingParser


PROJECT_ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = PROJECT_ROOT / "sample_docs" / "test.pdf"


def main():
    parser = DoclingParser()
    elements = parser.parse_elements(str(PDF_PATH))

    print(f"Extracted {len(elements)} elements")

    for element in elements[:10]:
        print("\nText:", element["text"][:200])
        print("Section:", element["section"])
        print("Pages:", element["page_numbers"])
        print("Label:", element["label"])


if __name__ == "__main__":
    main()