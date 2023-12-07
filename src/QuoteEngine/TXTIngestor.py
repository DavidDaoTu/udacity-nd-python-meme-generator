
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """Text Ingestor class."""
    allowed_extension = ['txt']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        """Returns a list of QuoteModel."""
        ext = cls.can_ingest(path)
        if not ext:
            raise Exception(f'File extension {ext} not supported!')
        quotes = []
        
        # Open text file & parse author and body
        with open(path, 'r', encoding='utf-8-sig') as file:
            for line in file.readlines():
                line = line.strip('\r\n').strip()   # cleaning the line
                if not len(line):
                    continue
                splited = line.split(' - ')
                quote = QuoteModel(splited[1], splited[0])
                quotes.append(quote)
            
        return quotes