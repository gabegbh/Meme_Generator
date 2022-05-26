from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """
    Ingestor for collecting quotes from PDF files
    Realizes IngestorInterface 
    Parse Method returns a List of QuoteModel objects
    """
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        open(tmp, 'a').close()
        subprocess.call(['pdftotext', path, tmp])
        
        with open(tmp, "r") as f:
            quotes = []
        
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split(' - ')
                    quote = QuoteModel(parsed[0].strip('"'), parsed[1])
                    quotes.append(quote)
                    
        os.remove(tmp)
        return quotes