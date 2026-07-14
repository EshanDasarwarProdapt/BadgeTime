"""Problem Statement:

You are tasked with designing a Library Management System for a small community library. The system should manage books, library members, and borrowing/returning of books.

Requirements:
1. Book Management:
Each book has a title, author, ISBN number, and availability status (available/borrowed).
You should be able to add new books, view book details, and update availability when a book is borrowed or returned.
2. Member Management:
Each library member has a name, unique member ID, and a list of borrowed books.
Members can borrow a book if it is available.
Members can return books they borrowed.
3. System Features:
Keep track of which member has borrowed which books.
Limit each member to borrow a maximum of 3 books at a time.
Display all books and their current availability."""

class Library:
    def __init__(self):
        self.books = []  # List to store all books
        self.members = []  # List to store all members

    def add_book(self, title, author, isbn):
        book = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }
        self.books.append(book)

    def view_books(self):
        for book in self.books:
            status = "Available" if book['available'] else "Borrowed"
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Status: {status}")

    def add_member(self, name, member_id):
        member = {
            'name': name,
            'member_id': member_id,
            'borrowed_books': []
        }
        self.members.append(member)

    def borrow_book(self, member_id, isbn):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        book = next((b for b in self.books if b['isbn'] == isbn), None)

        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return
        if not book['available']:
            print("Book is currently borrowed.")
            return
        if len(member['borrowed_books']) >= 3:
            print("Member has already borrowed the maximum number of books.")
            return

        book['available'] = False
        member['borrowed_books'].append(book)
        print(f"{member['name']} has borrowed '{book['title']}'.")

    def return_book(self, member_id, isbn):
        member = next((m for m in self.members if m['member_id'] == member_id), None)
        book = next((b for b in self.books if b['isbn'] == isbn), None)

        if not member:
            print("Member not found.")
            return
        if not book:
            print("Book not found.")
            return
        if book not in member['borrowed_books']:
            print("This book was not borrowed by the member.")
            return

        book['available'] = True
        member['borrowed_books'].remove(book)
        print(f"{member['name']} has returned '{book['title']}'.")

    
a = Library()
# b = Library()

a.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
a.add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
a.add_book("1984", "George Orwell", "9780451524935")

a.view_books()

a.add_member("Alice", "M001")
a.add_member("Bob", "M002")

a.borrow_book("M001", "9780743273565")  # Alice borrows The Great Gatsby



