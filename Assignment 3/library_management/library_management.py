# This program manages a simple library system using OPP and file handling.

class Book:
    def __init__(self, title, author, status="Avilable"):
        self.title = title
        self.author = author
        self.status = status

    def to_line(self):
        return f"{self.title},{self.author},{self.status}\n"
    
class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename

    def add_book(self, book):
        with open(self.filename, "a") as file:
            file.write(book.to_line())

    def display_books(self):
        try:
            with open(self.filename, "r") as file:
                print("Title\tAuthor\tStatus")
                for line in file:
                    print("\t".join(line.strip().split(",")))
        except FileNotFoundError:
            print("No books available.")

    def search_book(self, title):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    if title.lower() in line.lower():
                        print("Found:", line.strip())
                        return
                    print("Book not found.")
        except FileNotFoundError:
            print("File not found.")

    def update_status(self, title, new_status):
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            with open(self.filename, "w") as file:
                found = False
                for line in lines:
                    parts = line.strip().split(",")
                    if parts[0].lower() == title.lower():
                        parts[2] = new_status
                        found = True
                    file.write(",".join(parts) + "\n")
            if found:
                print("Book status updated.")
            else:
                print("Book not found.")
        except FileNotFoundError:
            print("File not found.")

library = Library()
while True:
    print("\n1. Add Book\n2. View Books\n3. Search Book\n4. Issue Book\n5. Return Book\n6. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        title = input("Title: ")
        author = input("Author: ")
        library.add_book(Book(title, author))
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        title = input("Enter title to search: ")
        library.search_book(title)
    elif choice == '4':
        title = input("Enter title to issue: ")
        library.update_status(title, "Issued")
    elif choice == '5':
        title = input("Enter title to return: ")
        library.update_status(title, "Available")
    elif choice == '6':
        break
    else:
        print("Invalid choice.")