import json


def asking_books(books):

    number_of_book = int(input("how many book do you want? "))

    for i in range(number_of_book):
        book = input("give a book : ")
        books.append(book)

    for book in books:
        print("your books :", book)

def save_books_info(book):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(book, file, ensure_ascii=False, indent=2)

def load_book_info():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []