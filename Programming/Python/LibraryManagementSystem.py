class Book:

    title = str()
    author = str()
    genre = str()
    availability = bool()

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def is_available(self):
        return self.availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            return True
        else:
            return False

    def return_book(self):
        if not self.availability:
            self.availability = True
            return True
        else:
            return False

class Member:

    name = str()
    member_id = int()
    books_borrowed = list()

    def __init__(self,name,member_id):
        self.name = name
        self.member_id = member_id
        self.books_borrowed = []

    def get_name(self):
        return self.name

    def get_member_id(self):
        return self.member_id

    def borrow_book(self,book):
        if book.borrow_book():
            self.books_borrowed.append(book)
            return True
        else:
            return False

    def return_book(self,book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.return_book()
            return True
        else:
            return False

    def get_books_borrowed(self):
        return self.books_borrowed


class Library:
    books = list()
    members = list()

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)

    def add_member(self,member):
        self.members.append(member)

    def remove_member(self,member):
        if member in self.members:
            self.members.remove(member)

    def borrow_book(self, member_id,title):
        for member in self.members:
            if member.get_member_id() == member_id:
                for book in self.books:
                    if book.get_title() == title:
                        if book.borrow_book():
                            member.borrow_book(book)
                            return f"Book '{title}' borrowed by {member.get_name()}.".title()
                        else:
                            return f"Book '{title}' is not available for borrowing.".title()
        return "Member or book not found."

    def return_book(self, member_id, title):
        for member in self.members:
            if member.get_member_id() == member_id:
                for book in member.get_books_borrowed():
                    if book.get_title() == title:
                        member.return_book(book)
                        return f"Book '{title}' returned by {member.get_name()}.".title()
        return "Member or book not found."

class DigitalLibrary(Library):

    def __init__(self):
        super().__init__()

class StudentMember(Member):
    student_id = int()

    def __init__(self,name,member_id,student_id):
        super().__init__(name,member_id)
        self.student_id = student_id

LibSystem = Library()
print("\t\t\t\tLIBRARY MANAGEMENT SYSTEM\t\t\t\t")
print("--------------------------------------------------------")
print("\nCreate Books")

while True:
    title = str(input("\nEnter Title: "))
    author = str(input("Enter Author: "))
    genre = str(input("Enter Genre: "))
    book = Book(title, author, genre)
    LibSystem.add_book(book)
    answer = input("\nAdd another book? (yes/no): ")
    answer = answer.lower()
    if answer == "yes":
        continue
    elif answer == "no":
        break
    else:
        print("Invalid input")
        continue

print("\nCreate Members")
while True:
    name = str(input("\nEnter Name: "))
    member_id = int(input("Enter Member ID: "))
    member = Member(name, member_id)
    LibSystem.add_member(member)
    answer = input("\nAdd another member? (yes/no): ")
    answer = answer.lower()
    if answer == "yes":
        continue
    elif answer == "no":
        break
    else:
        print("Invalid input")
        continue

print("\nMembers Borrow Books")
while True:
    member_id = int(input("\nEnter the member ID of the borrower: "))
    title = str(input("Enter the title of the book to borrow: "))
    print(LibSystem.borrow_book(member_id, title))
    answer = input("\nBorrow another book? (yes/no): ")
    answer = answer.lower()
    if answer == "yes":
        continue
    elif answer == "no":
        break
    else:
        print("Invalid input")
        continue




