""" 
QuoteModel class to encapsulate the body & author.
"""

class QuoteModel:
    def __init__(self, author:str, body:str):
        self.author = author
        self.body = body
    
    def __str__(self) -> str:
        return f'{self.author}: {self.body}'
    
    def __repr__(self) -> str:
        return f'<{self.author}: {self.body}>'
    
    