from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    Ingestor for collecting quotes from Docx files
    Realizes IngestorInterface
    Parse Method returns a List of QuoteModel objects
    """
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != '':
                parsed = para.text.split(' - ')
                quote = QuoteModel(parsed[0].strip('"'), parsed[1])
                quotes.append(quote)
        return quotes
