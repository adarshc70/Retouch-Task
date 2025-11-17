library = {}  

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    year = input("Enter publication year: ").strip()
    library[title] = {"author": author, "year": year}
    print(f"Book '{title}' added!\n")


def remove_book():
    title = input("Enter book title to remove: ").strip()
    if title in library:
        del library[title]
        print(f"Book '{title}' removed!\n")
    else:
        print("Book not found.\n")


def search_book():
    title = input("Enter book title to search: ").strip()
    if title in library:
        print(f"Title: {title}")
        print(f"Author: {library[title]['author']}")
        print(f"Year: {library[title]['year']}\n")
    else:
        print("Book not found.\n")

def display_books():
    if not library:
        print("Library is empty.\n")
        return
    print("\nLibrary Books:")
    for title, info in library.items():
        print(f"Title: {title}, Author: {info['author']}, Year: {info['year']}")
    print()

while True:
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")