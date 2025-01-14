class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self.next_book = None

class Library:
    def __init__(self):
        self.head = None

    def add_book(self, title, author, genre, book_id):
        new_book = Book(title, author, genre, book_id)
        
        if self.head is None:
            self.head = new_book
        else:
            current = self.head
            while current.next_book:
                current = current.next_book
            current.next_book = new_book

    def search_books(self, keyword):
        results = []
        current = self.head
        while current:
            if keyword.lower() in current.title.lower() or keyword.lower() in current.author.lower():
                results.append(f"{current.title} by {current.author}")
            current = current.next_book
            return results
            
    def recommend_books(self, genre):
        recommendatiion = []
        current = self.head
        while current:
            if current.genre.lower() == genre.lower():
                recommendatiion.append(f"{current.title} by {current.author}")
            current = current.next_book
        return recommendatiion
        
    def display_books(self):
        current = self.head
        while current:
            print(f"Title: {current.title}, Author: {current.author}, Genre: {current.genre}, ID: {current.book_id}")
            current = current.next_book


if __name__ == "__main__":
    library = Library()
    library.add_book("Nexus", "Yuval Noah Harari", "History", 1)
    library.add_book("1984", "George Orwell", "Dystopian", 2)
    library.add_book("Harry Potter", "JK Rolling", "Fiction", 3)

    print("All books in the library")
    library.display_books()

    print("\nSearch results for 'Yuval': ")
    search_results = library.search_books("Yuval")
    for result in search_results:
        print(result)

    print("\nRecommended books in 'Fiction' genre: ")
    recommendations = library.recommend_books("Fiction")
    for book in recommendations:
        print(book)