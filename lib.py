import json
FILE = "library.json"
# load books
def load_books():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
# save books
def save_books(books):
    with open(FILE, "w") as f:
        json.dump(books, f)
# add book
def add_book():
    books = load_books()

    title = input("Enter book title: ")
    author = input("Enter author: ")

    book = {
        "title": title,
        "author": author,
        "issued": False
    }

    books.append(book)
    save_books(books)

    print("Book added successfully\n")

# view books
def view_books():
    books = load_books()

    if not books:
        print("No books available\n")
        return

    for i, book in enumerate(books):
        status = "Issued" if book["issued"] else "Available"
        print(i+1, book["title"], "-", book["author"], "-", status)

    print()

# search book
def search_book():
    books = load_books()
    name = input("Enter book name: ")

    for book in books:
        if name.lower() in book["title"].lower():
            print(book["title"], "-", book["author"])

# issue book
def issue_book():
    books = load_books()

    view_books()
    n = int(input("Enter book number to issue: "))

    if books[n-1]["issued"]:
        print("Book already issued\n")
    else:
        books[n-1]["issued"] = True
        save_books(books)
        print("Book issued\n")

# return book
def return_book():
    books = load_books()

    view_books()
    n = int(input("Enter book number to return: "))

    books[n-1]["issued"] = False
    save_books(books)

    print("Book returned\n")

# delete book
def delete_book():
    books = load_books()

    view_books()
    n = int(input("Enter book number to delete: "))

    books.pop(n-1)
    save_books(books)

    print("Book deleted\n")

# main menu
while True:
    print("====== Library Management System ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        break
    else:
        print("Invalid choice\n")

