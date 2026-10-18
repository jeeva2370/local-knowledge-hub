from pathlib import Path

from docling.datamodel.accelerator_options import (
    AcceleratorDevice,
    AcceleratorOptions,
)
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption


class DoclingParser:
    def __init__(self):
        pipeline_options = PdfPipelineOptions()

        pipeline_options.accelerator_options = AcceleratorOptions(
            device=AcceleratorDevice.CUDA
        )

        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pipeline_options
                )
            }
        )

    def parse(self, file_path: str) -> dict:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Document not found: {path}")

        if path.suffix.lower() != ".pdf":
            raise ValueError("Only PDF files are supported currently.")

        result = self.converter.convert(str(path))
        document = result.document

        return {
            "document_name": path.name,
            "text": document.export_to_markdown(),
        }

    def parse_elements(self,file_path:str)->list[dict]:
        from pathlib import Path

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Document not found: {path}")

        if path.suffix.lower() != ".pdf":
            raise ValueError("Only PDF files are supported currently.")

        result = self.converter.convert(str(path))
        document = result.document

        elements = []
        current_section = "Uncategorized"

        for item in document.texts:
            text = item.text.strip()

            if not text:
                continue

            if item.label == "section_header":
                current_section = text

            page_numbers = sorted({
                provenance.page_no
                for provenance in item.prov
            })

            elements.append({
                "text":text,
                "section":current_section,
                "page_numbers":page_numbers,
                "label":str(item.label),
            })
        return elements