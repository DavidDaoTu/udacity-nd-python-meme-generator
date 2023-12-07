""" 
QuoteModel class to encapsulate the body & author.
"""

class QuoteModel:
    def __init__(self, author:str, body:str):
        self.author = author.strip('""')
        self.body = body if '"' in body else f'"{body}"'
    
    def __str__(self) -> str:
        return f'{self.body} - {self.author}'
    
    def __repr__(self) -> str:
        return f'{self.body} - {self.author}'
    
    