name = input("what`s your name? ")
print("hi", name)
number_of_book = int(input("how many book do you want? "))
books = []
for i in range(number_of_book):
    book = input("give a book : ")
    books.append(book)

for book in books:
    print("your books :", book)