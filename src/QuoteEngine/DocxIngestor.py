
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

from docx import Document
class DocxIngestor(IngestorInterface):
    allowed_extension = ['docx']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        
        ext = cls.can_ingest(path)
        if not ext:
            raise Exception(f'File extension {ext} not supported!')
        
        quotes = []
        
        # Open docx file & parse author and body
        doc = Document(path)
        for paragraph in doc.paragraphs:
            line = paragraph.text.strip().strip('\r\n')
            if line != "":
                splited = line.split(' - ')
                quote = QuoteModel(splited[1], splited[0])
                quotes.append(quote)
        return quotes