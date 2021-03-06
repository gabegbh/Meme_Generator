from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """
    Ingestor Abstract Base Class providing the
    structure for all ingestors to be able to test
    ingestability and then parse files of many types
    """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Boolean checker method to determine with
        filetypes to accept in each child class
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse skeleton class to enforce a parse
        implementation in all child classes
        """
        pass
        