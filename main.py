from books import asking_books, save_books_info, load_book_info
from dotenv import load_dotenv
import os


load_dotenv()


name = input("what`s your name? ")
print("hi", name)

admin_mode = input("do you want active admin mode? yes/no ")
if admin_mode == "yes":
    admin_pass = input("please enter admin mode password : ")
    if admin_pass == os.getenv("BOOK_MANAGER_ADMIN_PASSWORD"):
        print("admin mode active!")
    else:
        print("wrong!!")

books = []
load_books = load_book_info()

asking_books(load_books)
save_books_info(load_books)