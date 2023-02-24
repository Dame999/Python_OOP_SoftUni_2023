from project_library.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        for authors, books in self.books_available.items():
            for book in books:
                if book == book_name:
                    user.books.append(book_name)
                    self.books_available[authors].remove(book)

                    if user.username not in self.rented_books.keys():
                        self.rented_books[user.username] = {}
                    self.rented_books[user.username][book_name] = days_to_return

                    return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, data in self.rented_books.items():
            for book, return_days in data.items():
                if book == book_name:
                    return f'The book "{book_name}" is already rented and will be ' \
                           f'available in {return_days} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            if author not in self.books_available.keys():
                self.books_available[author] = []
            self.books_available[author].append(book_name)
            user.books.remove(book_name)
            del self.rented_books[user.username][book_name]
        else:
            return f"{user.username} doesn't have this book in his/her records!"

