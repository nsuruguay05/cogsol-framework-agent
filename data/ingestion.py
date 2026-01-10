from cogsol.content import BaseIngestionConfig, PDFParsingMode, ChunkingMode

class CogsolFrameworkIngestionConfig(BaseIngestionConfig):
    """ingestion configuration for documents."""

    name = "cogsol_framework_ingestion"
    pdf_parsing_mode = PDFParsingMode.MANUAL
    chunking_mode = ChunkingMode.AGENTIC_SPLITTER
    max_size_block = 1500
    chunk_overlap = 0
    separators = []
    ocr = False
    additional_prompt_instructions = ""
    assign_paths_as_metadata = False
