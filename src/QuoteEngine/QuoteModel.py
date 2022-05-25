class QuoteModel():
    """A class to represent a quote with a body and author
    
    :params 
        body: string of the contents of the quote
        author: string of author name 
    """
    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author
    
    def __repr__(self):
        return f"<'{self.body}' - {self.author}>"
