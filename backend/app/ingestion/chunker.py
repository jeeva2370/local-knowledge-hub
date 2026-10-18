import re


def chunk_text(text:str,
               document_name:str,
               page_number:int,
               section:str | None = None,
               chunk_size:int = 250,
               overlap:int = 40) ->list[dict]:
    """
    Split extracted text into overlapping word-based chunks.

    Each chunk return its document,page and section metadata.
    :param text:
    :param document_name:
    :param page_number:
    :param section:
    :param chunk_size:
    :param overlap:
    :return:
    """

    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater then zero")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")
    words = re.sub(r"\s+"," ",text).strip().split()

    if not words:
        return []

    chunks = []
    start = 0
    chunk_index = 0

    while start < len(words):
        end = min(start + chunk_size,len(words))

        chunks.append({
            "id":f"{document_name}:P{page_number}:c{chunk_index}",
            "text":" ".join(words[start:end]),
            "metadata":{
                "source":document_name,
                "page_number":page_number,
                "section":section or "unknown",
                "chunk_index":chunk_index
            }
        })

        if end == len(words):
            break
        start = end - overlap
        chunk_index += 1

    return chunks