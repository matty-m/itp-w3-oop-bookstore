class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.store = []
    
    def add_book(self, book):
        self.store.append(book)
    
    def get_books(self):
        return self.store
    
    def search_books(self, title=None, author=None):
        results = []
        for list_element in self.store:
            if author is None:
                if title.lower() in list_element.title.lower():
                    results.append(list_element)
            elif title is None:
                 if author.name.lower() in list_element.author.name.lower():
                    results.append(list_element)   
        return results
        

class Author(object):
    
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []

    def get_books(self):
        return self.books
 
        
class Book(object):
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
        
    
    
    


