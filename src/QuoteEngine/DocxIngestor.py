
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    allowed_extension = ['docx']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        
        ext = cls.can_ingest(path)
        if not ext:
            raise Exception(f'File extension {ext} not supported!')
        
        quotes = []
        return quotes