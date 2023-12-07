
from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel

import pandas
class CSVIngestor(IngestorInterface):
    allowed_extension = ['csv']
    
    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        
        ext = cls.can_ingest(path)
        if not ext:
            raise Exception(f'File extension {ext} not supported!')
        
        quotes = []
        
        # Read CSV file & parse author and body
        df = pandas.read_csv(path)
        for _, row in df.iterrows():
            quote = QuoteModel(row['author'], row['body'])
            quotes.append(quote)
        return quotes