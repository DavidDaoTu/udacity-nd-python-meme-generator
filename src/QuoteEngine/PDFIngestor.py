
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    allowed_extension = ['pdf']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        
        ext = cls.can_ingest(path)
        if not ext:
            raise Exception(f'File extension {ext} not supported!')
        
        quotes = []
        return quotes