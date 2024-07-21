class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name): 
        self.books.append(book_name)
        print(f'Book "{book_name}" has been added.')

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'Book "{book_name}" has been removed.')
        else:
            print(f'Book "{book_name}" not found in the library.')

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f'- {book}')
    
    def search_books(self,book_name):
        if not self.books:
            print("Not Found")
        else:
            print(f"'{book_name}'is presemt in liabrary")
    """def search_book(self,book_name):
        results = []
        for book_name in self.books:
            if book_name and book_name.lower() in book_name.lower():
                results.append(book_name)"""
          
    #return results

def show_menu():
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. List all books")
    print("4.Search a Book")
    print("5. Exit")

def main():
    library = Library()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == '2':
            book_name = input("Enter the name of the book to remove: ")
            library.remove_book(book_name)
        elif choice == '3':
            library.list_books()
        elif choice == '4':
            library.search_book()
        elif choice == '5':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

