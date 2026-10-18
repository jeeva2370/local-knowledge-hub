from app.ingestion.chunker import chunk_text


def main():
    text = (
        "Employees can reset their password from Account Settings. "
        "If they cannot access their account, they should contact IT. "
        "Employees should contact HR for questions about benefits."
    )

    chunks = chunk_text(
        text=text,
        document_name="employee_guide.pdf",
        page_number=3,
        section="Account Management",
        chunk_size=15,
        overlap=3,
    )

    for chunk in chunks:
        print(f"\nID: {chunk['id']}")
        print(f"Text: {chunk['text']}")
        print(f"Metadata: {chunk['metadata']}")


if __name__ == "__main__":
    main()