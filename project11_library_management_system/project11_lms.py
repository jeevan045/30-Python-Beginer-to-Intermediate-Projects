class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def mark_borrowed(self):
        self.available = False

    def mark_returned(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.borrow_count = 0   # track total borrow count

    def borrow_book(self, book):
        if book.available:
            book.mark_borrowed()
            self.borrowed_books.append(book)
            self.borrow_count += 1
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")


class Librarian(Member):
    def add_book(self, library, book):
        library.books.append(book)
        print(f"Librarian {self.name} added '{book.title}'.")

    def remove_book(self, library, book):
        if book in library.books:
            library.books.remove(book)
            print(f"Librarian {self.name} removed '{book.title}'.")
        else:
            print(f"'{book.title}' not found in library.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered with ID {member.member_id}.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Catalog:")
            for book in self.books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def list_due_books(self):
        print("\nBooks currently borrowed (due to be returned):")
        found = False
        for member in self.members:
            if member.borrowed_books:
                found = True
                print(f"\n{member.name} (ID: {member.member_id}) has borrowed:")
                for book in member.borrowed_books:
                    print(f"  - {book.title} by {book.author}")
        if not found:
            print("No books are due. All books are returned.")


def main():
    library = Library()
    librarian = Librarian("Alice", "L001")

    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Due Books")
        print("7. Member Borrow Stats")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            librarian.add_book(library, book)

        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.register_member(member)

        elif choice == "3":
            member_id = input("Enter your Member ID: ")
            member = library.find_member(member_id)
            if member:
                title = input("Enter book title to borrow: ")
                book = library.find_book(title)
                if book:
                    member.borrow_book(book)
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif choice == "4":
            member_id = input("Enter your Member ID: ")
            member = library.find_member(member_id)
            if member:
                title = input("Enter book title to return: ")
                book = library.find_book(title)
                if book:
                    member.return_book(book)
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            library.list_due_books()

        elif choice == "7":
            member_id = input("Enter Member ID: ")
            member = library.find_member(member_id)
            if member:
                print(f"{member.name} has borrowed {member.borrow_count} times in total.")
                if member.borrowed_books:
                    print("Currently borrowed books:")
                    for book in member.borrowed_books:
                        print(f"  - {book.title}")
                else:
                    print("No books currently borrowed.")
            else:
                print("Member not found.")

        elif choice == "8":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
