class Book:
    def __init__(self):
        # Constructor to initialize the list of pages
        self.pages = []

    def add_page(self, page):
        # Method to add a new page to the book
        self.pages.append(page)
        print(f"Page added: {page}")

    def show(self):
        # Method to show all the pages of the book
        print("All pages in the book:")
        for i, page in enumerate(self.pages, start=1):
            print(f"Page {i}: {page}")


# Example usage:
my_book = Book()  # Create a Book object

# Add pages to the book
my_book.add_page("Once upon a time...")
my_book.add_page("They lived happily ever after.")
my_book.add_page("The End.")

# Show all pages
my_book.show()
