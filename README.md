# Local Knowledge Hub

A local-first, AI-powered knowledge base that helps developers and users
find answers in technical documentation.

The project aims to combine structured document processing, embeddings,
hybrid retrieval, and local LLM inference to provide grounded answers
with source citations.

## Planned Features

- Ingest documents using Docling.
- Extract structured content and document metadata.
- Generate embeddings and store searchable document chunks.
- Detect unchanged documents to avoid unnecessary re-indexing.
- Replace existing chunks when a document is updated.
- Support semantic and keyword-based retrieval.
- Generate answers grounded in retrieved documentation.
- Provide source citations, including page numbers where available.
- Run the generation model locally.
- Evaluate retrieval accuracy and response latency.

## Planned Technology Stack

| Component | Technology |
|---|---|
| Language | Python |
| Document processing | Docling |
| Embeddings | EmbeddingGemma |
| Database | PostgreSQL |
| Vector search | pgvector |
| Keyword search | PostgreSQL full-text search |
| LLM inference | Ollama |
| Backend API | FastAPI |
| Initial UI | Streamlit |
| Testing | pytest |

The technology choices will be validated through implementation and
benchmarking.

## Development Status

The repository has been initialized. Core functionality is under
development.

## Project Goals

1. Reliable document ingestion.
2. Safe document updates without duplicate or obsolete chunks.
3. Fast and accurate retrieval from technical documentation.
4. Grounded answers with traceable citations.
5. Local-first operation and efficient resource usage.
6. Reproducible evaluation and automated tests.

## Security and Privacy

Do not commit confidential documents, credentials, environment files,
or generated databases. Use synthetic or redistributable documents for
examples and tests.

## License

A license has not yet been selected.
