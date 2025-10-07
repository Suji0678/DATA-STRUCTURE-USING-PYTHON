class BookStack:
    def __init__(self, max_size):
        self.stack = [] 
        self.top = -1 
        self.max_size = max_size 
    def push(self, book_title):
        if self.top >= self.max_size - 1:
            print("Stack Overflow! Cannot add more books.")
        else:
            self.stack.append(book_title)
            self.top += 1
            print(f'"{book_title}" added to the stack.')
    def pop(self):
        if self.top == -1:
            print("Stack Underflow! No books to remove.")
        else:
            removed_book = self.stack.pop()
            self.top -= 1
            print(f'"{removed_book}" removed from the stack.')
    def peek(self):
        if self.top == -1:
            print("Stack is empty. No books to display.")
        else:
            print(f'Top book in stack: "{self.stack[self.top]}"')
    def display(self):
        if self.top == -1:
            print("Stack is empty.")
        else:
            print("Books in the stack (Top to Bottom):")
            for i in range(self.top, -1, -1):
                print(f' {self.stack[i]}')
if __name__ == "__main__":
    max_books = int(input("Enter maximum number of books the stack can hold: "))
    book_stack = BookStack(max_books)

    while True:
        print("\n--- Stack Operations ---")
        print("1. Push (Add Book)")
        print("2. Pop (Remove Book)")
        print("3. Peek (View Top Book)")
        print("4. Display Stack")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            book = input("Enter book title to add: ")
            book_stack.push(book)
        elif choice == '2':
            book_stack.pop()
        elif choice == '3':
            book_stack.peek()
        elif choice == '4':
            book_stack.display()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
