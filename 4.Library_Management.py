
books = []             
issued = {}           
borrow_count = {}      

# Add a new book
def add_book():
    book = input("Enter book name to add: ")
    books.append(book)
    print(" Book added.")

# View all books
def view_books():
    print("\nAvailable Books:")
    if not books:
        print("No books available.")
    else:
        for b in books:
            print("-", b)

# Issue a book
def issue_book():
    name = input("Borrower's name: ")
    book = input("Book to issue: ")
    if book in books:
        books.remove(book)
        issued[name] = book
        borrow_count[book] = borrow_count.get(book, 0) + 1
        print("Book issued to", name)
    else:
        print("Book not available.")

# Return a book
def return_book():
    name = input("Borrower's name: ")
    if name in issued:
        book = issued[name]
        delay = int(input("Days late (0 if on time): "))
        fine = delay * 2  # ₹2 per late day
        print("Book returned:", book)
        if fine > 0:
            print("Late fine: ₹", fine)
        books.append(book)
        del issued[name]
    else:
        print("No book issued under that name.")

# Show most borrowed books
def most_borrowed():
    print("\nMost Borrowed Books:")
    for book, count in borrow_count.items():
        print(f"{book}: {count} times")


def export_log():
    f = open("borrow_log.txt", "w")
    f.write("Borrower Log:\n")
    for name, book in issued.items():
        f.write(f"{name} - {book}\n")
    f.close()
    print("Log saved as 'borrow_log.txt'")

# Menu
def menu():
    while True:
        print("\n=== LIBRARY MENU ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Most Borrowed Books")
        print("6. Export Log")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            most_borrowed()
        elif choice == '6':
            export_log()
        elif choice == '0':
            print("Exiting Library System.")
            break
        else:
            print("Invalid option.")

menu()
