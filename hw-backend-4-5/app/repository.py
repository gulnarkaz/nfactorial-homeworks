class BooksRepository:
    def __init__(self):
        self.books = [
            {
                "id": 1,
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "year": 1960,
                "total_pages": 336,
                "genre": "Fiction",
            },
            {
                "id": 2,
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "total_pages": 328,
                "genre": "Dystopian",
            },
            {
                "id": 3,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925,
                "total_pages": 180,
                "genre": "Classic",
            },
            {
                "id": 4,
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "year": 1954,
                "total_pages": 1178,
                "genre": "Fantasy",
            },
            {
                "id": 5,
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "year": 1951,
                "total_pages": 224,
                "genre": "Coming-of-age",
            },

        ]

    def get_all(self):
        return self.books

    def get_one(self, id):
        for book in self.books:
            if book["id"] == id:
                return book 
        return None
    def save(self, book):
        if "id" in book and book["id"] is not None:
            existing_book = self.get_one(book["id"])
            if existing_book:
                existing_book.update(book)
                return book
            
        
        if self.books:
            new_id = max([b["id"] for b in self.books], default=0) + 1
        else:
            new_id = 1
        book["id"] = new_id
        self.books.append(book)
        return book
    def delete(self, id: int):
        book = self.get_one(id)
        if book:
            self.books.remove(book)
        
