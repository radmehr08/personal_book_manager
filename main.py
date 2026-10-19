from books import asking_books, save_books_info, load_book_info

name = input("what`s your name? ")
print("hi", name)

admin_mode = input("do you want active admin mode? yes/no ")
if admin_mode == "yes":
    admin_pass = input("please enter admin mode password : ")


books = []
load_books = load_book_info()

asking_books(load_books)
save_books_info(load_books)