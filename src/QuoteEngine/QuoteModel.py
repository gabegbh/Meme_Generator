class QuoteModel():
    """A class to represent a quote with a body and author

    :params
        body: string of the contents of the quote
        author: string of author name
    """
    def __init__(self, body: str, author: str):
        if type(body) == str and type(author) == str:
            self.body = body
            self.author = author
        else:
            error = f"""body and author of a QuoteModel must be of\
             type 'str', ({type(body)}, {type(author)}) not accepted"""
            raise TypeError(error)

    def __repr__(self):
        return f"<'{self.body}' - {self.author}>"
