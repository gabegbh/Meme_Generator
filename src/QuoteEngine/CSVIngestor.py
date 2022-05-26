from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """
    Ingestor for collecting quotes from CSV files
    Realizes IngestorInterface
    Parse Method returns a List of QuoteModel objects
    """
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest extension')

        quotes = []
        df = pd.read_csv(path, header=0)

        for __, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
            