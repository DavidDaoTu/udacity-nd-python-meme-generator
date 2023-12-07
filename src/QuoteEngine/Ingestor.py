""" Ingestor class that realizes the IngesterInterface abstract base class
and encapsulates your helper classes. It should implement logic to select the 
appropriate helper for a given file, based on filetype
"""
from typing import List
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor

from .IngestorInterface import IngestorInterface

class Ingestor(IngestorInterface):
    importers = [TXTIngestor, CSVIngestor, DocxIngestor, PDFIngestor]
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
        raise Exception(f'Not found any proper importer for file: {path}')
            
    