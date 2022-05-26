from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor




class Ingestor(IngestorInterface):
    """
    Ingestor for collecting quotes from many file extensions
    Realizes IngestorInterface
    Parse Method returns a List of QuoteModel objects if file is 
    ingestable by one of the ingestor classes
    """
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        return None
