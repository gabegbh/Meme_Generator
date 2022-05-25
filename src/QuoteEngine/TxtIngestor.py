from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TxtIngestor(IngestorInterface):
    """
    Ingestor for collecting quotes from Txt files
    Realizes IngestorInterface 
    Parse Method returns a List of QuoteModel objects
    """
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        with open(path, "r") as f:
            quotes = []
        
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split(' - ')
                    quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(quote)
                    
        return quotes