from books import asking_books, save_books_info, load_book_info

name = input("what`s your name? ")
print("hi", name)

books = []
load_books = load_book_info()

asking_books(load_books)
save_books_info(load_books)