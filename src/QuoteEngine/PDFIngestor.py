
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor
import random
import subprocess
import os
class PDFIngestor(IngestorInterface):
    allowed_extension = ['pdf']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        
        ext = cls.can_ingest(path)
        if not ext:
            raise Exception(f'File extension {ext} not supported!')
        
        quotes = []
        
        # Convert pdf file to random text file name by 'pdftotext' command 
        file_name = f'{random.randint(0, 100000)}.txt'
        cmd = ['pdftotext', path, file_name]
        subprocess.run(cmd)
        
        # Call TXTIngestor to parse author & body
        try:
            quotes = TXTIngestor.parse(file_name)
        finally:
            os.remove(file_name)
            return quotes
            
        